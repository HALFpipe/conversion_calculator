from conversion_calculator import crosswalks


def test_crosswalks():
    assert crosswalks.cvlt_ldfr.instrument.id == "cvlt"
