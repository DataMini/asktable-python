# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import SequenceNotStr

__all__ = [
    "DatasourceUpdateParams",
    "AccessConfig",
    "AccessConfigAccessConfigConnectionUpdate",
    "AccessConfigAccessConfigFileUpdate",
    "AccessConfigAccessConfigFileUpdateFile",
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
            "bitable",
            "dap",
        ]
    ]
    """数据源引擎"""

    field_count: Optional[int]
    """字段数量"""

    meta_status: Optional[Literal["unavailable", "available"]]
    """数据源可用性"""

    name: Optional[str]
    """数据源的名称"""

    sample_questions: Optional[SequenceNotStr[str]]
    """示例问题"""

    schema_count: Optional[int]
    """库数量"""

    sync_error: Optional[Dict[str, object]]
    """同步错误信息"""

    sync_status: Optional[Literal["processing", "success", "failed", "warning"]]
    """同步状态"""

    table_count: Optional[int]
    """表数量"""


class AccessConfigAccessConfigConnectionUpdate(TypedDict, total=False):
    db: Optional[str]
    """数据库名称"""

    db_version: Optional[str]
    """数据库版本"""

    extra_config: Optional[Dict[str, object]]
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


class AccessConfigAccessConfigFileUpdateFile(TypedDict, total=False):
    id: Required[str]

    filename: Required[str]

    custom_config: Optional[Dict[str, object]]
    """文件自定义配置"""


class AccessConfigAccessConfigFileUpdate(TypedDict, total=False):
    files: Required[Iterable[AccessConfigAccessConfigFileUpdateFile]]
    """数据源文件 ID 列表"""


AccessConfig: TypeAlias = Union[AccessConfigAccessConfigConnectionUpdate, AccessConfigAccessConfigFileUpdate]
