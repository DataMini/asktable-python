# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from asktable import Asktable, AsyncAsktable
from tests.utils import assert_matches_type
from asktable.pagination import SyncPage, AsyncPage
from asktable.types.single_turn import Q2aResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestQ2a:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Asktable) -> None:
        q2a = client.single_turn.q2a.create(
            datasource_id="datasource_id",
            question="xxx",
        )
        assert_matches_type(Q2aResponse, q2a, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Asktable) -> None:
        q2a = client.single_turn.q2a.create(
            datasource_id="datasource_id",
            question="xxx",
            max_rows=0,
            role_id="role_id",
            role_variables={},
            with_json=True,
        )
        assert_matches_type(Q2aResponse, q2a, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Asktable) -> None:
        response = client.single_turn.q2a.with_raw_response.create(
            datasource_id="datasource_id",
            question="xxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        q2a = response.parse()
        assert_matches_type(Q2aResponse, q2a, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Asktable) -> None:
        with client.single_turn.q2a.with_streaming_response.create(
            datasource_id="datasource_id",
            question="xxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            q2a = response.parse()
            assert_matches_type(Q2aResponse, q2a, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Asktable) -> None:
        q2a = client.single_turn.q2a.list()
        assert_matches_type(SyncPage[Q2aResponse], q2a, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Asktable) -> None:
        q2a = client.single_turn.q2a.list(
            datasource_id="datasource_id",
            page=1,
            size=1,
        )
        assert_matches_type(SyncPage[Q2aResponse], q2a, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Asktable) -> None:
        response = client.single_turn.q2a.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        q2a = response.parse()
        assert_matches_type(SyncPage[Q2aResponse], q2a, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Asktable) -> None:
        with client.single_turn.q2a.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            q2a = response.parse()
            assert_matches_type(SyncPage[Q2aResponse], q2a, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncQ2a:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncAsktable) -> None:
        q2a = await async_client.single_turn.q2a.create(
            datasource_id="datasource_id",
            question="xxx",
        )
        assert_matches_type(Q2aResponse, q2a, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncAsktable) -> None:
        q2a = await async_client.single_turn.q2a.create(
            datasource_id="datasource_id",
            question="xxx",
            max_rows=0,
            role_id="role_id",
            role_variables={},
            with_json=True,
        )
        assert_matches_type(Q2aResponse, q2a, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncAsktable) -> None:
        response = await async_client.single_turn.q2a.with_raw_response.create(
            datasource_id="datasource_id",
            question="xxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        q2a = await response.parse()
        assert_matches_type(Q2aResponse, q2a, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncAsktable) -> None:
        async with async_client.single_turn.q2a.with_streaming_response.create(
            datasource_id="datasource_id",
            question="xxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            q2a = await response.parse()
            assert_matches_type(Q2aResponse, q2a, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncAsktable) -> None:
        q2a = await async_client.single_turn.q2a.list()
        assert_matches_type(AsyncPage[Q2aResponse], q2a, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncAsktable) -> None:
        q2a = await async_client.single_turn.q2a.list(
            datasource_id="datasource_id",
            page=1,
            size=1,
        )
        assert_matches_type(AsyncPage[Q2aResponse], q2a, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncAsktable) -> None:
        response = await async_client.single_turn.q2a.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        q2a = await response.parse()
        assert_matches_type(AsyncPage[Q2aResponse], q2a, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncAsktable) -> None:
        async with async_client.single_turn.q2a.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            q2a = await response.parse()
            assert_matches_type(AsyncPage[Q2aResponse], q2a, path=["response"])

        assert cast(Any, response.is_closed) is True
