# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["APIKeyCreateParams"]


class APIKeyCreateParams(TypedDict, total=False):
    ak_role: Required[Literal["sys", "admin", "asker", "visitor"]]
    """API key 的角色"""
