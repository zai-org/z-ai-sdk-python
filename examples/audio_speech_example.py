from zai import ZaiClient
import os
import traceback
import uuid


# Change working directory to project root
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(script_dir)
os.chdir(project_root)


def text_to_speech_non_stream():
	# Initialize client
	client = ZaiClient()

	# Audio format
	# Supported response formats: wav, pcm (default)
	response_format = 'pcm'

	try:
		# Generate speech audio from text
		response = client.audio.speech(
			model='glm-tts',
			input='Hello, this is a test for text-to-speech functionality.',
			voice='tongtong',
			response_format=response_format,
			stream=False
		)

		# Save audio to file with unique name
		output_file = f"audio_speech_{uuid.uuid4()}.{response_format}"
		with open(output_file, 'wb') as f:
			f.write(response.content)

		print(f"Audio saved to {os.path.abspath(output_file)}")
	except Exception as e:
		print(f"Exception: {e}\nTraceback: {traceback.format_exc()}")
		raise


def text_to_speech_stream():
	# Initialize client
	client = ZaiClient()

	# Audio format
	# Streaming only supports pcm format
	response_format = 'pcm'

	try:
		# Generate speech audio with streaming
		response = client.audio.speech(
			model='glm-tts',
			input='Hello, this is a test for text-to-speech functionality.',
			voice='tongtong',
			response_format=response_format,
			stream=True
		)

		# Process streaming response
		chunk_index = 0
		for chunk in response:
			try:
				choice = chunk.choices[0]
				if choice.delta is None:
					break
				if choice.delta.content:
					print(f"[Chunk {chunk_index}] {choice.delta.content}")
					chunk_index += 1
			except (AttributeError, IndexError) as e:
				print(f"Exception: {e}\nTraceback: {traceback.format_exc()}")
	except Exception as e:
		print(f"Exception: {e}\nTraceback: {traceback.format_exc()}")
		raise


if __name__ == '__main__':
	# Non-streaming text to speech
	text_to_speech_non_stream()

	# Streaming text to speech
	# text_to_speech_stream()
