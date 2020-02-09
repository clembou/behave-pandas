import datetime
from collections import OrderedDict

from behave import *
from behave_pandas import table_to_dataframe

import pandas as pd
import pandas.testing as pdt
import numpy as np

use_step_matcher("parse")


@then("it matches a manually created data frame with all valid nullable boolean dtypes")
def step_impl(context):
    all_dtypes_df = pd.concat(
        [pd.Series([True, False, pd.NA], dtype="boolean")], axis=1
    )
    pdt.assert_frame_equal(all_dtypes_df, context.parsed)


@then("it matches a manually created data frame with all valid nullable integer dtypes")
def step_impl(context):
    all_dtypes_df = pd.concat([pd.Series([0, 10, pd.NA], dtype="Int64"),], axis=1,)
    pdt.assert_frame_equal(all_dtypes_df, context.parsed)


@then("it matches a manually created data frame with all valid string dtypes")
def step_impl(context):
    all_dtypes_df = pd.concat(
        [
            pd.Series(["egg", "spam", pd.NA], dtype="string"),
            pd.Series(["silly walks", "", "dead parrot"], dtype="string"),
        ],
        axis=1,
    )
    pdt.assert_frame_equal(all_dtypes_df, context.parsed)
