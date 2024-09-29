# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .shared.policy import Policy

__all__ = ["PolicyListResponse"]


class PolicyListResponse(BaseModel):
    items: List[Policy]

    page: Optional[int] = None

    size: Optional[int] = None

    total: Optional[int] = None

    pages: Optional[int] = None
