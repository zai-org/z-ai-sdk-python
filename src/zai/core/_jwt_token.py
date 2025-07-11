# -*- coding:utf-8 -*-
import time

import cachetools.func
import jwt

# Cache time 3 minutes
CACHE_TTL_SECONDS = 3 * 60

# Token validity period is 30 seconds longer than cache time
API_TOKEN_TTL_SECONDS = CACHE_TTL_SECONDS + 30


@cachetools.func.ttl_cache(maxsize=10, ttl=CACHE_TTL_SECONDS)
def generate_token(apikey: str):
	try:
		api_key, secret = apikey.split('.')
	except Exception as e:
		raise Exception('invalid api_key', e)

	payload = {
		'api_key': api_key,
		'exp': int(round(time.time() * 1000)) + API_TOKEN_TTL_SECONDS * 1000,
		'timestamp': int(round(time.time() * 1000)),
	}
	ret = jwt.encode(
		payload,
		secret,
		algorithm='HS256',
		headers={'alg': 'HS256', 'sign_type': 'SIGN'},
	)
	return ret
