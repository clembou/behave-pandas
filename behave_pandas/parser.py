import pandas as pd
import numpy as np
from behave_pandas.dtypes import VALID_BOOL_DTYPES, VALID_DTYPES, VALID_INT_DTYPES, VALID_FLOAT_DTYPES, \
    VALID_DATETIME_DTYPES, VALID_OBJECT_DTYPES


def _get_column_index(column_rows, nb_cols):
    if len(column_rows) == 0:
        return range(nb_cols)
    elif len(column_rows) == 1:
        return column_rows[0].cells
    else:
        return list(zip(*[row.cells for row in column_rows]))
    pass


def table_to_dataframe(table, column_levels=1, index_levels=0, collapse_empty_index_levels=True):
    """
    Given a behave table, convert it to a pandas data frame using the following rules:
    - valid dtypes must be specified in the table heading
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
    if (not isinstance(column_levels, int)) or not (0 <= column_levels <= len(table.rows)):
        raise ValueError('Invalid number of column levels requested. '
                         'Max valid number for this table: {}'.format(len(table.rows)))

    if not isinstance(index_levels, int) or not (0 <= index_levels <= len(table.headings)):
        raise ValueError('Invalid number of column levels requested. '
                         'Max valid number for this table: {}'.format(len(table.headings)))

    dtypes = _get_dtypes(table.headings)
    columns = _get_column_index(table.rows[:column_levels], len(table.headings))

    data = [_convert_row_to_correct_type(row, dtypes) for row in table.rows[column_levels:]]

    bycol = list(zip(*data))
    if len(bycol) == 0:
        bycol = [None for col in columns]

    series = [
        pd.Series(col_data, dtype=dtype, name=col_name) for (col_name, col_data, dtype) in
        zip(columns, bycol, dtypes)
    ]

    df = pd.concat(series, axis=1)

    if index_levels > 0:
        index_cols = columns[:index_levels]
        df.set_index(index_cols, inplace=True)
        df.index.names = _flatten_index_names_if_needed(collapse_empty_index_levels, column_levels, index_cols)

    return df


def _flatten_index_names_if_needed(collapse_empty_index_levels, column_levels, index_cols):
    if collapse_empty_index_levels and column_levels > 1:
        index_cols = [tuple(v for v in index_col if v != '') for index_col in index_cols]
        index_cols = [tup[0] if len(tup) == 1 else tup for tup in index_cols]
    return index_cols


def _get_dtypes(headings):
    invalid_dtypes = [dtype for dtype in headings if dtype not in VALID_DTYPES]

    if len(invalid_dtypes) > 0:
        raise TypeError('Invalid dtype(s) detected in the table headings: {}. '
                        'Valid values are:\n{} '.format(', '.join(invalid_dtypes), ', '.join(VALID_DTYPES)))

    return [VALID_DTYPES[dtype_name] for dtype_name in headings]


def _convert_row_to_correct_type(row, dtypes):
    as_correct_type = []

    for col_index, cell in enumerate(row.cells):
        if dtypes[col_index] in VALID_BOOL_DTYPES.values():
            as_correct_type.append(parse_bool(cell, col_index, dtypes[col_index]))
        elif dtypes[col_index] in VALID_INT_DTYPES.values():
            as_correct_type.append(parse_integer(cell, col_index, dtypes[col_index]))
        elif dtypes[col_index] in VALID_FLOAT_DTYPES.values():
            as_correct_type.append(parse_dtype(cell, col_index, dtypes[col_index]))
        elif dtypes[col_index] in VALID_DATETIME_DTYPES.values():
            as_correct_type.append(parse_dtype(cell, col_index, dtypes[col_index]))
        elif dtypes[col_index] in VALID_OBJECT_DTYPES.values():
            as_correct_type.append(parse_string(cell))
        else:
            raise Exception(
                'Unable to convert table element {} on column {}. \n'
                'Check if the gherkin to pandas dataframe converter '
                'handles {}'.format(cell, col_index, dtypes[col_index])
            )

    return as_correct_type


def parse_bool(cell, col_index, dtype):
    if cell.lower() == 'true':
        return True
    elif cell.lower() == 'false':
        return False
    elif cell == '':
        raise ValueError('null values are not supported for boolean columns. '
                         'Check column at index {}'.format(col_index))
    else:
        raise ValueError('{} cannot be parsed as a {}'.format(cell, dtype))


def parse_integer(cell, col_index, dtype):
    if cell == '':
        raise ValueError('null values are not supported for integer columns. '
                         'Check column at index {}'.format(col_index))
    else:
        return dtype(cell)


def parse_dtype(cell, col_index, dtype):
    if cell == '':
        return np.nan
    else:
        return dtype(cell)


def parse_string(cell):
    if cell == '':
        return np.nan
    elif cell == '""':
        return ''
    else:
        return cell
