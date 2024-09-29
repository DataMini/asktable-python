# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["SecureTunnelLink", "Item"]


class Item(BaseModel):
    id: str

    created_at: datetime

    datasource_ids: List[str]

    modified_at: datetime

    proxy_port: int

    securetunnel_id: str

    status: str

    target_host: str

    target_port: int


class SecureTunnelLink(BaseModel):
    items: List[Item]

    page: Optional[int] = None

    size: Optional[int] = None

    total: Optional[int] = None

    pages: Optional[int] = None
