import re
from pydantic import BaseModel, root_validator


__all__ = [
    "Instrument",
    "InstrumentItem",
    "InstrumentMetadataType",
    "Trial",
    "ValueType",
    "ColumnName",
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
    def validate_instrument(cls, values):
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


class ColumnName(BaseModel):
    column_name: str

    @root_validator
    def validate_column_name(cls, values):
        """Get the class and class values, validate the column_name, and generate the derived fields"""
        COLUMN_TITLE_REGEX = r"^(cvlt|cvltc|ravlt|hvlt)_([a-z_0-9])+$"

        column_name = values.get("column_name")

        if not re.match(COLUMN_TITLE_REGEX, column_name):
            raise ValueError(
                "Invalid 'column_name' format. It should match the pattern: ^(cvlt|cvltc|ravlt|hvlt)_([a-z_])+$"
            )

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
