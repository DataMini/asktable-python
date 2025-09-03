# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["RoleCreateParams"]


class RoleCreateParams(TypedDict, total=False):
    name: Required[str]
    """名称"""

    policy_ids: Optional[SequenceNotStr[str]]
    """策略列表。注意：如果为空或者不传则不绑定策略"""
