# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options

__all__ = ["DownloadURLResource", "AsyncDownloadURLResource"]


class DownloadURLResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DownloadURLResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DataMini/asktable-python#accessing-raw-response-data-eg-headers
        """
        return DownloadURLResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DownloadURLResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DataMini/asktable-python#with_streaming_response
        """
        return DownloadURLResourceWithStreamingResponse(self)

    def retrieve(
        self,
        datasource_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        获取某个文件类型数据源的可直接下载的 URL

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not datasource_id:
            raise ValueError(f"Expected a non-empty value for `datasource_id` but received {datasource_id!r}")
        return self._get(
            f"/datasources/{datasource_id}/download_url",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncDownloadURLResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDownloadURLResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DataMini/asktable-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDownloadURLResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDownloadURLResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DataMini/asktable-python#with_streaming_response
        """
        return AsyncDownloadURLResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        datasource_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        获取某个文件类型数据源的可直接下载的 URL

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not datasource_id:
            raise ValueError(f"Expected a non-empty value for `datasource_id` but received {datasource_id!r}")
        return await self._get(
            f"/datasources/{datasource_id}/download_url",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class DownloadURLResourceWithRawResponse:
    def __init__(self, download_url: DownloadURLResource) -> None:
        self._download_url = download_url

        self.retrieve = to_raw_response_wrapper(
            download_url.retrieve,
        )


class AsyncDownloadURLResourceWithRawResponse:
    def __init__(self, download_url: AsyncDownloadURLResource) -> None:
        self._download_url = download_url

        self.retrieve = async_to_raw_response_wrapper(
            download_url.retrieve,
        )


class DownloadURLResourceWithStreamingResponse:
    def __init__(self, download_url: DownloadURLResource) -> None:
        self._download_url = download_url

        self.retrieve = to_streamed_response_wrapper(
            download_url.retrieve,
        )


class AsyncDownloadURLResourceWithStreamingResponse:
    def __init__(self, download_url: AsyncDownloadURLResource) -> None:
        self._download_url = download_url

        self.retrieve = async_to_streamed_response_wrapper(
            download_url.retrieve,
        )
