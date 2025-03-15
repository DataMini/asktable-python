# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["SecuretunnelUpdateParams"]


class SecuretunnelUpdateParams(TypedDict, total=False):
    client_info: Optional[object]
    """客户端信息"""

    name: Optional[str]
    """SecureTunnel 名称，不超过 20 个字符"""

    unique_key: Optional[str]
    """唯一标识，用于更新客户端信息（容器 ID）"""
