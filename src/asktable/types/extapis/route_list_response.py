# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .extapi_route import ExtapiRoute

__all__ = ["RouteListResponse"]

RouteListResponse: TypeAlias = List[ExtapiRoute]
