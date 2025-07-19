# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

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
from ...types.ats import test_case_list_params, test_case_create_params, test_case_update_params
from ...pagination import SyncPage, AsyncPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.ats.test_case_list_response import TestCaseListResponse
from ...types.ats.test_case_create_response import TestCaseCreateResponse
from ...types.ats.test_case_update_response import TestCaseUpdateResponse
from ...types.ats.test_case_retrieve_response import TestCaseRetrieveResponse

__all__ = ["TestCaseResource", "AsyncTestCaseResource"]


class TestCaseResource(SyncAPIResource):
    __test__ = False

    @cached_property
    def with_raw_response(self) -> TestCaseResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DataMini/asktable-python#accessing-raw-response-data-eg-headers
        """
        return TestCaseResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TestCaseResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DataMini/asktable-python#with_streaming_response
        """
        return TestCaseResourceWithStreamingResponse(self)

    def create(
        self,
        ats_id: str,
        *,
        expected_sql: str,
        question: str,
        role_id: Optional[str] | NotGiven = NOT_GIVEN,
        role_variables: Optional[object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TestCaseCreateResponse:
        """
        Create Test Case Endpoint

        Args:
          expected_sql: 用户期望生成的 sql

          question: 用户提问

          role_id: 角色 ID

          role_variables: 在扮演这个角色时需要传递的变量值，用 Key-Value 形式传递

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ats_id:
            raise ValueError(f"Expected a non-empty value for `ats_id` but received {ats_id!r}")
        return self._post(
            f"/v1/ats/{ats_id}/test-case",
            body=maybe_transform(
                {
                    "expected_sql": expected_sql,
                    "question": question,
                    "role_id": role_id,
                    "role_variables": role_variables,
                },
                test_case_create_params.TestCaseCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TestCaseCreateResponse,
        )

    def retrieve(
        self,
        atc_id: str,
        *,
        ats_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TestCaseRetrieveResponse:
        """
        Get Test Case Endpoint

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ats_id:
            raise ValueError(f"Expected a non-empty value for `ats_id` but received {ats_id!r}")
        if not atc_id:
            raise ValueError(f"Expected a non-empty value for `atc_id` but received {atc_id!r}")
        return self._get(
            f"/v1/ats/{ats_id}/test-case/{atc_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TestCaseRetrieveResponse,
        )

    def update(
        self,
        atc_id: str,
        *,
        ats_id: str,
        expected_sql: str,
        question: str,
        role_id: Optional[str] | NotGiven = NOT_GIVEN,
        role_variables: Optional[object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TestCaseUpdateResponse:
        """
        Update Test Case Endpoint

        Args:
          expected_sql: 用户期望生成的 sql

          question: 用户提问

          role_id: 角色 ID

          role_variables: 在扮演这个角色时需要传递的变量值，用 Key-Value 形式传递

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ats_id:
            raise ValueError(f"Expected a non-empty value for `ats_id` but received {ats_id!r}")
        if not atc_id:
            raise ValueError(f"Expected a non-empty value for `atc_id` but received {atc_id!r}")
        return self._patch(
            f"/v1/ats/{ats_id}/test-case/{atc_id}",
            body=maybe_transform(
                {
                    "expected_sql": expected_sql,
                    "question": question,
                    "role_id": role_id,
                    "role_variables": role_variables,
                },
                test_case_update_params.TestCaseUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TestCaseUpdateResponse,
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
    ) -> SyncPage[TestCaseListResponse]:
        """
        Get Test Cases Endpoint

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
            f"/v1/ats/{ats_id}/test-case",
            page=SyncPage[TestCaseListResponse],
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
                    test_case_list_params.TestCaseListParams,
                ),
            ),
            model=TestCaseListResponse,
        )

    def delete(
        self,
        atc_id: str,
        *,
        ats_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Delete Test Case Endpoint

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ats_id:
            raise ValueError(f"Expected a non-empty value for `ats_id` but received {ats_id!r}")
        if not atc_id:
            raise ValueError(f"Expected a non-empty value for `atc_id` but received {atc_id!r}")
        return self._delete(
            f"/v1/ats/{ats_id}/test-case/{atc_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncTestCaseResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTestCaseResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DataMini/asktable-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTestCaseResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTestCaseResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DataMini/asktable-python#with_streaming_response
        """
        return AsyncTestCaseResourceWithStreamingResponse(self)

    async def create(
        self,
        ats_id: str,
        *,
        expected_sql: str,
        question: str,
        role_id: Optional[str] | NotGiven = NOT_GIVEN,
        role_variables: Optional[object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TestCaseCreateResponse:
        """
        Create Test Case Endpoint

        Args:
          expected_sql: 用户期望生成的 sql

          question: 用户提问

          role_id: 角色 ID

          role_variables: 在扮演这个角色时需要传递的变量值，用 Key-Value 形式传递

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ats_id:
            raise ValueError(f"Expected a non-empty value for `ats_id` but received {ats_id!r}")
        return await self._post(
            f"/v1/ats/{ats_id}/test-case",
            body=await async_maybe_transform(
                {
                    "expected_sql": expected_sql,
                    "question": question,
                    "role_id": role_id,
                    "role_variables": role_variables,
                },
                test_case_create_params.TestCaseCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TestCaseCreateResponse,
        )

    async def retrieve(
        self,
        atc_id: str,
        *,
        ats_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TestCaseRetrieveResponse:
        """
        Get Test Case Endpoint

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ats_id:
            raise ValueError(f"Expected a non-empty value for `ats_id` but received {ats_id!r}")
        if not atc_id:
            raise ValueError(f"Expected a non-empty value for `atc_id` but received {atc_id!r}")
        return await self._get(
            f"/v1/ats/{ats_id}/test-case/{atc_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TestCaseRetrieveResponse,
        )

    async def update(
        self,
        atc_id: str,
        *,
        ats_id: str,
        expected_sql: str,
        question: str,
        role_id: Optional[str] | NotGiven = NOT_GIVEN,
        role_variables: Optional[object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TestCaseUpdateResponse:
        """
        Update Test Case Endpoint

        Args:
          expected_sql: 用户期望生成的 sql

          question: 用户提问

          role_id: 角色 ID

          role_variables: 在扮演这个角色时需要传递的变量值，用 Key-Value 形式传递

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ats_id:
            raise ValueError(f"Expected a non-empty value for `ats_id` but received {ats_id!r}")
        if not atc_id:
            raise ValueError(f"Expected a non-empty value for `atc_id` but received {atc_id!r}")
        return await self._patch(
            f"/v1/ats/{ats_id}/test-case/{atc_id}",
            body=await async_maybe_transform(
                {
                    "expected_sql": expected_sql,
                    "question": question,
                    "role_id": role_id,
                    "role_variables": role_variables,
                },
                test_case_update_params.TestCaseUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TestCaseUpdateResponse,
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
    ) -> AsyncPaginator[TestCaseListResponse, AsyncPage[TestCaseListResponse]]:
        """
        Get Test Cases Endpoint

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
            f"/v1/ats/{ats_id}/test-case",
            page=AsyncPage[TestCaseListResponse],
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
                    test_case_list_params.TestCaseListParams,
                ),
            ),
            model=TestCaseListResponse,
        )

    async def delete(
        self,
        atc_id: str,
        *,
        ats_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Delete Test Case Endpoint

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ats_id:
            raise ValueError(f"Expected a non-empty value for `ats_id` but received {ats_id!r}")
        if not atc_id:
            raise ValueError(f"Expected a non-empty value for `atc_id` but received {atc_id!r}")
        return await self._delete(
            f"/v1/ats/{ats_id}/test-case/{atc_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class TestCaseResourceWithRawResponse:
    __test__ = False

    def __init__(self, test_case: TestCaseResource) -> None:
        self._test_case = test_case

        self.create = to_raw_response_wrapper(
            test_case.create,
        )
        self.retrieve = to_raw_response_wrapper(
            test_case.retrieve,
        )
        self.update = to_raw_response_wrapper(
            test_case.update,
        )
        self.list = to_raw_response_wrapper(
            test_case.list,
        )
        self.delete = to_raw_response_wrapper(
            test_case.delete,
        )


class AsyncTestCaseResourceWithRawResponse:
    def __init__(self, test_case: AsyncTestCaseResource) -> None:
        self._test_case = test_case

        self.create = async_to_raw_response_wrapper(
            test_case.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            test_case.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            test_case.update,
        )
        self.list = async_to_raw_response_wrapper(
            test_case.list,
        )
        self.delete = async_to_raw_response_wrapper(
            test_case.delete,
        )


class TestCaseResourceWithStreamingResponse:
    __test__ = False

    def __init__(self, test_case: TestCaseResource) -> None:
        self._test_case = test_case

        self.create = to_streamed_response_wrapper(
            test_case.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            test_case.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            test_case.update,
        )
        self.list = to_streamed_response_wrapper(
            test_case.list,
        )
        self.delete = to_streamed_response_wrapper(
            test_case.delete,
        )


class AsyncTestCaseResourceWithStreamingResponse:
    def __init__(self, test_case: AsyncTestCaseResource) -> None:
        self._test_case = test_case

        self.create = async_to_streamed_response_wrapper(
            test_case.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            test_case.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            test_case.update,
        )
        self.list = async_to_streamed_response_wrapper(
            test_case.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            test_case.delete,
        )
