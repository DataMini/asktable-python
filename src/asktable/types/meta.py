# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["Meta", "Schemas", "SchemasTables", "SchemasTablesFields"]


class SchemasTablesFields(BaseModel):
    created_at: datetime
    """created time"""

    curr_desc_stat: str
    """current field description status"""

    full_name: str
    """field full name"""

    modified_at: datetime
    """modified time"""

    name: str
    """field_name"""

    curr_desc: Optional[str] = None
    """current field description"""

    data_type: Optional[str] = None
    """field data type"""

    origin_desc: Optional[str] = None
    """field description from database"""

    sample_data: Optional[str] = None
    """field sample data"""


class SchemasTables(BaseModel):
    curr_desc_stat: str
    """current table description status"""

    full_name: str
    """field full name"""

    name: str
    """table_name"""

    curr_desc: Optional[str] = None
    """current table description"""

    fields: Optional[Dict[str, SchemasTablesFields]] = None

    origin_desc: Optional[str] = None
    """table description from database"""


class Schemas(BaseModel):
    curr_desc_stat: str
    """current schema description status"""

    name: str
    """schema_name"""

    curr_desc: Optional[str] = None
    """current schema description"""

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
