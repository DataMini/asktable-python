# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import FileTypes

__all__ = ["DatasourceCreateFromFileParams"]


class DatasourceCreateFromFileParams(TypedDict, total=False):
    file: Required[FileTypes]

    async_process_meta: bool

    name: str

    value_index: bool
