from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import httpx

from zai.core import (
    BaseAPI,
    NOT_GIVEN,
    Body,
    Headers,
    NotGiven,
    deepcopy_minimal,
    make_request_options,
)
from zai.types.ocr.layout_parsing_resp import LayoutParsingResp

if TYPE_CHECKING:
    from zai._client import ZaiClient

__all__ = ["LayoutParsing"]


class LayoutParsing(BaseAPI):
    """
    Layout parsing API resource for document/image OCR with layout detection.
    
    This API supports parsing images and PDF documents to extract text content
    with detailed layout information.
    """

    def __init__(self, client: "ZaiClient") -> None:
        super().__init__(client)

    def create(
        self,
        *,
        model: str,
        file: str,
        return_crop_images: Optional[bool] | NotGiven = NOT_GIVEN,
        need_layout_visualization: Optional[bool] | NotGiven = NOT_GIVEN,
        start_page_id: Optional[int] | NotGiven = NOT_GIVEN,
        end_page_id: Optional[int] | NotGiven = NOT_GIVEN,
        request_id: Optional[str] | NotGiven = NOT_GIVEN,
        user_id: Optional[str] | NotGiven = NOT_GIVEN,
        extra_headers: Headers | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LayoutParsingResp:
        """
        Parse document or image layout and extract text content.

        Arguments:
            model (str): Model code, e.g., 'GLM-OCR' or 'glm-ocr'
            file (str): URL or base64 encoded image/PDF to parse.
                Supported formats: PDF, JPG, PNG.
                Size limits: Image ≤ 10MB, PDF ≤ 50MB, max 100 pages.
            return_crop_images (Optional[bool]): Whether to return crop images.
                Defaults to False. When True, returns cropped image information.
            need_layout_visualization (Optional[bool]): Whether to return detailed layout visualization results.
                Defaults to False. When True, returns detailed layout image result information.
            start_page_id (Optional[int]): Starting page number for PDF parsing.
            end_page_id (Optional[int]): Ending page number for PDF parsing.
            request_id (Optional[str]): Unique request identifier. Auto-generated if not provided.
            user_id (Optional[str]): End user ID for abuse monitoring.
                Length: 6-128 characters.
            extra_headers (Headers): Additional HTTP headers.
            extra_body (Body): Additional request body parameters.
            timeout (float | httpx.Timeout): Request timeout.

        Returns:
            LayoutParsingResp: Parsed layout result including:
                - id: Task ID
                - created: Unix timestamp
                - model: Model name
                - md_results: Markdown formatted recognition result
                - crop_images: Cropped image information (if return_crop_images=True)
                - layout_visualization: Detailed layout visualization information (if need_layout_visualization=True)
                - data_info: Document metadata (page count, dimensions)
        """
        if not model:
            raise ValueError("`model` must be provided.")
        if not file:
            raise ValueError("`file` must be provided.")

        body = deepcopy_minimal(
            {
                "model": model,
                "file": file,
                "return_crop_images": return_crop_images,
                "need_layout_visualization": need_layout_visualization,
                "start_page_id": start_page_id,
                "end_page_id": end_page_id,
                "request_id": request_id,
                "user_id": user_id,
            }
        )

        return self._post(
            "/layout_parsing",
            body=body,
            options=make_request_options(
                extra_headers=extra_headers, extra_body=extra_body, timeout=timeout
            ),
            cast_type=LayoutParsingResp,
        )
