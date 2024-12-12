# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from asktable import Asktable, AsyncAsktable
from tests.utils import assert_matches_type
from asktable.pagination import SyncPage, AsyncPage
from asktable.types.chats import (
    MessageListResponse,
    MessageRetrieveResponse,
    MessageSendMessageResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMessages:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Asktable) -> None:
        message = client.chats.messages.retrieve(
            message_id="message_id",
            chat_id="chat_id",
        )
        assert_matches_type(MessageRetrieveResponse, message, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Asktable) -> None:
        response = client.chats.messages.with_raw_response.retrieve(
            message_id="message_id",
            chat_id="chat_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(MessageRetrieveResponse, message, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Asktable) -> None:
        with client.chats.messages.with_streaming_response.retrieve(
            message_id="message_id",
            chat_id="chat_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(MessageRetrieveResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Asktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            client.chats.messages.with_raw_response.retrieve(
                message_id="message_id",
                chat_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.chats.messages.with_raw_response.retrieve(
                message_id="",
                chat_id="chat_id",
            )

    @parametrize
    def test_method_list(self, client: Asktable) -> None:
        message = client.chats.messages.list(
            chat_id="chat_id",
        )
        assert_matches_type(SyncPage[MessageListResponse], message, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Asktable) -> None:
        message = client.chats.messages.list(
            chat_id="chat_id",
            page=1,
            size=1,
        )
        assert_matches_type(SyncPage[MessageListResponse], message, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Asktable) -> None:
        response = client.chats.messages.with_raw_response.list(
            chat_id="chat_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(SyncPage[MessageListResponse], message, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Asktable) -> None:
        with client.chats.messages.with_streaming_response.list(
            chat_id="chat_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(SyncPage[MessageListResponse], message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Asktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            client.chats.messages.with_raw_response.list(
                chat_id="",
            )

    @parametrize
    def test_method_send_message(self, client: Asktable) -> None:
        message = client.chats.messages.send_message(
            chat_id="chat_id",
            question="question",
        )
        assert_matches_type(MessageSendMessageResponse, message, path=["response"])

    @parametrize
    def test_raw_response_send_message(self, client: Asktable) -> None:
        response = client.chats.messages.with_raw_response.send_message(
            chat_id="chat_id",
            question="question",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(MessageSendMessageResponse, message, path=["response"])

    @parametrize
    def test_streaming_response_send_message(self, client: Asktable) -> None:
        with client.chats.messages.with_streaming_response.send_message(
            chat_id="chat_id",
            question="question",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(MessageSendMessageResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_send_message(self, client: Asktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            client.chats.messages.with_raw_response.send_message(
                chat_id="",
                question="question",
            )


class TestAsyncMessages:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncAsktable) -> None:
        message = await async_client.chats.messages.retrieve(
            message_id="message_id",
            chat_id="chat_id",
        )
        assert_matches_type(MessageRetrieveResponse, message, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncAsktable) -> None:
        response = await async_client.chats.messages.with_raw_response.retrieve(
            message_id="message_id",
            chat_id="chat_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(MessageRetrieveResponse, message, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncAsktable) -> None:
        async with async_client.chats.messages.with_streaming_response.retrieve(
            message_id="message_id",
            chat_id="chat_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(MessageRetrieveResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncAsktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            await async_client.chats.messages.with_raw_response.retrieve(
                message_id="message_id",
                chat_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.chats.messages.with_raw_response.retrieve(
                message_id="",
                chat_id="chat_id",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncAsktable) -> None:
        message = await async_client.chats.messages.list(
            chat_id="chat_id",
        )
        assert_matches_type(AsyncPage[MessageListResponse], message, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncAsktable) -> None:
        message = await async_client.chats.messages.list(
            chat_id="chat_id",
            page=1,
            size=1,
        )
        assert_matches_type(AsyncPage[MessageListResponse], message, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncAsktable) -> None:
        response = await async_client.chats.messages.with_raw_response.list(
            chat_id="chat_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(AsyncPage[MessageListResponse], message, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncAsktable) -> None:
        async with async_client.chats.messages.with_streaming_response.list(
            chat_id="chat_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(AsyncPage[MessageListResponse], message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncAsktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            await async_client.chats.messages.with_raw_response.list(
                chat_id="",
            )

    @parametrize
    async def test_method_send_message(self, async_client: AsyncAsktable) -> None:
        message = await async_client.chats.messages.send_message(
            chat_id="chat_id",
            question="question",
        )
        assert_matches_type(MessageSendMessageResponse, message, path=["response"])

    @parametrize
    async def test_raw_response_send_message(self, async_client: AsyncAsktable) -> None:
        response = await async_client.chats.messages.with_raw_response.send_message(
            chat_id="chat_id",
            question="question",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(MessageSendMessageResponse, message, path=["response"])

    @parametrize
    async def test_streaming_response_send_message(self, async_client: AsyncAsktable) -> None:
        async with async_client.chats.messages.with_streaming_response.send_message(
            chat_id="chat_id",
            question="question",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(MessageSendMessageResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_send_message(self, async_client: AsyncAsktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            await async_client.chats.messages.with_raw_response.send_message(
                chat_id="",
                question="question",
            )
