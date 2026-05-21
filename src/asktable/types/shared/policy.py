# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Policy", "Fields", "FieldsPattern", "RowFilter", "Schemas", "SchemasPattern", "Tables", "TablesPattern"]


class FieldsPattern(BaseModel):
    type: Literal["exact", "prefix", "suffix", "include"]

    value: str


class Fields(BaseModel):
    """Field 匹配规则"""

    combinator: Optional[Literal["and", "or"]] = None

    patterns: Optional[List[FieldsPattern]] = None


class RowFilter(BaseModel):
    """单条行过滤器。schema_name / table_name / field_name 允许 "*" 通配。"""

    datasource_id: str

    field_name: str

    operator: Literal[
        "=", "!=", "<>", ">", "<", ">=", "<=", "IN", "NOT IN", "LIKE", "NOT LIKE", "IS NULL", "IS NOT NULL"
    ]

    schema_name: str

    table_name: str

    value: Optional[str] = None


class SchemasPattern(BaseModel):
    type: Literal["exact", "prefix", "suffix", "include"]

    value: str


class Schemas(BaseModel):
    """Schema 匹配规则；空 patterns = 不过滤"""

    combinator: Optional[Literal["and", "or"]] = None

    patterns: Optional[List[SchemasPattern]] = None


class TablesPattern(BaseModel):
    type: Literal["exact", "prefix", "suffix", "include"]

    value: str


class Tables(BaseModel):
    """Table 匹配规则"""

    combinator: Optional[Literal["and", "or"]] = None

    patterns: Optional[List[TablesPattern]] = None


class Policy(BaseModel):
    id: str

    created_at: datetime

    modified_at: datetime

    name: str
    """名称"""

    permission: Literal["allow", "deny"]
    """权限"""

    project_id: str

    datasource_ids: Optional[List[str]] = None
    """数据源 ID 列表；允许为空（新建空白态）"""

    description: Optional[str] = None
    """描述"""

    fields: Optional[Fields] = None
    """Field 匹配规则"""

    row_filters: Optional[List[RowFilter]] = None
    """行过滤器（顶层扁平 list，每项带 datasource_id）"""

    schemas: Optional[Schemas] = None
    """Schema 匹配规则；空 patterns = 不过滤"""

    tables: Optional[Tables] = None
    """Table 匹配规则"""
