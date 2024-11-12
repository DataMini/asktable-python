# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["KBCreateParams", "Body"]


class KBCreateParams(TypedDict, total=False):
    body: Required[Iterable[Body]]


class Body(TypedDict, total=False):
    content: Required[str]
    """文档内容"""

    name: Required[str]
    """文档名称"""

    payload: Optional[object]
    """文档元数据"""

    synonyms: Optional[List[str]]
    """文档同义词"""
