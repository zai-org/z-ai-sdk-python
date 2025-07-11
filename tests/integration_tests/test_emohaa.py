# -*- coding: utf-8 -*-

import logging
import logging.config

import zai
from zai import ZaiClient


def test_completions_emohaa(logging_conf):
	logging.config.dictConfig(logging_conf)  # type: ignore
	client = ZaiClient()  # Please fill in your own API Key
	try:
		response = client.chat.completions.create(
			model='emohaa',  # Fill in the model name to call
			messages=[
				{
					'role': 'assistant',
					'content': 'Hello, I am Emohaa. Nice to meet you. How can I help you today?',
				},
				{
					'role': 'user',
					'content': (
						"Today is my day off. I decided to take a stroll in Xi'an Baomi,"
						' wearing my favorite smoky wood fragrance.'
					),
				},
				{
					'role': 'assistant',
					'content': (
						"Today is my day off. I decided to take a stroll in Xi'an Baomi,"
						' wearing my favorite smoky wood fragrance.'
					),
				},
			],
			meta={
				'user_info': '30-year-old male software engineer interested in reading, hiking and programming',
				'bot_info': (
					"Emohaa is an emotional support AI based on Hill's helping "
					'theory with professional counseling skills'
				),
				'bot_name': 'Emohaa',
				'user_name': 'Lu Xingchen',
			},
		)
		print(response)

	except zai.core._errors.APIRequestFailedError as err:
		print(err)
	except zai.core._errors.APIInternalError as err:
		print(err)
	except zai.core._errors.APIStatusError as err:
		print(err)
