# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import preference_create_params, preference_update_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from .._base_client import make_request_options
from ..types.preference_create_response import PreferenceCreateResponse
from ..types.preference_update_response import PreferenceUpdateResponse
from ..types.preference_retrieve_response import PreferenceRetrieveResponse

__all__ = ["PreferencesResource", "AsyncPreferencesResource"]


class PreferencesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PreferencesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DataMini/asktable-python#accessing-raw-response-data-eg-headers
        """
        return PreferencesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PreferencesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DataMini/asktable-python#with_streaming_response
        """
        return PreferencesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        general_preference: str,
        sql_preference: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PreferenceCreateResponse:
        """
        创建偏好设置

        Args:
          general_preference: 通用偏好设置内容

          sql_preference: SQL 偏好设置内容

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/preference",
            body=maybe_transform(
                {
                    "general_preference": general_preference,
                    "sql_preference": sql_preference,
                },
                preference_create_params.PreferenceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PreferenceCreateResponse,
        )

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PreferenceRetrieveResponse:
        """获取偏好设置"""
        return self._get(
            "/preference",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PreferenceRetrieveResponse,
        )

    def update(
        self,
        *,
        general_preference: Optional[str] | NotGiven = NOT_GIVEN,
        sql_preference: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PreferenceUpdateResponse:
        """
        更新偏好设置

        Args:
          general_preference: 通用偏好设置内容

          sql_preference: SQL 偏好设置内容

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            "/preference",
            body=maybe_transform(
                {
                    "general_preference": general_preference,
                    "sql_preference": sql_preference,
                },
                preference_update_params.PreferenceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PreferenceUpdateResponse,
        )

    def delete(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """删除偏好设置"""
        return self._delete(
            "/preference",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncPreferencesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPreferencesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DataMini/asktable-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPreferencesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPreferencesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DataMini/asktable-python#with_streaming_response
        """
        return AsyncPreferencesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        general_preference: str,
        sql_preference: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PreferenceCreateResponse:
        """
        创建偏好设置

        Args:
          general_preference: 通用偏好设置内容

          sql_preference: SQL 偏好设置内容

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/preference",
            body=await async_maybe_transform(
                {
                    "general_preference": general_preference,
                    "sql_preference": sql_preference,
                },
                preference_create_params.PreferenceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PreferenceCreateResponse,
        )

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PreferenceRetrieveResponse:
        """获取偏好设置"""
        return await self._get(
            "/preference",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PreferenceRetrieveResponse,
        )

    async def update(
        self,
        *,
        general_preference: Optional[str] | NotGiven = NOT_GIVEN,
        sql_preference: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PreferenceUpdateResponse:
        """
        更新偏好设置

        Args:
          general_preference: 通用偏好设置内容

          sql_preference: SQL 偏好设置内容

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            "/preference",
            body=await async_maybe_transform(
                {
                    "general_preference": general_preference,
                    "sql_preference": sql_preference,
                },
                preference_update_params.PreferenceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PreferenceUpdateResponse,
        )

    async def delete(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """删除偏好设置"""
        return await self._delete(
            "/preference",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class PreferencesResourceWithRawResponse:
    def __init__(self, preferences: PreferencesResource) -> None:
        self._preferences = preferences

        self.create = to_raw_response_wrapper(
            preferences.create,
        )
        self.retrieve = to_raw_response_wrapper(
            preferences.retrieve,
        )
        self.update = to_raw_response_wrapper(
            preferences.update,
        )
        self.delete = to_raw_response_wrapper(
            preferences.delete,
        )


class AsyncPreferencesResourceWithRawResponse:
    def __init__(self, preferences: AsyncPreferencesResource) -> None:
        self._preferences = preferences

        self.create = async_to_raw_response_wrapper(
            preferences.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            preferences.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            preferences.update,
        )
        self.delete = async_to_raw_response_wrapper(
            preferences.delete,
        )


class PreferencesResourceWithStreamingResponse:
    def __init__(self, preferences: PreferencesResource) -> None:
        self._preferences = preferences

        self.create = to_streamed_response_wrapper(
            preferences.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            preferences.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            preferences.update,
        )
        self.delete = to_streamed_response_wrapper(
            preferences.delete,
        )


class AsyncPreferencesResourceWithStreamingResponse:
    def __init__(self, preferences: AsyncPreferencesResource) -> None:
        self._preferences = preferences

        self.create = async_to_streamed_response_wrapper(
            preferences.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            preferences.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            preferences.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            preferences.delete,
        )
