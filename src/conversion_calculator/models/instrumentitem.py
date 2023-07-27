import re

from pydantic import BaseModel, root_validator


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
