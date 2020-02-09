import pandas as pd


def before_scenario(context, scenario):
    if should_skip_scenario_due_to_pandas_version(context, scenario):
        scenario.skip()


def should_skip_scenario_due_to_pandas_version(context, scenario):
    """
    Allow to skip scenario for a given pandas version by decorating it with @skip.pandasversion_comparison
    ie @skip.pandas>, @skipApi>25, @skipApi<24, @skipApi>=25, @skipApi<=29
    """
    pandas_skip_tag = "skip.before.pandasv1"

    if pandas_skip_tag in scenario.effective_tags:
        if int(pd.__version__[0]) < 1:
            return True
    return False
