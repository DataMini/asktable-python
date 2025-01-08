# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

from .._types import FileTypes

__all__ = ["DatasourceAddFilesParams"]


class DatasourceAddFilesParams(TypedDict, total=False):
    files: Required[List[FileTypes]]