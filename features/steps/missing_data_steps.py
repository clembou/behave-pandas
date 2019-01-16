import datetime
from behave import *
from behave_pandas import table_to_dataframe

import pandas as pd
import pandas.testing as pdt
import numpy as np

use_step_matcher("parse")


@then("it matches a manually created data frame with null boolean data")
def step_impl(context):
    all_dtypes_df = pd.concat(
        [
            pd.Series([True, None, True, False], dtype=np.bool),
            pd.Series([None, None, None, None], dtype=np.bool),
        ],
        axis=1,
    )
    pdt.assert_frame_equal(all_dtypes_df, context.parsed)


@then("it matches a manually created data frame with null integer data")
def step_impl(context):
    all_dtypes_df = pd.concat(
        [
            pd.Series([np.nan, 1, 2], dtype=np.int),
            pd.Series([np.nan, np.nan, np.nan], dtype=np.int),
        ],
        axis=1,
    )
    pdt.assert_frame_equal(all_dtypes_df, context.parsed)


@then("it matches a manually created data frame with null float data")
def step_impl(context):
    all_dtypes_df = pd.concat(
        [
            pd.Series([np.nan, 4.1, 5.2], dtype=np.float),
            pd.Series([np.nan, np.nan, np.nan], dtype=np.float),
        ],
        axis=1,
    )
    pdt.assert_frame_equal(all_dtypes_df, context.parsed)


@then("it matches a manually created data frame with null datetime data")
def step_impl(context):
    all_dtypes_df = pd.concat(
        [
            pd.Series(
                [datetime.datetime(2018, 2, 1), np.nan, datetime.datetime(2018, 2, 3)],
                dtype=np.datetime64,
            ),
            pd.Series([np.nan, np.nan, np.nan], dtype=np.datetime64),
        ],
        axis=1,
    )
    pdt.assert_frame_equal(all_dtypes_df, context.parsed)


@then("it matches a manually created data frame with null object data")
def step_impl(context):
    all_dtypes_df = pd.concat(
        [
            pd.Series(["egg", np.nan, "bacon"], dtype=object),
            pd.Series([np.nan, np.nan, np.nan], dtype=str),
            pd.Series([np.nan, np.nan, np.nan], dtype=object),
            pd.Series([np.nan, np.nan, np.nan], dtype=object),
        ],
        axis=1,
    )
    pdt.assert_frame_equal(all_dtypes_df, context.parsed)


@then("it raises a ValueError exception")
def step_impl(context):
    assert isinstance(context.exception, ValueError)


@then("it matches a manually created empty data frame")
def step_impl(context):
    all_dtypes_df = pd.concat(
        [
            pd.Series(dtype=object),
            pd.Series(dtype=str),
            pd.Series(dtype=float),
            pd.Series(dtype=np.datetime64),
            pd.Series(dtype=object),
            pd.Series(dtype=object),
        ],
        axis=1,
    )
    pdt.assert_frame_equal(all_dtypes_df, context.parsed)
