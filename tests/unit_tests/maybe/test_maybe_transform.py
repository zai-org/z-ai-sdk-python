# -*- coding: utf-8 -*-
from zai.core import maybe_transform
from zai.types.batch import BatchCreateParams


def test_response_joblist_model_cast() -> None:
	params = maybe_transform(
		{
			'completion_window': '/v1/chat/completions',
			'endpoint': None,
			'metadata': {'key': 'value'},
		},
		BatchCreateParams,
	)
	assert isinstance(params, dict)
