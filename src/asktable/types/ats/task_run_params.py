# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["TaskRunParams"]


class TaskRunParams(TypedDict, total=False):
    datasource_id: Required[str]
    """数据源 ID"""

    specific_case_ids: Required[List[str]]
    """测试用例 ID 列表"""
