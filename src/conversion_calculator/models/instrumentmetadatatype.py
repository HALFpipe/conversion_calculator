import re

from pydantic import BaseModel, root_validator


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
