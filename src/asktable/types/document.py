# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["Document"]


class Document(BaseModel):
    id: str
    """文档 ID"""

    created_at: datetime
    """创建时间"""

    name: str
    """文档名称"""

    project_id: str
    """项目 ID"""

    updated_at: datetime
    """更新时间"""

    payload: Optional[object] = None
    """文档元数据"""

    synonyms: Optional[List[str]] = None
    """文档同义词"""
