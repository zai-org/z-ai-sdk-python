import logging
import logging.config

import zai
from zai import ZaiClient


def test_finetuning_create(logging_conf):
	logging.config.dictConfig(logging_conf)  # type: ignore
	client = ZaiClient()  # Please fill in your own API Key
	try:
		job = client.fine_tuning.jobs.create(
			model='chatglm3-6b',
			training_file='file-20240428021923715-xjng4',  # Please fill in the successfully uploaded file id
		validation_file='file-20240428021923715-xjng4',  # Please fill in the successfully uploaded file id
			suffix='demo_test',
		)
		job_id = job.id
		print(job_id)
		fine_tuning_job = client.fine_tuning.jobs.retrieve(fine_tuning_job_id=job_id)
		print(fine_tuning_job)
		#     ftjob-20240418110039323-j8lh2

	except zai.core._errors.APIRequestFailedError as err:
		print(err)
	except zai.core._errors.APIInternalError as err:
		print(err)
	except zai.core._errors.APIStatusError as err:
		print(err)


def test_finetuning_retrieve(logging_conf):
	logging.config.dictConfig(logging_conf)  # type: ignore
	client = ZaiClient()  # Please fill in your own API Key
	try:
		fine_tuning_job = client.fine_tuning.jobs.retrieve(fine_tuning_job_id='ftjob-20240429112551154-48vq7')
		print(fine_tuning_job)

	except zai.core._errors.APIRequestFailedError as err:
		print(err)
	except zai.core._errors.APIInternalError as err:
		print(err)
	except zai.core._errors.APIStatusError as err:
		print(err)


def test_finetuning_job_list(logging_conf):
	logging.config.dictConfig(logging_conf)  # type: ignore
	client = ZaiClient()  # Please fill in your own API Key
	try:
		job_list = client.fine_tuning.jobs.list()

		print(job_list)

	except zai.core._errors.APIRequestFailedError as err:
		print(err)
	except zai.core._errors.APIInternalError as err:
		print(err)
	except zai.core._errors.APIStatusError as err:
		print(err)


def test_finetuning_job_cancel(logging_conf):
	logging.config.dictConfig(logging_conf)  # type: ignore
	client = ZaiClient()  # Please fill in your own API Key
	try:
		cancel = client.fine_tuning.jobs.cancel(fine_tuning_job_id='ftjob-20240429112551154-48vq7')

		print(cancel)

	except zai.core._errors.APIRequestFailedError as err:
		print(err)
	except zai.core._errors.APIInternalError as err:
		print(err)
	except zai.core._errors.APIStatusError as err:
		print(err)


def test_finetuning_job_delete(logging_conf):
	logging.config.dictConfig(logging_conf)  # type: ignore
	client = ZaiClient()  # Please fill in your own API Key
	try:
		delete = client.fine_tuning.jobs.delete(fine_tuning_job_id='ftjob-20240126113041678-cs6s9')

		print(delete)

	except zai.core._errors.APIRequestFailedError as err:
		print(err)
	except zai.core._errors.APIInternalError as err:
		print(err)
	except zai.core._errors.APIStatusError as err:
		print(err)


def test_model_check(logging_conf):
	logging.config.dictConfig(logging_conf)  # type: ignore
	client = ZaiClient()  # Fill in your own API Key
	try:
		response = client.chat.completions.create(
			model='chatglm3-6b-8572905046912426020-demo_test',  # Fill in the model name to call
			messages=[
				{'role': 'user', 'content': '你是一位乐于助人，知识渊博的全能AI助手。'},
				{'role': 'user', 'content': '创造一个更精准、吸引人的slogan'},
			],
			extra_body={'temperature': 0.5, 'max_tokens': 50},
		)
		print(response.choices[0].message)

	except zai.core._errors.APIRequestFailedError as err:
		print(err)
	except zai.core._errors.APIInternalError as err:
		print(err)
	except zai.core._errors.APIStatusError as err:
		print(err)


def test_model_delete(logging_conf):
	logging.config.dictConfig(logging_conf)  # type: ignore
	client = ZaiClient()  # Fill in your own API Key
	try:
		delete = client.fine_tuning.models.delete(fine_tuned_model='chatglm3-6b-8572905046912426020-demo_test')

		print(delete)

	except zai.core._errors.APIRequestFailedError as err:
		print(err)
	except zai.core._errors.APIInternalError as err:
		print(err)
	except zai.core._errors.APIStatusError as err:
		print(err)


if __name__ == '__main__':
	test_finetuning_create()
