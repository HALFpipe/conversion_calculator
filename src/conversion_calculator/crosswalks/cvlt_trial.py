import numpy as np

from conversion_calculator.models import (CrossWalk, Instrument,
                                          InstrumentItem, Trial)

instrument_cvlt = Instrument(id="cvlt")

instrument_cvlt_item_immediate_recall = InstrumentItem(id="imfr")

instrument_trial_t1 = Trial(id="t1")
instrument_trial_t2 = Trial(id="t2")
instrument_trial_t3 = Trial(id="t3")
instrument_trial_t4 = Trial(id="t4")
instrument_trial_t5 = Trial(id="t5")

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

cvlt_t1 = CrossWalk(
    instrument=instrument_cvlt,
    trial=instrument_trial_t1,
    column_order=t_trial_column_order,
    lookup_table=t_trial_lookup_table,
)

cvlt_t2 = CrossWalk(
    instrument=instrument_cvlt,
    trial=instrument_trial_t2,
    column_order=t_trial_column_order,
    lookup_table=t_trial_lookup_table,
)

cvlt_t3 = CrossWalk(
    instrument=instrument_cvlt,
    trial=instrument_trial_t3,
    column_order=t_trial_column_order,
    lookup_table=t_trial_lookup_table,
)

cvlt_t4 = CrossWalk(
    instrument=instrument_cvlt,
    trial=instrument_trial_t4,
    column_order=t_trial_column_order,
    lookup_table=t_trial_lookup_table,
)

cvlt_t5 = CrossWalk(
    instrument=instrument_cvlt,
    trial=instrument_trial_t5,
    column_order=t_trial_column_order,
    lookup_table=t_trial_lookup_table,
)

cvlt_imfr_t1 = CrossWalk(
    instrument=instrument_cvlt,
    trial=instrument_trial_t1,
    column_order=t_trial_column_order,
    lookup_table=t_trial_lookup_table,
)

cvlt_imfr_t2 = CrossWalk(
    instrument=instrument_cvlt,
    instrument_item=instrument_cvlt_item_immediate_recall,
    trial=instrument_trial_t2,
    column_order=t_trial_column_order,
    lookup_table=t_trial_lookup_table,
)

cvlt_imfr_t3 = CrossWalk(
    instrument=instrument_cvlt,
    instrument_item=instrument_cvlt_item_immediate_recall,
    trial=instrument_trial_t3,
    column_order=t_trial_column_order,
    lookup_table=t_trial_lookup_table,
)

cvlt_imfr_t4 = CrossWalk(
    instrument=instrument_cvlt,
    instrument_item=instrument_cvlt_item_immediate_recall,
    trial=instrument_trial_t4,
    column_order=t_trial_column_order,
    lookup_table=t_trial_lookup_table,
)

cvlt_imfr_t5 = CrossWalk(
    instrument=instrument_cvlt,
    instrument_item=instrument_cvlt_item_immediate_recall,
    trial=instrument_trial_t5,
    column_order=t_trial_column_order,
    lookup_table=t_trial_lookup_table,
)
