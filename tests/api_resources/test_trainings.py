# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from asktable import Asktable, AsyncAsktable
from tests.utils import assert_matches_type
from asktable.types import (
    TrainingListResponse,
    TrainingCreateResponse,
)
from asktable.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTrainings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Asktable) -> None:
        training = client.trainings.create(
            datasource_id="datasource_id",
            body=[
                {
                    "question": "question",
                    "sql": "sql",
                }
            ],
        )
        assert_matches_type(TrainingCreateResponse, training, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Asktable) -> None:
        response = client.trainings.with_raw_response.create(
            datasource_id="datasource_id",
            body=[
                {
                    "question": "question",
                    "sql": "sql",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        training = response.parse()
        assert_matches_type(TrainingCreateResponse, training, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Asktable) -> None:
        with client.trainings.with_streaming_response.create(
            datasource_id="datasource_id",
            body=[
                {
                    "question": "question",
                    "sql": "sql",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            training = response.parse()
            assert_matches_type(TrainingCreateResponse, training, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Asktable) -> None:
        training = client.trainings.list(
            datasource_id="datasource_id",
        )
        assert_matches_type(SyncPage[TrainingListResponse], training, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Asktable) -> None:
        training = client.trainings.list(
            datasource_id="datasource_id",
            page=1,
            size=1,
        )
        assert_matches_type(SyncPage[TrainingListResponse], training, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Asktable) -> None:
        response = client.trainings.with_raw_response.list(
            datasource_id="datasource_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        training = response.parse()
        assert_matches_type(SyncPage[TrainingListResponse], training, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Asktable) -> None:
        with client.trainings.with_streaming_response.list(
            datasource_id="datasource_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            training = response.parse()
            assert_matches_type(SyncPage[TrainingListResponse], training, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Asktable) -> None:
        training = client.trainings.delete(
            id="id",
            datasource_id="datasource_id",
        )
        assert_matches_type(object, training, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Asktable) -> None:
        response = client.trainings.with_raw_response.delete(
            id="id",
            datasource_id="datasource_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        training = response.parse()
        assert_matches_type(object, training, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Asktable) -> None:
        with client.trainings.with_streaming_response.delete(
            id="id",
            datasource_id="datasource_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            training = response.parse()
            assert_matches_type(object, training, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Asktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.trainings.with_raw_response.delete(
                id="",
                datasource_id="datasource_id",
            )


class TestAsyncTrainings:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncAsktable) -> None:
        training = await async_client.trainings.create(
            datasource_id="datasource_id",
            body=[
                {
                    "question": "question",
                    "sql": "sql",
                }
            ],
        )
        assert_matches_type(TrainingCreateResponse, training, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncAsktable) -> None:
        response = await async_client.trainings.with_raw_response.create(
            datasource_id="datasource_id",
            body=[
                {
                    "question": "question",
                    "sql": "sql",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        training = await response.parse()
        assert_matches_type(TrainingCreateResponse, training, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncAsktable) -> None:
        async with async_client.trainings.with_streaming_response.create(
            datasource_id="datasource_id",
            body=[
                {
                    "question": "question",
                    "sql": "sql",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            training = await response.parse()
            assert_matches_type(TrainingCreateResponse, training, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncAsktable) -> None:
        training = await async_client.trainings.list(
            datasource_id="datasource_id",
        )
        assert_matches_type(AsyncPage[TrainingListResponse], training, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncAsktable) -> None:
        training = await async_client.trainings.list(
            datasource_id="datasource_id",
            page=1,
            size=1,
        )
        assert_matches_type(AsyncPage[TrainingListResponse], training, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncAsktable) -> None:
        response = await async_client.trainings.with_raw_response.list(
            datasource_id="datasource_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        training = await response.parse()
        assert_matches_type(AsyncPage[TrainingListResponse], training, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncAsktable) -> None:
        async with async_client.trainings.with_streaming_response.list(
            datasource_id="datasource_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            training = await response.parse()
            assert_matches_type(AsyncPage[TrainingListResponse], training, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncAsktable) -> None:
        training = await async_client.trainings.delete(
            id="id",
            datasource_id="datasource_id",
        )
        assert_matches_type(object, training, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncAsktable) -> None:
        response = await async_client.trainings.with_raw_response.delete(
            id="id",
            datasource_id="datasource_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        training = await response.parse()
        assert_matches_type(object, training, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncAsktable) -> None:
        async with async_client.trainings.with_streaming_response.delete(
            id="id",
            datasource_id="datasource_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            training = await response.parse()
            assert_matches_type(object, training, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncAsktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.trainings.with_raw_response.delete(
                id="",
                datasource_id="datasource_id",
            )
