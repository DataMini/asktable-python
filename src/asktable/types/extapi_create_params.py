# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

__all__ = ["ExtapiCreateParams"]


class ExtapiCreateParams(TypedDict, total=False):
    base_url: Required[str]
    """根 URL"""

    name: Required[str]
    """名称，不超过 64 个字符"""

    headers: Optional[Dict[str, str]]
    """HTTP Headers，JSON 格式"""
