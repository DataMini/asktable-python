# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

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
from ...types.roles import variable_list_params
from ..._base_client import make_request_options

__all__ = ["VariablesResource", "AsyncVariablesResource"]


class VariablesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VariablesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DataMini/asktable-python#accessing-raw-response-data-eg-headers
        """
        return VariablesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VariablesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DataMini/asktable-python#with_streaming_response
        """
        return VariablesResourceWithStreamingResponse(self)

    def list(
        self,
        role_id: str,
        *,
        bot_id: Optional[str] | NotGiven = NOT_GIVEN,
        datasource_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        查询某个角色的所有变量

        Args:
          bot_id: Bot ID

          datasource_ids: 数据源 ID 列表

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not role_id:
            raise ValueError(f"Expected a non-empty value for `role_id` but received {role_id!r}")
        return self._get(
            f"/roles/{role_id}/variables",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "bot_id": bot_id,
                        "datasource_ids": datasource_ids,
                    },
                    variable_list_params.VariableListParams,
                ),
            ),
            cast_to=object,
        )


class AsyncVariablesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVariablesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DataMini/asktable-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVariablesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVariablesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DataMini/asktable-python#with_streaming_response
        """
        return AsyncVariablesResourceWithStreamingResponse(self)

    async def list(
        self,
        role_id: str,
        *,
        bot_id: Optional[str] | NotGiven = NOT_GIVEN,
        datasource_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        查询某个角色的所有变量

        Args:
          bot_id: Bot ID

          datasource_ids: 数据源 ID 列表

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not role_id:
            raise ValueError(f"Expected a non-empty value for `role_id` but received {role_id!r}")
        return await self._get(
            f"/roles/{role_id}/variables",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "bot_id": bot_id,
                        "datasource_ids": datasource_ids,
                    },
                    variable_list_params.VariableListParams,
                ),
            ),
            cast_to=object,
        )


class VariablesResourceWithRawResponse:
    def __init__(self, variables: VariablesResource) -> None:
        self._variables = variables

        self.list = to_raw_response_wrapper(
            variables.list,
        )


class AsyncVariablesResourceWithRawResponse:
    def __init__(self, variables: AsyncVariablesResource) -> None:
        self._variables = variables

        self.list = async_to_raw_response_wrapper(
            variables.list,
        )


class VariablesResourceWithStreamingResponse:
    def __init__(self, variables: VariablesResource) -> None:
        self._variables = variables

        self.list = to_streamed_response_wrapper(
            variables.list,
        )


class AsyncVariablesResourceWithStreamingResponse:
    def __init__(self, variables: AsyncVariablesResource) -> None:
        self._variables = variables

        self.list = async_to_streamed_response_wrapper(
            variables.list,
        )
