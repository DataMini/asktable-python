# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ..._base_client import make_request_options
from ...types.single_turn import q2w_create_params

__all__ = ["Q2wResource", "AsyncQ2wResource"]


class Q2wResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> Q2wResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DataMini/asktable-python#accessing-raw-response-data-eg-headers
        """
        return Q2wResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> Q2wResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DataMini/asktable-python#with_streaming_response
        """
        return Q2wResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Create Q2W

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/single-turn/q2w",
            body=maybe_transform(body, q2w_create_params.Q2wCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """获取所有的 Q2W 记录"""
        return self._get(
            "/single-turn/q2w",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncQ2wResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncQ2wResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DataMini/asktable-python#accessing-raw-response-data-eg-headers
        """
        return AsyncQ2wResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncQ2wResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DataMini/asktable-python#with_streaming_response
        """
        return AsyncQ2wResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Create Q2W

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/single-turn/q2w",
            body=await async_maybe_transform(body, q2w_create_params.Q2wCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """获取所有的 Q2W 记录"""
        return await self._get(
            "/single-turn/q2w",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class Q2wResourceWithRawResponse:
    def __init__(self, q2w: Q2wResource) -> None:
        self._q2w = q2w

        self.create = to_raw_response_wrapper(
            q2w.create,
        )
        self.list = to_raw_response_wrapper(
            q2w.list,
        )


class AsyncQ2wResourceWithRawResponse:
    def __init__(self, q2w: AsyncQ2wResource) -> None:
        self._q2w = q2w

        self.create = async_to_raw_response_wrapper(
            q2w.create,
        )
        self.list = async_to_raw_response_wrapper(
            q2w.list,
        )


class Q2wResourceWithStreamingResponse:
    def __init__(self, q2w: Q2wResource) -> None:
        self._q2w = q2w

        self.create = to_streamed_response_wrapper(
            q2w.create,
        )
        self.list = to_streamed_response_wrapper(
            q2w.list,
        )


class AsyncQ2wResourceWithStreamingResponse:
    def __init__(self, q2w: AsyncQ2wResource) -> None:
        self._q2w = q2w

        self.create = async_to_streamed_response_wrapper(
            q2w.create,
        )
        self.list = async_to_streamed_response_wrapper(
            q2w.list,
        )
