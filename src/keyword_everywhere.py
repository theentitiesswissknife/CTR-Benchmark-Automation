import requests
import json
import pandas as pd
from src.utils import load_credentials, save_to_csv


def send_api_request(request_data):
    """
    Sends an API request.
    Args:
        request_data (dict): Request data.
    Returns:
        dict or None: API response JSON if successful, None otherwise.
    """
    # Load API credentials to get the endpoint
    api_credentials = load_credentials('config/api_credentials.json')
    if api_credentials is None:
        return None

    # Extract the endpoint from the credentials
    endpoint = api_credentials.get('Keyword_everywhere_api_endpoint')
    if not endpoint:
        print("Error: API endpoint not found in credentials.")
        return None

    # Prepare the headers for the request
    headers = {
        'Accept': 'application/json',
        'Authorization': f"Bearer {api_credentials.get('Keyword_everywhere_api_key')}"
    }

    # Send the API request
    response = requests.post(endpoint, data=request_data, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the API response as JSON
        api_data = response.content.decode('utf-8')
        return json.loads(api_data)
    else:
        print(f"Error: API request failed with status code {response.status_code}")
        return None


def generate_keyword_chunks(keywords, chunk_size):
    """
    Generates chunks of keywords for API requests.
    Args:
        keywords (list): List of keywords.
        chunk_size (int): Size of each chunk.
    Returns:
        list of lists: List of keyword chunks.
    """
    # Initialize an empty list to store the keyword chunks
    keyword_chunks = []

    # Iterate over the range of indices in increments of chunk_size
    for i in range(0, len(keywords), chunk_size):
        # Slice the keywords list to get the current chunk
        chunk = keywords[i:i + chunk_size]

        # Append the current chunk to the list of keyword chunks
        keyword_chunks.append(chunk)

    # Return the list of keyword chunks
    return keyword_chunks


def extract_keyword_data(keywords_dataframe):
    """
    Extracts CPC, competition, and volume data for keywords from an API and saves the data to a CSV file.
    Args:
        keywords_dataframe (DataFrame): DataFrame containing the keywords to retrieve data for.
    Returns:
        DataFrame: DataFrame with CPC, competition, and volume data for keywords.
    """
    # Extract keywords for API request
    keywords = keywords_dataframe['query'].tolist()
    chunk_size = 99
    keyword_chunks = generate_keyword_chunks(keywords, chunk_size)

    # Initialize lists to store CPC, competition, and volume values
    all_cpc_values = []
    all_competition_values = []
    all_volume_values = []

    # Send requests for each keyword chunk
    for chunk in keyword_chunks:
        request_data = {
            'country': 'us',
            'currency': 'USD',
            'dataSource': 'gkp',
            'kw[]': chunk
        }

        # Send API request
        api_json = send_api_request(request_data)

        # Parse API response
        if api_json:
            # Extract CPC, competition, and volume values from the API response
            cpc_values = [entry.get('cpc', {}).get('value') for entry in api_json.get('data', [])]
            competition_values = [entry.get('competition') for entry in api_json.get('data', [])]
            volume_values = [entry.get('vol') for entry in api_json.get('data', [])]

            # Append the values to the respective lists
            all_cpc_values.extend(cpc_values)
            all_competition_values.extend(competition_values)
            all_volume_values.extend(volume_values)

    # Add CPC, competition, and volume data to the DataFrame
    keywords_dataframe['CPC'] = all_cpc_values
    keywords_dataframe['competition'] = all_competition_values
    keywords_dataframe['vol'] = all_volume_values

    # Save volume, CPC, and competition score
    save_to_csv(keywords_dataframe, 'kw_everywhere_metrics.csv')
    return keywords_dataframe
