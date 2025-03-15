# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.dataframe_retrieve_response import DataframeRetrieveResponse

__all__ = ["DataframesResource", "AsyncDataframesResource"]


class DataframesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DataframesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DataMini/asktable-python#accessing-raw-response-data-eg-headers
        """
        return DataframesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DataframesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DataMini/asktable-python#with_streaming_response
        """
        return DataframesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        dataframe_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DataframeRetrieveResponse:
        """
        Get Dataframe

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dataframe_id:
            raise ValueError(f"Expected a non-empty value for `dataframe_id` but received {dataframe_id!r}")
        return self._get(
            f"/v1/dataframes/{dataframe_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataframeRetrieveResponse,
        )


class AsyncDataframesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDataframesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DataMini/asktable-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDataframesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDataframesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DataMini/asktable-python#with_streaming_response
        """
        return AsyncDataframesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        dataframe_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DataframeRetrieveResponse:
        """
        Get Dataframe

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dataframe_id:
            raise ValueError(f"Expected a non-empty value for `dataframe_id` but received {dataframe_id!r}")
        return await self._get(
            f"/v1/dataframes/{dataframe_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataframeRetrieveResponse,
        )


class DataframesResourceWithRawResponse:
    def __init__(self, dataframes: DataframesResource) -> None:
        self._dataframes = dataframes

        self.retrieve = to_raw_response_wrapper(
            dataframes.retrieve,
        )


class AsyncDataframesResourceWithRawResponse:
    def __init__(self, dataframes: AsyncDataframesResource) -> None:
        self._dataframes = dataframes

        self.retrieve = async_to_raw_response_wrapper(
            dataframes.retrieve,
        )


class DataframesResourceWithStreamingResponse:
    def __init__(self, dataframes: DataframesResource) -> None:
        self._dataframes = dataframes

        self.retrieve = to_streamed_response_wrapper(
            dataframes.retrieve,
        )


class AsyncDataframesResourceWithStreamingResponse:
    def __init__(self, dataframes: AsyncDataframesResource) -> None:
        self._dataframes = dataframes

        self.retrieve = async_to_streamed_response_wrapper(
            dataframes.retrieve,
        )
