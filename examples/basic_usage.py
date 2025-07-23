from zai import ZaiClient
from zai import ZhipuClient

def completion():
	# Initialize client
	client = ZaiClient()

	# Create chat completion
	response = client.chat.completions.create(
		model='glm-4',
		messages=[{'role': 'user', 'content': 'Hello, Z.ai!'}],
		temperature=0.7,
	)
	print(response.choices[0].message.content)


def completion_with_stream():
	# Initialize client
	client = ZaiClient()

	# Create chat completion
	response = client.chat.completions.create(
		model='glm-4',
		messages=[
			{'role': 'system', 'content': 'You are a helpful assistant.'},
			{'role': 'user', 'content': 'Tell me a story about AI.'},
		],
		stream=True,
	)

	for chunk in response:
		if chunk.choices[0].delta.content:
			print(chunk.choices[0].delta.content, end='')


def completion_with_websearch():
	# Initialize client
	client = ZaiClient()

	# Create chat completion
	response = client.chat.completions.create(
		model='glm-4',
		messages=[
			{'role': 'system', 'content': 'You are a helpful assistant.'},
			{'role': 'user', 'content': 'What is artificial intelligence?'},
		],
		tools=[
			{
				'type': 'web_search',
				'web_search': {
					'search_query': 'What is artificial intelligence?',
					'search_result': True,
				},
			}
		],
		temperature=0.5,
		max_tokens=2000,
	)

	print(response)


def multi_modal_chat():
	import base64

	def encode_image(image_path):
		"""Encode image to base64 format"""
		with open(image_path, 'rb') as image_file:
			return base64.b64encode(image_file.read()).decode('utf-8')

	client = ZaiClient()
	base64_image = encode_image('examples/test_multi_modal.jpeg')

	response = client.chat.completions.create(
		model='glm-4v',
		messages=[
			{
				'role': 'user',
				'content': [
					{'type': 'text', 'text': "What's in this image?"},
					{'type': 'image_url', 'image_url': {'url': f'data:image/jpeg;base64,{base64_image}'}},
				],
			}
		],
		temperature=0.5,
		max_tokens=2000,
	)
	print(response)


def role_play():
	# Initialize client
	client = ZaiClient()

	# Create chat completion
	response = client.chat.completions.create(
		model='charglm-3',
		messages=[{'role': 'user', 'content': 'Hello, how are you doing lately?'}],
		meta={
			'user_info': 'I am a film director who specializes in music-themed movies.',
			'bot_info': 'You are a popular domestic female singer and actress with outstanding musical talent.',
			'bot_name': 'Alice',
			'user_name': 'Director',
		},
	)
	print(response)


def assistant_conversation():
	# Initialize client
	client = ZaiClient()

	# Create assistant conversation
	response = client.assistant.conversation(
		assistant_id='65940acff94777010aa6b796',  # You can use 65940acff94777010aa6b796 for testing
		model='glm-4-assistant',
		messages=[
			{
				'role': 'user',
				'content': [
					{
						'type': 'text',
						'text': 'Help me search for the latest ZhipuAI product information',
					}
				],
			}
		],
		stream=True,
		attachments=None,
		metadata=None,
		request_id='request_1790291013237211136',
		user_id='12345678',
	)

	for chunk in response:
		if chunk.choices[0].delta.type == 'content':
			print(chunk.choices[0].delta.content, end='')


def video_generation():
	# Initialize client
	client = ZaiClient()

	# Create video generation
	response = client.videos.generations(
		model='cogvideo', prompt='A beautiful sunset beach scene', user_id='user_12345'
	)
	print(response)


def audio_transcription():
	# Initialize client
	client = ZaiClient()

	# Create audio transcription
	response = client.audio.transcriptions.create(
		model='glm-4',
		file='audio.mp3',
	)
	print(response.text)

def ofZai():
    client = ZaiClient()
    print(client.base_url)
    response = client.chat.completions.create(
        model='glm-4',
        messages=[{'role': 'user', 'content': 'Hello, Z.ai!'}],
        temperature=0.7,
    )
    print(response.choices[0].message.content)

def ofZhipu():
	client = ZhipuClient()
	print(client.base_url)
	response = client.chat.completions.create(
		model='glm-4',
		messages=[{'role': 'user', 'content': 'Hello, Z.ai!'}],
		temperature=0.7,
	)
	print(response.choices[0].message.content)

if __name__ == '__main__':
    # completion()
	# completion_with_websearch()
	# multi_modal_chat()
	# role_play()
	# assistant_conversation()
	# video_generation()
    ofZai()
    ofZhipu()
 
