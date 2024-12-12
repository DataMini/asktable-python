# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = [
    "MessageRetrieveResponse",
    "MessageUser",
    "MessageUserContent",
    "MessageUserContentAttachment",
    "MessageAssistant",
    "MessageAssistantContent",
    "MessageAssistantContentAttachment",
    "MessageAssistantToolCall",
    "MessageAssistantToolCallFunction",
    "MessageTool",
    "MessageToolContent",
    "MessageToolContentAttachment",
]


class MessageUserContentAttachment(BaseModel):
    info: object

    type: str
    """The type of the attachment"""


class MessageUserContent(BaseModel):
    text: str

    attachments: Optional[List[MessageUserContentAttachment]] = None


class MessageUser(BaseModel):
    content: MessageUserContent

    id: Optional[str] = None

    created_at: Optional[datetime] = None
    """创建时间"""

    name: Optional[str] = None

    role: Optional[Literal["human"]] = None


class MessageAssistantContentAttachment(BaseModel):
    info: object

    type: str
    """The type of the attachment"""


class MessageAssistantContent(BaseModel):
    text: str

    attachments: Optional[List[MessageAssistantContentAttachment]] = None


class MessageAssistantToolCallFunction(BaseModel):
    arguments: Dict[str, Union[str, float, bool, None]]

    name: str


class MessageAssistantToolCall(BaseModel):
    id: str

    function: MessageAssistantToolCallFunction

    type: Optional[Literal["function"]] = None


class MessageAssistant(BaseModel):
    content: MessageAssistantContent

    id: Optional[str] = None

    created_at: Optional[datetime] = None
    """创建时间"""

    end_turn: Optional[bool] = None

    metadata: Optional[object] = None

    name: Optional[str] = None

    reply_to_msg_id: Optional[str] = None

    role: Optional[Literal["ai"]] = None

    status: Optional[str] = None

    tool_calls: Optional[List[MessageAssistantToolCall]] = None

    trace_id: Optional[str] = None


class MessageToolContentAttachment(BaseModel):
    info: object

    type: str
    """The type of the attachment"""


class MessageToolContent(BaseModel):
    text: str

    attachments: Optional[List[MessageToolContentAttachment]] = None


class MessageTool(BaseModel):
    content: MessageToolContent

    tool_call_id: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None
    """创建时间"""

    name: Optional[str] = None

    role: Optional[Literal["tool"]] = None


MessageRetrieveResponse: TypeAlias = Union[MessageUser, MessageAssistant, MessageTool]
