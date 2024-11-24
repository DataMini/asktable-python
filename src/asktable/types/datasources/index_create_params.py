# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["IndexCreateParams"]


class IndexCreateParams(TypedDict, total=False):
    field_name: Required[str]
    """字段名"""

    schema_name: Required[str]
    """模式名称"""

    table_name: Required[str]
    """表名"""

    async_process: bool
