#  Z.ai 开放平台 Python SDK

[![PyPI version](https://img.shields.io/pypi/v/zai-sdk.svg)](https://pypi.org/project/zai-sdk/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)

[English Readme](README.md)

[Z.ai 开放平台](https://docs.z.ai/)官方 Python SDK，帮助开发者快速集成 Z.ai 强大的人工智能能力到Python应用中。

## ✨ 核心功能

### 🤖 **对话补全**
- **标准对话**: 支持 `glm-4`、`charglm-3` 等多种模型的对话补全
- **流式支持**: 实时流式响应，适用于交互式应用
- **工具调用**: 函数调用能力，增强 AI 交互体验
- **角色扮演**: 支持基于 `charglm-3` 模型的角色对话
- **多模态对话**: 支持图像理解的视觉模型

### 🧠 **向量嵌入**
- **文本嵌入**: 生成高质量的文本向量嵌入
- **可配置维度**: 自定义嵌入向量维度
- **批量处理**: 单次请求支持多个输入

### 🎥 **视频生成**
- **文本生成视频**: 从文本提示生成视频
- **图像生成视频**: 从图像输入创建视频
- **参数可定制**: 控制质量、时长、帧率和尺寸
- **音频支持**: 可选的视频音频生成

### 🎵 **音频处理**
- **语音转录**: 将音频文件转换为文本
- **多格式支持**: 支持各种音频文件格式

### 🤝 **智能助手 API**
- **对话管理**: 结构化对话处理
- **流式对话**: 实时助手交互
- **元数据支持**: 丰富的对话上下文和用户信息

### 🔧 **高级工具**
- **网络搜索**: 集成的网络搜索功能
- **文件管理**: 上传、下载和管理文件
- **批量操作**: 多请求的高效批量处理
- **知识库**: 知识管理和检索
- **内容审核**: 内置内容安全和审核
- **图像生成**: AI 驱动的图像创建
- **模型微调**: 自定义模型训练功能

## 📦 安装

### 环境要求
- Python 3.9 或更高版本
- pip 包管理器

### 使用 pip 安装

```sh
pip install zai-sdk
```
### 📋 **技术规格**

#### **Python 支持**
- **Python 版本**: 3.8, 3.9, 3.10, 3.11, 3.12
- **异步支持**: 完整的 async/await 兼容性
- **跨平台**: Windows、macOS、Linux 支持

#### **核心依赖**

本SDK使用以下核心依赖库：

| 依赖库 | 版本 | 用途 |
|--------|-----|------|
| `httpx` | `>=0.23.0` | HTTP客户端库 |
| `pydantic` | `>=1.9.0,<3.0.0` | 数据验证和序列化 |
| `typing-extensions` | `>=4.0.0` | 类型注解扩展 |
| `cachetools` | `>=4.2.2` | 缓存工具 |
| `pyjwt` | `>=2.8.0` | JSON Web Token 库 |

## 🚀 快速开始

### 基本用法

1. **使用API密钥创建客户端**
2. **调用相应的API方法**

完整示例请参考开放平台[接口文档](https://docs.z.ai/api-reference/)以及[使用指南](https://docs.z.ai/guides/)，记得替换为您自己的API密钥。

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
            {"role": "user", "content": "你好， Z.ai ！"}
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

### 联系我们

如有反馈和支持需求，请联系我们：**user_feedback@z.ai**
  
