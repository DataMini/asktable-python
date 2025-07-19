# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["TestCaseRetrieveResponse"]


class TestCaseRetrieveResponse(BaseModel):
    __test__ = False
    id: str
    """测试样例 ID"""

    ats_id: str
    """所属的测试集 ID"""

    created_at: datetime
    """创建时间"""

    expected_sql: str
    """用户期望生成的 sql"""

    modified_at: datetime
    """修改时间"""

    question: str
    """用户提问"""

    role_id: Optional[str] = None
    """角色 ID"""

    role_variables: Optional[object] = None
    """在扮演这个角色时需要传递的变量值，用 Key-Value 形式传递"""
