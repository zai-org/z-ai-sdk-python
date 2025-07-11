# 智谱AI开放平台 Python SDK

[![PyPI version](https://img.shields.io/pypi/v/z-ai.svg)](https://pypi.org/project/z-ai/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/)

[English Readme](README.md)

[智谱AI开放平台](https://open.bigmodel.cn/dev/api)官方 Python SDK，帮助开发者快速集成智谱AI强大的人工智能能力到Python应用中。

## ✨ 特性

- 🚀 **类型安全**: 所有接口完全类型封装，无需查阅API文档即可完成接入
- 🔧 **简单易用**: 简洁直观的API设计，快速上手
- ⚡ **高性能**: 基于现代Python库构建，性能优异
- 🛡️ **安全可靠**: 内置身份验证和令牌管理
- 📦 **轻量级**: 最小化依赖，易于项目集成
- 🔄 **流式支持**: 支持SSE流式响应和异步调用

## 📦 安装

### 环境要求
- Python 3.9 或更高版本
- pip 包管理器

### 使用 pip 安装

```sh
pip install z-ai
```

### 📋 核心依赖

本SDK使用以下核心依赖库：

| 依赖库 | 用途 |
|--------|------|
| httpx | HTTP客户端库 |
| pydantic | 数据验证和序列化 |
| typing-extensions | 类型注解扩展 |

## 🚀 快速开始

### 基本用法

1. **使用API密钥创建客户端**
2. **调用相应的API方法**

完整示例请参考开放平台[接口文档](https://open.bigmodel.cn/dev/api)以及[使用指南](https://open.bigmodel.cn/dev/howuse/)，记得替换为您自己的API密钥。

### 客户端配置

SDK支持多种方式配置API密钥：

**环境变量配置：**
```bash
export ZAI_API_KEY="your_api_key_here"
export ZAI_BASE_URL="https://api.z.ai/api/paas/v4/"  # 可选
```

**代码配置：**
```python
from zai import ZaiClient

client = ZaiClient(
    api_key="your_api_key_here",  # 填写您的 APIKey
) 
```
**高级配置：**

SDK提供了灵活的客户端配置选项：

```python
import httpx
from zai import ZaiClient

client = ZaiClient(
    api_key="your_api_key_here",
    timeout=httpx.Timeout(timeout=300.0, connect=8.0),  # 超时配置
    max_retries=3,  # 重试次数
    base_url="https://api.z.ai/api/paas/v4/"  # Custom API endpoint
)
```

**配置选项：**
- `timeout`: 控制接口连接和读取超时时间
- `max_retries`: 控制重试次数，默认为3次
- `base_url`: 自定义API基础URL


## 💡 使用示例

### 流式对话

```python
from zai import ZaiClient

# 初始化客户端
client = ZaiClient(api_key="your-api-key")

# 创建对话
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

### 工具调用

```python
from zai import ZaiClient

# 初始化客户端
client = ZaiClient(api_key="your-api-key")

# 创建对话
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

### 多模态对话

```python
from zai import ZaiClient
import base64

def encode_image(image_path):
    """将图片编码为base64格式"""
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
                {'type': 'text', 'text': "请描述这张图片的内容"},
                {'type': 'image_url', 'image_url': {'url': f'data:image/jpeg;base64,{base64_image}'}},
            ],
        }
    ],
    temperature=0.5,
    max_tokens=2000,
)
print(response)
```

### 角色扮演

```python
from zai import ZaiClient

# 初始化客户端
client = ZaiClient(api_key="your-api-key")

# 创建对话
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

### 智能体对话

```python
from zai import ZaiClient

# Initialize client
client = ZaiClient(api_key="your-api-key")

# Create assistant conversation
response = client.assistant.conversation(
    # 你可使用 65940acff94777010aa6b796 作为测试ID
    assistant_id='你的assistant_id',
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

### 视频生成

```python
from zai import ZaiClient

client = ZaiClient()  # 请填写您自己的APIKey

# 提交生成任务
response = client.videos.generations(
    model="cogvideox-2",  # 使用的视频生成模型
    image_url=image_url,  # 提供的图片URL地址或者 Base64 编码
    prompt="让画面动起来",  
    quality="speed",  # 输出模式，"quality"为质量优先，"speed"为速度优先
    with_audio=True,
    size="1920x1080",  # 视频分辨率，支持最高4K（如: "3840x2160"）
    fps=30,  # 帧率，可选为30或60
)
print(response)

# 获取生成结果
result = client.videos.retrieve_videos_result(id=response.id)
print(result)
```

## 🚨 异常处理

SDK提供了完善的异常处理机制：

```python
from zai import ZaiClient
import zai

client = ZaiClient(api_key="your-api-key")  # 请填写您自己的APIKey

try:
    response = client.chat.completions.create(
        model="glm-4",
        messages=[
            {"role": "user", "content": "你好，智谱AI！"}
        ]
    )
    print(response.choices[0].message.content)
    
except zai.APIStatusError as err:
    print(f"API状态错误: {err}")
except zai.APITimeoutError as err:
    print(f"请求超时: {err}")
except Exception as err:
    print(f"其他错误: {err}")
```

### 错误码说明

| 状态码 | 错误类型 | 说明 |
|--------|----------|------|
| 400 | `APIRequestFailedError` | 请求参数错误 |
| 401 | `APIAuthenticationError` | 身份验证失败 |
| 429 | `APIReachLimitError` | 请求频率超限 |
| 500 | `APIInternalError` | 服务器内部错误 |
| 503 | `APIServerFlowExceedError` | 服务器流量超限 |
| N/A | `APIStatusError` | 通用API错误 |

## 📈 版本更新

详细的版本更新记录和历史信息，请查看 [Release-Note.md](Release-Note.md)。

## 📄 许可证

本项目基于 MIT 许可证开源 - 详情请查看 [LICENSE](LICENSE) 文件。

## 🤝 贡献

欢迎贡献代码！请随时提交 Pull Request。

## 📞 支持

如有问题和技术支持，请访问 [Z.ai开放平台](https://docs.z.ai/) 或查看我们的文档。
  
