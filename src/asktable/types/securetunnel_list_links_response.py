# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from .._models import BaseModel

__all__ = ["SecuretunnelListLinksResponse"]


class SecuretunnelListLinksResponse(BaseModel):
    id: str

    atst_id: str

    created_at: datetime

    datasource_ids: List[str]

    modified_at: datetime

    proxy_port: int

    status: str

    target_host: str

    target_port: int
