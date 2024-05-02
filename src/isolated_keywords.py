import pandas as pd
from src.utils import save_to_csv


def filter_keywords(df, threshold_percentage):
    """
    Filters keywords based on cumulative percent and saves the isolated keywords to a CSV file.

    Args:
        df (DataFrame): DataFrame containing the keywords.
        threshold_percentage (float): Threshold percentage for cumulative percent.

    Returns:
        DataFrame: DataFrame with isolated keywords.
    """
    # Convert the threshold percentage to a decimal value
    threshold = threshold_percentage / 100

    # Make a copy of the DataFrame to avoid SettingWithCopyWarning
    df = df.copy()

    # Calculate cumulative percent
    total_clicks = df.groupby('page')['clicks'].sum().rename('total_clicks')
    df = df.join(total_clicks, on='page')
    df = df.sort_values(by=['page', 'clicks'], ascending=[True, False])
    df['cumulative_clicks'] = df.groupby('page')['clicks'].cumsum()
    df['cumulative_percent'] = df['cumulative_clicks'] / df['total_clicks']

    # Filter keywords based on cumulative percent
    df['include'] = (df['cumulative_percent'] <= threshold) | (df['cumulative_percent'].shift() < threshold)
    keywords_to_analyze = df[df['include']]

    # Define columns to exclude from the DataFrame
    columns_to_exclude = ['include']

    # Drop the specified columns
    keywords_to_analyze = keywords_to_analyze.drop(columns=columns_to_exclude)

    # Save the isolated keywords to CSV
    save_to_csv(keywords_to_analyze, 'isolated_keywords.csv')

    return keywords_to_analyze
