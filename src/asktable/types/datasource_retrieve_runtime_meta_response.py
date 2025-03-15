# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List

from .._models import BaseModel

__all__ = ["DatasourceRetrieveRuntimeMetaResponse"]


class DatasourceRetrieveRuntimeMetaResponse(BaseModel):
    schemas: Dict[str, List[str]]
    """元数据"""
