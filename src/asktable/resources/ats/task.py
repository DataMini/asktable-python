# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.ats import task_run_params, task_list_params, task_get_case_tasks_params
from ...pagination import SyncPage, AsyncPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.ats.task_run_response import TaskRunResponse
from ...types.ats.task_list_response import TaskListResponse
from ...types.ats.task_retrieve_response import TaskRetrieveResponse
from ...types.ats.task_get_case_tasks_response import TaskGetCaseTasksResponse

__all__ = ["TaskResource", "AsyncTaskResource"]


class TaskResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TaskResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DataMini/asktable-python#accessing-raw-response-data-eg-headers
        """
        return TaskResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TaskResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DataMini/asktable-python#with_streaming_response
        """
        return TaskResourceWithStreamingResponse(self)

    def retrieve(
        self,
        ats_task_id: str,
        *,
        ats_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskRetrieveResponse:
        """
        Get Test Task Endpoint

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ats_id:
            raise ValueError(f"Expected a non-empty value for `ats_id` but received {ats_id!r}")
        if not ats_task_id:
            raise ValueError(f"Expected a non-empty value for `ats_task_id` but received {ats_task_id!r}")
        return self._get(
            f"/v1/ats/{ats_id}/task/{ats_task_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskRetrieveResponse,
        )

    def list(
        self,
        ats_id: str,
        *,
        page: int | NotGiven = NOT_GIVEN,
        size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[TaskListResponse]:
        """
        Get Test Tasks Endpoint

        Args:
          page: Page number

          size: Page size

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ats_id:
            raise ValueError(f"Expected a non-empty value for `ats_id` but received {ats_id!r}")
        return self._get_api_list(
            f"/v1/ats/{ats_id}/task",
            page=SyncPage[TaskListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "size": size,
                    },
                    task_list_params.TaskListParams,
                ),
            ),
            model=TaskListResponse,
        )

    def get_case_tasks(
        self,
        ats_task_id: str,
        *,
        ats_id: str,
        page: int | NotGiven = NOT_GIVEN,
        size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskGetCaseTasksResponse:
        """
        Get Test Case Tasks Endpoint

        Args:
          page: Page number

          size: Page size

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ats_id:
            raise ValueError(f"Expected a non-empty value for `ats_id` but received {ats_id!r}")
        if not ats_task_id:
            raise ValueError(f"Expected a non-empty value for `ats_task_id` but received {ats_task_id!r}")
        return self._get(
            f"/v1/ats/{ats_id}/task/{ats_task_id}/case",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "size": size,
                    },
                    task_get_case_tasks_params.TaskGetCaseTasksParams,
                ),
            ),
            cast_to=TaskGetCaseTasksResponse,
        )

    def run(
        self,
        ats_id: str,
        *,
        datasource_id: str,
        specific_case_ids: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskRunResponse:
        """
        Run Task Endpoint

        Args:
          datasource_id: 数据源 ID

          specific_case_ids: 测试用例 ID 列表

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ats_id:
            raise ValueError(f"Expected a non-empty value for `ats_id` but received {ats_id!r}")
        return self._post(
            f"/v1/ats/{ats_id}/task",
            body=maybe_transform(
                {
                    "datasource_id": datasource_id,
                    "specific_case_ids": specific_case_ids,
                },
                task_run_params.TaskRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskRunResponse,
        )


class AsyncTaskResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTaskResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DataMini/asktable-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTaskResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTaskResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DataMini/asktable-python#with_streaming_response
        """
        return AsyncTaskResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        ats_task_id: str,
        *,
        ats_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskRetrieveResponse:
        """
        Get Test Task Endpoint

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ats_id:
            raise ValueError(f"Expected a non-empty value for `ats_id` but received {ats_id!r}")
        if not ats_task_id:
            raise ValueError(f"Expected a non-empty value for `ats_task_id` but received {ats_task_id!r}")
        return await self._get(
            f"/v1/ats/{ats_id}/task/{ats_task_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskRetrieveResponse,
        )

    def list(
        self,
        ats_id: str,
        *,
        page: int | NotGiven = NOT_GIVEN,
        size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[TaskListResponse, AsyncPage[TaskListResponse]]:
        """
        Get Test Tasks Endpoint

        Args:
          page: Page number

          size: Page size

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ats_id:
            raise ValueError(f"Expected a non-empty value for `ats_id` but received {ats_id!r}")
        return self._get_api_list(
            f"/v1/ats/{ats_id}/task",
            page=AsyncPage[TaskListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "size": size,
                    },
                    task_list_params.TaskListParams,
                ),
            ),
            model=TaskListResponse,
        )

    async def get_case_tasks(
        self,
        ats_task_id: str,
        *,
        ats_id: str,
        page: int | NotGiven = NOT_GIVEN,
        size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskGetCaseTasksResponse:
        """
        Get Test Case Tasks Endpoint

        Args:
          page: Page number

          size: Page size

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ats_id:
            raise ValueError(f"Expected a non-empty value for `ats_id` but received {ats_id!r}")
        if not ats_task_id:
            raise ValueError(f"Expected a non-empty value for `ats_task_id` but received {ats_task_id!r}")
        return await self._get(
            f"/v1/ats/{ats_id}/task/{ats_task_id}/case",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "size": size,
                    },
                    task_get_case_tasks_params.TaskGetCaseTasksParams,
                ),
            ),
            cast_to=TaskGetCaseTasksResponse,
        )

    async def run(
        self,
        ats_id: str,
        *,
        datasource_id: str,
        specific_case_ids: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskRunResponse:
        """
        Run Task Endpoint

        Args:
          datasource_id: 数据源 ID

          specific_case_ids: 测试用例 ID 列表

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ats_id:
            raise ValueError(f"Expected a non-empty value for `ats_id` but received {ats_id!r}")
        return await self._post(
            f"/v1/ats/{ats_id}/task",
            body=await async_maybe_transform(
                {
                    "datasource_id": datasource_id,
                    "specific_case_ids": specific_case_ids,
                },
                task_run_params.TaskRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskRunResponse,
        )


class TaskResourceWithRawResponse:
    def __init__(self, task: TaskResource) -> None:
        self._task = task

        self.retrieve = to_raw_response_wrapper(
            task.retrieve,
        )
        self.list = to_raw_response_wrapper(
            task.list,
        )
        self.get_case_tasks = to_raw_response_wrapper(
            task.get_case_tasks,
        )
        self.run = to_raw_response_wrapper(
            task.run,
        )


class AsyncTaskResourceWithRawResponse:
    def __init__(self, task: AsyncTaskResource) -> None:
        self._task = task

        self.retrieve = async_to_raw_response_wrapper(
            task.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            task.list,
        )
        self.get_case_tasks = async_to_raw_response_wrapper(
            task.get_case_tasks,
        )
        self.run = async_to_raw_response_wrapper(
            task.run,
        )


class TaskResourceWithStreamingResponse:
    def __init__(self, task: TaskResource) -> None:
        self._task = task

        self.retrieve = to_streamed_response_wrapper(
            task.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            task.list,
        )
        self.get_case_tasks = to_streamed_response_wrapper(
            task.get_case_tasks,
        )
        self.run = to_streamed_response_wrapper(
            task.run,
        )


class AsyncTaskResourceWithStreamingResponse:
    def __init__(self, task: AsyncTaskResource) -> None:
        self._task = task

        self.retrieve = async_to_streamed_response_wrapper(
            task.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            task.list,
        )
        self.get_case_tasks = async_to_streamed_response_wrapper(
            task.get_case_tasks,
        )
        self.run = async_to_streamed_response_wrapper(
            task.run,
        )
