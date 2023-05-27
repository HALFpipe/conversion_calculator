import io
from conversion_calculator.lib import (
    integer_check,
    get_csv_template_as_io,
    get_csv_template_as_str,
)


def test_get_csv_template_as_str():
    assert isinstance(get_csv_template_as_str(), str)


def test_get_csv_template_as_io():
    assert isinstance(get_csv_template_as_io(), io.StringIO)


def test_integer_check():
    assert integer_check(5) == True
    assert integer_check(5.0) == True
    assert integer_check(5.1) == False
