import asyncio
import pandas as pd
from src.domain_utils import format_domain
from src.google_search_console import fetch_gsc_data
from src.utils import save_to_csv, get_valid_days, get_threshold_percentage
from src.isolated_keywords import filter_keywords
from src.keyword_everywhere import extract_keyword_data
from src.intent_classification import process_keyword_metrics
from src.benchmark_test import analyze_and_filter_keywords
from src.scrapping_titles import scrape_page_titles
from src.data_for_seo import add_serp_data_to_df
from src.compare_title import update_title_format


def main():
    # # # Step 1: Format the input domain, days
    domain = format_domain()
    days = get_valid_days()
    threshold_percentage = get_threshold_percentage()

    # # # # Step 2: Fetch data from Google Search Console
    gsc_data = fetch_gsc_data(domain, days)

    # # # # Step 3: Filter and process data from Google Search Console
    isolated_keywords_df = filter_keywords(gsc_data, threshold_percentage)

    # # # # Step 4: Fetch keyword metrics using an Keywords Everywhere API
    keyword_metrics = extract_keyword_data(isolated_keywords_df)

    # # # # Step 5: Determine keyword intent based on the metrics
    keywords_with_intent = process_keyword_metrics(keyword_metrics)

    # # # # Step 6: Compare keyword metrics against benchmarks
    benchmarked_data = analyze_and_filter_keywords(keywords_with_intent)

    # # # Step 7: Scrape titles from URLs found in the Google Search Console data
    keywords_with_titles = asyncio.run(scrape_page_titles(benchmarked_data))

    # # Step 8: Fetch SERP data from a service like DataForSEO
    serp_data = add_serp_data_to_df(keywords_with_titles)

    # # Step 9: Compare the scraped titles with SERP data
    comparison_results = update_title_format(serp_data)


if __name__ == "__main__":
    main()
