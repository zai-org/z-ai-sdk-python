import logging
import logging.config
import os.path
import time

import zai
from zai import ZaiClient


def test_completions_temp0(logging_conf):
	logging.config.dictConfig(logging_conf)  # type: ignore
	client = ZaiClient()  # Fill in your own API Key
	try:
		# Generate request_id
		request_id = time.time()
		print(f'request_id:{request_id}')
		response = client.chat.completions.create(
			request_id=request_id,
			model='glm-4',
			messages=[{'role': 'user', 'content': 'tell me a joke'}],
			top_p=0.7,
			temperature=0,
			max_tokens=2000,
			user_id='12345678',
		)
		print(response)

	except zai.core._errors.APIRequestFailedError as err:
		print(err)
	except zai.core._errors.APIInternalError as err:
		print(err)
	except zai.core._errors.APIStatusError as err:
		print(err)


def test_completions_temp1(logging_conf):
	logging.config.dictConfig(logging_conf)  # type: ignore
	client = ZaiClient()  # Fill in your own API Key
	try:
		# Generate request_id
		request_id = time.time()
		print(f'request_id:{request_id}')
		response = client.chat.completions.create(
			request_id=request_id,
			model='glm-4',
			messages=[{'role': 'user', 'content': 'tell me a joke'}],
			top_p=0.7,
			temperature=1,
			max_tokens=2000,
			user_id='12345678',
		)
		print(response)

	except zai.core._errors.APIRequestFailedError as err:
		print(err)
	except zai.core._errors.APIInternalError as err:
		print(err)
	except zai.core._errors.APIStatusError as err:
		print(err)


def test_completions_top0(logging_conf):
	logging.config.dictConfig(logging_conf)  # type: ignore
	client = ZaiClient()  # Fill in your own API Key
	try:
		# Generate request_id
		request_id = time.time()
		print(f'request_id:{request_id}')
		response = client.chat.completions.create(
			request_id=request_id,
			model='glm-4',
			messages=[{'role': 'user', 'content': 'tell me a joke'}],
			top_p=0,
			temperature=0.9,
			max_tokens=2000,
			user_id='12345678',
		)
		print(response)

	except zai.core._errors.APIRequestFailedError as err:
		print(err)
	except zai.core._errors.APIInternalError as err:
		print(err)
	except zai.core._errors.APIStatusError as err:
		print(err)


def test_completions_top1(logging_conf):
	logging.config.dictConfig(logging_conf)  # type: ignore
	client = ZaiClient()  # Fill in your own API Key
	try:
		# Generate request_id
		request_id = time.time()
		print(f'request_id:{request_id}')
		response = client.chat.completions.create(
			request_id=request_id,
			model='glm-4',
			messages=[{'role': 'user', 'content': 'tell me a joke'}],
			top_p=1,
			temperature=0.9,
			max_tokens=2000,
			user_id='12345678',
		)
		print(response)

	except zai.core._errors.APIRequestFailedError as err:
		print(err)
	except zai.core._errors.APIInternalError as err:
		print(err)
	except zai.core._errors.APIStatusError as err:
		print(err)


def test_completions(logging_conf):
	logging.config.dictConfig(logging_conf)  # type: ignore
	client = ZaiClient()  # Fill in your own API Key
	try:
		# Generate request_id
		request_id = time.time()
		print(f'request_id:{request_id}')
		response = client.chat.completions.create(
			request_id=request_id,
			model='glm-4',  # Fill in the model name to call
			messages=[
				{
					'role': 'user',
					'content': 'As a marketing expert, please create an attractive slogan for my product',
				},
				{
					'role': 'assistant',
					'content': (
						'Of course, to create an attractive slogan, please tell me some information about your product'
					),
				},
				{'role': 'user', 'content': 'Z.ai Open Platform'},
				{
					'role': 'assistant',
					'content': 'Ignite the future, paint infinity - Z.AI, making innovation within reach!',
				},
				{'role': 'user', 'content': 'Create a more precise and attractive slogan'},
			],
			tools=[
				{
					'type': 'web_search',
					'web_search': {
						'search_query': 'Show me the admission rate of Tsinghua University',
						'search_result': True,
					},
				}
			],
			user_id='12345678',
			extra_body={'temperature': 0.5, 'max_tokens': 50},
		)
		print(response)

	except zai.core._errors.APIRequestFailedError as err:
		print(err)
	except zai.core._errors.APIInternalError as err:
		print(err)
	except zai.core._errors.APIStatusError as err:
		print(err)


def test_completions_disenable_web_search(logging_conf):
	logging.config.dictConfig(logging_conf)  # type: ignore
	client = ZaiClient()  # Fill in your own API Key
	try:
		# Generate request_id
		request_id = time.time()
		print(f'request_id:{request_id}')
		response = client.chat.completions.create(
			request_id=request_id,
			model='glm-4',  # Fill in the model name to call
			messages=[
				{
					'role': 'user',
					'content': 'As a marketing expert, please create an attractive slogan for my product',
				},
				{
					'role': 'assistant',
					'content': (
						'Of course, to create an attractive slogan, please tell me some information about your product'
					),
				},
				{'role': 'user', 'content': 'Z.ai Open Platform'},
				{
					'role': 'assistant',
					'content': 'Ignite the future, paint infinity - Z.AI, making innovation within reach!',
				},
				{'role': 'user', 'content': 'Create a more precise and attractive slogan'},
			],
			tools=[
				{
					'type': 'web_search',
					'web_search': {
						'search_query': 'Show me the admission rate of Tsinghua University',
						'search_result': True,
						'enable': False,
					},
				}
			],
			user_id='12345678',
			extra_body={'temperature': 0.5, 'max_tokens': 50},
		)
		print(response)

	except zai.core._errors.APIRequestFailedError as err:
		print(err)
	except zai.core._errors.APIInternalError as err:
		print(err)
	except zai.core._errors.APIStatusError as err:
		print(err)


def test_completions_enable_web_search(logging_conf):
	logging.config.dictConfig(logging_conf)  # type: ignore
	client = ZaiClient()  # Fill in your own API Key
	try:
		# Generate request_id
		request_id = time.time()
		print(f'request_id:{request_id}')
		response = client.chat.completions.create(
			request_id=request_id,
			model='glm-4',  # Fill in the model name to call
			messages=[
				{
					'role': 'user',
					'content': 'As a marketing expert, please create an attractive slogan for my product',
				},
				{
					'role': 'assistant',
					'content': (
						'Of course, to create an attractive slogan, please tell me some information about your product'
					),
				},
				{'role': 'user', 'content': 'Z.ai Open Platform'},
				{
					'role': 'assistant',
					'content': 'Ignite the future, paint infinity - Z.AI, making innovation within reach!',
				},
				{'role': 'user', 'content': 'Create a more precise and attractive slogan'},
			],
			tools=[
				{
					'type': 'web_search',
					'web_search': {
						'search_query': 'Show me the admission rate of Tsinghua University',
						'search_result': True,
						'enable': True,
					},
				}
			],
			extra_body={'temperature': 0.5, 'max_tokens': 50},
			user_id='12345678',
		)
		print(response)

	except zai.core._errors.APIRequestFailedError as err:
		print(err)
	except zai.core._errors.APIInternalError as err:
		print(err)
	except zai.core._errors.APIStatusError as err:
		print(err)


def test_completions_sensitive_word_check(logging_conf):
	logging.config.dictConfig(logging_conf)  # type: ignore
	client = ZaiClient()  # Fill in your own API Key
	try:
		# Generate request_id
		request_id = time.time()
		print(f'request_id:{request_id}')
		response = client.chat.completions.create(
			request_id=request_id,
			model='glm-4',  # Fill in the model name to call
			stream=True,
			messages=[
				{
					'role': 'user',
					'content': 'As a marketing expert, please create an attractive slogan for my product',
				},
				{
					'role': 'assistant',
					'content': (
						'Of course, to create an attractive slogan, please tell me some information about your product'
					),
				},
				{'role': 'user', 'content': 'Z.ai Open Platform'},
				{
					'role': 'assistant',
					'content': 'Ignite the future, paint infinity - Z.AI, making innovation within reach!',
				},
				{'role': 'user', 'content': 'Create a more precise and attractive slogan'},
			],
			extra_body={'temperature': 0.5, 'max_tokens': 50},
			user_id='12345678',
		)
		for item in response:
			print(item)

	except zai.core._errors.APIRequestFailedError as err:
		print(err)
	except zai.core._errors.APIInternalError as err:
		print(err)
	except zai.core._errors.APIStatusError as err:
		print(err)


# Function to encode the image
def encode_image(image_path):
	import base64

	with open(image_path, 'rb') as image_file:
		return base64.b64encode(image_file.read()).decode('utf-8')


def test_completions_stream_with_tools(logging_conf):
	logging.config.dictConfig(logging_conf)  # type: ignore
	client = ZaiClient()  # Fill in your own API Key
	try:
		# Generate request_id
		request_id = time.time()
		print(f'request_id:{request_id}')
		response = client.chat.completions.create(
			request_id=request_id,
			model='glm-4.6v',  # Fill in the model name to call
			extra_body={'temperature': 0.5, 'max_tokens': 50},
			messages=[
				{
					'role': 'user',
					'content': [
						{'type': 'text', 'text': 'What is in this image?'},
						{
							'type': 'image_url',
							'image_url': {
								'url': 'https://img1.baidu.com/it/u=1369931113,3388870256&fm=253&app=138&size=w931&n=0&f=JPEG&fmt=auto?sec=1703696400&t=f3028c7a1dca43a080aeb8239f09cc2f'
							},
						},
					],
				}
			],
			user_id='12345678',
		)
		print(response)

	except zai.core._errors.APIRequestFailedError as err:
		print(err)
	except zai.core._errors.APIInternalError as err:
		print(err)
	except zai.core._errors.APIStatusError as err:
		print(err)


def test_completions_vis_base64(test_file_path, logging_conf):
	logging.config.dictConfig(logging_conf)  # type: ignore
	client = ZaiClient()  # Fill in your own API Key
	try:
		base64_image = encode_image(os.path.join(test_file_path, 'img/MetaGLM.png'))
		# Generate request_id
		request_id = time.time()
		print(f'request_id:{request_id}')
		response = client.chat.completions.create(
			request_id=request_id,
			model='glm-4.6v',  # Fill in the model name to call
			extra_body={'temperature': 0.5, 'max_tokens': 50},
			messages=[
				{
					'role': 'user',
					'content': [
						{'type': 'text', 'text': 'What is in this image?'},
						# {
						#     "type": "image_url",
						#     "image_url": {
						#         "url": "https://img1.baidu.com/it/u=1369931113,3388870256&fm=253&app=138&size=w931&n=0&f=JPEG&fmt=auto?sec=1703696400&t=f3028c7a1dca43a080aeb8239f09cc2f"
						#     }
						# },
						{
							'type': 'image_url',
							'image_url': {'url': f'data:image/jpeg;base64,{base64_image}'},
						},
					],
				}
			],
			user_id='12345678',
		)
		print(response)

	except zai.core._errors.APIRequestFailedError as err:
		print(err)
	except zai.core._errors.APIInternalError as err:
		print(err)
	except zai.core._errors.APIStatusError as err:
		print(err)


def test_async_completions(logging_conf):
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
					'content': 'As a marketing expert, please create an attractive slogan for my product',
				},
				{
					'role': 'assistant',
					'content': (
						'Of course, to create an attractive slogan, please tell me some information about your product'
					),
				},
				{'role': 'user', 'content': 'Z.ai Open Platform'},
				{
					'role': 'assistant',
					'content': 'Ignite the future, paint infinity - Z.AI, making innovation within reach!',
				},
				{'role': 'user', 'content': 'Create a more precise and attractive slogan'},
			],
			tools=[
				{
					'type': 'web_search',
					'web_search': {
						'search_query': 'Show me the admission rate of Tsinghua University',
						'search_result': True,
					},
				}
			],
			extra_body={'temperature': 0.5, 'max_tokens': 50},
			user_id='12345678',
		)
		print(response)

	except zai.core._errors.APIRequestFailedError as err:
		print(err)
	except zai.core._errors.APIInternalError as err:
		print(err)
	except zai.core._errors.APIStatusError as err:
		print(err)


def test_retrieve_completion_result(logging_conf):
	logging.config.dictConfig(logging_conf)  # type: ignore
	client = ZaiClient()  # Fill in your own API Key
	try:
		response = client.chat.asyncCompletions.retrieve_completion_result(id='1014908592669352541651237')
		print(response)

	except zai.core._errors.APIRequestFailedError as err:
		print(err)
	except zai.core._errors.APIInternalError as err:
		print(err)
	except zai.core._errors.APIStatusError as err:
		print(err)


def test_completions_vis(logging_conf):
	logging.config.dictConfig(logging_conf)  # type: ignore
	client = ZaiClient()  # Fill in your own API Key
	try:
		# Generate request_id
		request_id = time.time()
		print(f'request_id:{request_id}')
		response = client.chat.completions.create(
			request_id=request_id,
			model='glm-4',
			messages=[{'role': 'user', 'content': 'tell me a joke'}],
			top_p=1,
			temperature=0.9,
			max_tokens=2000,
			sensitive_word_check={'type': 'ALL', 'status': 'DISABLE'},
			user_id='12345678',
		)
		print(response)

	except zai.core._errors.APIRequestFailedError as err:
		print(err)
	except zai.core._errors.APIInternalError as err:
		print(err)
	except zai.core._errors.APIStatusError as err:
		print(err)
