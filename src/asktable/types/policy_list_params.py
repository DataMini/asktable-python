# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["PolicyListParams"]


class PolicyListParams(TypedDict, total=False):
    name: Optional[str]
    """策略名称"""

    page: int
    """Page number"""

    policy_ids: Optional[SequenceNotStr[str]]
    """策略 ID 列表"""

    size: int
    """Page size"""
