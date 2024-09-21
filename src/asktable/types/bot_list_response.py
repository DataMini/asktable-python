# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .chat_bot import ChatBot

__all__ = ["BotListResponse"]


class BotListResponse(BaseModel):
    items: List[ChatBot]

    page: Optional[int] = None

    size: Optional[int] = None

    total: Optional[int] = None

    pages: Optional[int] = None
