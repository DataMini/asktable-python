# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Meta", "Schemas", "SchemasTables", "SchemasTablesFields", "SchemasTablesFieldsIndex"]


class SchemasTablesFieldsIndex(BaseModel):
    """索引信息"""

    id: str
    """索引 ID"""

    distinct_count: Optional[int] = None
    """不同值数量"""

    index_value_count: Optional[int] = None
    """索引值总数"""

    status_msg: Optional[str] = None
    """状态信息，为空表示成功"""

    value_count: Optional[int] = None
    """值总数"""


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

    avg_length: Optional[float] = None
    """sample average text length"""

    data_type: Optional[str] = None
    """field data type"""

    distinct_count: Optional[int] = None
    """sample distinct count"""

    identifiable_type: Optional[
        Literal["plain", "person_name", "email", "ssn", "id", "phone", "address", "company", "bank_card"]
    ] = None
    """identifiable type"""

    index: Optional[SchemasTablesFieldsIndex] = None
    """索引信息"""

    is_nullable: Optional[bool] = None
    """column nullability"""

    max_value: Optional[str] = None
    """sample maximum or latest"""

    min_value: Optional[str] = None
    """sample minimum or earliest"""

    nil_pct: Optional[float] = None
    """sample null ratio"""

    raw_data_type: Optional[str] = None
    """original DDL type string"""

    sample_data: Optional[str] = None
    """field sample data"""

    semantic_type: Optional[
        Literal[
            "PK",
            "FK",
            "Quantity",
            "Share",
            "Percentage",
            "Currency",
            "Income",
            "Discount",
            "Price",
            "GrossMargin",
            "Cost",
            "Score",
            "Duration",
            "Latitude",
            "Longitude",
            "City",
            "State",
            "Country",
            "ZipCode",
            "Email",
            "URL",
            "ImageURL",
            "AvatarURL",
            "Category",
            "Enum",
            "Name",
            "Title",
            "Description",
            "Comment",
            "SerializedJSON",
            "IPAddress",
            "CreationTimestamp",
            "CreationTime",
            "CreationDate",
            "JoinTimestamp",
            "JoinTime",
            "JoinDate",
            "CancelationTimestamp",
            "CancelationTime",
            "CancelationDate",
            "DeletionTimestamp",
            "DeletionTime",
            "DeletionDate",
            "UpdatedTimestamp",
            "UpdatedTime",
            "UpdatedDate",
            "Birthdate",
            "Source",
            "Author",
            "Owner",
            "Company",
            "Product",
            "Subscription",
        ]
    ] = None
    """字段语义类型，协议照抄 Metabase（值 = :type/ 前缀去除后的名字）。

    PK/FK 是关系类型，与语义共用一列（Metabase 同款）：来自同步元数据，非推断产物
    ，classifier 一律跳过。其余值由 classifier 推断或人工设置。
    """

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

    profiled_at: Optional[datetime] = None
    """last profiling time"""

    row_count: Optional[int] = None
    """sampled row count"""

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

    custom_configs: Optional[Dict[str, object]] = None
    """custom configs"""


class Meta(BaseModel):
    datasource_id: str
    """datasource_id"""

    schemas: Dict[str, Schemas]
