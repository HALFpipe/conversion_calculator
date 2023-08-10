import numpy as np

from conversion_calculator.models import CrossWalk, Instrument, Trial

from .cvlt_ldrf import cvlt_ldrf
from .cvlt_sdrf import cvlt_sdfr
from .cvlt_t1 import cvlt_t1
from .cvlt_t15 import cvlt_t15
from .hvlt_ldfr import hvlt_ldfr

instrument_hvlt = Instrument(id="hvlt")

instrument_trial_t1 = Trial(id="t1")


hvlt_t1 = CrossWalk(
    instrument=instrument_hvlt,
    trial=instrument_trial_t1,
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
    ),
)
