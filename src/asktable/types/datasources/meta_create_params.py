# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr

__all__ = [
    "MetaCreateParams",
    "Meta",
    "MetaSchemas",
    "MetaSchemasTables",
    "MetaSchemasTablesFields",
    "MetaSchemasTablesForeignKey",
]


class MetaCreateParams(TypedDict, total=False):
    async_process_meta: bool

    value_index: bool

    meta: Optional[Meta]

    selected_tables: Optional[Dict[str, SequenceNotStr[str]]]


class MetaSchemasTablesFields(TypedDict, total=False):
    name: Required[str]
    """field_name"""

    origin_desc: Required[str]
    """field description from database"""

    data_type: Optional[str]
    """field data type"""

    identifiable_type: Literal["plain", "person_name", "email", "ssn", "id", "phone", "address", "company", "bank_card"]
    """identifiable type"""

    is_nullable: Optional[bool]
    """column nullability"""

    raw_data_type: Optional[str]
    """original DDL type string"""

    sample_data: Optional[str]
    """field sample data"""

    visibility: bool
    """field visibility"""


class MetaSchemasTablesForeignKey(TypedDict, total=False):
    constrained_columns: Required[SequenceNotStr[str]]
    """FK columns on this table"""

    referred_columns: Required[SequenceNotStr[str]]
    """referred columns"""

    referred_table: Required[str]
    """referred table name"""

    referred_schema: Optional[str]
    """referred schema name"""


class MetaSchemasTables(TypedDict, total=False):
    name: Required[str]
    """table_name"""

    origin_desc: Required[str]
    """table description from database"""

    fields: Dict[str, MetaSchemasTablesFields]

    foreign_keys: Iterable[MetaSchemasTablesForeignKey]
    """foreign key constraints"""

    primary_key: SequenceNotStr[str]
    """primary key columns"""

    table_type: Literal["table", "view"]
    """table type"""


class MetaSchemas(TypedDict, total=False):
    name: Required[str]
    """schema_name"""

    origin_desc: Required[str]
    """schema description from database"""

    custom_configs: Optional[Dict[str, object]]
    """custom configs"""

    tables: Dict[str, MetaSchemasTables]


class Meta(TypedDict, total=False):
    schemas: Required[Dict[str, MetaSchemas]]
