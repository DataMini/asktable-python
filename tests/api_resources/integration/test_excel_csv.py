# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from asktable import Asktable, AsyncAsktable
from tests.utils import assert_matches_type
from asktable.types import DataSource

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExcelCsv:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Asktable) -> None:
        excel_csv = client.integration.excel_csv.create(
            file_url="file_url",
        )
        assert_matches_type(DataSource, excel_csv, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Asktable) -> None:
        response = client.integration.excel_csv.with_raw_response.create(
            file_url="file_url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        excel_csv = response.parse()
        assert_matches_type(DataSource, excel_csv, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Asktable) -> None:
        with client.integration.excel_csv.with_streaming_response.create(
            file_url="file_url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            excel_csv = response.parse()
            assert_matches_type(DataSource, excel_csv, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncExcelCsv:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncAsktable) -> None:
        excel_csv = await async_client.integration.excel_csv.create(
            file_url="file_url",
        )
        assert_matches_type(DataSource, excel_csv, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncAsktable) -> None:
        response = await async_client.integration.excel_csv.with_raw_response.create(
            file_url="file_url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        excel_csv = await response.parse()
        assert_matches_type(DataSource, excel_csv, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncAsktable) -> None:
        async with async_client.integration.excel_csv.with_streaming_response.create(
            file_url="file_url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            excel_csv = await response.parse()
            assert_matches_type(DataSource, excel_csv, path=["response"])

        assert cast(Any, response.is_closed) is True
