import pandas as pd
import numpy as np
import dateutil.parser as dup
from behave_pandas.dtypes import VALID_BOOL_DTYPES, VALID_DTYPES, VALID_INT_DTYPES, VALID_FLOAT_DTYPES, \
    VALID_DATETIME_DTYPES, VALID_OBJECT_DTYPES


def _get_column_index(column_rows, nb_cols):
    if len(column_rows) == 0:
        return range(nb_cols)
    elif len(column_rows) == 1:
        return column_rows[0].cells
    else:
        levels = [pd.Index(row.cells) for row in column_rows]
        return pd.MultiIndex.from_arrays(levels)
    pass


def table_to_dataframe(table, column_levels=1, index_levels=0):
    dtypes = _get_dtypes(table.headings)
    columns = _get_column_index(table.rows[:column_levels], len(table.headings))

    data = [_convert_row_to_correct_type(row, dtypes) for row in table.rows[column_levels:]]

    bycol = list(zip(*data))

    series = [
        pd.Series(col_data, dtype=dtype, name=col_name) for (col_name, col_data, dtype) in
        zip(columns, bycol, dtypes)
    ]

    df = pd.concat(series, axis=1)

    if index_levels > 0:
        df.set_index(columns[:index_levels], inplace=True)

    return df


def _get_dtypes(headings):
    invalid_dtypes = [dtype for dtype in headings if dtype not in VALID_DTYPES]

    if len(invalid_dtypes) > 0:
        raise TypeError('Invalid dtype(s) detected: {}. '
                        'Valid values are:\n{} '.format(', '.join(invalid_dtypes), ', '.join(VALID_DTYPES)))

    return [VALID_DTYPES[dtype_name] for dtype_name in headings]


def _convert_row_to_correct_type(row, dtypes):
    as_correct_type = []

    for col_index, cell in enumerate(row.cells):
        if dtypes[col_index] in VALID_BOOL_DTYPES.values():
            as_correct_type.append(dtypes[col_index](cell))
        elif dtypes[col_index] in VALID_INT_DTYPES.values():
            as_correct_type.append(dtypes[col_index](cell))
        elif dtypes[col_index] in VALID_FLOAT_DTYPES.values():
            as_correct_type.append(dtypes[col_index](cell))
        elif dtypes[col_index] in VALID_DATETIME_DTYPES.values():
            as_correct_type.append(dtypes[col_index](cell))
        elif dtypes[col_index] in VALID_OBJECT_DTYPES.values():
            as_correct_type.append(cell)
        else:
            raise Exception(
                'Unable to convert table element {}. \n'
                'Check if the gherkin to pandas dataframe converter '
                'handles {}'.format(cell, dtypes[col_index])
            )

    return as_correct_type
