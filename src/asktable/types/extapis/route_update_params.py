# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["RouteUpdateParams"]


class RouteUpdateParams(TypedDict, total=False):
    extapi_id: Required[str]

    body_params_desc: Optional[str]
    """请求体参数描述"""

    method: Optional[Literal["GET", "POST", "PUT", "DELETE"]]
    """HTTP 方法"""

    name: Optional[str]
    """API 方法名称，不超过 64 个字符"""

    path: Optional[str]
    """API 路径"""

    path_params_desc: Optional[str]
    """路径参数描述"""

    query_params_desc: Optional[str]
    """查询参数描述"""
