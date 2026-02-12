# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = [
    "ProjectRetrieveModelGroupsResponse",
    "ProjectRetrieveModelGroupsResponseItem",
    "ProjectRetrieveModelGroupsResponseItemModels",
]


class ProjectRetrieveModelGroupsResponseItemModels(BaseModel):
    """角色→模型映射"""

    agent: Optional[str] = None

    canvas: Optional[str] = None

    fast: Optional[str] = None

    image: Optional[str] = None

    omni: Optional[str] = None

    report: Optional[str] = None

    sql: Optional[str] = None


class ProjectRetrieveModelGroupsResponseItem(BaseModel):
    id: str
    """模型组 ID"""

    api_key: str
    """API 密钥"""

    available_models: List[str]
    """可用模型列表"""

    base_url: str
    """OpenAI 兼容 API 端点"""

    created_at: datetime
    """创建时间"""

    extra_headers: Dict[str, str]
    """额外请求头"""

    models: ProjectRetrieveModelGroupsResponseItemModels
    """角色 → 模型映射"""

    modified_at: datetime
    """修改时间"""

    name: str
    """模型组名称"""

    display_name: Optional[str] = None
    """展示名称"""

    is_default: Optional[bool] = None
    """是否为默认组"""


ProjectRetrieveModelGroupsResponse: TypeAlias = List[ProjectRetrieveModelGroupsResponseItem]
