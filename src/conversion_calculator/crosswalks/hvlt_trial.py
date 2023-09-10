import numpy as np

from conversion_calculator.models import (CrossWalk, Instrument,
                                          InstrumentItem, Trial, ValueType)

instrument_hvlt = Instrument(id="hvlt")
instrument_item_imfr = InstrumentItem(id="imfr")

trial_t1 = Trial(id="t1")
trial_t2 = Trial(id="t2")
trial_t3 = Trial(id="t3")
trial_t4 = Trial(id="t4")
trial_t5 = Trial(id="t5")
trial_t13 = Trial(id="t13")

value_type_c = ValueType(id="c")
value_type_total = ValueType(id="total")

hvlt_trial_column_order = {
    "hvlt": 0,
    "cvlt": 1,
    "ravlt": 2,
}

hvlt_trial_lookup_table = np.array(
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
    trial=trial_t1,
    column_order=hvlt_trial_column_order,
    lookup_table=hvlt_trial_lookup_table,
)

hvlt_t2 = CrossWalk(
    instrument=instrument_hvlt,
    trial=trial_t2,
    column_order=hvlt_trial_column_order,
    lookup_table=hvlt_trial_lookup_table,
)

hvlt_t3 = CrossWalk(
    instrument=instrument_hvlt,
    trial=trial_t3,
    column_order=hvlt_trial_column_order,
    lookup_table=hvlt_trial_lookup_table,
)

hvlt_t4 = CrossWalk(
    instrument=instrument_hvlt,
    trial=trial_t4,
    column_order=hvlt_trial_column_order,
    lookup_table=hvlt_trial_lookup_table,
)

hvlt_t5 = CrossWalk(
    instrument=instrument_hvlt,
    trial=trial_t5,
    column_order=hvlt_trial_column_order,
    lookup_table=hvlt_trial_lookup_table,
)

hvlt_imfr_t1 = CrossWalk(
    instrument=instrument_hvlt,
    instrument_item=instrument_item_imfr,
    trial=trial_t1,
    column_order=hvlt_trial_column_order,
    lookup_table=hvlt_trial_lookup_table,
)

hvlt_imfr_t2 = CrossWalk(
    instrument=instrument_hvlt,
    instrument_item=instrument_item_imfr,
    trial=trial_t2,
    column_order=hvlt_trial_column_order,
    lookup_table=hvlt_trial_lookup_table,
)

hvlt_imfr_t3 = CrossWalk(
    instrument=instrument_hvlt,
    instrument_item=instrument_item_imfr,
    trial=trial_t3,
    column_order=hvlt_trial_column_order,
    lookup_table=hvlt_trial_lookup_table,
)

hvlt_imfr_t4 = CrossWalk(
    instrument=instrument_hvlt,
    instrument_item=instrument_item_imfr,
    trial=trial_t4,
    column_order=hvlt_trial_column_order,
    lookup_table=hvlt_trial_lookup_table,
)

hvlt_imfr_t5 = CrossWalk(
    instrument=instrument_hvlt,
    instrument_item=instrument_item_imfr,
    trial=trial_t5,
    column_order=hvlt_trial_column_order,
    lookup_table=hvlt_trial_lookup_table,
)

hvlt_imfr_t1_c = CrossWalk(
    instrument=instrument_hvlt,
    instrument_item=instrument_item_imfr,
    trial=trial_t1,
    value_type=value_type_c,
    column_order=hvlt_trial_column_order,
    lookup_table=hvlt_trial_lookup_table,
)

hvlt_imfr_t2_c = CrossWalk(
    instrument=instrument_hvlt,
    instrument_item=instrument_item_imfr,
    trial=trial_t2,
    value_type=value_type_c,
    column_order=hvlt_trial_column_order,
    lookup_table=hvlt_trial_lookup_table,
)

hvlt_imfr_t3_c = CrossWalk(
    instrument=instrument_hvlt,
    instrument_item=instrument_item_imfr,
    trial=trial_t3,
    value_type=value_type_c,
    column_order=hvlt_trial_column_order,
    lookup_table=hvlt_trial_lookup_table,
)

hvlt_imfr_t13_total = CrossWalk(
    instrument=instrument_hvlt,
    instrument_item=instrument_item_imfr,
    trial=trial_t13,
    value_type=value_type_total,
    column_order=hvlt_trial_column_order,
    lookup_table=hvlt_trial_lookup_table,
)
