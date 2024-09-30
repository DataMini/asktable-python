# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from asktable import Asktable, AsyncAsktable
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVariables:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Asktable) -> None:
        variable = client.roles.variables.list(
            role_id="role_id",
        )
        assert_matches_type(object, variable, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Asktable) -> None:
        variable = client.roles.variables.list(
            role_id="role_id",
            bot_id="bot_id",
            datasource_ids=["string", "string", "string"],
        )
        assert_matches_type(object, variable, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Asktable) -> None:
        response = client.roles.variables.with_raw_response.list(
            role_id="role_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        variable = response.parse()
        assert_matches_type(object, variable, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Asktable) -> None:
        with client.roles.variables.with_streaming_response.list(
            role_id="role_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            variable = response.parse()
            assert_matches_type(object, variable, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Asktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `role_id` but received ''"):
            client.roles.variables.with_raw_response.list(
                role_id="",
            )


class TestAsyncVariables:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncAsktable) -> None:
        variable = await async_client.roles.variables.list(
            role_id="role_id",
        )
        assert_matches_type(object, variable, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncAsktable) -> None:
        variable = await async_client.roles.variables.list(
            role_id="role_id",
            bot_id="bot_id",
            datasource_ids=["string", "string", "string"],
        )
        assert_matches_type(object, variable, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncAsktable) -> None:
        response = await async_client.roles.variables.with_raw_response.list(
            role_id="role_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        variable = await response.parse()
        assert_matches_type(object, variable, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncAsktable) -> None:
        async with async_client.roles.variables.with_streaming_response.list(
            role_id="role_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            variable = await response.parse()
            assert_matches_type(object, variable, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncAsktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `role_id` but received ''"):
            await async_client.roles.variables.with_raw_response.list(
                role_id="",
            )