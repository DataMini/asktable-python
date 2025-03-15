# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["PolishCreateParams"]


class PolishCreateParams(TypedDict, total=False):
    max_word_count: Required[int]
    """润色后的最大字数，注意：该值不是绝对值，实际优化后的字数可能会超过该值"""

    user_desc: Required[str]
    """需要润色的用户输入"""

    polish_mode: Literal[0]
    """润色模式，默认是简化模式"""
