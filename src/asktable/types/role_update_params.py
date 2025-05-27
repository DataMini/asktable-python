# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import TypedDict

__all__ = ["RoleUpdateParams"]


class RoleUpdateParams(TypedDict, total=False):
    name: Optional[str]
    """名称"""

    policy_ids: Optional[List[str]]
    """策略列表。注意：如果为空或者不传则不绑定策略"""
