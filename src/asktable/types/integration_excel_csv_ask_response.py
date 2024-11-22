# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["IntegrationExcelCsvAskResponse", "Answer", "Datasource", "DatasourceAccessConfig"]


class Answer(BaseModel):
    id: str

    answer: Optional[object] = None

    created_at: datetime

    datasource_id: str
    """数据源 ID"""

    duration: int

    modified_at: datetime

    project_id: str

    question: str

    status: str

    err_msg: Optional[str] = None
    """错误信息"""

    max_rows: Optional[int] = None
    """最大返回行数，默认为 0，即不限制返回行数"""

    role_id: Optional[str] = None
    """
    角色 ID，将扮演这个角色来执行对话，用于权限控制。若无，则跳过鉴权，即可查询所有
    数据
    """

    role_variables: Optional[object] = None
    """在扮演这个角色时需要传递的变量值，用 Key-Value 形式传递"""

    with_json: Optional[bool] = None
    """是否同时将数据，作为 json 格式的附件一起返回"""


class DatasourceAccessConfig(BaseModel):
    atst_link_id: Optional[str] = None
    """安全隧道链接 ID"""

    db: Optional[str] = None
    """数据库引擎可以管理多个数据库，此参数用于指定数据库名称"""

    host: Optional[str] = None
    """数据库地址"""

    location_type: Optional[str] = None
    """Excel/CSV 文件位置"""

    location_url: Optional[str] = None
    """Excel/CSV 文件下载地址"""

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


class Datasource(BaseModel):
    id: str
    """数据源 ID"""

    created_at: datetime
    """创建时间"""

    engine: Literal["mysql", "tidb", "postgresql", "oceanbase", "clickhouse", "csv", "excel", "starrocks"]
    """数据源引擎"""

    meta_status: Literal["processing", "failed", "success", "unprocessed"]
    """元数据处理状态"""

    modified_at: datetime
    """修改时间"""

    project_id: str
    """项目 ID"""

    access_config: Optional[DatasourceAccessConfig] = None
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


class IntegrationExcelCsvAskResponse(BaseModel):
    answer: Answer

    datasource: Datasource
