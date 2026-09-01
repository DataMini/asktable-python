# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["APIKey"]


class APIKey(BaseModel):
    id: str
    """API Key ID"""

    ak_role: Literal["sys", "admin", "asker"]

    created_at: datetime
    """创建时间"""

    masked_ak_value: str
    """打码后的 API Key"""

    project_id: str
    """项目 ID"""

    status: int
    """状态"""

    created_by: Optional[str] = None
    """创建者 User ID"""

    expires_at: Optional[datetime] = None
    """过期时间"""

    last_used_at: Optional[datetime] = None
    """最后使用时间"""

    name: Optional[str] = None
    """API Key 名称；旧 key 可为空"""
