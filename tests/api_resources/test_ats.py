# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from asktable import Asktable, AsyncAsktable
from tests.utils import assert_matches_type
from asktable.types import (
    ATSListResponse,
    ATSCreateResponse,
    ATSUpdateResponse,
    ATSRetrieveResponse,
)
from asktable.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestATS:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Asktable) -> None:
        ats = client.ats.create(
            datasource_id="datasource_id",
            name="name",
        )
        assert_matches_type(ATSCreateResponse, ats, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Asktable) -> None:
        response = client.ats.with_raw_response.create(
            datasource_id="datasource_id",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ats = response.parse()
        assert_matches_type(ATSCreateResponse, ats, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Asktable) -> None:
        with client.ats.with_streaming_response.create(
            datasource_id="datasource_id",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ats = response.parse()
            assert_matches_type(ATSCreateResponse, ats, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Asktable) -> None:
        ats = client.ats.retrieve(
            "ats_id",
        )
        assert_matches_type(ATSRetrieveResponse, ats, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Asktable) -> None:
        response = client.ats.with_raw_response.retrieve(
            "ats_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ats = response.parse()
        assert_matches_type(ATSRetrieveResponse, ats, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Asktable) -> None:
        with client.ats.with_streaming_response.retrieve(
            "ats_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ats = response.parse()
            assert_matches_type(ATSRetrieveResponse, ats, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Asktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ats_id` but received ''"):
            client.ats.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Asktable) -> None:
        ats = client.ats.update(
            ats_id="ats_id",
            name="name",
        )
        assert_matches_type(ATSUpdateResponse, ats, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Asktable) -> None:
        response = client.ats.with_raw_response.update(
            ats_id="ats_id",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ats = response.parse()
        assert_matches_type(ATSUpdateResponse, ats, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Asktable) -> None:
        with client.ats.with_streaming_response.update(
            ats_id="ats_id",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ats = response.parse()
            assert_matches_type(ATSUpdateResponse, ats, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Asktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ats_id` but received ''"):
            client.ats.with_raw_response.update(
                ats_id="",
                name="name",
            )

    @parametrize
    def test_method_list(self, client: Asktable) -> None:
        ats = client.ats.list(
            datasource_id="datasource_id",
        )
        assert_matches_type(SyncPage[ATSListResponse], ats, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Asktable) -> None:
        ats = client.ats.list(
            datasource_id="datasource_id",
            page=1,
            size=1,
        )
        assert_matches_type(SyncPage[ATSListResponse], ats, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Asktable) -> None:
        response = client.ats.with_raw_response.list(
            datasource_id="datasource_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ats = response.parse()
        assert_matches_type(SyncPage[ATSListResponse], ats, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Asktable) -> None:
        with client.ats.with_streaming_response.list(
            datasource_id="datasource_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ats = response.parse()
            assert_matches_type(SyncPage[ATSListResponse], ats, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Asktable) -> None:
        ats = client.ats.delete(
            ats_id="ats_id",
            datasource_id="datasource_id",
        )
        assert_matches_type(object, ats, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Asktable) -> None:
        response = client.ats.with_raw_response.delete(
            ats_id="ats_id",
            datasource_id="datasource_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ats = response.parse()
        assert_matches_type(object, ats, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Asktable) -> None:
        with client.ats.with_streaming_response.delete(
            ats_id="ats_id",
            datasource_id="datasource_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ats = response.parse()
            assert_matches_type(object, ats, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Asktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ats_id` but received ''"):
            client.ats.with_raw_response.delete(
                ats_id="",
                datasource_id="datasource_id",
            )


class TestAsyncATS:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncAsktable) -> None:
        ats = await async_client.ats.create(
            datasource_id="datasource_id",
            name="name",
        )
        assert_matches_type(ATSCreateResponse, ats, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncAsktable) -> None:
        response = await async_client.ats.with_raw_response.create(
            datasource_id="datasource_id",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ats = await response.parse()
        assert_matches_type(ATSCreateResponse, ats, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncAsktable) -> None:
        async with async_client.ats.with_streaming_response.create(
            datasource_id="datasource_id",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ats = await response.parse()
            assert_matches_type(ATSCreateResponse, ats, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncAsktable) -> None:
        ats = await async_client.ats.retrieve(
            "ats_id",
        )
        assert_matches_type(ATSRetrieveResponse, ats, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncAsktable) -> None:
        response = await async_client.ats.with_raw_response.retrieve(
            "ats_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ats = await response.parse()
        assert_matches_type(ATSRetrieveResponse, ats, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncAsktable) -> None:
        async with async_client.ats.with_streaming_response.retrieve(
            "ats_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ats = await response.parse()
            assert_matches_type(ATSRetrieveResponse, ats, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncAsktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ats_id` but received ''"):
            await async_client.ats.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncAsktable) -> None:
        ats = await async_client.ats.update(
            ats_id="ats_id",
            name="name",
        )
        assert_matches_type(ATSUpdateResponse, ats, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncAsktable) -> None:
        response = await async_client.ats.with_raw_response.update(
            ats_id="ats_id",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ats = await response.parse()
        assert_matches_type(ATSUpdateResponse, ats, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncAsktable) -> None:
        async with async_client.ats.with_streaming_response.update(
            ats_id="ats_id",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ats = await response.parse()
            assert_matches_type(ATSUpdateResponse, ats, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncAsktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ats_id` but received ''"):
            await async_client.ats.with_raw_response.update(
                ats_id="",
                name="name",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncAsktable) -> None:
        ats = await async_client.ats.list(
            datasource_id="datasource_id",
        )
        assert_matches_type(AsyncPage[ATSListResponse], ats, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncAsktable) -> None:
        ats = await async_client.ats.list(
            datasource_id="datasource_id",
            page=1,
            size=1,
        )
        assert_matches_type(AsyncPage[ATSListResponse], ats, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncAsktable) -> None:
        response = await async_client.ats.with_raw_response.list(
            datasource_id="datasource_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ats = await response.parse()
        assert_matches_type(AsyncPage[ATSListResponse], ats, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncAsktable) -> None:
        async with async_client.ats.with_streaming_response.list(
            datasource_id="datasource_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ats = await response.parse()
            assert_matches_type(AsyncPage[ATSListResponse], ats, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncAsktable) -> None:
        ats = await async_client.ats.delete(
            ats_id="ats_id",
            datasource_id="datasource_id",
        )
        assert_matches_type(object, ats, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncAsktable) -> None:
        response = await async_client.ats.with_raw_response.delete(
            ats_id="ats_id",
            datasource_id="datasource_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ats = await response.parse()
        assert_matches_type(object, ats, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncAsktable) -> None:
        async with async_client.ats.with_streaming_response.delete(
            ats_id="ats_id",
            datasource_id="datasource_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ats = await response.parse()
            assert_matches_type(object, ats, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncAsktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ats_id` but received ''"):
            await async_client.ats.with_raw_response.delete(
                ats_id="",
                datasource_id="datasource_id",
            )
