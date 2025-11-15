from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import httpx

from zai.core import (
    NOT_GIVEN,
    BaseAPI,
    Body,
    Headers,
    NotGiven,
    deepcopy_minimal,
    make_request_options,
    maybe_transform,
)
from zai.types.web_reader.web_reader_params import WebReaderParams
from zai.types.web_reader.web_reader_resp import WebReaderResult

if TYPE_CHECKING:
    from zai._client import ZaiClient


class WebReaderApi(BaseAPI):
    def __init__(self, client: "ZaiClient") -> None:
        super().__init__(client)

    def web_reader(
        self,
        *,
        url: str,
        request_id: Optional[str] | NotGiven = NOT_GIVEN,
        user_id: Optional[str] | NotGiven = NOT_GIVEN,
        timeout: Optional[str] | NotGiven = NOT_GIVEN,
        no_cache: Optional[bool] | NotGiven = NOT_GIVEN,
        return_format: Optional[str] | NotGiven = NOT_GIVEN,
        retain_images: Optional[bool] | NotGiven = NOT_GIVEN,
        no_gfm: Optional[bool] | NotGiven = NOT_GIVEN,
        keep_img_data_url: Optional[bool] | NotGiven = NOT_GIVEN,
        with_images_summary: Optional[bool] | NotGiven = NOT_GIVEN,
        with_links_summary: Optional[bool] | NotGiven = NOT_GIVEN,
        extra_headers: Headers | None = None,
        extra_body: Body | None = None,
        timeout_override: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WebReaderResult:
        body = deepcopy_minimal(
            {
                "url": url,
                "request_id": request_id,
                "user_id": user_id,
                "timeout": timeout,
                "no_cache": no_cache,
                "return_format": return_format,
                "retain_images": retain_images,
                "no_gfm": no_gfm,
                "keep_img_data_url": keep_img_data_url,
                "with_images_summary": with_images_summary,
                "with_links_summary": with_links_summary,
            }
        )
        return self._post(
            "/reader",
            body=maybe_transform(body, WebReaderParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_body=extra_body, timeout=timeout_override
            ),
            cast_type=WebReaderResult,
        )