# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["DatasourceUpdateFieldParams"]


class DatasourceUpdateFieldParams(TypedDict, total=False):
    field_name: Required[str]

    schema_name: Required[str]

    table_name: Required[str]

    identifiable_type: Optional[Literal["plain", "person_name", "email", "ssn", "id", "phone", "address", "company"]]
    """identifiable type"""

    visibility: Optional[bool]
    """field visibility"""
