import numpy as np

from conversion_calculator.models import CrossWalk, Instrument, InstrumentItem

instrument_ravlt = Instrument(id="ravlt")

instrument_item_sdfr = InstrumentItem(id="sdfr")
instrument_ravlt_column_order = {"ravlt": 0, "cvlt": 1}
instrument_ravlt_lookup_table = np.array(
    [
        [0, 0],
        [0, 0],
        [1, 0],
        [2, 0],
        [3, 2],
        [4, 3],
        [5, 4],
        [6, 5],
        [7, 6],
        [8, 8],
        [9, 9],
        [10, 10],
        [11, 12],
        [12, 13],
        [13, 15],
        [14, 16],
        [15, 16],
    ]
)

ravlt_sdfr = CrossWalk(
    instrument=instrument_ravlt,
    instrument_item=instrument_item_sdfr,
    column_order=instrument_ravlt_column_order,
    lookup_table=instrument_ravlt_lookup_table,
)
