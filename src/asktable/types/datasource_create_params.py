# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["DatasourceCreateParams", "AccessConfig"]


class DatasourceCreateParams(TypedDict, total=False):
    engine: Required[
        Literal["mysql", "tidb", "postgresql", "oceanbase", "clickhouse", "csv", "excel", "starrocks", "hive"]
    ]
    """数据源引擎"""

    async_process_meta: bool

    value_index: bool

    access_config: Optional[AccessConfig]
    """不同引擎有不同的配置"""

    name: Optional[str]
    """数据源的名称"""


class AccessConfig(TypedDict, total=False):
    atst_link_id: Optional[str]
    """安全隧道链接 ID"""

    db: Optional[str]
    """数据库引擎可以管理多个数据库，此参数用于指定数据库名称"""

    db_version: Optional[str]
    """数据库版本"""

    host: Optional[str]
    """数据库地址"""

    location_type: Optional[str]
    """Excel/CSV 文件位置"""

    location_url: Optional[str]
    """Excel/CSV 文件下载地址"""

    password: Optional[str]
    """数据库密码"""

    port: Optional[int]
    """数据库端口"""

    proxy_host: Optional[str]
    """数据源代理地址"""

    proxy_port: Optional[int]
    """数据源代理端口"""

    securetunnel_id: Optional[str]
    """安全隧道 ID"""

    user: Optional[str]
    """数据库用户名"""
