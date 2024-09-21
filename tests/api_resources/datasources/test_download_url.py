# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from asktable import Asktable, AsyncAsktable
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDownloadURL:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Asktable) -> None:
        download_url = client.datasources.download_url.retrieve(
            "datasource_id",
        )
        assert_matches_type(object, download_url, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Asktable) -> None:
        response = client.datasources.download_url.with_raw_response.retrieve(
            "datasource_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        download_url = response.parse()
        assert_matches_type(object, download_url, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Asktable) -> None:
        with client.datasources.download_url.with_streaming_response.retrieve(
            "datasource_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            download_url = response.parse()
            assert_matches_type(object, download_url, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Asktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `datasource_id` but received ''"):
            client.datasources.download_url.with_raw_response.retrieve(
                "",
            )


class TestAsyncDownloadURL:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncAsktable) -> None:
        download_url = await async_client.datasources.download_url.retrieve(
            "datasource_id",
        )
        assert_matches_type(object, download_url, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncAsktable) -> None:
        response = await async_client.datasources.download_url.with_raw_response.retrieve(
            "datasource_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        download_url = await response.parse()
        assert_matches_type(object, download_url, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncAsktable) -> None:
        async with async_client.datasources.download_url.with_streaming_response.retrieve(
            "datasource_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            download_url = await response.parse()
            assert_matches_type(object, download_url, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncAsktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `datasource_id` but received ''"):
            await async_client.datasources.download_url.with_raw_response.retrieve(
                "",
            )
