# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from asktable import Asktable, AsyncAsktable
from tests.utils import assert_matches_type
from asktable.types import DataframeRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDataframes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Asktable) -> None:
        dataframe = client.dataframes.retrieve(
            "dataframe_id",
        )
        assert_matches_type(DataframeRetrieveResponse, dataframe, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Asktable) -> None:
        response = client.dataframes.with_raw_response.retrieve(
            "dataframe_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataframe = response.parse()
        assert_matches_type(DataframeRetrieveResponse, dataframe, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Asktable) -> None:
        with client.dataframes.with_streaming_response.retrieve(
            "dataframe_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataframe = response.parse()
            assert_matches_type(DataframeRetrieveResponse, dataframe, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Asktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataframe_id` but received ''"):
            client.dataframes.with_raw_response.retrieve(
                "",
            )


class TestAsyncDataframes:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncAsktable) -> None:
        dataframe = await async_client.dataframes.retrieve(
            "dataframe_id",
        )
        assert_matches_type(DataframeRetrieveResponse, dataframe, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncAsktable) -> None:
        response = await async_client.dataframes.with_raw_response.retrieve(
            "dataframe_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataframe = await response.parse()
        assert_matches_type(DataframeRetrieveResponse, dataframe, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncAsktable) -> None:
        async with async_client.dataframes.with_streaming_response.retrieve(
            "dataframe_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataframe = await response.parse()
            assert_matches_type(DataframeRetrieveResponse, dataframe, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncAsktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataframe_id` but received ''"):
            await async_client.dataframes.with_raw_response.retrieve(
                "",
            )
