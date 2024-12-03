# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from asktable import Asktable, AsyncAsktable
from tests.utils import assert_matches_type
from asktable.types import (
    SecureTunnel,
    SecuretunnelListLinksResponse,
)
from asktable.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSecuretunnels:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Asktable) -> None:
        securetunnel = client.securetunnels.create(
            name="我的测试机",
        )
        assert_matches_type(SecureTunnel, securetunnel, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Asktable) -> None:
        response = client.securetunnels.with_raw_response.create(
            name="我的测试机",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        securetunnel = response.parse()
        assert_matches_type(SecureTunnel, securetunnel, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Asktable) -> None:
        with client.securetunnels.with_streaming_response.create(
            name="我的测试机",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            securetunnel = response.parse()
            assert_matches_type(SecureTunnel, securetunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Asktable) -> None:
        securetunnel = client.securetunnels.retrieve(
            "securetunnel_id",
        )
        assert_matches_type(SecureTunnel, securetunnel, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Asktable) -> None:
        response = client.securetunnels.with_raw_response.retrieve(
            "securetunnel_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        securetunnel = response.parse()
        assert_matches_type(SecureTunnel, securetunnel, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Asktable) -> None:
        with client.securetunnels.with_streaming_response.retrieve(
            "securetunnel_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            securetunnel = response.parse()
            assert_matches_type(SecureTunnel, securetunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Asktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `securetunnel_id` but received ''"):
            client.securetunnels.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Asktable) -> None:
        securetunnel = client.securetunnels.update(
            securetunnel_id="securetunnel_id",
            name="我的测试机",
        )
        assert_matches_type(SecureTunnel, securetunnel, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Asktable) -> None:
        securetunnel = client.securetunnels.update(
            securetunnel_id="securetunnel_id",
            name="我的测试机",
            client_info={},
            unique_key="unique_key",
        )
        assert_matches_type(SecureTunnel, securetunnel, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Asktable) -> None:
        response = client.securetunnels.with_raw_response.update(
            securetunnel_id="securetunnel_id",
            name="我的测试机",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        securetunnel = response.parse()
        assert_matches_type(SecureTunnel, securetunnel, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Asktable) -> None:
        with client.securetunnels.with_streaming_response.update(
            securetunnel_id="securetunnel_id",
            name="我的测试机",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            securetunnel = response.parse()
            assert_matches_type(SecureTunnel, securetunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Asktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `securetunnel_id` but received ''"):
            client.securetunnels.with_raw_response.update(
                securetunnel_id="",
                name="我的测试机",
            )

    @parametrize
    def test_method_list(self, client: Asktable) -> None:
        securetunnel = client.securetunnels.list()
        assert_matches_type(SyncPage[SecureTunnel], securetunnel, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Asktable) -> None:
        securetunnel = client.securetunnels.list(
            page=1,
            size=1,
        )
        assert_matches_type(SyncPage[SecureTunnel], securetunnel, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Asktable) -> None:
        response = client.securetunnels.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        securetunnel = response.parse()
        assert_matches_type(SyncPage[SecureTunnel], securetunnel, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Asktable) -> None:
        with client.securetunnels.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            securetunnel = response.parse()
            assert_matches_type(SyncPage[SecureTunnel], securetunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Asktable) -> None:
        securetunnel = client.securetunnels.delete(
            "securetunnel_id",
        )
        assert securetunnel is None

    @parametrize
    def test_raw_response_delete(self, client: Asktable) -> None:
        response = client.securetunnels.with_raw_response.delete(
            "securetunnel_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        securetunnel = response.parse()
        assert securetunnel is None

    @parametrize
    def test_streaming_response_delete(self, client: Asktable) -> None:
        with client.securetunnels.with_streaming_response.delete(
            "securetunnel_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            securetunnel = response.parse()
            assert securetunnel is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Asktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `securetunnel_id` but received ''"):
            client.securetunnels.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_list_links(self, client: Asktable) -> None:
        securetunnel = client.securetunnels.list_links(
            securetunnel_id="securetunnel_id",
        )
        assert_matches_type(SyncPage[SecuretunnelListLinksResponse], securetunnel, path=["response"])

    @parametrize
    def test_method_list_links_with_all_params(self, client: Asktable) -> None:
        securetunnel = client.securetunnels.list_links(
            securetunnel_id="securetunnel_id",
            page=1,
            size=1,
        )
        assert_matches_type(SyncPage[SecuretunnelListLinksResponse], securetunnel, path=["response"])

    @parametrize
    def test_raw_response_list_links(self, client: Asktable) -> None:
        response = client.securetunnels.with_raw_response.list_links(
            securetunnel_id="securetunnel_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        securetunnel = response.parse()
        assert_matches_type(SyncPage[SecuretunnelListLinksResponse], securetunnel, path=["response"])

    @parametrize
    def test_streaming_response_list_links(self, client: Asktable) -> None:
        with client.securetunnels.with_streaming_response.list_links(
            securetunnel_id="securetunnel_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            securetunnel = response.parse()
            assert_matches_type(SyncPage[SecuretunnelListLinksResponse], securetunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list_links(self, client: Asktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `securetunnel_id` but received ''"):
            client.securetunnels.with_raw_response.list_links(
                securetunnel_id="",
            )


class TestAsyncSecuretunnels:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncAsktable) -> None:
        securetunnel = await async_client.securetunnels.create(
            name="我的测试机",
        )
        assert_matches_type(SecureTunnel, securetunnel, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncAsktable) -> None:
        response = await async_client.securetunnels.with_raw_response.create(
            name="我的测试机",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        securetunnel = await response.parse()
        assert_matches_type(SecureTunnel, securetunnel, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncAsktable) -> None:
        async with async_client.securetunnels.with_streaming_response.create(
            name="我的测试机",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            securetunnel = await response.parse()
            assert_matches_type(SecureTunnel, securetunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncAsktable) -> None:
        securetunnel = await async_client.securetunnels.retrieve(
            "securetunnel_id",
        )
        assert_matches_type(SecureTunnel, securetunnel, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncAsktable) -> None:
        response = await async_client.securetunnels.with_raw_response.retrieve(
            "securetunnel_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        securetunnel = await response.parse()
        assert_matches_type(SecureTunnel, securetunnel, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncAsktable) -> None:
        async with async_client.securetunnels.with_streaming_response.retrieve(
            "securetunnel_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            securetunnel = await response.parse()
            assert_matches_type(SecureTunnel, securetunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncAsktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `securetunnel_id` but received ''"):
            await async_client.securetunnels.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncAsktable) -> None:
        securetunnel = await async_client.securetunnels.update(
            securetunnel_id="securetunnel_id",
            name="我的测试机",
        )
        assert_matches_type(SecureTunnel, securetunnel, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncAsktable) -> None:
        securetunnel = await async_client.securetunnels.update(
            securetunnel_id="securetunnel_id",
            name="我的测试机",
            client_info={},
            unique_key="unique_key",
        )
        assert_matches_type(SecureTunnel, securetunnel, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncAsktable) -> None:
        response = await async_client.securetunnels.with_raw_response.update(
            securetunnel_id="securetunnel_id",
            name="我的测试机",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        securetunnel = await response.parse()
        assert_matches_type(SecureTunnel, securetunnel, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncAsktable) -> None:
        async with async_client.securetunnels.with_streaming_response.update(
            securetunnel_id="securetunnel_id",
            name="我的测试机",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            securetunnel = await response.parse()
            assert_matches_type(SecureTunnel, securetunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncAsktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `securetunnel_id` but received ''"):
            await async_client.securetunnels.with_raw_response.update(
                securetunnel_id="",
                name="我的测试机",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncAsktable) -> None:
        securetunnel = await async_client.securetunnels.list()
        assert_matches_type(AsyncPage[SecureTunnel], securetunnel, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncAsktable) -> None:
        securetunnel = await async_client.securetunnels.list(
            page=1,
            size=1,
        )
        assert_matches_type(AsyncPage[SecureTunnel], securetunnel, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncAsktable) -> None:
        response = await async_client.securetunnels.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        securetunnel = await response.parse()
        assert_matches_type(AsyncPage[SecureTunnel], securetunnel, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncAsktable) -> None:
        async with async_client.securetunnels.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            securetunnel = await response.parse()
            assert_matches_type(AsyncPage[SecureTunnel], securetunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncAsktable) -> None:
        securetunnel = await async_client.securetunnels.delete(
            "securetunnel_id",
        )
        assert securetunnel is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncAsktable) -> None:
        response = await async_client.securetunnels.with_raw_response.delete(
            "securetunnel_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        securetunnel = await response.parse()
        assert securetunnel is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncAsktable) -> None:
        async with async_client.securetunnels.with_streaming_response.delete(
            "securetunnel_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            securetunnel = await response.parse()
            assert securetunnel is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncAsktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `securetunnel_id` but received ''"):
            await async_client.securetunnels.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_list_links(self, async_client: AsyncAsktable) -> None:
        securetunnel = await async_client.securetunnels.list_links(
            securetunnel_id="securetunnel_id",
        )
        assert_matches_type(AsyncPage[SecuretunnelListLinksResponse], securetunnel, path=["response"])

    @parametrize
    async def test_method_list_links_with_all_params(self, async_client: AsyncAsktable) -> None:
        securetunnel = await async_client.securetunnels.list_links(
            securetunnel_id="securetunnel_id",
            page=1,
            size=1,
        )
        assert_matches_type(AsyncPage[SecuretunnelListLinksResponse], securetunnel, path=["response"])

    @parametrize
    async def test_raw_response_list_links(self, async_client: AsyncAsktable) -> None:
        response = await async_client.securetunnels.with_raw_response.list_links(
            securetunnel_id="securetunnel_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        securetunnel = await response.parse()
        assert_matches_type(AsyncPage[SecuretunnelListLinksResponse], securetunnel, path=["response"])

    @parametrize
    async def test_streaming_response_list_links(self, async_client: AsyncAsktable) -> None:
        async with async_client.securetunnels.with_streaming_response.list_links(
            securetunnel_id="securetunnel_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            securetunnel = await response.parse()
            assert_matches_type(AsyncPage[SecuretunnelListLinksResponse], securetunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list_links(self, async_client: AsyncAsktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `securetunnel_id` but received ''"):
            await async_client.securetunnels.with_raw_response.list_links(
                securetunnel_id="",
            )
