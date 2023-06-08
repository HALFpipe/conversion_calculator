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


# def test_convert_values():
#    from conversion_calculator import models
#
#    source_column = conversion_calculator.models.Column(
#        column_name="cvlt_ldfr_c", column_values=[10]
#    )
#    target_column = conversion_calculator.models.Column(column_name="ravlt_ldfr_c")
#    assert conversion_calculator.lib.convert_values(source_column, target_column) == [9]
