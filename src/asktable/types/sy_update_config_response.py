# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["SyUpdateConfigResponse"]


class SyUpdateConfigResponse(BaseModel):
    global_table_limit: Optional[int] = None
    """表限制数量"""
