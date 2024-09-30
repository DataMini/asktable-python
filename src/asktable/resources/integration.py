# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import integration_excel_ask_params
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
from ..types.shared.answer_model import AnswerModel

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

    def excel_ask(
        self,
        *,
        excel_file_url: str,
        question: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AnswerModel:
        """
        通过 Excel 文件 URL 添加数据并提问

        Args:
          excel_file_url: Excel 文件 URL

          question: 查询语句

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/integration/excel_ask",
            body=maybe_transform(
                {
                    "excel_file_url": excel_file_url,
                    "question": question,
                },
                integration_excel_ask_params.IntegrationExcelAskParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AnswerModel,
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

    async def excel_ask(
        self,
        *,
        excel_file_url: str,
        question: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AnswerModel:
        """
        通过 Excel 文件 URL 添加数据并提问

        Args:
          excel_file_url: Excel 文件 URL

          question: 查询语句

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/integration/excel_ask",
            body=await async_maybe_transform(
                {
                    "excel_file_url": excel_file_url,
                    "question": question,
                },
                integration_excel_ask_params.IntegrationExcelAskParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AnswerModel,
        )


class IntegrationResourceWithRawResponse:
    def __init__(self, integration: IntegrationResource) -> None:
        self._integration = integration

        self.excel_ask = to_raw_response_wrapper(
            integration.excel_ask,
        )


class AsyncIntegrationResourceWithRawResponse:
    def __init__(self, integration: AsyncIntegrationResource) -> None:
        self._integration = integration

        self.excel_ask = async_to_raw_response_wrapper(
            integration.excel_ask,
        )


class IntegrationResourceWithStreamingResponse:
    def __init__(self, integration: IntegrationResource) -> None:
        self._integration = integration

        self.excel_ask = to_streamed_response_wrapper(
            integration.excel_ask,
        )


class AsyncIntegrationResourceWithStreamingResponse:
    def __init__(self, integration: AsyncIntegrationResource) -> None:
        self._integration = integration

        self.excel_ask = async_to_streamed_response_wrapper(
            integration.excel_ask,
        )
