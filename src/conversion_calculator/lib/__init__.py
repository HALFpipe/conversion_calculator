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
    crosswalk_to_target = None

    # the below is already complex enough that future work should implement a better solution.  Decision tree?

    # only search for a crosswalk if the source and target instrument items and trials are defined and the same
    common_fields = []
    if (source_column.instrument_item and target_column.instrument_item) and (
        source_column.instrument_item.id == target_column.instrument_item.id
    ):
        common_fields.append("instrument_item")

        if (source_column.trial and target_column.trial) and (
            source_column.trial.id == target_column.trial.id
        ):
            common_fields.append("trial")
        elif (source_column.trial and target_column.trial) and (
            source_column.trial.id != target_column.trial.id
        ):
            raise errors.CrossWalkNotFound()
        elif (source_column.trial or target_column.trial) and not (
            source_column.trial and target_column.trial
        ):
            raise errors.CrossWalkNotFound()

    elif (source_column.instrument_item and target_column.instrument_item) and (
        source_column.instrument_item.id != target_column.instrument_item.id
    ):
        raise errors.CrossWalkNotFound()

    elif (source_column.instrument_item or target_column.instrument_item) and not (
        source_column.instrument_item and target_column.instrument_item
    ):
        raise errors.CrossWalkNotFound()

    else:
        raise errors.CrossWalkNotFound()

    # if we've reached this point, we should spend the effort to find a crosswalk
    for candidate_crosswalk in [
        obj
        for _, obj in inspect.getmembers(crosswalks)
        if isinstance(obj, models.CrossWalk)
    ]:
        for field in common_fields:
            if (
                getattr(source_column, field).id
                != getattr(candidate_crosswalk, f"source_{field}").id
            ):
                break

        if (
            source_column.instrument.id == candidate_crosswalk.source_instrument.id
            and target_column.instrument.id in candidate_crosswalk.column_order
        ):
            if hasattr(source_column, "instrument_item") and hasattr(
                source_column, "instrument_trial"
            ):
                if (
                    source_column.instrument_trial.id
                    == candidate_crosswalk.source_instrument_trial.id
                ) and (
                    source_column.instrument_item.id
                    == candidate_crosswalk.source_instrument_item.id
                ):
                    crosswalk_to_target = candidate_crosswalk
                    break

                if (
                    source_column.instrument_trial.id
                    == candidate_crosswalk.source_instrument_trial.id
                ):
                    crosswalk_to_target = candidate_crosswalk
                    break

            if hasattr(source_column, "instrument_item") and not hasattr(
                source_column, "instrument_trial"
            ):
                if (
                    source_column.instrument_item.id
                    == candidate_crosswalk.source_instrument_item.id
                ):
                    crosswalk_to_target = candidate_crosswalk
                    break

            raise errors.CrossWalkNotFound()

    return crosswalk_to_target


def convert_all_values(
    source_column: models.Column, target_column: models.Column
) -> pd.DataFrame:
    """Given a source column, and a target column, return the converted value."""
    ...
    if source_column.column_values is None or source_column.column_values.empty:
        raise ValueError("Source column has no values.")

    if not target_column.column_values.isna().values.all():
        raise ValueError("Target column already has values.")

    if source_column == target_column:
        return source_column.column_values

    try:
        crosswalk_to_target = find_crosswalk(source_column, target_column)

    except errors.CrossWalkNotFound:
        raise ValueError("No crosswalk found for source column.")

    converted_column_values = []
    for source_value_index, source_value in enumerate(
        source_column.column_values[source_column.column_name]
    ):
        for crosswalk_index, crosswalk_row in enumerate(
            crosswalk_to_target.lookup_table
        ):
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
