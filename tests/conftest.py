import pytest


instrument_names = ["cvlt", "cvltc", "ravlt", "hvlt"]

instrument_item_names = [
    "dr",
    "imfr",
    "ldcr",
    "ldfr",
    "recog",
    "sdcr",
    "sdfr",
    "rep",
    "int",
]

trial_names = [
    "t1",
    "t2",
    "t3",
    "t4",
    "t5",
    "t13",
    "t15",
    "tb",
    "b",
]

instrument_value_type_names = [
    "total",
    "hits",
    "c",
    "i",
    "fp",
]

instrument_metadata_types = [
    "form",
    "version",
]


@pytest.fixture
def five_value_column_name():
    return "this_is_not_a_realcolumnname"


@pytest.fixture
def one_component_column_name():
    return "subject"


@pytest.fixture
def all_two_component_column_names():
    names = []
    for instrument_name in instrument_names:
        for instrument_metadata_type in instrument_metadata_types:
            names.append(f"{instrument_name}_{instrument_metadata_type}")
    yield names


@pytest.fixture
def all_three_component_column_names():
    names = []
    for instrument_name in instrument_names:
        for instrument_item_name in instrument_item_names:
            for instrument_value_type_name in instrument_value_type_names:
                names.append(
                    f"{instrument_name}_{instrument_item_name}_{instrument_value_type_name}"
                )
    yield names


@pytest.fixture
def all_four_component_column_names():
    names = []
    for instrument_name in instrument_names:
        for instrument_item_name in instrument_item_names:
            for trial_name in trial_names:
                for instrument_value_type_name in instrument_value_type_names:
                    names.append(
                        f"{instrument_name}_{instrument_item_name}_{trial_name}_{instrument_value_type_name}"
                    )
    yield names
