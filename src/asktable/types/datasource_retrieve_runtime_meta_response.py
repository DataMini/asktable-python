# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DatasourceRetrieveRuntimeMetaResponse", "Schema"]


class Schema(BaseModel):
    name: str
    """表名称数据"""

    type: Literal["table", "view"]
    """表的类型"""


class DatasourceRetrieveRuntimeMetaResponse(BaseModel):
    schemas: Dict[str, List[Schema]]
    """元数据"""
