# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["TaskRunParams"]


class TaskRunParams(TypedDict, total=False):
    datasource_id: Required[str]
    """数据源 ID"""

    specific_case_ids: Required[SequenceNotStr[str]]
    """测试用例 ID 列表"""
