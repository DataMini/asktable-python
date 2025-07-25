# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["ProjectUpdateMyProjectParams"]


class ProjectUpdateMyProjectParams(TypedDict, total=False):
    llm_model_group: Optional[str]
    """模型组"""

    name: Optional[str]
    """项目名称"""
