# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["UserMessage", "Content", "ContentAttachment"]


class ContentAttachment(BaseModel):
    info: object

    type: str
    """The type of the attachment"""


class Content(BaseModel):
    text: str

    attachments: Optional[List[ContentAttachment]] = None


class UserMessage(BaseModel):
    content: Content

    id: Optional[str] = None

    created_at: Optional[datetime] = None
    """创建时间"""

    name: Optional[str] = None

    role: Optional[Literal["human"]] = None
