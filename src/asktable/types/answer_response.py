# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["AnswerResponse"]


class AnswerResponse(BaseModel):
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
