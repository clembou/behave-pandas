from behave import *

from behave_pandas import data_frame_to_table

use_step_matcher("re")


@then("it prints a valid string copy pasteable into gherkin files")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print(context.result)
    print('\n')
    print(context.text)
    assert context.result == context.text


@step("printed using data_frame_to_table")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.result = data_frame_to_table(context.parsed)