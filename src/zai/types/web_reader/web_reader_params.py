from __future__ import annotations

from typing import Optional

from typing_extensions import TypedDict


class WebReaderParams(TypedDict, total=False):
    """
    Web reader request parameters

    Attributes:
        url (str): Target page URL to read
        request_id (str): Unique request task ID (6-64 chars)
        user_id (str): Unique end-user ID (6-128 chars)
        timeout (str): Request timeout in seconds
        no_cache (bool): Disable cache
        return_format (str): Return format, e.g. 'markdown' or 'text'
        retain_images (bool): Keep images in output
        no_gfm (bool): Disable GitHub Flavored Markdown
        keep_img_data_url (bool): Keep image data URLs
        with_images_summary (bool): Include images summary
        with_links_summary (bool): Include links summary
    """

    url: str
    request_id: Optional[str]
    user_id: Optional[str]
    timeout: Optional[str]
    no_cache: Optional[bool]
    return_format: Optional[str]
    retain_images: Optional[bool]
    no_gfm: Optional[bool]
    keep_img_data_url: Optional[bool]
    with_images_summary: Optional[bool]
    with_links_summary: Optional[bool]