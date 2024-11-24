# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ExtapiRoute"]


class ExtapiRoute(BaseModel):
    id: str

    created_at: datetime

    extapi_id: str

    method: Literal["GET", "POST", "PUT", "DELETE"]
    """HTTP 方法"""

    name: str
    """API 方法名称，不超过 64 个字符"""

    path: str
    """API 路径"""

    project_id: str

    body_params_desc: Optional[str] = None
    """请求体参数描述"""

    path_params_desc: Optional[str] = None
    """路径参数描述"""

    query_params_desc: Optional[str] = None
    """查询参数描述"""

    updated_at: Optional[datetime] = None
