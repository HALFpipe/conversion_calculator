import re

from pydantic import BaseModel, root_validator


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
