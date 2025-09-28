import logging
import logging.config
from pathlib import Path

import zai
from zai import ZaiClient


def test_audio_speech(logging_conf):
	logging.config.dictConfig(logging_conf)  # type: ignore
	client = ZaiClient(base_url='', api_key='')  # Fill in your own API Key
	try:
		speech_file_path = Path(__file__).parent / 'asr1.pcm'
		response = client.audio.speech(
			model='cogtts',
			input='Hello, welcome to Z.ai Open Platform',
			voice='female',
			response_format='pcm',
			encode_format='base64',
			speed=1.0,
			volume=1.0,
		)
		response.stream_to_file(speech_file_path)

	except zai.core._errors.APIRequestFailedError as err:
		print(err)
	except zai.core._errors.APIInternalError as err:
		print(err)
	except zai.core._errors.APIStatusError as err:
		print(err)


def test_audio_customization(logging_conf):
	logging.config.dictConfig(logging_conf)
	client = ZaiClient()  # Fill in your own API Key
	with open(Path(__file__).parent / 'asr.wav', 'rb') as file:
		try:
			speech_file_path = Path(__file__).parent / 'asr.wav'
			response = client.audio.customization(
				model='cogtts',
				input='Hello, welcome to Z.ai Open Platform',
				voice_text='This is a test case',
				voice_data=file,
				response_format='wav',
			)
			response.stream_to_file(speech_file_path)

		except zai.core._errors.APIRequestFailedError as err:
			print(err)
		except zai.core._errors.APIInternalError as err:
			print(err)
		except zai.core._errors.APIStatusError as err:
			print(err)
