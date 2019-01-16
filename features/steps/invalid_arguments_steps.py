from behave import *

from behave_pandas import table_to_dataframe

use_step_matcher("re")


@when(
    "attempting to convert to a data frame using invalid number of row \((?P<index_levels>.+)\) or column \((?P<column_levels>.+)\) index levels"
)
def step_impl(context, index_levels, column_levels):
    try:
        column_levels = int(column_levels)
    except:
        pass
    try:
        index_levels = int(index_levels)
    except:
        pass

    try:
        context.parsed = table_to_dataframe(
            context.input, column_levels=column_levels, index_levels=index_levels
        )
    except Exception as e:
        context.exception = e


@then("it raises a ValueError Exception")
def step_impl(context):
    assert isinstance(context.exception, ValueError)
