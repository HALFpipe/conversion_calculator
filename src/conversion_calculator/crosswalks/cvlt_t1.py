import numpy as np

from conversion_calculator.models import CrossWalk, Instrument, Trial

instrument_cvlt = Instrument(id="cvlt")
instrument_trial_t1 = Trial(id="t1")


cvlt_t1 = CrossWalk(
    instrument=instrument_cvlt,
    trial=instrument_trial_t1,
    column_order={
        "cvlt": 0,
        "ravlt": 1,
        "hvlt": 2,
    },
    lookup_table=np.array(
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
    ),
)
