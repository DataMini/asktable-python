# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["Q2ListParams"]


class Q2ListParams(TypedDict, total=False):
    datasource_id: Optional[str]
    """数据源 ID"""

    page: int
    """Page number"""

    size: int
    """Page size"""
