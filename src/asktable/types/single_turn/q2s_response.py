# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["Q2sResponse", "Question"]


class Question(BaseModel):
    text: str

    keywords: Optional[List[str]] = None


class Q2sResponse(BaseModel):
    actual_used_table_names: List[str]

    ds_id: str

    header: object

    is_row_filtered: bool

    params: object

    prepared_statement: str

    question: Question

    cache_id: Optional[str] = None
