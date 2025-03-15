# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import polish_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.polish_create_response import PolishCreateResponse

__all__ = ["PolishResource", "AsyncPolishResource"]


class PolishResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PolishResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DataMini/asktable-python#accessing-raw-response-data-eg-headers
        """
        return PolishResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PolishResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DataMini/asktable-python#with_streaming_response
        """
        return PolishResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        max_word_count: int,
        user_desc: str,
        polish_mode: Literal[0] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PolishCreateResponse:
        """
        Polish Table Desc

        Args:
          max_word_count: 润色后的最大字数，注意：该值不是绝对值，实际优化后的字数可能会超过该值

          user_desc: 需要润色的用户输入

          polish_mode: 润色模式，默认是简化模式

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/polish",
            body=maybe_transform(
                {
                    "max_word_count": max_word_count,
                    "user_desc": user_desc,
                    "polish_mode": polish_mode,
                },
                polish_create_params.PolishCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PolishCreateResponse,
        )


class AsyncPolishResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPolishResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DataMini/asktable-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPolishResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPolishResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DataMini/asktable-python#with_streaming_response
        """
        return AsyncPolishResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        max_word_count: int,
        user_desc: str,
        polish_mode: Literal[0] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PolishCreateResponse:
        """
        Polish Table Desc

        Args:
          max_word_count: 润色后的最大字数，注意：该值不是绝对值，实际优化后的字数可能会超过该值

          user_desc: 需要润色的用户输入

          polish_mode: 润色模式，默认是简化模式

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/polish",
            body=await async_maybe_transform(
                {
                    "max_word_count": max_word_count,
                    "user_desc": user_desc,
                    "polish_mode": polish_mode,
                },
                polish_create_params.PolishCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PolishCreateResponse,
        )


class PolishResourceWithRawResponse:
    def __init__(self, polish: PolishResource) -> None:
        self._polish = polish

        self.create = to_raw_response_wrapper(
            polish.create,
        )


class AsyncPolishResourceWithRawResponse:
    def __init__(self, polish: AsyncPolishResource) -> None:
        self._polish = polish

        self.create = async_to_raw_response_wrapper(
            polish.create,
        )


class PolishResourceWithStreamingResponse:
    def __init__(self, polish: PolishResource) -> None:
        self._polish = polish

        self.create = to_streamed_response_wrapper(
            polish.create,
        )


class AsyncPolishResourceWithStreamingResponse:
    def __init__(self, polish: AsyncPolishResource) -> None:
        self._polish = polish

        self.create = async_to_streamed_response_wrapper(
            polish.create,
        )
