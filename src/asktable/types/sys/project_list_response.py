# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["ProjectListResponse", "Item"]


class Item(BaseModel):
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


class ProjectListResponse(BaseModel):
    items: List[Item]

    page: Optional[int] = None

    size: Optional[int] = None

    total: Optional[int] = None

    pages: Optional[int] = None
