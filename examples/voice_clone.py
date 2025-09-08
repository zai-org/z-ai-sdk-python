from zai import ZaiClient, ZhipuAiClient
import time
import os

def voice_clone():
	# Initialize client
	client = ZhipuAiClient()

	# Step 1: Upload the voice input audio file
	# First, we need to upload the voice sample audio file to get a file ID
	voice_input_file_path = "tests/integration_tests/voice_clone_input.mp3"
	
	try:
		with open(voice_input_file_path, 'rb') as f:
			upload_response = client.files.create(
				file=f,
				purpose='voice-clone-input',
			)
		
		print(f"Voice input file uploaded successfully with ID: {upload_response.id}")
		file_id = upload_response.id
		
	except FileNotFoundError:
		print(f"File not found: {voice_input_file_path}")
		return
	except Exception as e:
		print(f"File upload failed: {e}")
		return

	# Step 2: Clone voice using the uploaded file ID
	response = client.voice.clone(
		voice_name="My Test Voice!",
		text="This is sample text for voice cloning training",
		input="This is target text for voice preview generation",
		file_id=file_id,
		request_id=f"voice_clone_request_{int(time.time() * 1000)}",
		model="cogtts-clone"
	)
	print(f"Voice clone response: {response}")

def voice_delete():
	# Initialize client
	client = ZhipuAiClient()

	# Delete voice
	response = client.voice.delete(
		voice="Your voice id",
		request_id=f"voice_delete_request_{int(time.time() * 1000)}"
	)
	print(response)

def voice_list():
	# Initialize client
	client = ZhipuAiClient()

	# List voices with filter
	response = client.voice.list(
		voice_type="PRIVATE",
		voice_name="Test",
		request_id=f"voice_list_request_{int(time.time() * 1000)}"
	)
	print(response)

if __name__ == "__main__":
	# voice_clone()

	# voice_delete()

	voice_list()