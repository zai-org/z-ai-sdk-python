# ZaiClient Open Platform Python SDK

[![PyPI version](https://img.shields.io/pypi/v/zai.svg)](https://pypi.org/project/zai/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)

[中文文档](README_CN.md) | English

The official Python SDK for ZaiClient's large model open interface, making it easier for developers to call ZaiClient's open APIs.

## ✨ Features

- **Type Safety**: Complete type annotations for all interfaces
- **Easy Integration**: Simple initialization and intuitive method calls
- **High Performance**: Built-in connection pooling and request optimization
- **Secure**: Automatic token caching and secure API key management
- **Lightweight**: Minimal dependencies with efficient resource usage
- **Streaming Support**: Real-time streaming responses for chat completions

## 📦 Installation

### Requirements

- **Python**: 3.9+
- **Package Manager**: pip

### Install via pip

```bash
pip install zai
```

### Core Dependencies

| Package | Version | Purpose |
|---------|---------|----------|
| `httpx` | `>=0.23.0` | HTTP client for API requests |
| `pydantic` | `>=1.9.0,<3.0.0` | Data validation and serialization |
| `typing-extensions` | `>=4.0.0` | Enhanced type hints support |

## 🚀 Quick Start

### Basic Usage

```python
from zai import ZaiClient

# Initialize client
client = ZaiClient(api_key="your-api-key")

# Create chat completion
response = client.chat.completions.create(
    model="glm-4",
    messages=[
        {"role": "user", "content": "Hello, ZaiClient!"}
    ]
)
print(response.choices[0].message.content)
```

### Client Configuration

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

### Basic Chat

```python
from zai import ZaiClient

client = ZaiClient(api_key="your-api-key")  # Uses environment variable ZAI_API_KEY
response = client.chat.completions.create(
    model="glm-4",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is artificial intelligence?"}
    ],
    tools=[
        {
            "type": "web_search",
            "web_search": {
                "search_query": "Search the Z.ai",
                "search_result": True,
            }
        }
    ],
    extra_body={"temperature": 0.5, "max_tokens": 50}
)
print(response)
```

### Streaming Chat

```python
from zai import ZaiClient

client = ZaiClient(api_key="your-api-key")
response = client.chat.completions.create(
    model="glm-4",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Tell me a story about AI."}
    ],
    stream=True
)

for chunk in response:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content)
```

### Multimodal Chat

```python
import base64
from zai import ZaiClient

def encode_image(image_path):
    """Encode image to base64 format"""
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

client = ZaiClient(api_key="your-api-key")
base64_image = encode_image("path/to/your/image.jpg")

response = client.chat.completions.create(
    model="glm-4v",
    extra_body={"temperature": 0.5, "max_tokens": 50},
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "What's in this image?"
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_image}"
                    }
                }
            ]
        }
    ]
)
print(response)
```

### Character Role-Playing

```python
from zai import ZaiClient

client = ZaiClient(api_key="your-api-key")
response = client.chat.completions.create(
    model="charglm-3",
    messages=[
        {
            "role": "user",
            "content": "Hello, how are you doing lately?"
        }
    ],
    meta={
        "user_info": "I am a film director who specializes in music-themed movies.",
        "bot_info": "You are a popular domestic female singer and actress with outstanding musical talent.",
        "bot_name": "Xiaoya",
        "user_name": "Director"
    }
)
print(response)
```

### Assistant Conversation

```python
from zai import ZaiClient

client = ZaiClient(api_key="your-api-key")
response = client.assistant.conversation(
    assistant_id="your_assistant_id",
    model="glm-4-assistant",
    messages=[
        {
            "role": "user",
            "content": [{
                "type": "text",
                "text": "Help me search for the latest ZaiClient product information"
            }]
        }
    ],
    stream=True,
    attachments=None,
    metadata=None,
    request_id="request_1790291013237211136",
    user_id="12345678"
)

for chunk in response:
    print(chunk)
```

### Video Generation

```python
from zai import ZaiClient

client = ZaiClient(api_key="your-api-key")
response = client.videos.generations(
    model="cogvideo",
    prompt="A beautiful sunset beach scene",
    user_id="user_12345"
)
print(response)
```

## 🚨 Error Handling

The SDK provides comprehensive error handling:

```python
from zai import ZaiClient
import zai

client = ZaiClient()

try:
    response = client.chat.completions.create(
        model="glm-4",
        messages=[
            {"role": "user", "content": "Hello, ZaiClient!"}
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

For questions and technical support, please visit [ZaiClient Open Platform](https://open.bigmodel.cn/) or check our documentation.
  
