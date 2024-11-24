# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Policy", "DatasetConfig", "DatasetConfigRegexPatterns"]


class DatasetConfigRegexPatterns(BaseModel):
    fields_regex_pattern: Optional[str] = None
    """Field 正则表达式，空值默认全选"""

    schemas_regex_pattern: Optional[str] = None
    """Schema 正则表达式，空值默认全选"""

    tables_regex_pattern: Optional[str] = None
    """Table 正则表达式，空值默认全选"""


class DatasetConfig(BaseModel):
    datasource_ids: List[str]
    """
    数据源 ID 列表，必填。 - 描述：用于指定策略适用的数据源。可以使用通配符 _ 表示所
    有数据源。 - 示例：["ds_id_1","ds_id_2"]，["_"]。
    """

    regex_patterns: Optional[DatasetConfigRegexPatterns] = None
    """
    正则表达式。 - 描述：用于匹配指定数据源中 Schema（DB）、Table 和 Field 名称的三
    个正则表达式，即同时满足这三个正则表达式的 DB、Table 和 Field 才被允许访问。 -
    注意：此字段为可选项。如果未提供，则默认包含指定数据源的所有数据。
    """

    rows_filters: Optional[Dict[str, List[str]]] = None
    """行过滤器"""


class Policy(BaseModel):
    id: str

    created_at: datetime

    dataset_config: DatasetConfig

    description: Optional[str] = None

    modified_at: datetime

    name: str
    """名称，小写英文字母，数字和下划线组合，不超过 64 个字符"""

    permission: Literal["allow", "deny"]
    """权限"""

    project_id: str
