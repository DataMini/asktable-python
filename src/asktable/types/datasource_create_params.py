# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["DatasourceCreateParams", "AccessConfig"]


class DatasourceCreateParams(TypedDict, total=False):
    access_config: Required[AccessConfig]
    """不同引擎有不同的配置"""

    engine: Required[Literal["mysql", "tidb", "postgresql", "oceanbase", "clickhouse", "csv", "excel"]]
    """数据源引擎"""

    async_process_meta: bool
    """是否异步处理元数据"""

    skip_process_meta: bool
    """是否跳过元数据处理"""

    name: Optional[str]
    """数据源的名称"""


class AccessConfig(TypedDict, total=False):
    db: Optional[str]
    """数据库引擎可以管理多个数据库，此参数用于指定数据库名称"""

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

    securetunnel_id: Optional[str]
    """安全隧道 ID"""

    user: Optional[str]
    """数据库用户名"""
