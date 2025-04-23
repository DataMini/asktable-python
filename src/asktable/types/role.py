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

    project_id: str

    policy_ids: Optional[List[str]] = None
    """策略列表。注意：如果为空或者不传则不绑定策略"""
