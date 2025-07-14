# Z.ai Open Platform Python SDK

[![PyPI version](https://img.shields.io/pypi/v/zai-sdk.svg)](https://pypi.org/project/zai-sdk/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)

[中文文档](README_CN.md) | English

[Z.ai Open Platform](https://docs.z.ai/) The official Python SDK for Z.ai's large model open interface, making it easier for developers to call Z.ai's open APIs.

## ✨ Core Features

### 🤖 **Chat Completions**
- **Standard Chat**: Create chat completions with various models including `glm-4`, `charglm-3`
- **Streaming Support**: Real-time streaming responses for interactive applications
- **Tool Calling**: Function calling capabilities for enhanced AI interactions
- **Character Role-Playing**: Support for character-based conversations with `charglm-3` model
- **Multimodal Chat**: Image understanding capabilities with vision models

### 🧠 **Embeddings**
- **Text Embeddings**: Generate high-quality vector embeddings for text
- **Configurable Dimensions**: Customizable embedding dimensions
- **Batch Processing**: Support for multiple inputs in a single request

### 🎥 **Video Generation**
- **Text-to-Video**: Generate videos from text prompts
- **Image-to-Video**: Create videos from image inputs
- **Customizable Parameters**: Control quality, duration, FPS, and size
- **Audio Support**: Optional audio generation for videos

### 🎵 **Audio Processing**
- **Speech Transcription**: Convert audio files to text
- **Multiple Formats**: Support for various audio file formats

### 🤝 **Assistant API**
- **Conversation Management**: Structured conversation handling
- **Streaming Conversations**: Real-time assistant interactions
- **Metadata Support**: Rich conversation context and user information

### 🔧 **Advanced Tools**
- **Web Search**: Integrated web search capabilities
- **File Management**: Upload, download, and manage files
- **Batch Operations**: Efficient batch processing for multiple requests
- **Knowledge Base**: Knowledge management and retrieval
- **Content Moderation**: Built-in content safety and moderation
- **Image Generation**: AI-powered image creation
- **Fine-tuning**: Custom model training capabilities

## 📦 Installation

### Requirements

- **Python**: 3.9+
- **Package Manager**: pip

### Install via pip

```bash
pip install zai-sdk
```

### 📋 **Technical Specifications**

#### **Python Support**
- **Python Versions**: 3.8, 3.9, 3.10, 3.11, 3.12
- **Async Support**: Full async/await compatibility
- **Cross-platform**: Windows, macOS, Linux support

#### **Core Dependencies**

| Package | Version | Purpose |
|---------|---------|----------|
| `httpx` | `>=0.23.0` | HTTP client for API requests |
| `pydantic` | `>=1.9.0,<3.0.0` | Data validation and serialization |
| `typing-extensions` | `>=4.0.0` | Enhanced type hints support |
| `cachetools` | `>=4.2.2` | Caching utilities |
| `pyjwt` | `>=2.8.0` | JSON Web Token (JWT) handling |

## 🚀 Quick Start

### Create API Key
1. **Create client with API key**
2. **Call the corresponding API methods**

For complete examples, please refer to the open platform [API Reference](https://docs.z.ai/api-reference/) and [User Guide](https://docs.z.ai/guides/), and remember to replace with your own API key.

### Basic Usage

```python
from zai import ZaiClient

# Initialize client
client = ZaiClient(api_key="your-api-key")

# Create chat completion
response = client.chat.completions.create(
    model="glm-4",
    messages=[
        {"role": "user", "content": "Hello, Z.ai!"}
    ]
)
print(response.choices[0].message.content)
```

### Client Configuration

The SDK supports multiple ways to configure API keys:

#### Environment Variables

```bash
export ZAI_API_KEY="your-api-key"
export ZAI_BASE_URL="https://api.z.ai/api/paas/v4/"  # Optional
```

#### Code Configuration

```python
from zai import ZaiClient

client = ZaiClient(
    api_key="your-api-key",
    base_url="https://api.z.ai/api/paas/v4/"  # Optional
)
```

### Advanced Configuration

Customize client behavior with additional parameters:

```python
from zai import ZaiClient
import httpx

client = ZaiClient(
    api_key="your-api-key",
    timeout=httpx.Timeout(timeout=300.0, connect=8.0),  # Request timeout
    max_retries=3,  # Retry attempts
    base_url="https://api.z.ai/api/paas/v4/"  # Custom API endpoint
)
```

## 📖 Usage Examples

### Streaming Chat

```python
from zai import ZaiClient

# Initialize client
client = ZaiClient(api_key="your-api-key")

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
```

### Chat With Tool Call

```python
from zai import ZaiClient

# Initialize client
client = ZaiClient(api_key="your-api-key")

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
```

### Multimodal Chat

```python
from zai import ZaiClient
import base64

def encode_image(image_path):
    """Encode image to base64 format"""
    with open(image_path, 'rb') as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

client = ZaiClient(api_key="your-api-key")
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
```

### Character Role-Playing

```python
from zai import ZaiClient

# Initialize client
client = ZaiClient(api_key="your-api-key")

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
```

### Assistant Conversation

```python
from zai import ZaiClient

# Initialize client
client = ZaiClient(api_key="your-api-key")

# Create assistant conversation
response = client.assistant.conversation(
    # You can use 65940acff94777010aa6b796 for testing
    # or you can create your own assistant_id in ZhipuAI console
    assistant_id='your own assistant_id',
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
```

### Video Generation

```python
from zai import ZaiClient
client = ZaiClient(api_key="your-api-key")

# Generate video
response = client.videos.generations(
    model="cogvideox-2",
    prompt="A cat is playing with a ball.",
    quality="quality",  # Output mode, "quality" for quality priority, "speed" for speed priority
    with_audio=True, # Whether to include audio
    size="1920x1080",  # Video resolution, supports up to 4K (e.g., "3840x2160")
    fps=30,  # Frame rate, can be 30 or 60
    max_wait_time=300,  # Maximum wait time (seconds)
)
print(response)

# Get video result
result = client.videos.retrieve_videos_result(id=response.id)
print(result)
```

## 🚨 Error Handling

The SDK provides comprehensive error handling:

```python
from zai import ZaiClient
import zai

client = ZaiClient(api_key="your-api-key")

try:
    response = client.chat.completions.create(
        model="glm-4",
        messages=[
            {"role": "user", "content": "Hello, Z.ai!"}
        ]
    )
    print(response.choices[0].message.content)
    
except zai.APIStatusError as err:
    print(f"API Status Error: {err}")
except zai.APITimeoutError as err:
    print(f"Request Timeout: {err}")
except Exception as err:
    print(f"Unexpected Error: {err}")
```

### Error Codes

| Status Code | Error Type | Description |
|-------------|------------|-------------|
| 400 | `APIRequestFailedError` | Invalid request parameters |
| 401 | `APIAuthenticationError` | Authentication failed |
| 429 | `APIReachLimitError` | Rate limit exceeded |
| 500 | `APIInternalError` | Internal server error |
| 503 | `APIServerFlowExceedError` | Server overloaded |
| N/A | `APIStatusError` | General API error |

## 📈 Version Updates

For detailed version history and update information, please see [Release-Note.md](Release-Note.md).

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📞 Support

For questions and technical support, please visit [Z.ai Open Platform](https://docs.z.ai/) or check our documentation.

### Contact Us

For feedback and support, please contact us at: **user_feedback@z.ai**
