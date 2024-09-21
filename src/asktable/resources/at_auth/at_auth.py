# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .me import (
    MeResource,
    AsyncMeResource,
    MeResourceWithRawResponse,
    AsyncMeResourceWithRawResponse,
    MeResourceWithStreamingResponse,
    AsyncMeResourceWithStreamingResponse,
)
from .tokens import (
    TokensResource,
    AsyncTokensResource,
    TokensResourceWithRawResponse,
    AsyncTokensResourceWithRawResponse,
    TokensResourceWithStreamingResponse,
    AsyncTokensResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["AtAuthResource", "AsyncAtAuthResource"]


class AtAuthResource(SyncAPIResource):
    @cached_property
    def tokens(self) -> TokensResource:
        return TokensResource(self._client)

    @cached_property
    def me(self) -> MeResource:
        return MeResource(self._client)

    @cached_property
    def with_raw_response(self) -> AtAuthResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/asktable-python#accessing-raw-response-data-eg-headers
        """
        return AtAuthResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AtAuthResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/asktable-python#with_streaming_response
        """
        return AtAuthResourceWithStreamingResponse(self)


class AsyncAtAuthResource(AsyncAPIResource):
    @cached_property
    def tokens(self) -> AsyncTokensResource:
        return AsyncTokensResource(self._client)

    @cached_property
    def me(self) -> AsyncMeResource:
        return AsyncMeResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAtAuthResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/asktable-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAtAuthResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAtAuthResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/asktable-python#with_streaming_response
        """
        return AsyncAtAuthResourceWithStreamingResponse(self)


class AtAuthResourceWithRawResponse:
    def __init__(self, at_auth: AtAuthResource) -> None:
        self._at_auth = at_auth

    @cached_property
    def tokens(self) -> TokensResourceWithRawResponse:
        return TokensResourceWithRawResponse(self._at_auth.tokens)

    @cached_property
    def me(self) -> MeResourceWithRawResponse:
        return MeResourceWithRawResponse(self._at_auth.me)


class AsyncAtAuthResourceWithRawResponse:
    def __init__(self, at_auth: AsyncAtAuthResource) -> None:
        self._at_auth = at_auth

    @cached_property
    def tokens(self) -> AsyncTokensResourceWithRawResponse:
        return AsyncTokensResourceWithRawResponse(self._at_auth.tokens)

    @cached_property
    def me(self) -> AsyncMeResourceWithRawResponse:
        return AsyncMeResourceWithRawResponse(self._at_auth.me)


class AtAuthResourceWithStreamingResponse:
    def __init__(self, at_auth: AtAuthResource) -> None:
        self._at_auth = at_auth

    @cached_property
    def tokens(self) -> TokensResourceWithStreamingResponse:
        return TokensResourceWithStreamingResponse(self._at_auth.tokens)

    @cached_property
    def me(self) -> MeResourceWithStreamingResponse:
        return MeResourceWithStreamingResponse(self._at_auth.me)


class AsyncAtAuthResourceWithStreamingResponse:
    def __init__(self, at_auth: AsyncAtAuthResource) -> None:
        self._at_auth = at_auth

    @cached_property
    def tokens(self) -> AsyncTokensResourceWithStreamingResponse:
        return AsyncTokensResourceWithStreamingResponse(self._at_auth.tokens)

    @cached_property
    def me(self) -> AsyncMeResourceWithStreamingResponse:
        return AsyncMeResourceWithStreamingResponse(self._at_auth.me)
