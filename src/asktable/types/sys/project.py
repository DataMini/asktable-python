# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from ..._models import BaseModel

__all__ = ["Project"]


class Project(BaseModel):
    id: str
    """项目 ID"""

    created_at: datetime
    """创建时间"""

    llm_model_group: str
    """模型组"""

    locked: int
    """是否锁定"""

    modified_at: datetime
    """修改时间"""

    name: str
    """项目名称"""
