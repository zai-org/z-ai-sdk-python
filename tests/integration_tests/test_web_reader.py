import logging
import logging.config

import zai
from zai import ZaiClient


def test_web_reader(logging_conf):
    logging.config.dictConfig(logging_conf)  # type: ignore
    client = ZaiClient()  # Fill in your own API Key
    try:
        response = client.web_reader.web_reader(
            url="https://www.example.com/",
            return_format="markdown",
            retain_images=True,
            with_links_summary=True,
        )
        print(response)

    except zai.core._errors.APIRequestFailedError as err:
        print(err)
    except zai.core._errors.APIInternalError as err:
        print(err)
    except zai.core._errors.APIStatusError as err:
        print(err)