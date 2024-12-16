# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["PreferenceCreateParams"]


class PreferenceCreateParams(TypedDict, total=False):
    general_preference: Required[str]
    """通用偏好设置内容"""

    sql_preference: Optional[str]
    """SQL 偏好设置内容"""
