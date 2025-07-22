import os
from pydoc import cli
from zai import ZaiClient


def web_search_example():
    client = ZaiClient()
    response = client.web_search.web_search(
        search_engine="search_pro",
        search_query="Search for financial news in April 2025",
        count=15,  # Number of returned results, range 1-50, default 10
        search_domain_filter="www.sohu.com",  # Only access content from specified domain
        search_recency_filter="noLimit",  # Search content within specified time range
        content_size="high"  # Control the word count of web page summaries, default medium
    )
    print(response)

if __name__ == "__main__":
    web_search_example() 