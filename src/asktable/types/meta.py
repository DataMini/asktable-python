# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Meta", "Schemas", "SchemasTables", "SchemasTablesFields"]


class SchemasTablesFields(BaseModel):
    created_at: datetime
    """created time"""

    curr_desc: str
    """current field description"""

    curr_desc_stat: str
    """current field description status"""

    full_name: str
    """field full name"""

    modified_at: datetime
    """modified time"""

    name: str
    """field_name"""

    origin_desc: str
    """field description from database"""

    data_type: Optional[str] = None
    """field data type"""

    identifiable_type: Optional[
        Literal["plain", "person_name", "email", "ssn", "id", "phone", "address", "company"]
    ] = None
    """identifiable type"""

    sample_data: Optional[str] = None
    """field sample data"""

    visibility: Optional[bool] = None
    """field visibility"""


class SchemasTables(BaseModel):
    curr_desc: str
    """current table description"""

    curr_desc_stat: str
    """current table description status"""

    fields: Dict[str, SchemasTablesFields]

    full_name: str
    """field full name"""

    name: str
    """table_name"""

    origin_desc: str
    """table description from database"""

    table_type: Optional[Literal["table", "view"]] = None
    """table type"""


class Schemas(BaseModel):
    curr_desc: str
    """current schema description"""

    curr_desc_stat: str
    """current schema description status"""

    name: str
    """schema_name"""

    origin_desc: str
    """schema description from database"""

    tables: Dict[str, SchemasTables]

    custom_configs: Optional[object] = None
    """custom configs"""


class Meta(BaseModel):
    datasource_id: str
    """datasource_id"""

    schemas: Dict[str, Schemas]
