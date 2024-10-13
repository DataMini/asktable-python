# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import TypedDict

__all__ = ["PolicyListParams"]


class PolicyListParams(TypedDict, total=False):
    name: Optional[str]
    """策略名称"""

    page: int
    """Page number"""

    policy_ids: Optional[List[str]]
    """策略 ID 列表"""

    size: int
    """Page size"""
