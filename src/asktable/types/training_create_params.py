# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["TrainingCreateParams", "Body"]


class TrainingCreateParams(TypedDict, total=False):
    datasource_id: Required[str]
    """数据源 ID"""

    body: Required[Iterable[Body]]


class Body(TypedDict, total=False):
    question: Required[str]
    """用户问题"""

    sql: Required[str]
    """用户问题对应的 SQL"""

    chat_id: Optional[str]
    """聊天 ID"""

    msg_id: Optional[str]
    """消息 ID"""

    role_id: Optional[str]
    """角色 ID"""
