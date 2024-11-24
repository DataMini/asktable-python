# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncPage, AsyncPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.single_turn import q2a_list_params, q2a_create_params
from ...types.single_turn.q2a_response import Q2aResponse

__all__ = ["Q2aResource", "AsyncQ2aResource"]


class Q2aResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> Q2aResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DataMini/asktable-python#accessing-raw-response-data-eg-headers
        """
        return Q2aResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> Q2aResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DataMini/asktable-python#with_streaming_response
        """
        return Q2aResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        datasource_id: str,
        question: str,
        max_rows: Optional[int] | NotGiven = NOT_GIVEN,
        role_id: Optional[str] | NotGiven = NOT_GIVEN,
        role_variables: Optional[object] | NotGiven = NOT_GIVEN,
        with_json: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Q2aResponse:
        """
        发起查询的请求

        Args:
          datasource_id: 数据源 ID

          question: 查询语句

          max_rows: 最大返回行数，默认为 0，即不限制返回行数

          role_id: 角色 ID，将扮演这个角色来执行对话，用于权限控制。若无，则跳过鉴权，即可查询所有
              数据

          role_variables: 在扮演这个角色时需要传递的变量值，用 Key-Value 形式传递

          with_json: 是否同时将数据，作为 json 格式的附件一起返回

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/single-turn/q2a",
            body=maybe_transform(
                {
                    "datasource_id": datasource_id,
                    "question": question,
                    "max_rows": max_rows,
                    "role_id": role_id,
                    "role_variables": role_variables,
                    "with_json": with_json,
                },
                q2a_create_params.Q2aCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Q2aResponse,
        )

    def list(
        self,
        *,
        datasource_id: Optional[str] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[Q2aResponse]:
        """
        获取所有的 Q2A 记录

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
            "/single-turn/q2a",
            page=SyncPage[Q2aResponse],
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
                    q2a_list_params.Q2aListParams,
                ),
            ),
            model=Q2aResponse,
        )


class AsyncQ2aResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncQ2aResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DataMini/asktable-python#accessing-raw-response-data-eg-headers
        """
        return AsyncQ2aResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncQ2aResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DataMini/asktable-python#with_streaming_response
        """
        return AsyncQ2aResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        datasource_id: str,
        question: str,
        max_rows: Optional[int] | NotGiven = NOT_GIVEN,
        role_id: Optional[str] | NotGiven = NOT_GIVEN,
        role_variables: Optional[object] | NotGiven = NOT_GIVEN,
        with_json: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Q2aResponse:
        """
        发起查询的请求

        Args:
          datasource_id: 数据源 ID

          question: 查询语句

          max_rows: 最大返回行数，默认为 0，即不限制返回行数

          role_id: 角色 ID，将扮演这个角色来执行对话，用于权限控制。若无，则跳过鉴权，即可查询所有
              数据

          role_variables: 在扮演这个角色时需要传递的变量值，用 Key-Value 形式传递

          with_json: 是否同时将数据，作为 json 格式的附件一起返回

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/single-turn/q2a",
            body=await async_maybe_transform(
                {
                    "datasource_id": datasource_id,
                    "question": question,
                    "max_rows": max_rows,
                    "role_id": role_id,
                    "role_variables": role_variables,
                    "with_json": with_json,
                },
                q2a_create_params.Q2aCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Q2aResponse,
        )

    def list(
        self,
        *,
        datasource_id: Optional[str] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Q2aResponse, AsyncPage[Q2aResponse]]:
        """
        获取所有的 Q2A 记录

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
            "/single-turn/q2a",
            page=AsyncPage[Q2aResponse],
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
                    q2a_list_params.Q2aListParams,
                ),
            ),
            model=Q2aResponse,
        )


class Q2aResourceWithRawResponse:
    def __init__(self, q2a: Q2aResource) -> None:
        self._q2a = q2a

        self.create = to_raw_response_wrapper(
            q2a.create,
        )
        self.list = to_raw_response_wrapper(
            q2a.list,
        )


class AsyncQ2aResourceWithRawResponse:
    def __init__(self, q2a: AsyncQ2aResource) -> None:
        self._q2a = q2a

        self.create = async_to_raw_response_wrapper(
            q2a.create,
        )
        self.list = async_to_raw_response_wrapper(
            q2a.list,
        )


class Q2aResourceWithStreamingResponse:
    def __init__(self, q2a: Q2aResource) -> None:
        self._q2a = q2a

        self.create = to_streamed_response_wrapper(
            q2a.create,
        )
        self.list = to_streamed_response_wrapper(
            q2a.list,
        )


class AsyncQ2aResourceWithStreamingResponse:
    def __init__(self, q2a: AsyncQ2aResource) -> None:
        self._q2a = q2a

        self.create = async_to_streamed_response_wrapper(
            q2a.create,
        )
        self.list = async_to_streamed_response_wrapper(
            q2a.list,
        )
