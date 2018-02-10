from tabulate import tabulate
import pandas as pd


def dataframe_to_table(df):
    """
    converts a pandas DataFrame into a valid gherkin table that can be copy/ pasted into feature files.
    :param df: pd.DataFrame
    :return: str
    """
    to_format = df.reset_index()
    table_string_df = pd.concat([
        to_format.dtypes.to_frame().T,
        to_format.columns.to_frame().T,
        to_format.astype(str)
    ])
    return tabulate(table_string_df.values, tablefmt='jira')
