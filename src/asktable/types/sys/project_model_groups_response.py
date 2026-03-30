# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "ProjectModelGroupsResponse",
    "ProjectModelGroupsResponseItem",
    "ProjectModelGroupsResponseItemModels",
    "ProjectModelGroupsResponseItemModelConfigs",
]


class ProjectModelGroupsResponseItemModels(BaseModel):
    """角色→模型映射"""

    agent: Optional[str] = None

    canvas: Optional[str] = None

    fast: Optional[str] = None

    image: Optional[str] = None

    omni: Optional[str] = None

    report: Optional[str] = None

    sql: Optional[str] = None


class ProjectModelGroupsResponseItemModelConfigs(BaseModel):
    """Per-model 配置，key 为 model ID"""

    capabilities: Optional[Dict[str, object]] = None

    context_window: Optional[int] = None

    display_name: Optional[str] = None

    enabled: Optional[bool] = None

    provider_options: Optional[Dict[str, object]] = None


class ProjectModelGroupsResponseItem(BaseModel):
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

    models: ProjectModelGroupsResponseItemModels
    """角色 → 模型映射"""

    modified_at: datetime
    """修改时间"""

    name: str
    """模型组名称"""

    api_format: Optional[Literal["openai_chat", "anthropic"]] = None
    """API 协议格式"""

    display_name: Optional[str] = None
    """展示名称"""

    is_default: Optional[bool] = None
    """是否为默认组"""

    api_model_configs: Optional[Dict[str, ProjectModelGroupsResponseItemModelConfigs]] = FieldInfo(
        alias="model_configs", default=None
    )
    """Per-model 配置"""


ProjectModelGroupsResponse: TypeAlias = List[ProjectModelGroupsResponseItem]
