from behave import *
from behave_pandas import table_to_dataframe

use_step_matcher("parse")


@given("a gherkin table as input")
def step_impl(context,):
    context.input = context.table


@when(
    "converted to a data frame using {column_levels:d} row as column names and {index_levels:d} column as index"
)
def step_impl(context, column_levels, index_levels):
    context.parsed = table_to_dataframe(
        context.input, column_levels=column_levels, index_levels=index_levels
    )


@when(
    "attempting to convert to a data frame using "
    "{column_levels:d} row as column names and {index_levels:d} column as index"
)
def step_impl(context, column_levels, index_levels):
    try:
        context.parsed = table_to_dataframe(
            context.input, column_levels=column_levels, index_levels=index_levels
        )
    except Exception as e:
        context.exception = e
