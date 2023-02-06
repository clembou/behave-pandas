from typing import Iterable

import pandas as pd
from behave_pandas.column_types import (
    VALID_COLUMN_TYPES,
    ColumnParser,
)


def _get_column_index(column_rows, nb_cols):
    if len(column_rows) == 0:
        return range(nb_cols)
    elif len(column_rows) == 1:
        return column_rows[0].cells
    else:
        return list(zip(*[row.cells for row in column_rows]))
    pass


def table_to_dataframe(
    table, column_levels=1, index_levels=0, collapse_empty_index_levels=True
):
    """
    Given a behave table, convert it to a pandas data frame using the following rules:
    - valid column types must be specified in the table heading
    - 0 or more rows can be used to label columns (a multi index will be created if column_levels > 1)
    - 0 or more columns can be used to label columns (a multi index will be created if index_levels > 1)
    - For tables with multi indexed columns, row index level names will be flattened to a string by default
    instead of a tuple if needed, unless `collapse_empty_index_levels` is set to False.

    :param table: behave.Table
    :param column_levels: int
    :param index_levels: int
    :param collapse_empty_index_levels: bool
    :return: pd.DataFrame
    """
    if (not isinstance(column_levels, int)) or not (
        0 <= column_levels <= len(table.rows)
    ):
        raise ValueError(
            "Invalid number of column levels requested. "
            "Max valid number for this table: {}".format(len(table.rows))
        )

    if (not isinstance(index_levels, int)) or not (
        0 <= index_levels <= len(table.headings)
    ):
        raise ValueError(
            "Invalid number of column levels requested. "
            "Max valid number for this table: {}".format(len(table.headings))
        )

    column_types = _get_column_types(table.headings)
    columns = _get_column_index(table.rows[:column_levels], len(table.headings))

    data = [
        _convert_row_to_correct_type(row, column_types)
        for row in table.rows[column_levels:]
    ]

    bycol = list(zip(*data))
    if len(bycol) == 0:
        bycol = [None for col in columns]

    series = [
        pd.Series(col_data, name=col_name).astype(column_type.pandas_dtype_name, errors='raise')
        for (col_name, col_data, column_type) in zip(columns, bycol, column_types)
    ]

    df = pd.concat(series, axis=1)

    if index_levels > 0:
        index_cols = columns[:index_levels]
        df.set_index(index_cols, inplace=True)
        df.index.names = _flatten_index_names_if_needed(
            collapse_empty_index_levels, column_levels, index_cols
        )

    return df


def _flatten_index_names_if_needed(
    collapse_empty_index_levels, column_levels, index_cols
):
    if collapse_empty_index_levels and column_levels > 1:
        index_cols = [
            tuple(v for v in index_col if v != "") for index_col in index_cols
        ]
        index_cols = [tup[0] if len(tup) == 1 else tup for tup in index_cols]
    return index_cols


def _get_column_types(headings):
    invalid_column_type = [
        column_type for column_type in headings if column_type not in VALID_COLUMN_TYPES
    ]

    if len(invalid_column_type) > 0:
        raise TypeError(
            "Invalid column type(s) detected in the table headings: {}. "
            "Valid values are:\n{} ".format(
                ", ".join(invalid_column_type), ", ".join(VALID_COLUMN_TYPES)
            )
        )

    return [VALID_COLUMN_TYPES[column_type_name] for column_type_name in headings]


def _convert_row_to_correct_type(row, column_types: Iterable[ColumnParser]):
    as_correct_type = []

    for col_index, cell in enumerate(row.cells):
        parser = column_types[col_index]
        as_correct_type.append(parser.parse_value(cell))

    return as_correct_type
