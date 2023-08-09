import numpy as np

from conversion_calculator.models import CrossWalk, Instrument, InstrumentItem

instrument_cvlt = Instrument(id="cvlt")
instrument_item_ldfr = InstrumentItem(id="ldfr")

cvlt_ldrf = CrossWalk(
    instrument=instrument_cvlt,
    instrument_item=instrument_item_ldfr,
    column_order={"cvlt": 0, "ravlt": 1, "hvlt": 2},
    lookup_table=np.array(
        [
            [0, 0, 0],
            [1, 2, 3],
            [2, 2, 3],
            [3, 3, 4],
            [4, 4, 5],
            [5, 5, 5],
            [6, 6, 6],
            [7, 7, 6],
            [8, 8, 7],
            [9, 8, 8],
            [10, 9, 8],
            [11, 10, 9],
            [12, 11, 9],
            [13, 12, 10],
            [14, 12, 10],
            [15, 13, 11],
            [16, 14, 12],
        ]
    ),
)
