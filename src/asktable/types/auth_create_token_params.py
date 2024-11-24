# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["AuthCreateTokenParams", "ChatRole"]


class AuthCreateTokenParams(TypedDict, total=False):
    ak_role: Literal["sys", "admin", "asker", "visitor"]
    """The role for the API key"""

    chat_role: Optional[ChatRole]
    """The chat role"""

    token_ttl: int
    """The time-to-live for the token in seconds"""

    user_profile: Optional[object]
    """Optional user profile data"""


class ChatRole(TypedDict, total=False):
    role_id: Optional[str]
    """The chat role ID"""

    role_variables: Optional[object]
    """The chat role variables"""
