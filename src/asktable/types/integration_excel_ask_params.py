# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["IntegrationExcelAskParams"]


class IntegrationExcelAskParams(TypedDict, total=False):
    excel_file_url: Required[str]
    """Excel 文件 URL"""

    question: Required[str]
    """查询语句"""
