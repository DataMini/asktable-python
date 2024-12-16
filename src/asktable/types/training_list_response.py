# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["TrainingListResponse"]


class TrainingListResponse(BaseModel):
    id: str
    """训练数据 ID"""

    created_at: datetime

    datasource_id: str
    """数据源 ID"""

    project_id: str
    """项目 ID"""

    question: str
    """用户问题"""

    source: Literal["import", "auto"]
    """训练数据来源"""

    sql: str
    """用户问题对应的 SQL"""

    chat_id: Optional[str] = None
    """聊天 ID"""

    msg_id: Optional[str] = None
    """消息 ID"""

    role_id: Optional[str] = None
    """角色 ID"""
