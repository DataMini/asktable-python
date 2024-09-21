# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .secure_tunnel import SecureTunnel

__all__ = ["SecuretunnelListResponse"]


class SecuretunnelListResponse(BaseModel):
    items: List[SecureTunnel]

    page: Optional[int] = None

    size: Optional[int] = None

    total: Optional[int] = None

    pages: Optional[int] = None
