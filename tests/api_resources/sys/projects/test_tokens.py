# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from asktable import Asktable, AsyncAsktable
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTokens:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Asktable) -> None:
        token = client.sys.projects.tokens.create(
            project_id="project_id",
        )
        assert_matches_type(object, token, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Asktable) -> None:
        token = client.sys.projects.tokens.create(
            project_id="project_id",
            ak_role="sys",
            chat_role={
                "role_id": "1",
                "role_variables": {"id": "42"},
            },
            token_ttl=900,
            user_profile={"name": "张三"},
        )
        assert_matches_type(object, token, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Asktable) -> None:
        response = client.sys.projects.tokens.with_raw_response.create(
            project_id="project_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = response.parse()
        assert_matches_type(object, token, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Asktable) -> None:
        with client.sys.projects.tokens.with_streaming_response.create(
            project_id="project_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = response.parse()
            assert_matches_type(object, token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Asktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.sys.projects.tokens.with_raw_response.create(
                project_id="",
            )


class TestAsyncTokens:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncAsktable) -> None:
        token = await async_client.sys.projects.tokens.create(
            project_id="project_id",
        )
        assert_matches_type(object, token, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncAsktable) -> None:
        token = await async_client.sys.projects.tokens.create(
            project_id="project_id",
            ak_role="sys",
            chat_role={
                "role_id": "1",
                "role_variables": {"id": "42"},
            },
            token_ttl=900,
            user_profile={"name": "张三"},
        )
        assert_matches_type(object, token, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncAsktable) -> None:
        response = await async_client.sys.projects.tokens.with_raw_response.create(
            project_id="project_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = await response.parse()
        assert_matches_type(object, token, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncAsktable) -> None:
        async with async_client.sys.projects.tokens.with_streaming_response.create(
            project_id="project_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = await response.parse()
            assert_matches_type(object, token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncAsktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.sys.projects.tokens.with_raw_response.create(
                project_id="",
            )
