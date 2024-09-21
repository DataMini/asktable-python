# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from asktable import Asktable, AsyncAsktable
from tests.utils import assert_matches_type
from asktable.types import (
    Chat,
    Message,
    ChatListResponse,
    ChatRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestChats:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Asktable) -> None:
        chat = client.chats.create()
        assert_matches_type(Chat, chat, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Asktable) -> None:
        chat = client.chats.create(
            bot_id="bot_42",
            datasource_ids=["ds_42"],
            name="name",
            role_id="role_42",
            role_variables={"id": "123123123"},
            user_profile={
                "age": "string",
                "is_male": "string",
                "name": "张三",
            },
        )
        assert_matches_type(Chat, chat, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Asktable) -> None:
        response = client.chats.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(Chat, chat, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Asktable) -> None:
        with client.chats.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(Chat, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Asktable) -> None:
        chat = client.chats.retrieve(
            "chat_id",
        )
        assert_matches_type(ChatRetrieveResponse, chat, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Asktable) -> None:
        response = client.chats.with_raw_response.retrieve(
            "chat_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(ChatRetrieveResponse, chat, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Asktable) -> None:
        with client.chats.with_streaming_response.retrieve(
            "chat_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(ChatRetrieveResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Asktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            client.chats.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Asktable) -> None:
        chat = client.chats.list()
        assert_matches_type(ChatListResponse, chat, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Asktable) -> None:
        chat = client.chats.list(
            page=1,
            size=1,
        )
        assert_matches_type(ChatListResponse, chat, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Asktable) -> None:
        response = client.chats.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(ChatListResponse, chat, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Asktable) -> None:
        with client.chats.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(ChatListResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete_conversation(self, client: Asktable) -> None:
        chat = client.chats.delete_conversation(
            "chat_id",
        )
        assert_matches_type(object, chat, path=["response"])

    @parametrize
    def test_raw_response_delete_conversation(self, client: Asktable) -> None:
        response = client.chats.with_raw_response.delete_conversation(
            "chat_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(object, chat, path=["response"])

    @parametrize
    def test_streaming_response_delete_conversation(self, client: Asktable) -> None:
        with client.chats.with_streaming_response.delete_conversation(
            "chat_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(object, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete_conversation(self, client: Asktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            client.chats.with_raw_response.delete_conversation(
                "",
            )

    @parametrize
    def test_method_send(self, client: Asktable) -> None:
        chat = client.chats.send(
            chat_id="chat_id",
            question="question",
        )
        assert_matches_type(Message, chat, path=["response"])

    @parametrize
    def test_raw_response_send(self, client: Asktable) -> None:
        response = client.chats.with_raw_response.send(
            chat_id="chat_id",
            question="question",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(Message, chat, path=["response"])

    @parametrize
    def test_streaming_response_send(self, client: Asktable) -> None:
        with client.chats.with_streaming_response.send(
            chat_id="chat_id",
            question="question",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(Message, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_send(self, client: Asktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            client.chats.with_raw_response.send(
                chat_id="",
                question="question",
            )


class TestAsyncChats:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncAsktable) -> None:
        chat = await async_client.chats.create()
        assert_matches_type(Chat, chat, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncAsktable) -> None:
        chat = await async_client.chats.create(
            bot_id="bot_42",
            datasource_ids=["ds_42"],
            name="name",
            role_id="role_42",
            role_variables={"id": "123123123"},
            user_profile={
                "age": "string",
                "is_male": "string",
                "name": "张三",
            },
        )
        assert_matches_type(Chat, chat, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncAsktable) -> None:
        response = await async_client.chats.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(Chat, chat, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncAsktable) -> None:
        async with async_client.chats.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(Chat, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncAsktable) -> None:
        chat = await async_client.chats.retrieve(
            "chat_id",
        )
        assert_matches_type(ChatRetrieveResponse, chat, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncAsktable) -> None:
        response = await async_client.chats.with_raw_response.retrieve(
            "chat_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(ChatRetrieveResponse, chat, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncAsktable) -> None:
        async with async_client.chats.with_streaming_response.retrieve(
            "chat_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(ChatRetrieveResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncAsktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            await async_client.chats.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncAsktable) -> None:
        chat = await async_client.chats.list()
        assert_matches_type(ChatListResponse, chat, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncAsktable) -> None:
        chat = await async_client.chats.list(
            page=1,
            size=1,
        )
        assert_matches_type(ChatListResponse, chat, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncAsktable) -> None:
        response = await async_client.chats.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(ChatListResponse, chat, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncAsktable) -> None:
        async with async_client.chats.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(ChatListResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete_conversation(self, async_client: AsyncAsktable) -> None:
        chat = await async_client.chats.delete_conversation(
            "chat_id",
        )
        assert_matches_type(object, chat, path=["response"])

    @parametrize
    async def test_raw_response_delete_conversation(self, async_client: AsyncAsktable) -> None:
        response = await async_client.chats.with_raw_response.delete_conversation(
            "chat_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(object, chat, path=["response"])

    @parametrize
    async def test_streaming_response_delete_conversation(self, async_client: AsyncAsktable) -> None:
        async with async_client.chats.with_streaming_response.delete_conversation(
            "chat_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(object, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete_conversation(self, async_client: AsyncAsktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            await async_client.chats.with_raw_response.delete_conversation(
                "",
            )

    @parametrize
    async def test_method_send(self, async_client: AsyncAsktable) -> None:
        chat = await async_client.chats.send(
            chat_id="chat_id",
            question="question",
        )
        assert_matches_type(Message, chat, path=["response"])

    @parametrize
    async def test_raw_response_send(self, async_client: AsyncAsktable) -> None:
        response = await async_client.chats.with_raw_response.send(
            chat_id="chat_id",
            question="question",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(Message, chat, path=["response"])

    @parametrize
    async def test_streaming_response_send(self, async_client: AsyncAsktable) -> None:
        async with async_client.chats.with_streaming_response.send(
            chat_id="chat_id",
            question="question",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(Message, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_send(self, async_client: AsyncAsktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            await async_client.chats.with_raw_response.send(
                chat_id="",
                question="question",
            )
