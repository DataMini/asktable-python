# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from asktable import Asktable, AsyncAsktable
from tests.utils import assert_matches_type
from asktable.types.ats import (
    TaskRunResponse,
    TaskListResponse,
    TaskRetrieveResponse,
    TaskGetCaseTasksResponse,
)
from asktable.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTask:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Asktable) -> None:
        task = client.ats.task.retrieve(
            ats_task_id="ats_task_id",
            ats_id="ats_id",
        )
        assert_matches_type(TaskRetrieveResponse, task, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Asktable) -> None:
        response = client.ats.task.with_raw_response.retrieve(
            ats_task_id="ats_task_id",
            ats_id="ats_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = response.parse()
        assert_matches_type(TaskRetrieveResponse, task, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Asktable) -> None:
        with client.ats.task.with_streaming_response.retrieve(
            ats_task_id="ats_task_id",
            ats_id="ats_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = response.parse()
            assert_matches_type(TaskRetrieveResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Asktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ats_id` but received ''"):
            client.ats.task.with_raw_response.retrieve(
                ats_task_id="ats_task_id",
                ats_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ats_task_id` but received ''"):
            client.ats.task.with_raw_response.retrieve(
                ats_task_id="",
                ats_id="ats_id",
            )

    @parametrize
    def test_method_list(self, client: Asktable) -> None:
        task = client.ats.task.list(
            ats_id="ats_id",
        )
        assert_matches_type(SyncPage[TaskListResponse], task, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Asktable) -> None:
        task = client.ats.task.list(
            ats_id="ats_id",
            page=1,
            size=1,
        )
        assert_matches_type(SyncPage[TaskListResponse], task, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Asktable) -> None:
        response = client.ats.task.with_raw_response.list(
            ats_id="ats_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = response.parse()
        assert_matches_type(SyncPage[TaskListResponse], task, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Asktable) -> None:
        with client.ats.task.with_streaming_response.list(
            ats_id="ats_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = response.parse()
            assert_matches_type(SyncPage[TaskListResponse], task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Asktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ats_id` but received ''"):
            client.ats.task.with_raw_response.list(
                ats_id="",
            )

    @parametrize
    def test_method_get_case_tasks(self, client: Asktable) -> None:
        task = client.ats.task.get_case_tasks(
            ats_task_id="ats_task_id",
            ats_id="ats_id",
        )
        assert_matches_type(TaskGetCaseTasksResponse, task, path=["response"])

    @parametrize
    def test_method_get_case_tasks_with_all_params(self, client: Asktable) -> None:
        task = client.ats.task.get_case_tasks(
            ats_task_id="ats_task_id",
            ats_id="ats_id",
            page=1,
            size=1,
        )
        assert_matches_type(TaskGetCaseTasksResponse, task, path=["response"])

    @parametrize
    def test_raw_response_get_case_tasks(self, client: Asktable) -> None:
        response = client.ats.task.with_raw_response.get_case_tasks(
            ats_task_id="ats_task_id",
            ats_id="ats_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = response.parse()
        assert_matches_type(TaskGetCaseTasksResponse, task, path=["response"])

    @parametrize
    def test_streaming_response_get_case_tasks(self, client: Asktable) -> None:
        with client.ats.task.with_streaming_response.get_case_tasks(
            ats_task_id="ats_task_id",
            ats_id="ats_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = response.parse()
            assert_matches_type(TaskGetCaseTasksResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_case_tasks(self, client: Asktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ats_id` but received ''"):
            client.ats.task.with_raw_response.get_case_tasks(
                ats_task_id="ats_task_id",
                ats_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ats_task_id` but received ''"):
            client.ats.task.with_raw_response.get_case_tasks(
                ats_task_id="",
                ats_id="ats_id",
            )

    @parametrize
    def test_method_run(self, client: Asktable) -> None:
        task = client.ats.task.run(
            ats_id="ats_id",
            datasource_id="datasource_id",
            specific_case_ids=["string"],
        )
        assert_matches_type(TaskRunResponse, task, path=["response"])

    @parametrize
    def test_raw_response_run(self, client: Asktable) -> None:
        response = client.ats.task.with_raw_response.run(
            ats_id="ats_id",
            datasource_id="datasource_id",
            specific_case_ids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = response.parse()
        assert_matches_type(TaskRunResponse, task, path=["response"])

    @parametrize
    def test_streaming_response_run(self, client: Asktable) -> None:
        with client.ats.task.with_streaming_response.run(
            ats_id="ats_id",
            datasource_id="datasource_id",
            specific_case_ids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = response.parse()
            assert_matches_type(TaskRunResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_run(self, client: Asktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ats_id` but received ''"):
            client.ats.task.with_raw_response.run(
                ats_id="",
                datasource_id="datasource_id",
                specific_case_ids=["string"],
            )


class TestAsyncTask:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncAsktable) -> None:
        task = await async_client.ats.task.retrieve(
            ats_task_id="ats_task_id",
            ats_id="ats_id",
        )
        assert_matches_type(TaskRetrieveResponse, task, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncAsktable) -> None:
        response = await async_client.ats.task.with_raw_response.retrieve(
            ats_task_id="ats_task_id",
            ats_id="ats_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = await response.parse()
        assert_matches_type(TaskRetrieveResponse, task, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncAsktable) -> None:
        async with async_client.ats.task.with_streaming_response.retrieve(
            ats_task_id="ats_task_id",
            ats_id="ats_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = await response.parse()
            assert_matches_type(TaskRetrieveResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncAsktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ats_id` but received ''"):
            await async_client.ats.task.with_raw_response.retrieve(
                ats_task_id="ats_task_id",
                ats_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ats_task_id` but received ''"):
            await async_client.ats.task.with_raw_response.retrieve(
                ats_task_id="",
                ats_id="ats_id",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncAsktable) -> None:
        task = await async_client.ats.task.list(
            ats_id="ats_id",
        )
        assert_matches_type(AsyncPage[TaskListResponse], task, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncAsktable) -> None:
        task = await async_client.ats.task.list(
            ats_id="ats_id",
            page=1,
            size=1,
        )
        assert_matches_type(AsyncPage[TaskListResponse], task, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncAsktable) -> None:
        response = await async_client.ats.task.with_raw_response.list(
            ats_id="ats_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = await response.parse()
        assert_matches_type(AsyncPage[TaskListResponse], task, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncAsktable) -> None:
        async with async_client.ats.task.with_streaming_response.list(
            ats_id="ats_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = await response.parse()
            assert_matches_type(AsyncPage[TaskListResponse], task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncAsktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ats_id` but received ''"):
            await async_client.ats.task.with_raw_response.list(
                ats_id="",
            )

    @parametrize
    async def test_method_get_case_tasks(self, async_client: AsyncAsktable) -> None:
        task = await async_client.ats.task.get_case_tasks(
            ats_task_id="ats_task_id",
            ats_id="ats_id",
        )
        assert_matches_type(TaskGetCaseTasksResponse, task, path=["response"])

    @parametrize
    async def test_method_get_case_tasks_with_all_params(self, async_client: AsyncAsktable) -> None:
        task = await async_client.ats.task.get_case_tasks(
            ats_task_id="ats_task_id",
            ats_id="ats_id",
            page=1,
            size=1,
        )
        assert_matches_type(TaskGetCaseTasksResponse, task, path=["response"])

    @parametrize
    async def test_raw_response_get_case_tasks(self, async_client: AsyncAsktable) -> None:
        response = await async_client.ats.task.with_raw_response.get_case_tasks(
            ats_task_id="ats_task_id",
            ats_id="ats_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = await response.parse()
        assert_matches_type(TaskGetCaseTasksResponse, task, path=["response"])

    @parametrize
    async def test_streaming_response_get_case_tasks(self, async_client: AsyncAsktable) -> None:
        async with async_client.ats.task.with_streaming_response.get_case_tasks(
            ats_task_id="ats_task_id",
            ats_id="ats_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = await response.parse()
            assert_matches_type(TaskGetCaseTasksResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_case_tasks(self, async_client: AsyncAsktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ats_id` but received ''"):
            await async_client.ats.task.with_raw_response.get_case_tasks(
                ats_task_id="ats_task_id",
                ats_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ats_task_id` but received ''"):
            await async_client.ats.task.with_raw_response.get_case_tasks(
                ats_task_id="",
                ats_id="ats_id",
            )

    @parametrize
    async def test_method_run(self, async_client: AsyncAsktable) -> None:
        task = await async_client.ats.task.run(
            ats_id="ats_id",
            datasource_id="datasource_id",
            specific_case_ids=["string"],
        )
        assert_matches_type(TaskRunResponse, task, path=["response"])

    @parametrize
    async def test_raw_response_run(self, async_client: AsyncAsktable) -> None:
        response = await async_client.ats.task.with_raw_response.run(
            ats_id="ats_id",
            datasource_id="datasource_id",
            specific_case_ids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = await response.parse()
        assert_matches_type(TaskRunResponse, task, path=["response"])

    @parametrize
    async def test_streaming_response_run(self, async_client: AsyncAsktable) -> None:
        async with async_client.ats.task.with_streaming_response.run(
            ats_id="ats_id",
            datasource_id="datasource_id",
            specific_case_ids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = await response.parse()
            assert_matches_type(TaskRunResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_run(self, async_client: AsyncAsktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ats_id` but received ''"):
            await async_client.ats.task.with_raw_response.run(
                ats_id="",
                datasource_id="datasource_id",
                specific_case_ids=["string"],
            )
