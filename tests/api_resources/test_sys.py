# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from asktable import Asktable, AsyncAsktable
from tests.utils import assert_matches_type
from asktable.types import SyUpdateConfigResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSys:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update_config(self, client: Asktable) -> None:
        sy = client.sys.update_config()
        assert_matches_type(SyUpdateConfigResponse, sy, path=["response"])

    @parametrize
    def test_method_update_config_with_all_params(self, client: Asktable) -> None:
        sy = client.sys.update_config(
            global_table_limit=0,
        )
        assert_matches_type(SyUpdateConfigResponse, sy, path=["response"])

    @parametrize
    def test_raw_response_update_config(self, client: Asktable) -> None:
        response = client.sys.with_raw_response.update_config()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sy = response.parse()
        assert_matches_type(SyUpdateConfigResponse, sy, path=["response"])

    @parametrize
    def test_streaming_response_update_config(self, client: Asktable) -> None:
        with client.sys.with_streaming_response.update_config() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sy = response.parse()
            assert_matches_type(SyUpdateConfigResponse, sy, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSys:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_update_config(self, async_client: AsyncAsktable) -> None:
        sy = await async_client.sys.update_config()
        assert_matches_type(SyUpdateConfigResponse, sy, path=["response"])

    @parametrize
    async def test_method_update_config_with_all_params(self, async_client: AsyncAsktable) -> None:
        sy = await async_client.sys.update_config(
            global_table_limit=0,
        )
        assert_matches_type(SyUpdateConfigResponse, sy, path=["response"])

    @parametrize
    async def test_raw_response_update_config(self, async_client: AsyncAsktable) -> None:
        response = await async_client.sys.with_raw_response.update_config()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sy = await response.parse()
        assert_matches_type(SyUpdateConfigResponse, sy, path=["response"])

    @parametrize
    async def test_streaming_response_update_config(self, async_client: AsyncAsktable) -> None:
        async with async_client.sys.with_streaming_response.update_config() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sy = await response.parse()
            assert_matches_type(SyUpdateConfigResponse, sy, path=["response"])

        assert cast(Any, response.is_closed) is True
