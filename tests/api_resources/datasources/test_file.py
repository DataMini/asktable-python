# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from asktable import Asktable, AsyncAsktable
from tests.utils import assert_matches_type
from asktable.types import DataSource

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFile:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Asktable) -> None:
        file = client.datasources.file.create(
            name="name",
            file=b"raw file contents",
        )
        assert_matches_type(DataSource, file, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Asktable) -> None:
        file = client.datasources.file.create(
            name="name",
            file=b"raw file contents",
            async_process_meta=True,
            skip_process_meta=True,
        )
        assert_matches_type(DataSource, file, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Asktable) -> None:
        response = client.datasources.file.with_raw_response.create(
            name="name",
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(DataSource, file, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Asktable) -> None:
        with client.datasources.file.with_streaming_response.create(
            name="name",
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(DataSource, file, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFile:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncAsktable) -> None:
        file = await async_client.datasources.file.create(
            name="name",
            file=b"raw file contents",
        )
        assert_matches_type(DataSource, file, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncAsktable) -> None:
        file = await async_client.datasources.file.create(
            name="name",
            file=b"raw file contents",
            async_process_meta=True,
            skip_process_meta=True,
        )
        assert_matches_type(DataSource, file, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncAsktable) -> None:
        response = await async_client.datasources.file.with_raw_response.create(
            name="name",
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(DataSource, file, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncAsktable) -> None:
        async with async_client.datasources.file.with_streaming_response.create(
            name="name",
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(DataSource, file, path=["response"])

        assert cast(Any, response.is_closed) is True
