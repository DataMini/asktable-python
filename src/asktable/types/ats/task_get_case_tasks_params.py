# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TaskGetCaseTasksParams"]


class TaskGetCaseTasksParams(TypedDict, total=False):
    ats_id: Required[str]

    page: int
    """Page number"""

    size: int
    """Page size"""
