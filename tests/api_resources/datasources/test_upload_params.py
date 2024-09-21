# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from asktable import Asktable, AsyncAsktable
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUploadParams:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Asktable) -> None:
        upload_param = client.datasources.upload_params.create()
        assert_matches_type(object, upload_param, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Asktable) -> None:
        upload_param = client.datasources.upload_params.create(
            expiration=60,
            file_max_size=524288000,
        )
        assert_matches_type(object, upload_param, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Asktable) -> None:
        response = client.datasources.upload_params.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload_param = response.parse()
        assert_matches_type(object, upload_param, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Asktable) -> None:
        with client.datasources.upload_params.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload_param = response.parse()
            assert_matches_type(object, upload_param, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncUploadParams:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncAsktable) -> None:
        upload_param = await async_client.datasources.upload_params.create()
        assert_matches_type(object, upload_param, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncAsktable) -> None:
        upload_param = await async_client.datasources.upload_params.create(
            expiration=60,
            file_max_size=524288000,
        )
        assert_matches_type(object, upload_param, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncAsktable) -> None:
        response = await async_client.datasources.upload_params.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload_param = await response.parse()
        assert_matches_type(object, upload_param, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncAsktable) -> None:
        async with async_client.datasources.upload_params.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload_param = await response.parse()
            assert_matches_type(object, upload_param, path=["response"])

        assert cast(Any, response.is_closed) is True
