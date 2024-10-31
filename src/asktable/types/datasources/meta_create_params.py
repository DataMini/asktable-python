# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Required, TypeAlias, TypedDict

__all__ = [
    "MetaCreateParams",
    "MetaBase",
    "MetaBaseSchemas",
    "MetaBaseSchemasTables",
    "MetaBaseSchemasTablesFields",
    "Variant1",
]


class MetaBase(TypedDict, total=False):
    name: Required[str]
    """metadata_name"""

    schemas: Dict[str, MetaBaseSchemas]


class MetaBaseSchemasTablesFields(TypedDict, total=False):
    name: Required[str]
    """field_name"""

    data_type: Optional[str]
    """field data type"""

    origin_desc: Optional[str]
    """field description from database"""

    sample_data: Optional[str]
    """field sample data"""


class MetaBaseSchemasTables(TypedDict, total=False):
    name: Required[str]
    """table_name"""

    fields: Dict[str, MetaBaseSchemasTablesFields]

    origin_desc: Optional[str]
    """table description from database"""


class MetaBaseSchemas(TypedDict, total=False):
    name: Required[str]
    """schema_name"""

    custom_configs: Optional[object]
    """custom configs"""

    origin_desc: Optional[str]
    """schema description from database"""

    tables: Dict[str, MetaBaseSchemasTables]


class Variant1(TypedDict, total=False):
    body: Required[None]


MetaCreateParams: TypeAlias = Union[MetaBase, Variant1]
