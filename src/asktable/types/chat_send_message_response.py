# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .ai_message import AIMessage
from .tool_message import ToolMessage
from .user_message import UserMessage

__all__ = ["ChatSendMessageResponse"]

ChatSendMessageResponse: TypeAlias = Union[UserMessage, AIMessage, ToolMessage]
