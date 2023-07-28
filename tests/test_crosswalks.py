from conversion_calculator import crosswalks


def test_crosswalks():
    assert crosswalks.cvlt_ldrf.instrument.id == "cvlt"
