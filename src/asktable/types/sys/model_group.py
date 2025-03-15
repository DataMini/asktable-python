# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from ..._models import BaseModel

__all__ = ["ModelGroup"]


class ModelGroup(BaseModel):
    id: str
    """模型组 ID"""

    agent: str
    """Agent 模型"""

    fast: str
    """快速模型"""

    image: str
    """图片模型"""

    name: str
    """模型组名称"""

    omni: str
    """通用模型"""

    sql: str
    """SQL 模型"""
