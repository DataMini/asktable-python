# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict

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
from ...types.datasources import meta_update_params, meta_retrieve_params
from ...types.datasources.meta import Meta

__all__ = ["MetaResource", "AsyncMetaResource"]


class MetaResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MetaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DataMini/asktable-python#accessing-raw-response-data-eg-headers
        """
        return MetaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MetaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DataMini/asktable-python#with_streaming_response
        """
        return MetaResourceWithStreamingResponse(self)

    def create(
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
        更新元数据（自动异步）

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not datasource_id:
            raise ValueError(f"Expected a non-empty value for `datasource_id` but received {datasource_id!r}")
        return self._post(
            f"/datasources/{datasource_id}/meta",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def retrieve(
        self,
        datasource_id: str,
        *,
        from_where: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Meta:
        """
        从数据源中获取最新的元数据

        Args:
          from_where: 获取元数据的来源

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not datasource_id:
            raise ValueError(f"Expected a non-empty value for `datasource_id` but received {datasource_id!r}")
        return self._get(
            f"/datasources/{datasource_id}/meta",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"from_where": from_where}, meta_retrieve_params.MetaRetrieveParams),
            ),
            cast_to=Meta,
        )

    def update(
        self,
        *,
        path_datasource_id: str,
        body_datasource_id: str,
        name: str,
        schemas: Dict[str, meta_update_params.Schemas] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        修改元数据（手动上传）

        Args:
          body_datasource_id: datasource_id

          name: metadata_name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_datasource_id:
            raise ValueError(f"Expected a non-empty value for `path_datasource_id` but received {path_datasource_id!r}")
        return self._put(
            f"/datasources/{path_datasource_id}/meta",
            body=maybe_transform(
                {
                    "datasource_id": body_datasource_id,
                    "name": name,
                    "schemas": schemas,
                },
                meta_update_params.MetaUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncMetaResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMetaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DataMini/asktable-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMetaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMetaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DataMini/asktable-python#with_streaming_response
        """
        return AsyncMetaResourceWithStreamingResponse(self)

    async def create(
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
        更新元数据（自动异步）

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not datasource_id:
            raise ValueError(f"Expected a non-empty value for `datasource_id` but received {datasource_id!r}")
        return await self._post(
            f"/datasources/{datasource_id}/meta",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def retrieve(
        self,
        datasource_id: str,
        *,
        from_where: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Meta:
        """
        从数据源中获取最新的元数据

        Args:
          from_where: 获取元数据的来源

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not datasource_id:
            raise ValueError(f"Expected a non-empty value for `datasource_id` but received {datasource_id!r}")
        return await self._get(
            f"/datasources/{datasource_id}/meta",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"from_where": from_where}, meta_retrieve_params.MetaRetrieveParams),
            ),
            cast_to=Meta,
        )

    async def update(
        self,
        *,
        path_datasource_id: str,
        body_datasource_id: str,
        name: str,
        schemas: Dict[str, meta_update_params.Schemas] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        修改元数据（手动上传）

        Args:
          body_datasource_id: datasource_id

          name: metadata_name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_datasource_id:
            raise ValueError(f"Expected a non-empty value for `path_datasource_id` but received {path_datasource_id!r}")
        return await self._put(
            f"/datasources/{path_datasource_id}/meta",
            body=await async_maybe_transform(
                {
                    "datasource_id": body_datasource_id,
                    "name": name,
                    "schemas": schemas,
                },
                meta_update_params.MetaUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class MetaResourceWithRawResponse:
    def __init__(self, meta: MetaResource) -> None:
        self._meta = meta

        self.create = to_raw_response_wrapper(
            meta.create,
        )
        self.retrieve = to_raw_response_wrapper(
            meta.retrieve,
        )
        self.update = to_raw_response_wrapper(
            meta.update,
        )


class AsyncMetaResourceWithRawResponse:
    def __init__(self, meta: AsyncMetaResource) -> None:
        self._meta = meta

        self.create = async_to_raw_response_wrapper(
            meta.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            meta.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            meta.update,
        )


class MetaResourceWithStreamingResponse:
    def __init__(self, meta: MetaResource) -> None:
        self._meta = meta

        self.create = to_streamed_response_wrapper(
            meta.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            meta.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            meta.update,
        )


class AsyncMetaResourceWithStreamingResponse:
    def __init__(self, meta: AsyncMetaResource) -> None:
        self._meta = meta

        self.create = async_to_streamed_response_wrapper(
            meta.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            meta.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            meta.update,
        )
