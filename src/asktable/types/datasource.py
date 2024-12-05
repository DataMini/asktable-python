# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Datasource", "AccessConfig"]


class AccessConfig(BaseModel):
    atst_link_id: Optional[str] = None
    """安全隧道链接 ID"""

    db: Optional[str] = None
    """数据库引擎可以管理多个数据库，此参数用于指定数据库名称"""

    db_version: Optional[str] = None
    """数据库版本"""

    host: Optional[str] = None
    """数据库地址"""

    location_type: Optional[str] = None
    """Excel/CSV 文件位置"""

    location_url: Optional[str] = None
    """Excel/CSV 文件下载地址"""

    port: Optional[int] = None
    """数据库端口"""

    proxy_host: Optional[str] = None
    """数据源代理地址"""

    proxy_port: Optional[int] = None
    """数据源代理端口"""

    securetunnel_id: Optional[str] = None
    """安全隧道 ID"""

    user: Optional[str] = None
    """数据库用户名"""


class Datasource(BaseModel):
    id: str
    """数据源 ID"""

    created_at: datetime
    """创建时间"""

    engine: Literal["mysql", "tidb", "postgresql", "oceanbase", "clickhouse", "csv", "excel", "starrocks", "hive"]
    """数据源引擎"""

    meta_status: Literal["processing", "failed", "success", "unprocessed"]
    """元数据处理状态"""

    modified_at: datetime
    """修改时间"""

    project_id: str
    """项目 ID"""

    access_config: Optional[AccessConfig] = None
    """访问数据源的配置信息"""

    desc: Optional[str] = None
    """数据源描述"""

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
