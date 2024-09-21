# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from ..._models import BaseModel

__all__ = ["Project"]


class Project(BaseModel):
    id: str

    created_at: datetime

    locked: int

    modified_at: datetime

    name: str
    """项目名称"""
