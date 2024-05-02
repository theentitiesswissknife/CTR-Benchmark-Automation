import pandas as pd
from src.utils import save_to_csv


def compare_title(row):
    """
    Compare 'title' and 'SERP Title' columns for a single row and return the comparison result.
    Args:
        row (pd.Series): A single row of the DataFrame.
    Returns:
        str: The comparison result ('Exact Title', 'Rewritten', or "Couldn't be compared").
    """
    if pd.isna(row['title']) or pd.isna(row['SERP Title']):
        return "Couldn't be compared"
    elif row['title'].lower() == row['SERP Title'].lower():
        return 'Exact Title'
    else:
        return 'Rewritten'


def update_title_format(df):
    """
    Update the 'Title Format' column in the DataFrame based on the comparison between 'title' and 'SERP Title'.
    Args:
        df (pd.DataFrame): DataFrame containing 'title' and 'SERP Title' columns.
    Returns:
        pd.DataFrame: DataFrame with the 'Title Format' column added.
    """
    df['Title Format'] = df.apply(compare_title, axis=1)
    save_to_csv(df, 'final_output.csv')
    return df
