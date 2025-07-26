# -*- coding: utf-8 -*-
from typing import Type

import httpx
import pytest

from zai.core import BaseModel, HttpClient
from zai.core._base_type import ResponseT
from zai.core._request_opt import FinalRequestOptions
from zai.core._response import APIResponse
from zai.types.chat.async_chat_completion import (
	AsyncCompletion,
	AsyncTaskStatus,
)
from zai.types.chat.chat_completion import (
	Completion,
)
from zai.types.chat.chat_completion import (
	CompletionChoice as ChatCompletionChoice,
)
from zai.types.chat.chat_completion import (
	CompletionMessageToolCall as ChatCompletionMessageToolCall,
)
from zai.types.chat.chat_completion import (
	CompletionUsage as ChatCompletionUsage,
)
from zai.types.embeddings import Embedding, EmbeddingsResponded
from zai.types.files.file_object import FileObject, ListOfFileObject
from zai.types.image import GeneratedImage, ImagesResponded


class MockClient:
	_strict_response_validation: bool = False

	def _process_response_data(
		self,
		*,
		data: object,
		cast_type: Type[ResponseT],
		response: httpx.Response,
	) -> ResponseT:
		pass


@pytest.mark.parametrize(
	'R',
	[
		AsyncTaskStatus,
		AsyncCompletion,
		Completion,
	],
)
def test_response_chat_model_cast(R: Type[BaseModel]) -> None:
	MockClient._process_response_data = HttpClient._process_response_data
	response = httpx.Response(
		status_code=200,
		content="""{
    "id": "completion123",
    "request_id": "request456",
    "model": "model-name",
    "task_status": "completed",
    "choices": [
      {
        "index": 0,
        "finish_reason": "normal",
        "message": {
          "content": "This is the completion content.",
          "role": "assistant",
          "tool_calls": [
            {
              "id": "toolcall789",
              "function": {
                "arguments": "arg1, arg2",
                "name": "functionName"
              },
              "type": "function_call"
            }
          ]
        }
      }
    ],
    "usage": {
      "prompt_tokens": 10,
      "completion_tokens": 15,
      "total_tokens": 25
    }
  }""",
	)

	opts = FinalRequestOptions.construct(method='get', url='path')
	http_response = APIResponse(
		raw=response,
		cast_type=R,
		client=MockClient(),
		stream=False,
		stream_cls=None,
		options=opts,
	)
	model = http_response.parse()

	if R == AsyncTaskStatus:
		assert R == model.__class__
		assert isinstance(model, AsyncTaskStatus)
		assert model.id == 'completion123'
		assert model.request_id == 'request456'
		assert model.model == 'model-name'
		assert model.task_status == 'completed'

	elif R == AsyncCompletion:
		assert R == model.__class__
		assert isinstance(model, AsyncCompletion)
		assert model.id == 'completion123'
		assert model.request_id == 'request456'
		assert model.model == 'model-name'
		assert model.task_status == 'completed'
		assert isinstance(model.choices, list)
		assert model.choices[0].index == 0
		assert model.choices[0].finish_reason == 'normal'
		assert model.choices[0].message.content == 'This is the completion content.'
		assert model.choices[0].message.role == 'assistant'
		assert isinstance(model.choices[0].message.tool_calls, list)
		assert model.choices[0].message.tool_calls[0].id == 'toolcall789'
		assert model.choices[0].message.tool_calls[0].function.arguments == 'arg1, arg2'
		assert model.choices[0].message.tool_calls[0].function.name == 'functionName'
		assert model.choices[0].message.tool_calls[0].type == 'function_call'
		assert model.usage.prompt_tokens == 10
		assert model.usage.completion_tokens == 15
		assert model.usage.total_tokens == 25
	elif R == Completion:
		assert R == model.__class__
		assert isinstance(model, Completion)
		assert model.id == 'completion123'
		assert model.request_id == 'request456'
		assert model.model == 'model-name'
		assert model.created == None
		assert isinstance(model.choices, list)
		assert isinstance(model.choices[0], ChatCompletionChoice)
		assert model.choices[0].index == 0
		assert model.choices[0].finish_reason == 'normal'
		assert model.choices[0].message.content == 'This is the completion content.'
		assert model.choices[0].message.role == 'assistant'
		assert isinstance(model.choices[0].message.tool_calls, list)
		assert isinstance(
			model.choices[0].message.tool_calls[0],
			ChatCompletionMessageToolCall,
		)
		assert model.choices[0].message.tool_calls[0].id == 'toolcall789'
		assert model.choices[0].message.tool_calls[0].function.arguments == 'arg1, arg2'
		assert model.choices[0].message.tool_calls[0].function.name == 'functionName'
		assert model.choices[0].message.tool_calls[0].type == 'function_call'
		assert isinstance(model.usage, ChatCompletionUsage)
		assert model.usage.prompt_tokens == 10
		assert model.usage.completion_tokens == 15
		assert model.usage.total_tokens == 25

	else:
		assert False, f'Unexpected model type: {R}'


@pytest.mark.parametrize(
	'R',
	[EmbeddingsResponded],
)
def test_response_embedding_model_cast(R: Type[BaseModel]) -> None:
	MockClient._process_response_data = HttpClient._process_response_data
	response = httpx.Response(
		status_code=200,
		content="""{
    "object": "embeddings",
    "data": [
      {
        "object": "embedding",
        "index": 1,
        "embedding": [0.1, 0.2] 
      }
    ],
    "model": "some-model-name",
    "usage": {
      "prompt_tokens": 20,
      "completion_tokens": 30,
      "total_tokens": 50
    }
  }""",
	)

	opts = FinalRequestOptions.construct(method='get', url='path')
	http_response = APIResponse(
		raw=response,
		cast_type=R,
		client=MockClient(),
		stream=False,
		stream_cls=None,
		options=opts,
	)
	model = http_response.parse()

	assert R == model.__class__
	assert isinstance(model, EmbeddingsResponded)
	assert isinstance(model.data, list)
	assert isinstance(model.data[0], Embedding)
	assert model.data[0].object == 'embedding'
	assert model.data[0].index == 1
	assert model.data[0].embedding == [0.1, 0.2]
	assert model.object == 'embeddings'
	assert model.model == 'some-model-name'
	assert model.usage.prompt_tokens == 20
	assert model.usage.completion_tokens == 30
	assert model.usage.total_tokens == 50


@pytest.mark.parametrize(
	'R',
	[
		FileObject,
	],
)
def test_response_file_list_model_cast(R: Type[BaseModel]) -> None:
	MockClient._process_response_data = HttpClient._process_response_data
	response = httpx.Response(
		status_code=200,
		content=""" {
        "id": "12345",
        "bytes": 1024,
        "created_at": 1617181723,
        "filename": "example.txt",
        "object": "file",
        "purpose": "example purpose",
        "status": "uploaded",
        "status_details": "File uploaded successfully"
      }""",
	)

	opts = FinalRequestOptions.construct(method='get', url='path')
	http_response = APIResponse(
		raw=response,
		cast_type=R,
		client=MockClient(),
		stream=False,
		stream_cls=None,
		options=opts,
	)
	model = http_response.parse()

	assert R == model.__class__
	assert isinstance(model, FileObject)
	assert model.id == '12345'
	assert model.bytes == 1024
	assert model.created_at == 1617181723
	assert model.filename == 'example.txt'
	assert model.object == 'file'
	assert model.purpose == 'example purpose'
	assert model.status == 'uploaded'
	assert model.status_details == 'File uploaded successfully'


@pytest.mark.parametrize(
	'R',
	[
		ListOfFileObject,
	],
)
def test_response_file_list_model_cast(R: Type[BaseModel]) -> None:
	MockClient._process_response_data = HttpClient._process_response_data
	response = httpx.Response(
		status_code=200,
		content="""{
    "object": "list",
    "data": [
      {
        "id": "12345",
        "bytes": 1024,
        "created_at": 1617181723,
        "filename": "example.txt",
        "object": "file",
        "purpose": "example purpose",
        "status": "uploaded",
        "status_details": "File uploaded successfully"
      }
    ],
    "has_more": true
  }""",
	)

	opts = FinalRequestOptions.construct(method='get', url='path')
	http_response = APIResponse(
		raw=response,
		cast_type=R,
		client=MockClient(),
		stream=False,
		stream_cls=None,
		options=opts,
	)
	model = http_response.parse()

	assert R == model.__class__
	assert isinstance(model.data, list)
	assert isinstance(model.data[0], FileObject)
	assert model.data[0].id == '12345'
	assert model.data[0].bytes == 1024
	assert model.data[0].created_at == 1617181723
	assert model.data[0].filename == 'example.txt'
	assert model.data[0].object == 'file'
	assert model.data[0].purpose == 'example purpose'
	assert model.data[0].status == 'uploaded'
	assert model.data[0].status_details == 'File uploaded successfully'
	assert model.has_more == True


@pytest.mark.parametrize('R', [ImagesResponded])
def test_response_image_model_cast(R: Type[BaseModel]) -> None:
	MockClient._process_response_data = HttpClient._process_response_data
	response = httpx.Response(
		status_code=200,
		content="""{
"created": 1234567890,
"data": [
  {
    "b64_json": "base64_encoded_string",
    "url": "http://example.com/image.png",
    "revised_prompt": "Revised prompt text"
  }
]
}""",
	)

	opts = FinalRequestOptions.construct(method='get', url='path')
	http_response = APIResponse(
		raw=response,
		cast_type=R,
		client=MockClient(),
		stream=False,
		stream_cls=None,
		options=opts,
	)
	model = http_response.parse()

	assert R == model.__class__
	assert isinstance(model.data, list)
	assert isinstance(model.data[0], GeneratedImage)
	assert model.data[0].b64_json == 'base64_encoded_string'
