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
from ...types.single_turn import q2_list_params, q2_create_params
from ...types.single_turn.q2s_response import Q2sResponse

__all__ = ["Q2sResource", "AsyncQ2sResource"]


class Q2sResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> Q2sResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DataMini/asktable-python#accessing-raw-response-data-eg-headers
        """
        return Q2sResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> Q2sResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DataMini/asktable-python#with_streaming_response
        """
        return Q2sResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        datasource_id: str,
        question: str,
        role_id: Optional[str] | NotGiven = NOT_GIVEN,
        role_variables: Optional[object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Q2sResponse:
        """
        发起生成 sql 的请求

        Args:
          datasource_id: 数据源 ID

          question: 查询语句

          role_id: 角色 ID，将扮演这个角色来执行对话，用于权限控制。若无，则跳过鉴权，即可查询所有
              数据

          role_variables: 在扮演这个角色时需要传递的变量值，用 Key-Value 形式传递

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/single-turn/q2s",
            body=maybe_transform(
                {
                    "datasource_id": datasource_id,
                    "question": question,
                    "role_id": role_id,
                    "role_variables": role_variables,
                },
                q2_create_params.Q2CreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Q2sResponse,
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
    ) -> SyncPage[Q2sResponse]:
        """
        获取所有的 Q2S 记录

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
            "/single-turn/q2s",
            page=SyncPage[Q2sResponse],
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
                    q2_list_params.Q2ListParams,
                ),
            ),
            model=Q2sResponse,
        )


class AsyncQ2sResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncQ2sResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DataMini/asktable-python#accessing-raw-response-data-eg-headers
        """
        return AsyncQ2sResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncQ2sResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DataMini/asktable-python#with_streaming_response
        """
        return AsyncQ2sResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        datasource_id: str,
        question: str,
        role_id: Optional[str] | NotGiven = NOT_GIVEN,
        role_variables: Optional[object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Q2sResponse:
        """
        发起生成 sql 的请求

        Args:
          datasource_id: 数据源 ID

          question: 查询语句

          role_id: 角色 ID，将扮演这个角色来执行对话，用于权限控制。若无，则跳过鉴权，即可查询所有
              数据

          role_variables: 在扮演这个角色时需要传递的变量值，用 Key-Value 形式传递

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/single-turn/q2s",
            body=await async_maybe_transform(
                {
                    "datasource_id": datasource_id,
                    "question": question,
                    "role_id": role_id,
                    "role_variables": role_variables,
                },
                q2_create_params.Q2CreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Q2sResponse,
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
    ) -> AsyncPaginator[Q2sResponse, AsyncPage[Q2sResponse]]:
        """
        获取所有的 Q2S 记录

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
            "/single-turn/q2s",
            page=AsyncPage[Q2sResponse],
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
                    q2_list_params.Q2ListParams,
                ),
            ),
            model=Q2sResponse,
        )


class Q2sResourceWithRawResponse:
    def __init__(self, q2s: Q2sResource) -> None:
        self._q2s = q2s

        self.create = to_raw_response_wrapper(
            q2s.create,
        )
        self.list = to_raw_response_wrapper(
            q2s.list,
        )


class AsyncQ2sResourceWithRawResponse:
    def __init__(self, q2s: AsyncQ2sResource) -> None:
        self._q2s = q2s

        self.create = async_to_raw_response_wrapper(
            q2s.create,
        )
        self.list = async_to_raw_response_wrapper(
            q2s.list,
        )


class Q2sResourceWithStreamingResponse:
    def __init__(self, q2s: Q2sResource) -> None:
        self._q2s = q2s

        self.create = to_streamed_response_wrapper(
            q2s.create,
        )
        self.list = to_streamed_response_wrapper(
            q2s.list,
        )


class AsyncQ2sResourceWithStreamingResponse:
    def __init__(self, q2s: AsyncQ2sResource) -> None:
        self._q2s = q2s

        self.create = async_to_streamed_response_wrapper(
            q2s.create,
        )
        self.list = async_to_streamed_response_wrapper(
            q2s.list,
        )
