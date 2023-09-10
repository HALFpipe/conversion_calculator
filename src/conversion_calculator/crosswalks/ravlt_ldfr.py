import numpy as np

from conversion_calculator.models import CrossWalk, Instrument, InstrumentItem, ValueType

instrument_ravlt = Instrument(id="ravlt")

instrument_item_ldfr = InstrumentItem(id="ldfr")

c_value_type = ValueType(id="c")
i_value_type = ValueType(id="i")

ravlt_ldfr_column_order = {"ravlt": 0, "havlt": 1, "cvlt": 2}
ravlt_ldfr_lookup_table = np.array(
    [
        [0, 0, 0],
        [1, 2, 0],
        [2, 3, 1],
        [3, 4, 2],
        [4, 4, 4],
        [5, 5, 5],
        [6, 6, 6],
        [7, 7, 7],
        [8, 7, 9],
        [9, 8, 10],
        [10, 9, 11],
        [11, 10, 12],
        [12, 10, 14],
        [13, 11, 15],
        [14, 12, 16],
        [15, 12, 16],
    ]
)

ravlt_ldfr = CrossWalk(
    instrument=instrument_ravlt,
    instrument_item=instrument_item_ldfr,
    column_order=ravlt_ldfr_column_order,
    lookup_table=ravlt_ldfr_lookup_table,
)

ravlt_ldfr_c = CrossWalk(
    instrument=instrument_ravlt,
    instrument_item=instrument_item_ldfr,
    value_type = c_value_type,
    column_order=ravlt_ldfr_column_order,
    lookup_table=ravlt_ldfr_lookup_table,
)

ravlt_ldfr_i = CrossWalk(
    instrument=instrument_ravlt,
    instrument_item=instrument_item_ldfr,
    value_type = i_value_type,
    column_order=ravlt_ldfr_column_order,
    lookup_table=ravlt_ldfr_lookup_table,
)