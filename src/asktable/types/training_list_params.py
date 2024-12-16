# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TrainingListParams"]


class TrainingListParams(TypedDict, total=False):
    datasource_id: Required[str]
    """数据源 ID"""

    page: int
    """Page number"""

    size: int
    """Page size"""
