import re
from typing import Optional

from pydantic import BaseModel, root_validator


class Trial(BaseModel):
    id: str
    alias: Optional[str] = None

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
