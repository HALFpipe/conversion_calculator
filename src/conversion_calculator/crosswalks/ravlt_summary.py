import numpy as np

from conversion_calculator.models import (CrossWalk, Instrument,
                                          InstrumentItem, Trial, ValueType)

instrument_ravlt = Instrument(id="ravlt")

instrument_ravlt_item_immediate_recall = InstrumentItem(id="imfr")

trial_t15 = Trial(id="t15")

value_type_total = ValueType(id="total")

ravlt_summary_column_order = {
    "ravlt": 0,
    "havlt": 1,
    "cvlt": 2,
}

ravlt_summary_lookup_table = np.array(
    [
        [0, 4, 0],
        [1, 5, 0],
        [2, 5, 0],
        [3, 6, 1],
        [4, 6, 2],
        [5, 6, 3],
        [6, 7, 4],
        [7, 7, 5],
        [8, 7, 6],
        [9, 8, 7],
        [10, 8, 8],
        [11, 8, 9],
        [12, 9, 10],
        [13, 9, 11],
        [14, 10, 12],
        [15, 10, 13],
        [16, 10, 14],
        [17, 11, 15],
        [18, 11, 16],
        [19, 12, 17],
        [20, 12, 18],
        [21, 13, 19],
        [22, 13, 20],
        [23, 14, 21],
        [24, 14, 22],
        [25, 14, 23],
        [26, 15, 25],
        [27, 15, 26],
        [28, 16, 27],
        [29, 16, 28],
        [30, 17, 29],
        [31, 17, 30],
        [32, 18, 31],
        [33, 18, 32],
        [34, 19, 34],
        [35, 19, 35],
        [36, 20, 36],
        [37, 20, 37],
        [38, 21, 38],
        [39, 21, 39],
        [40, 22, 40],
        [41, 22, 41],
        [42, 23, 42],
        [43, 23, 44],
        [44, 24, 45],
        [45, 24, 46],
        [46, 25, 47],
        [47, 25, 48],
        [48, 26, 49],
        [49, 26, 50],
        [50, 27, 51],
        [51, 27, 52],
        [52, 28, 53],
        [53, 28, 54],
        [54, 29, 55],
        [55, 29, 56],
        [56, 30, 58],
        [57, 30, 59],
        [58, 30, 60],
        [59, 31, 61],
        [60, 31, 62],
        [61, 32, 63],
        [62, 32, 64],
        [63, 33, 65],
        [64, 33, 66],
        [65, 34, 67],
        [66, 34, 68],
        [67, 34, 68],
        [68, 35, 70],
        [69, 35, 70],
        [70, 36, 72],
        [71, 36, 72],
        [72, 36, 73],
        [73, 36, 74],
        [74, 36, 75],
        [75, 36, 76],
    ]
)

ravlt_t15 = CrossWalk(
    instrument=instrument_ravlt,
    trial=trial_t15,
    column_order=ravlt_summary_column_order,
    lookup_table=ravlt_summary_lookup_table,
)

ravlt_imfr_t15_total = CrossWalk(
    instrument=instrument_ravlt,
    instrument_item=instrument_ravlt_item_immediate_recall,
    trial=trial_t15,
    value_type=value_type_total,
    column_order=ravlt_summary_column_order,
    lookup_table=ravlt_summary_lookup_table,
)
