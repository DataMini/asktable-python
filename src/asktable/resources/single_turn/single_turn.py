# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .q2a import (
    Q2aResource,
    AsyncQ2aResource,
    Q2aResourceWithRawResponse,
    AsyncQ2aResourceWithRawResponse,
    Q2aResourceWithStreamingResponse,
    AsyncQ2aResourceWithStreamingResponse,
)
from .q2s import (
    Q2sResource,
    AsyncQ2sResource,
    Q2sResourceWithRawResponse,
    AsyncQ2sResourceWithRawResponse,
    Q2sResourceWithStreamingResponse,
    AsyncQ2sResourceWithStreamingResponse,
)
from .q2w import (
    Q2wResource,
    AsyncQ2wResource,
    Q2wResourceWithRawResponse,
    AsyncQ2wResourceWithRawResponse,
    Q2wResourceWithStreamingResponse,
    AsyncQ2wResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["SingleTurnResource", "AsyncSingleTurnResource"]


class SingleTurnResource(SyncAPIResource):
    @cached_property
    def q2a(self) -> Q2aResource:
        return Q2aResource(self._client)

    @cached_property
    def q2s(self) -> Q2sResource:
        return Q2sResource(self._client)

    @cached_property
    def q2w(self) -> Q2wResource:
        return Q2wResource(self._client)

    @cached_property
    def with_raw_response(self) -> SingleTurnResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DataMini/asktable-python#accessing-raw-response-data-eg-headers
        """
        return SingleTurnResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SingleTurnResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DataMini/asktable-python#with_streaming_response
        """
        return SingleTurnResourceWithStreamingResponse(self)


class AsyncSingleTurnResource(AsyncAPIResource):
    @cached_property
    def q2a(self) -> AsyncQ2aResource:
        return AsyncQ2aResource(self._client)

    @cached_property
    def q2s(self) -> AsyncQ2sResource:
        return AsyncQ2sResource(self._client)

    @cached_property
    def q2w(self) -> AsyncQ2wResource:
        return AsyncQ2wResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSingleTurnResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DataMini/asktable-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSingleTurnResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSingleTurnResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DataMini/asktable-python#with_streaming_response
        """
        return AsyncSingleTurnResourceWithStreamingResponse(self)


class SingleTurnResourceWithRawResponse:
    def __init__(self, single_turn: SingleTurnResource) -> None:
        self._single_turn = single_turn

    @cached_property
    def q2a(self) -> Q2aResourceWithRawResponse:
        return Q2aResourceWithRawResponse(self._single_turn.q2a)

    @cached_property
    def q2s(self) -> Q2sResourceWithRawResponse:
        return Q2sResourceWithRawResponse(self._single_turn.q2s)

    @cached_property
    def q2w(self) -> Q2wResourceWithRawResponse:
        return Q2wResourceWithRawResponse(self._single_turn.q2w)


class AsyncSingleTurnResourceWithRawResponse:
    def __init__(self, single_turn: AsyncSingleTurnResource) -> None:
        self._single_turn = single_turn

    @cached_property
    def q2a(self) -> AsyncQ2aResourceWithRawResponse:
        return AsyncQ2aResourceWithRawResponse(self._single_turn.q2a)

    @cached_property
    def q2s(self) -> AsyncQ2sResourceWithRawResponse:
        return AsyncQ2sResourceWithRawResponse(self._single_turn.q2s)

    @cached_property
    def q2w(self) -> AsyncQ2wResourceWithRawResponse:
        return AsyncQ2wResourceWithRawResponse(self._single_turn.q2w)


class SingleTurnResourceWithStreamingResponse:
    def __init__(self, single_turn: SingleTurnResource) -> None:
        self._single_turn = single_turn

    @cached_property
    def q2a(self) -> Q2aResourceWithStreamingResponse:
        return Q2aResourceWithStreamingResponse(self._single_turn.q2a)

    @cached_property
    def q2s(self) -> Q2sResourceWithStreamingResponse:
        return Q2sResourceWithStreamingResponse(self._single_turn.q2s)

    @cached_property
    def q2w(self) -> Q2wResourceWithStreamingResponse:
        return Q2wResourceWithStreamingResponse(self._single_turn.q2w)


class AsyncSingleTurnResourceWithStreamingResponse:
    def __init__(self, single_turn: AsyncSingleTurnResource) -> None:
        self._single_turn = single_turn

    @cached_property
    def q2a(self) -> AsyncQ2aResourceWithStreamingResponse:
        return AsyncQ2aResourceWithStreamingResponse(self._single_turn.q2a)

    @cached_property
    def q2s(self) -> AsyncQ2sResourceWithStreamingResponse:
        return AsyncQ2sResourceWithStreamingResponse(self._single_turn.q2s)

    @cached_property
    def q2w(self) -> AsyncQ2wResourceWithStreamingResponse:
        return AsyncQ2wResourceWithStreamingResponse(self._single_turn.q2w)
