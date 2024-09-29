# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .role import Role
from .._models import BaseModel

__all__ = ["RoleListResponse"]


class RoleListResponse(BaseModel):
    items: List[Role]

    page: Optional[int] = None

    size: Optional[int] = None

    total: Optional[int] = None

    pages: Optional[int] = None
