import numpy as np

from conversion_calculator.models import CrossWalk, Instrument, InstrumentItem, Trial

instrument_cvlt = Instrument(id="cvlt")
instrument_hvlt = Instrument(id="hvlt")
instrument_ravlt = Instrument(id="ravlt")

instrument_item_ldfr = InstrumentItem(id="ldfr")
instrument_item_sdfr = InstrumentItem(id="sdfr")

instrument_trial_t1 = Trial(id="t1")
instrument_trial_t15 = Trial(id="t15")

cvlt_ldrf = CrossWalk(
    source_instrument=instrument_cvlt,
    source_instrument_item=instrument_item_ldfr,
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

cvlt_sdfr = CrossWalk(
    source_instrument=instrument_cvlt,
    source_instrument_item=instrument_item_sdfr,
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

cvlt_t1 = CrossWalk(
    source_instrument=instrument_cvlt,
    source_trial=instrument_trial_t1,
    column_order={
        "cvlt": 0,
        "ravlt": 1,
        "hvlt": 2,
    },
    lookup_table=np.array(
        [
            [0, 0, 0],
            [1, 0, 3],
            [2, 1, 4],
            [3, 3, 4],
            [4, 4, 5],
            [5, 5, 6],
            [6, 6, 7],
            [7, 7, 8],
            [8, 8, 9],
            [9, 9, 10],
            [10, 11, 10],
            [11, 12, 11],
            [12, 14, 12],
            [13, 15, 12],
            [14, 15, 12],
            [15, 15, 12],
            [16, 15, 12],
        ]
    ),
)

cvlt_t15 = CrossWalk(
    source_instrument=instrument_cvlt,
    source_trial=instrument_trial_t15,
    column_order={
        "cvlt": 0,
        "ravlt": 1,
        "hvlt": 2,
    },
    lookup_table=np.array(
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
    ),
)

hvlt_ldfr = CrossWalk(
    source_instrument=instrument_hvlt,
    source_instrument_item=instrument_item_ldfr,
    column_order={
        "hvlt": 0,
        "cvlt": 1,
        "ravlt": 2,
    },
    lookup_table=np.array(
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
        ]
    ),
)

hvlt_t1 = CrossWalk(
    source_instrument=instrument_hvlt,
    source_trial=instrument_trial_t1,
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

hvlt_t15 = CrossWalk(
    source_instrument=instrument_hvlt,
    source_trial=instrument_trial_t15,
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

ravlt_ldfr = CrossWalk(
    source_instrument=instrument_ravlt,
    source_instrument_item=instrument_item_ldfr,
    column_order={
        "ravlt": 0,
        "havlt": 1,
        "cvlt": 2,
    },
    lookup_table=np.array(
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
    ),
)

ravlt_sdfr = CrossWalk(
    source_instrument=instrument_ravlt,
    source_instrument_item=instrument_item_sdfr,
    column_order={
        "ravlt": 0,
        "cvlt": 1,
    },
    lookup_table=np.array(
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
    ),
)

ravlt_t1 = CrossWalk(
    source_instrument=instrument_ravlt,
    source_trial=instrument_trial_t1,
    column_order={
        "ravlt": 0,
        "havlt": 1,
        "cvlt": 2,
    },
    lookup_table=np.array(
        [
            [0, 0, 0],
            [1, 3, 2],
            [2, 4, 2],
            [3, 4, 3],
            [4, 5, 4],
            [5, 6, 5],
            [6, 7, 6],
            [7, 8, 7],
            [8, 8, 8],
            [9, 9, 8],
            [10, 10, 9],
            [11, 11, 10],
            [12, 12, 11],
            [13, 12, 12],
            [14, 12, 12],
            [15, 12, 12],
        ]
    ),
)

ravlt_t15 = CrossWalk(
    source_instrument=instrument_ravlt,
    source_trial=instrument_trial_t15,
    column_order={
        "ravlt": 0,
        "havlt": 1,
        "cvlt": 2,
    },
    lookup_table=np.array(
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
    ),
)
