# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = ["TrainingCreateResponse", "TrainingCreateResponseItem"]


class TrainingCreateResponseItem(BaseModel):
    id: str
    """训练数据 ID"""

    created_at: datetime
    """创建时间"""

    datasource_id: str
    """数据源 ID"""

    modified_at: datetime
    """更新时间"""

    project_id: str
    """项目 ID"""

    question: str
    """用户问题"""

    source: Literal["import", "auto"]
    """训练数据来源"""

    sql: str
    """用户问题对应的 SQL"""

    active: Optional[bool] = None
    """是否启用"""

    chat_id: Optional[str] = None
    """聊天 ID"""

    msg_id: Optional[str] = None
    """消息 ID"""

    role_id: Optional[str] = None
    """角色 ID"""


TrainingCreateResponse: TypeAlias = List[TrainingCreateResponseItem]
