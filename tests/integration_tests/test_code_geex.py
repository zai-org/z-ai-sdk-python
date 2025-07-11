import logging
import logging.config
import time

import zai
from zai import ZaiClient


def test_code_geex(logging_conf):
	logging.config.dictConfig(logging_conf)  # type: ignore
	client = ZaiClient()  # Fill in your own API Key
	try:
		# Generate request_id
		request_id = time.time()
		print(f'request_id:{request_id}')
		response = client.chat.completions.create(
			request_id=request_id,
			model='codegeex-4',
			messages=[
				{
					'role': 'system',
					'content': """I am CodeGeeX, an intelligent programming assistant. 
					I can answer any programming, coding, and computer-related questions, 
					providing well-formatted, executable, accurate, 
					and secure code with detailed explanations when needed.
                    Task: Please provide well-formatted comments for the input code, 
					including both multi-line and single-line comments. 
					Note that the original code should not be modified - only add comments.
                    Please respond in English.""",
				},
				{'role': 'user', 'content': """Write a quicksort function"""},
			],
			top_p=0.7,
			temperature=0.9,
			max_tokens=2000,
			stop=['<|endoftext|>', '<|user|>', '<|assistant|>', '<|observation|>'],
			extra={
				'target': {
					'path': '11111',
					'language': 'Python',
					'code_prefix': 'EventSource.Factory factory = EventSources.createFactory(OkHttpUtils.getInstance());',
					'code_suffix': 'TaskMonitorLocal taskMonitorLocal = getTaskMonitorLocal(algoMqReq);',
				},
				'contexts': [
					{
						'path': '/1/2',
						'code': 'if(!sensitiveUser){ZpTraceUtils.addAsyncAttribute(algoMqReq.getTaskOrderNo(), ApiTraceProperty.request_params.getCode(), modelSendMap);',
					}
				],
			},
		)
		print(response)

	except zai.core._errors.APIRequestFailedError as err:
		print(err)
	except zai.core._errors.APIInternalError as err:
		print(err)
	except zai.core._errors.APIStatusError as err:
		print(err)


def test_code_geex_async(logging_conf):
	logging.config.dictConfig(logging_conf)  # type: ignore
	client = ZaiClient()  # Fill in your own API Key
	try:
		# Generate request_id
		request_id = time.time()
		print(f'request_id:{request_id}')
		response = client.chat.asyncCompletions.create(
			request_id=request_id,
			model='codegeex-4',
			messages=[
				{
					'role': 'system',
					'content': """I am CodeGeeX, an intelligent programming assistant. 
					I can answer any programming, coding, and computer-related questions, 
					providing well-formatted, executable, accurate, 
					and secure code with detailed explanations when needed.
                    Task: Please provide well-formatted comments for the input code, 
					including both multi-line and single-line comments. 
					Note that the original code should not be modified - only add comments.
                    Please respond in English.""",
				},
				{'role': 'user', 'content': """Write a quicksort function"""},
			],
			top_p=0.7,
			temperature=0.9,
			max_tokens=2000,
			stop=['<|endoftext|>', '<|user|>', '<|assistant|>', '<|observation|>'],
			extra={
				'target': {
					'path': '11111',
					'language': 'Python',
					'code_prefix': (
						'EventSource.Factory factory = EventSources.createFactory(OkHttpUtils.getInstance());'
					),
					'code_suffix': 'TaskMonitorLocal taskMonitorLocal = getTaskMonitorLocal(algoMqReq);',
				},
				'contexts': [
					{
						'path': '/1/2',
						'code': (
							'if(!sensitiveUser){ZpTraceUtils.addAsyncAttribute(algoMqReq.getTaskOrderNo(),'
							' ApiTraceProperty.request_params.getCode(), modelSendMap);'
						),
					}
				],
			},
		)
		print(response)

	except zai.core._errors.APIRequestFailedError as err:
		print(err)
	except zai.core._errors.APIInternalError as err:
		print(err)
	except zai.core._errors.APIStatusError as err:
		print(err)


def test_geex_result(logging_conf):
	logging.config.dictConfig(logging_conf)  # type: ignore
	client = ZaiClient()  # Please fill in your own API Key
	try:
		response = client.chat.asyncCompletions.retrieve_completion_result(id='1014908807577524653187108')
		print(response)

	except zai.core._errors.APIRequestFailedError as err:
		print(err)
	except zai.core._errors.APIInternalError as err:
		print(err)
	except zai.core._errors.APIStatusError as err:
		print(err)
