# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["DataframeRetrieveResponse"]


class DataframeRetrieveResponse(BaseModel):
    id: str
    """ID"""

    chart_options: Dict[str, object]
    """图表选项"""

    created_at: datetime
    """创建时间"""

    header: List[Dict[str, object]]
    """表头"""

    modified_at: datetime
    """更新时间"""

    project_id: str
    """项目 ID"""

    row_count: int
    """行数"""

    sql: str
    """SQL"""

    title: str
    """标题"""

    content: Optional[List[Dict[str, object]]] = None
    """内容"""

    msg_id: Optional[str] = None
    """消息 ID"""
