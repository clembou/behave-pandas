from behave import *

from behave_pandas import dataframe_to_table

use_step_matcher("re")


@then("it prints a valid string copy pasteable into gherkin files")
def step_impl(context):
    print(context.text)
    print(context.result)
    assert context.result == context.text


@step("printed using data_frame_to_table")
def step_impl(context):
    context.result = dataframe_to_table(context.parsed)
