# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AuthMeResponse"]


class AuthMeResponse(BaseModel):
    ak_role: Literal["sys", "admin", "asker"]

    project_id: str

    ak_id: Optional[str] = None

    chat_role: Optional[Dict[str, object]] = None

    exp: Optional[int] = None

    locked: Optional[bool] = None

    user_profile: Optional[Dict[str, object]] = None
