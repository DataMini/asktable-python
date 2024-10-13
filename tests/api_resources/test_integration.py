# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from asktable import Asktable, AsyncAsktable
from tests.utils import assert_matches_type
from asktable.types import AnswerDataSourceOut

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIntegration:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_excel_csv_ask(self, client: Asktable) -> None:
        integration = client.integration.excel_csv_ask(
            file_url="file_url",
            question="question",
        )
        assert_matches_type(AnswerDataSourceOut, integration, path=["response"])

    @parametrize
    def test_method_excel_csv_ask_with_all_params(self, client: Asktable) -> None:
        integration = client.integration.excel_csv_ask(
            file_url="file_url",
            question="question",
            with_json=True,
        )
        assert_matches_type(AnswerDataSourceOut, integration, path=["response"])

    @parametrize
    def test_raw_response_excel_csv_ask(self, client: Asktable) -> None:
        response = client.integration.with_raw_response.excel_csv_ask(
            file_url="file_url",
            question="question",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = response.parse()
        assert_matches_type(AnswerDataSourceOut, integration, path=["response"])

    @parametrize
    def test_streaming_response_excel_csv_ask(self, client: Asktable) -> None:
        with client.integration.with_streaming_response.excel_csv_ask(
            file_url="file_url",
            question="question",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = response.parse()
            assert_matches_type(AnswerDataSourceOut, integration, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncIntegration:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_excel_csv_ask(self, async_client: AsyncAsktable) -> None:
        integration = await async_client.integration.excel_csv_ask(
            file_url="file_url",
            question="question",
        )
        assert_matches_type(AnswerDataSourceOut, integration, path=["response"])

    @parametrize
    async def test_method_excel_csv_ask_with_all_params(self, async_client: AsyncAsktable) -> None:
        integration = await async_client.integration.excel_csv_ask(
            file_url="file_url",
            question="question",
            with_json=True,
        )
        assert_matches_type(AnswerDataSourceOut, integration, path=["response"])

    @parametrize
    async def test_raw_response_excel_csv_ask(self, async_client: AsyncAsktable) -> None:
        response = await async_client.integration.with_raw_response.excel_csv_ask(
            file_url="file_url",
            question="question",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = await response.parse()
        assert_matches_type(AnswerDataSourceOut, integration, path=["response"])

    @parametrize
    async def test_streaming_response_excel_csv_ask(self, async_client: AsyncAsktable) -> None:
        async with async_client.integration.with_streaming_response.excel_csv_ask(
            file_url="file_url",
            question="question",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = await response.parse()
            assert_matches_type(AnswerDataSourceOut, integration, path=["response"])

        assert cast(Any, response.is_closed) is True
