import re
from typing import List, Optional, Union

import pandas as pd
from pydantic import BaseModel, root_validator, validator

from .bounds import max_values, min_values
from .instrument import Instrument
from .instrumentitem import InstrumentItem
from .instrumentmetadatatype import InstrumentMetadataType
from .trial import Trial
from .valuetype import ValueType


class Column(BaseModel):
    column_name: str
    column_values: Optional[Union[None, List[int], pd.Series, pd.DataFrame]] = None
    min_value: Optional[int]
    max_value: Optional[int]
    instrument: Optional[Instrument]
    instrument_item: Optional[InstrumentItem]
    instrument_metadata_type: Optional[InstrumentMetadataType]
    trial: Optional[Trial]
    value_type: Optional[ValueType]

    class Config:
        arbitrary_types_allowed = True
        validate_assignment = True

    @root_validator
    def validate_column_name(cls, values):
        """Get the class and class values, validate the column_name, and generate the derived fields"""
        COLUMN_TITLE_REGEX = r"^(cvlt|cvltc|ravlt|hvlt)_([a-z_0-9])+$"

        column_name = values.get("column_name")

        if values.get("column_values") is None:
            values["column_values"] = pd.DataFrame({column_name: []})

        if not re.match(COLUMN_TITLE_REGEX, column_name):
            raise ValueError(
                "Invalid 'column_name' format. It should match the pattern: ^(cvlt|cvltc|ravlt|hvlt)_([a-z_])+$"
            )

        if not values["min_value"]:
            values["min_value"] = min_values.get(column_name, 0)

        if not values["max_value"]:
            values["max_value"] = max_values.get(column_name, None)

        # The below is already a little more complicated than what might be readily maintainable, though the alternative
        # would be a full tokenizer of some sort, or a more verbose and explicit format.  Neither of which are simple.
        values["column_name_components"] = column_name.split("_")

        if 5 < len(values["column_name_components"]) < 1:
            raise ValueError(
                "Invalid 'column_name' format. It should match the pattern: ^(cvlt|cvltc|ravlt|hvlt)_([a-z_])+$"
            )

        if len(values["column_name_components"]) == 2:
            values["instrument"] = Instrument(id=values["column_name_components"][0])
            values["instrument_metadata_type"] = InstrumentMetadataType(
                id=values["column_name_components"][1]
            )
            return values

        if len(values["column_name_components"]) == 3:
            values["instrument"] = Instrument(id=values["column_name_components"][0])
            values["instrument_item"] = InstrumentItem(
                id=values["column_name_components"][1]
            )
            values["value_type"] = ValueType(id=values["column_name_components"][2])
            return values

        if len(values["column_name_components"]) == 4:
            values["instrument"] = Instrument(id=values["column_name_components"][0])
            values["instrument_item"] = InstrumentItem(
                id=values["column_name_components"][1]
            )
            values["trial"] = Trial(id=values["column_name_components"][2])
            values["value_type"] = ValueType(id=values["column_name_components"][3])
            return values

        return values

    @validator("column_values")
    def convert_to_dataframe_or_default(cls, value, values):
        if isinstance(value, pd.DataFrame) or isinstance(value, pd.Series):
            if isinstance(value, pd.Series):
                value = value.to_frame()

            if value.shape[1] != 1:
                raise ValueError(
                    "Invalid column_values. Expected a single column dataframe."
                )
            if values["column_name"] != value.columns[0]:
                raise ValueError(
                    "Invalid column_values. Expected column name to match column_name."
                )
            if not value.iloc[:, 0].apply(lambda x: isinstance(x, (int, float))).all():
                raise ValueError(
                    "Invalid column_values. Expected a single column dataframe of numeric values."
                )
            # check that the index of the first int or float is 0, and no NaNs have an index of 0 skipping the column name
            if (
                value.iloc[:, 0].apply(lambda x: isinstance(x, (int, float))).idxmax()
                != 0
            ):
                raise ValueError(
                    "Invalid column_values. Expected a single column dataframe with no NaNs above the first numeric value."
                )
            return value

        elif isinstance(value, list):
            for v in value:
                if not isinstance(v, (int, float)):
                    raise ValueError(
                        "Invalid column_values. Expected a list of numeric values."
                    )
            return pd.DataFrame({values["column_name"]: value})

        else:
            return pd.DataFrame({values["column_name"]: []})
