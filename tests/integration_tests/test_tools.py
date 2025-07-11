import logging
import logging.config

import zai
from zai import ZaiClient


def test_tools(logging_conf):
	logging.config.dictConfig(logging_conf)  # type: ignore
	client = ZaiClient()  # Fill in your own API Key
	try:
		response = client.tools.web_search(
			model='web-search-pro',
			messages=[
				{
					'content': 'hello',
					'role': 'user',
				}
			],
			stream=False,
		)
		print(response)

	except zai.core._errors.APIRequestFailedError as err:
		print(err)
	except zai.core._errors.APIInternalError as err:
		print(err)
	except zai.core._errors.APIStatusError as err:
		print(err)


def test_tools_stream(logging_conf):
	logging.config.dictConfig(logging_conf)  # type: ignore
	client = ZaiClient()  # Fill in your own API Key
	try:
		response = client.tools.web_search(
			model='web-search-pro',
			messages=[
				{
					'content': 'hello',
					'role': 'user',
				}
			],
			stream=True,
		)
		for item in response:
			print(item)

	except zai.core._errors.APIRequestFailedError as err:
		print(err)
	except zai.core._errors.APIInternalError as err:
		print(err)
	except zai.core._errors.APIStatusError as err:
		print(err)
