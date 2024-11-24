# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from asktable import Asktable, AsyncAsktable
from tests.utils import assert_matches_type
from asktable.types import (
    Role,
    RoleGetPolicesResponse,
)
from asktable.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRoles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Asktable) -> None:
        role = client.roles.create(
            name="name",
        )
        assert_matches_type(Role, role, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Asktable) -> None:
        role = client.roles.create(
            name="name",
            policy_ids=["policy_6uOnay1xDNsxLoHmCGf3", "policy_6uOnay1xDNsxLoHmCGf2"],
        )
        assert_matches_type(Role, role, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Asktable) -> None:
        response = client.roles.with_raw_response.create(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        role = response.parse()
        assert_matches_type(Role, role, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Asktable) -> None:
        with client.roles.with_streaming_response.create(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            role = response.parse()
            assert_matches_type(Role, role, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Asktable) -> None:
        role = client.roles.retrieve(
            "role_id",
        )
        assert_matches_type(Role, role, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Asktable) -> None:
        response = client.roles.with_raw_response.retrieve(
            "role_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        role = response.parse()
        assert_matches_type(Role, role, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Asktable) -> None:
        with client.roles.with_streaming_response.retrieve(
            "role_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            role = response.parse()
            assert_matches_type(Role, role, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Asktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `role_id` but received ''"):
            client.roles.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Asktable) -> None:
        role = client.roles.update(
            role_id="role_id",
        )
        assert_matches_type(Role, role, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Asktable) -> None:
        role = client.roles.update(
            role_id="role_id",
            name="name",
            policy_ids=["policy_6uOnay1xDNsxLoHmCGf3", "policy_6uOnay1xDNsxLoHmCGf2"],
        )
        assert_matches_type(Role, role, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Asktable) -> None:
        response = client.roles.with_raw_response.update(
            role_id="role_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        role = response.parse()
        assert_matches_type(Role, role, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Asktable) -> None:
        with client.roles.with_streaming_response.update(
            role_id="role_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            role = response.parse()
            assert_matches_type(Role, role, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Asktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `role_id` but received ''"):
            client.roles.with_raw_response.update(
                role_id="",
            )

    @parametrize
    def test_method_list(self, client: Asktable) -> None:
        role = client.roles.list()
        assert_matches_type(SyncPage[Role], role, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Asktable) -> None:
        role = client.roles.list(
            name="name",
            page=1,
            role_ids=["string"],
            size=1,
        )
        assert_matches_type(SyncPage[Role], role, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Asktable) -> None:
        response = client.roles.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        role = response.parse()
        assert_matches_type(SyncPage[Role], role, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Asktable) -> None:
        with client.roles.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            role = response.parse()
            assert_matches_type(SyncPage[Role], role, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Asktable) -> None:
        role = client.roles.delete(
            "role_id",
        )
        assert_matches_type(object, role, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Asktable) -> None:
        response = client.roles.with_raw_response.delete(
            "role_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        role = response.parse()
        assert_matches_type(object, role, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Asktable) -> None:
        with client.roles.with_streaming_response.delete(
            "role_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            role = response.parse()
            assert_matches_type(object, role, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Asktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `role_id` but received ''"):
            client.roles.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_get_polices(self, client: Asktable) -> None:
        role = client.roles.get_polices(
            "role_id",
        )
        assert_matches_type(RoleGetPolicesResponse, role, path=["response"])

    @parametrize
    def test_raw_response_get_polices(self, client: Asktable) -> None:
        response = client.roles.with_raw_response.get_polices(
            "role_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        role = response.parse()
        assert_matches_type(RoleGetPolicesResponse, role, path=["response"])

    @parametrize
    def test_streaming_response_get_polices(self, client: Asktable) -> None:
        with client.roles.with_streaming_response.get_polices(
            "role_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            role = response.parse()
            assert_matches_type(RoleGetPolicesResponse, role, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_polices(self, client: Asktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `role_id` but received ''"):
            client.roles.with_raw_response.get_polices(
                "",
            )

    @parametrize
    def test_method_get_variables(self, client: Asktable) -> None:
        role = client.roles.get_variables(
            role_id="role_id",
        )
        assert_matches_type(object, role, path=["response"])

    @parametrize
    def test_method_get_variables_with_all_params(self, client: Asktable) -> None:
        role = client.roles.get_variables(
            role_id="role_id",
            bot_id="bot_id",
            datasource_ids=["string"],
        )
        assert_matches_type(object, role, path=["response"])

    @parametrize
    def test_raw_response_get_variables(self, client: Asktable) -> None:
        response = client.roles.with_raw_response.get_variables(
            role_id="role_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        role = response.parse()
        assert_matches_type(object, role, path=["response"])

    @parametrize
    def test_streaming_response_get_variables(self, client: Asktable) -> None:
        with client.roles.with_streaming_response.get_variables(
            role_id="role_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            role = response.parse()
            assert_matches_type(object, role, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_variables(self, client: Asktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `role_id` but received ''"):
            client.roles.with_raw_response.get_variables(
                role_id="",
            )


class TestAsyncRoles:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncAsktable) -> None:
        role = await async_client.roles.create(
            name="name",
        )
        assert_matches_type(Role, role, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncAsktable) -> None:
        role = await async_client.roles.create(
            name="name",
            policy_ids=["policy_6uOnay1xDNsxLoHmCGf3", "policy_6uOnay1xDNsxLoHmCGf2"],
        )
        assert_matches_type(Role, role, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncAsktable) -> None:
        response = await async_client.roles.with_raw_response.create(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        role = await response.parse()
        assert_matches_type(Role, role, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncAsktable) -> None:
        async with async_client.roles.with_streaming_response.create(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            role = await response.parse()
            assert_matches_type(Role, role, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncAsktable) -> None:
        role = await async_client.roles.retrieve(
            "role_id",
        )
        assert_matches_type(Role, role, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncAsktable) -> None:
        response = await async_client.roles.with_raw_response.retrieve(
            "role_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        role = await response.parse()
        assert_matches_type(Role, role, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncAsktable) -> None:
        async with async_client.roles.with_streaming_response.retrieve(
            "role_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            role = await response.parse()
            assert_matches_type(Role, role, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncAsktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `role_id` but received ''"):
            await async_client.roles.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncAsktable) -> None:
        role = await async_client.roles.update(
            role_id="role_id",
        )
        assert_matches_type(Role, role, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncAsktable) -> None:
        role = await async_client.roles.update(
            role_id="role_id",
            name="name",
            policy_ids=["policy_6uOnay1xDNsxLoHmCGf3", "policy_6uOnay1xDNsxLoHmCGf2"],
        )
        assert_matches_type(Role, role, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncAsktable) -> None:
        response = await async_client.roles.with_raw_response.update(
            role_id="role_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        role = await response.parse()
        assert_matches_type(Role, role, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncAsktable) -> None:
        async with async_client.roles.with_streaming_response.update(
            role_id="role_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            role = await response.parse()
            assert_matches_type(Role, role, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncAsktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `role_id` but received ''"):
            await async_client.roles.with_raw_response.update(
                role_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncAsktable) -> None:
        role = await async_client.roles.list()
        assert_matches_type(AsyncPage[Role], role, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncAsktable) -> None:
        role = await async_client.roles.list(
            name="name",
            page=1,
            role_ids=["string"],
            size=1,
        )
        assert_matches_type(AsyncPage[Role], role, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncAsktable) -> None:
        response = await async_client.roles.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        role = await response.parse()
        assert_matches_type(AsyncPage[Role], role, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncAsktable) -> None:
        async with async_client.roles.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            role = await response.parse()
            assert_matches_type(AsyncPage[Role], role, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncAsktable) -> None:
        role = await async_client.roles.delete(
            "role_id",
        )
        assert_matches_type(object, role, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncAsktable) -> None:
        response = await async_client.roles.with_raw_response.delete(
            "role_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        role = await response.parse()
        assert_matches_type(object, role, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncAsktable) -> None:
        async with async_client.roles.with_streaming_response.delete(
            "role_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            role = await response.parse()
            assert_matches_type(object, role, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncAsktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `role_id` but received ''"):
            await async_client.roles.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_get_polices(self, async_client: AsyncAsktable) -> None:
        role = await async_client.roles.get_polices(
            "role_id",
        )
        assert_matches_type(RoleGetPolicesResponse, role, path=["response"])

    @parametrize
    async def test_raw_response_get_polices(self, async_client: AsyncAsktable) -> None:
        response = await async_client.roles.with_raw_response.get_polices(
            "role_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        role = await response.parse()
        assert_matches_type(RoleGetPolicesResponse, role, path=["response"])

    @parametrize
    async def test_streaming_response_get_polices(self, async_client: AsyncAsktable) -> None:
        async with async_client.roles.with_streaming_response.get_polices(
            "role_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            role = await response.parse()
            assert_matches_type(RoleGetPolicesResponse, role, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_polices(self, async_client: AsyncAsktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `role_id` but received ''"):
            await async_client.roles.with_raw_response.get_polices(
                "",
            )

    @parametrize
    async def test_method_get_variables(self, async_client: AsyncAsktable) -> None:
        role = await async_client.roles.get_variables(
            role_id="role_id",
        )
        assert_matches_type(object, role, path=["response"])

    @parametrize
    async def test_method_get_variables_with_all_params(self, async_client: AsyncAsktable) -> None:
        role = await async_client.roles.get_variables(
            role_id="role_id",
            bot_id="bot_id",
            datasource_ids=["string"],
        )
        assert_matches_type(object, role, path=["response"])

    @parametrize
    async def test_raw_response_get_variables(self, async_client: AsyncAsktable) -> None:
        response = await async_client.roles.with_raw_response.get_variables(
            role_id="role_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        role = await response.parse()
        assert_matches_type(object, role, path=["response"])

    @parametrize
    async def test_streaming_response_get_variables(self, async_client: AsyncAsktable) -> None:
        async with async_client.roles.with_streaming_response.get_variables(
            role_id="role_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            role = await response.parse()
            assert_matches_type(object, role, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_variables(self, async_client: AsyncAsktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `role_id` but received ''"):
            await async_client.roles.with_raw_response.get_variables(
                role_id="",
            )
