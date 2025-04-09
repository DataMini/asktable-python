# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = [
    "DatasourceRetrieveResponse",
    "AccessConfig",
    "AccessConfigAccessConfigConnectionResponse",
    "AccessConfigAccessConfigFileResponse",
]


class AccessConfigAccessConfigConnectionResponse(BaseModel):
    host: str
    """数据库地址"""

    atst_link_id: Optional[str] = None
    """安全隧道链接 ID"""

    db: Optional[str] = None
    """数据库名称"""

    db_version: Optional[str] = None
    """数据库版本"""

    extra_config: Optional[object] = None
    """额外配置"""

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


class AccessConfigAccessConfigFileResponse(BaseModel):
    files: List[str]
    """数据源文件列表"""


AccessConfig: TypeAlias = Union[AccessConfigAccessConfigConnectionResponse, AccessConfigAccessConfigFileResponse, None]


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
    ]
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
