# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["Project"]


class Project(BaseModel):
    id: str
    """项目 ID"""

    created_at: datetime
    """创建时间"""

    locked: int
    """是否锁定"""

    modified_at: datetime
    """修改时间"""

    name: str
    """项目名称"""

    llm_model_group: Optional[str] = None
    """模型组，None 表示跟随系统默认"""
