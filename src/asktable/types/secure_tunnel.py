# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["SecureTunnel"]


class SecureTunnel(BaseModel):
    id: str

    created_at: datetime

    modified_at: datetime

    name: str
    """SecureTunnel 名称，不超过 20 个字符"""

    project_id: str

    status: str

    atst_server_host: Optional[str] = None

    atst_server_port: Optional[int] = None

    info: Optional[object] = None

    links_count: Optional[int] = None

    unique_key: Optional[str] = None
