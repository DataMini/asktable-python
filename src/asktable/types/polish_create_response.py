# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from .._models import BaseModel

__all__ = ["PolishCreateResponse"]


class PolishCreateResponse(BaseModel):
    polish_desc: str
    """润色后的结果"""
