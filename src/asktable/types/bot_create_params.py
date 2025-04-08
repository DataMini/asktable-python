# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Required, TypedDict

__all__ = ["BotCreateParams"]


class BotCreateParams(TypedDict, total=False):
    datasource_ids: Required[List[str]]
    """数据源 ID，目前只支持 1 个数据源。"""

    name: Required[str]
    """名称，不超过 64 个字符"""

    color_theme: Optional[str]
    """颜色主题"""

    debug: bool
    """调试模式"""

    extapi_ids: List[str]
    """扩展 API ID 列表，扩展 API ID 的逗号分隔列表。"""

    magic_input: Optional[str]
    """魔法提示词"""

    max_rows: int
    """最大返回行数，默认不限制"""

    publish: bool
    """是否公开"""

    query_balance: Optional[int]
    """bot 的查询次数，默认是 None，表示无限次查询，入参为大于等于 0 的整数"""

    sample_questions: Optional[List[str]]
    """示例问题列表"""

    webhooks: List[str]
    """Webhook URL 列表"""

    welcome_message: Optional[str]
    """欢迎消息"""
