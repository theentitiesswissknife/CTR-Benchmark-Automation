# utils.py
# Contains general utility functions used across various parts of the project. These functions include
# loading credentials, saving data to CSV files, and other reusable code snippets. This module facilitates common
# operations needed by multiple other modules within the application.
import os
import json
import pandas as pd

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


def save_to_csv(df: object, filename: object) -> object:
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
    df.to_csv(filepath, index=False, encoding='utf-8')


def get_valid_days():
    """
    Prompts the user to enter the number of days to fetch data and validates the input.
    Returns:
        int: Number of days to fetch data.
    """
    while True:
        try:
            days = int(input("Enter the number of days to fetch data: "))
            if days <= 0:
                print("Please enter a positive integer.")
            else:
                return days
        except ValueError:
            print("Please enter a valid integer.")


def get_threshold_percentage():
    # Loop until a valid threshold percentage is provided by the user
    while True:
        threshold_percentage_str = input("Enter the threshold value for cumulative percent (e.g., 40 for 40%): ")

        # Check if the input is numeric
        if not threshold_percentage_str.replace('.', '', 1).isdigit():  # Check if numeric after removing the decimal point
            print("Invalid input. Please enter a numeric value.")
            continue

        # Convert the input to a float
        threshold_percentage = float(threshold_percentage_str)

        # Check if the input is within the valid range (0 to 100)
        if 0 <= threshold_percentage <= 100:
            return threshold_percentage
        else:
            print("Invalid input. Please enter a value between 0 and 100.")

