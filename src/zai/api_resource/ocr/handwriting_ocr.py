from __future__ import annotations

from typing import TYPE_CHECKING, Mapping, cast

import httpx
from typing_extensions import Literal
from zai.core import (
    BaseAPI,
    maybe_transform,
    NOT_GIVEN,
    Body,
    Headers,
    NotGiven,
    FileTypes,
    deepcopy_minimal,
    extract_files,
    make_request_options
)
from zai.types.ocr.handwriting_ocr_params import HandwritingOCRParams
from zai.types.ocr.handwriting_ocr_resp import HandwritingOCRResp

if TYPE_CHECKING:
    from zai._client import ZaiClient

__all__ = ["HandwritingOCR"]


class HandwritingOCR(BaseAPI):

    def __init__(self, client: "ZaiClient") -> None:
        super().__init__(client)

    def handwriting_ocr(
            self,
            *,
            file: FileTypes,
            tool_type: Literal["hand_write"],
            language_type: str = None,  # optional,
            probability: bool = None,
            extra_headers: Headers | None = None,
            extra_body: Body | None = None,
            timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HandwritingOCRResp:
        if not file:
            raise ValueError("`file` must be provided.")
        if not tool_type:
            raise ValueError("`tool_type` must be provided.")
        body = deepcopy_minimal(
            {
                "file": file,
                "tool_type": tool_type,
                "language_type": language_type,
                "probability": probability
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        if files:
            extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/files/ocr",
            body=maybe_transform(body, HandwritingOCRParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_body=extra_body, timeout=timeout
            ),
            cast_type=HandwritingOCRResp,
        )
