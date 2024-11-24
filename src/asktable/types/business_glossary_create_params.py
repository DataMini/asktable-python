# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["BusinessGlossaryCreateParams", "Body"]


class BusinessGlossaryCreateParams(TypedDict, total=False):
    body: Required[Iterable[Body]]


class Body(TypedDict, total=False):
    definition: Required[str]
    """业务术语定义"""

    term: Required[str]
    """业务术语"""

    aliases: Optional[List[str]]
    """业务术语同义词"""

    payload: Optional[object]
    """业务术语元数据"""
