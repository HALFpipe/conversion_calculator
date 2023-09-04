import numpy as np

from conversion_calculator.models import (CrossWalk, Instrument,
                                          InstrumentItem, Trial, ValueType)

instrument_cvlt = Instrument(id="cvlt")
instrument_item_imfr = InstrumentItem(id="imfr")
value_type_c = ValueType(id="c")
trial_t1 = Trial(id="t1")
trial_t2 = Trial(id="t2")
trial_t3 = Trial(id="t3")
trial_t4 = Trial(id="t4")
trial_t5 = Trial(id="t5")
trial_t15 = Trial(id="t15")
trial_b = Trial(id='b')

t_trial_column_order = {
    "cvlt": 0,
    "ravlt": 1,
    "hvlt": 2,
}

t_trial_lookup_table = np.array(
    [
        [0, 0, 0],
        [1, 0, 3],
        [2, 1, 4],
        [3, 3, 4],
        [4, 4, 5],
        [5, 5, 6],
        [6, 6, 7],
        [7, 7, 8],
        [8, 8, 9],
        [9, 9, 10],
        [10, 11, 10],
        [11, 12, 11],
        [12, 14, 12],
        [13, 15, 12],
        [14, 15, 12],
        [15, 15, 12],
        [16, 15, 12],
    ]
)

cvlt_imfr_t1_c = CrossWalk(
    instrument=instrument_cvlt,
    instrument_item=instrument_item_imfr,
    trial=trial_t1,
    value_type=value_type_c,
    column_order=t_trial_column_order,
    lookup_table=t_trial_lookup_table,
)

cvlt_imfr_t2_c = CrossWalk(
    instrument=instrument_cvlt,
    instrument_item=instrument_item_imfr,
    trial=trial_t2,
    value_type=value_type_c,
    column_order=t_trial_column_order,
    lookup_table=t_trial_lookup_table,
)

cvlt_imfr_t3_c = CrossWalk(
    instrument=instrument_cvlt,
    instrument_item=instrument_item_imfr,
    trial=trial_t3,
    value_type=value_type_c,
    column_order=t_trial_column_order,
    lookup_table=t_trial_lookup_table,
)

cvlt_imfr_t4_c = CrossWalk(
    instrument=instrument_cvlt,
    instrument_item=instrument_item_imfr,
    trial=trial_t4,
    value_type=value_type_c,
    column_order=t_trial_column_order,
    lookup_table=t_trial_lookup_table,
)

cvlt_imfr_t5_c = CrossWalk(
    instrument=instrument_cvlt,
    instrument_item=instrument_item_imfr,
    trial=trial_t5,
    value_type=value_type_c,
    column_order=t_trial_column_order,
    lookup_table=t_trial_lookup_table,
)

cvlt_imfr_b_c = CrossWalk(
    instrument=instrument_cvlt,
    instrument_item=instrument_item_imfr,
    trial=trial_b,
    value_type=value_type_c,
    column_order=t_trial_column_order,
    lookup_table=t_trial_lookup_table,
)
