# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["RouteCreateParams"]


class RouteCreateParams(TypedDict, total=False):
    path_extapi_id: Required[Annotated[str, PropertyInfo(alias="extapi_id")]]

    id: Required[str]

    created_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]

    body_extapi_id: Required[Annotated[str, PropertyInfo(alias="extapi_id")]]

    method: Required[Literal["GET", "POST", "PUT", "DELETE"]]
    """HTTP 方法"""

    name: Required[str]
    """API 方法名称，不超过 64 个字符"""

    path: Required[str]
    """API 路径"""

    project_id: Required[str]

    body_params_desc: Optional[str]
    """请求体参数描述"""

    path_params_desc: Optional[str]
    """路径参数描述"""

    query_params_desc: Optional[str]
    """查询参数描述"""

    updated_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
