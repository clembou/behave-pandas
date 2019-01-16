from behave import *
import pandas as pd
import pandas.testing as pdt
import numpy as np

from behave_pandas import table_to_dataframe

use_step_matcher("parse")


@then("it matches a manually created data frame with a single index")
def step_impl(context):
    expected_df = get_expected_table()
    expected_df.set_index("index_col", inplace=True)
    pdt.assert_frame_equal(expected_df, context.parsed)


def get_expected_table():
    expected_df = pd.DataFrame(
        data={
            "index_col": pd.Series(["egg", "spam", "bacon"], dtype=str),
            "float_col": pd.Series([3.0, 4.1, 5.2], dtype=np.float),
            "str_col": pd.Series(
                ["silly walks", "spanish inquisition", "dead parrot"], dtype=str
            ),
        }
    )
    return expected_df


@then("it matches a manually created data frame with a multi index")
def step_impl(context):
    expected_df = get_expected_table()
    expected_df.set_index(["index_col", "float_col"], inplace=True)
    pdt.assert_frame_equal(expected_df, context.parsed)


@then("it matches a manually created data frame with a multi index on columns")
def step_impl(context):
    col_index = pd.MultiIndex.from_arrays(
        [
            ["country", "age", "age", "height", "height"],
            ["", "min", "max", "min", "max"],
        ]
    )
    expected_df = pd.DataFrame(
        data=[
            ("France", 3, 9, 15.0, 18.0),
            ("UK", 4, 8, 13.1, 19.2),
            ("USA", 5, 10, 12.2, 15.7),
        ],
        columns=col_index,
    )

    pdt.assert_frame_equal(expected_df, context.parsed)


@then(
    "it matches a manually created data frame with a multi index on columns and single row index"
)
def step_impl(context):
    col_index = pd.MultiIndex.from_arrays(
        [["age", "age", "height", "height"], ["min", "max", "min", "max"]]
    )
    row_index = pd.Index(["France", "UK", "USA"], name="country", dtype=str)

    expected_df = pd.DataFrame(
        data=[(3, 9, 15.0, 18.0), (4, 8, 13.1, 19.2), (5, 10, 12.2, 15.7)],
        columns=col_index,
        index=row_index,
    )

    pdt.assert_frame_equal(expected_df, context.parsed)


@then(
    "it matches a manually created data frame with a multi index on columns and multi row index"
)
def step_impl(context):
    col_index = pd.MultiIndex.from_arrays(
        [["age", "age", "height", "height"], ["min", "max", "min", "max"]]
    )
    row_index = pd.MultiIndex.from_tuples(
        [
            ("France", "Nantes"),
            ("France", "Paris"),
            ("UK", "London"),
            ("UK", "Manchester"),
        ],
        names=("country", "city"),
    )

    expected_df = pd.DataFrame(
        data=[
            (3, 9, 15.0, 18.0),
            (5, 11, 16.0, 21.0),
            (4, 8, 13.1, 19.2),
            (2, 6, 8.1, 11.2),
        ],
        columns=col_index,
        index=row_index,
    )

    pdt.assert_frame_equal(expected_df, context.parsed)


@when(
    "converted to a data frame using {column_levels:d} row as column names "
    "and {index_levels:d} column as index without flattening index names"
)
def step_impl(context, column_levels, index_levels):
    context.parsed = table_to_dataframe(
        context.input,
        column_levels=column_levels,
        index_levels=index_levels,
        collapse_empty_index_levels=False,
    )


@then(
    "it matches a manually created data frame with a multi index on columns "
    "and multi row index and unflattened index names"
)
def step_impl(context):
    col_index = pd.MultiIndex.from_arrays(
        [["age", "age", "height", "height"], ["min", "max", "min", "max"]]
    )
    row_index = pd.MultiIndex.from_tuples(
        [
            ("France", "Nantes"),
            ("France", "Paris"),
            ("UK", "London"),
            ("UK", "Manchester"),
        ],
        names=(("country", ""), ("city", "")),
    )

    expected_df = pd.DataFrame(
        data=[
            (3, 9, 15.0, 18.0),
            (5, 11, 16.0, 21.0),
            (4, 8, 13.1, 19.2),
            (2, 6, 8.1, 11.2),
        ],
        columns=col_index,
        index=row_index,
    )

    pdt.assert_frame_equal(expected_df, context.parsed)


@then(
    "it matches a similar table definition where index column names have been set on the second row"
)
def step_impl(context):
    pdt.assert_frame_equal(
        context.parsed,
        table_to_dataframe(context.table, column_levels=2, index_levels=2),
    )


@then(
    "it matches a manually created data frame with a multi index on columns and multi row index and complex column name combination"
)
def step_impl(context):
    col_index = pd.MultiIndex.from_arrays(
        [["age", "height", "height"], ["max", "min", "max"]]
    )
    row_index = pd.MultiIndex.from_tuples(
        [
            ("France", "Nantes", 3),
            ("France", "Paris", 5),
            ("UK", "London", 4),
            ("UK", "Manchester", 2),
        ],
        names=(("country", ""), ("city", ""), ("age", "")),
    )

    expected_df = pd.DataFrame(
        data=[(9, 15.0, 18.0), (11, 16.0, 21.0), (8, 13.1, 19.2), (6, 8.1, 11.2)],
        columns=col_index,
        index=row_index,
    )

    pdt.assert_frame_equal(expected_df, context.parsed)
