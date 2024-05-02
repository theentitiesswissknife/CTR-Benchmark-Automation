from src.domain_utils import format_domain
from src.google_search_console import fetch_gsc_data
# from src.keyword_analysis import process_keywords, fetch_keyword_data, determine_intent
# from src.title_scraper import scrape_titles
# from src.serp_analysis import get_serp_data
# from src.utils import save_to_csv


def main():
    # Step 1: Format the input domain
    domain = format_domain()

    # # Step 2: Fetch data from Google Search Console
    gsc_data = fetch_gsc_data(domain)

    # # Step 3: Filter and process data from Google Search Console
    # processed_data = process_keywords(gsc_data)
    # save_to_csv(processed_data, 'filtered_keywords.csv')
    #
    # # Step 4: Fetch keyword metrics using an Keywords Everywhere API
    # keyword_metrics = fetch_keyword_data(processed_data)
    # save_to_csv(keyword_metrics, 'keyword_metrics.csv')
    #
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
