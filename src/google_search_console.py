# google_search_console.py
# Manages authentication and data retrieval from the Google Search Console API.
# This module handles all interactions with Google Search Console, providing necessary data for further analysis.

import pandas as pd
import searchconsole
from src.utils import load_credentials, save_to_csv


def fetch_gsc_data(domain):
    """
    Fetches data from Google Search Console for a given domain.
    Args:
        domain (str): The domain to fetch data for, including protocol (e.g., https://example.com).
    Returns:
        DataFrame: A DataFrame containing query data from Google Search Console.
    """
    # Load credentials from your configuration file
    credentials = load_credentials('config/client_secrets.json')

    # Authenticate and construct the service object
    account = searchconsole.authenticate(client_config=credentials)
    web_property = account[domain]

    # Define the date range and query parameters
    # Here, 'today' - 28 days range is used as an example
    report = web_property.query.range('today', days=-28).dimension('query', 'page').get()

    # Convert the report to a DataFrame
    df = report.to_dataframe()

    # Optionally, save the data to a CSV file for later use
    save_to_csv(df, 'search_console_data.csv')

    return df
