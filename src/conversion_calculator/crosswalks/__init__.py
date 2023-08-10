import numpy as np

from conversion_calculator.models import CrossWalk, Instrument, InstrumentItem, Trial

from .cvlt_ldrf import cvlt_ldrf
from .cvlt_sdrf import cvlt_sdfr
from .cvlt_t1 import cvlt_t1
from .cvlt_t15 import cvlt_t15
from .hvlt_ldfr import hvlt_ldfr
from .hvlt_t1 import hvlt_t1
from .hvlt_t15 import hvlt_t15
from .ravlt_ldfr import ravlt_ldfr
from .ravlt_sdfr import ravlt_sdfr
from .ravlt_t1 import ravlt_t1
from .ravlt_t15 import ravlt_t15

instrument_cvlt = Instrument(id="cvlt")
instrument_hvlt = Instrument(id="hvlt")
instrument_ravlt = Instrument(id="ravlt")

instrument_item_ldfr = InstrumentItem(id="ldfr")
instrument_item_sdfr = InstrumentItem(id="sdfr")

instrument_trial_t1 = Trial(id="t1")
instrument_trial_t15 = Trial(id="t15")

__all__ = [
    "cvlt_ldrf",
    "cvlt_sdfr",
    "cvlt_t1",
    "cvlt_t15",
    "hvlt_ldfr",
    "hvlt_t1",
    "hvlt_t15",
    "ravlt_ldfr",
    "ravlt_sdfr",
    "ravlt_t1",
    "ravlt_t15",
]
