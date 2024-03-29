import numpy as np

from conversion_calculator.models import (CrossWalk, Instrument,
                                          InstrumentItem, ValueType, Trial)

instrument_cvlt = Instrument(id="cvlt")

instrument_item_imfr = InstrumentItem(id="imfr")

trial_t15 = Trial(id="t15")

value_type_total = ValueType(id="total")

cvlt_summary_column_order = {
    "cvlt": 0,
    "ravlt": 1,
    "hvlt": 2,
}

cvlt_summary_lookup_table = np.array(
    [
        [0, 0, 4],
        [1, 3, 6],
        [2, 4, 6],
        [3, 5, 6],
        [4, 6, 7],
        [5, 7, 7],
        [6, 8, 8],
        [7, 9, 8],
        [8, 10, 8],
        [9, 11, 9],
        [10, 12, 9],
        [11, 13, 9],
        [12, 14, 10],
        [13, 15, 10],
        [14, 16, 11],
        [15, 17, 11],
        [16, 18, 11],
        [17, 19, 12],
        [18, 20, 12],
        [19, 21, 13],
        [20, 22, 13],
        [21, 23, 13],
        [22, 24, 14],
        [23, 25, 14],
        [24, 26, 15],
        [25, 26, 15],
        [26, 27, 16],
        [27, 28, 16],
        [28, 29, 16],
        [29, 30, 17],
        [30, 31, 17],
        [31, 32, 18],
        [32, 33, 18],
        [33, 34, 19],
        [34, 34, 19],
        [35, 35, 19],
        [36, 36, 20],
        [37, 37, 20],
        [38, 38, 21],
        [39, 39, 21],
        [40, 40, 22],
        [41, 41, 22],
        [42, 42, 23],
        [43, 42, 23],
        [44, 44, 24],
        [45, 44, 24],
        [46, 45, 24],
        [47, 46, 25],
        [48, 47, 25],
        [49, 48, 26],
        [50, 49, 26],
        [51, 50, 27],
        [52, 51, 27],
        [53, 52, 28],
        [54, 53, 28],
        [55, 54, 28],
        [56, 54, 29],
        [57, 56, 29],
        [58, 56, 30],
        [59, 57, 30],
        [60, 58, 31],
        [61, 59, 31],
        [62, 60, 32],
        [63, 61, 32],
        [64, 62, 32],
        [65, 63, 33],
        [66, 64, 33],
        [67, 65, 34],
        [68, 66, 34],
        [69, 67, 34],
        [70, 68, 35],
        [71, 70, 35],
        [72, 71, 36],
        [73, 72, 36],
        [74, 73, 36],
        [75, 74, 36],
        [76, 75, 36],
        [77, 75, 36],
        [78, 75, 36],
        [79, 75, 36],
        [80, 75, 36],
    ]
)

cvlt_t15 = CrossWalk(
    instrument=instrument_cvlt,
    trial=trial_t15,
    column_order=cvlt_summary_column_order,
    lookup_table=cvlt_summary_lookup_table,
)

cvlt_imfr_t15_total = CrossWalk(
    instrument=instrument_cvlt,
    instrument_item=instrument_item_imfr,
    trial=trial_t15,
    value_type=value_type_total,
    column_order=cvlt_summary_column_order,
    lookup_table=cvlt_summary_lookup_table,
)
