import pandas as pd
from src.utils import save_to_csv


def get_benchmark_ctr(row, benchmark_df):
    """
    Get benchmark CTR for a keyword based on its intent and position.
    Args:
        row (Series): Row containing keyword data.
        benchmark_df (DataFrame): Benchmark data.
    Returns:
        float: Benchmark CTR.
    """
    keyword_type = row['keyword_intent']
    position = min(row['position'], len(benchmark_df))
    benchmark_ctr = benchmark_df.iloc[position - 1][keyword_type]
    return benchmark_ctr


def analyze_and_filter_keywords(keywords_df):
    """
    Analyze keywords with benchmark CTR and filter keywords below the benchmark.
    Args:
        keywords_df (DataFrame): Keywords data with intent.
    Returns:
        DataFrame: Filtered DataFrame containing keywords below the benchmark.
    """
    benchmark_df = pd.read_csv('data/benchmark.csv')
    keywords_df['position'] = keywords_df['position'].astype(int)
    keywords_df['benchmark_ctr'] = keywords_df.apply(get_benchmark_ctr, args=(benchmark_df,), axis=1)
    keywords_df['CTR_comparison'] = keywords_df.apply(
        lambda row: 'Below Benchmark' if row['ctr'] < row['benchmark_ctr'] else 'Above or Equal to Benchmark', axis=1)
    filtered_keywords = keywords_df[keywords_df['CTR_comparison'] == 'Below Benchmark']
    save_to_csv(filtered_keywords, 'keywords_below_benchmark.csv')
    return filtered_keywords
