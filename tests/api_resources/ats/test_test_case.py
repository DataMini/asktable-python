# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from asktable import Asktable, AsyncAsktable
from tests.utils import assert_matches_type
from asktable.types.ats import (
    TestCaseListResponse,
    TestCaseCreateResponse,
    TestCaseUpdateResponse,
    TestCaseRetrieveResponse,
)
from asktable.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTestCase:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Asktable) -> None:
        test_case = client.ats.test_case.create(
            ats_id="ats_id",
            expected_sql="expected_sql",
            question="question",
        )
        assert_matches_type(TestCaseCreateResponse, test_case, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Asktable) -> None:
        test_case = client.ats.test_case.create(
            ats_id="ats_id",
            expected_sql="expected_sql",
            question="question",
            role_id="role_id",
            role_variables={},
        )
        assert_matches_type(TestCaseCreateResponse, test_case, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Asktable) -> None:
        response = client.ats.test_case.with_raw_response.create(
            ats_id="ats_id",
            expected_sql="expected_sql",
            question="question",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test_case = response.parse()
        assert_matches_type(TestCaseCreateResponse, test_case, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Asktable) -> None:
        with client.ats.test_case.with_streaming_response.create(
            ats_id="ats_id",
            expected_sql="expected_sql",
            question="question",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test_case = response.parse()
            assert_matches_type(TestCaseCreateResponse, test_case, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Asktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ats_id` but received ''"):
            client.ats.test_case.with_raw_response.create(
                ats_id="",
                expected_sql="expected_sql",
                question="question",
            )

    @parametrize
    def test_method_retrieve(self, client: Asktable) -> None:
        test_case = client.ats.test_case.retrieve(
            atc_id="atc_id",
            ats_id="ats_id",
        )
        assert_matches_type(TestCaseRetrieveResponse, test_case, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Asktable) -> None:
        response = client.ats.test_case.with_raw_response.retrieve(
            atc_id="atc_id",
            ats_id="ats_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test_case = response.parse()
        assert_matches_type(TestCaseRetrieveResponse, test_case, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Asktable) -> None:
        with client.ats.test_case.with_streaming_response.retrieve(
            atc_id="atc_id",
            ats_id="ats_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test_case = response.parse()
            assert_matches_type(TestCaseRetrieveResponse, test_case, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Asktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ats_id` but received ''"):
            client.ats.test_case.with_raw_response.retrieve(
                atc_id="atc_id",
                ats_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `atc_id` but received ''"):
            client.ats.test_case.with_raw_response.retrieve(
                atc_id="",
                ats_id="ats_id",
            )

    @parametrize
    def test_method_update(self, client: Asktable) -> None:
        test_case = client.ats.test_case.update(
            atc_id="atc_id",
            ats_id="ats_id",
            expected_sql="expected_sql",
            question="question",
        )
        assert_matches_type(TestCaseUpdateResponse, test_case, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Asktable) -> None:
        test_case = client.ats.test_case.update(
            atc_id="atc_id",
            ats_id="ats_id",
            expected_sql="expected_sql",
            question="question",
            role_id="role_id",
            role_variables={},
        )
        assert_matches_type(TestCaseUpdateResponse, test_case, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Asktable) -> None:
        response = client.ats.test_case.with_raw_response.update(
            atc_id="atc_id",
            ats_id="ats_id",
            expected_sql="expected_sql",
            question="question",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test_case = response.parse()
        assert_matches_type(TestCaseUpdateResponse, test_case, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Asktable) -> None:
        with client.ats.test_case.with_streaming_response.update(
            atc_id="atc_id",
            ats_id="ats_id",
            expected_sql="expected_sql",
            question="question",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test_case = response.parse()
            assert_matches_type(TestCaseUpdateResponse, test_case, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Asktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ats_id` but received ''"):
            client.ats.test_case.with_raw_response.update(
                atc_id="atc_id",
                ats_id="",
                expected_sql="expected_sql",
                question="question",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `atc_id` but received ''"):
            client.ats.test_case.with_raw_response.update(
                atc_id="",
                ats_id="ats_id",
                expected_sql="expected_sql",
                question="question",
            )

    @parametrize
    def test_method_list(self, client: Asktable) -> None:
        test_case = client.ats.test_case.list(
            ats_id="ats_id",
        )
        assert_matches_type(SyncPage[TestCaseListResponse], test_case, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Asktable) -> None:
        test_case = client.ats.test_case.list(
            ats_id="ats_id",
            page=1,
            size=1,
        )
        assert_matches_type(SyncPage[TestCaseListResponse], test_case, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Asktable) -> None:
        response = client.ats.test_case.with_raw_response.list(
            ats_id="ats_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test_case = response.parse()
        assert_matches_type(SyncPage[TestCaseListResponse], test_case, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Asktable) -> None:
        with client.ats.test_case.with_streaming_response.list(
            ats_id="ats_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test_case = response.parse()
            assert_matches_type(SyncPage[TestCaseListResponse], test_case, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Asktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ats_id` but received ''"):
            client.ats.test_case.with_raw_response.list(
                ats_id="",
            )

    @parametrize
    def test_method_delete(self, client: Asktable) -> None:
        test_case = client.ats.test_case.delete(
            atc_id="atc_id",
            ats_id="ats_id",
        )
        assert_matches_type(object, test_case, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Asktable) -> None:
        response = client.ats.test_case.with_raw_response.delete(
            atc_id="atc_id",
            ats_id="ats_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test_case = response.parse()
        assert_matches_type(object, test_case, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Asktable) -> None:
        with client.ats.test_case.with_streaming_response.delete(
            atc_id="atc_id",
            ats_id="ats_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test_case = response.parse()
            assert_matches_type(object, test_case, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Asktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ats_id` but received ''"):
            client.ats.test_case.with_raw_response.delete(
                atc_id="atc_id",
                ats_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `atc_id` but received ''"):
            client.ats.test_case.with_raw_response.delete(
                atc_id="",
                ats_id="ats_id",
            )


class TestAsyncTestCase:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncAsktable) -> None:
        test_case = await async_client.ats.test_case.create(
            ats_id="ats_id",
            expected_sql="expected_sql",
            question="question",
        )
        assert_matches_type(TestCaseCreateResponse, test_case, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncAsktable) -> None:
        test_case = await async_client.ats.test_case.create(
            ats_id="ats_id",
            expected_sql="expected_sql",
            question="question",
            role_id="role_id",
            role_variables={},
        )
        assert_matches_type(TestCaseCreateResponse, test_case, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncAsktable) -> None:
        response = await async_client.ats.test_case.with_raw_response.create(
            ats_id="ats_id",
            expected_sql="expected_sql",
            question="question",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test_case = await response.parse()
        assert_matches_type(TestCaseCreateResponse, test_case, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncAsktable) -> None:
        async with async_client.ats.test_case.with_streaming_response.create(
            ats_id="ats_id",
            expected_sql="expected_sql",
            question="question",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test_case = await response.parse()
            assert_matches_type(TestCaseCreateResponse, test_case, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncAsktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ats_id` but received ''"):
            await async_client.ats.test_case.with_raw_response.create(
                ats_id="",
                expected_sql="expected_sql",
                question="question",
            )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncAsktable) -> None:
        test_case = await async_client.ats.test_case.retrieve(
            atc_id="atc_id",
            ats_id="ats_id",
        )
        assert_matches_type(TestCaseRetrieveResponse, test_case, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncAsktable) -> None:
        response = await async_client.ats.test_case.with_raw_response.retrieve(
            atc_id="atc_id",
            ats_id="ats_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test_case = await response.parse()
        assert_matches_type(TestCaseRetrieveResponse, test_case, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncAsktable) -> None:
        async with async_client.ats.test_case.with_streaming_response.retrieve(
            atc_id="atc_id",
            ats_id="ats_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test_case = await response.parse()
            assert_matches_type(TestCaseRetrieveResponse, test_case, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncAsktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ats_id` but received ''"):
            await async_client.ats.test_case.with_raw_response.retrieve(
                atc_id="atc_id",
                ats_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `atc_id` but received ''"):
            await async_client.ats.test_case.with_raw_response.retrieve(
                atc_id="",
                ats_id="ats_id",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncAsktable) -> None:
        test_case = await async_client.ats.test_case.update(
            atc_id="atc_id",
            ats_id="ats_id",
            expected_sql="expected_sql",
            question="question",
        )
        assert_matches_type(TestCaseUpdateResponse, test_case, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncAsktable) -> None:
        test_case = await async_client.ats.test_case.update(
            atc_id="atc_id",
            ats_id="ats_id",
            expected_sql="expected_sql",
            question="question",
            role_id="role_id",
            role_variables={},
        )
        assert_matches_type(TestCaseUpdateResponse, test_case, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncAsktable) -> None:
        response = await async_client.ats.test_case.with_raw_response.update(
            atc_id="atc_id",
            ats_id="ats_id",
            expected_sql="expected_sql",
            question="question",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test_case = await response.parse()
        assert_matches_type(TestCaseUpdateResponse, test_case, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncAsktable) -> None:
        async with async_client.ats.test_case.with_streaming_response.update(
            atc_id="atc_id",
            ats_id="ats_id",
            expected_sql="expected_sql",
            question="question",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test_case = await response.parse()
            assert_matches_type(TestCaseUpdateResponse, test_case, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncAsktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ats_id` but received ''"):
            await async_client.ats.test_case.with_raw_response.update(
                atc_id="atc_id",
                ats_id="",
                expected_sql="expected_sql",
                question="question",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `atc_id` but received ''"):
            await async_client.ats.test_case.with_raw_response.update(
                atc_id="",
                ats_id="ats_id",
                expected_sql="expected_sql",
                question="question",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncAsktable) -> None:
        test_case = await async_client.ats.test_case.list(
            ats_id="ats_id",
        )
        assert_matches_type(AsyncPage[TestCaseListResponse], test_case, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncAsktable) -> None:
        test_case = await async_client.ats.test_case.list(
            ats_id="ats_id",
            page=1,
            size=1,
        )
        assert_matches_type(AsyncPage[TestCaseListResponse], test_case, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncAsktable) -> None:
        response = await async_client.ats.test_case.with_raw_response.list(
            ats_id="ats_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test_case = await response.parse()
        assert_matches_type(AsyncPage[TestCaseListResponse], test_case, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncAsktable) -> None:
        async with async_client.ats.test_case.with_streaming_response.list(
            ats_id="ats_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test_case = await response.parse()
            assert_matches_type(AsyncPage[TestCaseListResponse], test_case, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncAsktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ats_id` but received ''"):
            await async_client.ats.test_case.with_raw_response.list(
                ats_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncAsktable) -> None:
        test_case = await async_client.ats.test_case.delete(
            atc_id="atc_id",
            ats_id="ats_id",
        )
        assert_matches_type(object, test_case, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncAsktable) -> None:
        response = await async_client.ats.test_case.with_raw_response.delete(
            atc_id="atc_id",
            ats_id="ats_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test_case = await response.parse()
        assert_matches_type(object, test_case, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncAsktable) -> None:
        async with async_client.ats.test_case.with_streaming_response.delete(
            atc_id="atc_id",
            ats_id="ats_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test_case = await response.parse()
            assert_matches_type(object, test_case, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncAsktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ats_id` but received ''"):
            await async_client.ats.test_case.with_raw_response.delete(
                atc_id="atc_id",
                ats_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `atc_id` but received ''"):
            await async_client.ats.test_case.with_raw_response.delete(
                atc_id="",
                ats_id="ats_id",
            )
