# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .data_source_out import DataSourceOut

__all__ = ["PageDataSourceOut"]


class PageDataSourceOut(BaseModel):
    items: List[DataSourceOut]

    page: Optional[int] = None

    size: Optional[int] = None

    total: Optional[int] = None

    pages: Optional[int] = None
