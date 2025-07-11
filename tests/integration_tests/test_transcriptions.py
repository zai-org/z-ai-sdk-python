import logging
import logging.config
from pathlib import Path

import zai
from zai import ZaiClient


def test_transcriptions(logging_conf):
	logging.config.dictConfig(logging_conf)  # type: ignore
	client = ZaiClient()  # Fill in your own API Key
	try:
		with open(Path(__file__).parent / 'asr1.wav', 'rb') as audio_file:
			transcriptResponse = client.audio.transcriptions.create(model='glm-asr', file=audio_file, stream=False)
			print(transcriptResponse)
	except zai.core._errors.APIRequestFailedError as err:
		print(err)
	except zai.core._errors.APIInternalError as err:
		print(err)
	except zai.core._errors.APIStatusError as err:
		print(err)


def test_transcriptions_stream(logging_conf):
	logging.config.dictConfig(logging_conf)  # type: ignore
	client = ZaiClient()  # Fill in your own API Key
	try:
		with open(Path(__file__).parent / 'asr1.wav', 'rb') as audio_file:
			transcriptResponse = client.audio.transcriptions.create(model='glm-asr', file=audio_file, stream=True)
			for item in transcriptResponse:
				print(item)
	except zai.core._errors.APIRequestFailedError as err:
		print(err)
	except zai.core._errors.APIInternalError as err:
		print(err)
	except zai.core._errors.APIStatusError as err:
		print(err)
