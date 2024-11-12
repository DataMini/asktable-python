# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["KBListParams"]


class KBListParams(TypedDict, total=False):
    name: str
    """文档名称"""

    page: int
    """Page number"""

    size: int
    """Page size"""
