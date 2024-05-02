# utils.py
# Contains general utility functions used across various parts of the project. These functions include
# loading credentials, saving data to CSV files, and other reusable code snippets. This module facilitates common
# operations needed by multiple other modules within the application.
import os
import json
import pandas as pd
import logging

OUTPUT_FOLDER = 'output'


def load_credentials(file_path):
    """
    Loads JSON formatted credentials from a given file path.
    Handles errors if file is not found or JSON is malformed.
    Args:
        file_path (str): The path to the credentials file.
    Returns:
        dict: The loaded credentials, or None if an error occurs.
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
        return None
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from file - {file_path}")
        return None


def save_to_csv(df, filename):
    """
    Saves a DataFrame to a CSV file.
    Args:
        df (DataFrame): The DataFrame to save.
        filename (str): The filename to save the DataFrame to.
    """
    # Create the output folder if it doesn't exist
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    # Construct the full path to the output file
    filepath = os.path.join(OUTPUT_FOLDER, filename)
    # Save the DataFrame to a CSV file
    df.to_csv(filepath, index=False)



