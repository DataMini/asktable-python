# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["Index"]


class Index(BaseModel):
    id: str
    """索引 ID"""

    created_at: datetime
    """创建时间"""

    datasource_id: str
    """数据源 ID"""

    field_name: str
    """字段名"""

    index_value_count: int
    """索引值总数"""

    modified_at: datetime
    """修改时间"""

    schema_name: str
    """模式名称"""

    table_name: str
    """表名"""

    avg_length: Optional[float] = None
    """平均长度"""

    distinct_count: Optional[int] = None
    """不同值数量"""

    max_length: Optional[int] = None
    """最大长度"""

    min_length: Optional[int] = None
    """最小长度"""

    status_msg: Optional[str] = None
    """状态信息"""

    value_count: Optional[int] = None
    """值总数"""
