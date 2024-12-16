# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["PreferenceUpdateResponse"]


class PreferenceUpdateResponse(BaseModel):
    id: str
    """偏好设置 ID"""

    general_preference: str
    """通用偏好设置内容"""

    project_id: str
    """项目 ID"""

    sql_preference: Optional[str] = None
    """SQL 偏好设置内容"""
