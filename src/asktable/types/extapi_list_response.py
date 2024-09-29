# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .ext_api_model import ExtAPIModel

__all__ = ["ExtapiListResponse"]


class ExtapiListResponse(BaseModel):
    items: List[ExtAPIModel]

    page: Optional[int] = None

    size: Optional[int] = None

    total: Optional[int] = None

    pages: Optional[int] = None
