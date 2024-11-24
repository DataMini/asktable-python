# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["Role"]


class Role(BaseModel):
    id: str

    created_at: datetime

    description: Optional[str] = None

    modified_at: datetime

    name: str
    """名称，小写英文字母，数字和下划线组合，不超过 64 个字符"""

    project_id: str

    policy_ids: Optional[List[str]] = None
    """策略列表。注意：如果为空或者不传则不绑定策略"""
