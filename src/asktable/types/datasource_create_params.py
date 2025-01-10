# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "DatasourceCreateParams",
    "AccessConfig",
    "AccessConfigAccessConfigConnectionCreate",
    "AccessConfigAccessConfigFileCreate",
]


class DatasourceCreateParams(TypedDict, total=False):
    engine: Required[
        Literal[
            "mysql",
            "tidb",
            "postgresql",
            "oceanbase",
            "clickhouse",
            "csv",
            "excel",
            "starrocks",
            "hive",
            "oracle",
            "polardbmysql",
            "polardbpg",
        ]
    ]
    """数据源引擎"""

    async_process_meta: bool

    value_index: bool

    access_config: Optional[AccessConfig]
    """不同引擎有不同的配置"""

    name: Optional[str]
    """数据源的名称"""


class AccessConfigAccessConfigConnectionCreate(TypedDict, total=False):
    host: Required[str]
    """数据库地址"""

    db: Optional[str]
    """数据库名称"""

    db_version: Optional[str]
    """数据库版本"""

    extra_config: Optional[object]
    """额外配置"""

    password: Optional[str]
    """数据库密码"""

    port: int
    """数据库端口"""

    securetunnel_id: Optional[str]
    """安全隧道 ID"""

    user: Optional[str]
    """数据库用户名"""


class AccessConfigAccessConfigFileCreate(TypedDict, total=False):
    files: Required[List[str]]
    """数据源文件列表"""


AccessConfig: TypeAlias = Union[AccessConfigAccessConfigConnectionCreate, AccessConfigAccessConfigFileCreate]
