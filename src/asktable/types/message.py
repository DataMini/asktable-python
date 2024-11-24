# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Message"]


class Message(BaseModel):
    id: str

    content: object

    created_at: datetime
    """创建时间"""

    role: Literal["human", "ai"]

    reply_to_msg_id: Optional[str] = None

    trace_id: Optional[str] = None
