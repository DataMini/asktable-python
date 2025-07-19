# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["TestCaseCreateParams"]


class TestCaseCreateParams(TypedDict, total=False):
    expected_sql: Required[str]
    """用户期望生成的 sql"""

    question: Required[str]
    """用户提问"""

    role_id: Optional[str]
    """角色 ID"""

    role_variables: Optional[object]
    """在扮演这个角色时需要传递的变量值，用 Key-Value 形式传递"""
