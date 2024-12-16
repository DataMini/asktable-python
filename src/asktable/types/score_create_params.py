# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ScoreCreateParams"]


class ScoreCreateParams(TypedDict, total=False):
    chat_id: Required[str]
    """聊天 ID"""

    message_id: Required[str]
    """消息 ID"""

    score: Required[bool]
    """评分"""
