# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from asktable import Asktable, AsyncAsktable
from tests.utils import assert_matches_type
from asktable.types import Meta

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMeta:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_overload_1(self, client: Asktable) -> None:
        meta = client.datasources.meta.create(
            datasource_id="datasource_id",
            name="name",
        )
        assert_matches_type(object, meta, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: Asktable) -> None:
        meta = client.datasources.meta.create(
            datasource_id="datasource_id",
            name="name",
            async_process_meta=True,
            value_index=True,
            schemas={
                "foo": {
                    "name": "name",
                    "custom_configs": {},
                    "origin_desc": "origin_desc",
                    "tables": {
                        "foo": {
                            "name": "name",
                            "fields": {
                                "foo": {
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
    def test_raw_response_create_overload_1(self, client: Asktable) -> None:
        response = client.datasources.meta.with_raw_response.create(
            datasource_id="datasource_id",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        meta = response.parse()
        assert_matches_type(object, meta, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_1(self, client: Asktable) -> None:
        with client.datasources.meta.with_streaming_response.create(
            datasource_id="datasource_id",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            meta = response.parse()
            assert_matches_type(object, meta, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_overload_1(self, client: Asktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `datasource_id` but received ''"):
            client.datasources.meta.with_raw_response.create(
                datasource_id="",
                name="name",
            )

    @parametrize
    def test_method_create_overload_2(self, client: Asktable) -> None:
        meta = client.datasources.meta.create(
            datasource_id="datasource_id",
            body=None,
        )
        assert_matches_type(object, meta, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: Asktable) -> None:
        meta = client.datasources.meta.create(
            datasource_id="datasource_id",
            body=None,
            async_process_meta=True,
            value_index=True,
        )
        assert_matches_type(object, meta, path=["response"])

    @parametrize
    def test_raw_response_create_overload_2(self, client: Asktable) -> None:
        response = client.datasources.meta.with_raw_response.create(
            datasource_id="datasource_id",
            body=None,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        meta = response.parse()
        assert_matches_type(object, meta, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_2(self, client: Asktable) -> None:
        with client.datasources.meta.with_streaming_response.create(
            datasource_id="datasource_id",
            body=None,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            meta = response.parse()
            assert_matches_type(object, meta, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_overload_2(self, client: Asktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `datasource_id` but received ''"):
            client.datasources.meta.with_raw_response.create(
                datasource_id="",
                body=None,
            )

    @parametrize
    def test_method_retrieve(self, client: Asktable) -> None:
        meta = client.datasources.meta.retrieve(
            "datasource_id",
        )
        assert_matches_type(Meta, meta, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Asktable) -> None:
        response = client.datasources.meta.with_raw_response.retrieve(
            "datasource_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        meta = response.parse()
        assert_matches_type(Meta, meta, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Asktable) -> None:
        with client.datasources.meta.with_streaming_response.retrieve(
            "datasource_id",
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
                "",
            )

    @parametrize
    def test_method_update_overload_1(self, client: Asktable) -> None:
        meta = client.datasources.meta.update(
            datasource_id="datasource_id",
            name="name",
        )
        assert_matches_type(object, meta, path=["response"])

    @parametrize
    def test_method_update_with_all_params_overload_1(self, client: Asktable) -> None:
        meta = client.datasources.meta.update(
            datasource_id="datasource_id",
            name="name",
            schemas={
                "foo": {
                    "name": "name",
                    "custom_configs": {},
                    "origin_desc": "origin_desc",
                    "tables": {
                        "foo": {
                            "name": "name",
                            "fields": {
                                "foo": {
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
    def test_raw_response_update_overload_1(self, client: Asktable) -> None:
        response = client.datasources.meta.with_raw_response.update(
            datasource_id="datasource_id",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        meta = response.parse()
        assert_matches_type(object, meta, path=["response"])

    @parametrize
    def test_streaming_response_update_overload_1(self, client: Asktable) -> None:
        with client.datasources.meta.with_streaming_response.update(
            datasource_id="datasource_id",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            meta = response.parse()
            assert_matches_type(object, meta, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_overload_1(self, client: Asktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `datasource_id` but received ''"):
            client.datasources.meta.with_raw_response.update(
                datasource_id="",
                name="name",
            )

    @parametrize
    def test_method_update_overload_2(self, client: Asktable) -> None:
        meta = client.datasources.meta.update(
            datasource_id="datasource_id",
            body=None,
        )
        assert_matches_type(object, meta, path=["response"])

    @parametrize
    def test_raw_response_update_overload_2(self, client: Asktable) -> None:
        response = client.datasources.meta.with_raw_response.update(
            datasource_id="datasource_id",
            body=None,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        meta = response.parse()
        assert_matches_type(object, meta, path=["response"])

    @parametrize
    def test_streaming_response_update_overload_2(self, client: Asktable) -> None:
        with client.datasources.meta.with_streaming_response.update(
            datasource_id="datasource_id",
            body=None,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            meta = response.parse()
            assert_matches_type(object, meta, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_overload_2(self, client: Asktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `datasource_id` but received ''"):
            client.datasources.meta.with_raw_response.update(
                datasource_id="",
                body=None,
            )

    @parametrize
    def test_method_annotate(self, client: Asktable) -> None:
        meta = client.datasources.meta.annotate(
            datasource_id="datasource_id",
            schemas={"foo": {"tables": {"foo": {"fields": {"foo": "string"}}}}},
        )
        assert_matches_type(object, meta, path=["response"])

    @parametrize
    def test_raw_response_annotate(self, client: Asktable) -> None:
        response = client.datasources.meta.with_raw_response.annotate(
            datasource_id="datasource_id",
            schemas={"foo": {"tables": {"foo": {"fields": {"foo": "string"}}}}},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        meta = response.parse()
        assert_matches_type(object, meta, path=["response"])

    @parametrize
    def test_streaming_response_annotate(self, client: Asktable) -> None:
        with client.datasources.meta.with_streaming_response.annotate(
            datasource_id="datasource_id",
            schemas={"foo": {"tables": {"foo": {"fields": {"foo": "string"}}}}},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            meta = response.parse()
            assert_matches_type(object, meta, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_annotate(self, client: Asktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `datasource_id` but received ''"):
            client.datasources.meta.with_raw_response.annotate(
                datasource_id="",
                schemas={"foo": {"tables": {"foo": {"fields": {"foo": "string"}}}}},
            )


class TestAsyncMeta:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncAsktable) -> None:
        meta = await async_client.datasources.meta.create(
            datasource_id="datasource_id",
            name="name",
        )
        assert_matches_type(object, meta, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncAsktable) -> None:
        meta = await async_client.datasources.meta.create(
            datasource_id="datasource_id",
            name="name",
            async_process_meta=True,
            value_index=True,
            schemas={
                "foo": {
                    "name": "name",
                    "custom_configs": {},
                    "origin_desc": "origin_desc",
                    "tables": {
                        "foo": {
                            "name": "name",
                            "fields": {
                                "foo": {
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
    async def test_raw_response_create_overload_1(self, async_client: AsyncAsktable) -> None:
        response = await async_client.datasources.meta.with_raw_response.create(
            datasource_id="datasource_id",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        meta = await response.parse()
        assert_matches_type(object, meta, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncAsktable) -> None:
        async with async_client.datasources.meta.with_streaming_response.create(
            datasource_id="datasource_id",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            meta = await response.parse()
            assert_matches_type(object, meta, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_overload_1(self, async_client: AsyncAsktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `datasource_id` but received ''"):
            await async_client.datasources.meta.with_raw_response.create(
                datasource_id="",
                name="name",
            )

    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncAsktable) -> None:
        meta = await async_client.datasources.meta.create(
            datasource_id="datasource_id",
            body=None,
        )
        assert_matches_type(object, meta, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncAsktable) -> None:
        meta = await async_client.datasources.meta.create(
            datasource_id="datasource_id",
            body=None,
            async_process_meta=True,
            value_index=True,
        )
        assert_matches_type(object, meta, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncAsktable) -> None:
        response = await async_client.datasources.meta.with_raw_response.create(
            datasource_id="datasource_id",
            body=None,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        meta = await response.parse()
        assert_matches_type(object, meta, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncAsktable) -> None:
        async with async_client.datasources.meta.with_streaming_response.create(
            datasource_id="datasource_id",
            body=None,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            meta = await response.parse()
            assert_matches_type(object, meta, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_overload_2(self, async_client: AsyncAsktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `datasource_id` but received ''"):
            await async_client.datasources.meta.with_raw_response.create(
                datasource_id="",
                body=None,
            )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncAsktable) -> None:
        meta = await async_client.datasources.meta.retrieve(
            "datasource_id",
        )
        assert_matches_type(Meta, meta, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncAsktable) -> None:
        response = await async_client.datasources.meta.with_raw_response.retrieve(
            "datasource_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        meta = await response.parse()
        assert_matches_type(Meta, meta, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncAsktable) -> None:
        async with async_client.datasources.meta.with_streaming_response.retrieve(
            "datasource_id",
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
                "",
            )

    @parametrize
    async def test_method_update_overload_1(self, async_client: AsyncAsktable) -> None:
        meta = await async_client.datasources.meta.update(
            datasource_id="datasource_id",
            name="name",
        )
        assert_matches_type(object, meta, path=["response"])

    @parametrize
    async def test_method_update_with_all_params_overload_1(self, async_client: AsyncAsktable) -> None:
        meta = await async_client.datasources.meta.update(
            datasource_id="datasource_id",
            name="name",
            schemas={
                "foo": {
                    "name": "name",
                    "custom_configs": {},
                    "origin_desc": "origin_desc",
                    "tables": {
                        "foo": {
                            "name": "name",
                            "fields": {
                                "foo": {
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
    async def test_raw_response_update_overload_1(self, async_client: AsyncAsktable) -> None:
        response = await async_client.datasources.meta.with_raw_response.update(
            datasource_id="datasource_id",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        meta = await response.parse()
        assert_matches_type(object, meta, path=["response"])

    @parametrize
    async def test_streaming_response_update_overload_1(self, async_client: AsyncAsktable) -> None:
        async with async_client.datasources.meta.with_streaming_response.update(
            datasource_id="datasource_id",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            meta = await response.parse()
            assert_matches_type(object, meta, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_overload_1(self, async_client: AsyncAsktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `datasource_id` but received ''"):
            await async_client.datasources.meta.with_raw_response.update(
                datasource_id="",
                name="name",
            )

    @parametrize
    async def test_method_update_overload_2(self, async_client: AsyncAsktable) -> None:
        meta = await async_client.datasources.meta.update(
            datasource_id="datasource_id",
            body=None,
        )
        assert_matches_type(object, meta, path=["response"])

    @parametrize
    async def test_raw_response_update_overload_2(self, async_client: AsyncAsktable) -> None:
        response = await async_client.datasources.meta.with_raw_response.update(
            datasource_id="datasource_id",
            body=None,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        meta = await response.parse()
        assert_matches_type(object, meta, path=["response"])

    @parametrize
    async def test_streaming_response_update_overload_2(self, async_client: AsyncAsktable) -> None:
        async with async_client.datasources.meta.with_streaming_response.update(
            datasource_id="datasource_id",
            body=None,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            meta = await response.parse()
            assert_matches_type(object, meta, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_overload_2(self, async_client: AsyncAsktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `datasource_id` but received ''"):
            await async_client.datasources.meta.with_raw_response.update(
                datasource_id="",
                body=None,
            )

    @parametrize
    async def test_method_annotate(self, async_client: AsyncAsktable) -> None:
        meta = await async_client.datasources.meta.annotate(
            datasource_id="datasource_id",
            schemas={"foo": {"tables": {"foo": {"fields": {"foo": "string"}}}}},
        )
        assert_matches_type(object, meta, path=["response"])

    @parametrize
    async def test_raw_response_annotate(self, async_client: AsyncAsktable) -> None:
        response = await async_client.datasources.meta.with_raw_response.annotate(
            datasource_id="datasource_id",
            schemas={"foo": {"tables": {"foo": {"fields": {"foo": "string"}}}}},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        meta = await response.parse()
        assert_matches_type(object, meta, path=["response"])

    @parametrize
    async def test_streaming_response_annotate(self, async_client: AsyncAsktable) -> None:
        async with async_client.datasources.meta.with_streaming_response.annotate(
            datasource_id="datasource_id",
            schemas={"foo": {"tables": {"foo": {"fields": {"foo": "string"}}}}},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            meta = await response.parse()
            assert_matches_type(object, meta, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_annotate(self, async_client: AsyncAsktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `datasource_id` but received ''"):
            await async_client.datasources.meta.with_raw_response.annotate(
                datasource_id="",
                schemas={"foo": {"tables": {"foo": {"fields": {"foo": "string"}}}}},
            )
