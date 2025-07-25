# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from asktable import Asktable, AsyncAsktable
from tests.utils import assert_matches_type
from asktable.types import AuthMeResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAuth:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_token(self, client: Asktable) -> None:
        auth = client.auth.create_token()
        assert_matches_type(object, auth, path=["response"])

    @parametrize
    def test_method_create_token_with_all_params(self, client: Asktable) -> None:
        auth = client.auth.create_token(
            ak_role="asker",
            chat_role={
                "role_id": "1",
                "role_variables": {"id": "42"},
            },
            token_ttl=900,
            user_profile={"name": "张三"},
        )
        assert_matches_type(object, auth, path=["response"])

    @parametrize
    def test_raw_response_create_token(self, client: Asktable) -> None:
        response = client.auth.with_raw_response.create_token()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = response.parse()
        assert_matches_type(object, auth, path=["response"])

    @parametrize
    def test_streaming_response_create_token(self, client: Asktable) -> None:
        with client.auth.with_streaming_response.create_token() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = response.parse()
            assert_matches_type(object, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_me(self, client: Asktable) -> None:
        auth = client.auth.me()
        assert_matches_type(AuthMeResponse, auth, path=["response"])

    @parametrize
    def test_raw_response_me(self, client: Asktable) -> None:
        response = client.auth.with_raw_response.me()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = response.parse()
        assert_matches_type(AuthMeResponse, auth, path=["response"])

    @parametrize
    def test_streaming_response_me(self, client: Asktable) -> None:
        with client.auth.with_streaming_response.me() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = response.parse()
            assert_matches_type(AuthMeResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAuth:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create_token(self, async_client: AsyncAsktable) -> None:
        auth = await async_client.auth.create_token()
        assert_matches_type(object, auth, path=["response"])

    @parametrize
    async def test_method_create_token_with_all_params(self, async_client: AsyncAsktable) -> None:
        auth = await async_client.auth.create_token(
            ak_role="asker",
            chat_role={
                "role_id": "1",
                "role_variables": {"id": "42"},
            },
            token_ttl=900,
            user_profile={"name": "张三"},
        )
        assert_matches_type(object, auth, path=["response"])

    @parametrize
    async def test_raw_response_create_token(self, async_client: AsyncAsktable) -> None:
        response = await async_client.auth.with_raw_response.create_token()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = await response.parse()
        assert_matches_type(object, auth, path=["response"])

    @parametrize
    async def test_streaming_response_create_token(self, async_client: AsyncAsktable) -> None:
        async with async_client.auth.with_streaming_response.create_token() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = await response.parse()
            assert_matches_type(object, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_me(self, async_client: AsyncAsktable) -> None:
        auth = await async_client.auth.me()
        assert_matches_type(AuthMeResponse, auth, path=["response"])

    @parametrize
    async def test_raw_response_me(self, async_client: AsyncAsktable) -> None:
        response = await async_client.auth.with_raw_response.me()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = await response.parse()
        assert_matches_type(AuthMeResponse, auth, path=["response"])

    @parametrize
    async def test_streaming_response_me(self, async_client: AsyncAsktable) -> None:
        async with async_client.auth.with_streaming_response.me() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = await response.parse()
            assert_matches_type(AuthMeResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True
