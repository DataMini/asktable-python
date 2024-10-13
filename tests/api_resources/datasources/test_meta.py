# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from asktable import Asktable, AsyncAsktable
from tests.utils import assert_matches_type
from asktable.types.datasources import Meta

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMeta:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Asktable) -> None:
        meta = client.datasources.meta.create(
            "datasource_id",
        )
        assert_matches_type(object, meta, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Asktable) -> None:
        response = client.datasources.meta.with_raw_response.create(
            "datasource_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        meta = response.parse()
        assert_matches_type(object, meta, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Asktable) -> None:
        with client.datasources.meta.with_streaming_response.create(
            "datasource_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            meta = response.parse()
            assert_matches_type(object, meta, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Asktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `datasource_id` but received ''"):
            client.datasources.meta.with_raw_response.create(
                "",
            )

    @parametrize
    def test_method_retrieve(self, client: Asktable) -> None:
        meta = client.datasources.meta.retrieve(
            datasource_id="datasource_id",
        )
        assert_matches_type(Meta, meta, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Asktable) -> None:
        meta = client.datasources.meta.retrieve(
            datasource_id="datasource_id",
            from_where="in_brain",
        )
        assert_matches_type(Meta, meta, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Asktable) -> None:
        response = client.datasources.meta.with_raw_response.retrieve(
            datasource_id="datasource_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        meta = response.parse()
        assert_matches_type(Meta, meta, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Asktable) -> None:
        with client.datasources.meta.with_streaming_response.retrieve(
            datasource_id="datasource_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            meta = response.parse()
            assert_matches_type(Meta, meta, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Asktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `datasource_id` but received ''"):
            client.datasources.meta.with_raw_response.retrieve(
                datasource_id="",
            )

    @parametrize
    def test_method_update(self, client: Asktable) -> None:
        meta = client.datasources.meta.update(
            path_datasource_id="datasource_id",
            body_datasource_id="datasource_id",
            name="name",
        )
        assert_matches_type(object, meta, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Asktable) -> None:
        meta = client.datasources.meta.update(
            path_datasource_id="datasource_id",
            body_datasource_id="datasource_id",
            name="name",
            schemas={
                "foo": {
                    "curr_desc": "curr_desc",
                    "curr_desc_stat": "curr_desc_stat",
                    "name": "name",
                    "custom_configs": {},
                    "origin_desc": "origin_desc",
                    "tables": {
                        "foo": {
                            "curr_desc": "curr_desc",
                            "curr_desc_stat": "curr_desc_stat",
                            "full_name": "full_name",
                            "name": "name",
                            "fields": {
                                "foo": {
                                    "curr_desc": "curr_desc",
                                    "curr_desc_stat": "curr_desc_stat",
                                    "full_name": "full_name",
                                    "name": "name",
                                    "data_type": "data_type",
                                    "origin_desc": "origin_desc",
                                    "sample_data": "sample_data",
                                }
                            },
                            "origin_desc": "origin_desc",
                        }
                    },
                }
            },
        )
        assert_matches_type(object, meta, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Asktable) -> None:
        response = client.datasources.meta.with_raw_response.update(
            path_datasource_id="datasource_id",
            body_datasource_id="datasource_id",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        meta = response.parse()
        assert_matches_type(object, meta, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Asktable) -> None:
        with client.datasources.meta.with_streaming_response.update(
            path_datasource_id="datasource_id",
            body_datasource_id="datasource_id",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            meta = response.parse()
            assert_matches_type(object, meta, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Asktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_datasource_id` but received ''"):
            client.datasources.meta.with_raw_response.update(
                path_datasource_id="",
                body_datasource_id="",
                name="name",
            )


class TestAsyncMeta:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncAsktable) -> None:
        meta = await async_client.datasources.meta.create(
            "datasource_id",
        )
        assert_matches_type(object, meta, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncAsktable) -> None:
        response = await async_client.datasources.meta.with_raw_response.create(
            "datasource_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        meta = await response.parse()
        assert_matches_type(object, meta, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncAsktable) -> None:
        async with async_client.datasources.meta.with_streaming_response.create(
            "datasource_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            meta = await response.parse()
            assert_matches_type(object, meta, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncAsktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `datasource_id` but received ''"):
            await async_client.datasources.meta.with_raw_response.create(
                "",
            )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncAsktable) -> None:
        meta = await async_client.datasources.meta.retrieve(
            datasource_id="datasource_id",
        )
        assert_matches_type(Meta, meta, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncAsktable) -> None:
        meta = await async_client.datasources.meta.retrieve(
            datasource_id="datasource_id",
            from_where="in_brain",
        )
        assert_matches_type(Meta, meta, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncAsktable) -> None:
        response = await async_client.datasources.meta.with_raw_response.retrieve(
            datasource_id="datasource_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        meta = await response.parse()
        assert_matches_type(Meta, meta, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncAsktable) -> None:
        async with async_client.datasources.meta.with_streaming_response.retrieve(
            datasource_id="datasource_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            meta = await response.parse()
            assert_matches_type(Meta, meta, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncAsktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `datasource_id` but received ''"):
            await async_client.datasources.meta.with_raw_response.retrieve(
                datasource_id="",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncAsktable) -> None:
        meta = await async_client.datasources.meta.update(
            path_datasource_id="datasource_id",
            body_datasource_id="datasource_id",
            name="name",
        )
        assert_matches_type(object, meta, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncAsktable) -> None:
        meta = await async_client.datasources.meta.update(
            path_datasource_id="datasource_id",
            body_datasource_id="datasource_id",
            name="name",
            schemas={
                "foo": {
                    "curr_desc": "curr_desc",
                    "curr_desc_stat": "curr_desc_stat",
                    "name": "name",
                    "custom_configs": {},
                    "origin_desc": "origin_desc",
                    "tables": {
                        "foo": {
                            "curr_desc": "curr_desc",
                            "curr_desc_stat": "curr_desc_stat",
                            "full_name": "full_name",
                            "name": "name",
                            "fields": {
                                "foo": {
                                    "curr_desc": "curr_desc",
                                    "curr_desc_stat": "curr_desc_stat",
                                    "full_name": "full_name",
                                    "name": "name",
                                    "data_type": "data_type",
                                    "origin_desc": "origin_desc",
                                    "sample_data": "sample_data",
                                }
                            },
                            "origin_desc": "origin_desc",
                        }
                    },
                }
            },
        )
        assert_matches_type(object, meta, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncAsktable) -> None:
        response = await async_client.datasources.meta.with_raw_response.update(
            path_datasource_id="datasource_id",
            body_datasource_id="datasource_id",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        meta = await response.parse()
        assert_matches_type(object, meta, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncAsktable) -> None:
        async with async_client.datasources.meta.with_streaming_response.update(
            path_datasource_id="datasource_id",
            body_datasource_id="datasource_id",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            meta = await response.parse()
            assert_matches_type(object, meta, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncAsktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_datasource_id` but received ''"):
            await async_client.datasources.meta.with_raw_response.update(
                path_datasource_id="",
                body_datasource_id="",
                name="name",
            )
