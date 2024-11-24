# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import TypedDict

__all__ = ["BusinessGlossaryUpdateParams"]


class BusinessGlossaryUpdateParams(TypedDict, total=False):
    aliases: Optional[List[str]]
    """业务术语同义词"""

    definition: Optional[str]
    """业务术语定义"""

    payload: Optional[object]
    """业务术语元数据"""

    term: Optional[str]
    """业务术语"""
