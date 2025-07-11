# Release Notes

## v0.0.1a1 - Initial Release (2025-01-02)

🎉 **Welcome to the first release of the Z.ai Python SDK!**

This initial release provides comprehensive access to Z.ai's powerful AI capabilities through a modern, type-safe Python SDK.

### ✨ Core Features

#### 🤖 **Chat Completions**
- **Standard Chat**: Create chat completions with various models including `glm-4`, `charglm-3`
- **Streaming Support**: Real-time streaming responses for interactive applications
- **Tool Calling**: Function calling capabilities for enhanced AI interactions
- **Character Role-Playing**: Support for character-based conversations with `charglm-3` model
- **Multimodal Chat**: Image understanding capabilities with vision models

#### 🧠 **Embeddings**
- **Text Embeddings**: Generate high-quality vector embeddings for text
- **Configurable Dimensions**: Customizable embedding dimensions
- **Batch Processing**: Support for multiple inputs in a single request

#### 🎥 **Video Generation**
- **Text-to-Video**: Generate videos from text prompts
- **Image-to-Video**: Create videos from image inputs
- **Customizable Parameters**: Control quality, duration, FPS, and size
- **Audio Support**: Optional audio generation for videos

#### 🎵 **Audio Processing**
- **Speech Transcription**: Convert audio files to text
- **Multiple Formats**: Support for various audio file formats

#### 🤝 **Assistant API**
- **Conversation Management**: Structured conversation handling
- **Streaming Conversations**: Real-time assistant interactions
- **Metadata Support**: Rich conversation context and user information

#### 🔧 **Advanced Tools**
- **Web Search**: Integrated web search capabilities
- **File Management**: Upload, download, and manage files
- **Batch Operations**: Efficient batch processing for multiple requests
- **Knowledge Base**: Knowledge management and retrieval
- **Content Moderation**: Built-in content safety and moderation
- **Image Generation**: AI-powered image creation
- **Fine-tuning**: Custom model training capabilities

### 🛡️ **Developer Experience**

#### **Type Safety**
- Complete type annotations for all APIs
- Full IDE support with autocomplete and type checking
- Pydantic-based request/response validation

#### **Error Handling**
- Comprehensive error types for different failure scenarios
- Detailed error messages and debugging information
- Automatic retry mechanisms with configurable settings

#### **Performance & Reliability**
- Built-in connection pooling and request optimization
- Configurable timeout and retry strategies
- Efficient resource management

#### **Security**
- Secure API key management
- Optional token caching with security controls
- Built-in authentication handling

### 📋 **Technical Specifications**

#### **Python Support**
- **Python Versions**: 3.8, 3.9, 3.10, 3.11, 3.12
- **Async Support**: Full async/await compatibility
- **Cross-platform**: Windows, macOS, Linux support

#### **Dependencies**
- `httpx` (≥0.23.0): Modern HTTP client
- `pydantic` (≥1.9.0, <3.0): Data validation and serialization
- `typing-extensions` (≥4.0.0): Enhanced type hints
- `cachetools` (≥4.2.2): Caching utilities
- `pyjwt` (~2.8.0): JWT token handling

### 🚀 **Getting Started**

```bash
pip install z-ai
```

```python
from zai import ZaiClient

# Initialize client
client = ZaiClient(api_key="your-api-key")

# Create chat completion
response = client.chat.completions.create(
    model="glm-4",
    messages=[{"role": "user", "content": "Hello, Z.ai!"}]
)

print(response.choices[0].message.content)
```

### 📚 **Documentation & Support**

- **Documentation**: [Z.ai Open Platform](https://docs.z.ai/)
- **Examples**: Comprehensive examples in the `/examples` directory
- **Community**: GitHub Issues and Discussions
- **Contact**: user_feedback@z.ai

### 🔮 **What's Next**

This initial release establishes the foundation for Z.ai's Python SDK. Future releases will include:
- Additional model support
- Enhanced streaming capabilities
- More advanced tool integrations
- Performance optimizations
- Extended documentation and examples

---

## Migration Guide

*This is the initial release - no migration needed!*

For future versions, migration guides will be provided here to help you upgrade smoothly.

---

# 版本更新

## v0.0.1a1 - 首次发布 (2025-07-15)

🎉 **欢迎使用 Z.ai Python SDK 的首个版本！**

这个初始版本通过现代化、类型安全的 Python SDK 提供了对 Z.ai 强大 AI 能力的全面访问。

### ✨ 核心功能

#### 🤖 **对话补全**
- **标准对话**: 支持 `glm-4`、`charglm-3` 等多种模型的对话补全
- **流式支持**: 实时流式响应，适用于交互式应用
- **工具调用**: 函数调用能力，增强 AI 交互体验
- **角色扮演**: 支持基于 `charglm-3` 模型的角色对话
- **多模态对话**: 支持图像理解的视觉模型

#### 🧠 **向量嵌入**
- **文本嵌入**: 生成高质量的文本向量嵌入
- **可配置维度**: 自定义嵌入向量维度
- **批量处理**: 单次请求支持多个输入

#### 🎥 **视频生成**
- **文本生成视频**: 从文本提示生成视频
- **图像生成视频**: 从图像输入创建视频
- **参数可定制**: 控制质量、时长、帧率和尺寸
- **音频支持**: 可选的视频音频生成

#### 🎵 **音频处理**
- **语音转录**: 将音频文件转换为文本
- **多格式支持**: 支持各种音频文件格式

#### 🤝 **智能助手 API**
- **对话管理**: 结构化对话处理
- **流式对话**: 实时助手交互
- **元数据支持**: 丰富的对话上下文和用户信息

#### 🔧 **高级工具**
- **网络搜索**: 集成的网络搜索功能
- **文件管理**: 上传、下载和管理文件
- **批量操作**: 多请求的高效批量处理
- **知识库**: 知识管理和检索
- **内容审核**: 内置内容安全和审核
- **图像生成**: AI 驱动的图像创建
- **模型微调**: 自定义模型训练功能

### 🛡️ **开发者体验**

#### **类型安全**
- 所有 API 的完整类型注解
- 完整的 IDE 支持，包括自动补全和类型检查
- 基于 Pydantic 的请求/响应验证

#### **错误处理**
- 针对不同失败场景的全面错误类型
- 详细的错误消息和调试信息
- 可配置设置的自动重试机制

#### **性能与可靠性**
- 内置连接池和请求优化
- 可配置的超时和重试策略
- 高效的资源管理

#### **安全性**
- 安全的 API 密钥管理
- 带安全控制的可选令牌缓存
- 内置身份验证处理

### 📋 **技术规格**

#### **Python 支持**
- **Python 版本**: 3.8, 3.9, 3.10, 3.11, 3.12
- **异步支持**: 完整的 async/await 兼容性
- **跨平台**: Windows、macOS、Linux 支持

#### **依赖项**
- `httpx` (≥0.23.0): 现代 HTTP 客户端
- `pydantic` (≥1.9.0, <3.0): 数据验证和序列化
- `typing-extensions` (≥4.0.0): 增强类型提示
- `cachetools` (≥4.2.2): 缓存工具
- `pyjwt` (~2.8.0): JWT 令牌处理

### 🚀 **快速开始**

```bash
pip install z-ai
```

```python
from zai import ZaiClient

# 初始化客户端
client = ZaiClient(api_key="your-api-key")

# 创建对话补全
response = client.chat.completions.create(
    model="glm-4",
    messages=[{"role": "user", "content": "你好，Z.ai！"}]
)

print(response.choices[0].message.content)
```

### 📚 **文档与支持**

- **文档**: [Z.ai 开放平台](https://docs.z.ai/)
- **示例**: `/examples` 目录中的全面示例
- **社区**: GitHub Issues 和 Discussions
- **联系**: user_feedback@z.ai

### 🔮 **未来规划**

这个初始版本为 Z.ai Python SDK 奠定了基础。未来版本将包括：
- 更多模型支持
- 增强的流式功能
- 更多高级工具集成
- 性能优化
- 扩展的文档和示例

---

## 迁移指南

*这是初始版本 - 无需迁移！*

对于未来版本，我们将在此提供迁移指南，帮助您顺利升级。