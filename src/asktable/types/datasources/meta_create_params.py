# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["MetaCreateParams", "Meta", "MetaSchemas", "MetaSchemasTables", "MetaSchemasTablesFields"]


class MetaCreateParams(TypedDict, total=False):
    async_process_meta: bool

    value_index: bool

    meta: Optional[Meta]

    selected_tables: Optional[Dict[str, List[str]]]


class MetaSchemasTablesFields(TypedDict, total=False):
    name: Required[str]
    """field_name"""

    origin_desc: Required[str]
    """field description from database"""

    data_type: Optional[str]
    """field data type"""

    identifiable_type: Literal["plain", "person_name", "email", "ssn", "id", "phone", "address", "company"]
    """identifiable type"""

    sample_data: Optional[str]
    """field sample data"""

    visibility: bool
    """field visibility"""


class MetaSchemasTables(TypedDict, total=False):
    name: Required[str]
    """table_name"""

    origin_desc: Required[str]
    """table description from database"""

    fields: Dict[str, MetaSchemasTablesFields]

    table_type: Literal["table", "view"]
    """table type"""


class MetaSchemas(TypedDict, total=False):
    name: Required[str]
    """schema_name"""

    origin_desc: Required[str]
    """schema description from database"""

    custom_configs: Optional[object]
    """custom configs"""

    tables: Dict[str, MetaSchemasTables]


class Meta(TypedDict, total=False):
    schemas: Required[Dict[str, MetaSchemas]]
