# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

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
from ...types.extapis import route_create_params, route_update_params
from ...types.extapis.extapi_route import ExtapiRoute
from ...types.extapis.route_list_response import RouteListResponse

__all__ = ["RoutesResource", "AsyncRoutesResource"]


class RoutesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RoutesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DataMini/asktable-python#accessing-raw-response-data-eg-headers
        """
        return RoutesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RoutesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DataMini/asktable-python#with_streaming_response
        """
        return RoutesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        path_extapi_id: str,
        id: str,
        created_at: Union[str, datetime],
        body_extapi_id: str,
        method: Literal["GET", "POST", "PUT", "DELETE"],
        name: str,
        path: str,
        project_id: str,
        body_params_desc: Optional[str] | NotGiven = NOT_GIVEN,
        path_params_desc: Optional[str] | NotGiven = NOT_GIVEN,
        query_params_desc: Optional[str] | NotGiven = NOT_GIVEN,
        updated_at: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExtapiRoute:
        """
        为某个 ExtAPI 创建新的路径

        Args:
          method: HTTP 方法

          name: API 方法名称，不超过 64 个字符

          path: API 路径

          body_params_desc: 请求体参数描述

          path_params_desc: 路径参数描述

          query_params_desc: 查询参数描述

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_extapi_id:
            raise ValueError(f"Expected a non-empty value for `path_extapi_id` but received {path_extapi_id!r}")
        return self._post(
            f"/extapis/{path_extapi_id}/routes",
            body=maybe_transform(
                {
                    "id": id,
                    "created_at": created_at,
                    "body_extapi_id": body_extapi_id,
                    "method": method,
                    "name": name,
                    "path": path,
                    "project_id": project_id,
                    "body_params_desc": body_params_desc,
                    "path_params_desc": path_params_desc,
                    "query_params_desc": query_params_desc,
                    "updated_at": updated_at,
                },
                route_create_params.RouteCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtapiRoute,
        )

    def retrieve(
        self,
        route_id: str,
        *,
        extapi_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExtapiRoute:
        """
        获取某个 ExtAPI Route

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not extapi_id:
            raise ValueError(f"Expected a non-empty value for `extapi_id` but received {extapi_id!r}")
        if not route_id:
            raise ValueError(f"Expected a non-empty value for `route_id` but received {route_id!r}")
        return self._get(
            f"/extapis/{extapi_id}/routes/{route_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtapiRoute,
        )

    def update(
        self,
        route_id: str,
        *,
        extapi_id: str,
        body_params_desc: Optional[str] | NotGiven = NOT_GIVEN,
        method: Optional[Literal["GET", "POST", "PUT", "DELETE"]] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        path: Optional[str] | NotGiven = NOT_GIVEN,
        path_params_desc: Optional[str] | NotGiven = NOT_GIVEN,
        query_params_desc: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExtapiRoute:
        """
        更新某个 ExtAPI Route

        Args:
          body_params_desc: 请求体参数描述

          method: HTTP 方法

          name: API 方法名称，不超过 64 个字符

          path: API 路径

          path_params_desc: 路径参数描述

          query_params_desc: 查询参数描述

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not extapi_id:
            raise ValueError(f"Expected a non-empty value for `extapi_id` but received {extapi_id!r}")
        if not route_id:
            raise ValueError(f"Expected a non-empty value for `route_id` but received {route_id!r}")
        return self._post(
            f"/extapis/{extapi_id}/routes/{route_id}",
            body=maybe_transform(
                {
                    "body_params_desc": body_params_desc,
                    "method": method,
                    "name": name,
                    "path": path,
                    "path_params_desc": path_params_desc,
                    "query_params_desc": query_params_desc,
                },
                route_update_params.RouteUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtapiRoute,
        )

    def list(
        self,
        extapi_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RouteListResponse:
        """
        获取某个 ExtAPI 的所有路径

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not extapi_id:
            raise ValueError(f"Expected a non-empty value for `extapi_id` but received {extapi_id!r}")
        return self._get(
            f"/extapis/{extapi_id}/routes",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RouteListResponse,
        )

    def delete(
        self,
        route_id: str,
        *,
        extapi_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        删除某个 ExtAPI Route

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not extapi_id:
            raise ValueError(f"Expected a non-empty value for `extapi_id` but received {extapi_id!r}")
        if not route_id:
            raise ValueError(f"Expected a non-empty value for `route_id` but received {route_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/extapis/{extapi_id}/routes/{route_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncRoutesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRoutesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DataMini/asktable-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRoutesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRoutesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DataMini/asktable-python#with_streaming_response
        """
        return AsyncRoutesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        path_extapi_id: str,
        id: str,
        created_at: Union[str, datetime],
        body_extapi_id: str,
        method: Literal["GET", "POST", "PUT", "DELETE"],
        name: str,
        path: str,
        project_id: str,
        body_params_desc: Optional[str] | NotGiven = NOT_GIVEN,
        path_params_desc: Optional[str] | NotGiven = NOT_GIVEN,
        query_params_desc: Optional[str] | NotGiven = NOT_GIVEN,
        updated_at: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExtapiRoute:
        """
        为某个 ExtAPI 创建新的路径

        Args:
          method: HTTP 方法

          name: API 方法名称，不超过 64 个字符

          path: API 路径

          body_params_desc: 请求体参数描述

          path_params_desc: 路径参数描述

          query_params_desc: 查询参数描述

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_extapi_id:
            raise ValueError(f"Expected a non-empty value for `path_extapi_id` but received {path_extapi_id!r}")
        return await self._post(
            f"/extapis/{path_extapi_id}/routes",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "created_at": created_at,
                    "body_extapi_id": body_extapi_id,
                    "method": method,
                    "name": name,
                    "path": path,
                    "project_id": project_id,
                    "body_params_desc": body_params_desc,
                    "path_params_desc": path_params_desc,
                    "query_params_desc": query_params_desc,
                    "updated_at": updated_at,
                },
                route_create_params.RouteCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtapiRoute,
        )

    async def retrieve(
        self,
        route_id: str,
        *,
        extapi_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExtapiRoute:
        """
        获取某个 ExtAPI Route

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not extapi_id:
            raise ValueError(f"Expected a non-empty value for `extapi_id` but received {extapi_id!r}")
        if not route_id:
            raise ValueError(f"Expected a non-empty value for `route_id` but received {route_id!r}")
        return await self._get(
            f"/extapis/{extapi_id}/routes/{route_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtapiRoute,
        )

    async def update(
        self,
        route_id: str,
        *,
        extapi_id: str,
        body_params_desc: Optional[str] | NotGiven = NOT_GIVEN,
        method: Optional[Literal["GET", "POST", "PUT", "DELETE"]] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        path: Optional[str] | NotGiven = NOT_GIVEN,
        path_params_desc: Optional[str] | NotGiven = NOT_GIVEN,
        query_params_desc: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExtapiRoute:
        """
        更新某个 ExtAPI Route

        Args:
          body_params_desc: 请求体参数描述

          method: HTTP 方法

          name: API 方法名称，不超过 64 个字符

          path: API 路径

          path_params_desc: 路径参数描述

          query_params_desc: 查询参数描述

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not extapi_id:
            raise ValueError(f"Expected a non-empty value for `extapi_id` but received {extapi_id!r}")
        if not route_id:
            raise ValueError(f"Expected a non-empty value for `route_id` but received {route_id!r}")
        return await self._post(
            f"/extapis/{extapi_id}/routes/{route_id}",
            body=await async_maybe_transform(
                {
                    "body_params_desc": body_params_desc,
                    "method": method,
                    "name": name,
                    "path": path,
                    "path_params_desc": path_params_desc,
                    "query_params_desc": query_params_desc,
                },
                route_update_params.RouteUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtapiRoute,
        )

    async def list(
        self,
        extapi_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RouteListResponse:
        """
        获取某个 ExtAPI 的所有路径

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not extapi_id:
            raise ValueError(f"Expected a non-empty value for `extapi_id` but received {extapi_id!r}")
        return await self._get(
            f"/extapis/{extapi_id}/routes",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RouteListResponse,
        )

    async def delete(
        self,
        route_id: str,
        *,
        extapi_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        删除某个 ExtAPI Route

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not extapi_id:
            raise ValueError(f"Expected a non-empty value for `extapi_id` but received {extapi_id!r}")
        if not route_id:
            raise ValueError(f"Expected a non-empty value for `route_id` but received {route_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/extapis/{extapi_id}/routes/{route_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class RoutesResourceWithRawResponse:
    def __init__(self, routes: RoutesResource) -> None:
        self._routes = routes

        self.create = to_raw_response_wrapper(
            routes.create,
        )
        self.retrieve = to_raw_response_wrapper(
            routes.retrieve,
        )
        self.update = to_raw_response_wrapper(
            routes.update,
        )
        self.list = to_raw_response_wrapper(
            routes.list,
        )
        self.delete = to_raw_response_wrapper(
            routes.delete,
        )


class AsyncRoutesResourceWithRawResponse:
    def __init__(self, routes: AsyncRoutesResource) -> None:
        self._routes = routes

        self.create = async_to_raw_response_wrapper(
            routes.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            routes.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            routes.update,
        )
        self.list = async_to_raw_response_wrapper(
            routes.list,
        )
        self.delete = async_to_raw_response_wrapper(
            routes.delete,
        )


class RoutesResourceWithStreamingResponse:
    def __init__(self, routes: RoutesResource) -> None:
        self._routes = routes

        self.create = to_streamed_response_wrapper(
            routes.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            routes.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            routes.update,
        )
        self.list = to_streamed_response_wrapper(
            routes.list,
        )
        self.delete = to_streamed_response_wrapper(
            routes.delete,
        )


class AsyncRoutesResourceWithStreamingResponse:
    def __init__(self, routes: AsyncRoutesResource) -> None:
        self._routes = routes

        self.create = async_to_streamed_response_wrapper(
            routes.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            routes.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            routes.update,
        )
        self.list = async_to_streamed_response_wrapper(
            routes.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            routes.delete,
        )
