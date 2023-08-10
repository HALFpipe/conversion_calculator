from typing import Dict, Optional

import numpy as np
from pydantic import BaseModel, validator

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

    class Config:
        arbitrary_types_allowed = True

    @validator("lookup_table")
    def validate_lookup_table(cls, lookup_table):
        if not isinstance(lookup_table, np.ndarray):
            raise ValueError("Invalid array type. Expected numpy.ndarray.")
        return lookup_table

    def check_instrument_match(self, column: Column) -> bool:
        # instrument must match
        return self.instrument == column.instrument

    def check_instrument_item_match(self, column: Column) -> bool:
        # check if the crosswalk and column have the same instrument item, or are both None
        if (column.instrument_item and self.instrument_item) and (
            (column.instrument_item == self.instrument_item)
            or (
                column.instrument_item.id in ["dr", "ldfr"]
                and self.instrument_item.id in ["dr", "ldfr"]
            )
        ):
            return True

        if (column.instrument_item is None) and (self.instrument_item is None):
            return True

        return False

    def check_trial_match(self, column: Column) -> bool:
        # check if the crosswalk and column have the same trial or are both None

        if (column.trial and self.trial) and (column.trial == self.trial):
            return True

        if column.trial is None and self.trial is None:
            return True

        return False

    def check_same_attributes_set(self, column: Column) -> bool:
        # check if the crosswalk and column have the same attributes set
        # please note, this only checks that the 'truthyness' of the attributes are the same
        # checking that those attributes are the same values is done elsewhere
        same_attributes = []

        if (
            self.instrument_item is not None and column.instrument_item is not None
        ) or (self.instrument_item is None and column.instrument_item is None):
            same_attributes.append(True)

        if (self.trial is not None and column.trial is not None) or (
            self.trial is None and column.trial is None
        ):
            same_attributes.append(True)

        return all(same_attributes)

    def check_for_valid_values(
        self, source_column: Column, target_column: Column
    ) -> bool:
        if source_column.column_values is None or source_column.column_values.empty:
            return False

        if not target_column.column_values.isna().values.all():
            return False

        return True

    def check_target_instrument_in_lookup_table(self, target_column: Column) -> bool:
        return target_column.instrument.id in self.column_order

    def walk_possible(self, source_column: Column, target_column: Column) -> bool:
        return all(
            [
                self.check_instrument_match(source_column),
                self.check_instrument_item_match(source_column),
                self.check_trial_match(source_column),
                self.check_instrument_item_match(target_column),
                self.check_trial_match(target_column),
                self.check_same_attributes_set(source_column),
                self.check_same_attributes_set(target_column),
                self.check_for_valid_values(source_column, target_column),
                self.check_target_instrument_in_lookup_table(target_column),
            ]
        )
