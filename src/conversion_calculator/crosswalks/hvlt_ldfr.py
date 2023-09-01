import numpy as np

from conversion_calculator.models import CrossWalk, Instrument, InstrumentItem

instrument_hvlt = Instrument(id="hvlt")

instrument_item_ldfr = InstrumentItem(id="ldfr")

hvlt_ldfr_column_order = {"hvlt": 0, "cvlt": 1, "ravlt": 2}
hvlt_ldfr_lookup_table = np.array(
        [
            [0, 0, 0],
            [1, 0, 0],
            [2, 0, 1],
            [3, 1, 2],
            [4, 3, 3],
            [5, 4, 5],
            [6, 6, 6],
            [7, 8, 7],
            [8, 10, 9],
            [9, 11, 10],
            [10, 13, 12],
            [11, 15, 13],
            [12, 16, 14],
        ])

hvlt_ldfr = CrossWalk(
    instrument=instrument_hvlt,
    instrument_item=instrument_item_ldfr,
    column_order=hvlt_ldfr_column_order,
    lookup_table=hvlt_ldfr_lookup_table,
)
