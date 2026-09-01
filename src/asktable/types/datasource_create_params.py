# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import SequenceNotStr

__all__ = [
    "DatasourceCreateParams",
    "AccessConfig",
    "AccessConfigAccessConfigConnectionCreate",
    "AccessConfigAccessConfigFileCreate",
    "AccessConfigAccessConfigWorkbookCreate",
]


class DatasourceCreateParams(TypedDict, total=False):
    engine: Required[
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
            "bigquery",
            "dap",
            "duckdb",
            "workbook",
        ]
    ]
    """数据源引擎"""

    access_config: Optional[AccessConfig]
    """不同引擎有不同的配置"""

    name: Optional[str]
    """数据源的名称"""


class AccessConfigAccessConfigConnectionCreate(TypedDict, total=False):
    credentials: Optional[str]
    """数据库凭证 JSON"""

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

    user: Optional[str]
    """数据库用户名"""


class AccessConfigAccessConfigFileCreate(TypedDict, total=False):
    files: Required[SequenceNotStr[str]]
    """数据源文件 URL 列表, 创建时可以传入 URL"""


class AccessConfigAccessConfigWorkbookCreate(TypedDict, total=False):
    """workbook 创建时前端不传 workbook_id，flow 用 datasource_id 填充。"""

    workbook_id: Optional[str]
    """workbook 标识，等于 datasource_id；创建时由 flow 分配"""


AccessConfig: TypeAlias = Union[
    AccessConfigAccessConfigConnectionCreate, AccessConfigAccessConfigFileCreate, AccessConfigAccessConfigWorkbookCreate
]
