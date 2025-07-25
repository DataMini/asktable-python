# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from asktable import Asktable, AsyncAsktable
from tests.utils import assert_matches_type
from asktable.types import Index
from asktable.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIndexes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Asktable) -> None:
        index = client.datasources.indexes.create(
            ds_id="ds_id",
            field_name="field_name",
            schema_name="schema_name",
            table_name="table_name",
        )
        assert_matches_type(object, index, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Asktable) -> None:
        index = client.datasources.indexes.create(
            ds_id="ds_id",
            field_name="field_name",
            schema_name="schema_name",
            table_name="table_name",
            async_process=True,
        )
        assert_matches_type(object, index, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Asktable) -> None:
        response = client.datasources.indexes.with_raw_response.create(
            ds_id="ds_id",
            field_name="field_name",
            schema_name="schema_name",
            table_name="table_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        index = response.parse()
        assert_matches_type(object, index, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Asktable) -> None:
        with client.datasources.indexes.with_streaming_response.create(
            ds_id="ds_id",
            field_name="field_name",
            schema_name="schema_name",
            table_name="table_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            index = response.parse()
            assert_matches_type(object, index, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Asktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ds_id` but received ''"):
            client.datasources.indexes.with_raw_response.create(
                ds_id="",
                field_name="field_name",
                schema_name="schema_name",
                table_name="table_name",
            )

    @parametrize
    def test_method_list(self, client: Asktable) -> None:
        index = client.datasources.indexes.list(
            ds_id="ds_id",
        )
        assert_matches_type(SyncPage[Index], index, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Asktable) -> None:
        index = client.datasources.indexes.list(
            ds_id="ds_id",
            page=1,
            size=1,
        )
        assert_matches_type(SyncPage[Index], index, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Asktable) -> None:
        response = client.datasources.indexes.with_raw_response.list(
            ds_id="ds_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        index = response.parse()
        assert_matches_type(SyncPage[Index], index, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Asktable) -> None:
        with client.datasources.indexes.with_streaming_response.list(
            ds_id="ds_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            index = response.parse()
            assert_matches_type(SyncPage[Index], index, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Asktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ds_id` but received ''"):
            client.datasources.indexes.with_raw_response.list(
                ds_id="",
            )

    @parametrize
    def test_method_delete(self, client: Asktable) -> None:
        index = client.datasources.indexes.delete(
            index_id="index_id",
            ds_id="ds_id",
        )
        assert_matches_type(object, index, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Asktable) -> None:
        response = client.datasources.indexes.with_raw_response.delete(
            index_id="index_id",
            ds_id="ds_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        index = response.parse()
        assert_matches_type(object, index, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Asktable) -> None:
        with client.datasources.indexes.with_streaming_response.delete(
            index_id="index_id",
            ds_id="ds_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            index = response.parse()
            assert_matches_type(object, index, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Asktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ds_id` but received ''"):
            client.datasources.indexes.with_raw_response.delete(
                index_id="index_id",
                ds_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `index_id` but received ''"):
            client.datasources.indexes.with_raw_response.delete(
                index_id="",
                ds_id="ds_id",
            )


class TestAsyncIndexes:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncAsktable) -> None:
        index = await async_client.datasources.indexes.create(
            ds_id="ds_id",
            field_name="field_name",
            schema_name="schema_name",
            table_name="table_name",
        )
        assert_matches_type(object, index, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncAsktable) -> None:
        index = await async_client.datasources.indexes.create(
            ds_id="ds_id",
            field_name="field_name",
            schema_name="schema_name",
            table_name="table_name",
            async_process=True,
        )
        assert_matches_type(object, index, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncAsktable) -> None:
        response = await async_client.datasources.indexes.with_raw_response.create(
            ds_id="ds_id",
            field_name="field_name",
            schema_name="schema_name",
            table_name="table_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        index = await response.parse()
        assert_matches_type(object, index, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncAsktable) -> None:
        async with async_client.datasources.indexes.with_streaming_response.create(
            ds_id="ds_id",
            field_name="field_name",
            schema_name="schema_name",
            table_name="table_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            index = await response.parse()
            assert_matches_type(object, index, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncAsktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ds_id` but received ''"):
            await async_client.datasources.indexes.with_raw_response.create(
                ds_id="",
                field_name="field_name",
                schema_name="schema_name",
                table_name="table_name",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncAsktable) -> None:
        index = await async_client.datasources.indexes.list(
            ds_id="ds_id",
        )
        assert_matches_type(AsyncPage[Index], index, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncAsktable) -> None:
        index = await async_client.datasources.indexes.list(
            ds_id="ds_id",
            page=1,
            size=1,
        )
        assert_matches_type(AsyncPage[Index], index, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncAsktable) -> None:
        response = await async_client.datasources.indexes.with_raw_response.list(
            ds_id="ds_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        index = await response.parse()
        assert_matches_type(AsyncPage[Index], index, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncAsktable) -> None:
        async with async_client.datasources.indexes.with_streaming_response.list(
            ds_id="ds_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            index = await response.parse()
            assert_matches_type(AsyncPage[Index], index, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncAsktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ds_id` but received ''"):
            await async_client.datasources.indexes.with_raw_response.list(
                ds_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncAsktable) -> None:
        index = await async_client.datasources.indexes.delete(
            index_id="index_id",
            ds_id="ds_id",
        )
        assert_matches_type(object, index, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncAsktable) -> None:
        response = await async_client.datasources.indexes.with_raw_response.delete(
            index_id="index_id",
            ds_id="ds_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        index = await response.parse()
        assert_matches_type(object, index, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncAsktable) -> None:
        async with async_client.datasources.indexes.with_streaming_response.delete(
            index_id="index_id",
            ds_id="ds_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            index = await response.parse()
            assert_matches_type(object, index, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncAsktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ds_id` but received ''"):
            await async_client.datasources.indexes.with_raw_response.delete(
                index_id="index_id",
                ds_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `index_id` but received ''"):
            await async_client.datasources.indexes.with_raw_response.delete(
                index_id="",
                ds_id="ds_id",
            )
