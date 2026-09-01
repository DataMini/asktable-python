# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["APIKeyCreateParams"]


class APIKeyCreateParams(TypedDict, total=False):
    ak_role: Required[Literal["sys", "admin", "asker"]]
    """API key 的角色"""

    name: Required[str]
    """API Key 名称"""

    expires_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """过期时间；空表示不过期"""
