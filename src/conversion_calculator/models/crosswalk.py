from typing import Callable, Dict, List, Optional

import numpy as np
from pydantic import BaseModel, Field, validator

from .column import Column
from .instrument import Instrument
from .instrumentitem import InstrumentItem
from .trial import Trial


class CrossWalk(BaseModel):
    column_order: Dict[str, int]
    lookup_table: np.ndarray
    instrument: Instrument
    instrument_item: Optional[InstrumentItem] = None
    trial: Optional[Trial] = None
    rules: Optional[List[Callable]] = Field(default=[])

    class Config:
        arbitrary_types_allowed = True

    @validator("lookup_table")
    def validate_lookup_table(cls, lookup_table):
        if not isinstance(lookup_table, np.ndarray):
            raise ValueError("Invalid array type. Expected numpy.ndarray.")
        return lookup_table

    def walk_possible(self, source_column: Column, target_column: Column) -> bool:
        """
        Check if a crosswalk is possible between two columns.
        """
        if self.rules:
            rule_results = []
            for rule in self.rules:
                rule_results.append(rule(self, target_column))
            return all(rule_results)

        return False
