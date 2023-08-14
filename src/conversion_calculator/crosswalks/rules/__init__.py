from models import Column, Crosswalk
from rule_engine import Rule


def check_instrument_match(crosswalk: Crosswalk, target_column: Column) -> bool:
    # instrument must match
    return crosswalk.instrument == target_column.instrument


def check_instrument_item_match(crosswalk: Crosswalk, target_column: Column) -> bool:
    # check if the source and target column have the same instrument item, or are both None
    if (crosswalk.instrument_item and target_column.instrument_item) and (
        (crosswalk.instrument_item == target_column.instrument_item)
        or (
            crosswalk.instrument_item.id in ["dr", "ldfr"]
            and target_column.instrument_item.id in ["dr", "ldfr"]
        )
    ):
        return True

    if (crosswalk.instrument_item is None) and (target_column.instrument_item is None):
        return True

    return False


def check_trial_match(crosswalk: Crosswalk, target_column: Column) -> bool:
    # check if the crosswalk and column have the same trial or are both None

    if (target_column.trial and crosswalk.trial) and (
        target_column.trial == crosswalk.trial
    ):
        return True

    if target_column.trial is None and crosswalk.trial is None:
        return True

    return False


def check_same_attributes_set(crosswalk: Crosswalk, target_column: Column) -> bool:
    # check if the crosswalk and column have the same attributes set
    # please note, this only checks that the 'truthyness' of the attributes are the same
    # checking that those attributes are the same values is done elsewhere
    same_attributes = []

    if (
        crosswalk.instrument_item is not None
        and target_column.instrument_item is not None
    ) or (crosswalk.instrument_item is None and target_column.instrument_item is None):
        same_attributes.append(True)

    if (crosswalk.trial is not None and target_column.trial is not None) or (
        crosswalk.trial is None and target_column.trial is None
    ):
        same_attributes.append(True)

    return all(same_attributes)


def check_for_valid_values(crosswalk: Crosswalk, target_column: Column) -> bool:
    if crosswalk.column_values is None or crosswalk.column_values.empty:
        return False

    if not target_column.column_values.isna().values.all():
        return False

    return True


def check_target_instrument_in_lookup_table(
    crosswalk: Crosswalk, target_column: Column
) -> bool:
    return target_column.instrument.id in crosswalk.column_order
