# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DataSource"]


class DataSource(BaseModel):
    id: str
    """数据源 ID"""

    created_at: datetime
    """创建时间"""

    engine: Literal["mysql", "tidb", "postgresql", "oceanbase", "clickhouse", "csv", "excel"]
    """数据源引擎"""

    meta_status: Literal["processing", "failed", "success", "unprocessed"]
    """元数据处理状态"""

    project_id: str
    """项目 ID"""

    field_count: Optional[int] = None
    """字段数量"""

    meta_error: Optional[str] = None
    """元数据处理错误"""

    name: Optional[str] = None
    """数据源的名称"""

    sample_questions: Optional[str] = None
    """示例问题"""

    schema_count: Optional[int] = None
    """库数量"""

    table_count: Optional[int] = None
    """表数量"""