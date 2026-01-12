from zai import ZaiClient
import os
import traceback


# Change working directory to project root
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(script_dir)
os.chdir(project_root)


def audio_transcription_non_stream():
	# Initialize client
	client = ZaiClient()

	# Audio file path
	# Supported formats: .wav, .mp3
	# File size limit: <= 25 MB, Duration limit: <= 30 seconds
	audio_file_path = "tests/integration_tests/asr.wav"

	# Check if file exists
	if not os.path.exists(audio_file_path):
		print(f"Audio file not found: {audio_file_path}")
		return

	try:
		# Open the audio file and create transcription
		with open(audio_file_path, 'rb') as audio_file:
			response = client.audio.transcriptions.create(
				model='glm-asr-2512',
				file=audio_file,
				stream=False
			)

		# Print transcription result
		print(response.text)
	except Exception as e:
		print(f"Exception: {e}\nTraceback: {traceback.format_exc()}")
		raise


def audio_transcription_stream():
	# Initialize client
	client = ZaiClient()

	# Audio file path
	# Supported formats: .wav, .mp3
	# File size limit: <= 25 MB, Duration limit: <= 30 seconds
	audio_file_path = "tests/integration_tests/asr.wav"

	# Check if file exists
	if not os.path.exists(audio_file_path):
		print(f"Audio file not found: {audio_file_path}")
		return

	try:
		# Open the audio file and create transcription with streaming
		with open(audio_file_path, 'rb') as audio_file:
			response = client.audio.transcriptions.create(
				model='glm-asr-2512',
				file=audio_file,
				stream=True
			)

		# Process streaming response
		print("Streaming transcription:")
		for chunk in response:
			try:
				if hasattr(chunk, 'delta') and chunk.delta:
					print(chunk.delta, flush=True)
			except (AttributeError, IndexError) as e:
				print(f"Exception: {e}\nTraceback: {traceback.format_exc()}")
	except Exception as e:
		print(f"Exception: {e}\nTraceback: {traceback.format_exc()}")
		raise


if __name__ == '__main__':
	# Non-streaming audio transcription
	audio_transcription_non_stream()

	# Streaming audio transcription
	# audio_transcription_stream()