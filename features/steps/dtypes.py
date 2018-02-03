import datetime
from behave import *
from behave_pandas import table_to_dataframe

import pandas as pd
import pandas.testing as pdt
import numpy as np

use_step_matcher("parse")


@given('a gherkin table as input')
def step_impl(context, ):
    context.input = context.table


@when('converted to a data frame using {column_levels:d} row as column names and {index_levels:d} column as index')
def step_impl(context, column_levels, index_levels):
    context.parsed = table_to_dataframe(context.input, column_levels=column_levels, index_levels=index_levels)


@then("it matches a manually created data frame with correct dtypes")
def step_impl(context):
    all_dtypes_df = pd.DataFrame(data={
        'integer_col': pd.Series([0, 1, 2], dtype=np.int),
        'integer32_col': pd.Series([0, 10, 20], dtype=np.int32),
        'integer64_col': pd.Series([0, 100, 200], dtype=np.int64),
        'float_col': pd.Series([3.0, 4.1, 5.2], dtype=np.float),
        'float32_col': pd.Series([3.0, 4.1, 5.2], dtype=np.float32),
        'float64_col': pd.Series([3.0, 4.1, 5.2], dtype=np.float64),
        'datetime_col': pd.Series(
            [datetime.datetime(2018, 2, 1), datetime.datetime(2018, 2, 2), datetime.datetime(2018, 2, 3)],
            dtype=np.datetime64),
        'datetime64_col': pd.Series(
            [datetime.datetime(2018, 2, 1), datetime.datetime(2018, 2, 2), datetime.datetime(2018, 2, 3)],
            dtype=np.datetime64),
        'object_col': pd.Series(['egg', 'spam', 'bacon'], dtype=object),
        'str_col': pd.Series(['silly walks', 'spanish inquisition', 'dead parrot'], dtype=str),

    })

    pdt.assert_frame_equal(all_dtypes_df, context.parsed)
