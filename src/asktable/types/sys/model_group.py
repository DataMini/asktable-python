# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["ModelGroup"]


class ModelGroup(BaseModel):
    id: str
    """模型组 ID"""

    agent_model: str
    """Agent 模型"""

    image_models: List[str]
    """图像模型列表"""

    name: str
    """模型组名称"""

    text_models: List[str]
    """文本模型列表"""
