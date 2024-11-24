# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import overload

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    required_args,
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
from ...types.meta import Meta
from ..._base_client import make_request_options
from ...types.datasources import meta_create_params, meta_update_params, meta_annotate_params

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

    @overload
    def create(
        self,
        datasource_id: str,
        *,
        name: str,
        async_process_meta: bool | NotGiven = NOT_GIVEN,
        value_index: bool | NotGiven = NOT_GIVEN,
        schemas: Dict[str, meta_create_params.MetaCreateSchemas] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        创建数据源的 meta，如果已经存在，则删除旧的

        如果上传了 meta，则使用用户上传的数据创建。

        否则从数据源中自动获取。

        Args:
          name: metadata_name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        datasource_id: str,
        *,
        body: None,
        async_process_meta: bool | NotGiven = NOT_GIVEN,
        value_index: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        创建数据源的 meta，如果已经存在，则删除旧的

        如果上传了 meta，则使用用户上传的数据创建。

        否则从数据源中自动获取。

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["name"], ["body"])
    def create(
        self,
        datasource_id: str,
        *,
        name: str | NotGiven = NOT_GIVEN,
        async_process_meta: bool | NotGiven = NOT_GIVEN,
        value_index: bool | NotGiven = NOT_GIVEN,
        schemas: Dict[str, meta_create_params.MetaCreateSchemas] | NotGiven = NOT_GIVEN,
        body: None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        if not datasource_id:
            raise ValueError(f"Expected a non-empty value for `datasource_id` but received {datasource_id!r}")
        return self._post(
            f"/datasources/{datasource_id}/meta",
            body=maybe_transform(
                {
                    "name": name,
                    "schemas": schemas,
                    "body": body,
                },
                meta_create_params.MetaCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "async_process_meta": async_process_meta,
                        "value_index": value_index,
                    },
                    meta_create_params.MetaCreateParams,
                ),
            ),
            cast_to=object,
        )

    def retrieve(
        self,
        datasource_id: str,
        *,
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
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Meta,
        )

    @overload
    def update(
        self,
        datasource_id: str,
        *,
        name: str,
        schemas: Dict[str, meta_update_params.MetaCreateSchemas] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        用于更新 DB 类型的数据源的 Meta（增加新表或者删除老表）

        Args:
          name: metadata_name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        datasource_id: str,
        *,
        body: None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        用于更新 DB 类型的数据源的 Meta（增加新表或者删除老表）

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["name"], ["body"])
    def update(
        self,
        datasource_id: str,
        *,
        name: str | NotGiven = NOT_GIVEN,
        schemas: Dict[str, meta_update_params.MetaCreateSchemas] | NotGiven = NOT_GIVEN,
        body: None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        if not datasource_id:
            raise ValueError(f"Expected a non-empty value for `datasource_id` but received {datasource_id!r}")
        return self._put(
            f"/datasources/{datasource_id}/meta",
            body=maybe_transform(
                {
                    "name": name,
                    "schemas": schemas,
                    "body": body,
                },
                meta_update_params.MetaUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def annotate(
        self,
        datasource_id: str,
        *,
        schemas: Dict[str, meta_annotate_params.Schemas],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        修改数据 meta 的描述，用来修改表和字段的备注

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not datasource_id:
            raise ValueError(f"Expected a non-empty value for `datasource_id` but received {datasource_id!r}")
        return self._patch(
            f"/datasources/{datasource_id}/meta",
            body=maybe_transform({"schemas": schemas}, meta_annotate_params.MetaAnnotateParams),
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

    @overload
    async def create(
        self,
        datasource_id: str,
        *,
        name: str,
        async_process_meta: bool | NotGiven = NOT_GIVEN,
        value_index: bool | NotGiven = NOT_GIVEN,
        schemas: Dict[str, meta_create_params.MetaCreateSchemas] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        创建数据源的 meta，如果已经存在，则删除旧的

        如果上传了 meta，则使用用户上传的数据创建。

        否则从数据源中自动获取。

        Args:
          name: metadata_name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        datasource_id: str,
        *,
        body: None,
        async_process_meta: bool | NotGiven = NOT_GIVEN,
        value_index: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        创建数据源的 meta，如果已经存在，则删除旧的

        如果上传了 meta，则使用用户上传的数据创建。

        否则从数据源中自动获取。

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["name"], ["body"])
    async def create(
        self,
        datasource_id: str,
        *,
        name: str | NotGiven = NOT_GIVEN,
        async_process_meta: bool | NotGiven = NOT_GIVEN,
        value_index: bool | NotGiven = NOT_GIVEN,
        schemas: Dict[str, meta_create_params.MetaCreateSchemas] | NotGiven = NOT_GIVEN,
        body: None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        if not datasource_id:
            raise ValueError(f"Expected a non-empty value for `datasource_id` but received {datasource_id!r}")
        return await self._post(
            f"/datasources/{datasource_id}/meta",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "schemas": schemas,
                    "body": body,
                },
                meta_create_params.MetaCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "async_process_meta": async_process_meta,
                        "value_index": value_index,
                    },
                    meta_create_params.MetaCreateParams,
                ),
            ),
            cast_to=object,
        )

    async def retrieve(
        self,
        datasource_id: str,
        *,
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
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Meta,
        )

    @overload
    async def update(
        self,
        datasource_id: str,
        *,
        name: str,
        schemas: Dict[str, meta_update_params.MetaCreateSchemas] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        用于更新 DB 类型的数据源的 Meta（增加新表或者删除老表）

        Args:
          name: metadata_name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        datasource_id: str,
        *,
        body: None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        用于更新 DB 类型的数据源的 Meta（增加新表或者删除老表）

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["name"], ["body"])
    async def update(
        self,
        datasource_id: str,
        *,
        name: str | NotGiven = NOT_GIVEN,
        schemas: Dict[str, meta_update_params.MetaCreateSchemas] | NotGiven = NOT_GIVEN,
        body: None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        if not datasource_id:
            raise ValueError(f"Expected a non-empty value for `datasource_id` but received {datasource_id!r}")
        return await self._put(
            f"/datasources/{datasource_id}/meta",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "schemas": schemas,
                    "body": body,
                },
                meta_update_params.MetaUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def annotate(
        self,
        datasource_id: str,
        *,
        schemas: Dict[str, meta_annotate_params.Schemas],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        修改数据 meta 的描述，用来修改表和字段的备注

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not datasource_id:
            raise ValueError(f"Expected a non-empty value for `datasource_id` but received {datasource_id!r}")
        return await self._patch(
            f"/datasources/{datasource_id}/meta",
            body=await async_maybe_transform({"schemas": schemas}, meta_annotate_params.MetaAnnotateParams),
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
        self.annotate = to_raw_response_wrapper(
            meta.annotate,
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
        self.annotate = async_to_raw_response_wrapper(
            meta.annotate,
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
        self.annotate = to_streamed_response_wrapper(
            meta.annotate,
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
        self.annotate = async_to_streamed_response_wrapper(
            meta.annotate,
        )
