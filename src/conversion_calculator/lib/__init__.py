import importlib.resources as pkg_resources
import inspect
import io
from itertools import permutations
from typing import List, Union

import numpy as np
import pandas as pd
from pydantic import ValidationError

from conversion_calculator import crosswalks, errors, models


def get_csv_template_path() -> str:
    return str(
        pkg_resources.files("conversion_calculator").joinpath(
            "static", "verbal-learning-template.csv"
        )
    )


def get_csv_template_as_str() -> str:
    """Return the CSV template as a string."""
    template_csv_path = get_csv_template_path()
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


def dataframe_to_csv(dataframe: pd.DataFrame) -> str:
    """Convert a pandas DataFrame to a CSV string."""
    return dataframe.to_csv(index=False)


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


def find_crosswalk(
    source_column: models.Column, target_column: models.Column
) -> models.CrossWalk:
    crosswalk_to_target = []

    for candidate_crosswalk in [
        obj
        for _, obj in inspect.getmembers(crosswalks)
        if isinstance(obj, models.CrossWalk)
    ]:
        if candidate_crosswalk.walk_possible(source_column, target_column):
            crosswalk_to_target.append(candidate_crosswalk)

    if len(crosswalk_to_target) == 1:
        return crosswalk_to_target[0]

    elif len(crosswalk_to_target) > 1:
        # if we see this, we've included a bad crosswalk in this module
        raise errors.MultipleCrossWalksFound()

    else:
        raise errors.CrossWalkNotFound()


def convert_all_values(
    source_column: models.Column, target_column: models.Column
) -> pd.DataFrame:
    """Given a source column, and a target column, return the converted value."""
    if source_column.column_name == target_column.column_name:
        return source_column.column_values

    try:
        crosswalk_to_target = find_crosswalk(source_column, target_column)
    except errors.CrossWalkNotFound:
        raise ValueError("No crosswalk found for source column.")

    converted_column_values = []
    for _, source_value in enumerate(
        source_column.column_values[source_column.column_name]
    ):
        for _, crosswalk_row in enumerate(crosswalk_to_target.lookup_table):
            if (
                crosswalk_row[
                    crosswalk_to_target.column_order[source_column.instrument.id]
                ]
                == source_value
            ):
                converted_column_values.append(
                    crosswalk_row[
                        crosswalk_to_target.column_order[target_column.instrument.id]
                    ]
                )
                break

    return pd.DataFrame({target_column.column_name: converted_column_values})


def convert_spreadsheet(input_data: pd.DataFrame) -> pd.DataFrame:
    valid_columns = []
    for column in input_data.columns:
        try:
            valid_columns.append(
                models.Column(column_name=column, column_values=input_data[column])
            )
        except ValidationError:
            # this is how we ignore columns that don't validate
            # when we have more error conditions than just Valid or Not, add them here so we can tell users what's wrong
            pass

    if valid_columns == []:
        raise ValueError("No valid columns found in input data.")

    for source_column, target_column in permutations(valid_columns, 2):
        try:
            input_data[target_column.column_name] = convert_all_values(
                source_column, target_column
            ).values
        except ValueError as e:
            print(
                f"Error converting {source_column.column_name} to {target_column.column_name}: {e}"
            )
            pass

    return input_data
