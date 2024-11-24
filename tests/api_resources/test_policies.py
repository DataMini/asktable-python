# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from asktable import Asktable, AsyncAsktable
from tests.utils import assert_matches_type
from asktable.pagination import SyncPage, AsyncPage
from asktable.types.shared import Policy

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPolicies:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Asktable) -> None:
        policy = client.policies.create(
            dataset_config={"datasource_ids": ["string"]},
            name="name",
            permission="allow",
        )
        assert_matches_type(Policy, policy, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Asktable) -> None:
        policy = client.policies.create(
            dataset_config={
                "datasource_ids": ["string"],
                "regex_patterns": {
                    "fields_regex_pattern": ".*password.* | .*pwd.*",
                    "schemas_regex_pattern": "^public.*$",
                    "tables_regex_pattern": "^(user|shop).*$",
                },
                "rows_filters": {
                    "ds_sJAbnNOUzu3R4DdCCOw2": ["public.shop.merchantId = {{merchant_id}}"],
                    "ds_sJAbnNOUzu3R4DdCCOwe": [
                        "public.user.created_at > '2023-01-01 00:00:00 +00:00'",
                        "public.*.id = {{user_id}}",
                        "public.shop.city_id = {{city_id}}",
                        "*.shop.status = 'online'",
                    ],
                },
            },
            name="name",
            permission="allow",
        )
        assert_matches_type(Policy, policy, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Asktable) -> None:
        response = client.policies.with_raw_response.create(
            dataset_config={"datasource_ids": ["string"]},
            name="name",
            permission="allow",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = response.parse()
        assert_matches_type(Policy, policy, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Asktable) -> None:
        with client.policies.with_streaming_response.create(
            dataset_config={"datasource_ids": ["string"]},
            name="name",
            permission="allow",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = response.parse()
            assert_matches_type(Policy, policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Asktable) -> None:
        policy = client.policies.retrieve(
            "policy_id",
        )
        assert_matches_type(Policy, policy, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Asktable) -> None:
        response = client.policies.with_raw_response.retrieve(
            "policy_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = response.parse()
        assert_matches_type(Policy, policy, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Asktable) -> None:
        with client.policies.with_streaming_response.retrieve(
            "policy_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = response.parse()
            assert_matches_type(Policy, policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Asktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            client.policies.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Asktable) -> None:
        policy = client.policies.update(
            policy_id="policy_id",
        )
        assert_matches_type(Policy, policy, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Asktable) -> None:
        policy = client.policies.update(
            policy_id="policy_id",
            dataset_config={
                "datasource_ids": ["string"],
                "regex_patterns": {
                    "fields_regex_pattern": ".*password.* | .*pwd.*",
                    "schemas_regex_pattern": "^public.*$",
                    "tables_regex_pattern": "^(user|shop).*$",
                },
                "rows_filters": {
                    "ds_sJAbnNOUzu3R4DdCCOw2": [
                        {
                            "condition": "condition",
                            "db_regex": "db_regex",
                            "field_regex": "field_regex",
                            "operator_expression": "operator_expression",
                            "table_regex": "table_regex",
                            "variables": ["string"],
                        }
                    ],
                    "ds_sJAbnNOUzu3R4DdCCOwe": [
                        {
                            "condition": "condition",
                            "db_regex": "db_regex",
                            "field_regex": "field_regex",
                            "operator_expression": "operator_expression",
                            "table_regex": "table_regex",
                            "variables": ["string"],
                        },
                        {
                            "condition": "condition",
                            "db_regex": "db_regex",
                            "field_regex": "field_regex",
                            "operator_expression": "operator_expression",
                            "table_regex": "table_regex",
                            "variables": ["string"],
                        },
                        {
                            "condition": "condition",
                            "db_regex": "db_regex",
                            "field_regex": "field_regex",
                            "operator_expression": "operator_expression",
                            "table_regex": "table_regex",
                            "variables": ["string"],
                        },
                        {
                            "condition": "condition",
                            "db_regex": "db_regex",
                            "field_regex": "field_regex",
                            "operator_expression": "operator_expression",
                            "table_regex": "table_regex",
                            "variables": ["string"],
                        },
                    ],
                },
            },
            name="name",
            permission="allow",
        )
        assert_matches_type(Policy, policy, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Asktable) -> None:
        response = client.policies.with_raw_response.update(
            policy_id="policy_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = response.parse()
        assert_matches_type(Policy, policy, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Asktable) -> None:
        with client.policies.with_streaming_response.update(
            policy_id="policy_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = response.parse()
            assert_matches_type(Policy, policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Asktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            client.policies.with_raw_response.update(
                policy_id="",
            )

    @parametrize
    def test_method_list(self, client: Asktable) -> None:
        policy = client.policies.list()
        assert_matches_type(SyncPage[Policy], policy, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Asktable) -> None:
        policy = client.policies.list(
            name="name",
            page=1,
            policy_ids=["string"],
            size=1,
        )
        assert_matches_type(SyncPage[Policy], policy, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Asktable) -> None:
        response = client.policies.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = response.parse()
        assert_matches_type(SyncPage[Policy], policy, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Asktable) -> None:
        with client.policies.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = response.parse()
            assert_matches_type(SyncPage[Policy], policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Asktable) -> None:
        policy = client.policies.delete(
            "policy_id",
        )
        assert policy is None

    @parametrize
    def test_raw_response_delete(self, client: Asktable) -> None:
        response = client.policies.with_raw_response.delete(
            "policy_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = response.parse()
        assert policy is None

    @parametrize
    def test_streaming_response_delete(self, client: Asktable) -> None:
        with client.policies.with_streaming_response.delete(
            "policy_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = response.parse()
            assert policy is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Asktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            client.policies.with_raw_response.delete(
                "",
            )


class TestAsyncPolicies:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncAsktable) -> None:
        policy = await async_client.policies.create(
            dataset_config={"datasource_ids": ["string"]},
            name="name",
            permission="allow",
        )
        assert_matches_type(Policy, policy, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncAsktable) -> None:
        policy = await async_client.policies.create(
            dataset_config={
                "datasource_ids": ["string"],
                "regex_patterns": {
                    "fields_regex_pattern": ".*password.* | .*pwd.*",
                    "schemas_regex_pattern": "^public.*$",
                    "tables_regex_pattern": "^(user|shop).*$",
                },
                "rows_filters": {
                    "ds_sJAbnNOUzu3R4DdCCOw2": ["public.shop.merchantId = {{merchant_id}}"],
                    "ds_sJAbnNOUzu3R4DdCCOwe": [
                        "public.user.created_at > '2023-01-01 00:00:00 +00:00'",
                        "public.*.id = {{user_id}}",
                        "public.shop.city_id = {{city_id}}",
                        "*.shop.status = 'online'",
                    ],
                },
            },
            name="name",
            permission="allow",
        )
        assert_matches_type(Policy, policy, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncAsktable) -> None:
        response = await async_client.policies.with_raw_response.create(
            dataset_config={"datasource_ids": ["string"]},
            name="name",
            permission="allow",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = await response.parse()
        assert_matches_type(Policy, policy, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncAsktable) -> None:
        async with async_client.policies.with_streaming_response.create(
            dataset_config={"datasource_ids": ["string"]},
            name="name",
            permission="allow",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = await response.parse()
            assert_matches_type(Policy, policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncAsktable) -> None:
        policy = await async_client.policies.retrieve(
            "policy_id",
        )
        assert_matches_type(Policy, policy, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncAsktable) -> None:
        response = await async_client.policies.with_raw_response.retrieve(
            "policy_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = await response.parse()
        assert_matches_type(Policy, policy, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncAsktable) -> None:
        async with async_client.policies.with_streaming_response.retrieve(
            "policy_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = await response.parse()
            assert_matches_type(Policy, policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncAsktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            await async_client.policies.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncAsktable) -> None:
        policy = await async_client.policies.update(
            policy_id="policy_id",
        )
        assert_matches_type(Policy, policy, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncAsktable) -> None:
        policy = await async_client.policies.update(
            policy_id="policy_id",
            dataset_config={
                "datasource_ids": ["string"],
                "regex_patterns": {
                    "fields_regex_pattern": ".*password.* | .*pwd.*",
                    "schemas_regex_pattern": "^public.*$",
                    "tables_regex_pattern": "^(user|shop).*$",
                },
                "rows_filters": {
                    "ds_sJAbnNOUzu3R4DdCCOw2": [
                        {
                            "condition": "condition",
                            "db_regex": "db_regex",
                            "field_regex": "field_regex",
                            "operator_expression": "operator_expression",
                            "table_regex": "table_regex",
                            "variables": ["string"],
                        }
                    ],
                    "ds_sJAbnNOUzu3R4DdCCOwe": [
                        {
                            "condition": "condition",
                            "db_regex": "db_regex",
                            "field_regex": "field_regex",
                            "operator_expression": "operator_expression",
                            "table_regex": "table_regex",
                            "variables": ["string"],
                        },
                        {
                            "condition": "condition",
                            "db_regex": "db_regex",
                            "field_regex": "field_regex",
                            "operator_expression": "operator_expression",
                            "table_regex": "table_regex",
                            "variables": ["string"],
                        },
                        {
                            "condition": "condition",
                            "db_regex": "db_regex",
                            "field_regex": "field_regex",
                            "operator_expression": "operator_expression",
                            "table_regex": "table_regex",
                            "variables": ["string"],
                        },
                        {
                            "condition": "condition",
                            "db_regex": "db_regex",
                            "field_regex": "field_regex",
                            "operator_expression": "operator_expression",
                            "table_regex": "table_regex",
                            "variables": ["string"],
                        },
                    ],
                },
            },
            name="name",
            permission="allow",
        )
        assert_matches_type(Policy, policy, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncAsktable) -> None:
        response = await async_client.policies.with_raw_response.update(
            policy_id="policy_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = await response.parse()
        assert_matches_type(Policy, policy, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncAsktable) -> None:
        async with async_client.policies.with_streaming_response.update(
            policy_id="policy_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = await response.parse()
            assert_matches_type(Policy, policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncAsktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            await async_client.policies.with_raw_response.update(
                policy_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncAsktable) -> None:
        policy = await async_client.policies.list()
        assert_matches_type(AsyncPage[Policy], policy, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncAsktable) -> None:
        policy = await async_client.policies.list(
            name="name",
            page=1,
            policy_ids=["string"],
            size=1,
        )
        assert_matches_type(AsyncPage[Policy], policy, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncAsktable) -> None:
        response = await async_client.policies.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = await response.parse()
        assert_matches_type(AsyncPage[Policy], policy, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncAsktable) -> None:
        async with async_client.policies.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = await response.parse()
            assert_matches_type(AsyncPage[Policy], policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncAsktable) -> None:
        policy = await async_client.policies.delete(
            "policy_id",
        )
        assert policy is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncAsktable) -> None:
        response = await async_client.policies.with_raw_response.delete(
            "policy_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = await response.parse()
        assert policy is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncAsktable) -> None:
        async with async_client.policies.with_streaming_response.delete(
            "policy_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = await response.parse()
            assert policy is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncAsktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            await async_client.policies.with_raw_response.delete(
                "",
            )
