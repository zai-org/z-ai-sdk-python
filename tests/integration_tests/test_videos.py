import logging
import logging.config

import zai
from zai import ZaiClient


def test_videos(logging_conf):
	logging.config.dictConfig(logging_conf)  # type: ignore
	client = ZaiClient()  # Fill in your own API Key
	try:
		response = client.videos.generations(model='cogvideox', prompt='A person sailing a boat', user_id='1212222')
		print(response)

	except zai.core._errors.APIRequestFailedError as err:
		print(err)
	except zai.core._errors.APIInternalError as err:
		print(err)
	except zai.core._errors.APIStatusError as err:
		print(err)


def test_videos_sensitive_word_check(logging_conf):
	logging.config.dictConfig(logging_conf)  # type: ignore
	client = ZaiClient()  # Fill in your own API Key
	try:
		response = client.videos.generations(
			model='cogvideo',
			prompt='A person sailing a boat',
			sensitive_word_check={'type': 'ALL', 'status': 'DISABLE'},
			user_id='1212222',
		)
		print(response)

	except zai.core._errors.APIRequestFailedError as err:
		print(err)
	except zai.core._errors.APIInternalError as err:
		print(err)
	except zai.core._errors.APIStatusError as err:
		print(err)


def test_videos_image_url(logging_conf):
	logging.config.dictConfig(logging_conf)  # type: ignore
	client = ZaiClient()  # Fill in your own API Key
	try:
		response = client.videos.generations(
			model='cogvideo',
			image_url='https://cdn.bigmodel.cn/static/platform/images/solutions/car/empowerment/icon-metric.png',
			prompt='A person holding a light',
			user_id='12222211',
		)
		print(response)

	except zai.core._errors.APIRequestFailedError as err:
		print(err)
	except zai.core._errors.APIInternalError as err:
		print(err)
	except zai.core._errors.APIStatusError as err:
		print(err)


def test_retrieve_videos_result(logging_conf):
	logging.config.dictConfig(logging_conf)  # type: ignore
	client = ZaiClient()  # Fill in your own API Key
	try:
		response = client.videos.retrieve_videos_result(id='1014908869548405238276203')
		print(response)

	except zai.core._errors.APIRequestFailedError as err:
		print(err)
	except zai.core._errors.APIInternalError as err:
		print(err)
	except zai.core._errors.APIStatusError as err:
		print(err)
