# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["EntryWithDefinition"]


class EntryWithDefinition(BaseModel):
    id: str
    """业务术语 ID"""

    created_at: datetime
    """创建时间"""

    definition: str
    """业务术语定义"""

    modified_at: datetime
    """更新时间"""

    project_id: str
    """项目 ID"""

    term: str
    """业务术语"""

    aliases: Optional[List[str]] = None
    """业务术语同义词"""

    payload: Optional[object] = None
    """业务术语元数据"""
