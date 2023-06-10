import importlib.resources as pkg_resources
import inspect
import io
from typing import List, Union

import pandas as pd

from conversion_calculator import crosswalks, models, errors


def get_csv_template_as_str() -> str:
    """Return the CSV template as a string."""
    template_csv_path = str(
        pkg_resources.files("conversion_calculator").joinpath(
            "static", "verbal-learning-template.csv"
        )
    )
    with open(template_csv_path, "r") as f:
        csv_template = f.read()
    return csv_template


def get_csv_template_as_io() -> io.StringIO:
    """Return the CSV template as a StringIO object."""
    csv_template = get_csv_template_as_str()
    return io.StringIO(csv_template)


def parse_input_csv(input: str) -> pd.DataFrame:
    """Parse the input CSV into a pandas DataFrame."""
    return pd.read_csv(input, on_bad_lines="error")


def integer_check(input: Union[int, float]) -> bool:
    """Check if the input is an integer."""
    if isinstance(input, int):
        return True
    if isinstance(input, float):
        try:
            if int(input) == input:
                return True
            else:
                return False
        except ValueError:
            return False
    return False


def find_crosswalk(source_column: models.Column, target_column: models.Column) -> models.CrossWalk:
    crosswalk_to_target = None
    for candidate_crosswalk in [
        obj
        for _, obj in inspect.getmembers(crosswalks)
        if isinstance(obj, models.CrossWalk)
    ]:
        if source_column.instrument == candidate_crosswalk.source_instrument and (
            source_column.instrument_item == candidate_crosswalk.source_instrument_item
            or source_column.trial == candidate_crosswalk.source_trial
        ):
            crosswalk_to_target = candidate_crosswalk
            break 

    if crosswalk_to_target is None:
        raise errors.CrossWalkNotFound("No crosswalk found for source column to target column.")

    return crosswalk_to_target



def convert_values(
    source_column: models.Column, target_column: models.Column
) -> pd.DataFrame:
    """Given a source column, and a target column, return the converted value."""
    ...
    if source_column.column_values is None or source_column.column_values.empty:
        raise ValueError("Source column has no values.")

    if target_column.column_values is not None and not target_column.column_values.empty:
        raise ValueError("Target column already has values.")

    if source_column == target_column:
        return source_column.column_values

    try:
        crosswalk_to_target = find_crosswalk(source_column, target_column)

    except errors.CrossWalkNotFound:
        raise ValueError("No crosswalk found for source column.")

    converted_column_values = []
    for column_value in source_column.column_values:
        target_row = crosswalk_to_target.lookup_table[
            crosswalk_to_target.lookup_table[
                :, crosswalk_to_target.column_order[source_column.instrument.id]
            ]
            == column_value
        ].flatten()
        converted_column_values.append(
            target_row[crosswalk_to_target.column_order[target_column.instrument.id]]
        )

    return converted_column_values
