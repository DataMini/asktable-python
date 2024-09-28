# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..shared.message_model import MessageModel

__all__ = ["PageMessageModel"]


class PageMessageModel(BaseModel):
    items: List[MessageModel]

    page: Optional[int] = None

    size: Optional[int] = None

    total: Optional[int] = None

    pages: Optional[int] = None
