from behave import *
import pandas as pd
import pandas.testing as pdt
import numpy as np

use_step_matcher("parse")


@then("it matches a manually created data frame with a single index")
def step_impl(context):
    expected_df = get_expected_table()
    expected_df.set_index('index_col', inplace=True)
    pdt.assert_frame_equal(expected_df, context.parsed)


def get_expected_table():
    expected_df = pd.DataFrame(data={
        'index_col': pd.Series(['egg', 'spam', 'bacon'], dtype=str),
        'float_col': pd.Series([3.0, 4.1, 5.2], dtype=np.float),
        'str_col': pd.Series(['silly walks', 'spanish inquisition', 'dead parrot'], dtype=str),
    })
    return expected_df


@then("it matches a manually created data frame with a multi index")
def step_impl(context):
    expected_df = get_expected_table()
    expected_df.set_index(['index_col', 'float_col'], inplace=True)
    pdt.assert_frame_equal(expected_df, context.parsed)


@then("it matches a manually created data frame with a multi index on columns")
def step_impl(context):
    col_index = pd.MultiIndex.from_arrays([
        ['country', 'age', 'age', 'height', 'height'],
        ['', 'min', 'max', 'min', 'max']])
    expected_df = pd.DataFrame(data=[
        ('France', 3, 9, 15.0, 18.0),
        ('UK', 4, 8, 13.1, 19.2),
        ('USA', 5, 10, 12.2, 15.7),
    ], columns=col_index)

    pdt.assert_frame_equal(expected_df, context.parsed)
