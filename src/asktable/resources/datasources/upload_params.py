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
from ..._base_client import make_request_options
from ...types.datasources import upload_param_create_params

__all__ = ["UploadParamsResource", "AsyncUploadParamsResource"]


class UploadParamsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UploadParamsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DataMini/asktable-python#accessing-raw-response-data-eg-headers
        """
        return UploadParamsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UploadParamsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DataMini/asktable-python#with_streaming_response
        """
        return UploadParamsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        expiration: Optional[int] | NotGiven = NOT_GIVEN,
        file_max_size: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        获取 OSS 签名参数

        Args:
          expiration: URL 有效期，单位为分钟

          file_max_size: 文件大小限制，单位为 MB

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/datasources/upload_params",
            body=maybe_transform(
                {
                    "expiration": expiration,
                    "file_max_size": file_max_size,
                },
                upload_param_create_params.UploadParamCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncUploadParamsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUploadParamsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DataMini/asktable-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUploadParamsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUploadParamsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DataMini/asktable-python#with_streaming_response
        """
        return AsyncUploadParamsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        expiration: Optional[int] | NotGiven = NOT_GIVEN,
        file_max_size: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        获取 OSS 签名参数

        Args:
          expiration: URL 有效期，单位为分钟

          file_max_size: 文件大小限制，单位为 MB

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/datasources/upload_params",
            body=await async_maybe_transform(
                {
                    "expiration": expiration,
                    "file_max_size": file_max_size,
                },
                upload_param_create_params.UploadParamCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class UploadParamsResourceWithRawResponse:
    def __init__(self, upload_params: UploadParamsResource) -> None:
        self._upload_params = upload_params

        self.create = to_raw_response_wrapper(
            upload_params.create,
        )


class AsyncUploadParamsResourceWithRawResponse:
    def __init__(self, upload_params: AsyncUploadParamsResource) -> None:
        self._upload_params = upload_params

        self.create = async_to_raw_response_wrapper(
            upload_params.create,
        )


class UploadParamsResourceWithStreamingResponse:
    def __init__(self, upload_params: UploadParamsResource) -> None:
        self._upload_params = upload_params

        self.create = to_streamed_response_wrapper(
            upload_params.create,
        )


class AsyncUploadParamsResourceWithStreamingResponse:
    def __init__(self, upload_params: AsyncUploadParamsResource) -> None:
        self._upload_params = upload_params

        self.create = async_to_streamed_response_wrapper(
            upload_params.create,
        )
