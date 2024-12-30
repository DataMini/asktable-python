# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from asktable import Asktable, AsyncAsktable
from tests.utils import assert_matches_type
from asktable.types import ProjectListModelGroupsResponse
from asktable.types.sys import Project

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProject:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Asktable) -> None:
        project = client.project.retrieve()
        assert_matches_type(Project, project, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Asktable) -> None:
        response = client.project.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert_matches_type(Project, project, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Asktable) -> None:
        with client.project.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert_matches_type(Project, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Asktable) -> None:
        project = client.project.update()
        assert_matches_type(Project, project, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Asktable) -> None:
        project = client.project.update(
            llm_model_group="llm_model_group",
            name="name",
        )
        assert_matches_type(Project, project, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Asktable) -> None:
        response = client.project.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert_matches_type(Project, project, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Asktable) -> None:
        with client.project.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert_matches_type(Project, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list_model_groups(self, client: Asktable) -> None:
        project = client.project.list_model_groups()
        assert_matches_type(ProjectListModelGroupsResponse, project, path=["response"])

    @parametrize
    def test_raw_response_list_model_groups(self, client: Asktable) -> None:
        response = client.project.with_raw_response.list_model_groups()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert_matches_type(ProjectListModelGroupsResponse, project, path=["response"])

    @parametrize
    def test_streaming_response_list_model_groups(self, client: Asktable) -> None:
        with client.project.with_streaming_response.list_model_groups() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert_matches_type(ProjectListModelGroupsResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncProject:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncAsktable) -> None:
        project = await async_client.project.retrieve()
        assert_matches_type(Project, project, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncAsktable) -> None:
        response = await async_client.project.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert_matches_type(Project, project, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncAsktable) -> None:
        async with async_client.project.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert_matches_type(Project, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncAsktable) -> None:
        project = await async_client.project.update()
        assert_matches_type(Project, project, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncAsktable) -> None:
        project = await async_client.project.update(
            llm_model_group="llm_model_group",
            name="name",
        )
        assert_matches_type(Project, project, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncAsktable) -> None:
        response = await async_client.project.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert_matches_type(Project, project, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncAsktable) -> None:
        async with async_client.project.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert_matches_type(Project, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list_model_groups(self, async_client: AsyncAsktable) -> None:
        project = await async_client.project.list_model_groups()
        assert_matches_type(ProjectListModelGroupsResponse, project, path=["response"])

    @parametrize
    async def test_raw_response_list_model_groups(self, async_client: AsyncAsktable) -> None:
        response = await async_client.project.with_raw_response.list_model_groups()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert_matches_type(ProjectListModelGroupsResponse, project, path=["response"])

    @parametrize
    async def test_streaming_response_list_model_groups(self, async_client: AsyncAsktable) -> None:
        async with async_client.project.with_streaming_response.list_model_groups() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert_matches_type(ProjectListModelGroupsResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True
