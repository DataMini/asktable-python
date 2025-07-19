# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ATSCreateParams"]


class ATSCreateParams(TypedDict, total=False):
    datasource_id: Required[str]
    """该测试集对应数据源的 ID"""

    name: Required[str]
    """测试集名称"""
