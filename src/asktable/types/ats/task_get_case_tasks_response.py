# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["TaskGetCaseTasksResponse", "Item"]


class Item(BaseModel):
    id: str
    """测试用例运行记录 ID"""

    ats_task_id: str
    """对应的测试任务 ID"""

    created_at: datetime
    """创建时间"""

    expected_sql: str
    """sql 答案"""

    modified_at: datetime
    """修改时间"""

    question: str
    """提问内容"""

    status: str
    """测试状态"""

    atc_id: Optional[str] = None
    """对应的测试用例 ID"""

    duration: Optional[float] = None
    """测试用例执行时间,单位为秒"""

    expected_query_result: Union[List[object], object, None] = None
    """预期查询出来的数据"""

    generated_sql: Optional[str] = None
    """生成的 sql"""

    generated_sql_query_result: Union[List[object], object, None] = None
    """测试样本生成的 sql 查询结果"""

    last_run: Optional[datetime] = None
    """上次该测试样例运行时间"""

    role_id: Optional[str] = None
    """角色 ID"""

    role_variables: Optional[object] = None
    """扮演角色需要传递的值"""

    status_message: Optional[str] = None
    """测试日志保存字段"""

    task_id: Optional[str] = None
    """测试调用接口对应任务的 id"""


class TaskGetCaseTasksResponse(BaseModel):
    items: List[Item]

    page: Optional[int] = None

    size: Optional[int] = None

    total: Optional[int] = None

    pages: Optional[int] = None
