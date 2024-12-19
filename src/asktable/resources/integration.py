# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import integration_excel_csv_ask_params, integration_create_excel_ds_params
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
from ..types.datasource import Datasource
from ..types.file_ask_response import FileAskResponse

__all__ = ["IntegrationResource", "AsyncIntegrationResource"]


class IntegrationResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IntegrationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DataMini/asktable-python#accessing-raw-response-data-eg-headers
        """
        return IntegrationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IntegrationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DataMini/asktable-python#with_streaming_response
        """
        return IntegrationResourceWithStreamingResponse(self)

    def create_excel_ds(
        self,
        *,
        file_url: str,
        value_index: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Datasource:
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
                query=maybe_transform(
                    {
                        "file_url": file_url,
                        "value_index": value_index,
                    },
                    integration_create_excel_ds_params.IntegrationCreateExcelDsParams,
                ),
            ),
            cast_to=Datasource,
        )

    def excel_csv_ask(
        self,
        *,
        file_url: str,
        question: str,
        with_json: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FileAskResponse:
        """
        通过 Excel/CSV 文件 URL 添加数据并提问

        Args:
          file_url: 文件 URL(支持 Excel/CSV)

          question: 用户问题

          with_json: 是否将数据作为 json 附件返回

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/integration/excel_csv_ask",
            body=maybe_transform(
                {
                    "file_url": file_url,
                    "question": question,
                    "with_json": with_json,
                },
                integration_excel_csv_ask_params.IntegrationExcelCsvAskParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileAskResponse,
        )


class AsyncIntegrationResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIntegrationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DataMini/asktable-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIntegrationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIntegrationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DataMini/asktable-python#with_streaming_response
        """
        return AsyncIntegrationResourceWithStreamingResponse(self)

    async def create_excel_ds(
        self,
        *,
        file_url: str,
        value_index: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Datasource:
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
                query=await async_maybe_transform(
                    {
                        "file_url": file_url,
                        "value_index": value_index,
                    },
                    integration_create_excel_ds_params.IntegrationCreateExcelDsParams,
                ),
            ),
            cast_to=Datasource,
        )

    async def excel_csv_ask(
        self,
        *,
        file_url: str,
        question: str,
        with_json: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FileAskResponse:
        """
        通过 Excel/CSV 文件 URL 添加数据并提问

        Args:
          file_url: 文件 URL(支持 Excel/CSV)

          question: 用户问题

          with_json: 是否将数据作为 json 附件返回

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/integration/excel_csv_ask",
            body=await async_maybe_transform(
                {
                    "file_url": file_url,
                    "question": question,
                    "with_json": with_json,
                },
                integration_excel_csv_ask_params.IntegrationExcelCsvAskParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileAskResponse,
        )


class IntegrationResourceWithRawResponse:
    def __init__(self, integration: IntegrationResource) -> None:
        self._integration = integration

        self.create_excel_ds = to_raw_response_wrapper(
            integration.create_excel_ds,
        )
        self.excel_csv_ask = to_raw_response_wrapper(
            integration.excel_csv_ask,
        )


class AsyncIntegrationResourceWithRawResponse:
    def __init__(self, integration: AsyncIntegrationResource) -> None:
        self._integration = integration

        self.create_excel_ds = async_to_raw_response_wrapper(
            integration.create_excel_ds,
        )
        self.excel_csv_ask = async_to_raw_response_wrapper(
            integration.excel_csv_ask,
        )


class IntegrationResourceWithStreamingResponse:
    def __init__(self, integration: IntegrationResource) -> None:
        self._integration = integration

        self.create_excel_ds = to_streamed_response_wrapper(
            integration.create_excel_ds,
        )
        self.excel_csv_ask = to_streamed_response_wrapper(
            integration.excel_csv_ask,
        )


class AsyncIntegrationResourceWithStreamingResponse:
    def __init__(self, integration: AsyncIntegrationResource) -> None:
        self._integration = integration

        self.create_excel_ds = async_to_streamed_response_wrapper(
            integration.create_excel_ds,
        )
        self.excel_csv_ask = async_to_streamed_response_wrapper(
            integration.excel_csv_ask,
        )
