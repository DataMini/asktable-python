# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..._types import FileTypes

__all__ = ["FileCreateParams"]


class FileCreateParams(TypedDict, total=False):
    name: Required[str]

    file: Required[FileTypes]

    async_process_meta: bool
    """是否异步处理元数据"""

    skip_process_meta: bool
    """是否跳过元数据处理"""
