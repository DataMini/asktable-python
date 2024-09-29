# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .data_source import DataSource

__all__ = ["DatasourceListResponse"]


class DatasourceListResponse(BaseModel):
    items: List[DataSource]

    page: Optional[int] = None

    size: Optional[int] = None

    total: Optional[int] = None

    pages: Optional[int] = None
