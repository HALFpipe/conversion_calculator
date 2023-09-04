from typing import Dict, Optional

import numpy as np
from pydantic import BaseModel, validator

from ..models import ValueBounds
from .column import Column
from .instrument import Instrument
from .instrumentitem import InstrumentItem
from .trial import Trial
from .valuetype import ValueType


class CrossWalk(BaseModel):
    column_order: Dict[str, int]
    lookup_table: np.ndarray
    instrument: Instrument
    instrument_item: Optional[InstrumentItem] = None
    trial: Optional[Trial] = None
    value_bounds: Optional[ValueBounds] = None
    value_type: Optional[ValueType] = None

    class Config:
        arbitrary_types_allowed = True

    @validator("lookup_table")
    def validate_lookup_table(cls, lookup_table):
        if not isinstance(lookup_table, np.ndarray):
            raise ValueError("Invalid array type. Expected numpy.ndarray.")
        return lookup_table

    def check_instrument_matches_crosswalk(self, column: Column) -> bool:
        # instrument must match
        return self.instrument == column.instrument

    def check_instrument_item_matches_crosswalk(self, column: Column) -> bool:
        # check if the crosswalk and column have the same instrument item, or are both None
        if (column.instrument_item and self.instrument_item) and (
            column.instrument_item == self.instrument_item
        ):
            return True

        if (column.instrument_item is None) and (self.instrument_item is None):
            return True
        
        if (column.instrument_item in ['dr', 'ldfr']) and (self.instrument_item in ['dr', 'ldfr']):
            return True

        return False

    def check_trial_matches_crosswalk(self, column: Column) -> bool:
        # check if the crosswalk and column have the same trial or are both None

        if (column.trial and self.trial) and (column.trial == self.trial):
            return True

        if column.trial is None and self.trial is None:
            return True

        return False
    
    def check_value_type_matches_crosswalk(self, column: Column) -> bool:
        # check if the crosswalk and column have the same value type or are both None

        if (column.value_type and self.value_type) and (column.value_type == self.value_type):
            return True

        if column.value_type is None and self.value_type is None:
            return True

        return False

    def check_target_instrument_in_lookup_table(self, target_column: Column) -> bool:
        return target_column.instrument.id in self.column_order

    def both_columns_have_same_attribute_set(self, source_column: Column, target_column: Column) -> bool:
        for attribute in [ "instrument_item", "instrument_metadata_type", "value_type", "trial" ]:
            if getattr(source_column, attribute) != getattr(target_column, attribute):
                return False
        return True

    def check_for_valid_values(
        self, source_column: Column, target_column: Column
    ) -> bool:
        if source_column.column_values is None or source_column.column_values.empty:
            return False

        if not target_column.column_values.isna().values.all():
            return False

        return True

    def walk_possible(self, source_column: Column, target_column: Column) -> bool:
        return all(
            [
                self.check_instrument_matches_crosswalk(source_column),
                self.check_instrument_item_matches_crosswalk(source_column),
                self.check_trial_matches_crosswalk(source_column),
                self.check_instrument_item_matches_crosswalk(target_column),
                self.check_trial_matches_crosswalk(target_column),
                self.check_value_type_matches_crosswalk(source_column),
                self.check_for_valid_values(source_column, target_column),
                self.both_columns_have_same_attribute_set(source_column, target_column),
                self.check_target_instrument_in_lookup_table(target_column),
            ]
        )

def column_to_column_crosswalk_possible(crosswalk: CrossWalk, source_column: Column, target_column: Column) -> bool:
    # crosswalk instrument and source instrument must match
    # if set, crosswalk instrument item and source column instrument item must match
    #    exception: if the source column instrument item is dr, or ldfr, then the crosswalk can be ldfr
    # if set, crosswalk instrument meta data type and source column instrument meta data type must match
    # if set, crosswalk trial and source column trial must match
    # if set, crosswalk value_type and source column value_type must match
    return crosswalk.walk_possible(source_column, target_column)
