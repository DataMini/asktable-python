# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional

import httpx

from .routes import (
    RoutesResource,
    AsyncRoutesResource,
    RoutesResourceWithRawResponse,
    AsyncRoutesResourceWithRawResponse,
    RoutesResourceWithStreamingResponse,
    AsyncRoutesResourceWithStreamingResponse,
)
from ...types import extapi_list_params, extapi_create_params, extapi_update_params
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
from ...pagination import SyncPage, AsyncPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.extapi import Extapi

__all__ = ["ExtapisResource", "AsyncExtapisResource"]


class ExtapisResource(SyncAPIResource):
    @cached_property
    def routes(self) -> RoutesResource:
        return RoutesResource(self._client)

    @cached_property
    def with_raw_response(self) -> ExtapisResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DataMini/asktable-python#accessing-raw-response-data-eg-headers
        """
        return ExtapisResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExtapisResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DataMini/asktable-python#with_streaming_response
        """
        return ExtapisResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        base_url: str,
        name: str,
        headers: Optional[Dict[str, str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Extapi:
        """
        创建一个新的 ExtAPI

        Args:
          base_url: 根 URL

          name: 名称，不超过 64 个字符

          headers: HTTP Headers，JSON 格式

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/extapis",
            body=maybe_transform(
                {
                    "base_url": base_url,
                    "name": name,
                    "headers": headers,
                },
                extapi_create_params.ExtapiCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Extapi,
        )

    def retrieve(
        self,
        extapi_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Extapi:
        """
        获取某个 ExtAPI

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not extapi_id:
            raise ValueError(f"Expected a non-empty value for `extapi_id` but received {extapi_id!r}")
        return self._get(
            f"/extapis/{extapi_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Extapi,
        )

    def update(
        self,
        extapi_id: str,
        *,
        base_url: Optional[str] | NotGiven = NOT_GIVEN,
        headers: Optional[Dict[str, str]] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Extapi:
        """
        更新某个 ExtAPI

        Args:
          base_url: 根 URL

          headers: HTTP Headers，JSON 格式

          name: 名称，不超过 64 个字符

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not extapi_id:
            raise ValueError(f"Expected a non-empty value for `extapi_id` but received {extapi_id!r}")
        return self._post(
            f"/extapis/{extapi_id}",
            body=maybe_transform(
                {
                    "base_url": base_url,
                    "headers": headers,
                    "name": name,
                },
                extapi_update_params.ExtapiUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Extapi,
        )

    def list(
        self,
        *,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[Extapi]:
        """
        查询所有 ExtAPI

        Args:
          name: 名称

          page: Page number

          size: Page size

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/extapis",
            page=SyncPage[Extapi],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "name": name,
                        "page": page,
                        "size": size,
                    },
                    extapi_list_params.ExtapiListParams,
                ),
            ),
            model=Extapi,
        )

    def delete(
        self,
        extapi_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        删除某个 ExtAPI

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not extapi_id:
            raise ValueError(f"Expected a non-empty value for `extapi_id` but received {extapi_id!r}")
        return self._delete(
            f"/extapis/{extapi_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncExtapisResource(AsyncAPIResource):
    @cached_property
    def routes(self) -> AsyncRoutesResource:
        return AsyncRoutesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncExtapisResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DataMini/asktable-python#accessing-raw-response-data-eg-headers
        """
        return AsyncExtapisResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExtapisResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DataMini/asktable-python#with_streaming_response
        """
        return AsyncExtapisResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        base_url: str,
        name: str,
        headers: Optional[Dict[str, str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Extapi:
        """
        创建一个新的 ExtAPI

        Args:
          base_url: 根 URL

          name: 名称，不超过 64 个字符

          headers: HTTP Headers，JSON 格式

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/extapis",
            body=await async_maybe_transform(
                {
                    "base_url": base_url,
                    "name": name,
                    "headers": headers,
                },
                extapi_create_params.ExtapiCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Extapi,
        )

    async def retrieve(
        self,
        extapi_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Extapi:
        """
        获取某个 ExtAPI

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not extapi_id:
            raise ValueError(f"Expected a non-empty value for `extapi_id` but received {extapi_id!r}")
        return await self._get(
            f"/extapis/{extapi_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Extapi,
        )

    async def update(
        self,
        extapi_id: str,
        *,
        base_url: Optional[str] | NotGiven = NOT_GIVEN,
        headers: Optional[Dict[str, str]] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Extapi:
        """
        更新某个 ExtAPI

        Args:
          base_url: 根 URL

          headers: HTTP Headers，JSON 格式

          name: 名称，不超过 64 个字符

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not extapi_id:
            raise ValueError(f"Expected a non-empty value for `extapi_id` but received {extapi_id!r}")
        return await self._post(
            f"/extapis/{extapi_id}",
            body=await async_maybe_transform(
                {
                    "base_url": base_url,
                    "headers": headers,
                    "name": name,
                },
                extapi_update_params.ExtapiUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Extapi,
        )

    def list(
        self,
        *,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Extapi, AsyncPage[Extapi]]:
        """
        查询所有 ExtAPI

        Args:
          name: 名称

          page: Page number

          size: Page size

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/extapis",
            page=AsyncPage[Extapi],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "name": name,
                        "page": page,
                        "size": size,
                    },
                    extapi_list_params.ExtapiListParams,
                ),
            ),
            model=Extapi,
        )

    async def delete(
        self,
        extapi_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        删除某个 ExtAPI

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not extapi_id:
            raise ValueError(f"Expected a non-empty value for `extapi_id` but received {extapi_id!r}")
        return await self._delete(
            f"/extapis/{extapi_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class ExtapisResourceWithRawResponse:
    def __init__(self, extapis: ExtapisResource) -> None:
        self._extapis = extapis

        self.create = to_raw_response_wrapper(
            extapis.create,
        )
        self.retrieve = to_raw_response_wrapper(
            extapis.retrieve,
        )
        self.update = to_raw_response_wrapper(
            extapis.update,
        )
        self.list = to_raw_response_wrapper(
            extapis.list,
        )
        self.delete = to_raw_response_wrapper(
            extapis.delete,
        )

    @cached_property
    def routes(self) -> RoutesResourceWithRawResponse:
        return RoutesResourceWithRawResponse(self._extapis.routes)


class AsyncExtapisResourceWithRawResponse:
    def __init__(self, extapis: AsyncExtapisResource) -> None:
        self._extapis = extapis

        self.create = async_to_raw_response_wrapper(
            extapis.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            extapis.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            extapis.update,
        )
        self.list = async_to_raw_response_wrapper(
            extapis.list,
        )
        self.delete = async_to_raw_response_wrapper(
            extapis.delete,
        )

    @cached_property
    def routes(self) -> AsyncRoutesResourceWithRawResponse:
        return AsyncRoutesResourceWithRawResponse(self._extapis.routes)


class ExtapisResourceWithStreamingResponse:
    def __init__(self, extapis: ExtapisResource) -> None:
        self._extapis = extapis

        self.create = to_streamed_response_wrapper(
            extapis.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            extapis.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            extapis.update,
        )
        self.list = to_streamed_response_wrapper(
            extapis.list,
        )
        self.delete = to_streamed_response_wrapper(
            extapis.delete,
        )

    @cached_property
    def routes(self) -> RoutesResourceWithStreamingResponse:
        return RoutesResourceWithStreamingResponse(self._extapis.routes)


class AsyncExtapisResourceWithStreamingResponse:
    def __init__(self, extapis: AsyncExtapisResource) -> None:
        self._extapis = extapis

        self.create = async_to_streamed_response_wrapper(
            extapis.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            extapis.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            extapis.update,
        )
        self.list = async_to_streamed_response_wrapper(
            extapis.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            extapis.delete,
        )

    @cached_property
    def routes(self) -> AsyncRoutesResourceWithStreamingResponse:
        return AsyncRoutesResourceWithStreamingResponse(self._extapis.routes)
