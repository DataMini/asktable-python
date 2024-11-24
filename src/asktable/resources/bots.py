# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

import httpx

from ..types import bot_list_params, bot_create_params, bot_invite_params, bot_update_params
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
from ..types.chatbot import Chatbot

__all__ = ["BotsResource", "AsyncBotsResource"]


class BotsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BotsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DataMini/asktable-python#accessing-raw-response-data-eg-headers
        """
        return BotsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BotsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DataMini/asktable-python#with_streaming_response
        """
        return BotsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        datasource_ids: List[str],
        name: str,
        color_theme: Optional[str] | NotGiven = NOT_GIVEN,
        debug: bool | NotGiven = NOT_GIVEN,
        extapi_ids: List[str] | NotGiven = NOT_GIVEN,
        magic_input: Optional[str] | NotGiven = NOT_GIVEN,
        max_rows: int | NotGiven = NOT_GIVEN,
        publish: bool | NotGiven = NOT_GIVEN,
        sample_questions: Optional[List[str]] | NotGiven = NOT_GIVEN,
        welcome_message: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Chatbot:
        """
        创建一个新的 Bot

        Args:
          datasource_ids: 数据源 ID，目前只支持 1 个数据源。

          name: 名称，不超过 64 个字符

          color_theme: 颜色主题

          debug: 调试模式

          extapi_ids: 扩展 API ID 列表，扩展 API ID 的逗号分隔列表。

          magic_input: 魔法提示词

          max_rows: 最大返回行数，默认不限制

          publish: 是否公开

          sample_questions: 示例问题列表

          welcome_message: 欢迎消息

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/bots",
            body=maybe_transform(
                {
                    "datasource_ids": datasource_ids,
                    "name": name,
                    "color_theme": color_theme,
                    "debug": debug,
                    "extapi_ids": extapi_ids,
                    "magic_input": magic_input,
                    "max_rows": max_rows,
                    "publish": publish,
                    "sample_questions": sample_questions,
                    "welcome_message": welcome_message,
                },
                bot_create_params.BotCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Chatbot,
        )

    def retrieve(
        self,
        bot_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Chatbot:
        """
        获取某个 Bot

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bot_id:
            raise ValueError(f"Expected a non-empty value for `bot_id` but received {bot_id!r}")
        return self._get(
            f"/bots/{bot_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Chatbot,
        )

    def update(
        self,
        bot_id: str,
        *,
        avatar_url: Optional[str] | NotGiven = NOT_GIVEN,
        color_theme: Optional[str] | NotGiven = NOT_GIVEN,
        datasource_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        debug: Optional[bool] | NotGiven = NOT_GIVEN,
        extapi_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        magic_input: Optional[str] | NotGiven = NOT_GIVEN,
        max_rows: Optional[int] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        publish: Optional[bool] | NotGiven = NOT_GIVEN,
        sample_questions: Optional[List[str]] | NotGiven = NOT_GIVEN,
        welcome_message: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Chatbot:
        """
        更新某个 Bot

        Args:
          avatar_url: 头像 URL

          color_theme: 颜色主题

          datasource_ids: 数据源 ID，目前只支持 1 个数据源。

          debug: 调试模式

          extapi_ids: 扩展 API ID 列表，扩展 API ID 的逗号分隔列表。

          magic_input: 魔法提示词

          max_rows: 最大返回行数，默认不限制

          name: 名称，不超过 64 个字符

          publish: 是否公开

          sample_questions: 示例问题列表

          welcome_message: 欢迎消息

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bot_id:
            raise ValueError(f"Expected a non-empty value for `bot_id` but received {bot_id!r}")
        return self._patch(
            f"/bots/{bot_id}",
            body=maybe_transform(
                {
                    "avatar_url": avatar_url,
                    "color_theme": color_theme,
                    "datasource_ids": datasource_ids,
                    "debug": debug,
                    "extapi_ids": extapi_ids,
                    "magic_input": magic_input,
                    "max_rows": max_rows,
                    "name": name,
                    "publish": publish,
                    "sample_questions": sample_questions,
                    "welcome_message": welcome_message,
                },
                bot_update_params.BotUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Chatbot,
        )

    def list(
        self,
        *,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[Chatbot]:
        """
        查询所有 Bot

        Args:
          name: 名称

          page: Page number

          size: Page size

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/bots",
            page=SyncPage[Chatbot],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "name": name,
                        "page": page,
                        "size": size,
                    },
                    bot_list_params.BotListParams,
                ),
            ),
            model=Chatbot,
        )

    def delete(
        self,
        bot_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        删除某个 Bot

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bot_id:
            raise ValueError(f"Expected a non-empty value for `bot_id` but received {bot_id!r}")
        return self._delete(
            f"/bots/{bot_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def invite(
        self,
        bot_id: str,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        邀请用户加入对话

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bot_id:
            raise ValueError(f"Expected a non-empty value for `bot_id` but received {bot_id!r}")
        return self._post(
            f"/bots/{bot_id}/invite",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"project_id": project_id}, bot_invite_params.BotInviteParams),
            ),
            cast_to=object,
        )


class AsyncBotsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBotsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DataMini/asktable-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBotsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBotsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DataMini/asktable-python#with_streaming_response
        """
        return AsyncBotsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        datasource_ids: List[str],
        name: str,
        color_theme: Optional[str] | NotGiven = NOT_GIVEN,
        debug: bool | NotGiven = NOT_GIVEN,
        extapi_ids: List[str] | NotGiven = NOT_GIVEN,
        magic_input: Optional[str] | NotGiven = NOT_GIVEN,
        max_rows: int | NotGiven = NOT_GIVEN,
        publish: bool | NotGiven = NOT_GIVEN,
        sample_questions: Optional[List[str]] | NotGiven = NOT_GIVEN,
        welcome_message: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Chatbot:
        """
        创建一个新的 Bot

        Args:
          datasource_ids: 数据源 ID，目前只支持 1 个数据源。

          name: 名称，不超过 64 个字符

          color_theme: 颜色主题

          debug: 调试模式

          extapi_ids: 扩展 API ID 列表，扩展 API ID 的逗号分隔列表。

          magic_input: 魔法提示词

          max_rows: 最大返回行数，默认不限制

          publish: 是否公开

          sample_questions: 示例问题列表

          welcome_message: 欢迎消息

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/bots",
            body=await async_maybe_transform(
                {
                    "datasource_ids": datasource_ids,
                    "name": name,
                    "color_theme": color_theme,
                    "debug": debug,
                    "extapi_ids": extapi_ids,
                    "magic_input": magic_input,
                    "max_rows": max_rows,
                    "publish": publish,
                    "sample_questions": sample_questions,
                    "welcome_message": welcome_message,
                },
                bot_create_params.BotCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Chatbot,
        )

    async def retrieve(
        self,
        bot_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Chatbot:
        """
        获取某个 Bot

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bot_id:
            raise ValueError(f"Expected a non-empty value for `bot_id` but received {bot_id!r}")
        return await self._get(
            f"/bots/{bot_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Chatbot,
        )

    async def update(
        self,
        bot_id: str,
        *,
        avatar_url: Optional[str] | NotGiven = NOT_GIVEN,
        color_theme: Optional[str] | NotGiven = NOT_GIVEN,
        datasource_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        debug: Optional[bool] | NotGiven = NOT_GIVEN,
        extapi_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        magic_input: Optional[str] | NotGiven = NOT_GIVEN,
        max_rows: Optional[int] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        publish: Optional[bool] | NotGiven = NOT_GIVEN,
        sample_questions: Optional[List[str]] | NotGiven = NOT_GIVEN,
        welcome_message: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Chatbot:
        """
        更新某个 Bot

        Args:
          avatar_url: 头像 URL

          color_theme: 颜色主题

          datasource_ids: 数据源 ID，目前只支持 1 个数据源。

          debug: 调试模式

          extapi_ids: 扩展 API ID 列表，扩展 API ID 的逗号分隔列表。

          magic_input: 魔法提示词

          max_rows: 最大返回行数，默认不限制

          name: 名称，不超过 64 个字符

          publish: 是否公开

          sample_questions: 示例问题列表

          welcome_message: 欢迎消息

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bot_id:
            raise ValueError(f"Expected a non-empty value for `bot_id` but received {bot_id!r}")
        return await self._patch(
            f"/bots/{bot_id}",
            body=await async_maybe_transform(
                {
                    "avatar_url": avatar_url,
                    "color_theme": color_theme,
                    "datasource_ids": datasource_ids,
                    "debug": debug,
                    "extapi_ids": extapi_ids,
                    "magic_input": magic_input,
                    "max_rows": max_rows,
                    "name": name,
                    "publish": publish,
                    "sample_questions": sample_questions,
                    "welcome_message": welcome_message,
                },
                bot_update_params.BotUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Chatbot,
        )

    def list(
        self,
        *,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Chatbot, AsyncPage[Chatbot]]:
        """
        查询所有 Bot

        Args:
          name: 名称

          page: Page number

          size: Page size

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/bots",
            page=AsyncPage[Chatbot],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "name": name,
                        "page": page,
                        "size": size,
                    },
                    bot_list_params.BotListParams,
                ),
            ),
            model=Chatbot,
        )

    async def delete(
        self,
        bot_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        删除某个 Bot

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bot_id:
            raise ValueError(f"Expected a non-empty value for `bot_id` but received {bot_id!r}")
        return await self._delete(
            f"/bots/{bot_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def invite(
        self,
        bot_id: str,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        邀请用户加入对话

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bot_id:
            raise ValueError(f"Expected a non-empty value for `bot_id` but received {bot_id!r}")
        return await self._post(
            f"/bots/{bot_id}/invite",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"project_id": project_id}, bot_invite_params.BotInviteParams),
            ),
            cast_to=object,
        )


class BotsResourceWithRawResponse:
    def __init__(self, bots: BotsResource) -> None:
        self._bots = bots

        self.create = to_raw_response_wrapper(
            bots.create,
        )
        self.retrieve = to_raw_response_wrapper(
            bots.retrieve,
        )
        self.update = to_raw_response_wrapper(
            bots.update,
        )
        self.list = to_raw_response_wrapper(
            bots.list,
        )
        self.delete = to_raw_response_wrapper(
            bots.delete,
        )
        self.invite = to_raw_response_wrapper(
            bots.invite,
        )


class AsyncBotsResourceWithRawResponse:
    def __init__(self, bots: AsyncBotsResource) -> None:
        self._bots = bots

        self.create = async_to_raw_response_wrapper(
            bots.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            bots.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            bots.update,
        )
        self.list = async_to_raw_response_wrapper(
            bots.list,
        )
        self.delete = async_to_raw_response_wrapper(
            bots.delete,
        )
        self.invite = async_to_raw_response_wrapper(
            bots.invite,
        )


class BotsResourceWithStreamingResponse:
    def __init__(self, bots: BotsResource) -> None:
        self._bots = bots

        self.create = to_streamed_response_wrapper(
            bots.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            bots.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            bots.update,
        )
        self.list = to_streamed_response_wrapper(
            bots.list,
        )
        self.delete = to_streamed_response_wrapper(
            bots.delete,
        )
        self.invite = to_streamed_response_wrapper(
            bots.invite,
        )


class AsyncBotsResourceWithStreamingResponse:
    def __init__(self, bots: AsyncBotsResource) -> None:
        self._bots = bots

        self.create = async_to_streamed_response_wrapper(
            bots.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            bots.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            bots.update,
        )
        self.list = async_to_streamed_response_wrapper(
            bots.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            bots.delete,
        )
        self.invite = async_to_streamed_response_wrapper(
            bots.invite,
        )
