# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ExtapiCreateParams"]


class ExtapiCreateParams(TypedDict, total=False):
    id: Required[str]

    base_url: Required[str]
    """根 URL"""

    created_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]

    name: Required[str]
    """名称，不超过 64 个字符"""

    project_id: Required[str]

    headers: Optional[Dict[str, str]]
    """HTTP Headers，JSON 格式"""

    updated_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
