# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ...._models import BaseModel

__all__ = ["APIKeyListResponse", "APIKeyListResponseItem"]


class APIKeyListResponseItem(BaseModel):
    id: str
    """API Key ID"""

    ak_role: Literal["sys", "admin", "asker", "visitor"]
    """API key 的角色"""

    created_at: datetime
    """创建时间"""

    masked_ak_value: str
    """打码后的 API Key"""

    project_id: str
    """项目 ID"""

    status: int
    """状态"""

    last_used_at: Optional[datetime] = None
    """最后使用时间"""


APIKeyListResponse: TypeAlias = List[APIKeyListResponseItem]
