# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .extapi_model import ExtapiModel

__all__ = ["ExtapiListResponse"]


class ExtapiListResponse(BaseModel):
    items: List[ExtapiModel]

    page: Optional[int] = None

    size: Optional[int] = None

    total: Optional[int] = None

    pages: Optional[int] = None
