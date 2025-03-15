# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["DatasourceUpdateFieldParams"]


class DatasourceUpdateFieldParams(TypedDict, total=False):
    field_name: Required[str]

    schema_name: Required[str]

    table_name: Required[str]

    visibility: Optional[bool]
    """field visibility"""
