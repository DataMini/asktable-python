# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Mapping, Optional, cast
from typing_extensions import Literal

import httpx

from .meta import (
    MetaResource,
    AsyncMetaResource,
    MetaResourceWithRawResponse,
    AsyncMetaResourceWithRawResponse,
    MetaResourceWithStreamingResponse,
    AsyncMetaResourceWithStreamingResponse,
)
from ...types import (
    datasource_list_params,
    datasource_create_params,
    datasource_update_params,
    datasource_create_from_file_params,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven, FileTypes
from ..._utils import (
    extract_files,
    maybe_transform,
    deepcopy_minimal,
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
from .upload_params import (
    UploadParamsResource,
    AsyncUploadParamsResource,
    UploadParamsResourceWithRawResponse,
    AsyncUploadParamsResourceWithRawResponse,
    UploadParamsResourceWithStreamingResponse,
    AsyncUploadParamsResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from ...types.data_source import DataSource
from ...types.datasource_list_response import DatasourceListResponse

__all__ = ["DatasourcesResource", "AsyncDatasourcesResource"]


class DatasourcesResource(SyncAPIResource):
    @cached_property
    def meta(self) -> MetaResource:
        return MetaResource(self._client)

    @cached_property
    def upload_params(self) -> UploadParamsResource:
        return UploadParamsResource(self._client)

    @cached_property
    def with_raw_response(self) -> DatasourcesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DataMini/asktable-python#accessing-raw-response-data-eg-headers
        """
        return DatasourcesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DatasourcesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DataMini/asktable-python#with_streaming_response
        """
        return DatasourcesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        access_config: datasource_create_params.AccessConfig,
        engine: Literal["mysql", "tidb", "postgresql", "oceanbase", "clickhouse", "csv", "excel"],
        async_process_meta: bool | NotGiven = NOT_GIVEN,
        skip_process_meta: bool | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DataSource:
        """
        创建数据源

        Args:
          access_config: 不同引擎有不同的配置

          engine: 数据源引擎

          async_process_meta: 是否异步处理元数据

          skip_process_meta: 是否跳过元数据处理

          name: 数据源的名称

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/datasources",
            body=maybe_transform(
                {
                    "access_config": access_config,
                    "engine": engine,
                    "name": name,
                },
                datasource_create_params.DatasourceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "async_process_meta": async_process_meta,
                        "skip_process_meta": skip_process_meta,
                    },
                    datasource_create_params.DatasourceCreateParams,
                ),
            ),
            cast_to=DataSource,
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
    ) -> DataSource:
        """
        获取某个数据源

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not datasource_id:
            raise ValueError(f"Expected a non-empty value for `datasource_id` but received {datasource_id!r}")
        return self._get(
            f"/datasources/{datasource_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataSource,
        )

    def update(
        self,
        datasource_id: str,
        *,
        access_config: Optional[datasource_update_params.AccessConfig] | NotGiven = NOT_GIVEN,
        field_count: Optional[int] | NotGiven = NOT_GIVEN,
        meta_error: Optional[str] | NotGiven = NOT_GIVEN,
        meta_status: Optional[Literal["processing", "failed", "success", "unprocessed"]] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        sample_questions: Optional[str] | NotGiven = NOT_GIVEN,
        schema_count: Optional[int] | NotGiven = NOT_GIVEN,
        table_count: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DataSource:
        """
        修改数据源

        Args:
          access_config: 不同引擎有不同的配置

          field_count: 字段数量

          meta_error: 元数据处理错误

          meta_status: 元数据处理状态

          name: 数据源的名称

          sample_questions: 示例问题

          schema_count: 库数量

          table_count: 表数量

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not datasource_id:
            raise ValueError(f"Expected a non-empty value for `datasource_id` but received {datasource_id!r}")
        return self._patch(
            f"/datasources/{datasource_id}",
            body=maybe_transform(
                {
                    "access_config": access_config,
                    "field_count": field_count,
                    "meta_error": meta_error,
                    "meta_status": meta_status,
                    "name": name,
                    "sample_questions": sample_questions,
                    "schema_count": schema_count,
                    "table_count": table_count,
                },
                datasource_update_params.DatasourceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataSource,
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
    ) -> DatasourceListResponse:
        """
        获取数据源列表

        Args:
          page: Page number

          size: Page size

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/datasources",
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
                    datasource_list_params.DatasourceListParams,
                ),
            ),
            cast_to=DatasourceListResponse,
        )

    def delete(
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
        删除数据源

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not datasource_id:
            raise ValueError(f"Expected a non-empty value for `datasource_id` but received {datasource_id!r}")
        return self._delete(
            f"/datasources/{datasource_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def create_from_file(
        self,
        *,
        name: str,
        file: FileTypes,
        async_process_meta: bool | NotGiven = NOT_GIVEN,
        skip_process_meta: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DataSource:
        """
        上传文件并创建数据源

        Args:
          async_process_meta: 是否异步处理元数据

          skip_process_meta: 是否跳过元数据处理

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal({"file": file})
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/datasources/file",
            body=maybe_transform(body, datasource_create_from_file_params.DatasourceCreateFromFileParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "name": name,
                        "async_process_meta": async_process_meta,
                        "skip_process_meta": skip_process_meta,
                    },
                    datasource_create_from_file_params.DatasourceCreateFromFileParams,
                ),
            ),
            cast_to=DataSource,
        )


class AsyncDatasourcesResource(AsyncAPIResource):
    @cached_property
    def meta(self) -> AsyncMetaResource:
        return AsyncMetaResource(self._client)

    @cached_property
    def upload_params(self) -> AsyncUploadParamsResource:
        return AsyncUploadParamsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDatasourcesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DataMini/asktable-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDatasourcesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDatasourcesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DataMini/asktable-python#with_streaming_response
        """
        return AsyncDatasourcesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        access_config: datasource_create_params.AccessConfig,
        engine: Literal["mysql", "tidb", "postgresql", "oceanbase", "clickhouse", "csv", "excel"],
        async_process_meta: bool | NotGiven = NOT_GIVEN,
        skip_process_meta: bool | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DataSource:
        """
        创建数据源

        Args:
          access_config: 不同引擎有不同的配置

          engine: 数据源引擎

          async_process_meta: 是否异步处理元数据

          skip_process_meta: 是否跳过元数据处理

          name: 数据源的名称

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/datasources",
            body=await async_maybe_transform(
                {
                    "access_config": access_config,
                    "engine": engine,
                    "name": name,
                },
                datasource_create_params.DatasourceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "async_process_meta": async_process_meta,
                        "skip_process_meta": skip_process_meta,
                    },
                    datasource_create_params.DatasourceCreateParams,
                ),
            ),
            cast_to=DataSource,
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
    ) -> DataSource:
        """
        获取某个数据源

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not datasource_id:
            raise ValueError(f"Expected a non-empty value for `datasource_id` but received {datasource_id!r}")
        return await self._get(
            f"/datasources/{datasource_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataSource,
        )

    async def update(
        self,
        datasource_id: str,
        *,
        access_config: Optional[datasource_update_params.AccessConfig] | NotGiven = NOT_GIVEN,
        field_count: Optional[int] | NotGiven = NOT_GIVEN,
        meta_error: Optional[str] | NotGiven = NOT_GIVEN,
        meta_status: Optional[Literal["processing", "failed", "success", "unprocessed"]] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        sample_questions: Optional[str] | NotGiven = NOT_GIVEN,
        schema_count: Optional[int] | NotGiven = NOT_GIVEN,
        table_count: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DataSource:
        """
        修改数据源

        Args:
          access_config: 不同引擎有不同的配置

          field_count: 字段数量

          meta_error: 元数据处理错误

          meta_status: 元数据处理状态

          name: 数据源的名称

          sample_questions: 示例问题

          schema_count: 库数量

          table_count: 表数量

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not datasource_id:
            raise ValueError(f"Expected a non-empty value for `datasource_id` but received {datasource_id!r}")
        return await self._patch(
            f"/datasources/{datasource_id}",
            body=await async_maybe_transform(
                {
                    "access_config": access_config,
                    "field_count": field_count,
                    "meta_error": meta_error,
                    "meta_status": meta_status,
                    "name": name,
                    "sample_questions": sample_questions,
                    "schema_count": schema_count,
                    "table_count": table_count,
                },
                datasource_update_params.DatasourceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataSource,
        )

    async def list(
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
    ) -> DatasourceListResponse:
        """
        获取数据源列表

        Args:
          page: Page number

          size: Page size

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/datasources",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "name": name,
                        "page": page,
                        "size": size,
                    },
                    datasource_list_params.DatasourceListParams,
                ),
            ),
            cast_to=DatasourceListResponse,
        )

    async def delete(
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
        删除数据源

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not datasource_id:
            raise ValueError(f"Expected a non-empty value for `datasource_id` but received {datasource_id!r}")
        return await self._delete(
            f"/datasources/{datasource_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def create_from_file(
        self,
        *,
        name: str,
        file: FileTypes,
        async_process_meta: bool | NotGiven = NOT_GIVEN,
        skip_process_meta: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DataSource:
        """
        上传文件并创建数据源

        Args:
          async_process_meta: 是否异步处理元数据

          skip_process_meta: 是否跳过元数据处理

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal({"file": file})
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/datasources/file",
            body=await async_maybe_transform(body, datasource_create_from_file_params.DatasourceCreateFromFileParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "name": name,
                        "async_process_meta": async_process_meta,
                        "skip_process_meta": skip_process_meta,
                    },
                    datasource_create_from_file_params.DatasourceCreateFromFileParams,
                ),
            ),
            cast_to=DataSource,
        )


class DatasourcesResourceWithRawResponse:
    def __init__(self, datasources: DatasourcesResource) -> None:
        self._datasources = datasources

        self.create = to_raw_response_wrapper(
            datasources.create,
        )
        self.retrieve = to_raw_response_wrapper(
            datasources.retrieve,
        )
        self.update = to_raw_response_wrapper(
            datasources.update,
        )
        self.list = to_raw_response_wrapper(
            datasources.list,
        )
        self.delete = to_raw_response_wrapper(
            datasources.delete,
        )
        self.create_from_file = to_raw_response_wrapper(
            datasources.create_from_file,
        )

    @cached_property
    def meta(self) -> MetaResourceWithRawResponse:
        return MetaResourceWithRawResponse(self._datasources.meta)

    @cached_property
    def upload_params(self) -> UploadParamsResourceWithRawResponse:
        return UploadParamsResourceWithRawResponse(self._datasources.upload_params)


class AsyncDatasourcesResourceWithRawResponse:
    def __init__(self, datasources: AsyncDatasourcesResource) -> None:
        self._datasources = datasources

        self.create = async_to_raw_response_wrapper(
            datasources.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            datasources.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            datasources.update,
        )
        self.list = async_to_raw_response_wrapper(
            datasources.list,
        )
        self.delete = async_to_raw_response_wrapper(
            datasources.delete,
        )
        self.create_from_file = async_to_raw_response_wrapper(
            datasources.create_from_file,
        )

    @cached_property
    def meta(self) -> AsyncMetaResourceWithRawResponse:
        return AsyncMetaResourceWithRawResponse(self._datasources.meta)

    @cached_property
    def upload_params(self) -> AsyncUploadParamsResourceWithRawResponse:
        return AsyncUploadParamsResourceWithRawResponse(self._datasources.upload_params)


class DatasourcesResourceWithStreamingResponse:
    def __init__(self, datasources: DatasourcesResource) -> None:
        self._datasources = datasources

        self.create = to_streamed_response_wrapper(
            datasources.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            datasources.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            datasources.update,
        )
        self.list = to_streamed_response_wrapper(
            datasources.list,
        )
        self.delete = to_streamed_response_wrapper(
            datasources.delete,
        )
        self.create_from_file = to_streamed_response_wrapper(
            datasources.create_from_file,
        )

    @cached_property
    def meta(self) -> MetaResourceWithStreamingResponse:
        return MetaResourceWithStreamingResponse(self._datasources.meta)

    @cached_property
    def upload_params(self) -> UploadParamsResourceWithStreamingResponse:
        return UploadParamsResourceWithStreamingResponse(self._datasources.upload_params)


class AsyncDatasourcesResourceWithStreamingResponse:
    def __init__(self, datasources: AsyncDatasourcesResource) -> None:
        self._datasources = datasources

        self.create = async_to_streamed_response_wrapper(
            datasources.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            datasources.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            datasources.update,
        )
        self.list = async_to_streamed_response_wrapper(
            datasources.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            datasources.delete,
        )
        self.create_from_file = async_to_streamed_response_wrapper(
            datasources.create_from_file,
        )

    @cached_property
    def meta(self) -> AsyncMetaResourceWithStreamingResponse:
        return AsyncMetaResourceWithStreamingResponse(self._datasources.meta)

    @cached_property
    def upload_params(self) -> AsyncUploadParamsResourceWithStreamingResponse:
        return AsyncUploadParamsResourceWithStreamingResponse(self._datasources.upload_params)
