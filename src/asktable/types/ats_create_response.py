# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .._models import BaseModel

__all__ = ["ATSCreateResponse"]


class ATSCreateResponse(BaseModel):
    id: str
    """测试集的 ID"""

    created_at: datetime
    """测试集的创建时间"""

    datasource_id: str
    """该测试集对应数据源的 ID"""

    modified_at: datetime
    """测试集的修改时间"""

    name: str
    """测试集名称"""

    project_id: str
    """项目 ID"""
