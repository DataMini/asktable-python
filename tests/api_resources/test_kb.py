# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from asktable import Asktable, AsyncAsktable
from tests.utils import assert_matches_type
from asktable.types import Document, PageDocument, KBCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestKB:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Asktable) -> None:
        kb = client.kb.create(
            body=[
                {
                    "content": "content",
                    "name": "name",
                },
                {
                    "content": "content",
                    "name": "name",
                },
                {
                    "content": "content",
                    "name": "name",
                },
            ],
        )
        assert_matches_type(KBCreateResponse, kb, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Asktable) -> None:
        response = client.kb.with_raw_response.create(
            body=[
                {
                    "content": "content",
                    "name": "name",
                },
                {
                    "content": "content",
                    "name": "name",
                },
                {
                    "content": "content",
                    "name": "name",
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        kb = response.parse()
        assert_matches_type(KBCreateResponse, kb, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Asktable) -> None:
        with client.kb.with_streaming_response.create(
            body=[
                {
                    "content": "content",
                    "name": "name",
                },
                {
                    "content": "content",
                    "name": "name",
                },
                {
                    "content": "content",
                    "name": "name",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            kb = response.parse()
            assert_matches_type(KBCreateResponse, kb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Asktable) -> None:
        kb = client.kb.retrieve(
            "doc_id",
        )
        assert_matches_type(Document, kb, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Asktable) -> None:
        response = client.kb.with_raw_response.retrieve(
            "doc_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        kb = response.parse()
        assert_matches_type(Document, kb, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Asktable) -> None:
        with client.kb.with_streaming_response.retrieve(
            "doc_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            kb = response.parse()
            assert_matches_type(Document, kb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Asktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `doc_id` but received ''"):
            client.kb.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Asktable) -> None:
        kb = client.kb.list()
        assert_matches_type(PageDocument, kb, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Asktable) -> None:
        kb = client.kb.list(
            name="name",
            page=1,
            size=1,
        )
        assert_matches_type(PageDocument, kb, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Asktable) -> None:
        response = client.kb.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        kb = response.parse()
        assert_matches_type(PageDocument, kb, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Asktable) -> None:
        with client.kb.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            kb = response.parse()
            assert_matches_type(PageDocument, kb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Asktable) -> None:
        kb = client.kb.delete(
            "doc_id",
        )
        assert_matches_type(object, kb, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Asktable) -> None:
        response = client.kb.with_raw_response.delete(
            "doc_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        kb = response.parse()
        assert_matches_type(object, kb, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Asktable) -> None:
        with client.kb.with_streaming_response.delete(
            "doc_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            kb = response.parse()
            assert_matches_type(object, kb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Asktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `doc_id` but received ''"):
            client.kb.with_raw_response.delete(
                "",
            )


class TestAsyncKB:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncAsktable) -> None:
        kb = await async_client.kb.create(
            body=[
                {
                    "content": "content",
                    "name": "name",
                },
                {
                    "content": "content",
                    "name": "name",
                },
                {
                    "content": "content",
                    "name": "name",
                },
            ],
        )
        assert_matches_type(KBCreateResponse, kb, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncAsktable) -> None:
        response = await async_client.kb.with_raw_response.create(
            body=[
                {
                    "content": "content",
                    "name": "name",
                },
                {
                    "content": "content",
                    "name": "name",
                },
                {
                    "content": "content",
                    "name": "name",
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        kb = await response.parse()
        assert_matches_type(KBCreateResponse, kb, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncAsktable) -> None:
        async with async_client.kb.with_streaming_response.create(
            body=[
                {
                    "content": "content",
                    "name": "name",
                },
                {
                    "content": "content",
                    "name": "name",
                },
                {
                    "content": "content",
                    "name": "name",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            kb = await response.parse()
            assert_matches_type(KBCreateResponse, kb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncAsktable) -> None:
        kb = await async_client.kb.retrieve(
            "doc_id",
        )
        assert_matches_type(Document, kb, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncAsktable) -> None:
        response = await async_client.kb.with_raw_response.retrieve(
            "doc_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        kb = await response.parse()
        assert_matches_type(Document, kb, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncAsktable) -> None:
        async with async_client.kb.with_streaming_response.retrieve(
            "doc_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            kb = await response.parse()
            assert_matches_type(Document, kb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncAsktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `doc_id` but received ''"):
            await async_client.kb.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncAsktable) -> None:
        kb = await async_client.kb.list()
        assert_matches_type(PageDocument, kb, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncAsktable) -> None:
        kb = await async_client.kb.list(
            name="name",
            page=1,
            size=1,
        )
        assert_matches_type(PageDocument, kb, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncAsktable) -> None:
        response = await async_client.kb.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        kb = await response.parse()
        assert_matches_type(PageDocument, kb, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncAsktable) -> None:
        async with async_client.kb.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            kb = await response.parse()
            assert_matches_type(PageDocument, kb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncAsktable) -> None:
        kb = await async_client.kb.delete(
            "doc_id",
        )
        assert_matches_type(object, kb, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncAsktable) -> None:
        response = await async_client.kb.with_raw_response.delete(
            "doc_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        kb = await response.parse()
        assert_matches_type(object, kb, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncAsktable) -> None:
        async with async_client.kb.with_streaming_response.delete(
            "doc_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            kb = await response.parse()
            assert_matches_type(object, kb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncAsktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `doc_id` but received ''"):
            await async_client.kb.with_raw_response.delete(
                "",
            )
