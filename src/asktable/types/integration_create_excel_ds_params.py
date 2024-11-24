# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["IntegrationCreateExcelDsParams"]


class IntegrationCreateExcelDsParams(TypedDict, total=False):
    file_url: Required[str]

    value_index: bool
