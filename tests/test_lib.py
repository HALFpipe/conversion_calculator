import io

import numpy as np
import pytest

import conversion_calculator


def test_get_csv_template_as_str():
    assert isinstance(conversion_calculator.lib.get_csv_template_as_str(), str)


def test_get_csv_template_as_io():
    assert isinstance(conversion_calculator.lib.get_csv_template_as_io(), io.StringIO)


def test_integer_check():
    assert conversion_calculator.lib.integer_check(5) == True
    assert conversion_calculator.lib.integer_check(5.0) == True
    assert conversion_calculator.lib.integer_check(5.1) == False


def test_convert_all_values_raises_with_empty_source_column():
    source_column = conversion_calculator.models.Column(column_name="cvlt_ldfr_c")
    target_column = conversion_calculator.models.Column(column_name="ravlt_ldfr_c")

    with pytest.raises(ValueError):
        conversion_calculator.lib.convert_all_values(source_column, target_column)


def test_convert_all_values_raises_with_nonempty_target_column():
    source_column = conversion_calculator.models.Column(
        column_name="cvlt_ldfr_c", column_values=[10]
    )
    target_column = conversion_calculator.models.Column(
        column_name="ravlt_ldfr_c", column_values=[10]
    )

    with pytest.raises(ValueError):
        conversion_calculator.lib.convert_all_values(source_column, target_column)


def test_find_crosswalk_when_columns_are_compatible():
    source_column = conversion_calculator.models.Column(
        column_name="cvlt_ldfr_c", column_values=[10]
    )
    target_column = conversion_calculator.models.Column(column_name="hvlt_ldfr_c")
    assert (
        conversion_calculator.lib.find_crosswalk(source_column, target_column)
        == conversion_calculator.crosswalks.cvlt_ldrf
    )


def test_convert_all_values_raises_when_no_crosswalk_found():
    source_column = conversion_calculator.models.Column(
        column_name="cvlt_sdfr_c", column_values=[10]
    )
    target_column = conversion_calculator.models.Column(column_name="hvlt_ldfr_c")

    with pytest.raises(ValueError):
        conversion_calculator.lib.convert_all_values(source_column, target_column)


def test_convert_all_values_can_crosswalk_columns():
    source_column = conversion_calculator.models.Column(
        column_name="cvlt_ldfr_c", column_values=[10]
    )
    target_column = conversion_calculator.models.Column(column_name="hvlt_ldfr_c")
    test_values = conversion_calculator.lib.convert_all_values(
        source_column, target_column
    )
    assert np.all(test_values.values.flatten() == np.array([8]))


def test_find_crosswalk_raises_when_instrument_items_are_not_the_same():
    with pytest.raises(conversion_calculator.errors.CrossWalkNotFound):
        conversion_calculator.lib.find_crosswalk(
            conversion_calculator.models.Column(column_name="cvlt_ldfr_t1_c"),
            conversion_calculator.models.Column(column_name="ravlt_sdfr_t1_c"),
        )

    with pytest.raises(conversion_calculator.errors.CrossWalkNotFound):
        conversion_calculator.lib.find_crosswalk(
            conversion_calculator.models.Column(column_name="cvlt_ldfr_c"),
            conversion_calculator.models.Column(column_name="ravlt_sdfr_c"),
        )

    with pytest.raises(conversion_calculator.errors.CrossWalkNotFound):
        conversion_calculator.lib.find_crosswalk(
            conversion_calculator.models.Column(column_name="cvlt_ldfr_t3_c"),
            conversion_calculator.models.Column(column_name="ravlt_sdfr_c"),
        )


def test_find_crosswalk_raises_when_instrument_items_are_the_same_but_trials_are_different():
    with pytest.raises(conversion_calculator.errors.CrossWalkNotFound):
        conversion_calculator.lib.find_crosswalk(
            conversion_calculator.models.Column(column_name="cvlt_ldfr_t3_c"),
            conversion_calculator.models.Column(column_name="ravlt_ldfr_t1_c"),
        )

    with pytest.raises(conversion_calculator.errors.CrossWalkNotFound):
        conversion_calculator.lib.find_crosswalk(
            conversion_calculator.models.Column(column_name="cvlt_ldfr_c"),
            conversion_calculator.models.Column(column_name="ravlt_ldfr_t1_c"),
        )
