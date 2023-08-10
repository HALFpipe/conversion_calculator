import numpy as np

from conversion_calculator.models import CrossWalk, Instrument, Trial

instrument_hvlt = Instrument(id="hvlt")

instrument_trial_t15 = Trial(id="t15")


hvlt_t15 = CrossWalk(
    instrument=instrument_hvlt,
    trial=instrument_trial_t15,
    column_order={
        "hvlt": 0,
        "cvlt": 1,
        "ravlt": 2,
    },
    lookup_table=np.array(
        [
            [0, 0, 0],
            [1, 0, 0],
            [2, 0, 0],
            [3, 0, 0],
            [4, 0, 0],
            [5, 0, 1],
            [6, 2, 4],
            [7, 5, 7],
            [8, 7, 10],
            [9, 10, 12],
            [10, 12, 15],
            [11, 15, 17],
            [12, 18, 20],
            [13, 20, 22],
            [14, 22, 24],
            [15, 25, 26],
            [16, 27, 28],
            [17, 29, 30],
            [18, 32, 32],
            [19, 34, 34],
            [20, 36, 36],
            [21, 38, 38],
            [22, 41, 40],
            [23, 43, 42],
            [24, 45, 44],
            [25, 47, 46],
            [26, 49, 48],
            [27, 52, 50],
            [28, 54, 52],
            [29, 56, 55],
            [30, 58, 57],
            [31, 61, 59],
            [32, 63, 61],
            [33, 65, 64],
            [34, 68, 66],
            [35, 70, 68],
            [36, 72, 71],
        ]
    ),
)
