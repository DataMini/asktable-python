# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import score_create_params
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
from ..types.score_create_response import ScoreCreateResponse

__all__ = ["ScoresResource", "AsyncScoresResource"]


class ScoresResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ScoresResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DataMini/asktable-python#accessing-raw-response-data-eg-headers
        """
        return ScoresResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ScoresResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DataMini/asktable-python#with_streaming_response
        """
        return ScoresResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        chat_id: str,
        message_id: str,
        score: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScoreCreateResponse:
        """
        Score

        Args:
          chat_id: 聊天 ID

          message_id: 消息 ID

          score: 评分

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/score",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "chat_id": chat_id,
                        "message_id": message_id,
                        "score": score,
                    },
                    score_create_params.ScoreCreateParams,
                ),
            ),
            cast_to=ScoreCreateResponse,
        )


class AsyncScoresResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncScoresResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DataMini/asktable-python#accessing-raw-response-data-eg-headers
        """
        return AsyncScoresResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncScoresResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DataMini/asktable-python#with_streaming_response
        """
        return AsyncScoresResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        chat_id: str,
        message_id: str,
        score: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScoreCreateResponse:
        """
        Score

        Args:
          chat_id: 聊天 ID

          message_id: 消息 ID

          score: 评分

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/score",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "chat_id": chat_id,
                        "message_id": message_id,
                        "score": score,
                    },
                    score_create_params.ScoreCreateParams,
                ),
            ),
            cast_to=ScoreCreateResponse,
        )


class ScoresResourceWithRawResponse:
    def __init__(self, scores: ScoresResource) -> None:
        self._scores = scores

        self.create = to_raw_response_wrapper(
            scores.create,
        )


class AsyncScoresResourceWithRawResponse:
    def __init__(self, scores: AsyncScoresResource) -> None:
        self._scores = scores

        self.create = async_to_raw_response_wrapper(
            scores.create,
        )


class ScoresResourceWithStreamingResponse:
    def __init__(self, scores: ScoresResource) -> None:
        self._scores = scores

        self.create = to_streamed_response_wrapper(
            scores.create,
        )


class AsyncScoresResourceWithStreamingResponse:
    def __init__(self, scores: AsyncScoresResource) -> None:
        self._scores = scores

        self.create = async_to_streamed_response_wrapper(
            scores.create,
        )
