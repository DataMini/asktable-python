# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["TaskRunResponse"]


class TaskRunResponse(BaseModel):
    id: str
    """测试任务 ID"""

    accuracy: float
    """测试正确率"""

    ats_id: str
    """测试集 ID"""

    completed_case_count: int
    """已完成测试用例数"""

    created_at: datetime
    """创建时间"""

    failed_case_count: int
    """未通过测试用例数"""

    modified_at: datetime
    """修改时间"""

    passed_case_count: int
    """通过测试用例数"""

    status: str
    """测试状态"""

    total_case_count: int
    """测试用例总数"""

    duration: Optional[float] = None
    """测试任务时间,单位为秒"""

    last_run: Optional[datetime] = None
    """上次测试运行时间"""

    status_message: Optional[str] = None
    """测试日志"""
