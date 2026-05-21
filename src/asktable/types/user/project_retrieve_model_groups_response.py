# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["ProjectRetrieveModelGroupsResponse", "ProjectRetrieveModelGroupsResponseItem"]


class ProjectRetrieveModelGroupsResponseItem(BaseModel):
    """
    项目级用户视角，仅暴露选择器需要的字段。
    敏感配置（api_key/base_url/extra_headers/model_configs）由系统级端点处理。
    """

    id: str
    """模型组 ID"""

    name: str
    """模型组名称（绑定 project.llm_model_group）"""

    display_name: Optional[str] = None
    """展示名称"""

    is_default: Optional[bool] = None
    """是否为系统默认组"""


ProjectRetrieveModelGroupsResponse: TypeAlias = List[ProjectRetrieveModelGroupsResponseItem]
