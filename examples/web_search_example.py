import os
from zai import ZaiClient

# Try to load .env file
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

api_key = os.getenv('ZAI_API_KEY')
if not api_key:
    print("Please set the ZAI_API_KEY environment variable or configure it in the .env file")
    exit()

client = ZaiClient(api_key=api_key)

def web_search_example():
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