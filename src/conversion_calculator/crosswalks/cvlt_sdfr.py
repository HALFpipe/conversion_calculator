import numpy as np

from conversion_calculator.models import CrossWalk, Instrument, InstrumentItem

instrument_cvlt = Instrument(id="cvlt")
instrument_item_sdfr = InstrumentItem(id="sdfr")

cvlt_sdfr = CrossWalk(
    instrument=instrument_cvlt,
    instrument_item=instrument_item_sdfr,
    column_order={
        "cvlt": 0,
        "ravlt": 1,
    },
    lookup_table=np.array(
        [
            [0, 0],
            [1, 2],
            [2, 3],
            [3, 4],
            [4, 5],
            [5, 6],
            [6, 7],
            [7, 7],
            [8, 8],
            [9, 9],
            [10, 10],
            [11, 10],
            [12, 11],
            [13, 12],
            [14, 12],
            [15, 13],
            [16, 14],
        ]
    ),
)
