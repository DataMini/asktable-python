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
from ...types.data_source import DataSource
from ...types.integration import excel_csv_create_params

__all__ = ["ExcelCsvResource", "AsyncExcelCsvResource"]


class ExcelCsvResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ExcelCsvResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DataMini/asktable-python#accessing-raw-response-data-eg-headers
        """
        return ExcelCsvResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExcelCsvResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DataMini/asktable-python#with_streaming_response
        """
        return ExcelCsvResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        file_url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DataSource:
        """
        通过 Excel/CSV 文件 URL 创建数据源

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/integration/create_excel_ds",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"file_url": file_url}, excel_csv_create_params.ExcelCsvCreateParams),
            ),
            cast_to=DataSource,
        )


class AsyncExcelCsvResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncExcelCsvResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DataMini/asktable-python#accessing-raw-response-data-eg-headers
        """
        return AsyncExcelCsvResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExcelCsvResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DataMini/asktable-python#with_streaming_response
        """
        return AsyncExcelCsvResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        file_url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DataSource:
        """
        通过 Excel/CSV 文件 URL 创建数据源

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/integration/create_excel_ds",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"file_url": file_url}, excel_csv_create_params.ExcelCsvCreateParams),
            ),
            cast_to=DataSource,
        )


class ExcelCsvResourceWithRawResponse:
    def __init__(self, excel_csv: ExcelCsvResource) -> None:
        self._excel_csv = excel_csv

        self.create = to_raw_response_wrapper(
            excel_csv.create,
        )


class AsyncExcelCsvResourceWithRawResponse:
    def __init__(self, excel_csv: AsyncExcelCsvResource) -> None:
        self._excel_csv = excel_csv

        self.create = async_to_raw_response_wrapper(
            excel_csv.create,
        )


class ExcelCsvResourceWithStreamingResponse:
    def __init__(self, excel_csv: ExcelCsvResource) -> None:
        self._excel_csv = excel_csv

        self.create = to_streamed_response_wrapper(
            excel_csv.create,
        )


class AsyncExcelCsvResourceWithStreamingResponse:
    def __init__(self, excel_csv: AsyncExcelCsvResource) -> None:
        self._excel_csv = excel_csv

        self.create = async_to_streamed_response_wrapper(
            excel_csv.create,
        )
