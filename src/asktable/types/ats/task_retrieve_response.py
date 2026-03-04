# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["TaskRetrieveResponse"]


class TaskRetrieveResponse(BaseModel):
    id: str
    """测试任务 ID"""

    accuracy: float
    """测试正确率"""

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

    suite_id: str
    """测试集 ID"""

    total_case_count: int
    """测试用例总数"""

    duration: Optional[float] = None
    """测试任务时间,单位为秒"""

    last_run: Optional[datetime] = None
    """上次测试运行时间"""

    api_model_group: Optional[Dict[str, object]] = FieldInfo(alias="model_group", default=None)
    """运行使用的模型组"""

    status_message: Optional[str] = None
    """测试日志"""
