# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["SecuretunnelCreateParams"]


class SecuretunnelCreateParams(TypedDict, total=False):
    name: Optional[str]
    """SecureTunnel 名称，不超过 20 个字符"""
