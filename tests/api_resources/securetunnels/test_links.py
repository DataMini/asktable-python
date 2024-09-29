# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from asktable import Asktable, AsyncAsktable
from tests.utils import assert_matches_type
from asktable.types.securetunnels import SecureTunnelLink

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLinks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Asktable) -> None:
        link = client.securetunnels.links.list(
            securetunnel_id="securetunnel_id",
        )
        assert_matches_type(SecureTunnelLink, link, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Asktable) -> None:
        link = client.securetunnels.links.list(
            securetunnel_id="securetunnel_id",
            page=1,
            size=1,
        )
        assert_matches_type(SecureTunnelLink, link, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Asktable) -> None:
        response = client.securetunnels.links.with_raw_response.list(
            securetunnel_id="securetunnel_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        link = response.parse()
        assert_matches_type(SecureTunnelLink, link, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Asktable) -> None:
        with client.securetunnels.links.with_streaming_response.list(
            securetunnel_id="securetunnel_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            link = response.parse()
            assert_matches_type(SecureTunnelLink, link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Asktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `securetunnel_id` but received ''"):
            client.securetunnels.links.with_raw_response.list(
                securetunnel_id="",
            )


class TestAsyncLinks:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncAsktable) -> None:
        link = await async_client.securetunnels.links.list(
            securetunnel_id="securetunnel_id",
        )
        assert_matches_type(SecureTunnelLink, link, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncAsktable) -> None:
        link = await async_client.securetunnels.links.list(
            securetunnel_id="securetunnel_id",
            page=1,
            size=1,
        )
        assert_matches_type(SecureTunnelLink, link, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncAsktable) -> None:
        response = await async_client.securetunnels.links.with_raw_response.list(
            securetunnel_id="securetunnel_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        link = await response.parse()
        assert_matches_type(SecureTunnelLink, link, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncAsktable) -> None:
        async with async_client.securetunnels.links.with_streaming_response.list(
            securetunnel_id="securetunnel_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            link = await response.parse()
            assert_matches_type(SecureTunnelLink, link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncAsktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `securetunnel_id` but received ''"):
            await async_client.securetunnels.links.with_raw_response.list(
                securetunnel_id="",
            )
