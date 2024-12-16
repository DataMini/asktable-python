# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..types import training_list_params, training_create_params, training_delete_params
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
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.training_list_response import TrainingListResponse
from ..types.training_create_response import TrainingCreateResponse

__all__ = ["TrainingsResource", "AsyncTrainingsResource"]


class TrainingsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TrainingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DataMini/asktable-python#accessing-raw-response-data-eg-headers
        """
        return TrainingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TrainingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DataMini/asktable-python#with_streaming_response
        """
        return TrainingsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        datasource_id: str,
        body: Iterable[training_create_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TrainingCreateResponse:
        """
        Create Training Pair

        Args:
          datasource_id: 数据源 ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/training",
            body=maybe_transform(body, Iterable[training_create_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"datasource_id": datasource_id}, training_create_params.TrainingCreateParams),
            ),
            cast_to=TrainingCreateResponse,
        )

    def list(
        self,
        *,
        datasource_id: str,
        page: int | NotGiven = NOT_GIVEN,
        size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[TrainingListResponse]:
        """
        Get Training Pairs

        Args:
          datasource_id: 数据源 ID

          page: Page number

          size: Page size

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/training",
            page=SyncPage[TrainingListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "datasource_id": datasource_id,
                        "page": page,
                        "size": size,
                    },
                    training_list_params.TrainingListParams,
                ),
            ),
            model=TrainingListResponse,
        )

    def delete(
        self,
        id: str,
        *,
        datasource_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Delete Training Pair

        Args:
          datasource_id: 数据源 ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/training/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"datasource_id": datasource_id}, training_delete_params.TrainingDeleteParams),
            ),
            cast_to=object,
        )


class AsyncTrainingsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTrainingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DataMini/asktable-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTrainingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTrainingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DataMini/asktable-python#with_streaming_response
        """
        return AsyncTrainingsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        datasource_id: str,
        body: Iterable[training_create_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TrainingCreateResponse:
        """
        Create Training Pair

        Args:
          datasource_id: 数据源 ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/training",
            body=await async_maybe_transform(body, Iterable[training_create_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"datasource_id": datasource_id}, training_create_params.TrainingCreateParams
                ),
            ),
            cast_to=TrainingCreateResponse,
        )

    def list(
        self,
        *,
        datasource_id: str,
        page: int | NotGiven = NOT_GIVEN,
        size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[TrainingListResponse, AsyncPage[TrainingListResponse]]:
        """
        Get Training Pairs

        Args:
          datasource_id: 数据源 ID

          page: Page number

          size: Page size

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/training",
            page=AsyncPage[TrainingListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "datasource_id": datasource_id,
                        "page": page,
                        "size": size,
                    },
                    training_list_params.TrainingListParams,
                ),
            ),
            model=TrainingListResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        datasource_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Delete Training Pair

        Args:
          datasource_id: 数据源 ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/training/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"datasource_id": datasource_id}, training_delete_params.TrainingDeleteParams
                ),
            ),
            cast_to=object,
        )


class TrainingsResourceWithRawResponse:
    def __init__(self, trainings: TrainingsResource) -> None:
        self._trainings = trainings

        self.create = to_raw_response_wrapper(
            trainings.create,
        )
        self.list = to_raw_response_wrapper(
            trainings.list,
        )
        self.delete = to_raw_response_wrapper(
            trainings.delete,
        )


class AsyncTrainingsResourceWithRawResponse:
    def __init__(self, trainings: AsyncTrainingsResource) -> None:
        self._trainings = trainings

        self.create = async_to_raw_response_wrapper(
            trainings.create,
        )
        self.list = async_to_raw_response_wrapper(
            trainings.list,
        )
        self.delete = async_to_raw_response_wrapper(
            trainings.delete,
        )


class TrainingsResourceWithStreamingResponse:
    def __init__(self, trainings: TrainingsResource) -> None:
        self._trainings = trainings

        self.create = to_streamed_response_wrapper(
            trainings.create,
        )
        self.list = to_streamed_response_wrapper(
            trainings.list,
        )
        self.delete = to_streamed_response_wrapper(
            trainings.delete,
        )


class AsyncTrainingsResourceWithStreamingResponse:
    def __init__(self, trainings: AsyncTrainingsResource) -> None:
        self._trainings = trainings

        self.create = async_to_streamed_response_wrapper(
            trainings.create,
        )
        self.list = async_to_streamed_response_wrapper(
            trainings.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            trainings.delete,
        )
