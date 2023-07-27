from typing import Dict, Optional

import numpy as np
from pydantic import BaseModel, validator

from .instrument import Instrument
from .instrumentitem import InstrumentItem
from .trial import Trial


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
