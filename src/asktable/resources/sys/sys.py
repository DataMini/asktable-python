# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ...types import sy_update_config_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from .projects.projects import (
    ProjectsResource,
    AsyncProjectsResource,
    ProjectsResourceWithRawResponse,
    AsyncProjectsResourceWithRawResponse,
    ProjectsResourceWithStreamingResponse,
    AsyncProjectsResourceWithStreamingResponse,
)
from ...types.sy_update_config_response import SyUpdateConfigResponse

__all__ = ["SysResource", "AsyncSysResource"]


class SysResource(SyncAPIResource):
    @cached_property
    def projects(self) -> ProjectsResource:
        return ProjectsResource(self._client)

    @cached_property
    def with_raw_response(self) -> SysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DataMini/asktable-python#accessing-raw-response-data-eg-headers
        """
        return SysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DataMini/asktable-python#with_streaming_response
        """
        return SysResourceWithStreamingResponse(self)

    def update_config(
        self,
        *,
        global_table_limit: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyUpdateConfigResponse:
        """
        Update Config

        Args:
          global_table_limit: 表限制数量

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            "/v1/sys/config",
            body=maybe_transform(
                {"global_table_limit": global_table_limit}, sy_update_config_params.SyUpdateConfigParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SyUpdateConfigResponse,
        )


class AsyncSysResource(AsyncAPIResource):
    @cached_property
    def projects(self) -> AsyncProjectsResource:
        return AsyncProjectsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DataMini/asktable-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DataMini/asktable-python#with_streaming_response
        """
        return AsyncSysResourceWithStreamingResponse(self)

    async def update_config(
        self,
        *,
        global_table_limit: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyUpdateConfigResponse:
        """
        Update Config

        Args:
          global_table_limit: 表限制数量

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            "/v1/sys/config",
            body=await async_maybe_transform(
                {"global_table_limit": global_table_limit}, sy_update_config_params.SyUpdateConfigParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SyUpdateConfigResponse,
        )


class SysResourceWithRawResponse:
    def __init__(self, sys: SysResource) -> None:
        self._sys = sys

        self.update_config = to_raw_response_wrapper(
            sys.update_config,
        )

    @cached_property
    def projects(self) -> ProjectsResourceWithRawResponse:
        return ProjectsResourceWithRawResponse(self._sys.projects)


class AsyncSysResourceWithRawResponse:
    def __init__(self, sys: AsyncSysResource) -> None:
        self._sys = sys

        self.update_config = async_to_raw_response_wrapper(
            sys.update_config,
        )

    @cached_property
    def projects(self) -> AsyncProjectsResourceWithRawResponse:
        return AsyncProjectsResourceWithRawResponse(self._sys.projects)


class SysResourceWithStreamingResponse:
    def __init__(self, sys: SysResource) -> None:
        self._sys = sys

        self.update_config = to_streamed_response_wrapper(
            sys.update_config,
        )

    @cached_property
    def projects(self) -> ProjectsResourceWithStreamingResponse:
        return ProjectsResourceWithStreamingResponse(self._sys.projects)


class AsyncSysResourceWithStreamingResponse:
    def __init__(self, sys: AsyncSysResource) -> None:
        self._sys = sys

        self.update_config = async_to_streamed_response_wrapper(
            sys.update_config,
        )

    @cached_property
    def projects(self) -> AsyncProjectsResourceWithStreamingResponse:
        return AsyncProjectsResourceWithStreamingResponse(self._sys.projects)
