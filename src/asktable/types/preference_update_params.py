# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["PreferenceUpdateParams"]


class PreferenceUpdateParams(TypedDict, total=False):
    general_preference: Optional[str]
    """通用偏好设置内容"""

    sql_preference: Optional[str]
    """SQL 偏好设置内容"""
