# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["Chatbot"]


class Chatbot(BaseModel):
    id: str

    created_at: datetime

    datasource_ids: List[str]
    """数据源 ID，目前只支持 1 个数据源。"""

    modified_at: datetime

    name: str
    """名称，不超过 64 个字符"""

    project_id: str

    avatar_url: Optional[str] = None
    """头像 URL"""

    color_theme: Optional[str] = None
    """颜色主题"""

    debug: Optional[bool] = None
    """调试模式"""

    extapi_ids: Optional[List[str]] = None
    """扩展 API ID 列表，扩展 API ID 的逗号分隔列表。"""

    magic_input: Optional[str] = None
    """魔法提示词"""

    max_rows: Optional[int] = None
    """最大返回行数，默认不限制"""

    publish: Optional[bool] = None
    """是否公开"""

    sample_questions: Optional[List[str]] = None
    """示例问题列表"""

    welcome_message: Optional[str] = None
    """欢迎消息"""
