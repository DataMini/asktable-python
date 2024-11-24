# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import TypedDict

__all__ = ["RoleGetVariablesParams"]


class RoleGetVariablesParams(TypedDict, total=False):
    bot_id: Optional[str]
    """Bot ID"""

    datasource_ids: Optional[List[str]]
    """数据源 ID 列表"""
