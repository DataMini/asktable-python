# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = [
    "ProjectListModelGroupsResponse",
    "ProjectListModelGroupsResponseItem",
    "ProjectListModelGroupsResponseItemModels",
]


class ProjectListModelGroupsResponseItemModels(BaseModel):
    """角色→模型映射"""

    agent: Optional[str] = None

    canvas: Optional[str] = None

    fast: Optional[str] = None

    image: Optional[str] = None

    omni: Optional[str] = None

    report: Optional[str] = None

    sql: Optional[str] = None


class ProjectListModelGroupsResponseItem(BaseModel):
    id: str
    """模型组 ID"""

    api_key: str
    """解密后的 API 密钥"""

    available_models: List[str]
    """可用模型列表"""

    base_url: str
    """OpenAI 兼容 API 端点"""

    created_at: datetime
    """创建时间"""

    models: ProjectListModelGroupsResponseItemModels
    """角色 → 模型映射"""

    modified_at: datetime
    """修改时间"""

    name: str
    """模型组名称"""


ProjectListModelGroupsResponse: TypeAlias = List[ProjectListModelGroupsResponseItem]
