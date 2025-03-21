# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "DatasourceUpdateParams",
    "AccessConfig",
    "AccessConfigAccessConfigConnectionUpdate",
    "AccessConfigAccessConfigFileUpdate",
]


class DatasourceUpdateParams(TypedDict, total=False):
    access_config: Optional[AccessConfig]
    """不同引擎有不同的配置"""

    desc: Optional[str]
    """数据源描述"""

    engine: Optional[
        Literal[
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
    ]
    """数据源引擎"""

    field_count: Optional[int]
    """字段数量"""

    meta_error: Optional[str]
    """元数据处理错误"""

    meta_status: Optional[Literal["processing", "failed", "success", "unprocessed"]]
    """元数据处理状态"""

    name: Optional[str]
    """数据源的名称"""

    sample_questions: Optional[str]
    """示例问题"""

    schema_count: Optional[int]
    """库数量"""

    table_count: Optional[int]
    """表数量"""


class AccessConfigAccessConfigConnectionUpdate(TypedDict, total=False):
    db: Optional[str]
    """数据库名称"""

    db_version: Optional[str]
    """数据库版本"""

    extra_config: Optional[object]
    """额外配置"""

    host: Optional[str]
    """数据库地址"""

    password: Optional[str]
    """数据库密码"""

    port: Optional[int]
    """数据库端口"""

    securetunnel_id: Optional[str]
    """安全隧道 ID"""

    user: Optional[str]
    """数据库用户名"""


class AccessConfigAccessConfigFileUpdate(TypedDict, total=False):
    files: Required[List[str]]
    """数据源文件列表"""


AccessConfig: TypeAlias = Union[AccessConfigAccessConfigConnectionUpdate, AccessConfigAccessConfigFileUpdate]
