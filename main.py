from src.domain_utils import format_domain
from src.google_search_console import fetch_gsc_data
from src.utils import save_to_csv, get_valid_days, get_threshold_percentage
from src.isolated_keywords import filter_keywords
from src.keyword_everywhere import extract_keyword_data


# from src.keyword_analysis import process_keywords, fetch_keyword_data, determine_intent
# from src.title_scraper import scrape_titles
# from src.serp_analysis import get_serp_data


def main():
    # Step 1: Format the input domain, days
    domain = format_domain()
    days = get_valid_days()
    threshold_percentage = get_threshold_percentage()

    # # Step 2: Fetch data from Google Search Console
    gsc_data = fetch_gsc_data(domain, days)

    # # Step 3: Filter and process data from Google Search Console
    isolated_keywords_df = filter_keywords(gsc_data, threshold_percentage)

    # # Step 4: Fetch keyword metrics using an Keywords Everywhere API
    keyword_metrics = extract_keyword_data(isolated_keywords_df)

    print('keyword everywhere data saved')

    # # Step 5: Determine keyword intent based on the metrics
    # keyword_intents = determine_intent(keyword_metrics)
    # save_to_csv(keyword_intents, 'keyword_intents.csv')
    #
    # # Step 6: Compare keyword metrics against benchmarks
    # benchmarked_data = compare_with_benchmark(keyword_intents)
    # save_to_csv(benchmarked_data, 'benchmarked_keywords.csv')
    #
    # # Step 7: Scrape titles from URLs found in the Google Search Console data
    # titles = scrape_titles(processed_data)
    # save_to_csv(titles, 'scraped_titles.csv')
    #
    # # Step 8: Fetch SERP data from a service like DataForSEO
    # serp_data = get_serp_data(processed_data)
    # save_to_csv(serp_data, 'serp_data.csv')
    #
    # # Step 9: Compare the scraped titles with SERP data
    # comparison_results = compare_titles_with_serp(titles, serp_data)
    # save_to_csv(comparison_results, 'final_analysis.csv')


if __name__ == "__main__":
    main()
