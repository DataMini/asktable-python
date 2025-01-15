# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["QueryResponse", "Query", "Request"]


class Query(BaseModel):
    sql: str
    """SQL 语句"""


class Request(BaseModel):
    datasource_id: str
    """数据源 ID"""

    question: str
    """查询语句"""

    role_id: Optional[str] = None
    """
    角色 ID，将扮演这个角色来执行对话，用于权限控制。若无，则跳过鉴权，即可查询所有
    数据
    """

    role_variables: Optional[object] = None
    """在扮演这个角色时需要传递的变量值，用 Key-Value 形式传递"""


class QueryResponse(BaseModel):
    id: str

    created_at: datetime

    duration: int

    modified_at: datetime

    project_id: str

    query: Optional[Query] = None

    request: Request

    status: str

    err_msg: Optional[str] = None

    trace_id: Optional[str] = None
