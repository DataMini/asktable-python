# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from asktable import Asktable, AsyncAsktable
from tests.utils import assert_matches_type
from asktable.types import Chatbot
from asktable.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBots:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Asktable) -> None:
        bot = client.bots.create(
            datasource_ids=["ds_sJAbnNOUzu3R4DdCCOwe"],
            name="name",
        )
        assert_matches_type(Chatbot, bot, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Asktable) -> None:
        bot = client.bots.create(
            datasource_ids=["ds_sJAbnNOUzu3R4DdCCOwe"],
            name="name",
            color_theme="default",
            debug=True,
            extapi_ids=["string"],
            magic_input="magic_input",
            max_rows=50,
            publish=True,
            sample_questions=["你好！今天中午有什么适合我的午餐？"],
            welcome_message="欢迎使用AskTable",
        )
        assert_matches_type(Chatbot, bot, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Asktable) -> None:
        response = client.bots.with_raw_response.create(
            datasource_ids=["ds_sJAbnNOUzu3R4DdCCOwe"],
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bot = response.parse()
        assert_matches_type(Chatbot, bot, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Asktable) -> None:
        with client.bots.with_streaming_response.create(
            datasource_ids=["ds_sJAbnNOUzu3R4DdCCOwe"],
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bot = response.parse()
            assert_matches_type(Chatbot, bot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Asktable) -> None:
        bot = client.bots.retrieve(
            "bot_id",
        )
        assert_matches_type(Chatbot, bot, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Asktable) -> None:
        response = client.bots.with_raw_response.retrieve(
            "bot_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bot = response.parse()
        assert_matches_type(Chatbot, bot, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Asktable) -> None:
        with client.bots.with_streaming_response.retrieve(
            "bot_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bot = response.parse()
            assert_matches_type(Chatbot, bot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Asktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bot_id` but received ''"):
            client.bots.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Asktable) -> None:
        bot = client.bots.update(
            bot_id="bot_id",
        )
        assert_matches_type(Chatbot, bot, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Asktable) -> None:
        bot = client.bots.update(
            bot_id="bot_id",
            avatar_url="avatar_url",
            color_theme="default",
            datasource_ids=["ds_sJAbnNOUzu3R4DdCCOwe"],
            debug=True,
            extapi_ids=["string"],
            magic_input="magic_input",
            max_rows=50,
            name="name",
            publish=True,
            sample_questions=["你好！今天中午有什么适合我的午餐？"],
            welcome_message="欢迎使用AskTable",
        )
        assert_matches_type(Chatbot, bot, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Asktable) -> None:
        response = client.bots.with_raw_response.update(
            bot_id="bot_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bot = response.parse()
        assert_matches_type(Chatbot, bot, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Asktable) -> None:
        with client.bots.with_streaming_response.update(
            bot_id="bot_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bot = response.parse()
            assert_matches_type(Chatbot, bot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Asktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bot_id` but received ''"):
            client.bots.with_raw_response.update(
                bot_id="",
            )

    @parametrize
    def test_method_list(self, client: Asktable) -> None:
        bot = client.bots.list()
        assert_matches_type(SyncPage[Chatbot], bot, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Asktable) -> None:
        bot = client.bots.list(
            name="name",
            page=1,
            size=1,
        )
        assert_matches_type(SyncPage[Chatbot], bot, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Asktable) -> None:
        response = client.bots.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bot = response.parse()
        assert_matches_type(SyncPage[Chatbot], bot, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Asktable) -> None:
        with client.bots.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bot = response.parse()
            assert_matches_type(SyncPage[Chatbot], bot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Asktable) -> None:
        bot = client.bots.delete(
            "bot_id",
        )
        assert_matches_type(object, bot, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Asktable) -> None:
        response = client.bots.with_raw_response.delete(
            "bot_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bot = response.parse()
        assert_matches_type(object, bot, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Asktable) -> None:
        with client.bots.with_streaming_response.delete(
            "bot_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bot = response.parse()
            assert_matches_type(object, bot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Asktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bot_id` but received ''"):
            client.bots.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_invite(self, client: Asktable) -> None:
        bot = client.bots.invite(
            bot_id="bot_id",
            project_id="project_id",
        )
        assert_matches_type(object, bot, path=["response"])

    @parametrize
    def test_raw_response_invite(self, client: Asktable) -> None:
        response = client.bots.with_raw_response.invite(
            bot_id="bot_id",
            project_id="project_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bot = response.parse()
        assert_matches_type(object, bot, path=["response"])

    @parametrize
    def test_streaming_response_invite(self, client: Asktable) -> None:
        with client.bots.with_streaming_response.invite(
            bot_id="bot_id",
            project_id="project_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bot = response.parse()
            assert_matches_type(object, bot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_invite(self, client: Asktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bot_id` but received ''"):
            client.bots.with_raw_response.invite(
                bot_id="",
                project_id="project_id",
            )


class TestAsyncBots:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncAsktable) -> None:
        bot = await async_client.bots.create(
            datasource_ids=["ds_sJAbnNOUzu3R4DdCCOwe"],
            name="name",
        )
        assert_matches_type(Chatbot, bot, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncAsktable) -> None:
        bot = await async_client.bots.create(
            datasource_ids=["ds_sJAbnNOUzu3R4DdCCOwe"],
            name="name",
            color_theme="default",
            debug=True,
            extapi_ids=["string"],
            magic_input="magic_input",
            max_rows=50,
            publish=True,
            sample_questions=["你好！今天中午有什么适合我的午餐？"],
            welcome_message="欢迎使用AskTable",
        )
        assert_matches_type(Chatbot, bot, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncAsktable) -> None:
        response = await async_client.bots.with_raw_response.create(
            datasource_ids=["ds_sJAbnNOUzu3R4DdCCOwe"],
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bot = await response.parse()
        assert_matches_type(Chatbot, bot, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncAsktable) -> None:
        async with async_client.bots.with_streaming_response.create(
            datasource_ids=["ds_sJAbnNOUzu3R4DdCCOwe"],
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bot = await response.parse()
            assert_matches_type(Chatbot, bot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncAsktable) -> None:
        bot = await async_client.bots.retrieve(
            "bot_id",
        )
        assert_matches_type(Chatbot, bot, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncAsktable) -> None:
        response = await async_client.bots.with_raw_response.retrieve(
            "bot_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bot = await response.parse()
        assert_matches_type(Chatbot, bot, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncAsktable) -> None:
        async with async_client.bots.with_streaming_response.retrieve(
            "bot_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bot = await response.parse()
            assert_matches_type(Chatbot, bot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncAsktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bot_id` but received ''"):
            await async_client.bots.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncAsktable) -> None:
        bot = await async_client.bots.update(
            bot_id="bot_id",
        )
        assert_matches_type(Chatbot, bot, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncAsktable) -> None:
        bot = await async_client.bots.update(
            bot_id="bot_id",
            avatar_url="avatar_url",
            color_theme="default",
            datasource_ids=["ds_sJAbnNOUzu3R4DdCCOwe"],
            debug=True,
            extapi_ids=["string"],
            magic_input="magic_input",
            max_rows=50,
            name="name",
            publish=True,
            sample_questions=["你好！今天中午有什么适合我的午餐？"],
            welcome_message="欢迎使用AskTable",
        )
        assert_matches_type(Chatbot, bot, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncAsktable) -> None:
        response = await async_client.bots.with_raw_response.update(
            bot_id="bot_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bot = await response.parse()
        assert_matches_type(Chatbot, bot, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncAsktable) -> None:
        async with async_client.bots.with_streaming_response.update(
            bot_id="bot_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bot = await response.parse()
            assert_matches_type(Chatbot, bot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncAsktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bot_id` but received ''"):
            await async_client.bots.with_raw_response.update(
                bot_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncAsktable) -> None:
        bot = await async_client.bots.list()
        assert_matches_type(AsyncPage[Chatbot], bot, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncAsktable) -> None:
        bot = await async_client.bots.list(
            name="name",
            page=1,
            size=1,
        )
        assert_matches_type(AsyncPage[Chatbot], bot, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncAsktable) -> None:
        response = await async_client.bots.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bot = await response.parse()
        assert_matches_type(AsyncPage[Chatbot], bot, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncAsktable) -> None:
        async with async_client.bots.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bot = await response.parse()
            assert_matches_type(AsyncPage[Chatbot], bot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncAsktable) -> None:
        bot = await async_client.bots.delete(
            "bot_id",
        )
        assert_matches_type(object, bot, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncAsktable) -> None:
        response = await async_client.bots.with_raw_response.delete(
            "bot_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bot = await response.parse()
        assert_matches_type(object, bot, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncAsktable) -> None:
        async with async_client.bots.with_streaming_response.delete(
            "bot_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bot = await response.parse()
            assert_matches_type(object, bot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncAsktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bot_id` but received ''"):
            await async_client.bots.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_invite(self, async_client: AsyncAsktable) -> None:
        bot = await async_client.bots.invite(
            bot_id="bot_id",
            project_id="project_id",
        )
        assert_matches_type(object, bot, path=["response"])

    @parametrize
    async def test_raw_response_invite(self, async_client: AsyncAsktable) -> None:
        response = await async_client.bots.with_raw_response.invite(
            bot_id="bot_id",
            project_id="project_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bot = await response.parse()
        assert_matches_type(object, bot, path=["response"])

    @parametrize
    async def test_streaming_response_invite(self, async_client: AsyncAsktable) -> None:
        async with async_client.bots.with_streaming_response.invite(
            bot_id="bot_id",
            project_id="project_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bot = await response.parse()
            assert_matches_type(object, bot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_invite(self, async_client: AsyncAsktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bot_id` but received ''"):
            await async_client.bots.with_raw_response.invite(
                bot_id="",
                project_id="project_id",
            )
