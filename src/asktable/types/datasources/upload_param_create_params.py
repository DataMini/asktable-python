# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["UploadParamCreateParams"]


class UploadParamCreateParams(TypedDict, total=False):
    expiration: Optional[int]
    """URL 有效期，单位为分钟"""

    file_max_size: Optional[int]
    """文件大小限制，单位为 MB"""
