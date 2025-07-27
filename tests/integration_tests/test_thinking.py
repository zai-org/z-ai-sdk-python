import logging
import logging.config
import time

import zai
from zai import ZaiClient


def test_chat_completion_with_thinking(logging_conf):
	logging.config.dictConfig(logging_conf)  # type: ignore
	client = ZaiClient()  # Fill in your own API Key
	try:
		# Generate request_id
		request_id = time.time()
		print(f'request_id:{request_id}')
		response = client.chat.completions.create(
			request_id=request_id,
			model='glm-4.5',
			messages=[{'role': 'user', 'content': '请介绍一下Agent的原理，并给出详细的推理过程'}],
			top_p=0.7,
			temperature=0.9,
		)
		print(response)

	except zai.core._errors.APIRequestFailedError as err:
		print(err)
	except zai.core._errors.APIInternalError as err:
		print(err)
	except zai.core._errors.APIStatusError as err:
		print(err)


def test_chat_completion_without_thinking(logging_conf):
	logging.config.dictConfig(logging_conf)  # type: ignore
	client = ZaiClient()  # Fill in your own API Key
	try:
		# Generate request_id
		request_id = time.time()
		print(f'request_id:{request_id}')
		response = client.chat.completions.create(
			request_id=request_id,
			model='glm-4.5',
			messages=[{'role': 'user', 'content': '请介绍一下Agent的原理'}],
			top_p=0.7,
			temperature=0.9,
			thinking={
				'type': 'disabled',
			},
		)
		print(response)

	except zai.core._errors.APIRequestFailedError as err:
		print(err)
	except zai.core._errors.APIInternalError as err:
		print(err)
	except zai.core._errors.APIStatusError as err:
		print(err)
