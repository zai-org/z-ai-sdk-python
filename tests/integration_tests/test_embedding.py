import logging
import logging.config

import zai
from zai import ZaiClient


def test_embeddings(logging_conf):
	logging.config.dictConfig(logging_conf)  # type: ignore

	client = ZaiClient()
	try:
		response = client.embeddings.create(
			model='embedding-2',  # Fill in the model name to call
			input='hello',
			extra_body={'model_version': 'v1'},
		)
		print(response)

	except zai.core._errors.APIRequestFailedError as err:
		print(err)
	except zai.core._errors.APIInternalError as err:
		print(err)
	except zai.core._errors.APIStatusError as err:
		print(err)


def test_embeddings_dimensions(logging_conf):
	logging.config.dictConfig(logging_conf)  # type: ignore

	client = ZaiClient()
	try:
		response = client.embeddings.create(
			model='embedding-3',  # Fill in the model name to call
			input='hello',
			dimensions=512,
			extra_body={'model_version': 'v1'},
		)
		assert response.data[0].object == 'embedding'
		assert len(response.data[0].embedding) == 512
		print(len(response.data[0].embedding))

	except zai.core._errors.APIRequestFailedError as err:
		print(err)
	except zai.core._errors.APIInternalError as err:
		print(err)
	except zai.core._errors.APIStatusError as err:
		print(err)
