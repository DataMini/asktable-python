# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
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
    datasource_add_file_params,
    datasource_update_field_params,
)
from .indexes import (
    IndexesResource,
    AsyncIndexesResource,
    IndexesResourceWithRawResponse,
    AsyncIndexesResourceWithRawResponse,
    IndexesResourceWithStreamingResponse,
    AsyncIndexesResourceWithStreamingResponse,
)
from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncPage, AsyncPage
from .upload_params import (
    UploadParamsResource,
    AsyncUploadParamsResource,
    UploadParamsResourceWithRawResponse,
    AsyncUploadParamsResourceWithRawResponse,
    UploadParamsResourceWithStreamingResponse,
    AsyncUploadParamsResourceWithStreamingResponse,
)
from ..._base_client import AsyncPaginator, make_request_options
from ...types.datasource import Datasource
from ...types.datasource_retrieve_response import DatasourceRetrieveResponse
from ...types.datasource_retrieve_runtime_meta_response import DatasourceRetrieveRuntimeMetaResponse

__all__ = ["DatasourcesResource", "AsyncDatasourcesResource"]


class DatasourcesResource(SyncAPIResource):
    """数据源管理"""

    @cached_property
    def meta(self) -> MetaResource:
        """数据源管理"""
        return MetaResource(self._client)

    @cached_property
    def upload_params(self) -> UploadParamsResource:
        """数据源管理"""
        return UploadParamsResource(self._client)

    @cached_property
    def indexes(self) -> IndexesResource:
        """索引管理"""
        return IndexesResource(self._client)

    @cached_property
    def with_raw_response(self) -> DatasourcesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
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
        engine: Literal[
            "mysql",
            "tidb",
            "postgresql",
            "oceanbase",
            "clickhouse",
            "excel",
            "starrocks",
            "hive",
            "oracle",
            "polardbmysql",
            "polardbpg",
            "dameng",
            "adbmysql",
            "adbpostgres",
            "xugu",
            "doris",
            "greenplum",
            "selectdb",
            "databend",
            "sqlserver",
            "mogdb",
            "hologres",
            "maxcompute",
            "gaussdb",
            "tdsqlmysql",
            "tdsqlpg",
            "kingbasees",
            "gbase8c",
            "yashandb",
            "gbase8a",
            "gaussdbdws",
            "bigquery",
            "dap",
            "duckdb",
            "workbook",
        ],
        access_config: Optional[datasource_create_params.AccessConfig] | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Datasource:
        """
        创建一个新的数据源

        Args:
          engine: 数据源引擎

          access_config: 不同引擎有不同的配置

          name: 数据源的名称

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/datasources",
            body=maybe_transform(
                {
                    "engine": engine,
                    "access_config": access_config,
                    "name": name,
                },
                datasource_create_params.DatasourceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Datasource,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DatasourceRetrieveResponse:
        """
        根据 id 获取指定数据源

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not datasource_id:
            raise ValueError(f"Expected a non-empty value for `datasource_id` but received {datasource_id!r}")
        return self._get(
            path_template("/v1/datasources/{datasource_id}", datasource_id=datasource_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatasourceRetrieveResponse,
        )

    def update(
        self,
        datasource_id: str,
        *,
        access_config: Optional[datasource_update_params.AccessConfig] | Omit = omit,
        desc: Optional[str] | Omit = omit,
        engine: Optional[
            Literal[
                "mysql",
                "tidb",
                "postgresql",
                "oceanbase",
                "clickhouse",
                "excel",
                "starrocks",
                "hive",
                "oracle",
                "polardbmysql",
                "polardbpg",
                "dameng",
                "adbmysql",
                "adbpostgres",
                "xugu",
                "doris",
                "greenplum",
                "selectdb",
                "databend",
                "sqlserver",
                "mogdb",
                "hologres",
                "maxcompute",
                "gaussdb",
                "tdsqlmysql",
                "tdsqlpg",
                "kingbasees",
                "gbase8c",
                "yashandb",
                "gbase8a",
                "gaussdbdws",
                "bigquery",
                "dap",
                "duckdb",
                "workbook",
            ]
        ]
        | Omit = omit,
        field_count: Optional[int] | Omit = omit,
        meta_status: Optional[Literal["unavailable", "available"]] | Omit = omit,
        name: Optional[str] | Omit = omit,
        query_timeout_seconds: Optional[int] | Omit = omit,
        sample_questions: Optional[SequenceNotStr[str]] | Omit = omit,
        schema_count: Optional[int] | Omit = omit,
        sync_error: Optional[Dict[str, object]] | Omit = omit,
        sync_status: Optional[Literal["queued", "processing", "success", "failed", "warning"]] | Omit = omit,
        table_count: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Datasource:
        """
        更新指定数据源信息

        Args:
          access_config: 不同引擎有不同的配置

          desc: 数据源描述

          engine: 数据源引擎

          field_count: 字段数量

          meta_status: 数据源可用性

          name: 数据源的名称

          query_timeout_seconds: 查询超时秒数；空值表示继承系统配置

          sample_questions: 示例问题

          schema_count: 库数量

          sync_error: 同步错误信息

          sync_status: 同步状态

          table_count: 表数量

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not datasource_id:
            raise ValueError(f"Expected a non-empty value for `datasource_id` but received {datasource_id!r}")
        return self._patch(
            path_template("/v1/datasources/{datasource_id}", datasource_id=datasource_id),
            body=maybe_transform(
                {
                    "access_config": access_config,
                    "desc": desc,
                    "engine": engine,
                    "field_count": field_count,
                    "meta_status": meta_status,
                    "name": name,
                    "query_timeout_seconds": query_timeout_seconds,
                    "sample_questions": sample_questions,
                    "schema_count": schema_count,
                    "sync_error": sync_error,
                    "sync_status": sync_status,
                    "table_count": table_count,
                },
                datasource_update_params.DatasourceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Datasource,
        )

    def list(
        self,
        *,
        name: Optional[str] | Omit = omit,
        page: int | Omit = omit,
        size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[Datasource]:
        """
        获取所有的数据源

        Args:
          page: Page number

          size: Page size

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/datasources",
            page=SyncPage[Datasource],
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
            model=Datasource,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        根据 id 删除指定数据源

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not datasource_id:
            raise ValueError(f"Expected a non-empty value for `datasource_id` but received {datasource_id!r}")
        return self._delete(
            path_template("/v1/datasources/{datasource_id}", datasource_id=datasource_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def add_file(
        self,
        datasource_id: str,
        *,
        file: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        为数据源添加文件

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not datasource_id:
            raise ValueError(f"Expected a non-empty value for `datasource_id` but received {datasource_id!r}")
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            path_template("/v1/datasources/{datasource_id}/files", datasource_id=datasource_id),
            body=maybe_transform({"file": file}, datasource_add_file_params.DatasourceAddFileParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def delete_file(
        self,
        file_id: str,
        *,
        datasource_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        删除数据源的单个文件

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not datasource_id:
            raise ValueError(f"Expected a non-empty value for `datasource_id` but received {datasource_id!r}")
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        return self._delete(
            path_template(
                "/v1/datasources/{datasource_id}/files/{file_id}", datasource_id=datasource_id, file_id=file_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def retrieve_runtime_meta(
        self,
        datasource_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DatasourceRetrieveRuntimeMetaResponse:
        """
        获取指定数据源的运行时元数据

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not datasource_id:
            raise ValueError(f"Expected a non-empty value for `datasource_id` but received {datasource_id!r}")
        return self._get(
            path_template("/v1/datasources/{datasource_id}/runtime-meta", datasource_id=datasource_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatasourceRetrieveRuntimeMetaResponse,
        )

    def update_field(
        self,
        datasource_id: str,
        *,
        field_name: str,
        schema_name: str,
        table_name: str,
        identifiable_type: Optional[
            Literal["plain", "person_name", "email", "ssn", "id", "phone", "address", "company", "bank_card"]
        ]
        | Omit = omit,
        semantic_type: Optional[
            Literal[
                "PK",
                "FK",
                "Quantity",
                "Share",
                "Percentage",
                "Currency",
                "Income",
                "Discount",
                "Price",
                "GrossMargin",
                "Cost",
                "Score",
                "Duration",
                "Latitude",
                "Longitude",
                "City",
                "State",
                "Country",
                "ZipCode",
                "Email",
                "URL",
                "ImageURL",
                "AvatarURL",
                "Category",
                "Enum",
                "Name",
                "Title",
                "Description",
                "Comment",
                "SerializedJSON",
                "IPAddress",
                "CreationTimestamp",
                "CreationTime",
                "CreationDate",
                "JoinTimestamp",
                "JoinTime",
                "JoinDate",
                "CancelationTimestamp",
                "CancelationTime",
                "CancelationDate",
                "DeletionTimestamp",
                "DeletionTime",
                "DeletionDate",
                "UpdatedTimestamp",
                "UpdatedTime",
                "UpdatedDate",
                "Birthdate",
                "Source",
                "Author",
                "Owner",
                "Company",
                "Product",
                "Subscription",
            ]
        ]
        | Omit = omit,
        visibility: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        更新数据源的某个字段的描述

        Args:
          identifiable_type: identifiable type

          semantic_type: 字段语义类型，协议照抄 Metabase（值 = :type/ 前缀去除后的名字）。

              PK/FK 是关系类型，与语义共用一列（Metabase 同款）：来自同步元数据，非推断产物
              ，classifier 一律跳过。其余值由 classifier 推断或人工设置。

          visibility: field visibility

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not datasource_id:
            raise ValueError(f"Expected a non-empty value for `datasource_id` but received {datasource_id!r}")
        return self._patch(
            path_template("/v1/datasources/{datasource_id}/field", datasource_id=datasource_id),
            body=maybe_transform(
                {
                    "identifiable_type": identifiable_type,
                    "semantic_type": semantic_type,
                    "visibility": visibility,
                },
                datasource_update_field_params.DatasourceUpdateFieldParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "field_name": field_name,
                        "schema_name": schema_name,
                        "table_name": table_name,
                    },
                    datasource_update_field_params.DatasourceUpdateFieldParams,
                ),
            ),
            cast_to=object,
        )


class AsyncDatasourcesResource(AsyncAPIResource):
    """数据源管理"""

    @cached_property
    def meta(self) -> AsyncMetaResource:
        """数据源管理"""
        return AsyncMetaResource(self._client)

    @cached_property
    def upload_params(self) -> AsyncUploadParamsResource:
        """数据源管理"""
        return AsyncUploadParamsResource(self._client)

    @cached_property
    def indexes(self) -> AsyncIndexesResource:
        """索引管理"""
        return AsyncIndexesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDatasourcesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
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
        engine: Literal[
            "mysql",
            "tidb",
            "postgresql",
            "oceanbase",
            "clickhouse",
            "excel",
            "starrocks",
            "hive",
            "oracle",
            "polardbmysql",
            "polardbpg",
            "dameng",
            "adbmysql",
            "adbpostgres",
            "xugu",
            "doris",
            "greenplum",
            "selectdb",
            "databend",
            "sqlserver",
            "mogdb",
            "hologres",
            "maxcompute",
            "gaussdb",
            "tdsqlmysql",
            "tdsqlpg",
            "kingbasees",
            "gbase8c",
            "yashandb",
            "gbase8a",
            "gaussdbdws",
            "bigquery",
            "dap",
            "duckdb",
            "workbook",
        ],
        access_config: Optional[datasource_create_params.AccessConfig] | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Datasource:
        """
        创建一个新的数据源

        Args:
          engine: 数据源引擎

          access_config: 不同引擎有不同的配置

          name: 数据源的名称

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/datasources",
            body=await async_maybe_transform(
                {
                    "engine": engine,
                    "access_config": access_config,
                    "name": name,
                },
                datasource_create_params.DatasourceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Datasource,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DatasourceRetrieveResponse:
        """
        根据 id 获取指定数据源

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not datasource_id:
            raise ValueError(f"Expected a non-empty value for `datasource_id` but received {datasource_id!r}")
        return await self._get(
            path_template("/v1/datasources/{datasource_id}", datasource_id=datasource_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatasourceRetrieveResponse,
        )

    async def update(
        self,
        datasource_id: str,
        *,
        access_config: Optional[datasource_update_params.AccessConfig] | Omit = omit,
        desc: Optional[str] | Omit = omit,
        engine: Optional[
            Literal[
                "mysql",
                "tidb",
                "postgresql",
                "oceanbase",
                "clickhouse",
                "excel",
                "starrocks",
                "hive",
                "oracle",
                "polardbmysql",
                "polardbpg",
                "dameng",
                "adbmysql",
                "adbpostgres",
                "xugu",
                "doris",
                "greenplum",
                "selectdb",
                "databend",
                "sqlserver",
                "mogdb",
                "hologres",
                "maxcompute",
                "gaussdb",
                "tdsqlmysql",
                "tdsqlpg",
                "kingbasees",
                "gbase8c",
                "yashandb",
                "gbase8a",
                "gaussdbdws",
                "bigquery",
                "dap",
                "duckdb",
                "workbook",
            ]
        ]
        | Omit = omit,
        field_count: Optional[int] | Omit = omit,
        meta_status: Optional[Literal["unavailable", "available"]] | Omit = omit,
        name: Optional[str] | Omit = omit,
        query_timeout_seconds: Optional[int] | Omit = omit,
        sample_questions: Optional[SequenceNotStr[str]] | Omit = omit,
        schema_count: Optional[int] | Omit = omit,
        sync_error: Optional[Dict[str, object]] | Omit = omit,
        sync_status: Optional[Literal["queued", "processing", "success", "failed", "warning"]] | Omit = omit,
        table_count: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Datasource:
        """
        更新指定数据源信息

        Args:
          access_config: 不同引擎有不同的配置

          desc: 数据源描述

          engine: 数据源引擎

          field_count: 字段数量

          meta_status: 数据源可用性

          name: 数据源的名称

          query_timeout_seconds: 查询超时秒数；空值表示继承系统配置

          sample_questions: 示例问题

          schema_count: 库数量

          sync_error: 同步错误信息

          sync_status: 同步状态

          table_count: 表数量

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not datasource_id:
            raise ValueError(f"Expected a non-empty value for `datasource_id` but received {datasource_id!r}")
        return await self._patch(
            path_template("/v1/datasources/{datasource_id}", datasource_id=datasource_id),
            body=await async_maybe_transform(
                {
                    "access_config": access_config,
                    "desc": desc,
                    "engine": engine,
                    "field_count": field_count,
                    "meta_status": meta_status,
                    "name": name,
                    "query_timeout_seconds": query_timeout_seconds,
                    "sample_questions": sample_questions,
                    "schema_count": schema_count,
                    "sync_error": sync_error,
                    "sync_status": sync_status,
                    "table_count": table_count,
                },
                datasource_update_params.DatasourceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Datasource,
        )

    def list(
        self,
        *,
        name: Optional[str] | Omit = omit,
        page: int | Omit = omit,
        size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Datasource, AsyncPage[Datasource]]:
        """
        获取所有的数据源

        Args:
          page: Page number

          size: Page size

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/datasources",
            page=AsyncPage[Datasource],
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
            model=Datasource,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        根据 id 删除指定数据源

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not datasource_id:
            raise ValueError(f"Expected a non-empty value for `datasource_id` but received {datasource_id!r}")
        return await self._delete(
            path_template("/v1/datasources/{datasource_id}", datasource_id=datasource_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def add_file(
        self,
        datasource_id: str,
        *,
        file: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        为数据源添加文件

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not datasource_id:
            raise ValueError(f"Expected a non-empty value for `datasource_id` but received {datasource_id!r}")
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            path_template("/v1/datasources/{datasource_id}/files", datasource_id=datasource_id),
            body=await async_maybe_transform({"file": file}, datasource_add_file_params.DatasourceAddFileParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def delete_file(
        self,
        file_id: str,
        *,
        datasource_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        删除数据源的单个文件

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not datasource_id:
            raise ValueError(f"Expected a non-empty value for `datasource_id` but received {datasource_id!r}")
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        return await self._delete(
            path_template(
                "/v1/datasources/{datasource_id}/files/{file_id}", datasource_id=datasource_id, file_id=file_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def retrieve_runtime_meta(
        self,
        datasource_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DatasourceRetrieveRuntimeMetaResponse:
        """
        获取指定数据源的运行时元数据

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not datasource_id:
            raise ValueError(f"Expected a non-empty value for `datasource_id` but received {datasource_id!r}")
        return await self._get(
            path_template("/v1/datasources/{datasource_id}/runtime-meta", datasource_id=datasource_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatasourceRetrieveRuntimeMetaResponse,
        )

    async def update_field(
        self,
        datasource_id: str,
        *,
        field_name: str,
        schema_name: str,
        table_name: str,
        identifiable_type: Optional[
            Literal["plain", "person_name", "email", "ssn", "id", "phone", "address", "company", "bank_card"]
        ]
        | Omit = omit,
        semantic_type: Optional[
            Literal[
                "PK",
                "FK",
                "Quantity",
                "Share",
                "Percentage",
                "Currency",
                "Income",
                "Discount",
                "Price",
                "GrossMargin",
                "Cost",
                "Score",
                "Duration",
                "Latitude",
                "Longitude",
                "City",
                "State",
                "Country",
                "ZipCode",
                "Email",
                "URL",
                "ImageURL",
                "AvatarURL",
                "Category",
                "Enum",
                "Name",
                "Title",
                "Description",
                "Comment",
                "SerializedJSON",
                "IPAddress",
                "CreationTimestamp",
                "CreationTime",
                "CreationDate",
                "JoinTimestamp",
                "JoinTime",
                "JoinDate",
                "CancelationTimestamp",
                "CancelationTime",
                "CancelationDate",
                "DeletionTimestamp",
                "DeletionTime",
                "DeletionDate",
                "UpdatedTimestamp",
                "UpdatedTime",
                "UpdatedDate",
                "Birthdate",
                "Source",
                "Author",
                "Owner",
                "Company",
                "Product",
                "Subscription",
            ]
        ]
        | Omit = omit,
        visibility: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        更新数据源的某个字段的描述

        Args:
          identifiable_type: identifiable type

          semantic_type: 字段语义类型，协议照抄 Metabase（值 = :type/ 前缀去除后的名字）。

              PK/FK 是关系类型，与语义共用一列（Metabase 同款）：来自同步元数据，非推断产物
              ，classifier 一律跳过。其余值由 classifier 推断或人工设置。

          visibility: field visibility

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not datasource_id:
            raise ValueError(f"Expected a non-empty value for `datasource_id` but received {datasource_id!r}")
        return await self._patch(
            path_template("/v1/datasources/{datasource_id}/field", datasource_id=datasource_id),
            body=await async_maybe_transform(
                {
                    "identifiable_type": identifiable_type,
                    "semantic_type": semantic_type,
                    "visibility": visibility,
                },
                datasource_update_field_params.DatasourceUpdateFieldParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "field_name": field_name,
                        "schema_name": schema_name,
                        "table_name": table_name,
                    },
                    datasource_update_field_params.DatasourceUpdateFieldParams,
                ),
            ),
            cast_to=object,
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
        self.add_file = to_raw_response_wrapper(
            datasources.add_file,
        )
        self.delete_file = to_raw_response_wrapper(
            datasources.delete_file,
        )
        self.retrieve_runtime_meta = to_raw_response_wrapper(
            datasources.retrieve_runtime_meta,
        )
        self.update_field = to_raw_response_wrapper(
            datasources.update_field,
        )

    @cached_property
    def meta(self) -> MetaResourceWithRawResponse:
        """数据源管理"""
        return MetaResourceWithRawResponse(self._datasources.meta)

    @cached_property
    def upload_params(self) -> UploadParamsResourceWithRawResponse:
        """数据源管理"""
        return UploadParamsResourceWithRawResponse(self._datasources.upload_params)

    @cached_property
    def indexes(self) -> IndexesResourceWithRawResponse:
        """索引管理"""
        return IndexesResourceWithRawResponse(self._datasources.indexes)


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
        self.add_file = async_to_raw_response_wrapper(
            datasources.add_file,
        )
        self.delete_file = async_to_raw_response_wrapper(
            datasources.delete_file,
        )
        self.retrieve_runtime_meta = async_to_raw_response_wrapper(
            datasources.retrieve_runtime_meta,
        )
        self.update_field = async_to_raw_response_wrapper(
            datasources.update_field,
        )

    @cached_property
    def meta(self) -> AsyncMetaResourceWithRawResponse:
        """数据源管理"""
        return AsyncMetaResourceWithRawResponse(self._datasources.meta)

    @cached_property
    def upload_params(self) -> AsyncUploadParamsResourceWithRawResponse:
        """数据源管理"""
        return AsyncUploadParamsResourceWithRawResponse(self._datasources.upload_params)

    @cached_property
    def indexes(self) -> AsyncIndexesResourceWithRawResponse:
        """索引管理"""
        return AsyncIndexesResourceWithRawResponse(self._datasources.indexes)


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
        self.add_file = to_streamed_response_wrapper(
            datasources.add_file,
        )
        self.delete_file = to_streamed_response_wrapper(
            datasources.delete_file,
        )
        self.retrieve_runtime_meta = to_streamed_response_wrapper(
            datasources.retrieve_runtime_meta,
        )
        self.update_field = to_streamed_response_wrapper(
            datasources.update_field,
        )

    @cached_property
    def meta(self) -> MetaResourceWithStreamingResponse:
        """数据源管理"""
        return MetaResourceWithStreamingResponse(self._datasources.meta)

    @cached_property
    def upload_params(self) -> UploadParamsResourceWithStreamingResponse:
        """数据源管理"""
        return UploadParamsResourceWithStreamingResponse(self._datasources.upload_params)

    @cached_property
    def indexes(self) -> IndexesResourceWithStreamingResponse:
        """索引管理"""
        return IndexesResourceWithStreamingResponse(self._datasources.indexes)


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
        self.add_file = async_to_streamed_response_wrapper(
            datasources.add_file,
        )
        self.delete_file = async_to_streamed_response_wrapper(
            datasources.delete_file,
        )
        self.retrieve_runtime_meta = async_to_streamed_response_wrapper(
            datasources.retrieve_runtime_meta,
        )
        self.update_field = async_to_streamed_response_wrapper(
            datasources.update_field,
        )

    @cached_property
    def meta(self) -> AsyncMetaResourceWithStreamingResponse:
        """数据源管理"""
        return AsyncMetaResourceWithStreamingResponse(self._datasources.meta)

    @cached_property
    def upload_params(self) -> AsyncUploadParamsResourceWithStreamingResponse:
        """数据源管理"""
        return AsyncUploadParamsResourceWithStreamingResponse(self._datasources.upload_params)

    @cached_property
    def indexes(self) -> AsyncIndexesResourceWithStreamingResponse:
        """索引管理"""
        return AsyncIndexesResourceWithStreamingResponse(self._datasources.indexes)
