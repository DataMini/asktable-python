# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["DatasourceListParams"]


class DatasourceListParams(TypedDict, total=False):
    name: Optional[str]

    page: int
    """Page number"""

    size: int
    """Page size"""
