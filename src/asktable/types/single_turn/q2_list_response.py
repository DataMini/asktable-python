# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .q2s_model import Q2sModel

__all__ = ["Q2ListResponse"]


class Q2ListResponse(BaseModel):
    items: List[Q2sModel]

    page: Optional[int] = None

    size: Optional[int] = None

    total: Optional[int] = None

    pages: Optional[int] = None
