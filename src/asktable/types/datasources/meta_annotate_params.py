# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

__all__ = ["MetaAnnotateParams", "Schemas", "SchemasTables"]


class MetaAnnotateParams(TypedDict, total=False):
    schemas: Required[Dict[str, Schemas]]


class SchemasTables(TypedDict, total=False):
    fields: Required[Dict[str, str]]

    desc: Optional[str]


class Schemas(TypedDict, total=False):
    tables: Required[Dict[str, SchemasTables]]

    desc: Optional[str]
