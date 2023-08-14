import numpy as np

from conversion_calculator.models import CrossWalk, Instrument, InstrumentItem, Trial

instrument_ravlt = Instrument(id="ravlt")
instrument_ravlt_immediate_recall = InstrumentItem(id="imfr")

instrument_trial_t1 = Trial(id="t1")
instrument_trial_t2 = Trial(id="t2")
instrument_trial_t3 = Trial(id="t3")
instrument_trial_t4 = Trial(id="t4")
instrument_trial_t5 = Trial(id="t5")

t_trial_column_order = {
    "ravlt": 0,
    "havlt": 1,
    "cvlt": 2,
}

t_trial_lookup_table = np.array(
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

ravlt_t1 = CrossWalk(
    instrument=instrument_ravlt,
    trial=instrument_trial_t1,
    column_order=t_trial_column_order,
    lookup_table=t_trial_lookup_table,
)

ravlt_t2 = CrossWalk(
    instrument=instrument_ravlt,
    trial=instrument_trial_t2,
    column_order=t_trial_column_order,
    lookup_table=t_trial_lookup_table,
)

ravlt_t3 = CrossWalk(
    instrument=instrument_ravlt,
    trial=instrument_trial_t3,
    column_order=t_trial_column_order,
    lookup_table=t_trial_lookup_table,
)

ravlt_t4 = CrossWalk(
    instrument=instrument_ravlt,
    trial=instrument_trial_t4,
    column_order=t_trial_column_order,
    lookup_table=t_trial_lookup_table,
)

ravlt_t5 = CrossWalk(
    instrument=instrument_ravlt,
    trial=instrument_trial_t5,
    column_order=t_trial_column_order,
    lookup_table=t_trial_lookup_table,
)

ravlt_imfr_t1 = CrossWalk(
    instrument=instrument_ravlt,
    instrument_item=instrument_ravlt_immediate_recall,
    trial=instrument_trial_t1,
    column_order=t_trial_column_order,
    lookup_table=t_trial_lookup_table,
)

ravlt_imfr_t2 = CrossWalk(
    instrument=instrument_ravlt,
    instrument_item=instrument_ravlt_immediate_recall,
    trial=instrument_trial_t2,
    column_order=t_trial_column_order,
    lookup_table=t_trial_lookup_table,
)

ravlt_imfr_t3 = CrossWalk(
    instrument=instrument_ravlt,
    instrument_item=instrument_ravlt_immediate_recall,
    trial=instrument_trial_t3,
    column_order=t_trial_column_order,
    lookup_table=t_trial_lookup_table,
)

ravlt_imfr_t4 = CrossWalk(
    instrument=instrument_ravlt,
    instrument_item=instrument_ravlt_immediate_recall,
    trial=instrument_trial_t4,
    column_order=t_trial_column_order,
    lookup_table=t_trial_lookup_table,
)

ravlt_imfr_t5 = CrossWalk(
    instrument=instrument_ravlt,
    instrument_item=instrument_ravlt_immediate_recall,
    trial=instrument_trial_t5,
    column_order=t_trial_column_order,
    lookup_table=t_trial_lookup_table,
)