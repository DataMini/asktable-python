# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["DatasourceUpdateParams", "AccessConfig"]


class DatasourceUpdateParams(TypedDict, total=False):
    access_config: Optional[AccessConfig]
    """不同引擎有不同的配置"""

    desc: Optional[str]
    """数据源描述"""

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
