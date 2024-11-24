# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["Extapi"]


class Extapi(BaseModel):
    id: str

    base_url: str
    """根 URL"""

    created_at: datetime

    name: str
    """名称，不超过 64 个字符"""

    project_id: str

    headers: Optional[Dict[str, str]] = None
    """HTTP Headers，JSON 格式"""

    updated_at: Optional[datetime] = None
