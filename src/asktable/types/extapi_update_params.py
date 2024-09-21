# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import TypedDict

__all__ = ["ExtapiUpdateParams"]


class ExtapiUpdateParams(TypedDict, total=False):
    base_url: Optional[str]
    """根 URL"""

    headers: Optional[Dict[str, str]]
    """HTTP Headers，JSON 格式"""

    name: Optional[str]
    """名称，不超过 64 个字符"""
