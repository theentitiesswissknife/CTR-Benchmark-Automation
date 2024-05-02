from src.seodata import RestClient
import pandas as pd
from src.utils import load_credentials, save_to_csv


def get_serp_data(keyword):
    """
    Fetches SERP data for a given keyword.
    Args:
        keyword (str): The keyword to fetch SERP data for.
    Returns:
        List[Dict[str, str]]: List of dictionaries containing SERP data.
    """
    api_credentials = load_credentials('config/api_credentials.json')
    if api_credentials is None:
        return None
    email = api_credentials.get('email_data_for_seo')
    password = api_credentials.get('password_data_for_seo')
    data_for_seo_endpoint = api_credentials.get('data_for_seo_endpoint')
    client = RestClient(email, password)
    post_data = {
        0: {
            "language_code": "en",
            "location_code": 2840,
            "keyword": keyword,
        }
    }
    res = client.post(data_for_seo_endpoint, post_data)
    data = res['tasks'][0]['result'][0]['items']
    return data


def add_serp_data_to_df(df: pd.DataFrame) -> pd.DataFrame:
    """
    Adds SERP data to a DataFrame containing keywords and titles.
    Args:
        df (pd.DataFrame): DataFrame containing keywords and titles.
    Returns:
        pd.DataFrame: DataFrame with SERP data added.
    """
    # Initialize new columns for Absolute Rank and SERP Title
    df['Absolute Rank'] = ''
    df['SERP Title'] = ''

    # Iterate over rows
    for index, row in df.iterrows():
        # Extract keyword from 'query' column
        keyword = row['query']

        # Send API request to get SERP data
        serp_data = get_serp_data(keyword)

        # Iterate over SERP data
        for item in serp_data:
            if item['url'] == row['page']:
                df.at[index, 'Absolute Rank'] = item['rank_absolute']
                df.at[index, 'SERP Title'] = item['title']
                break

    save_to_csv(df,'keywords_serp_title.csv')
    return df
