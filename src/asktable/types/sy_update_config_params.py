# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["SyUpdateConfigParams"]


class SyUpdateConfigParams(TypedDict, total=False):
    global_table_limit: Optional[int]
    """表限制数量"""
