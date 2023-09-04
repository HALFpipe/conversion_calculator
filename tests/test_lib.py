import io
import random

import numpy as np
import pytest

import conversion_calculator
from conversion_calculator.models.bounds import max_values, min_values
from conversion_calculator.models.column import Column


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
        == conversion_calculator.crosswalks.cvlt_ldfr_c
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


def dummy_column_factory(column_name: str):
    """ when given a column name, will return a Column object with dummy values between the min and max values for that column """

    try:
        min_val = min_values.get(column_name, 0)
        max_val = max_values[column_name]

    except KeyError:
        raise ValueError("Invalid column name")
    
    dummy_values = []
    for _ in range(0,14):
        dummy_values.append(random.randint(min_val, max_val)) 

    return Column(column_name=column_name, column_values=dummy_values)
