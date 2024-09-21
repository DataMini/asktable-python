# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Union, Mapping
from typing_extensions import Self, override

import httpx

from . import resources, _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import (
    is_given,
    get_async_library,
)
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "resources",
    "Asktable",
    "AsyncAsktable",
    "Client",
    "AsyncClient",
]


class Asktable(SyncAPIClient):
    sys: resources.SysResource
    securetunnels: resources.SecuretunnelsResource
    auth: resources.AuthResource
    chats: resources.ChatsResource
    datasources: resources.DatasourcesResource
    bots: resources.BotsResource
    extapis: resources.ExtapisResource
    at_auth: resources.AtAuthResource
    single_turn: resources.SingleTurnResource
    caches: resources.CachesResource
    with_raw_response: AsktableWithRawResponse
    with_streaming_response: AsktableWithStreamedResponse

    # client options

    def __init__(
        self,
        *,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous asktable client instance."""
        if base_url is None:
            base_url = os.environ.get("ASKTABLE_BASE_URL")
        if base_url is None:
            base_url = f"/v1"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.sys = resources.SysResource(self)
        self.securetunnels = resources.SecuretunnelsResource(self)
        self.auth = resources.AuthResource(self)
        self.chats = resources.ChatsResource(self)
        self.datasources = resources.DatasourcesResource(self)
        self.bots = resources.BotsResource(self)
        self.extapis = resources.ExtapisResource(self)
        self.at_auth = resources.AtAuthResource(self)
        self.single_turn = resources.SingleTurnResource(self)
        self.caches = resources.CachesResource(self)
        self.with_raw_response = AsktableWithRawResponse(self)
        self.with_streaming_response = AsktableWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncAsktable(AsyncAPIClient):
    sys: resources.AsyncSysResource
    securetunnels: resources.AsyncSecuretunnelsResource
    auth: resources.AsyncAuthResource
    chats: resources.AsyncChatsResource
    datasources: resources.AsyncDatasourcesResource
    bots: resources.AsyncBotsResource
    extapis: resources.AsyncExtapisResource
    at_auth: resources.AsyncAtAuthResource
    single_turn: resources.AsyncSingleTurnResource
    caches: resources.AsyncCachesResource
    with_raw_response: AsyncAsktableWithRawResponse
    with_streaming_response: AsyncAsktableWithStreamedResponse

    # client options

    def __init__(
        self,
        *,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async asktable client instance."""
        if base_url is None:
            base_url = os.environ.get("ASKTABLE_BASE_URL")
        if base_url is None:
            base_url = f"/v1"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.sys = resources.AsyncSysResource(self)
        self.securetunnels = resources.AsyncSecuretunnelsResource(self)
        self.auth = resources.AsyncAuthResource(self)
        self.chats = resources.AsyncChatsResource(self)
        self.datasources = resources.AsyncDatasourcesResource(self)
        self.bots = resources.AsyncBotsResource(self)
        self.extapis = resources.AsyncExtapisResource(self)
        self.at_auth = resources.AsyncAtAuthResource(self)
        self.single_turn = resources.AsyncSingleTurnResource(self)
        self.caches = resources.AsyncCachesResource(self)
        self.with_raw_response = AsyncAsktableWithRawResponse(self)
        self.with_streaming_response = AsyncAsktableWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsktableWithRawResponse:
    def __init__(self, client: Asktable) -> None:
        self.sys = resources.SysResourceWithRawResponse(client.sys)
        self.securetunnels = resources.SecuretunnelsResourceWithRawResponse(client.securetunnels)
        self.auth = resources.AuthResourceWithRawResponse(client.auth)
        self.chats = resources.ChatsResourceWithRawResponse(client.chats)
        self.datasources = resources.DatasourcesResourceWithRawResponse(client.datasources)
        self.bots = resources.BotsResourceWithRawResponse(client.bots)
        self.extapis = resources.ExtapisResourceWithRawResponse(client.extapis)
        self.at_auth = resources.AtAuthResourceWithRawResponse(client.at_auth)
        self.single_turn = resources.SingleTurnResourceWithRawResponse(client.single_turn)
        self.caches = resources.CachesResourceWithRawResponse(client.caches)


class AsyncAsktableWithRawResponse:
    def __init__(self, client: AsyncAsktable) -> None:
        self.sys = resources.AsyncSysResourceWithRawResponse(client.sys)
        self.securetunnels = resources.AsyncSecuretunnelsResourceWithRawResponse(client.securetunnels)
        self.auth = resources.AsyncAuthResourceWithRawResponse(client.auth)
        self.chats = resources.AsyncChatsResourceWithRawResponse(client.chats)
        self.datasources = resources.AsyncDatasourcesResourceWithRawResponse(client.datasources)
        self.bots = resources.AsyncBotsResourceWithRawResponse(client.bots)
        self.extapis = resources.AsyncExtapisResourceWithRawResponse(client.extapis)
        self.at_auth = resources.AsyncAtAuthResourceWithRawResponse(client.at_auth)
        self.single_turn = resources.AsyncSingleTurnResourceWithRawResponse(client.single_turn)
        self.caches = resources.AsyncCachesResourceWithRawResponse(client.caches)


class AsktableWithStreamedResponse:
    def __init__(self, client: Asktable) -> None:
        self.sys = resources.SysResourceWithStreamingResponse(client.sys)
        self.securetunnels = resources.SecuretunnelsResourceWithStreamingResponse(client.securetunnels)
        self.auth = resources.AuthResourceWithStreamingResponse(client.auth)
        self.chats = resources.ChatsResourceWithStreamingResponse(client.chats)
        self.datasources = resources.DatasourcesResourceWithStreamingResponse(client.datasources)
        self.bots = resources.BotsResourceWithStreamingResponse(client.bots)
        self.extapis = resources.ExtapisResourceWithStreamingResponse(client.extapis)
        self.at_auth = resources.AtAuthResourceWithStreamingResponse(client.at_auth)
        self.single_turn = resources.SingleTurnResourceWithStreamingResponse(client.single_turn)
        self.caches = resources.CachesResourceWithStreamingResponse(client.caches)


class AsyncAsktableWithStreamedResponse:
    def __init__(self, client: AsyncAsktable) -> None:
        self.sys = resources.AsyncSysResourceWithStreamingResponse(client.sys)
        self.securetunnels = resources.AsyncSecuretunnelsResourceWithStreamingResponse(client.securetunnels)
        self.auth = resources.AsyncAuthResourceWithStreamingResponse(client.auth)
        self.chats = resources.AsyncChatsResourceWithStreamingResponse(client.chats)
        self.datasources = resources.AsyncDatasourcesResourceWithStreamingResponse(client.datasources)
        self.bots = resources.AsyncBotsResourceWithStreamingResponse(client.bots)
        self.extapis = resources.AsyncExtapisResourceWithStreamingResponse(client.extapis)
        self.at_auth = resources.AsyncAtAuthResourceWithStreamingResponse(client.at_auth)
        self.single_turn = resources.AsyncSingleTurnResourceWithStreamingResponse(client.single_turn)
        self.caches = resources.AsyncCachesResourceWithStreamingResponse(client.caches)


Client = Asktable

AsyncClient = AsyncAsktable
