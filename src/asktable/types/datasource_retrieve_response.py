# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = [
    "DatasourceRetrieveResponse",
    "AccessConfig",
    "AccessConfigAccessConfigConnectionResponse",
    "AccessConfigAccessConfigFileResponse",
    "AccessConfigAccessConfigFileResponseFile",
    "AccessConfigAccessConfigWorkbookResponse",
]


class AccessConfigAccessConfigConnectionResponse(BaseModel):
    atst_link_id: Optional[str] = None
    """安全隧道链接 ID"""

    db: Optional[str] = None
    """数据库名称"""

    db_version: Optional[str] = None
    """数据库版本"""

    extra_config: Optional[Dict[str, object]] = None
    """额外配置"""

    host: Optional[str] = None
    """数据库地址"""

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


class AccessConfigAccessConfigFileResponseFile(BaseModel):
    id: str

    filename: str

    custom_config: Optional[Dict[str, object]] = None
    """文件自定义配置"""


class AccessConfigAccessConfigFileResponse(BaseModel):
    files: List[AccessConfigAccessConfigFileResponseFile]
    """数据源文件 ID 列表"""


class AccessConfigAccessConfigWorkbookResponse(BaseModel):
    workbook_id: Optional[str] = None
    """workbook 标识，等于 datasource_id；创建时由 flow 分配"""


AccessConfig: TypeAlias = Union[
    AccessConfigAccessConfigConnectionResponse,
    AccessConfigAccessConfigFileResponse,
    AccessConfigAccessConfigWorkbookResponse,
    None,
]


class DatasourceRetrieveResponse(BaseModel):
    id: str
    """数据源 ID"""

    created_at: datetime
    """创建时间"""

    engine: Literal[
        "mysql",
        "tidb",
        "postgresql",
        "oceanbase",
        "clickhouse",
        "excel",
        "starrocks",
        "hive",
        "oracle",
        "polardbmysql",
        "polardbpg",
        "dameng",
        "adbmysql",
        "adbpostgres",
        "xugu",
        "doris",
        "greenplum",
        "selectdb",
        "databend",
        "sqlserver",
        "mogdb",
        "hologres",
        "maxcompute",
        "gaussdb",
        "tdsqlmysql",
        "tdsqlpg",
        "kingbasees",
        "gbase8c",
        "yashandb",
        "gbase8a",
        "gaussdbdws",
        "bigquery",
        "dap",
        "duckdb",
        "workbook",
    ]
    """数据源引擎"""

    meta_status: Literal["unavailable", "available"]
    """数据源可用性"""

    modified_at: datetime
    """修改时间"""

    project_id: str
    """项目 ID"""

    sync_status: Literal["queued", "processing", "success", "failed", "warning"]
    """同步状态"""

    access_config: Optional[AccessConfig] = None
    """访问数据源的配置信息"""

    desc: Optional[str] = None
    """数据源描述"""

    field_count: Optional[int] = None
    """字段数量"""

    name: Optional[str] = None
    """数据源的名称"""

    sample_questions: Optional[List[str]] = None
    """示例问题"""

    schema_count: Optional[int] = None
    """库数量"""

    sync_error: Optional[Dict[str, object]] = None
    """同步错误信息"""

    synced_at: Optional[datetime] = None
    """上次同步完成时间"""

    table_count: Optional[int] = None
    """表数量"""
