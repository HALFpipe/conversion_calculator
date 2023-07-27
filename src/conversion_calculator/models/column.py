import re
from typing import List, Optional, Union

import pandas as pd
from pydantic import BaseModel, root_validator, validator

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

    @root_validator
    def validate_column_name(cls, values):
        """Get the class and class values, validate the column_name, and generate the derived fields"""
        COLUMN_TITLE_REGEX = r"^(cvlt|cvltc|ravlt|hvlt)_([a-z_0-9])+$"

        column_name = values.get("column_name")

        if values.get("column_values") is None:
            values["column_values"] = pd.DataFrame({column_name: []})

        # ToDo: consider creating bounds models for these
        min_values = {
            "cvlt_form": 0,
            "cvlt_imfr_t1_c": 0,
            "cvlt_imfr_t2_c": 0,
            "cvlt_imfr_t3_c": 0,
            "cvlt_imfr_t4_c": 0,
            "cvlt_imfr_t5_c": 0,
            "cvlt_imfr_t15_total": 0,
            "cvlt_imfr_b_c": 0,
            "cvlt_sdfr_c": 0,
            "cvlt_sdcr_c": 0,
            "cvlt_ldfr_c": 0,
            "cvlt_ldcr_c": 0,
            "cvlt_rep_tot": 0,
            "cvlt_int_tot": 0,
            "cvlt_recog_hits": 0,
            "cvlt_recog_fp": 0,
            "cvltc_imfr_t1_c": 0,
            "cvltc_imfr_t2_c": 0,
            "cvltc_imfr_t3_c": 0,
            "cvltc_imfr_t4_c": 0,
            "cvltc_imfr_t5_c": 0,
            "cvltc_imfr_t15_total": 0,
            "cvltc_imfr_tb_c": 0,
            "cvltc_sdfr_c": 0,
            "cvltc_sdcr_c": 0,
            "cvltc_ldfr_c": 0,
            "cvltc_ldcr_c": 0,
            "cvltc_recog_hits": 0,
            "ravlt_form": 0,
            "ravlt_imfr_t1_c": 0,
            "ravlt_imfr_t1_i": 0,
            "ravlt_imfr_t2_c": 0,
            "ravlt_imfr_t2_i": 0,
            "ravlt_imfr_t3_c": 0,
            "ravlt_imfr_t3_i": 0,
            "ravlt_imfr_t4_c": 0,
            "ravlt_imfr_t4_i": 0,
            "ravlt_imfr_t5_c": 0,
            "ravlt_imfr_t5_i": 0,
            "ravlt_imfr_t15_total": 0,
            "ravlt_imfr_b_c": 0,
            "ravlt_imfr_b_i": 0,
            "ravlt_sdfr_c": 0,
            "ravlt_sdfr_i": 0,
            "ravlt_ldfr_c": 0,
            "ravlt_ldfr_i": 0,
            "ravlt_recog_hits": 0,
            "hvlt_version": 0,
            "hvlt_imfr_t1_c": 0,
            "hvlt_imfr_t2_c": 0,
            "hvlt_imfr_t3_c": 0,
            "hvlt_imfr_t13_total": 0,
            "hvlt_dr_c": 0,
            "hvlt_recog_hits": 0,
        }
        max_values = {
            "cvlt_form": 17,
            "cvlt_imfr_t1_c": 16,
            "cvlt_imfr_t2_c": 16,
            "cvlt_imfr_t3_c": 16,
            "cvlt_imfr_t4_c": 16,
            "cvlt_imfr_t5_c": 80,
            "cvlt_imfr_t15_total": 16,
            "cvlt_imfr_b_c": 16,
            "cvlt_sdfr_c": 16,
            "cvlt_sdcr_c": 16,
            "cvlt_ldfr_c": 16,
            "cvlt_int_tot": 16,
            "cvlt_recog_hits": 32,
            "cvlt_recog_fp": 15,
            "cvltc_imfr_t1_c": 15,
            "cvltc_imfr_t2_c": 15,
            "cvltc_imfr_t3_c": 15,
            "cvltc_imfr_t4_c": 15,
            "cvltc_imfr_t5_c": 75,
            "cvltc_imfr_t15_total": 15,
            "cvltc_imfr_tb_c": 15,
            "cvltc_sdfr_c": 15,
            "cvltc_sdcr_c": 15,
            "cvltc_ldfr_c": 15,
            "cvltc_ldcr_c": 15,
            "cvltc_recog_hits": 30,
            "ravlt_form": 16,
            "ravlt_imfr_t1_i": 16,
            "ravlt_imfr_t2_i": 16,
            "ravlt_imfr_t3_i": 16,
            "ravlt_imfr_t4_i": 16,
            "ravlt_imfr_t5_i": 75,
            "ravlt_imfr_t15_total": 16,
            "ravlt_imfr_b_i": 16,
            "ravlt_sdfr_i": 16,
            "ravlt_ldfr_i": 15,
            "ravlt_recog_hits": 36,
            "hvlt_version": 12,
            "hvlt_imfr_t1_c": 12,
            "hvlt_imfr_t2_c": 12,
            "hvlt_imfr_t3_c": 36,
            "hvlt_imfr_t13_total": 12,
            "hvlt_dr_c": 12,
            "hvlt_recog_hits": 12,
        }

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
