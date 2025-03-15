# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from .._models import BaseModel

__all__ = ["DataframeRetrieveResponse"]


class DataframeRetrieveResponse(BaseModel):
    id: str
    """ID"""

    chart_options: object
    """图表选项"""

    content: List[object]
    """内容"""

    created_at: datetime
    """创建时间"""

    header: List[object]
    """表头"""

    modified_at: datetime
    """更新时间"""

    msg_id: str
    """消息 ID"""

    project_id: str
    """项目 ID"""

    row_count: int
    """行数"""

    sql: str
    """SQL"""

    title: str
    """标题"""
