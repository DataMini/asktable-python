# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Datasource"]


class Datasource(BaseModel):
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
        "bitable",
        "dap",
    ]
    """数据源引擎"""

    meta_status: Literal["unavailable", "available"]
    """数据源可用性"""

    modified_at: datetime
    """修改时间"""

    project_id: str
    """项目 ID"""

    sync_status: Literal["processing", "success", "failed", "warning"]
    """同步状态"""

    desc: Optional[str] = None
    """数据源描述"""

    field_count: Optional[int] = None
    """字段数量"""

    name: Optional[str] = None
    """数据源的名称"""

    sample_questions: Optional[str] = None
    """示例问题"""

    schema_count: Optional[int] = None
    """库数量"""

    sync_error: Optional[Dict[str, object]] = None
    """同步错误信息"""

    synced_at: Optional[datetime] = None
    """上次同步完成时间"""

    table_count: Optional[int] = None
    """表数量"""
