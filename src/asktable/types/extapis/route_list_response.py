# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .ext_api_route_model import ExtAPIRouteModel

__all__ = ["RouteListResponse"]

RouteListResponse: TypeAlias = List[ExtAPIRouteModel]
