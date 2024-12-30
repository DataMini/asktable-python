# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["AnswerCreateParams"]


class AnswerCreateParams(TypedDict, total=False):
    datasource_id: Required[str]
    """数据源 ID"""

    question: Required[str]
    """查询语句"""

    max_rows: Optional[int]
    """最大返回行数，默认为 0，即不限制返回行数"""

    role_id: Optional[str]
    """
    角色 ID，将扮演这个角色来执行对话，用于权限控制。若无，则跳过鉴权，即可查询所有
    数据
    """

    role_variables: Optional[object]
    """在扮演这个角色时需要传递的变量值，用 Key-Value 形式传递"""

    with_json: Optional[bool]
    """是否同时将数据，作为 json 格式的附件一起返回"""
