# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from ..._models import BaseModel

__all__ = ["Meta", "Schemas", "SchemasTables", "SchemasTablesFields"]


class SchemasTablesFields(BaseModel):
    curr_desc: str
    """current field description"""

    curr_desc_stat: str
    """current field description status"""

    full_name: str
    """field full name"""

    name: str
    """field_name"""

    data_type: Optional[str] = None
    """field data type"""

    origin_desc: Optional[str] = None
    """field description from database"""

    sample_data: Optional[str] = None
    """field sample data"""


class SchemasTables(BaseModel):
    curr_desc: str
    """current table description"""

    curr_desc_stat: str
    """current table description status"""

    full_name: str
    """field full name"""

    name: str
    """table_name"""

    fields: Optional[Dict[str, SchemasTablesFields]] = None

    origin_desc: Optional[str] = None
    """table description from database"""


class Schemas(BaseModel):
    curr_desc: str
    """current schema description"""

    curr_desc_stat: str
    """current schema description status"""

    name: str
    """schema_name"""

    custom_configs: Optional[object] = None
    """custom configs"""

    origin_desc: Optional[str] = None
    """schema description from database"""

    tables: Optional[Dict[str, SchemasTables]] = None


class Meta(BaseModel):
    datasource_id: str
    """datasource_id"""

    name: str
    """metadata_name"""

    schemas: Optional[Dict[str, Schemas]] = None
