import logging
import logging.config
import time

import zai
from zai import ZaiClient


def test_completions_vlm_thinking(logging_conf):
	logging.config.dictConfig(logging_conf)  # type: ignore
	client = ZaiClient()  # Fill in your own API Key
	try:
		# Generate request_id
		request_id = time.time()
		print(f'request_id:{request_id}')
		response = client.chat.completions.create(
			request_id=request_id,
			model='glm-4.6v',  # Fill in the model name to call
			messages=[
				{
					'role': 'user',
					'content': [
						{'type': 'text', 'text': 'What is in the image?'},
						{
							'type': 'image_url',
							'image_url': {
								'url': 'https://img1.baidu.com/it/u=1369931113,3388870256&fm=253&app=138&size=w931&n=0&f=JPEG&fmt=auto?sec=1703696400&t=f3028c7a1dca43a080aeb8239f09cc2f'
							},
						},
					],
				}
			],
			temperature=0.5,
			max_tokens=1024,
			user_id='12345678',
		)
		print(response)

	except zai.core._errors.APIRequestFailedError as err:
		print(err)
	except zai.core._errors.APIInternalError as err:
		print(err)
	except zai.core._errors.APIStatusError as err:
		print(err)


def test_completions_vlm_thinking_stream(logging_conf):
	logging.config.dictConfig(logging_conf)  # type: ignore
	client = ZaiClient()  # Fill in your own API Key
	try:
		# Generate request_id
		request_id = time.time()
		print(f'request_id:{request_id}')
		response = client.chat.completions.create(
			request_id=request_id,
			model='glm-4.6v',  # Fill in the model name to call
			messages=[
				{
					'role': 'user',
					'content': [
						{'type': 'text', 'text': 'What is in the image?'},
						{
							'type': 'image_url',
							'image_url': {
								'url': 'https://img1.baidu.com/it/u=1369931113,3388870256&fm=253&app=138&size=w931&n=0&f=JPEG&fmt=auto?sec=1703696400&t=f3028c7a1dca43a080aeb8239f09cc2f'
							},
						},
					],
				}
			],
			temperature=0.5,
			max_tokens=1024,
			user_id='12345678',
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
