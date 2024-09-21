# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["APIKey"]


class APIKey(BaseModel):
    id: str

    ak_role: Literal["sys", "admin", "asker"]
    """API key 的角色"""

    created_at: str

    hashed_ak_value: str

    last_used_at: str

    masked_ak_value: str

    original_ak_value: str

    project_id: str

    status: int
