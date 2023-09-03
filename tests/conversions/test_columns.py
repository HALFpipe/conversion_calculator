import pytest

from conversion_calculator.models import Column


def test_five_value_column_name(five_value_column_name):
    with pytest.raises(ValueError):
        _ = Column(column_name=five_value_column_name)


def test_one_component_column_name(one_component_column_name):
    with pytest.raises(ValueError):
        _ = Column(column_name=one_component_column_name)


def test_two_component_column_name(all_two_component_column_names):
    for column_name in all_two_component_column_names:
        column_name_components = column_name.split("_")
        column_under_test = Column(column_name=column_name)
        assert column_under_test.column_name == column_name
        assert column_under_test.instrument.id == column_name_components[0]
        assert (
            column_under_test.instrument_metadata_type.id == column_name_components[1]
        )


def test_three_component_column_name(all_three_component_column_names):
    for column_name in all_three_component_column_names:
        column_name_components = column_name.split("_")
        column_under_test = Column(column_name=column_name)
        assert column_under_test.column_name == column_name
        assert column_under_test.instrument_item.id == column_name_components[1]
        assert column_under_test.value_type.id == column_name_components[2]


def test_four_component_column_name(all_four_component_column_names):
    for column_name in all_four_component_column_names:
        column_name_components = column_name.split("_")
        column_under_test = Column(column_name=column_name)
        assert column_under_test.column_name == column_name
        assert column_under_test.instrument_item.id == column_name_components[1]
        assert column_under_test.trial.id == column_name_components[2]
        assert column_under_test.value_type.id == column_name_components[3]
