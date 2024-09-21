# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["MetaRetrieveParams"]


class MetaRetrieveParams(TypedDict, total=False):
    from_where: str
    """获取元数据的来源"""
