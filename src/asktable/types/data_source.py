# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DataSource", "AccessConfig"]


class AccessConfig(BaseModel):
    db: Optional[str] = None
    """数据库引擎可以管理多个数据库，此参数用于指定数据库名称"""

    host: Optional[str] = None
    """数据库地址"""

    location_type: Optional[str] = None
    """Excel/CSV 文件位置"""

    location_url: Optional[str] = None
    """Excel/CSV 文件下载地址"""

    port: Optional[int] = None
    """数据库端口"""

    securetunnel_id: Optional[str] = None
    """安全隧道 ID"""

    user: Optional[str] = None
    """数据库用户名"""


class DataSource(BaseModel):
    id: str
    """数据源 ID"""

    access_config: AccessConfig

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
