# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AIMessage", "Content", "ContentAttachment", "ToolCall", "ToolCallFunction"]


class ContentAttachment(BaseModel):
    info: object

    type: str
    """The type of the attachment"""


class Content(BaseModel):
    text: str

    attachments: Optional[List[ContentAttachment]] = None


class ToolCallFunction(BaseModel):
    arguments: Dict[str, Union[str, float, bool, None]]

    name: str


class ToolCall(BaseModel):
    id: str

    function: ToolCallFunction

    type: Optional[Literal["function"]] = None


class AIMessage(BaseModel):
    content: Content

    id: Optional[str] = None

    created_at: Optional[datetime] = None
    """创建时间"""

    end_turn: Optional[bool] = None

    metadata: Optional[object] = None

    name: Optional[str] = None

    reply_to_msg_id: Optional[str] = None

    role: Optional[Literal["ai"]] = None

    status: Optional[str] = None

    tool_calls: Optional[List[ToolCall]] = None

    trace_id: Optional[str] = None
