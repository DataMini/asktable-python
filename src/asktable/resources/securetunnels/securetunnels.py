# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from .links import (
    LinksResource,
    AsyncLinksResource,
    LinksResourceWithRawResponse,
    AsyncLinksResourceWithRawResponse,
    LinksResourceWithStreamingResponse,
    AsyncLinksResourceWithStreamingResponse,
)
from ...types import securetunnel_list_params, securetunnel_create_params, securetunnel_update_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
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
from ...types.secure_tunnel import SecureTunnel
from ...types.securetunnel_list_response import SecuretunnelListResponse

__all__ = ["SecuretunnelsResource", "AsyncSecuretunnelsResource"]


class SecuretunnelsResource(SyncAPIResource):
    @cached_property
    def links(self) -> LinksResource:
        return LinksResource(self._client)

    @cached_property
    def with_raw_response(self) -> SecuretunnelsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DataMini/asktable-python#accessing-raw-response-data-eg-headers
        """
        return SecuretunnelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SecuretunnelsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DataMini/asktable-python#with_streaming_response
        """
        return SecuretunnelsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SecureTunnel:
        """
        创建安全隧道

        Args:
          name: SecureTunnel 名称，不超过 20 个字符

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/securetunnels",
            body=maybe_transform({"name": name}, securetunnel_create_params.SecuretunnelCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SecureTunnel,
        )

    def retrieve(
        self,
        securetunnel_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SecureTunnel:
        """
        获取某个 ATST

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not securetunnel_id:
            raise ValueError(f"Expected a non-empty value for `securetunnel_id` but received {securetunnel_id!r}")
        return self._get(
            f"/securetunnels/{securetunnel_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SecureTunnel,
        )

    def update(
        self,
        securetunnel_id: str,
        *,
        client_info: Optional[object] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        unique_key: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        更新某个 ATST

        Args:
          client_info: 客户端信息

          name: SecureTunnel 名称，不超过 20 个字符

          unique_key: 唯一标识，用于更新客户端信息（容器 ID）

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not securetunnel_id:
            raise ValueError(f"Expected a non-empty value for `securetunnel_id` but received {securetunnel_id!r}")
        return self._patch(
            f"/securetunnels/{securetunnel_id}",
            body=maybe_transform(
                {
                    "client_info": client_info,
                    "name": name,
                    "unique_key": unique_key,
                },
                securetunnel_update_params.SecuretunnelUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def list(
        self,
        *,
        page: int | NotGiven = NOT_GIVEN,
        size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SecuretunnelListResponse:
        """
        查询安全隧道列表

        Args:
          page: Page number

          size: Page size

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/securetunnels",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "size": size,
                    },
                    securetunnel_list_params.SecuretunnelListParams,
                ),
            ),
            cast_to=SecuretunnelListResponse,
        )

    def delete(
        self,
        securetunnel_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        删除某个 ATST

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not securetunnel_id:
            raise ValueError(f"Expected a non-empty value for `securetunnel_id` but received {securetunnel_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/securetunnels/{securetunnel_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncSecuretunnelsResource(AsyncAPIResource):
    @cached_property
    def links(self) -> AsyncLinksResource:
        return AsyncLinksResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSecuretunnelsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DataMini/asktable-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSecuretunnelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSecuretunnelsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DataMini/asktable-python#with_streaming_response
        """
        return AsyncSecuretunnelsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SecureTunnel:
        """
        创建安全隧道

        Args:
          name: SecureTunnel 名称，不超过 20 个字符

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/securetunnels",
            body=await async_maybe_transform({"name": name}, securetunnel_create_params.SecuretunnelCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SecureTunnel,
        )

    async def retrieve(
        self,
        securetunnel_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SecureTunnel:
        """
        获取某个 ATST

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not securetunnel_id:
            raise ValueError(f"Expected a non-empty value for `securetunnel_id` but received {securetunnel_id!r}")
        return await self._get(
            f"/securetunnels/{securetunnel_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SecureTunnel,
        )

    async def update(
        self,
        securetunnel_id: str,
        *,
        client_info: Optional[object] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        unique_key: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        更新某个 ATST

        Args:
          client_info: 客户端信息

          name: SecureTunnel 名称，不超过 20 个字符

          unique_key: 唯一标识，用于更新客户端信息（容器 ID）

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not securetunnel_id:
            raise ValueError(f"Expected a non-empty value for `securetunnel_id` but received {securetunnel_id!r}")
        return await self._patch(
            f"/securetunnels/{securetunnel_id}",
            body=await async_maybe_transform(
                {
                    "client_info": client_info,
                    "name": name,
                    "unique_key": unique_key,
                },
                securetunnel_update_params.SecuretunnelUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def list(
        self,
        *,
        page: int | NotGiven = NOT_GIVEN,
        size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SecuretunnelListResponse:
        """
        查询安全隧道列表

        Args:
          page: Page number

          size: Page size

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/securetunnels",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "size": size,
                    },
                    securetunnel_list_params.SecuretunnelListParams,
                ),
            ),
            cast_to=SecuretunnelListResponse,
        )

    async def delete(
        self,
        securetunnel_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        删除某个 ATST

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not securetunnel_id:
            raise ValueError(f"Expected a non-empty value for `securetunnel_id` but received {securetunnel_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/securetunnels/{securetunnel_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class SecuretunnelsResourceWithRawResponse:
    def __init__(self, securetunnels: SecuretunnelsResource) -> None:
        self._securetunnels = securetunnels

        self.create = to_raw_response_wrapper(
            securetunnels.create,
        )
        self.retrieve = to_raw_response_wrapper(
            securetunnels.retrieve,
        )
        self.update = to_raw_response_wrapper(
            securetunnels.update,
        )
        self.list = to_raw_response_wrapper(
            securetunnels.list,
        )
        self.delete = to_raw_response_wrapper(
            securetunnels.delete,
        )

    @cached_property
    def links(self) -> LinksResourceWithRawResponse:
        return LinksResourceWithRawResponse(self._securetunnels.links)


class AsyncSecuretunnelsResourceWithRawResponse:
    def __init__(self, securetunnels: AsyncSecuretunnelsResource) -> None:
        self._securetunnels = securetunnels

        self.create = async_to_raw_response_wrapper(
            securetunnels.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            securetunnels.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            securetunnels.update,
        )
        self.list = async_to_raw_response_wrapper(
            securetunnels.list,
        )
        self.delete = async_to_raw_response_wrapper(
            securetunnels.delete,
        )

    @cached_property
    def links(self) -> AsyncLinksResourceWithRawResponse:
        return AsyncLinksResourceWithRawResponse(self._securetunnels.links)


class SecuretunnelsResourceWithStreamingResponse:
    def __init__(self, securetunnels: SecuretunnelsResource) -> None:
        self._securetunnels = securetunnels

        self.create = to_streamed_response_wrapper(
            securetunnels.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            securetunnels.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            securetunnels.update,
        )
        self.list = to_streamed_response_wrapper(
            securetunnels.list,
        )
        self.delete = to_streamed_response_wrapper(
            securetunnels.delete,
        )

    @cached_property
    def links(self) -> LinksResourceWithStreamingResponse:
        return LinksResourceWithStreamingResponse(self._securetunnels.links)


class AsyncSecuretunnelsResourceWithStreamingResponse:
    def __init__(self, securetunnels: AsyncSecuretunnelsResource) -> None:
        self._securetunnels = securetunnels

        self.create = async_to_streamed_response_wrapper(
            securetunnels.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            securetunnels.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            securetunnels.update,
        )
        self.list = async_to_streamed_response_wrapper(
            securetunnels.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            securetunnels.delete,
        )

    @cached_property
    def links(self) -> AsyncLinksResourceWithStreamingResponse:
        return AsyncLinksResourceWithStreamingResponse(self._securetunnels.links)
