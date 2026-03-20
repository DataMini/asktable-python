# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional

import httpx

from ...types import chat_list_params, chat_create_params
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from .messages import (
    MessagesResource,
    AsyncMessagesResource,
    MessagesResourceWithRawResponse,
    AsyncMessagesResourceWithRawResponse,
    MessagesResourceWithStreamingResponse,
    AsyncMessagesResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncPage, AsyncPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.chat_list_response import ChatListResponse
from ...types.chat_create_response import ChatCreateResponse
from ...types.chat_retrieve_response import ChatRetrieveResponse

__all__ = ["ChatsResource", "AsyncChatsResource"]


class ChatsResource(SyncAPIResource):
    """聊天管理"""

    @cached_property
    def messages(self) -> MessagesResource:
        """聊天管理"""
        return MessagesResource(self._client)

    @cached_property
    def with_raw_response(self) -> ChatsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DataMini/asktable-python#accessing-raw-response-data-eg-headers
        """
        return ChatsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ChatsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DataMini/asktable-python#with_streaming_response
        """
        return ChatsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        bot_id: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        role_id: Optional[str] | Omit = omit,
        role_variables: Optional[Dict[str, Union[str, int, bool]]] | Omit = omit,
        user_profile: Optional[Dict[str, Union[str, int, bool]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatCreateResponse:
        """
        创建对话

        Args:
          bot_id: 机器人 ID，如果需要使用高级功能，请使用 bot_id 来创建对话。在机器人中你可以定义
              可以访问的数据、可以执行的任务以及是否开启调试模式等设置。

          name: New name for the chat

          role_id: 角色 ID，将扮演这个角色来执行对话，用于权限控制。若无，则跳过鉴权，即可查询所有
              数据

          role_variables: 在扮演这个角色时需要传递的变量值，用 Key-Value 形式传递

          user_profile: 用户信息，用于在对话中传递用户的信息，用 Key-Value 形式传递

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/chats",
            body=maybe_transform(
                {
                    "bot_id": bot_id,
                    "name": name,
                    "role_id": role_id,
                    "role_variables": role_variables,
                    "user_profile": user_profile,
                },
                chat_create_params.ChatCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatCreateResponse,
        )

    def retrieve(
        self,
        chat_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatRetrieveResponse:
        """
        获取某个对话

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return self._get(
            path_template("/v1/chats/{chat_id}", chat_id=chat_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatRetrieveResponse,
        )

    def list(
        self,
        *,
        page: int | Omit = omit,
        size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[ChatListResponse]:
        """
        查询对话列表

        Args:
          page: Page number

          size: Page size

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/chats",
            page=SyncPage[ChatListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "size": size,
                    },
                    chat_list_params.ChatListParams,
                ),
            ),
            model=ChatListResponse,
        )

    def delete(
        self,
        chat_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        删除某个对话（包含消息）

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/v1/chats/{chat_id}", chat_id=chat_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncChatsResource(AsyncAPIResource):
    """聊天管理"""

    @cached_property
    def messages(self) -> AsyncMessagesResource:
        """聊天管理"""
        return AsyncMessagesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncChatsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DataMini/asktable-python#accessing-raw-response-data-eg-headers
        """
        return AsyncChatsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncChatsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DataMini/asktable-python#with_streaming_response
        """
        return AsyncChatsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        bot_id: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        role_id: Optional[str] | Omit = omit,
        role_variables: Optional[Dict[str, Union[str, int, bool]]] | Omit = omit,
        user_profile: Optional[Dict[str, Union[str, int, bool]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatCreateResponse:
        """
        创建对话

        Args:
          bot_id: 机器人 ID，如果需要使用高级功能，请使用 bot_id 来创建对话。在机器人中你可以定义
              可以访问的数据、可以执行的任务以及是否开启调试模式等设置。

          name: New name for the chat

          role_id: 角色 ID，将扮演这个角色来执行对话，用于权限控制。若无，则跳过鉴权，即可查询所有
              数据

          role_variables: 在扮演这个角色时需要传递的变量值，用 Key-Value 形式传递

          user_profile: 用户信息，用于在对话中传递用户的信息，用 Key-Value 形式传递

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/chats",
            body=await async_maybe_transform(
                {
                    "bot_id": bot_id,
                    "name": name,
                    "role_id": role_id,
                    "role_variables": role_variables,
                    "user_profile": user_profile,
                },
                chat_create_params.ChatCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatCreateResponse,
        )

    async def retrieve(
        self,
        chat_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatRetrieveResponse:
        """
        获取某个对话

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return await self._get(
            path_template("/v1/chats/{chat_id}", chat_id=chat_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatRetrieveResponse,
        )

    def list(
        self,
        *,
        page: int | Omit = omit,
        size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ChatListResponse, AsyncPage[ChatListResponse]]:
        """
        查询对话列表

        Args:
          page: Page number

          size: Page size

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/chats",
            page=AsyncPage[ChatListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "size": size,
                    },
                    chat_list_params.ChatListParams,
                ),
            ),
            model=ChatListResponse,
        )

    async def delete(
        self,
        chat_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        删除某个对话（包含消息）

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/v1/chats/{chat_id}", chat_id=chat_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class ChatsResourceWithRawResponse:
    def __init__(self, chats: ChatsResource) -> None:
        self._chats = chats

        self.create = to_raw_response_wrapper(
            chats.create,
        )
        self.retrieve = to_raw_response_wrapper(
            chats.retrieve,
        )
        self.list = to_raw_response_wrapper(
            chats.list,
        )
        self.delete = to_raw_response_wrapper(
            chats.delete,
        )

    @cached_property
    def messages(self) -> MessagesResourceWithRawResponse:
        """聊天管理"""
        return MessagesResourceWithRawResponse(self._chats.messages)


class AsyncChatsResourceWithRawResponse:
    def __init__(self, chats: AsyncChatsResource) -> None:
        self._chats = chats

        self.create = async_to_raw_response_wrapper(
            chats.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            chats.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            chats.list,
        )
        self.delete = async_to_raw_response_wrapper(
            chats.delete,
        )

    @cached_property
    def messages(self) -> AsyncMessagesResourceWithRawResponse:
        """聊天管理"""
        return AsyncMessagesResourceWithRawResponse(self._chats.messages)


class ChatsResourceWithStreamingResponse:
    def __init__(self, chats: ChatsResource) -> None:
        self._chats = chats

        self.create = to_streamed_response_wrapper(
            chats.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            chats.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            chats.list,
        )
        self.delete = to_streamed_response_wrapper(
            chats.delete,
        )

    @cached_property
    def messages(self) -> MessagesResourceWithStreamingResponse:
        """聊天管理"""
        return MessagesResourceWithStreamingResponse(self._chats.messages)


class AsyncChatsResourceWithStreamingResponse:
    def __init__(self, chats: AsyncChatsResource) -> None:
        self._chats = chats

        self.create = async_to_streamed_response_wrapper(
            chats.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            chats.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            chats.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            chats.delete,
        )

    @cached_property
    def messages(self) -> AsyncMessagesResourceWithStreamingResponse:
        """聊天管理"""
        return AsyncMessagesResourceWithStreamingResponse(self._chats.messages)
