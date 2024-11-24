# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Required, TypeAlias, TypedDict

__all__ = [
    "MetaCreateParams",
    "MetaCreate",
    "MetaCreateSchemas",
    "MetaCreateSchemasTables",
    "MetaCreateSchemasTablesFields",
    "Variant1",
]


class MetaCreate(TypedDict, total=False):
    name: Required[str]
    """metadata_name"""

    async_process_meta: bool

    value_index: bool

    schemas: Dict[str, MetaCreateSchemas]


class MetaCreateSchemasTablesFields(TypedDict, total=False):
    name: Required[str]
    """field_name"""

    data_type: Optional[str]
    """field data type"""

    origin_desc: Optional[str]
    """field description from database"""

    sample_data: Optional[str]
    """field sample data"""


class MetaCreateSchemasTables(TypedDict, total=False):
    name: Required[str]
    """table_name"""

    fields: Dict[str, MetaCreateSchemasTablesFields]

    origin_desc: Optional[str]
    """table description from database"""


class MetaCreateSchemas(TypedDict, total=False):
    name: Required[str]
    """schema_name"""

    custom_configs: Optional[object]
    """custom configs"""

    origin_desc: Optional[str]
    """schema description from database"""

    tables: Dict[str, MetaCreateSchemasTables]


class Variant1(TypedDict, total=False):
    body: Required[None]

    async_process_meta: bool

    value_index: bool


MetaCreateParams: TypeAlias = Union[MetaCreate, Variant1]
