# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["TrainingUpdateParams"]


class TrainingUpdateParams(TypedDict, total=False):
    datasource_id: Required[str]
    """数据源 ID"""

    active: Optional[bool]
    """是否启用"""

    question: Optional[str]
    """用户问题"""

    role_id: Optional[str]
    """角色 ID"""

    sql: Optional[str]
    """用户问题对应的 SQL"""
