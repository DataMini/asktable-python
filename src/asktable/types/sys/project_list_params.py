# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from ..._types import SequenceNotStr

__all__ = ["ProjectListParams"]


class ProjectListParams(TypedDict, total=False):
    page: int
    """Page number"""

    project_ids: Optional[SequenceNotStr[str]]
    """项目 ID 列表"""

    size: int
    """Page size"""
