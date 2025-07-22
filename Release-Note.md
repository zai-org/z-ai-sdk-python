# Release Notes

## v0.0.1b1 - Major Enhancements & Restructuring (2025-07-22)

🚀 **A comprehensive update focusing on developer experience, code organization, and expanded examples!**

This release brings significant improvements to the SDK structure, comprehensive examples for all features, and enhanced developer experience.

### 🎯 **Major Features Examples**

#### 📹 **Comprehensive Video Generation Examples**
- **Complete Model Coverage**: Added examples for all supported video generation models:
  - `cogvideox-3`: Text-to-video, image-to-video, start-end frame video
  - `cogvideox-2`: Enhanced text-to-video generation
  - `viduq1-text`, `viduq1-image`, `viduq1-start-end`: VidU Q1 series models
  - `vidu2-image`, `vidu2-start-end`, `vidu2-reference`: VidU 2 series models
- **Advanced Features**: Support for 4K resolution, 60fps, audio generation, and custom quality settings
- **Async Task Management**: Comprehensive polling and timeout handling for video generation tasks

#### 🤖 **Agent Invocation System Examples**
- **General Translation Agent**: Multi-language translation with streaming support
  - Supports 10 languages: English, Chinese, Japanese, Korean, French, German, Spanish, Russian, Arabic, Portuguese
  - Real-time streaming translation responses
- **Special Effects Video Agent**: Advanced video creation with template support
  - Async task submission and result polling
  - Template-based video generation (e.g., "french_kiss" template)
  - Image input support for video effects

#### 🧠 **GLM-4 Model Integration Examples**
- **Synchronous Calls**: Direct model invocation with web search tool integration
- **Streaming Responses**: Real-time text generation with SSE support
- **Asynchronous Operations**: Task-based async processing with result polling
- **Tool Integration**: Built-in web search capabilities for enhanced responses

#### 🔍 **Web Search Examples**
- **Advanced Search Filters**: Domain filtering, recency filtering, content size control
- **Multiple Search Engines**: Support for different search engines including "search_pro"
- **Configurable Results**: Customizable result count (1-50) and content detail level
- **GLM-4 Integration**: Seamless integration with chat models for search-enhanced responses

### 🏗️ **Architecture & Code Organization**

#### 📁 **Module Structure Refactoring**
- **API Resources Reorganization**:
  ```
  src/zai/api_resource/
  ├── embeddings/
  │   ├── __init__.py
  │   └── embeddings.py
  ├── files/
  │   ├── __init__.py
  │   └── files.py
  ├── images/
  │   ├── __init__.py
  │   └── images.py
  └── batch/
      ├── __init__.py
      └── batches.py
  ```

- **Type Definitions Reorganization**:
  ```
  src/zai/types/
  ├── batch/
  │   ├── __init__.py
  │   ├── batch.py
  │   ├── batch_create_params.py
  │   ├── batch_error.py
  │   ├── batch_list_params.py
  │   └── batch_request_counts.py
  ├── image/
  │   ├── __init__.py
  │   └── image.py
  ├── embeddings/
  │   ├── __init__.py
  │   └── embeddings.py
  └── [other organized modules...]
  ```

#### 🔗 **Import System Overhaul**
- **Absolute Imports**: Converted all relative imports (`from ..core`) to absolute imports (`from zai.core`)
- **Centralized Exports**: Moved all `__all__` definitions from individual modules to `__init__.py` files
- **Backward Compatibility**: Maintained full compatibility with existing import patterns
- **Clean Dependencies**: Eliminated circular imports and improved module loading

### 🛠️ **Developer Experience Improvements**

#### ⚙️ **Environment Configuration**
- **Enhanced .env Support**: Robust environment variable loading with `python-dotenv`
- **Fallback Mechanisms**: Graceful fallback to system environment variables
- **API Key Validation**: Comprehensive error handling for missing or invalid API keys
- **Setup Guidance**: Clear instructions for environment configuration

#### 🌍 **Internationalization**
- **Complete English Translation**: All Chinese content translated to English
  - Code comments and documentation
  - Print statements and user messages
  - Error messages and status updates
  - Example code and variable names
- **Consistent Terminology**: Standardized technical terms across all examples

### 📚 **Comprehensive Example Suite**

#### 📖 **New Example Files**
- **`examples/video_models_examples.py`**: Complete guide for all video generation models
- **`examples/agent_examples.py`**: Agent invocation patterns and best practices
- **`examples/glm4_example.py`**: GLM-4 model usage in all modes (sync, async, streaming)
- **`examples/web_search_example.py`**: Web search integration and configuration
- **`examples/video_generator.py`**: Enhanced async video generation (updated)

#### 🔧 **Enhanced Existing Examples**
- **`examples/basic_usage.py`**: Maintained comprehensive basic SDK usage
- **Error Handling**: Added proper exception handling across all examples
- **Type Hints**: Enhanced type annotations for better IDE support
- **Documentation**: Improved inline documentation and usage explanations

### 🐛 **Bug Fixes & Stability**

#### 🔧 **Import Resolution**
- Fixed `ModuleNotFoundError` issues after module restructuring
- Corrected import paths in `src/zai/_client.py` for batch operations
- Resolved circular dependency issues in type definitions
- Ensured backward compatibility for existing test imports

#### 🔑 **API Key Management**
- Fixed API key loading from `.env` files
- Enhanced error messages for authentication issues
- Improved error handling for missing environment variables

#### ⏱️ **Async Operations**
- Enhanced timeout and polling mechanisms for video generation
- Improved error handling in async task management
- Better exception handling for network and API errors

### 📋 **Technical Improvements**

#### 🏃‍♂️ **Performance Optimizations**
- Optimized module loading with improved import structure
- Reduced memory footprint through better resource management
- Enhanced async operation handling in examples

#### 🛡️ **Code Quality**
- Consistent error handling patterns across all modules
- Enhanced type safety with comprehensive type hints
- Improved code documentation and comments
- Standardized coding conventions

### 📦 **Dependencies & Compatibility**

#### 📌 **New Optional Dependencies**
- `python-dotenv`: For enhanced environment variable management
- Maintained backward compatibility - all dependencies remain optional

#### 🔄 **Python Version Support**
- Continued support for Python 3.8, 3.9, 3.10, 3.11, 3.12
- Enhanced async/await compatibility
- Cross-platform stability improvements

### 🚀 **Migration Guide**

#### ✅ **For Existing Users**
1. **No Breaking Changes**: All existing code continues to work without modifications
2. **Optional Enhancements**: Consider adding `.env` file for API key management
3. **New Examples**: Explore new example files for advanced usage patterns
4. **Import Compatibility**: All existing imports remain functional

#### 📝 **Recommended Updates**
```python
# Before (still works)
from zai import ZaiClient
client = ZaiClient(api_key="your-key")

# Enhanced (recommended)
import os
from zai import ZaiClient
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('ZAI_API_KEY')
client = ZaiClient(api_key=api_key)
```

### 🔮 **What's Coming Next**

- Additional video generation models and features
- Enhanced streaming capabilities for all APIs
- More agent templates and scenarios
- Performance optimizations for large-scale usage
- Extended tool integrations

---

## v0.0.1a1 - Initial Release (2025-07-14)

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
pip install zai-sdk
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

### From v0.0.1a1 to v0.0.1b1
*No breaking changes - all existing code continues to work!*

**Optional Enhancements:**
1. Add `.env` file support for better API key management
2. Explore new example files for advanced usage patterns
3. Consider using the new agent invocation examples
4. Try the comprehensive video generation examples

For future versions, detailed migration guides will be provided here to help you upgrade smoothly.

---

**Note**: This release significantly enhances the developer experience while maintaining full backward compatibility. All improvements are additive, ensuring your existing code continues to work seamlessly.