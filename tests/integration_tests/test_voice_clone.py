import logging
import logging.config
import time
from pathlib import Path

import zai
from zai import ZaiClient

def test_voice_clone(logging_conf):
	"""Test voice cloning with existing file ID"""
	logging.config.dictConfig(logging_conf)  # type: ignore
	client = ZaiClient()  # Fill in your own API Key
	
	try:
		# Upload file first
		voice_input_file_path = Path(__file__).parent / 'voice_clone_input.mp3'
		with open(voice_input_file_path, 'rb') as f:
			upload_response = client.files.create(
				file=f,
				purpose='voice-clone-input',
			)
		
		# Clone voice
		request_id = f"voice_clone_only_test_{int(time.time() * 1000)}"
		response = client.voice.clone(
			voice_name="Test Voice Clone Only",
			voice_text_input="This is sample text for voice cloning training",
			voice_text_output="This is target text for voice preview generation",
			file_id=upload_response.id,
			request_id=request_id
		)
		print(f"Voice clone response: {response}")
		
	except FileNotFoundError:
		print("Voice input file not found: voice_clone_input.mp3")
	except zai.core._errors.APIRequestFailedError as err:
		print(f"API Request Failed: {err}")
	except zai.core._errors.APIInternalError as err:
		print(f"API Internal Error: {err}")
	except zai.core._errors.APIStatusError as err:
		print(f"API Status Error: {err}")


def test_voice_list(logging_conf):
	"""Test voice listing functionality"""
	logging.config.dictConfig(logging_conf)  # type: ignore
	client = ZaiClient()  # Fill in your own API Key
	
	try:
		request_id = f"voice_list_test_{int(time.time() * 1000)}"
		response = client.voice.list(
			voice_type="PRIVATE",
			request_id=request_id
		)
		print(f"Voice list response: {response}")
		
	except zai.core._errors.APIRequestFailedError as err:
		print(f"API Request Failed: {err}")
	except zai.core._errors.APIInternalError as err:
		print(f"API Internal Error: {err}")
	except zai.core._errors.APIStatusError as err:
		print(f"API Status Error: {err}")


def test_voice_delete(logging_conf):
	"""Test voice deletion functionality"""
	logging.config.dictConfig(logging_conf)  # type: ignore
	client = ZaiClient()  # Fill in your own API Key
	
	try:
		# Note: Replace with actual voice_id from a previous clone operation
		voice_id = "test_voice_id_placeholder"
		request_id = f"voice_delete_test_{int(time.time() * 1000)}"
		response = client.voice.delete(
			voice_id=voice_id,
			request_id=request_id
		)
		print(f"Voice delete response: {response}")
		
	except zai.core._errors.APIRequestFailedError as err:
		print(f"API Request Failed: {err}")
	except zai.core._errors.APIInternalError as err:
		print(f"API Internal Error: {err}")
	except zai.core._errors.APIStatusError as err:
		print(f"API Status Error: {err}")