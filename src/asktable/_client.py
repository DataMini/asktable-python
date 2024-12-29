# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Union, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
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
from .resources import (
    auth,
    bots,
    roles,
    caches,
    scores,
    project,
    policies,
    trainings,
    integration,
    preferences,
    securetunnels,
    business_glossary,
)
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import AsktableError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)
from .resources.sys import sys
from .resources.chats import chats
from .resources.extapis import extapis
from .resources.datasources import datasources
from .resources.single_turn import single_turn

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "Asktable",
    "AsyncAsktable",
    "Client",
    "AsyncClient",
]


class Asktable(SyncAPIClient):
    sys: sys.SysResource
    securetunnels: securetunnels.SecuretunnelsResource
    roles: roles.RolesResource
    policies: policies.PoliciesResource
    chats: chats.ChatsResource
    datasources: datasources.DatasourcesResource
    bots: bots.BotsResource
    extapis: extapis.ExtapisResource
    auth: auth.AuthResource
    single_turn: single_turn.SingleTurnResource
    caches: caches.CachesResource
    integration: integration.IntegrationResource
    business_glossary: business_glossary.BusinessGlossaryResource
    preferences: preferences.PreferencesResource
    trainings: trainings.TrainingsResource
    project: project.ProjectResource
    scores: scores.ScoresResource
    with_raw_response: AsktableWithRawResponse
    with_streaming_response: AsktableWithStreamedResponse

    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
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
        """Construct a new synchronous asktable client instance.

        This automatically infers the `api_key` argument from the `ASKTABLE_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("ASKTABLE_API_KEY")
        if api_key is None:
            raise AsktableError(
                "The api_key client option must be set either by passing api_key to the client or by setting the ASKTABLE_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("ASKTABLE_BASE_URL")
        if base_url is None:
            base_url = f"https://api.asktable.com/v1"

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

        self.sys = sys.SysResource(self)
        self.securetunnels = securetunnels.SecuretunnelsResource(self)
        self.roles = roles.RolesResource(self)
        self.policies = policies.PoliciesResource(self)
        self.chats = chats.ChatsResource(self)
        self.datasources = datasources.DatasourcesResource(self)
        self.bots = bots.BotsResource(self)
        self.extapis = extapis.ExtapisResource(self)
        self.auth = auth.AuthResource(self)
        self.single_turn = single_turn.SingleTurnResource(self)
        self.caches = caches.CachesResource(self)
        self.integration = integration.IntegrationResource(self)
        self.business_glossary = business_glossary.BusinessGlossaryResource(self)
        self.preferences = preferences.PreferencesResource(self)
        self.trainings = trainings.TrainingsResource(self)
        self.project = project.ProjectResource(self)
        self.scores = scores.ScoresResource(self)
        self.with_raw_response = AsktableWithRawResponse(self)
        self.with_streaming_response = AsktableWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="repeat")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

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
        api_key: str | None = None,
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
            api_key=api_key or self.api_key,
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
    sys: sys.AsyncSysResource
    securetunnels: securetunnels.AsyncSecuretunnelsResource
    roles: roles.AsyncRolesResource
    policies: policies.AsyncPoliciesResource
    chats: chats.AsyncChatsResource
    datasources: datasources.AsyncDatasourcesResource
    bots: bots.AsyncBotsResource
    extapis: extapis.AsyncExtapisResource
    auth: auth.AsyncAuthResource
    single_turn: single_turn.AsyncSingleTurnResource
    caches: caches.AsyncCachesResource
    integration: integration.AsyncIntegrationResource
    business_glossary: business_glossary.AsyncBusinessGlossaryResource
    preferences: preferences.AsyncPreferencesResource
    trainings: trainings.AsyncTrainingsResource
    project: project.AsyncProjectResource
    scores: scores.AsyncScoresResource
    with_raw_response: AsyncAsktableWithRawResponse
    with_streaming_response: AsyncAsktableWithStreamedResponse

    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
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
        """Construct a new async asktable client instance.

        This automatically infers the `api_key` argument from the `ASKTABLE_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("ASKTABLE_API_KEY")
        if api_key is None:
            raise AsktableError(
                "The api_key client option must be set either by passing api_key to the client or by setting the ASKTABLE_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("ASKTABLE_BASE_URL")
        if base_url is None:
            base_url = f"https://api.asktable.com/v1"

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

        self.sys = sys.AsyncSysResource(self)
        self.securetunnels = securetunnels.AsyncSecuretunnelsResource(self)
        self.roles = roles.AsyncRolesResource(self)
        self.policies = policies.AsyncPoliciesResource(self)
        self.chats = chats.AsyncChatsResource(self)
        self.datasources = datasources.AsyncDatasourcesResource(self)
        self.bots = bots.AsyncBotsResource(self)
        self.extapis = extapis.AsyncExtapisResource(self)
        self.auth = auth.AsyncAuthResource(self)
        self.single_turn = single_turn.AsyncSingleTurnResource(self)
        self.caches = caches.AsyncCachesResource(self)
        self.integration = integration.AsyncIntegrationResource(self)
        self.business_glossary = business_glossary.AsyncBusinessGlossaryResource(self)
        self.preferences = preferences.AsyncPreferencesResource(self)
        self.trainings = trainings.AsyncTrainingsResource(self)
        self.project = project.AsyncProjectResource(self)
        self.scores = scores.AsyncScoresResource(self)
        self.with_raw_response = AsyncAsktableWithRawResponse(self)
        self.with_streaming_response = AsyncAsktableWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="repeat")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

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
        api_key: str | None = None,
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
            api_key=api_key or self.api_key,
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
        self.sys = sys.SysResourceWithRawResponse(client.sys)
        self.securetunnels = securetunnels.SecuretunnelsResourceWithRawResponse(client.securetunnels)
        self.roles = roles.RolesResourceWithRawResponse(client.roles)
        self.policies = policies.PoliciesResourceWithRawResponse(client.policies)
        self.chats = chats.ChatsResourceWithRawResponse(client.chats)
        self.datasources = datasources.DatasourcesResourceWithRawResponse(client.datasources)
        self.bots = bots.BotsResourceWithRawResponse(client.bots)
        self.extapis = extapis.ExtapisResourceWithRawResponse(client.extapis)
        self.auth = auth.AuthResourceWithRawResponse(client.auth)
        self.single_turn = single_turn.SingleTurnResourceWithRawResponse(client.single_turn)
        self.caches = caches.CachesResourceWithRawResponse(client.caches)
        self.integration = integration.IntegrationResourceWithRawResponse(client.integration)
        self.business_glossary = business_glossary.BusinessGlossaryResourceWithRawResponse(client.business_glossary)
        self.preferences = preferences.PreferencesResourceWithRawResponse(client.preferences)
        self.trainings = trainings.TrainingsResourceWithRawResponse(client.trainings)
        self.project = project.ProjectResourceWithRawResponse(client.project)
        self.scores = scores.ScoresResourceWithRawResponse(client.scores)


class AsyncAsktableWithRawResponse:
    def __init__(self, client: AsyncAsktable) -> None:
        self.sys = sys.AsyncSysResourceWithRawResponse(client.sys)
        self.securetunnels = securetunnels.AsyncSecuretunnelsResourceWithRawResponse(client.securetunnels)
        self.roles = roles.AsyncRolesResourceWithRawResponse(client.roles)
        self.policies = policies.AsyncPoliciesResourceWithRawResponse(client.policies)
        self.chats = chats.AsyncChatsResourceWithRawResponse(client.chats)
        self.datasources = datasources.AsyncDatasourcesResourceWithRawResponse(client.datasources)
        self.bots = bots.AsyncBotsResourceWithRawResponse(client.bots)
        self.extapis = extapis.AsyncExtapisResourceWithRawResponse(client.extapis)
        self.auth = auth.AsyncAuthResourceWithRawResponse(client.auth)
        self.single_turn = single_turn.AsyncSingleTurnResourceWithRawResponse(client.single_turn)
        self.caches = caches.AsyncCachesResourceWithRawResponse(client.caches)
        self.integration = integration.AsyncIntegrationResourceWithRawResponse(client.integration)
        self.business_glossary = business_glossary.AsyncBusinessGlossaryResourceWithRawResponse(
            client.business_glossary
        )
        self.preferences = preferences.AsyncPreferencesResourceWithRawResponse(client.preferences)
        self.trainings = trainings.AsyncTrainingsResourceWithRawResponse(client.trainings)
        self.project = project.AsyncProjectResourceWithRawResponse(client.project)
        self.scores = scores.AsyncScoresResourceWithRawResponse(client.scores)


class AsktableWithStreamedResponse:
    def __init__(self, client: Asktable) -> None:
        self.sys = sys.SysResourceWithStreamingResponse(client.sys)
        self.securetunnels = securetunnels.SecuretunnelsResourceWithStreamingResponse(client.securetunnels)
        self.roles = roles.RolesResourceWithStreamingResponse(client.roles)
        self.policies = policies.PoliciesResourceWithStreamingResponse(client.policies)
        self.chats = chats.ChatsResourceWithStreamingResponse(client.chats)
        self.datasources = datasources.DatasourcesResourceWithStreamingResponse(client.datasources)
        self.bots = bots.BotsResourceWithStreamingResponse(client.bots)
        self.extapis = extapis.ExtapisResourceWithStreamingResponse(client.extapis)
        self.auth = auth.AuthResourceWithStreamingResponse(client.auth)
        self.single_turn = single_turn.SingleTurnResourceWithStreamingResponse(client.single_turn)
        self.caches = caches.CachesResourceWithStreamingResponse(client.caches)
        self.integration = integration.IntegrationResourceWithStreamingResponse(client.integration)
        self.business_glossary = business_glossary.BusinessGlossaryResourceWithStreamingResponse(
            client.business_glossary
        )
        self.preferences = preferences.PreferencesResourceWithStreamingResponse(client.preferences)
        self.trainings = trainings.TrainingsResourceWithStreamingResponse(client.trainings)
        self.project = project.ProjectResourceWithStreamingResponse(client.project)
        self.scores = scores.ScoresResourceWithStreamingResponse(client.scores)


class AsyncAsktableWithStreamedResponse:
    def __init__(self, client: AsyncAsktable) -> None:
        self.sys = sys.AsyncSysResourceWithStreamingResponse(client.sys)
        self.securetunnels = securetunnels.AsyncSecuretunnelsResourceWithStreamingResponse(client.securetunnels)
        self.roles = roles.AsyncRolesResourceWithStreamingResponse(client.roles)
        self.policies = policies.AsyncPoliciesResourceWithStreamingResponse(client.policies)
        self.chats = chats.AsyncChatsResourceWithStreamingResponse(client.chats)
        self.datasources = datasources.AsyncDatasourcesResourceWithStreamingResponse(client.datasources)
        self.bots = bots.AsyncBotsResourceWithStreamingResponse(client.bots)
        self.extapis = extapis.AsyncExtapisResourceWithStreamingResponse(client.extapis)
        self.auth = auth.AsyncAuthResourceWithStreamingResponse(client.auth)
        self.single_turn = single_turn.AsyncSingleTurnResourceWithStreamingResponse(client.single_turn)
        self.caches = caches.AsyncCachesResourceWithStreamingResponse(client.caches)
        self.integration = integration.AsyncIntegrationResourceWithStreamingResponse(client.integration)
        self.business_glossary = business_glossary.AsyncBusinessGlossaryResourceWithStreamingResponse(
            client.business_glossary
        )
        self.preferences = preferences.AsyncPreferencesResourceWithStreamingResponse(client.preferences)
        self.trainings = trainings.AsyncTrainingsResourceWithStreamingResponse(client.trainings)
        self.project = project.AsyncProjectResourceWithStreamingResponse(client.project)
        self.scores = scores.AsyncScoresResourceWithStreamingResponse(client.scores)


Client = Asktable

AsyncClient = AsyncAsktable
