def test_sdk_import_unit():
	import zai

	print(zai.__version__)


def test_os_import_unit():
	import os

	print(os)


def test_sdk_import():
	from zai import ZaiClient

	client = ZaiClient(api_key='empty')  # Please fill in your own API Key

	if client is not None:
		print('SDK import success')
	else:
		print('SDK import failed')
