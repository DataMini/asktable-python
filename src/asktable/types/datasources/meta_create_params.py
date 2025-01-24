# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

__all__ = ["MetaCreateParams", "Schemas", "SchemasTables", "SchemasTablesFields"]


class MetaCreateParams(TypedDict, total=False):
    async_process_meta: bool

    value_index: bool

    schemas: Dict[str, Schemas]


class SchemasTablesFields(TypedDict, total=False):
    name: Required[str]
    """field_name"""

    data_type: Optional[str]
    """field data type"""

    origin_desc: Optional[str]
    """field description from database"""

    sample_data: Optional[str]
    """field sample data"""


class SchemasTables(TypedDict, total=False):
    name: Required[str]
    """table_name"""

    fields: Dict[str, SchemasTablesFields]

    origin_desc: Optional[str]
    """table description from database"""


class Schemas(TypedDict, total=False):
    name: Required[str]
    """schema_name"""

    custom_configs: Optional[object]
    """custom configs"""

    origin_desc: Optional[str]
    """schema description from database"""

    tables: Dict[str, SchemasTables]
