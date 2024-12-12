# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from asktable import Asktable, AsyncAsktable
from tests.utils import assert_matches_type
from asktable.types import (
    Entry,
    EntryWithDefinition,
    BusinessGlossaryCreateResponse,
)
from asktable.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBusinessGlossary:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Asktable) -> None:
        business_glossary = client.business_glossary.create(
            body=[
                {
                    "definition": "definition",
                    "term": "term",
                }
            ],
        )
        assert_matches_type(BusinessGlossaryCreateResponse, business_glossary, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Asktable) -> None:
        response = client.business_glossary.with_raw_response.create(
            body=[
                {
                    "definition": "definition",
                    "term": "term",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        business_glossary = response.parse()
        assert_matches_type(BusinessGlossaryCreateResponse, business_glossary, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Asktable) -> None:
        with client.business_glossary.with_streaming_response.create(
            body=[
                {
                    "definition": "definition",
                    "term": "term",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            business_glossary = response.parse()
            assert_matches_type(BusinessGlossaryCreateResponse, business_glossary, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Asktable) -> None:
        business_glossary = client.business_glossary.retrieve(
            "entry_id",
        )
        assert_matches_type(EntryWithDefinition, business_glossary, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Asktable) -> None:
        response = client.business_glossary.with_raw_response.retrieve(
            "entry_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        business_glossary = response.parse()
        assert_matches_type(EntryWithDefinition, business_glossary, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Asktable) -> None:
        with client.business_glossary.with_streaming_response.retrieve(
            "entry_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            business_glossary = response.parse()
            assert_matches_type(EntryWithDefinition, business_glossary, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Asktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entry_id` but received ''"):
            client.business_glossary.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Asktable) -> None:
        business_glossary = client.business_glossary.update(
            entry_id="entry_id",
        )
        assert_matches_type(Entry, business_glossary, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Asktable) -> None:
        business_glossary = client.business_glossary.update(
            entry_id="entry_id",
            aliases=["string"],
            definition="definition",
            payload={},
            term="term",
        )
        assert_matches_type(Entry, business_glossary, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Asktable) -> None:
        response = client.business_glossary.with_raw_response.update(
            entry_id="entry_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        business_glossary = response.parse()
        assert_matches_type(Entry, business_glossary, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Asktable) -> None:
        with client.business_glossary.with_streaming_response.update(
            entry_id="entry_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            business_glossary = response.parse()
            assert_matches_type(Entry, business_glossary, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Asktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entry_id` but received ''"):
            client.business_glossary.with_raw_response.update(
                entry_id="",
            )

    @parametrize
    def test_method_list(self, client: Asktable) -> None:
        business_glossary = client.business_glossary.list()
        assert_matches_type(SyncPage[EntryWithDefinition], business_glossary, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Asktable) -> None:
        business_glossary = client.business_glossary.list(
            page=1,
            size=1,
            term="term",
        )
        assert_matches_type(SyncPage[EntryWithDefinition], business_glossary, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Asktable) -> None:
        response = client.business_glossary.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        business_glossary = response.parse()
        assert_matches_type(SyncPage[EntryWithDefinition], business_glossary, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Asktable) -> None:
        with client.business_glossary.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            business_glossary = response.parse()
            assert_matches_type(SyncPage[EntryWithDefinition], business_glossary, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Asktable) -> None:
        business_glossary = client.business_glossary.delete(
            "entry_id",
        )
        assert_matches_type(object, business_glossary, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Asktable) -> None:
        response = client.business_glossary.with_raw_response.delete(
            "entry_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        business_glossary = response.parse()
        assert_matches_type(object, business_glossary, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Asktable) -> None:
        with client.business_glossary.with_streaming_response.delete(
            "entry_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            business_glossary = response.parse()
            assert_matches_type(object, business_glossary, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Asktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entry_id` but received ''"):
            client.business_glossary.with_raw_response.delete(
                "",
            )


class TestAsyncBusinessGlossary:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncAsktable) -> None:
        business_glossary = await async_client.business_glossary.create(
            body=[
                {
                    "definition": "definition",
                    "term": "term",
                }
            ],
        )
        assert_matches_type(BusinessGlossaryCreateResponse, business_glossary, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncAsktable) -> None:
        response = await async_client.business_glossary.with_raw_response.create(
            body=[
                {
                    "definition": "definition",
                    "term": "term",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        business_glossary = await response.parse()
        assert_matches_type(BusinessGlossaryCreateResponse, business_glossary, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncAsktable) -> None:
        async with async_client.business_glossary.with_streaming_response.create(
            body=[
                {
                    "definition": "definition",
                    "term": "term",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            business_glossary = await response.parse()
            assert_matches_type(BusinessGlossaryCreateResponse, business_glossary, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncAsktable) -> None:
        business_glossary = await async_client.business_glossary.retrieve(
            "entry_id",
        )
        assert_matches_type(EntryWithDefinition, business_glossary, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncAsktable) -> None:
        response = await async_client.business_glossary.with_raw_response.retrieve(
            "entry_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        business_glossary = await response.parse()
        assert_matches_type(EntryWithDefinition, business_glossary, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncAsktable) -> None:
        async with async_client.business_glossary.with_streaming_response.retrieve(
            "entry_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            business_glossary = await response.parse()
            assert_matches_type(EntryWithDefinition, business_glossary, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncAsktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entry_id` but received ''"):
            await async_client.business_glossary.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncAsktable) -> None:
        business_glossary = await async_client.business_glossary.update(
            entry_id="entry_id",
        )
        assert_matches_type(Entry, business_glossary, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncAsktable) -> None:
        business_glossary = await async_client.business_glossary.update(
            entry_id="entry_id",
            aliases=["string"],
            definition="definition",
            payload={},
            term="term",
        )
        assert_matches_type(Entry, business_glossary, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncAsktable) -> None:
        response = await async_client.business_glossary.with_raw_response.update(
            entry_id="entry_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        business_glossary = await response.parse()
        assert_matches_type(Entry, business_glossary, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncAsktable) -> None:
        async with async_client.business_glossary.with_streaming_response.update(
            entry_id="entry_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            business_glossary = await response.parse()
            assert_matches_type(Entry, business_glossary, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncAsktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entry_id` but received ''"):
            await async_client.business_glossary.with_raw_response.update(
                entry_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncAsktable) -> None:
        business_glossary = await async_client.business_glossary.list()
        assert_matches_type(AsyncPage[EntryWithDefinition], business_glossary, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncAsktable) -> None:
        business_glossary = await async_client.business_glossary.list(
            page=1,
            size=1,
            term="term",
        )
        assert_matches_type(AsyncPage[EntryWithDefinition], business_glossary, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncAsktable) -> None:
        response = await async_client.business_glossary.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        business_glossary = await response.parse()
        assert_matches_type(AsyncPage[EntryWithDefinition], business_glossary, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncAsktable) -> None:
        async with async_client.business_glossary.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            business_glossary = await response.parse()
            assert_matches_type(AsyncPage[EntryWithDefinition], business_glossary, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncAsktable) -> None:
        business_glossary = await async_client.business_glossary.delete(
            "entry_id",
        )
        assert_matches_type(object, business_glossary, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncAsktable) -> None:
        response = await async_client.business_glossary.with_raw_response.delete(
            "entry_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        business_glossary = await response.parse()
        assert_matches_type(object, business_glossary, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncAsktable) -> None:
        async with async_client.business_glossary.with_streaming_response.delete(
            "entry_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            business_glossary = await response.parse()
            assert_matches_type(object, business_glossary, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncAsktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entry_id` but received ''"):
            await async_client.business_glossary.with_raw_response.delete(
                "",
            )
