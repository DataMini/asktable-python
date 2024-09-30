# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options

__all__ = ["CachesResource", "AsyncCachesResource"]


class CachesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CachesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DataMini/asktable-python#accessing-raw-response-data-eg-headers
        """
        return CachesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CachesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DataMini/asktable-python#with_streaming_response
        """
        return CachesResourceWithStreamingResponse(self)

    def delete(
        self,
        cache_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        清除缓存

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not cache_id:
            raise ValueError(f"Expected a non-empty value for `cache_id` but received {cache_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/caches/{cache_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncCachesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCachesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DataMini/asktable-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCachesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCachesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DataMini/asktable-python#with_streaming_response
        """
        return AsyncCachesResourceWithStreamingResponse(self)

    async def delete(
        self,
        cache_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        清除缓存

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not cache_id:
            raise ValueError(f"Expected a non-empty value for `cache_id` but received {cache_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/caches/{cache_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class CachesResourceWithRawResponse:
    def __init__(self, caches: CachesResource) -> None:
        self._caches = caches

        self.delete = to_raw_response_wrapper(
            caches.delete,
        )


class AsyncCachesResourceWithRawResponse:
    def __init__(self, caches: AsyncCachesResource) -> None:
        self._caches = caches

        self.delete = async_to_raw_response_wrapper(
            caches.delete,
        )


class CachesResourceWithStreamingResponse:
    def __init__(self, caches: CachesResource) -> None:
        self._caches = caches

        self.delete = to_streamed_response_wrapper(
            caches.delete,
        )


class AsyncCachesResourceWithStreamingResponse:
    def __init__(self, caches: AsyncCachesResource) -> None:
        self._caches = caches

        self.delete = async_to_streamed_response_wrapper(
            caches.delete,
        )
