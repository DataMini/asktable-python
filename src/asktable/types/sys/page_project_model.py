# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .project_model import ProjectModel

__all__ = ["PageProjectModel"]


class PageProjectModel(BaseModel):
    items: List[ProjectModel]

    page: Optional[int] = None

    size: Optional[int] = None

    total: Optional[int] = None

    pages: Optional[int] = None
