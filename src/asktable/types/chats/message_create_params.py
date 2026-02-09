# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["MessageCreateParams"]


class MessageCreateParams(TypedDict, total=False):
    query_question: Annotated[Optional[str], PropertyInfo(alias="question")]

    body_question: Annotated[Optional[str], PropertyInfo(alias="question")]
    """用户问题"""
