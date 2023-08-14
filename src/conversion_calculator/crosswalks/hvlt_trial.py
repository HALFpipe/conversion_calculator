import numpy as np

from conversion_calculator.crosswalks.rules import (
    check_for_valid_values,
    check_instrument_match,
    check_same_attributes_set,
    check_target_instrument_in_lookup_table,
    check_trial_match,
)
from conversion_calculator.models import CrossWalk, Instrument, Trial

instrument_hvlt = Instrument(id="hvlt")

instrument_trial_t1 = Trial(id="t1")
instrument_trial_t2 = Trial(id="t2")
instrument_trial_t3 = Trial(id="t3")
instrument_trial_t4 = Trial(id="t4")
instrument_trial_t5 = Trial(id="t5")

t_trial_common_rules = [
    check_for_valid_values,
    check_instrument_match,
    check_same_attributes_set,
    check_target_instrument_in_lookup_table,
    check_trial_match,
]

t_trial_column_order = {
    "hvlt": 0,
    "cvlt": 1,
    "ravlt": 2,
}

t_trial_lookup_table = np.array(
    [
        [0, 0, 0],
        [1, 0, 0],
        [2, 0, 0],
        [3, 1, 0],
        [4, 2, 2],
        [5, 4, 4],
        [6, 5, 5],
        [7, 6, 6],
        [8, 7, 7],
        [9, 8, 9],
        [10, 9, 10],
        [11, 10, 11],
        [12, 11, 13],
    ]
)

hvlt_t1 = CrossWalk(
    instrument=instrument_hvlt,
    trial=instrument_trial_t1,
    column_order=t_trial_column_order,
    lookup_table=t_trial_lookup_table,
    rules=t_trial_common_rules,
)

hvlt_t2 = CrossWalk(
    instrument=instrument_hvlt,
    trial=instrument_trial_t2,
    column_order=t_trial_column_order,
    lookup_table=t_trial_lookup_table,
    rules=t_trial_common_rules,
)

hvlt_t3 = CrossWalk(
    instrument=instrument_hvlt,
    trial=instrument_trial_t3,
    column_order=t_trial_column_order,
    lookup_table=t_trial_lookup_table,
    rules=t_trial_common_rules,
)

hvlt_t4 = CrossWalk(
    instrument=instrument_hvlt,
    trial=instrument_trial_t4,
    column_order=t_trial_column_order,
    lookup_table=t_trial_lookup_table,
    rules=t_trial_common_rules,
)

hvlt_t5 = CrossWalk(
    instrument=instrument_hvlt,
    trial=instrument_trial_t5,
    column_order=t_trial_column_order,
    lookup_table=t_trial_lookup_table,
    rules=t_trial_common_rules,
)
