import numpy as np

from conversion_calculator.models import CrossWalk, Instrument, Trial

instrument_ravlt = Instrument(id="ravlt")

instrument_trial_t1 = Trial(id="t1")
instrument_trial_t15 = Trial(id="t15")


ravlt_t1 = CrossWalk(
    instrument=instrument_ravlt,
    trial=instrument_trial_t1,
    column_order={
        "ravlt": 0,
        "havlt": 1,
        "cvlt": 2,
    },
    lookup_table=np.array(
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
    ),
)
