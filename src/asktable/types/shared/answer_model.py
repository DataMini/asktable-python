# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["AnswerModel", "Attachment", "QueryInsight", "QueryInsightInsight"]


class Attachment(BaseModel):
    info: object

    type: str
    """The type of the attachment"""


class QueryInsightInsight(BaseModel):
    duration: float

    name: str

    detail: Optional[object] = None


class QueryInsight(BaseModel):
    datasource_id: str

    insight: List[QueryInsightInsight]

    question: str

    task: str


class AnswerModel(BaseModel):
    attachments: Optional[List[Attachment]] = None

    duration: int

    error_detail: Optional[str] = None

    error_msg: Optional[str] = None

    payload: Optional[object] = None

    query_insight: Optional[QueryInsight] = None

    status: str

    text: str
