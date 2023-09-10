import numpy as np

from conversion_calculator.models import (CrossWalk, Instrument,
                                          InstrumentItem, Trial, ValueType)

instrument_ravlt = Instrument(id="ravlt")
instrument_ravlt_immediate_recall = InstrumentItem(id="imfr")
value_type_c = ValueType(id="c")
value_type_i = ValueType(id="i")
trial_t1 = Trial(id="t1")
trial_t2 = Trial(id="t2")
trial_t3 = Trial(id="t3")
trial_t4 = Trial(id="t4")
trial_t5 = Trial(id="t5")
trial_t15 = Trial(id="t15")
trial_b = Trial(id='b')

ravlt_trial_column_order = {
    "ravlt": 0,
    "havlt": 1,
    "cvlt": 2,
}

ravlt_trial_lookup_table = np.array(
    [
        [0, 0, 0],
        [1, 3, 2],
        [2, 4, 2],
        [3, 4, 3],
        [4, 5, 4],
        [5, 6, 5],
        [6, 7, 6],
        [7, 8, 7],
        [8, 8, 8],
        [9, 9, 8],
        [10, 10, 9],
        [11, 11, 10],
        [12, 12, 11],
        [13, 12, 12],
        [14, 12, 12],
        [15, 12, 12],
    ]
)

ravlt_imfr_t1_c = CrossWalk(
    instrument=instrument_ravlt,
    instrument_item=instrument_ravlt_immediate_recall,
    trial=trial_t1,
    value_type=value_type_c,
    column_order=ravlt_trial_column_order,
    lookup_table=ravlt_trial_lookup_table,
)

ravlt_imfr_t2_c = CrossWalk(
    instrument=instrument_ravlt,
    instrument_item=instrument_ravlt_immediate_recall,
    trial=trial_t2,
    value_type=value_type_c,
    column_order=ravlt_trial_column_order,
    lookup_table=ravlt_trial_lookup_table,
)

ravlt_imfr_t3_c = CrossWalk(
    instrument=instrument_ravlt,
    instrument_item=instrument_ravlt_immediate_recall,
    trial=trial_t3,
    value_type=value_type_c,
    column_order=ravlt_trial_column_order,
    lookup_table=ravlt_trial_lookup_table,
)

ravlt_imfr_t4_c = CrossWalk(
    instrument=instrument_ravlt,
    instrument_item=instrument_ravlt_immediate_recall,
    trial=trial_t4,
    value_type=value_type_c,
    column_order=ravlt_trial_column_order,
    lookup_table=ravlt_trial_lookup_table,
)

ravlt_imfr_t5_c = CrossWalk(
    instrument=instrument_ravlt,
    instrument_item=instrument_ravlt_immediate_recall,
    trial=trial_t5,
    value_type=value_type_c,
    column_order=ravlt_trial_column_order,
    lookup_table=ravlt_trial_lookup_table,
)

ravlt_imfr_b_c = CrossWalk(
    instrument=instrument_ravlt,
    instrument_item=instrument_ravlt_immediate_recall,
    trial=trial_b,
    value_type=value_type_c,
    column_order=ravlt_trial_column_order,
    lookup_table=ravlt_trial_lookup_table,
)

ravlt_imfr_t1_i = CrossWalk(
    instrument=instrument_ravlt,
    instrument_item=instrument_ravlt_immediate_recall,
    trial=trial_t1,
    value_type=value_type_i,
    column_order=ravlt_trial_column_order,
    lookup_table=ravlt_trial_lookup_table,
)

ravlt_imfr_t2_i = CrossWalk(
    instrument=instrument_ravlt,
    instrument_item=instrument_ravlt_immediate_recall,
    trial=trial_t2,
    value_type=value_type_i,
    column_order=ravlt_trial_column_order,
    lookup_table=ravlt_trial_lookup_table,
)

ravlt_imfr_t3_i = CrossWalk(
    instrument=instrument_ravlt,
    instrument_item=instrument_ravlt_immediate_recall,
    trial=trial_t3,
    value_type=value_type_i,
    column_order=ravlt_trial_column_order,
    lookup_table=ravlt_trial_lookup_table,
)

ravlt_imfr_t4_i = CrossWalk(
    instrument=instrument_ravlt,
    instrument_item=instrument_ravlt_immediate_recall,
    trial=trial_t4,
    value_type=value_type_i,
    column_order=ravlt_trial_column_order,
    lookup_table=ravlt_trial_lookup_table,
)

ravlt_imfr_t5_i = CrossWalk(
    instrument=instrument_ravlt,
    instrument_item=instrument_ravlt_immediate_recall,
    trial=trial_t5,
    value_type=value_type_i,
    column_order=ravlt_trial_column_order,
    lookup_table=ravlt_trial_lookup_table,
)

ravlt_imfr_b_i = CrossWalk(
    instrument=instrument_ravlt,
    instrument_item=instrument_ravlt_immediate_recall,
    trial=trial_b,
    value_type=value_type_i,
    column_order=ravlt_trial_column_order,
    lookup_table=ravlt_trial_lookup_table,
)
