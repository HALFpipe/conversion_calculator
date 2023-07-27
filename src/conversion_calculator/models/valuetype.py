import re

from pydantic import BaseModel, root_validator


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
