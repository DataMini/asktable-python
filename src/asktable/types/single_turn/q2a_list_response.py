# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .q2a_model import Q2aModel

__all__ = ["Q2aListResponse"]


class Q2aListResponse(BaseModel):
    items: List[Q2aModel]

    page: Optional[int] = None

    size: Optional[int] = None

    total: Optional[int] = None

    pages: Optional[int] = None
