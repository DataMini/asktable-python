# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ChatRetrieveResponse"]


class ChatRetrieveResponse(BaseModel):
    id: str
    """对话 ID"""

    created_at: datetime
    """创建时间"""

    modified_at: datetime
    """修改时间"""

    project_id: str

    status: Literal["active", "pending", "warning", "error"]

    bot_id: Optional[str] = None
    """
    AI 数据助手 ID，如果需要使用高级功能，请使用 bot_id 来创建对话。在 AI 数据助手中
    你可以定义可以访问的数据、可以执行的任务以及是否开启调试模式等设置。
    """

    datasource_ids: Optional[List[str]] = None

    error_detail: Optional[Dict[str, object]] = None

    name: Optional[str] = None
    """New name for the chat"""

    role_id: Optional[str] = None
    """
    角色 ID，将扮演这个角色来执行对话，用于权限控制。若无，则跳过鉴权，即可查询所有
    数据
    """

    role_name: Optional[str] = None
    """角色名称"""

    role_variables: Optional[Dict[str, Union[str, int, bool]]] = None
    """在扮演这个角色时需要传递的变量值，用 Key-Value 形式传递"""

    sample_questions: Optional[List[str]] = None

    user_profile: Optional[Dict[str, Union[str, int, bool]]] = None
    """用户信息，用于在对话中传递用户的信息，用 Key-Value 形式传递"""

    welcome_message: Optional[str] = None
