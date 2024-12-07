# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from asktable import Asktable, AsyncAsktable
from tests.utils import assert_matches_type
from asktable.types import (
    Datasource,
)
from asktable.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDatasources:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Asktable) -> None:
        datasource = client.datasources.create(
            engine="mysql",
        )
        assert_matches_type(Datasource, datasource, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Asktable) -> None:
        datasource = client.datasources.create(
            engine="mysql",
            async_process_meta=True,
            value_index=True,
            access_config={
                "atst_link_id": "atst_link_123456",
                "db": "test",
                "db_version": "5.7",
                "host": "192.168.0.10",
                "location_type": "local",
                "location_url": "http://example.com/data.csv",
                "password": "root",
                "port": 3306,
                "proxy_host": "192.168.0.10",
                "proxy_port": 3306,
                "securetunnel_id": "atst_123456",
                "user": "root",
            },
            name="用户库",
        )
        assert_matches_type(Datasource, datasource, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Asktable) -> None:
        response = client.datasources.with_raw_response.create(
            engine="mysql",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        datasource = response.parse()
        assert_matches_type(Datasource, datasource, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Asktable) -> None:
        with client.datasources.with_streaming_response.create(
            engine="mysql",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            datasource = response.parse()
            assert_matches_type(Datasource, datasource, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Asktable) -> None:
        datasource = client.datasources.retrieve(
            "datasource_id",
        )
        assert_matches_type(Datasource, datasource, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Asktable) -> None:
        response = client.datasources.with_raw_response.retrieve(
            "datasource_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        datasource = response.parse()
        assert_matches_type(Datasource, datasource, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Asktable) -> None:
        with client.datasources.with_streaming_response.retrieve(
            "datasource_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            datasource = response.parse()
            assert_matches_type(Datasource, datasource, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Asktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `datasource_id` but received ''"):
            client.datasources.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Asktable) -> None:
        datasource = client.datasources.update(
            datasource_id="datasource_id",
        )
        assert_matches_type(Datasource, datasource, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Asktable) -> None:
        datasource = client.datasources.update(
            datasource_id="datasource_id",
            access_config={
                "atst_link_id": "atst_link_123456",
                "db": "test",
                "db_version": "5.7",
                "host": "192.168.0.10",
                "location_type": "local",
                "location_url": "http://example.com/data.csv",
                "password": "root",
                "port": 3306,
                "proxy_host": "192.168.0.10",
                "proxy_port": 3306,
                "securetunnel_id": "atst_123456",
                "user": "root",
            },
            desc="数据源描述",
            field_count=1,
            meta_error="error message",
            meta_status="processing",
            name="用户库",
            sample_questions="示例问题",
            schema_count=1,
            table_count=1,
        )
        assert_matches_type(Datasource, datasource, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Asktable) -> None:
        response = client.datasources.with_raw_response.update(
            datasource_id="datasource_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        datasource = response.parse()
        assert_matches_type(Datasource, datasource, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Asktable) -> None:
        with client.datasources.with_streaming_response.update(
            datasource_id="datasource_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            datasource = response.parse()
            assert_matches_type(Datasource, datasource, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Asktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `datasource_id` but received ''"):
            client.datasources.with_raw_response.update(
                datasource_id="",
            )

    @parametrize
    def test_method_list(self, client: Asktable) -> None:
        datasource = client.datasources.list()
        assert_matches_type(SyncPage[Datasource], datasource, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Asktable) -> None:
        datasource = client.datasources.list(
            name="name",
            page=1,
            size=1,
        )
        assert_matches_type(SyncPage[Datasource], datasource, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Asktable) -> None:
        response = client.datasources.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        datasource = response.parse()
        assert_matches_type(SyncPage[Datasource], datasource, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Asktable) -> None:
        with client.datasources.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            datasource = response.parse()
            assert_matches_type(SyncPage[Datasource], datasource, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Asktable) -> None:
        datasource = client.datasources.delete(
            "datasource_id",
        )
        assert_matches_type(object, datasource, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Asktable) -> None:
        response = client.datasources.with_raw_response.delete(
            "datasource_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        datasource = response.parse()
        assert_matches_type(object, datasource, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Asktable) -> None:
        with client.datasources.with_streaming_response.delete(
            "datasource_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            datasource = response.parse()
            assert_matches_type(object, datasource, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Asktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `datasource_id` but received ''"):
            client.datasources.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_create_from_file(self, client: Asktable) -> None:
        datasource = client.datasources.create_from_file(
            file=b"raw file contents",
        )
        assert_matches_type(Datasource, datasource, path=["response"])

    @parametrize
    def test_method_create_from_file_with_all_params(self, client: Asktable) -> None:
        datasource = client.datasources.create_from_file(
            file=b"raw file contents",
            async_process_meta=True,
            name="name",
            value_index=True,
        )
        assert_matches_type(Datasource, datasource, path=["response"])

    @parametrize
    def test_raw_response_create_from_file(self, client: Asktable) -> None:
        response = client.datasources.with_raw_response.create_from_file(
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        datasource = response.parse()
        assert_matches_type(Datasource, datasource, path=["response"])

    @parametrize
    def test_streaming_response_create_from_file(self, client: Asktable) -> None:
        with client.datasources.with_streaming_response.create_from_file(
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            datasource = response.parse()
            assert_matches_type(Datasource, datasource, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDatasources:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncAsktable) -> None:
        datasource = await async_client.datasources.create(
            engine="mysql",
        )
        assert_matches_type(Datasource, datasource, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncAsktable) -> None:
        datasource = await async_client.datasources.create(
            engine="mysql",
            async_process_meta=True,
            value_index=True,
            access_config={
                "atst_link_id": "atst_link_123456",
                "db": "test",
                "db_version": "5.7",
                "host": "192.168.0.10",
                "location_type": "local",
                "location_url": "http://example.com/data.csv",
                "password": "root",
                "port": 3306,
                "proxy_host": "192.168.0.10",
                "proxy_port": 3306,
                "securetunnel_id": "atst_123456",
                "user": "root",
            },
            name="用户库",
        )
        assert_matches_type(Datasource, datasource, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncAsktable) -> None:
        response = await async_client.datasources.with_raw_response.create(
            engine="mysql",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        datasource = await response.parse()
        assert_matches_type(Datasource, datasource, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncAsktable) -> None:
        async with async_client.datasources.with_streaming_response.create(
            engine="mysql",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            datasource = await response.parse()
            assert_matches_type(Datasource, datasource, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncAsktable) -> None:
        datasource = await async_client.datasources.retrieve(
            "datasource_id",
        )
        assert_matches_type(Datasource, datasource, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncAsktable) -> None:
        response = await async_client.datasources.with_raw_response.retrieve(
            "datasource_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        datasource = await response.parse()
        assert_matches_type(Datasource, datasource, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncAsktable) -> None:
        async with async_client.datasources.with_streaming_response.retrieve(
            "datasource_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            datasource = await response.parse()
            assert_matches_type(Datasource, datasource, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncAsktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `datasource_id` but received ''"):
            await async_client.datasources.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncAsktable) -> None:
        datasource = await async_client.datasources.update(
            datasource_id="datasource_id",
        )
        assert_matches_type(Datasource, datasource, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncAsktable) -> None:
        datasource = await async_client.datasources.update(
            datasource_id="datasource_id",
            access_config={
                "atst_link_id": "atst_link_123456",
                "db": "test",
                "db_version": "5.7",
                "host": "192.168.0.10",
                "location_type": "local",
                "location_url": "http://example.com/data.csv",
                "password": "root",
                "port": 3306,
                "proxy_host": "192.168.0.10",
                "proxy_port": 3306,
                "securetunnel_id": "atst_123456",
                "user": "root",
            },
            desc="数据源描述",
            field_count=1,
            meta_error="error message",
            meta_status="processing",
            name="用户库",
            sample_questions="示例问题",
            schema_count=1,
            table_count=1,
        )
        assert_matches_type(Datasource, datasource, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncAsktable) -> None:
        response = await async_client.datasources.with_raw_response.update(
            datasource_id="datasource_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        datasource = await response.parse()
        assert_matches_type(Datasource, datasource, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncAsktable) -> None:
        async with async_client.datasources.with_streaming_response.update(
            datasource_id="datasource_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            datasource = await response.parse()
            assert_matches_type(Datasource, datasource, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncAsktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `datasource_id` but received ''"):
            await async_client.datasources.with_raw_response.update(
                datasource_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncAsktable) -> None:
        datasource = await async_client.datasources.list()
        assert_matches_type(AsyncPage[Datasource], datasource, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncAsktable) -> None:
        datasource = await async_client.datasources.list(
            name="name",
            page=1,
            size=1,
        )
        assert_matches_type(AsyncPage[Datasource], datasource, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncAsktable) -> None:
        response = await async_client.datasources.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        datasource = await response.parse()
        assert_matches_type(AsyncPage[Datasource], datasource, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncAsktable) -> None:
        async with async_client.datasources.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            datasource = await response.parse()
            assert_matches_type(AsyncPage[Datasource], datasource, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncAsktable) -> None:
        datasource = await async_client.datasources.delete(
            "datasource_id",
        )
        assert_matches_type(object, datasource, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncAsktable) -> None:
        response = await async_client.datasources.with_raw_response.delete(
            "datasource_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        datasource = await response.parse()
        assert_matches_type(object, datasource, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncAsktable) -> None:
        async with async_client.datasources.with_streaming_response.delete(
            "datasource_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            datasource = await response.parse()
            assert_matches_type(object, datasource, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncAsktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `datasource_id` but received ''"):
            await async_client.datasources.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_create_from_file(self, async_client: AsyncAsktable) -> None:
        datasource = await async_client.datasources.create_from_file(
            file=b"raw file contents",
        )
        assert_matches_type(Datasource, datasource, path=["response"])

    @parametrize
    async def test_method_create_from_file_with_all_params(self, async_client: AsyncAsktable) -> None:
        datasource = await async_client.datasources.create_from_file(
            file=b"raw file contents",
            async_process_meta=True,
            name="name",
            value_index=True,
        )
        assert_matches_type(Datasource, datasource, path=["response"])

    @parametrize
    async def test_raw_response_create_from_file(self, async_client: AsyncAsktable) -> None:
        response = await async_client.datasources.with_raw_response.create_from_file(
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        datasource = await response.parse()
        assert_matches_type(Datasource, datasource, path=["response"])

    @parametrize
    async def test_streaming_response_create_from_file(self, async_client: AsyncAsktable) -> None:
        async with async_client.datasources.with_streaming_response.create_from_file(
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            datasource = await response.parse()
            assert_matches_type(Datasource, datasource, path=["response"])

        assert cast(Any, response.is_closed) is True
