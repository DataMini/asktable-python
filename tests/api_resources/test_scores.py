# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from asktable import Asktable, AsyncAsktable
from tests.utils import assert_matches_type
from asktable.types import ScoreCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestScores:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Asktable) -> None:
        score = client.scores.create(
            chat_id="chat_id",
            message_id="message_id",
            score=True,
        )
        assert_matches_type(ScoreCreateResponse, score, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Asktable) -> None:
        response = client.scores.with_raw_response.create(
            chat_id="chat_id",
            message_id="message_id",
            score=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        score = response.parse()
        assert_matches_type(ScoreCreateResponse, score, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Asktable) -> None:
        with client.scores.with_streaming_response.create(
            chat_id="chat_id",
            message_id="message_id",
            score=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            score = response.parse()
            assert_matches_type(ScoreCreateResponse, score, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncScores:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncAsktable) -> None:
        score = await async_client.scores.create(
            chat_id="chat_id",
            message_id="message_id",
            score=True,
        )
        assert_matches_type(ScoreCreateResponse, score, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncAsktable) -> None:
        response = await async_client.scores.with_raw_response.create(
            chat_id="chat_id",
            message_id="message_id",
            score=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        score = await response.parse()
        assert_matches_type(ScoreCreateResponse, score, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncAsktable) -> None:
        async with async_client.scores.with_streaming_response.create(
            chat_id="chat_id",
            message_id="message_id",
            score=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            score = await response.parse()
            assert_matches_type(ScoreCreateResponse, score, path=["response"])

        assert cast(Any, response.is_closed) is True
