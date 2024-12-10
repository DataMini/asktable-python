# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import (
    securetunnel_list_params,
    securetunnel_create_params,
    securetunnel_update_params,
    securetunnel_list_links_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
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
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.secure_tunnel import SecureTunnel
from ..types.securetunnel_list_links_response import SecuretunnelListLinksResponse

__all__ = ["SecuretunnelsResource", "AsyncSecuretunnelsResource"]


class SecuretunnelsResource(SyncAPIResource):
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
        name: str,
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
        name: str,
        client_info: Optional[object] | NotGiven = NOT_GIVEN,
        unique_key: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SecureTunnel:
        """
        更新某个 ATST

        Args:
          name: SecureTunnel 名称，不超过 20 个字符

          client_info: 客户端信息

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
                    "name": name,
                    "client_info": client_info,
                    "unique_key": unique_key,
                },
                securetunnel_update_params.SecuretunnelUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SecureTunnel,
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
    ) -> SyncPage[SecureTunnel]:
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
        return self._get_api_list(
            "/securetunnels",
            page=SyncPage[SecureTunnel],
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
            model=SecureTunnel,
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

    def list_links(
        self,
        securetunnel_id: str,
        *,
        page: int | NotGiven = NOT_GIVEN,
        size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[SecuretunnelListLinksResponse]:
        """
        查询安全隧道的所有 Link

        Args:
          page: Page number

          size: Page size

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not securetunnel_id:
            raise ValueError(f"Expected a non-empty value for `securetunnel_id` but received {securetunnel_id!r}")
        return self._get_api_list(
            f"/securetunnels/{securetunnel_id}/links",
            page=SyncPage[SecuretunnelListLinksResponse],
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
                    securetunnel_list_links_params.SecuretunnelListLinksParams,
                ),
            ),
            model=SecuretunnelListLinksResponse,
        )


class AsyncSecuretunnelsResource(AsyncAPIResource):
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
        name: str,
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
        name: str,
        client_info: Optional[object] | NotGiven = NOT_GIVEN,
        unique_key: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SecureTunnel:
        """
        更新某个 ATST

        Args:
          name: SecureTunnel 名称，不超过 20 个字符

          client_info: 客户端信息

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
                    "name": name,
                    "client_info": client_info,
                    "unique_key": unique_key,
                },
                securetunnel_update_params.SecuretunnelUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SecureTunnel,
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
    ) -> AsyncPaginator[SecureTunnel, AsyncPage[SecureTunnel]]:
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
        return self._get_api_list(
            "/securetunnels",
            page=AsyncPage[SecureTunnel],
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
            model=SecureTunnel,
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

    def list_links(
        self,
        securetunnel_id: str,
        *,
        page: int | NotGiven = NOT_GIVEN,
        size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[SecuretunnelListLinksResponse, AsyncPage[SecuretunnelListLinksResponse]]:
        """
        查询安全隧道的所有 Link

        Args:
          page: Page number

          size: Page size

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not securetunnel_id:
            raise ValueError(f"Expected a non-empty value for `securetunnel_id` but received {securetunnel_id!r}")
        return self._get_api_list(
            f"/securetunnels/{securetunnel_id}/links",
            page=AsyncPage[SecuretunnelListLinksResponse],
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
                    securetunnel_list_links_params.SecuretunnelListLinksParams,
                ),
            ),
            model=SecuretunnelListLinksResponse,
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
        self.list_links = to_raw_response_wrapper(
            securetunnels.list_links,
        )


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
        self.list_links = async_to_raw_response_wrapper(
            securetunnels.list_links,
        )


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
        self.list_links = to_streamed_response_wrapper(
            securetunnels.list_links,
        )


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
        self.list_links = async_to_streamed_response_wrapper(
            securetunnels.list_links,
        )
