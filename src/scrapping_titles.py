import aiohttp
import asyncio
import pandas as pd
from bs4 import BeautifulSoup
from src.utils import save_to_csv

# Dictionary to store scraped titles for each unique URL
url_titles = {}


async def get_page_title(url):
    """
    Scrape the title from a given URL asynchronously.
    Args:
        url (str): The URL to scrape the title from.
    Returns:
        str or None: The title of the page, or None if an error occurs.
    """
    headers_browser = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/124.0.0.0 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9'
    }
    if url in url_titles:
        return url_titles[url]
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers_browser) as response:
                html = await response.text()
                soup = BeautifulSoup(html, 'html.parser')
                title = soup.title.string
                # Store the title in the dictionary
                url_titles[url] = title
                return title
    except Exception as e:
        print(f"Error occurred while fetching title for URL: {url}")
        return None


async def scrape_page_titles(keywords_df):
    """
    Scrape titles for each unique URL asynchronously.
    Args:
        keywords_df (DataFrame): DataFrame containing URLs to scrape titles from.
    Returns:
        DataFrame: DataFrame with scraped titles added as a new column.
    """
    tasks = [get_page_title(row['page']) for index, row in keywords_df.iterrows()]
    scraped_titles = await asyncio.gather(*tasks)
    keywords_df['title'] = scraped_titles
    save_to_csv(keywords_df, 'with_html_title.csv')
    return keywords_df




# Example usage:
if __name__ == "__main__":
    keywords_with_benchmark_ctr = pd.read_csv('raw/keywords_with_benchmark_ctr.csv')
    keywords_with_titles = asyncio.run(scrape_page_titles(keywords_with_benchmark_ctr))
    save_dataframe_with_titles(keywords_with_titles, 'raw/keywords_with_title.csv')
