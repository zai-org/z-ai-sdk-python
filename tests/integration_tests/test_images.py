import logging
import logging.config

import zai
from zai import ZaiClient


def test_images(logging_conf):
	logging.config.dictConfig(logging_conf)  # type: ignore
	client = ZaiClient()  # Fill in your own API Key
	try:
		response = client.images.generations(
			model='cogview-3',  # Fill in the model name to call
			prompt='a cute little kitten',
			extra_body={'user_id': '1222212'},
			user_id='12345678',
		)
		print(response)

	except zai.core._errors.APIRequestFailedError as err:
		print(err)
	except zai.core._errors.APIInternalError as err:
		print(err)
	except zai.core._errors.APIStatusError as err:
		print(err)


def test_images_sensitive_word_check(logging_conf):
	logging.config.dictConfig(logging_conf)  # type: ignore
	client = ZaiClient()  # Fill in your own API Key
	try:
		response = client.images.generations(
			model='cogview-3',  # Fill in the model name to call
			prompt='a cute little kitten',
			sensitive_word_check={'type': 'ALL', 'status': 'DISABLE'},
			extra_body={'user_id': '1222212'},
			user_id='12345678',
		)
		print(response)

	except zai.core._errors.APIRequestFailedError as err:
		print(err)
	except zai.core._errors.APIInternalError as err:
		print(err)
	except zai.core._errors.APIStatusError as err:
		print(err)
