# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["ModelGroup"]


class ModelGroup(BaseModel):
    image_models: List[str]
    """图像模型列表"""

    name: str
    """模型组名称"""

    text_models: List[str]
    """文本模型列表"""
