# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from asktable import Asktable, AsyncAsktable
from tests.utils import assert_matches_type
from asktable.types import PolishCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPolish:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Asktable) -> None:
        polish = client.polish.create(
            max_word_count=0,
            user_desc="user_desc",
        )
        assert_matches_type(PolishCreateResponse, polish, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Asktable) -> None:
        polish = client.polish.create(
            max_word_count=0,
            user_desc="user_desc",
            polish_mode=0,
        )
        assert_matches_type(PolishCreateResponse, polish, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Asktable) -> None:
        response = client.polish.with_raw_response.create(
            max_word_count=0,
            user_desc="user_desc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        polish = response.parse()
        assert_matches_type(PolishCreateResponse, polish, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Asktable) -> None:
        with client.polish.with_streaming_response.create(
            max_word_count=0,
            user_desc="user_desc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            polish = response.parse()
            assert_matches_type(PolishCreateResponse, polish, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPolish:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncAsktable) -> None:
        polish = await async_client.polish.create(
            max_word_count=0,
            user_desc="user_desc",
        )
        assert_matches_type(PolishCreateResponse, polish, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncAsktable) -> None:
        polish = await async_client.polish.create(
            max_word_count=0,
            user_desc="user_desc",
            polish_mode=0,
        )
        assert_matches_type(PolishCreateResponse, polish, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncAsktable) -> None:
        response = await async_client.polish.with_raw_response.create(
            max_word_count=0,
            user_desc="user_desc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        polish = await response.parse()
        assert_matches_type(PolishCreateResponse, polish, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncAsktable) -> None:
        async with async_client.polish.with_streaming_response.create(
            max_word_count=0,
            user_desc="user_desc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            polish = await response.parse()
            assert_matches_type(PolishCreateResponse, polish, path=["response"])

        assert cast(Any, response.is_closed) is True
