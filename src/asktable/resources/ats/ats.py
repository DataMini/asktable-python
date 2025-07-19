# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .task import (
    TaskResource,
    AsyncTaskResource,
    TaskResourceWithRawResponse,
    AsyncTaskResourceWithRawResponse,
    TaskResourceWithStreamingResponse,
    AsyncTaskResourceWithStreamingResponse,
)
from ...types import ats_list_params, ats_create_params, ats_delete_params, ats_update_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from .test_case import (
    TestCaseResource,
    AsyncTestCaseResource,
    TestCaseResourceWithRawResponse,
    AsyncTestCaseResourceWithRawResponse,
    TestCaseResourceWithStreamingResponse,
    AsyncTestCaseResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncPage, AsyncPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.ats_list_response import ATSListResponse
from ...types.ats_create_response import ATSCreateResponse
from ...types.ats_update_response import ATSUpdateResponse
from ...types.ats_retrieve_response import ATSRetrieveResponse

__all__ = ["ATSResource", "AsyncATSResource"]


class ATSResource(SyncAPIResource):
    @cached_property
    def test_case(self) -> TestCaseResource:
        return TestCaseResource(self._client)

    @cached_property
    def task(self) -> TaskResource:
        return TaskResource(self._client)

    @cached_property
    def with_raw_response(self) -> ATSResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DataMini/asktable-python#accessing-raw-response-data-eg-headers
        """
        return ATSResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ATSResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DataMini/asktable-python#with_streaming_response
        """
        return ATSResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        datasource_id: str,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ATSCreateResponse:
        """
        Create Test Set Endpoint

        Args:
          datasource_id: 该测试集对应数据源的 ID

          name: 测试集名称

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/ats",
            body=maybe_transform(
                {
                    "datasource_id": datasource_id,
                    "name": name,
                },
                ats_create_params.ATSCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ATSCreateResponse,
        )

    def retrieve(
        self,
        ats_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ATSRetrieveResponse:
        """
        Get Test Set Endpoint

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ats_id:
            raise ValueError(f"Expected a non-empty value for `ats_id` but received {ats_id!r}")
        return self._get(
            f"/v1/ats/{ats_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ATSRetrieveResponse,
        )

    def update(
        self,
        ats_id: str,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ATSUpdateResponse:
        """
        Update Test Set Endpoint

        Args:
          name: 测试集更新的名字

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ats_id:
            raise ValueError(f"Expected a non-empty value for `ats_id` but received {ats_id!r}")
        return self._patch(
            f"/v1/ats/{ats_id}",
            body=maybe_transform({"name": name}, ats_update_params.ATSUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ATSUpdateResponse,
        )

    def list(
        self,
        *,
        datasource_id: str,
        page: int | NotGiven = NOT_GIVEN,
        size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[ATSListResponse]:
        """
        Get Test Sets Endpoint

        Args:
          datasource_id: 数据源 ID

          page: Page number

          size: Page size

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/ats",
            page=SyncPage[ATSListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "datasource_id": datasource_id,
                        "page": page,
                        "size": size,
                    },
                    ats_list_params.ATSListParams,
                ),
            ),
            model=ATSListResponse,
        )

    def delete(
        self,
        ats_id: str,
        *,
        datasource_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Delete Test Set Endpoint

        Args:
          datasource_id: 数据源 ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ats_id:
            raise ValueError(f"Expected a non-empty value for `ats_id` but received {ats_id!r}")
        return self._delete(
            f"/v1/ats/{ats_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"datasource_id": datasource_id}, ats_delete_params.ATSDeleteParams),
            ),
            cast_to=object,
        )


class AsyncATSResource(AsyncAPIResource):
    @cached_property
    def test_case(self) -> AsyncTestCaseResource:
        return AsyncTestCaseResource(self._client)

    @cached_property
    def task(self) -> AsyncTaskResource:
        return AsyncTaskResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncATSResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DataMini/asktable-python#accessing-raw-response-data-eg-headers
        """
        return AsyncATSResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncATSResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DataMini/asktable-python#with_streaming_response
        """
        return AsyncATSResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        datasource_id: str,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ATSCreateResponse:
        """
        Create Test Set Endpoint

        Args:
          datasource_id: 该测试集对应数据源的 ID

          name: 测试集名称

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/ats",
            body=await async_maybe_transform(
                {
                    "datasource_id": datasource_id,
                    "name": name,
                },
                ats_create_params.ATSCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ATSCreateResponse,
        )

    async def retrieve(
        self,
        ats_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ATSRetrieveResponse:
        """
        Get Test Set Endpoint

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ats_id:
            raise ValueError(f"Expected a non-empty value for `ats_id` but received {ats_id!r}")
        return await self._get(
            f"/v1/ats/{ats_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ATSRetrieveResponse,
        )

    async def update(
        self,
        ats_id: str,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ATSUpdateResponse:
        """
        Update Test Set Endpoint

        Args:
          name: 测试集更新的名字

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ats_id:
            raise ValueError(f"Expected a non-empty value for `ats_id` but received {ats_id!r}")
        return await self._patch(
            f"/v1/ats/{ats_id}",
            body=await async_maybe_transform({"name": name}, ats_update_params.ATSUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ATSUpdateResponse,
        )

    def list(
        self,
        *,
        datasource_id: str,
        page: int | NotGiven = NOT_GIVEN,
        size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[ATSListResponse, AsyncPage[ATSListResponse]]:
        """
        Get Test Sets Endpoint

        Args:
          datasource_id: 数据源 ID

          page: Page number

          size: Page size

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/ats",
            page=AsyncPage[ATSListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "datasource_id": datasource_id,
                        "page": page,
                        "size": size,
                    },
                    ats_list_params.ATSListParams,
                ),
            ),
            model=ATSListResponse,
        )

    async def delete(
        self,
        ats_id: str,
        *,
        datasource_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Delete Test Set Endpoint

        Args:
          datasource_id: 数据源 ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ats_id:
            raise ValueError(f"Expected a non-empty value for `ats_id` but received {ats_id!r}")
        return await self._delete(
            f"/v1/ats/{ats_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"datasource_id": datasource_id}, ats_delete_params.ATSDeleteParams),
            ),
            cast_to=object,
        )


class ATSResourceWithRawResponse:
    def __init__(self, ats: ATSResource) -> None:
        self._ats = ats

        self.create = to_raw_response_wrapper(
            ats.create,
        )
        self.retrieve = to_raw_response_wrapper(
            ats.retrieve,
        )
        self.update = to_raw_response_wrapper(
            ats.update,
        )
        self.list = to_raw_response_wrapper(
            ats.list,
        )
        self.delete = to_raw_response_wrapper(
            ats.delete,
        )

    @cached_property
    def test_case(self) -> TestCaseResourceWithRawResponse:
        return TestCaseResourceWithRawResponse(self._ats.test_case)

    @cached_property
    def task(self) -> TaskResourceWithRawResponse:
        return TaskResourceWithRawResponse(self._ats.task)


class AsyncATSResourceWithRawResponse:
    def __init__(self, ats: AsyncATSResource) -> None:
        self._ats = ats

        self.create = async_to_raw_response_wrapper(
            ats.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            ats.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            ats.update,
        )
        self.list = async_to_raw_response_wrapper(
            ats.list,
        )
        self.delete = async_to_raw_response_wrapper(
            ats.delete,
        )

    @cached_property
    def test_case(self) -> AsyncTestCaseResourceWithRawResponse:
        return AsyncTestCaseResourceWithRawResponse(self._ats.test_case)

    @cached_property
    def task(self) -> AsyncTaskResourceWithRawResponse:
        return AsyncTaskResourceWithRawResponse(self._ats.task)


class ATSResourceWithStreamingResponse:
    def __init__(self, ats: ATSResource) -> None:
        self._ats = ats

        self.create = to_streamed_response_wrapper(
            ats.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            ats.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            ats.update,
        )
        self.list = to_streamed_response_wrapper(
            ats.list,
        )
        self.delete = to_streamed_response_wrapper(
            ats.delete,
        )

    @cached_property
    def test_case(self) -> TestCaseResourceWithStreamingResponse:
        return TestCaseResourceWithStreamingResponse(self._ats.test_case)

    @cached_property
    def task(self) -> TaskResourceWithStreamingResponse:
        return TaskResourceWithStreamingResponse(self._ats.task)


class AsyncATSResourceWithStreamingResponse:
    def __init__(self, ats: AsyncATSResource) -> None:
        self._ats = ats

        self.create = async_to_streamed_response_wrapper(
            ats.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            ats.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            ats.update,
        )
        self.list = async_to_streamed_response_wrapper(
            ats.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            ats.delete,
        )

    @cached_property
    def test_case(self) -> AsyncTestCaseResourceWithStreamingResponse:
        return AsyncTestCaseResourceWithStreamingResponse(self._ats.test_case)

    @cached_property
    def task(self) -> AsyncTaskResourceWithStreamingResponse:
        return AsyncTaskResourceWithStreamingResponse(self._ats.task)
