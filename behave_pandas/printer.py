from tabulate import tabulate
import pandas as pd


def data_frame_to_table(df):
    to_format = df.reset_index()
    table_string_df = pd.concat([
        to_format.dtypes.to_frame().T,
        to_format.columns.to_frame().T,
        to_format.astype(str)
    ])
    return tabulate(table_string_df.values, tablefmt='jira')
