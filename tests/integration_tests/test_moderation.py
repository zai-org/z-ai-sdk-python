import logging
import logging.config
import time

import zai
from zai import ZaiClient


def test_completions_temp0(logging_conf):
	logging.config.dictConfig(logging_conf)  # type: ignore
	client = ZaiClient(disable_token_cache=False)  # Fill in your own API Key
	try:
		# Generate request_id
		request_id = time.time()
		print(f'request_id:{request_id}')
		response = client.moderations.create(model='moderation', input={'type': 'text', 'text': 'hello world '})
		print(response)

	except zai.core._errors.APIRequestFailedError as err:
		print(err)
	except zai.core._errors.APIInternalError as err:
		print(err)
	except zai.core._errors.APIStatusError as err:
		print(err)
