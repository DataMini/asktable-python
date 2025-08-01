# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["TestCaseListParams"]


class TestCaseListParams(TypedDict, total=False):
    page: int
    """Page number"""

    size: int
    """Page size"""
