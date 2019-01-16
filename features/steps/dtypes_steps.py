import datetime
from collections import OrderedDict

from behave import *
from behave_pandas import table_to_dataframe

import pandas as pd
import pandas.testing as pdt
import numpy as np

use_step_matcher("parse")


@then("it matches a manually created data frame with all valid boolean dtypes")
def step_impl(context):
    all_dtypes_df = pd.concat(
        [pd.Series([True, False, True, False], dtype=np.bool)], axis=1
    )
    pdt.assert_frame_equal(all_dtypes_df, context.parsed)


@then("it matches a manually created data frame with all valid integer dtypes")
def step_impl(context):
    all_dtypes_df = pd.concat(
        [
            pd.Series([0, 1, 2], dtype=np.int),
            pd.Series([0, 10, 20], dtype=np.int32),
            pd.Series([0, 100, 200], dtype=np.int64),
        ],
        axis=1,
    )
    pdt.assert_frame_equal(all_dtypes_df, context.parsed)


@then("it matches a manually created data frame with all valid float dtypes")
def step_impl(context):
    all_dtypes_df = pd.concat(
        [
            pd.Series([3.0, 4.1, 5.2], dtype=np.float),
            pd.Series([3.0, 4.1, 5.2], dtype=np.float32),
            pd.Series([3.0, 4.1, 5.2], dtype=np.float64),
        ],
        axis=1,
    )
    pdt.assert_frame_equal(all_dtypes_df, context.parsed)


@then("it matches a manually created data frame with all valid datetime dtypes")
def step_impl(context):
    all_dtypes_df = pd.concat(
        [
            pd.Series(
                [
                    datetime.datetime(2018, 2, 1),
                    datetime.datetime(2018, 2, 2),
                    datetime.datetime(2018, 2, 3),
                ],
                dtype=np.datetime64,
            ),
            pd.Series(
                [
                    datetime.datetime(2018, 2, 1),
                    datetime.datetime(2018, 2, 2),
                    datetime.datetime(2018, 2, 3),
                ],
                dtype=np.datetime64,
            ),
            pd.Series(
                [
                    datetime.datetime(2018, 2, 1),
                    datetime.datetime(2018, 2, 2),
                    datetime.datetime(2018, 2, 3),
                ],
                dtype=np.datetime64,
            ),
        ],
        axis=1,
    )
    pdt.assert_frame_equal(all_dtypes_df, context.parsed)


@then("it matches a manually created data frame with all valid object dtypes")
def step_impl(context):
    all_dtypes_df = pd.concat(
        [
            pd.Series(["egg", "spam", "bacon"], dtype=object),
            pd.Series(["silly walks", "spanish inquisition", "dead parrot"], dtype=str),
            pd.Series([{}, {"a": None}, {"a": []}], dtype=object),
            pd.Series([[], [1], ["a"]], dtype=object),
            pd.Series(
                [
                    OrderedDict([]),
                    OrderedDict([("a", 1), ("b", None)]),
                    OrderedDict([("a", 1), ("b", [])]),
                ],
                dtype=object,
            ),
            pd.Series(
                [
                    OrderedDict([]),
                    OrderedDict([("a", 1), ("b", None)]),
                    OrderedDict([("a", 1), ("b", [])]),
                ],
                dtype=object,
            ),
        ],
        axis=1,
    )
    pdt.assert_frame_equal(all_dtypes_df, context.parsed)


@then("it raises an Exception")
def step_impl(context):
    assert isinstance(context.exception, TypeError)
