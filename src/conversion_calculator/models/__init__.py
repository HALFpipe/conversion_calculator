import re
from typing import Dict, List, Optional, Union

import pandas as pd
import numpy as np
from pydantic import BaseModel, root_validator, validator

__all__ = [
    "Instrument",
    "InstrumentItem",
    "InstrumentMetadataType",
    "Trial",
    "ValueType",
    "Column",
]


class Instrument(BaseModel):
    id: str

    @root_validator
    def validate_instrument(cls, values):
        """Get class and class values, and lookup the friendly name"""
        INSTRUMENT_NAME_REGEX = r"^(cvlt|cvltc|ravlt|hvlt)$"
        instrument_id_to_friendly_name = {
            "cvlt": "California Verbal Learning Test",
            "cvltc": "California Verbal Learning Test - Children's Version",
            "ravlt": "Rey Auditory Verbal Learning Test",
            "hvlt": "Hopkins Verbal Learning Test",
        }

        if not re.match(INSTRUMENT_NAME_REGEX, values["id"]):
            raise ValueError(
                f"Invalid 'id' format. It should match the pattern: {INSTRUMENT_NAME_REGEX}"
            )

        values["friendly_name"] = instrument_id_to_friendly_name.get(values["id"])
        return values


class InstrumentItem(BaseModel):
    id: str

    @root_validator
    def validate_instrumentitem(cls, values):
        """Get class and class values, and lookup the friendly name"""
        INSTRUMENT_ITEM_NAME_REGEX = r"^(dr|imfr|ldfr|ldcr|recog|sdcr|sdfr|rep|int)$"
        instrument_item_id_to_friendly_name = {
            "dr": "Delayed Recall",
            "imfr": "Encoding",
            "ldcr": "Long-Delay Cued Recall",
            "ldfr": "Long-Delay Spontaneous Recall",
            "recog": "Recognition",
            "sdcr": "Short-Delay Cued Recall",
            "sdfr": "Short-Delay Spontaneous Recall",
            "rep": "EDITOR: add friendly name",
            "int": "EDITOR: add friendly name",
        }

        if not re.match(INSTRUMENT_ITEM_NAME_REGEX, values["id"]):
            raise ValueError(
                f"Invalid 'id' format. It should match the pattern: {INSTRUMENT_ITEM_NAME_REGEX}"
            )

        values["friendly_name"] = instrument_item_id_to_friendly_name.get(values["id"])
        return values


class InstrumentMetadataType(BaseModel):
    id: str

    @root_validator
    def validate_instrument_metadata_type(cls, values):
        """Get class and class values, and lookup the friendly name"""
        INSTRUMENT_METADATA_TYPE_REGEX = r"^(form|version)$"
        instrument_metadata_type_id_to_friendly_name = {
            "form": "Form",
            "version": "Version",
        }

        if not re.match(INSTRUMENT_METADATA_TYPE_REGEX, values["id"]):
            raise ValueError(
                f"Invalid 'id' format. It should match the pattern: {INSTRUMENT_METADATA_TYPE_REGEX}"
            )

        values["friendly_name"] = instrument_metadata_type_id_to_friendly_name.get(
            values["id"]
        )
        return values


class Trial(BaseModel):
    id: str

    @root_validator
    def validate_trial(cls, values):
        """Get class and class values, and lookup the friendly name"""
        TRIAL_NAME_REGEX = r"^(t1|t2|t3|t4|t5|t13|t15|tb|b)$"
        trial_id_to_friendly_name = {
            "t1": "Trial 1",
            "t2": "Trial 2",
            "t3": "Trial 3",
            "t4": "Trial 4",
            "t5": "Trial 5",
            "t13": "Trial 1-3",
            "t15": "Trial 1-5",
            "tb": "Total",
            "b": "EDITOR: add friendly name",
        }

        if not re.match(TRIAL_NAME_REGEX, values["id"]):
            raise ValueError(
                f"Invalid 'id' format. It should match the pattern: {TRIAL_NAME_REGEX}"
            )

        values["friendly_name"] = trial_id_to_friendly_name.get(values["id"])
        return values


class ValueType(BaseModel):
    id: str

    @root_validator
    def validate_value_type(cls, values):
        """Get class and class values, and lookup the friendly name"""
        VALUE_TYPES_REGEX = r"^(total|hits|c|i|fp)$"
        value_type_id_to_friendly_name = {
            "total": "Total",
            "hits": "Hits",
            "c": "Cue",
            "i": "Intrusion",
            "fp": "EDITOR: add friendly name for fp",
        }

        if not re.match(VALUE_TYPES_REGEX, values["id"]):
            raise ValueError(
                f"Invalid 'id' format. It should match the pattern: {VALUE_TYPES_REGEX}"
            )

        values["friendly_name"] = value_type_id_to_friendly_name.get(values["id"])
        return values


class Column(BaseModel):
    column_name: str
    column_values: Optional[Union[List[int], pd.DataFrame]]
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

    @validator('column_values', pre=True)
    def convert_to_dataframe_or_default(cls, value, values):
        if isinstance(value, pd.DataFrame):
            if value.shape[1] != 1:
                raise ValueError("Invalid column_values. Expected a single column dataframe.")
            if values['column_name'] != value.columns[0]:
                raise ValueError("Invalid column_values. Expected column name to match column_name.")
            return value
        elif isinstance(value, list):
            return pd.DataFrame({values['column_name']: value})
        else:
            return pd.DataFrame({values['column_name']: []})

class CrossWalk(BaseModel):
    column_order: Dict[str, int]
    lookup_table: np.ndarray
    source_instrument: Instrument
    source_instrument_item: Optional[InstrumentItem] = None
    source_trial: Optional[Trial] = None

    class Config:
        arbitrary_types_allowed = True

    @validator("lookup_table")
    def validate_lookup_table(cls, lookup_table):
        if not isinstance(lookup_table, np.ndarray):
            raise ValueError("Invalid array type. Expected numpy.ndarray.")
        return lookup_table
