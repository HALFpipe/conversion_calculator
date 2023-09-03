import pandas as pd
import pytest
from pydantic import ValidationError

import conversion_calculator.models


@pytest.mark.parametrize(
    "id, friendly_name",
    [
        ("cvlt", "California Verbal Learning Test"),
        ("cvltc", "California Verbal Learning Test - Children's Version"),
        ("ravlt", "Rey Auditory Verbal Learning Test"),
        ("hvlt", "Hopkins Verbal Learning Test"),
        ("invalid_id", None),
        ("", None),
        (None, None),
    ],
)
def test_instrument(id, friendly_name):
    if id == "invalid_id" or id == "":
        with pytest.raises(ValueError):
            _ = conversion_calculator.models.Instrument(id=id)
    elif id == None:
        with pytest.raises(ValidationError):
            _ = conversion_calculator.models.Instrument(id=id)
    else:
        instrument = conversion_calculator.models.Instrument(id=id)
        assert instrument.id == id
        assert instrument.friendly_name == friendly_name


@pytest.mark.parametrize(
    "id, friendly_name",
    [
        ("dr", "Delayed Recall"),
        ("imfr", "Encoding"),
        ("ldcr", "Long-Delay Cued Recall"),
        ("ldfr", "Long-Delay Spontaneous Recall"),
        ("recog", "Recognition"),
        ("sdcr", "Short-Delay Cued Recall"),
        ("sdfr", "Short-Delay Spontaneous Recall"),
        ("invalid_id", None),
    ],
)
def test_instrument_item(id, friendly_name):
    if id == "invalid_id":
        with pytest.raises(ValueError):
            _ = conversion_calculator.models.InstrumentItem(id=id)
    else:
        instrument_item = conversion_calculator.models.InstrumentItem(id=id)
        assert instrument_item.id == id
        assert instrument_item.friendly_name == friendly_name


@pytest.mark.parametrize(
    "id, friendly_name",
    [
        ("form", "Form"),
        ("version", "Version"),
        ("invalid_id", None),
    ],
)
def test_instrument_metadata_type(id, friendly_name):
    if id == "invalid_id":
        with pytest.raises(ValueError):
            _ = conversion_calculator.models.InstrumentMetadataType(id=id)
    else:
        instrument_metadata_type = conversion_calculator.models.InstrumentMetadataType(
            id=id
        )
        assert instrument_metadata_type.id == id
        assert instrument_metadata_type.friendly_name == friendly_name


@pytest.mark.parametrize(
    "id, friendly_name",
    [
        ("t1", "Trial 1"),
        ("t2", "Trial 2"),
        ("t3", "Trial 3"),
        ("t4", "Trial 4"),
        ("t5", "Trial 5"),
        ("t15", "Trial 1-5"),
        ("tb", "Total"),
        ("invalid_id", None),
    ],
)
def test_trial(id, friendly_name):
    if id == "invalid_id":
        with pytest.raises(ValueError):
            _ = conversion_calculator.models.Trial(id=id)
    else:
        trial = conversion_calculator.models.Trial(id=id)
        assert trial.id == id
        assert trial.friendly_name == friendly_name


@pytest.mark.parametrize(
    "id, friendly_name",
    [
        ("total", "Total"),
        ("hits", "Hits"),
        ("c", "Cue"),
        ("i", "Intrusion"),
        ("invalid_id", None),
    ],
)
def test_valuetype(id, friendly_name):
    if id == "invalid_id":
        with pytest.raises(ValueError):
            _ = conversion_calculator.models.ValueType(id=id)
    else:
        valuetype = conversion_calculator.models.ValueType(id=id)
        assert valuetype.id == id
        assert valuetype.friendly_name == friendly_name


@pytest.mark.parametrize(
    "column_name, column_name_components",
    [
        ("cvlt_form", ["cvlt", "form"]),
        ("cvlt_imfr_t1_c", ["cvlt", "imfr", "t1", "c"]),
        ("cvlt_imfr_t2_c", ["cvlt", "imfr", "t2", "c"]),
        ("cvlt_imfr_t3_c", ["cvlt", "imfr", "t3", "c"]),
        ("cvlt_imfr_t4_c", ["cvlt", "imfr", "t4", "c"]),
        ("cvlt_imfr_t5_c", ["cvlt", "imfr", "t5", "c"]),
        ("cvlt_imfr_t15_total", ["cvlt", "imfr", "t15", "total"]),
        ("cvlt_imfr_b_c", ["cvlt", "imfr", "b", "c"]),
        ("cvlt_sdfr_c", ["cvlt", "sdfr", "c"]),
        ("cvlt_sdcr_c", ["cvlt", "sdcr", "c"]),
        ("cvlt_ldfr_c", ["cvlt", "ldfr", "c"]),
        ("cvlt_ldcr_c", ["cvlt", "ldcr", "c"]),
        ("cvlt_rep_total", ["cvlt", "rep", "total"]),
        ("cvlt_int_total", ["cvlt", "int", "total"]),
        ("cvlt_recog_hits", ["cvlt", "recog", "hits"]),
        ("cvlt_recog_fp", ["cvlt", "recog", "fp"]),
        ("cvltc_imfr_t1_c", ["cvltc", "imfr", "t1", "c"]),
        ("cvltc_imfr_t2_c", ["cvltc", "imfr", "t2", "c"]),
        ("cvltc_imfr_t3_c", ["cvltc", "imfr", "t3", "c"]),
        ("cvltc_imfr_t4_c", ["cvltc", "imfr", "t4", "c"]),
        ("cvltc_imfr_t5_c", ["cvltc", "imfr", "t5", "c"]),
        ("cvltc_imfr_t15_total", ["cvltc", "imfr", "t15", "total"]),
        ("cvltc_imfr_tb_c", ["cvltc", "imfr", "tb", "c"]),
        ("cvltc_sdfr_c", ["cvltc", "sdfr", "c"]),
        ("cvltc_sdcr_c", ["cvltc", "sdcr", "c"]),
        ("cvltc_ldfr_c", ["cvltc", "ldfr", "c"]),
        ("cvltc_ldcr_c", ["cvltc", "ldcr", "c"]),
        ("cvltc_recog_hits", ["cvltc", "recog", "hits"]),
        ("cvltc_recog_fp", ["cvltc", "recog", "fp"]),
        ("ravlt_form", ["ravlt", "form"]),
        ("ravlt_imfr_t1_c", ["ravlt", "imfr", "t1", "c"]),
        ("ravlt_imfr_t1_i", ["ravlt", "imfr", "t1", "i"]),
        ("ravlt_imfr_t2_c", ["ravlt", "imfr", "t2", "c"]),
        ("ravlt_imfr_t2_i", ["ravlt", "imfr", "t2", "i"]),
        ("ravlt_imfr_t3_c", ["ravlt", "imfr", "t3", "c"]),
        ("ravlt_imfr_t3_i", ["ravlt", "imfr", "t3", "i"]),
        ("ravlt_imfr_t4_c", ["ravlt", "imfr", "t4", "c"]),
        ("ravlt_imfr_t4_i", ["ravlt", "imfr", "t4", "i"]),
        ("ravlt_imfr_t5_c", ["ravlt", "imfr", "t5", "c"]),
        ("ravlt_imfr_t5_i", ["ravlt", "imfr", "t5", "i"]),
        ("ravlt_imfr_t15_total", ["ravlt", "imfr", "t15", "total"]),
        ("ravlt_imfr_b_c", ["ravlt", "imfr", "b", "c"]),
        ("ravlt_imfr_b_i", ["ravlt", "imfr", "b", "i"]),
        ("ravlt_sdfr_c", ["ravlt", "sdfr", "c"]),
        ("ravlt_sdfr_i", ["ravlt", "sdfr", "i"]),
        ("ravlt_ldfr_c", ["ravlt", "ldfr", "c"]),
        ("ravlt_ldfr_i", ["ravlt", "ldfr", "i"]),
        ("ravlt_recog_hits", ["ravlt", "recog", "hits"]),
        ("ravlt_recog_fp", ["ravlt", "recog", "fp"]),
        ("hvlt_version", ["hvlt", "version"]),
        ("hvlt_imfr_t1_c", ["hvlt", "imfr", "t1", "c"]),
        ("hvlt_imfr_t2_c", ["hvlt", "imfr", "t2", "c"]),
        ("hvlt_imfr_t3_c", ["hvlt", "imfr", "t3", "c"]),
        ("hvlt_imfr_t13_total", ["hvlt", "imfr", "t13", "total"]),
        ("hvlt_dr_c", ["hvlt", "dr", "c"]),
        ("hvlt_recog_hits", ["hvlt", "recog", "hits"]),
        ("hvlt_recog_fp", ["hvlt", "recog", "fp"]),
    ],
)
def test_in_scope_column_name(column_name, column_name_components):
    column = conversion_calculator.models.Column(column_name=column_name)
    assert column.column_name_components == column_name_components
    assert column.min_value == 0
    assert isinstance(column.max_value, int) or column.max_value is None


@pytest.mark.parametrize(
    "column_name",
    [
        "site",
        "subject_id",
        "clin_group",
        "tbi_status",
        "age",
        "sex",
        "gender",
        "raceUS",
        "ethUS",
        "raceINT",
        "edu",
        "parent_edu",
        "lang",
    ],
)
def test_out_of_scope_column_name(column_name):
    with pytest.raises(ValueError):
        column_name = conversion_calculator.models.Column(column_name=column_name)
        assert column_name.column_name_components == column_name_components


def test_can_create_column_with_list_column_values():
    default_column_name = "cvlt_sdfr_c"
    default_values = [0, 1, 2]
    column = conversion_calculator.models.Column(
        column_name=default_column_name,
        column_values=default_values,
    )
    assert column.column_name == default_column_name
    assert column.column_values.columns == [default_column_name]
    assert column.column_values.shape == (3, 1)
    assert (column.column_values.to_numpy().flatten() == default_values).all()


def test_can_create_column_with_pandas_column_values():
    default_column_name = "cvlt_sdfr_c"
    default_values = pd.DataFrame({default_column_name: [0, 1, 2]})
    column = conversion_calculator.models.Column(
        column_name=default_column_name,
        column_values=default_values,
    )
    assert column.column_name == default_column_name
    assert column.column_values.columns == [default_column_name]
    assert column.column_values.shape == (3, 1)
    assert column.column_values.compare(default_values).empty

    nan_at_the_end_column_name = "cvlt_sdfr_c"
    nan_at_the_end_values = pd.DataFrame({nan_at_the_end_column_name: [0, 1, 2, None]})
    column = conversion_calculator.models.Column(
        column_name=nan_at_the_end_column_name,
        column_values=nan_at_the_end_values,
    )
    assert column.column_name == nan_at_the_end_column_name
    assert column.column_values.columns == [nan_at_the_end_column_name]
    assert column.column_values.shape == (4, 1)
    assert column.column_values.compare(nan_at_the_end_values).empty


def test_can_not_create_column_with_bad_column_values():
    string_column_name = "cvlt_sdfr_c"
    string_values = pd.DataFrame({string_column_name: ["zero", "one", "two"]})
    with pytest.raises(ValueError):
        _ = conversion_calculator.models.Column(
            column_name=string_column_name,
            column_values=string_values,
        )

    leading_nan_column_name = "cvlt_sdfr_c"
    leading_nan_values = pd.DataFrame({string_column_name: [None, "one", "two"]})
    with pytest.raises(ValueError):
        _ = conversion_calculator.models.Column(
            column_name=leading_nan_column_name,
            column_values=leading_nan_values,
        )

    wide_column_name = "cvlt_sdfr_c"
    wide_values = pd.DataFrame(
        {string_column_name: [0, 1, 2], "other_column": [0, 1, 2]}
    )
    with pytest.raises(ValueError):
        _ = conversion_calculator.models.Column(
            column_name=wide_column_name,
            column_values=wide_values,
        )

    missing_column_name = "cvlt_sdfr_c"
    missing_column_name_values = pd.DataFrame([0, 1, 2])
    with pytest.raises(ValueError):
        _ = conversion_calculator.models.Column(
            column_name=missing_column_name,
            column_values=missing_column_name_values,
        )


def test_bounds_raise_with_min_lt_0():
    with pytest.raises(ValueError):
        _ = conversion_calculator.models.bounds.ValueBounds(min_value=-1, max_value=1)


def test_bounds_raise_with_max_eq_0():
    with pytest.raises(ValueError):
        _ = conversion_calculator.models.bounds.ValueBounds(min_value=0, max_value=0)


def test_bounds_raise_with_min_eq_max():
    with pytest.raises(ValueError):
        _ = conversion_calculator.models.bounds.ValueBounds(min_value=1, max_value=1)
