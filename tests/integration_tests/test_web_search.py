import logging
import logging.config

import zai
from zai import ZaiClient


def test_web_search(logging_conf):
	logging.config.dictConfig(logging_conf)  # type: ignore
	client = ZaiClient()  # Fill in your own API Key
	try:
		response = client.web_search.web_search(
			search_engine='search-std',
			search_query='2025特朗普向中国加征了多少关税',
			count=50,
			search_domain_filter='finance.sina.com.cn',
			search_recency_filter='oneYear',
			content_size='high',
			search_intent=True,
		)
		print(response)

	except zai.core._errors.APIRequestFailedError as err:
		print(err)
	except zai.core._errors.APIInternalError as err:
		print(err)
	except zai.core._errors.APIStatusError as err:
		print(err)
