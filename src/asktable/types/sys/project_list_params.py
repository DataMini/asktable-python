# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import TypedDict

__all__ = ["ProjectListParams"]


class ProjectListParams(TypedDict, total=False):
    page: int
    """Page number"""

    project_ids: Optional[List[str]]
    """项目 ID 列表"""

    size: int
    """Page size"""
