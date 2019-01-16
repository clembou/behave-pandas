from tabulate import tabulate
import pandas as pd

from behave_pandas.dtypes import (
    VALID_FLOAT_DTYPES,
    VALID_DATETIME_DTYPES,
    VALID_OBJECT_DTYPES,
)


def dataframe_to_table(df):
    """
    converts a pandas DataFrame into a valid gherkin table that can be copy/ pasted into feature files.
    :param df: pd.DataFrame
    :return: str
    """
    to_format = df.reset_index()
    cols_with_potential_nones = to_format.select_dtypes("object").columns
    to_format.loc[:, cols_with_potential_nones] = to_format.loc[
        :, cols_with_potential_nones
    ].fillna("")

    cols_with_potential_nans = [
        col
        for col, dtype in to_format.dtypes.iteritems()
        if str(dtype) in VALID_FLOAT_DTYPES.keys() or str(dtype) in VALID_OBJECT_DTYPES
    ]
    cols_with_potential_nats = [
        col
        for col, dtype in to_format.dtypes.iteritems()
        if str(dtype) in VALID_DATETIME_DTYPES.keys()
    ]

    as_string = to_format.astype(str)
    as_string.loc[:, cols_with_potential_nans] = as_string.loc[
        :, cols_with_potential_nans
    ].replace("nan", "")
    as_string.loc[:, cols_with_potential_nats] = as_string.loc[
        :, cols_with_potential_nats
    ].replace("NaT", "")

    table_string_df = pd.concat(
        [to_format.dtypes.to_frame().T, to_format.columns.to_frame().T, as_string]
    )
    return tabulate(table_string_df.values, tablefmt="jira")
