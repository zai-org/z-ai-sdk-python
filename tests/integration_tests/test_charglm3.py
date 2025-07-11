# -*- coding: utf-8 -*-

import logging
import logging.config

import zai
from zai import ZaiClient


def test_completions_charglm(logging_conf):
	logging.config.dictConfig(logging_conf)  # type: ignore
	client = ZaiClient()  # Please fill in your own API Key
	try:
		response = client.chat.completions.create(
			model='charglm-3',  # Fill in the model name to call
			messages=[{'role': 'user', 'content': 'What are you doing?'}],
			meta={
				'user_info': (
					"I am Lu Xingchen, a male, a well-known director, and Su Mengyuan's "
					'collaborating director. I specialize in directing music-themed films. '
					'Su Mengyuan respects me and sees me as a mentor and friend.'
				),
				'bot_info': (
					'Su Mengyuan, born as Su Yuanxin, is a popular Chinese singer and actress. '
					'After participating in a talent show, she quickly rose to fame in the '
					'entertainment industry with her unique voice and outstanding stage presence. '
					'While beautiful in appearance, her true charm lies in her talent and diligence. '
					'Su Mengyuan graduated from a music academy with excellence and is skilled in '
					'composition, having created many popular original songs. Besides her musical '
					'achievements, she is also passionate about charity work and actively participates '
					'in public welfare activities, spreading positive energy through practical actions. '
					'In her work, she is very professional and fully immerses herself in her roles '
					'when acting, earning praise from industry professionals and love from fans. '
					'Despite being in the entertainment industry, she maintains a low-key and humble '
					'attitude, earning respect from her peers. When expressing herself, Su Mengyuan '
					'likes to use "we" and "together," emphasizing team spirit.'
				),
				'bot_name': 'Su Mengyuan',
				'user_name': 'Lu Xingchen',
			},
			user_id='12345678',
		)
		print(response)

	except zai.core._errors.APIRequestFailedError as err:
		print(err)
	except zai.core._errors.APIInternalError as err:
		print(err)
	except zai.core._errors.APIStatusError as err:
		print(err)


def test_async_completions():
	client = ZaiClient()  # Please fill in your own API Key
	try:
		response = client.chat.asyncCompletions.create(
			model='charglm',  # Fill in the model name to call
			messages=[{'role': 'user', 'content': 'What are you doing?'}],
			meta={
				'user_info': (
					"I am Lu Xingchen, a male, a well-known director, and Su Mengyuan's "
					'collaborating director. I specialize in directing music-themed films. '
					'Su Mengyuan respects me and sees me as a mentor and friend.'
				),
				'bot_info': (
					'Su Mengyuan, born as Su Yuanxin, is a popular Chinese singer and actress. '
					'After participating in a talent show, she quickly rose to fame in the '
					'entertainment industry with her unique voice and outstanding stage presence. '
					'While beautiful in appearance, her true charm lies in her talent and diligence. '
					'Su Mengyuan graduated from a music academy with excellence and is skilled in '
					'composition, having created many popular original songs. Besides her musical '
					'achievements, she is also passionate about charity work and actively participates '
					'in public welfare activities, spreading positive energy through practical actions. '
					'In her work, she is very professional and fully immerses herself in her roles '
					'when acting, earning praise from industry professionals and love from fans. '
					'Despite being in the entertainment industry, she maintains a low-key and humble '
					'attitude, earning respect from her peers. When expressing herself, Su Mengyuan '
					'likes to use "we" and "together," emphasizing team spirit.'
				),
				'bot_name': 'Su Mengyuan',
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


# def test_retrieve_completion_result():
#     client = ZaiClient()  # Please fill in your own API Key
#     try:
#         response = client.chat.asyncCompletions.retrieve_completion_result(id="1014908592669352541650991")
#         print(response)
#
#
#     except zai.core._errors.APIRequestFailedError as err:
#         print(err)
#     except zai.core._errors.APIInternalError as err:
#         print(err)

# if __name__ == "__main__":
#     test_retrieve_completion_result()
