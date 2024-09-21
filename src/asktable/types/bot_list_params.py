# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["BotListParams"]


class BotListParams(TypedDict, total=False):
    name: Optional[str]
    """名称"""

    page: int
    """Page number"""

    size: int
    """Page size"""
