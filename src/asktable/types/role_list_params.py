# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import TypedDict

__all__ = ["RoleListParams"]


class RoleListParams(TypedDict, total=False):
    name: Optional[str]
    """角色名称"""

    page: int
    """Page number"""

    role_ids: Optional[List[str]]
    """角色 ID 列表"""

    size: int
    """Page size"""
