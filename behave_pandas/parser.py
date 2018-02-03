import pandas as pd
import numpy as np
import dateutil.parser as dup
from behave_pandas.dtypes import VALID_BOOL_DTYPES, VALID_DTYPES, VALID_INT_DTYPES, VALID_FLOAT_DTYPES, \
    VALID_DATETIME_DTYPES, VALID_OBJECT_DTYPES


def get_column_index(column_rows):
    if len(column_rows) == 0:
        return []
    elif len(column_rows) == 1:
        return column_rows[0].cells
    else:
        levels = [pd.Index(row.cells) for row in column_rows]
        return pd.MultiIndex.from_arrays(levels)
    pass


def table_to_dataframe(table, column_levels=1, index_levels=0):
    dtypes = [VALID_DTYPES.get(dtype_name, None) for dtype_name in table.headings]

    columns = get_column_index(table.rows[:column_levels])

    data = []
    for row in table.rows[column_levels:]:
        data.append(_convert_to_correct_type(row, dtypes))

    bycol = list(zip(*data))

    series = [
        pd.Series(col_data, dtype=dtype, name=col_name) for (col_name, col_data, dtype) in
        zip(columns, bycol, dtypes)
    ]

    df = pd.concat(series, axis=1)

    if index_levels > 0:
        df.set_index(columns[:index_levels], inplace=True)

    return df


def _convert_to_correct_type(row, dtypes):
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
