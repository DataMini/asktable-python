# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["MetaUpdateParams", "Schemas", "SchemasTables", "SchemasTablesFields"]


class MetaUpdateParams(TypedDict, total=False):
    path_datasource_id: Required[Annotated[str, PropertyInfo(alias="datasource_id")]]

    body_datasource_id: Required[Annotated[str, PropertyInfo(alias="datasource_id")]]
    """datasource_id"""

    name: Required[str]
    """metadata_name"""

    schemas: Dict[str, Schemas]


class SchemasTablesFields(TypedDict, total=False):
    curr_desc: Required[str]
    """current field description"""

    curr_desc_stat: Required[str]
    """current field description status"""

    full_name: Required[str]
    """field full name"""

    name: Required[str]
    """field_name"""

    data_type: Optional[str]
    """field data type"""

    origin_desc: Optional[str]
    """field description from database"""

    sample_data: Optional[str]
    """field sample data"""


class SchemasTables(TypedDict, total=False):
    curr_desc: Required[str]
    """current table description"""

    curr_desc_stat: Required[str]
    """current table description status"""

    full_name: Required[str]
    """field full name"""

    name: Required[str]
    """table_name"""

    fields: Dict[str, SchemasTablesFields]

    origin_desc: Optional[str]
    """table description from database"""


class Schemas(TypedDict, total=False):
    curr_desc: Required[str]
    """current schema description"""

    curr_desc_stat: Required[str]
    """current schema description status"""

    name: Required[str]
    """schema_name"""

    custom_configs: Optional[object]
    """custom configs"""

    origin_desc: Optional[str]
    """schema description from database"""

    tables: Dict[str, SchemasTables]
