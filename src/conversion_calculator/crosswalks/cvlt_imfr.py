import numpy as np

from conversion_calculator.models import CrossWalk, Instrument, InstrumentItem

instrument_cvlt = Instrument(id="cvlt")
instrument_item_imfr = InstrumentItem(id="imfr")

cvlt_imfr_column_order = {"cvlt": 0, "ravlt": 1, "hvlt": 2}
cvlt_imfr_lookup_table = np.array(
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
)

cvlt_imfr = CrossWalk(
    instrument=instrument_cvlt,
    instrument_item=instrument_item_imfr,
    column_order=cvlt_imfr_column_order,
    lookup_table=cvlt_imfr_lookup_table,
)
