import httpx

RAW_RESPONSE_HEADER = 'X-Stainless-Raw-Response'
# Control interface `connect` and `read` timeout through `Timeout`, default is `timeout=300.0, connect=8.0`
ZAI_DEFAULT_TIMEOUT = httpx.Timeout(timeout=300.0, connect=8.0)
# Control retry count through `retry` parameter, default is 3 times
ZAI_DEFAULT_MAX_RETRIES = 3
# Control max connections and keep-alive connections through `Limits`,
# default is `max_connections=50, max_keepalive_connections=10`
ZAI_DEFAULT_LIMITS = httpx.Limits(max_connections=50, max_keepalive_connections=10)

INITIAL_RETRY_DELAY = 0.5
MAX_RETRY_DELAY = 8.0
