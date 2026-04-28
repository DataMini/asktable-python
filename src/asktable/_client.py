# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import (
    is_given,
    is_mapping_t,
    get_async_library,
)
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import AsktableError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import (
        ats,
        sys,
        auth,
        bots,
        sqls,
        user,
        chats,
        files,
        roles,
        polish,
        scores,
        answers,
        project,
        policies,
        dataframes,
        datasources,
        integration,
        preferences,
        securetunnels,
        business_glossary,
    )
    from .resources.auth import AuthResource, AsyncAuthResource
    from .resources.bots import BotsResource, AsyncBotsResource
    from .resources.sqls import SqlsResource, AsyncSqlsResource
    from .resources.files import FilesResource, AsyncFilesResource
    from .resources.roles import RolesResource, AsyncRolesResource
    from .resources.polish import PolishResource, AsyncPolishResource
    from .resources.scores import ScoresResource, AsyncScoresResource
    from .resources.answers import AnswersResource, AsyncAnswersResource
    from .resources.ats.ats import ATSResource, AsyncATSResource
    from .resources.project import ProjectResource, AsyncProjectResource
    from .resources.sys.sys import SysResource, AsyncSysResource
    from .resources.policies import PoliciesResource, AsyncPoliciesResource
    from .resources.user.user import UserResource, AsyncUserResource
    from .resources.dataframes import DataframesResource, AsyncDataframesResource
    from .resources.chats.chats import ChatsResource, AsyncChatsResource
    from .resources.integration import IntegrationResource, AsyncIntegrationResource
    from .resources.preferences import PreferencesResource, AsyncPreferencesResource
    from .resources.securetunnels import SecuretunnelsResource, AsyncSecuretunnelsResource
    from .resources.business_glossary import BusinessGlossaryResource, AsyncBusinessGlossaryResource
    from .resources.datasources.datasources import DatasourcesResource, AsyncDatasourcesResource

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
    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
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
        """Construct a new synchronous Asktable client instance.

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
            base_url = f"https://api.asktable.com"

        custom_headers_env = os.environ.get("ASKTABLE_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}

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

    @cached_property
    def sys(self) -> SysResource:
        from .resources.sys import SysResource

        return SysResource(self)

    @cached_property
    def securetunnels(self) -> SecuretunnelsResource:
        """安全隧道"""
        from .resources.securetunnels import SecuretunnelsResource

        return SecuretunnelsResource(self)

    @cached_property
    def roles(self) -> RolesResource:
        """角色管理"""
        from .resources.roles import RolesResource

        return RolesResource(self)

    @cached_property
    def policies(self) -> PoliciesResource:
        """策略管理"""
        from .resources.policies import PoliciesResource

        return PoliciesResource(self)

    @cached_property
    def chats(self) -> ChatsResource:
        """聊天管理"""
        from .resources.chats import ChatsResource

        return ChatsResource(self)

    @cached_property
    def datasources(self) -> DatasourcesResource:
        """数据源管理"""
        from .resources.datasources import DatasourcesResource

        return DatasourcesResource(self)

    @cached_property
    def bots(self) -> BotsResource:
        """AI 数据助手"""
        from .resources.bots import BotsResource

        return BotsResource(self)

    @cached_property
    def auth(self) -> AuthResource:
        """AskTable 系统认证管理"""
        from .resources.auth import AuthResource

        return AuthResource(self)

    @cached_property
    def answers(self) -> AnswersResource:
        """单轮对话"""
        from .resources.answers import AnswersResource

        return AnswersResource(self)

    @cached_property
    def sqls(self) -> SqlsResource:
        """单轮对话"""
        from .resources.sqls import SqlsResource

        return SqlsResource(self)

    @cached_property
    def integration(self) -> IntegrationResource:
        """与第三方平台集成"""
        from .resources.integration import IntegrationResource

        return IntegrationResource(self)

    @cached_property
    def business_glossary(self) -> BusinessGlossaryResource:
        """业务术语管理"""
        from .resources.business_glossary import BusinessGlossaryResource

        return BusinessGlossaryResource(self)

    @cached_property
    def preferences(self) -> PreferencesResource:
        """偏好设置"""
        from .resources.preferences import PreferencesResource

        return PreferencesResource(self)

    @cached_property
    def project(self) -> ProjectResource:
        """我的项目"""
        from .resources.project import ProjectResource

        return ProjectResource(self)

    @cached_property
    def scores(self) -> ScoresResource:
        """评分"""
        from .resources.scores import ScoresResource

        return ScoresResource(self)

    @cached_property
    def files(self) -> FilesResource:
        """数据源管理"""
        from .resources.files import FilesResource

        return FilesResource(self)

    @cached_property
    def dataframes(self) -> DataframesResource:
        from .resources.dataframes import DataframesResource

        return DataframesResource(self)

    @cached_property
    def polish(self) -> PolishResource:
        """润色"""
        from .resources.polish import PolishResource

        return PolishResource(self)

    @cached_property
    def user(self) -> UserResource:
        from .resources.user import UserResource

        return UserResource(self)

    @cached_property
    def ats(self) -> ATSResource:
        """测试系统"""
        from .resources.ats import ATSResource

        return ATSResource(self)

    @cached_property
    def with_raw_response(self) -> AsktableWithRawResponse:
        return AsktableWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsktableWithStreamedResponse:
        return AsktableWithStreamedResponse(self)

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
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
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
    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
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
        """Construct a new async AsyncAsktable client instance.

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
            base_url = f"https://api.asktable.com"

        custom_headers_env = os.environ.get("ASKTABLE_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}

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

    @cached_property
    def sys(self) -> AsyncSysResource:
        from .resources.sys import AsyncSysResource

        return AsyncSysResource(self)

    @cached_property
    def securetunnels(self) -> AsyncSecuretunnelsResource:
        """安全隧道"""
        from .resources.securetunnels import AsyncSecuretunnelsResource

        return AsyncSecuretunnelsResource(self)

    @cached_property
    def roles(self) -> AsyncRolesResource:
        """角色管理"""
        from .resources.roles import AsyncRolesResource

        return AsyncRolesResource(self)

    @cached_property
    def policies(self) -> AsyncPoliciesResource:
        """策略管理"""
        from .resources.policies import AsyncPoliciesResource

        return AsyncPoliciesResource(self)

    @cached_property
    def chats(self) -> AsyncChatsResource:
        """聊天管理"""
        from .resources.chats import AsyncChatsResource

        return AsyncChatsResource(self)

    @cached_property
    def datasources(self) -> AsyncDatasourcesResource:
        """数据源管理"""
        from .resources.datasources import AsyncDatasourcesResource

        return AsyncDatasourcesResource(self)

    @cached_property
    def bots(self) -> AsyncBotsResource:
        """AI 数据助手"""
        from .resources.bots import AsyncBotsResource

        return AsyncBotsResource(self)

    @cached_property
    def auth(self) -> AsyncAuthResource:
        """AskTable 系统认证管理"""
        from .resources.auth import AsyncAuthResource

        return AsyncAuthResource(self)

    @cached_property
    def answers(self) -> AsyncAnswersResource:
        """单轮对话"""
        from .resources.answers import AsyncAnswersResource

        return AsyncAnswersResource(self)

    @cached_property
    def sqls(self) -> AsyncSqlsResource:
        """单轮对话"""
        from .resources.sqls import AsyncSqlsResource

        return AsyncSqlsResource(self)

    @cached_property
    def integration(self) -> AsyncIntegrationResource:
        """与第三方平台集成"""
        from .resources.integration import AsyncIntegrationResource

        return AsyncIntegrationResource(self)

    @cached_property
    def business_glossary(self) -> AsyncBusinessGlossaryResource:
        """业务术语管理"""
        from .resources.business_glossary import AsyncBusinessGlossaryResource

        return AsyncBusinessGlossaryResource(self)

    @cached_property
    def preferences(self) -> AsyncPreferencesResource:
        """偏好设置"""
        from .resources.preferences import AsyncPreferencesResource

        return AsyncPreferencesResource(self)

    @cached_property
    def project(self) -> AsyncProjectResource:
        """我的项目"""
        from .resources.project import AsyncProjectResource

        return AsyncProjectResource(self)

    @cached_property
    def scores(self) -> AsyncScoresResource:
        """评分"""
        from .resources.scores import AsyncScoresResource

        return AsyncScoresResource(self)

    @cached_property
    def files(self) -> AsyncFilesResource:
        """数据源管理"""
        from .resources.files import AsyncFilesResource

        return AsyncFilesResource(self)

    @cached_property
    def dataframes(self) -> AsyncDataframesResource:
        from .resources.dataframes import AsyncDataframesResource

        return AsyncDataframesResource(self)

    @cached_property
    def polish(self) -> AsyncPolishResource:
        """润色"""
        from .resources.polish import AsyncPolishResource

        return AsyncPolishResource(self)

    @cached_property
    def user(self) -> AsyncUserResource:
        from .resources.user import AsyncUserResource

        return AsyncUserResource(self)

    @cached_property
    def ats(self) -> AsyncATSResource:
        """测试系统"""
        from .resources.ats import AsyncATSResource

        return AsyncATSResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncAsktableWithRawResponse:
        return AsyncAsktableWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAsktableWithStreamedResponse:
        return AsyncAsktableWithStreamedResponse(self)

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
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
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
    _client: Asktable

    def __init__(self, client: Asktable) -> None:
        self._client = client

    @cached_property
    def sys(self) -> sys.SysResourceWithRawResponse:
        from .resources.sys import SysResourceWithRawResponse

        return SysResourceWithRawResponse(self._client.sys)

    @cached_property
    def securetunnels(self) -> securetunnels.SecuretunnelsResourceWithRawResponse:
        """安全隧道"""
        from .resources.securetunnels import SecuretunnelsResourceWithRawResponse

        return SecuretunnelsResourceWithRawResponse(self._client.securetunnels)

    @cached_property
    def roles(self) -> roles.RolesResourceWithRawResponse:
        """角色管理"""
        from .resources.roles import RolesResourceWithRawResponse

        return RolesResourceWithRawResponse(self._client.roles)

    @cached_property
    def policies(self) -> policies.PoliciesResourceWithRawResponse:
        """策略管理"""
        from .resources.policies import PoliciesResourceWithRawResponse

        return PoliciesResourceWithRawResponse(self._client.policies)

    @cached_property
    def chats(self) -> chats.ChatsResourceWithRawResponse:
        """聊天管理"""
        from .resources.chats import ChatsResourceWithRawResponse

        return ChatsResourceWithRawResponse(self._client.chats)

    @cached_property
    def datasources(self) -> datasources.DatasourcesResourceWithRawResponse:
        """数据源管理"""
        from .resources.datasources import DatasourcesResourceWithRawResponse

        return DatasourcesResourceWithRawResponse(self._client.datasources)

    @cached_property
    def bots(self) -> bots.BotsResourceWithRawResponse:
        """AI 数据助手"""
        from .resources.bots import BotsResourceWithRawResponse

        return BotsResourceWithRawResponse(self._client.bots)

    @cached_property
    def auth(self) -> auth.AuthResourceWithRawResponse:
        """AskTable 系统认证管理"""
        from .resources.auth import AuthResourceWithRawResponse

        return AuthResourceWithRawResponse(self._client.auth)

    @cached_property
    def answers(self) -> answers.AnswersResourceWithRawResponse:
        """单轮对话"""
        from .resources.answers import AnswersResourceWithRawResponse

        return AnswersResourceWithRawResponse(self._client.answers)

    @cached_property
    def sqls(self) -> sqls.SqlsResourceWithRawResponse:
        """单轮对话"""
        from .resources.sqls import SqlsResourceWithRawResponse

        return SqlsResourceWithRawResponse(self._client.sqls)

    @cached_property
    def integration(self) -> integration.IntegrationResourceWithRawResponse:
        """与第三方平台集成"""
        from .resources.integration import IntegrationResourceWithRawResponse

        return IntegrationResourceWithRawResponse(self._client.integration)

    @cached_property
    def business_glossary(self) -> business_glossary.BusinessGlossaryResourceWithRawResponse:
        """业务术语管理"""
        from .resources.business_glossary import BusinessGlossaryResourceWithRawResponse

        return BusinessGlossaryResourceWithRawResponse(self._client.business_glossary)

    @cached_property
    def preferences(self) -> preferences.PreferencesResourceWithRawResponse:
        """偏好设置"""
        from .resources.preferences import PreferencesResourceWithRawResponse

        return PreferencesResourceWithRawResponse(self._client.preferences)

    @cached_property
    def project(self) -> project.ProjectResourceWithRawResponse:
        """我的项目"""
        from .resources.project import ProjectResourceWithRawResponse

        return ProjectResourceWithRawResponse(self._client.project)

    @cached_property
    def scores(self) -> scores.ScoresResourceWithRawResponse:
        """评分"""
        from .resources.scores import ScoresResourceWithRawResponse

        return ScoresResourceWithRawResponse(self._client.scores)

    @cached_property
    def files(self) -> files.FilesResourceWithRawResponse:
        """数据源管理"""
        from .resources.files import FilesResourceWithRawResponse

        return FilesResourceWithRawResponse(self._client.files)

    @cached_property
    def dataframes(self) -> dataframes.DataframesResourceWithRawResponse:
        from .resources.dataframes import DataframesResourceWithRawResponse

        return DataframesResourceWithRawResponse(self._client.dataframes)

    @cached_property
    def polish(self) -> polish.PolishResourceWithRawResponse:
        """润色"""
        from .resources.polish import PolishResourceWithRawResponse

        return PolishResourceWithRawResponse(self._client.polish)

    @cached_property
    def user(self) -> user.UserResourceWithRawResponse:
        from .resources.user import UserResourceWithRawResponse

        return UserResourceWithRawResponse(self._client.user)

    @cached_property
    def ats(self) -> ats.ATSResourceWithRawResponse:
        """测试系统"""
        from .resources.ats import ATSResourceWithRawResponse

        return ATSResourceWithRawResponse(self._client.ats)


class AsyncAsktableWithRawResponse:
    _client: AsyncAsktable

    def __init__(self, client: AsyncAsktable) -> None:
        self._client = client

    @cached_property
    def sys(self) -> sys.AsyncSysResourceWithRawResponse:
        from .resources.sys import AsyncSysResourceWithRawResponse

        return AsyncSysResourceWithRawResponse(self._client.sys)

    @cached_property
    def securetunnels(self) -> securetunnels.AsyncSecuretunnelsResourceWithRawResponse:
        """安全隧道"""
        from .resources.securetunnels import AsyncSecuretunnelsResourceWithRawResponse

        return AsyncSecuretunnelsResourceWithRawResponse(self._client.securetunnels)

    @cached_property
    def roles(self) -> roles.AsyncRolesResourceWithRawResponse:
        """角色管理"""
        from .resources.roles import AsyncRolesResourceWithRawResponse

        return AsyncRolesResourceWithRawResponse(self._client.roles)

    @cached_property
    def policies(self) -> policies.AsyncPoliciesResourceWithRawResponse:
        """策略管理"""
        from .resources.policies import AsyncPoliciesResourceWithRawResponse

        return AsyncPoliciesResourceWithRawResponse(self._client.policies)

    @cached_property
    def chats(self) -> chats.AsyncChatsResourceWithRawResponse:
        """聊天管理"""
        from .resources.chats import AsyncChatsResourceWithRawResponse

        return AsyncChatsResourceWithRawResponse(self._client.chats)

    @cached_property
    def datasources(self) -> datasources.AsyncDatasourcesResourceWithRawResponse:
        """数据源管理"""
        from .resources.datasources import AsyncDatasourcesResourceWithRawResponse

        return AsyncDatasourcesResourceWithRawResponse(self._client.datasources)

    @cached_property
    def bots(self) -> bots.AsyncBotsResourceWithRawResponse:
        """AI 数据助手"""
        from .resources.bots import AsyncBotsResourceWithRawResponse

        return AsyncBotsResourceWithRawResponse(self._client.bots)

    @cached_property
    def auth(self) -> auth.AsyncAuthResourceWithRawResponse:
        """AskTable 系统认证管理"""
        from .resources.auth import AsyncAuthResourceWithRawResponse

        return AsyncAuthResourceWithRawResponse(self._client.auth)

    @cached_property
    def answers(self) -> answers.AsyncAnswersResourceWithRawResponse:
        """单轮对话"""
        from .resources.answers import AsyncAnswersResourceWithRawResponse

        return AsyncAnswersResourceWithRawResponse(self._client.answers)

    @cached_property
    def sqls(self) -> sqls.AsyncSqlsResourceWithRawResponse:
        """单轮对话"""
        from .resources.sqls import AsyncSqlsResourceWithRawResponse

        return AsyncSqlsResourceWithRawResponse(self._client.sqls)

    @cached_property
    def integration(self) -> integration.AsyncIntegrationResourceWithRawResponse:
        """与第三方平台集成"""
        from .resources.integration import AsyncIntegrationResourceWithRawResponse

        return AsyncIntegrationResourceWithRawResponse(self._client.integration)

    @cached_property
    def business_glossary(self) -> business_glossary.AsyncBusinessGlossaryResourceWithRawResponse:
        """业务术语管理"""
        from .resources.business_glossary import AsyncBusinessGlossaryResourceWithRawResponse

        return AsyncBusinessGlossaryResourceWithRawResponse(self._client.business_glossary)

    @cached_property
    def preferences(self) -> preferences.AsyncPreferencesResourceWithRawResponse:
        """偏好设置"""
        from .resources.preferences import AsyncPreferencesResourceWithRawResponse

        return AsyncPreferencesResourceWithRawResponse(self._client.preferences)

    @cached_property
    def project(self) -> project.AsyncProjectResourceWithRawResponse:
        """我的项目"""
        from .resources.project import AsyncProjectResourceWithRawResponse

        return AsyncProjectResourceWithRawResponse(self._client.project)

    @cached_property
    def scores(self) -> scores.AsyncScoresResourceWithRawResponse:
        """评分"""
        from .resources.scores import AsyncScoresResourceWithRawResponse

        return AsyncScoresResourceWithRawResponse(self._client.scores)

    @cached_property
    def files(self) -> files.AsyncFilesResourceWithRawResponse:
        """数据源管理"""
        from .resources.files import AsyncFilesResourceWithRawResponse

        return AsyncFilesResourceWithRawResponse(self._client.files)

    @cached_property
    def dataframes(self) -> dataframes.AsyncDataframesResourceWithRawResponse:
        from .resources.dataframes import AsyncDataframesResourceWithRawResponse

        return AsyncDataframesResourceWithRawResponse(self._client.dataframes)

    @cached_property
    def polish(self) -> polish.AsyncPolishResourceWithRawResponse:
        """润色"""
        from .resources.polish import AsyncPolishResourceWithRawResponse

        return AsyncPolishResourceWithRawResponse(self._client.polish)

    @cached_property
    def user(self) -> user.AsyncUserResourceWithRawResponse:
        from .resources.user import AsyncUserResourceWithRawResponse

        return AsyncUserResourceWithRawResponse(self._client.user)

    @cached_property
    def ats(self) -> ats.AsyncATSResourceWithRawResponse:
        """测试系统"""
        from .resources.ats import AsyncATSResourceWithRawResponse

        return AsyncATSResourceWithRawResponse(self._client.ats)


class AsktableWithStreamedResponse:
    _client: Asktable

    def __init__(self, client: Asktable) -> None:
        self._client = client

    @cached_property
    def sys(self) -> sys.SysResourceWithStreamingResponse:
        from .resources.sys import SysResourceWithStreamingResponse

        return SysResourceWithStreamingResponse(self._client.sys)

    @cached_property
    def securetunnels(self) -> securetunnels.SecuretunnelsResourceWithStreamingResponse:
        """安全隧道"""
        from .resources.securetunnels import SecuretunnelsResourceWithStreamingResponse

        return SecuretunnelsResourceWithStreamingResponse(self._client.securetunnels)

    @cached_property
    def roles(self) -> roles.RolesResourceWithStreamingResponse:
        """角色管理"""
        from .resources.roles import RolesResourceWithStreamingResponse

        return RolesResourceWithStreamingResponse(self._client.roles)

    @cached_property
    def policies(self) -> policies.PoliciesResourceWithStreamingResponse:
        """策略管理"""
        from .resources.policies import PoliciesResourceWithStreamingResponse

        return PoliciesResourceWithStreamingResponse(self._client.policies)

    @cached_property
    def chats(self) -> chats.ChatsResourceWithStreamingResponse:
        """聊天管理"""
        from .resources.chats import ChatsResourceWithStreamingResponse

        return ChatsResourceWithStreamingResponse(self._client.chats)

    @cached_property
    def datasources(self) -> datasources.DatasourcesResourceWithStreamingResponse:
        """数据源管理"""
        from .resources.datasources import DatasourcesResourceWithStreamingResponse

        return DatasourcesResourceWithStreamingResponse(self._client.datasources)

    @cached_property
    def bots(self) -> bots.BotsResourceWithStreamingResponse:
        """AI 数据助手"""
        from .resources.bots import BotsResourceWithStreamingResponse

        return BotsResourceWithStreamingResponse(self._client.bots)

    @cached_property
    def auth(self) -> auth.AuthResourceWithStreamingResponse:
        """AskTable 系统认证管理"""
        from .resources.auth import AuthResourceWithStreamingResponse

        return AuthResourceWithStreamingResponse(self._client.auth)

    @cached_property
    def answers(self) -> answers.AnswersResourceWithStreamingResponse:
        """单轮对话"""
        from .resources.answers import AnswersResourceWithStreamingResponse

        return AnswersResourceWithStreamingResponse(self._client.answers)

    @cached_property
    def sqls(self) -> sqls.SqlsResourceWithStreamingResponse:
        """单轮对话"""
        from .resources.sqls import SqlsResourceWithStreamingResponse

        return SqlsResourceWithStreamingResponse(self._client.sqls)

    @cached_property
    def integration(self) -> integration.IntegrationResourceWithStreamingResponse:
        """与第三方平台集成"""
        from .resources.integration import IntegrationResourceWithStreamingResponse

        return IntegrationResourceWithStreamingResponse(self._client.integration)

    @cached_property
    def business_glossary(self) -> business_glossary.BusinessGlossaryResourceWithStreamingResponse:
        """业务术语管理"""
        from .resources.business_glossary import BusinessGlossaryResourceWithStreamingResponse

        return BusinessGlossaryResourceWithStreamingResponse(self._client.business_glossary)

    @cached_property
    def preferences(self) -> preferences.PreferencesResourceWithStreamingResponse:
        """偏好设置"""
        from .resources.preferences import PreferencesResourceWithStreamingResponse

        return PreferencesResourceWithStreamingResponse(self._client.preferences)

    @cached_property
    def project(self) -> project.ProjectResourceWithStreamingResponse:
        """我的项目"""
        from .resources.project import ProjectResourceWithStreamingResponse

        return ProjectResourceWithStreamingResponse(self._client.project)

    @cached_property
    def scores(self) -> scores.ScoresResourceWithStreamingResponse:
        """评分"""
        from .resources.scores import ScoresResourceWithStreamingResponse

        return ScoresResourceWithStreamingResponse(self._client.scores)

    @cached_property
    def files(self) -> files.FilesResourceWithStreamingResponse:
        """数据源管理"""
        from .resources.files import FilesResourceWithStreamingResponse

        return FilesResourceWithStreamingResponse(self._client.files)

    @cached_property
    def dataframes(self) -> dataframes.DataframesResourceWithStreamingResponse:
        from .resources.dataframes import DataframesResourceWithStreamingResponse

        return DataframesResourceWithStreamingResponse(self._client.dataframes)

    @cached_property
    def polish(self) -> polish.PolishResourceWithStreamingResponse:
        """润色"""
        from .resources.polish import PolishResourceWithStreamingResponse

        return PolishResourceWithStreamingResponse(self._client.polish)

    @cached_property
    def user(self) -> user.UserResourceWithStreamingResponse:
        from .resources.user import UserResourceWithStreamingResponse

        return UserResourceWithStreamingResponse(self._client.user)

    @cached_property
    def ats(self) -> ats.ATSResourceWithStreamingResponse:
        """测试系统"""
        from .resources.ats import ATSResourceWithStreamingResponse

        return ATSResourceWithStreamingResponse(self._client.ats)


class AsyncAsktableWithStreamedResponse:
    _client: AsyncAsktable

    def __init__(self, client: AsyncAsktable) -> None:
        self._client = client

    @cached_property
    def sys(self) -> sys.AsyncSysResourceWithStreamingResponse:
        from .resources.sys import AsyncSysResourceWithStreamingResponse

        return AsyncSysResourceWithStreamingResponse(self._client.sys)

    @cached_property
    def securetunnels(self) -> securetunnels.AsyncSecuretunnelsResourceWithStreamingResponse:
        """安全隧道"""
        from .resources.securetunnels import AsyncSecuretunnelsResourceWithStreamingResponse

        return AsyncSecuretunnelsResourceWithStreamingResponse(self._client.securetunnels)

    @cached_property
    def roles(self) -> roles.AsyncRolesResourceWithStreamingResponse:
        """角色管理"""
        from .resources.roles import AsyncRolesResourceWithStreamingResponse

        return AsyncRolesResourceWithStreamingResponse(self._client.roles)

    @cached_property
    def policies(self) -> policies.AsyncPoliciesResourceWithStreamingResponse:
        """策略管理"""
        from .resources.policies import AsyncPoliciesResourceWithStreamingResponse

        return AsyncPoliciesResourceWithStreamingResponse(self._client.policies)

    @cached_property
    def chats(self) -> chats.AsyncChatsResourceWithStreamingResponse:
        """聊天管理"""
        from .resources.chats import AsyncChatsResourceWithStreamingResponse

        return AsyncChatsResourceWithStreamingResponse(self._client.chats)

    @cached_property
    def datasources(self) -> datasources.AsyncDatasourcesResourceWithStreamingResponse:
        """数据源管理"""
        from .resources.datasources import AsyncDatasourcesResourceWithStreamingResponse

        return AsyncDatasourcesResourceWithStreamingResponse(self._client.datasources)

    @cached_property
    def bots(self) -> bots.AsyncBotsResourceWithStreamingResponse:
        """AI 数据助手"""
        from .resources.bots import AsyncBotsResourceWithStreamingResponse

        return AsyncBotsResourceWithStreamingResponse(self._client.bots)

    @cached_property
    def auth(self) -> auth.AsyncAuthResourceWithStreamingResponse:
        """AskTable 系统认证管理"""
        from .resources.auth import AsyncAuthResourceWithStreamingResponse

        return AsyncAuthResourceWithStreamingResponse(self._client.auth)

    @cached_property
    def answers(self) -> answers.AsyncAnswersResourceWithStreamingResponse:
        """单轮对话"""
        from .resources.answers import AsyncAnswersResourceWithStreamingResponse

        return AsyncAnswersResourceWithStreamingResponse(self._client.answers)

    @cached_property
    def sqls(self) -> sqls.AsyncSqlsResourceWithStreamingResponse:
        """单轮对话"""
        from .resources.sqls import AsyncSqlsResourceWithStreamingResponse

        return AsyncSqlsResourceWithStreamingResponse(self._client.sqls)

    @cached_property
    def integration(self) -> integration.AsyncIntegrationResourceWithStreamingResponse:
        """与第三方平台集成"""
        from .resources.integration import AsyncIntegrationResourceWithStreamingResponse

        return AsyncIntegrationResourceWithStreamingResponse(self._client.integration)

    @cached_property
    def business_glossary(self) -> business_glossary.AsyncBusinessGlossaryResourceWithStreamingResponse:
        """业务术语管理"""
        from .resources.business_glossary import AsyncBusinessGlossaryResourceWithStreamingResponse

        return AsyncBusinessGlossaryResourceWithStreamingResponse(self._client.business_glossary)

    @cached_property
    def preferences(self) -> preferences.AsyncPreferencesResourceWithStreamingResponse:
        """偏好设置"""
        from .resources.preferences import AsyncPreferencesResourceWithStreamingResponse

        return AsyncPreferencesResourceWithStreamingResponse(self._client.preferences)

    @cached_property
    def project(self) -> project.AsyncProjectResourceWithStreamingResponse:
        """我的项目"""
        from .resources.project import AsyncProjectResourceWithStreamingResponse

        return AsyncProjectResourceWithStreamingResponse(self._client.project)

    @cached_property
    def scores(self) -> scores.AsyncScoresResourceWithStreamingResponse:
        """评分"""
        from .resources.scores import AsyncScoresResourceWithStreamingResponse

        return AsyncScoresResourceWithStreamingResponse(self._client.scores)

    @cached_property
    def files(self) -> files.AsyncFilesResourceWithStreamingResponse:
        """数据源管理"""
        from .resources.files import AsyncFilesResourceWithStreamingResponse

        return AsyncFilesResourceWithStreamingResponse(self._client.files)

    @cached_property
    def dataframes(self) -> dataframes.AsyncDataframesResourceWithStreamingResponse:
        from .resources.dataframes import AsyncDataframesResourceWithStreamingResponse

        return AsyncDataframesResourceWithStreamingResponse(self._client.dataframes)

    @cached_property
    def polish(self) -> polish.AsyncPolishResourceWithStreamingResponse:
        """润色"""
        from .resources.polish import AsyncPolishResourceWithStreamingResponse

        return AsyncPolishResourceWithStreamingResponse(self._client.polish)

    @cached_property
    def user(self) -> user.AsyncUserResourceWithStreamingResponse:
        from .resources.user import AsyncUserResourceWithStreamingResponse

        return AsyncUserResourceWithStreamingResponse(self._client.user)

    @cached_property
    def ats(self) -> ats.AsyncATSResourceWithStreamingResponse:
        """测试系统"""
        from .resources.ats import AsyncATSResourceWithStreamingResponse

        return AsyncATSResourceWithStreamingResponse(self._client.ats)


Client = Asktable

AsyncClient = AsyncAsktable
