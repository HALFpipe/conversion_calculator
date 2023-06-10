import pytest
import io

import conversion_calculator


def test_get_csv_template_as_str():
    assert isinstance(conversion_calculator.lib.get_csv_template_as_str(), str)


def test_get_csv_template_as_io():
    assert isinstance(conversion_calculator.lib.get_csv_template_as_io(), io.StringIO)


def test_integer_check():
    assert conversion_calculator.lib.integer_check(5) == True
    assert conversion_calculator.lib.integer_check(5.0) == True
    assert conversion_calculator.lib.integer_check(5.1) == False


def test_convert_values_raises_with_empty_source_column():
    source_column = conversion_calculator.models.Column(column_name="cvlt_ldfr_c")
    target_column = conversion_calculator.models.Column(column_name="ravlt_ldfr_c")

    with pytest.raises(ValueError):
        conversion_calculator.lib.convert_values(source_column, target_column)


def test_convert_values_raises_with_nonempty_target_column():
    source_column = conversion_calculator.models.Column(
        column_name="cvlt_ldfr_c", column_values=[10]
    )
    target_column = conversion_calculator.models.Column(
        column_name="ravlt_ldfr_c", column_values=[10]
    )

    with pytest.raises(ValueError):
        conversion_calculator.lib.convert_values(source_column, target_column)


@pytest.mark.xfail()
def test_convert_values_raises_when_no_crosswalk_found():
    source_column = conversion_calculator.models.Column(
        column_name="cvlt_sdfr_c", column_values=[10]
    )
    target_column = conversion_calculator.models.Column(column_name="hvlt_ldfr_c")

    with pytest.raises(ValueError):
        conversion_calculator.lib.convert_values(source_column, target_column)
