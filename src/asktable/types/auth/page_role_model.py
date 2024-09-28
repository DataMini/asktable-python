# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .role_model import RoleModel

__all__ = ["PageRoleModel"]


class PageRoleModel(BaseModel):
    items: List[RoleModel]

    page: Optional[int] = None

    size: Optional[int] = None

    total: Optional[int] = None

    pages: Optional[int] = None
