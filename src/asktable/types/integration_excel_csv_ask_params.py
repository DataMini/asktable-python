# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["IntegrationExcelCsvAskParams"]


class IntegrationExcelCsvAskParams(TypedDict, total=False):
    file_url: Required[str]
    """文件 URL(支持 Excel/CSV)"""

    question: Required[str]
    """用户问题"""

    with_json: Optional[bool]
    """是否将数据作为 json 附件返回"""
