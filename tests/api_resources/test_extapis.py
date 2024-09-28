# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from asktable import Asktable, AsyncAsktable
from tests.utils import assert_matches_type
from asktable.types import (
    ExtapiModel,
    ExtapiListResponse,
)
from asktable._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExtapis:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Asktable) -> None:
        extapi = client.extapis.create(
            id="id",
            base_url="https://api.example.com/v1",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            name="name",
            project_id="project_id",
        )
        assert_matches_type(ExtapiModel, extapi, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Asktable) -> None:
        extapi = client.extapis.create(
            id="id",
            base_url="https://api.example.com/v1",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            name="name",
            project_id="project_id",
            headers={"Authorization": "Bearer <token>"},
            updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ExtapiModel, extapi, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Asktable) -> None:
        response = client.extapis.with_raw_response.create(
            id="id",
            base_url="https://api.example.com/v1",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            name="name",
            project_id="project_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extapi = response.parse()
        assert_matches_type(ExtapiModel, extapi, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Asktable) -> None:
        with client.extapis.with_streaming_response.create(
            id="id",
            base_url="https://api.example.com/v1",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            name="name",
            project_id="project_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extapi = response.parse()
            assert_matches_type(ExtapiModel, extapi, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Asktable) -> None:
        extapi = client.extapis.retrieve(
            "extapi_id",
        )
        assert_matches_type(ExtapiModel, extapi, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Asktable) -> None:
        response = client.extapis.with_raw_response.retrieve(
            "extapi_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extapi = response.parse()
        assert_matches_type(ExtapiModel, extapi, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Asktable) -> None:
        with client.extapis.with_streaming_response.retrieve(
            "extapi_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extapi = response.parse()
            assert_matches_type(ExtapiModel, extapi, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Asktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `extapi_id` but received ''"):
            client.extapis.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Asktable) -> None:
        extapi = client.extapis.update(
            extapi_id="extapi_id",
        )
        assert_matches_type(ExtapiModel, extapi, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Asktable) -> None:
        extapi = client.extapis.update(
            extapi_id="extapi_id",
            base_url="https://api.example.com/v1",
            headers={"Authorization": "Bearer <token>"},
            name="name",
        )
        assert_matches_type(ExtapiModel, extapi, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Asktable) -> None:
        response = client.extapis.with_raw_response.update(
            extapi_id="extapi_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extapi = response.parse()
        assert_matches_type(ExtapiModel, extapi, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Asktable) -> None:
        with client.extapis.with_streaming_response.update(
            extapi_id="extapi_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extapi = response.parse()
            assert_matches_type(ExtapiModel, extapi, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Asktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `extapi_id` but received ''"):
            client.extapis.with_raw_response.update(
                extapi_id="",
            )

    @parametrize
    def test_method_list(self, client: Asktable) -> None:
        extapi = client.extapis.list()
        assert_matches_type(ExtapiListResponse, extapi, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Asktable) -> None:
        extapi = client.extapis.list(
            name="name",
            page=1,
            size=1,
        )
        assert_matches_type(ExtapiListResponse, extapi, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Asktable) -> None:
        response = client.extapis.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extapi = response.parse()
        assert_matches_type(ExtapiListResponse, extapi, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Asktable) -> None:
        with client.extapis.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extapi = response.parse()
            assert_matches_type(ExtapiListResponse, extapi, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Asktable) -> None:
        extapi = client.extapis.delete(
            "extapi_id",
        )
        assert_matches_type(object, extapi, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Asktable) -> None:
        response = client.extapis.with_raw_response.delete(
            "extapi_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extapi = response.parse()
        assert_matches_type(object, extapi, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Asktable) -> None:
        with client.extapis.with_streaming_response.delete(
            "extapi_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extapi = response.parse()
            assert_matches_type(object, extapi, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Asktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `extapi_id` but received ''"):
            client.extapis.with_raw_response.delete(
                "",
            )


class TestAsyncExtapis:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncAsktable) -> None:
        extapi = await async_client.extapis.create(
            id="id",
            base_url="https://api.example.com/v1",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            name="name",
            project_id="project_id",
        )
        assert_matches_type(ExtapiModel, extapi, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncAsktable) -> None:
        extapi = await async_client.extapis.create(
            id="id",
            base_url="https://api.example.com/v1",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            name="name",
            project_id="project_id",
            headers={"Authorization": "Bearer <token>"},
            updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ExtapiModel, extapi, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncAsktable) -> None:
        response = await async_client.extapis.with_raw_response.create(
            id="id",
            base_url="https://api.example.com/v1",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            name="name",
            project_id="project_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extapi = await response.parse()
        assert_matches_type(ExtapiModel, extapi, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncAsktable) -> None:
        async with async_client.extapis.with_streaming_response.create(
            id="id",
            base_url="https://api.example.com/v1",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            name="name",
            project_id="project_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extapi = await response.parse()
            assert_matches_type(ExtapiModel, extapi, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncAsktable) -> None:
        extapi = await async_client.extapis.retrieve(
            "extapi_id",
        )
        assert_matches_type(ExtapiModel, extapi, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncAsktable) -> None:
        response = await async_client.extapis.with_raw_response.retrieve(
            "extapi_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extapi = await response.parse()
        assert_matches_type(ExtapiModel, extapi, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncAsktable) -> None:
        async with async_client.extapis.with_streaming_response.retrieve(
            "extapi_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extapi = await response.parse()
            assert_matches_type(ExtapiModel, extapi, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncAsktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `extapi_id` but received ''"):
            await async_client.extapis.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncAsktable) -> None:
        extapi = await async_client.extapis.update(
            extapi_id="extapi_id",
        )
        assert_matches_type(ExtapiModel, extapi, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncAsktable) -> None:
        extapi = await async_client.extapis.update(
            extapi_id="extapi_id",
            base_url="https://api.example.com/v1",
            headers={"Authorization": "Bearer <token>"},
            name="name",
        )
        assert_matches_type(ExtapiModel, extapi, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncAsktable) -> None:
        response = await async_client.extapis.with_raw_response.update(
            extapi_id="extapi_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extapi = await response.parse()
        assert_matches_type(ExtapiModel, extapi, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncAsktable) -> None:
        async with async_client.extapis.with_streaming_response.update(
            extapi_id="extapi_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extapi = await response.parse()
            assert_matches_type(ExtapiModel, extapi, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncAsktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `extapi_id` but received ''"):
            await async_client.extapis.with_raw_response.update(
                extapi_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncAsktable) -> None:
        extapi = await async_client.extapis.list()
        assert_matches_type(ExtapiListResponse, extapi, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncAsktable) -> None:
        extapi = await async_client.extapis.list(
            name="name",
            page=1,
            size=1,
        )
        assert_matches_type(ExtapiListResponse, extapi, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncAsktable) -> None:
        response = await async_client.extapis.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extapi = await response.parse()
        assert_matches_type(ExtapiListResponse, extapi, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncAsktable) -> None:
        async with async_client.extapis.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extapi = await response.parse()
            assert_matches_type(ExtapiListResponse, extapi, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncAsktable) -> None:
        extapi = await async_client.extapis.delete(
            "extapi_id",
        )
        assert_matches_type(object, extapi, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncAsktable) -> None:
        response = await async_client.extapis.with_raw_response.delete(
            "extapi_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extapi = await response.parse()
        assert_matches_type(object, extapi, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncAsktable) -> None:
        async with async_client.extapis.with_streaming_response.delete(
            "extapi_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extapi = await response.parse()
            assert_matches_type(object, extapi, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncAsktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `extapi_id` but received ''"):
            await async_client.extapis.with_raw_response.delete(
                "",
            )
