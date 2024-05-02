import pandas as pd
from src.utils import save_to_csv


def convert_to_float(df):
    """
    Convert 'competition' and 'CPC' columns to float in the DataFrame.
    Args:
        df (DataFrame): DataFrame containing keyword metrics.
    Returns:
        DataFrame: DataFrame with 'competition' and 'CPC' columns converted to float.
    """
    df['competition'] = df['competition'].astype(float)
    df['CPC'] = df['CPC'].astype(float)
    return df


def calculate_commercial_scale(row):
    """
    Calculate commercial scale for each keyword based on competition and CPC.
    Args:
        row (Series): DataFrame row representing a keyword.
    Returns:
        int: Commercial scale value.
    """
    if row['competition'] == 0 or row['CPC'] == 0:
        return 0
    else:
        return int(row['competition'] * row['CPC'] * 100)


def determine_intent(row):
    """
    Determine keyword intent based on commercial scale.
    Args:
        row (Series): DataFrame row representing a keyword.
    Returns:
        str: Keyword intent ('Commercial' or 'Informational').
    """
    if row['commercial_scale'] > 0:
        return 'Commercial'
    else:
        return 'Informational'


def classify_intent(df):
    """
    Classify keyword intent and add the 'keyword_intent' column to the DataFrame.
    Args:
        df (DataFrame): DataFrame containing keyword metrics.
    Returns:
        DataFrame: DataFrame with 'keyword_intent' column added.
    """
    # Calculate commercial scale
    df['commercial_scale'] = df.apply(calculate_commercial_scale, axis=1)
    # Determine keyword intent
    df['keyword_intent'] = df.apply(determine_intent, axis=1)
    return df


def process_keyword_metrics(df):
    """
    Process keyword metrics by converting columns to float, calculating commercial scale,
    and classifying keyword intent.
    Args:
        df (DataFrame): DataFrame containing keyword metrics.
    Returns:
        DataFrame: DataFrame with keyword metrics processed.
    """
    # Convert columns to float
    df = convert_to_float(df)
    # Classify keyword intent
    df = classify_intent(df)
    save_to_csv(df, 'keywords_with_intent.csv')
    return df
