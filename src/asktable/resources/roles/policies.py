# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.roles.policy_list_response import PolicyListResponse

__all__ = ["PoliciesResource", "AsyncPoliciesResource"]


class PoliciesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PoliciesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DataMini/asktable-python#accessing-raw-response-data-eg-headers
        """
        return PoliciesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PoliciesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DataMini/asktable-python#with_streaming_response
        """
        return PoliciesResourceWithStreamingResponse(self)

    def list(
        self,
        role_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PolicyListResponse:
        """
        查询某个角色的所有策略

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not role_id:
            raise ValueError(f"Expected a non-empty value for `role_id` but received {role_id!r}")
        return self._get(
            f"/roles/{role_id}/policies",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PolicyListResponse,
        )


class AsyncPoliciesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPoliciesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DataMini/asktable-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPoliciesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPoliciesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DataMini/asktable-python#with_streaming_response
        """
        return AsyncPoliciesResourceWithStreamingResponse(self)

    async def list(
        self,
        role_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PolicyListResponse:
        """
        查询某个角色的所有策略

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not role_id:
            raise ValueError(f"Expected a non-empty value for `role_id` but received {role_id!r}")
        return await self._get(
            f"/roles/{role_id}/policies",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PolicyListResponse,
        )


class PoliciesResourceWithRawResponse:
    def __init__(self, policies: PoliciesResource) -> None:
        self._policies = policies

        self.list = to_raw_response_wrapper(
            policies.list,
        )


class AsyncPoliciesResourceWithRawResponse:
    def __init__(self, policies: AsyncPoliciesResource) -> None:
        self._policies = policies

        self.list = async_to_raw_response_wrapper(
            policies.list,
        )


class PoliciesResourceWithStreamingResponse:
    def __init__(self, policies: PoliciesResource) -> None:
        self._policies = policies

        self.list = to_streamed_response_wrapper(
            policies.list,
        )


class AsyncPoliciesResourceWithStreamingResponse:
    def __init__(self, policies: AsyncPoliciesResource) -> None:
        self._policies = policies

        self.list = async_to_streamed_response_wrapper(
            policies.list,
        )
