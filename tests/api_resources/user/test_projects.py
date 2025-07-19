# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from asktable import Asktable, AsyncAsktable
from tests.utils import assert_matches_type
from asktable.types.sys import Project
from asktable.types.user import ProjectRetrieveModelGroupsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProjects:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve_model_groups(self, client: Asktable) -> None:
        project = client.user.projects.retrieve_model_groups()
        assert_matches_type(ProjectRetrieveModelGroupsResponse, project, path=["response"])

    @parametrize
    def test_raw_response_retrieve_model_groups(self, client: Asktable) -> None:
        response = client.user.projects.with_raw_response.retrieve_model_groups()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert_matches_type(ProjectRetrieveModelGroupsResponse, project, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_model_groups(self, client: Asktable) -> None:
        with client.user.projects.with_streaming_response.retrieve_model_groups() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert_matches_type(ProjectRetrieveModelGroupsResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve_my_project(self, client: Asktable) -> None:
        project = client.user.projects.retrieve_my_project()
        assert_matches_type(Project, project, path=["response"])

    @parametrize
    def test_raw_response_retrieve_my_project(self, client: Asktable) -> None:
        response = client.user.projects.with_raw_response.retrieve_my_project()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert_matches_type(Project, project, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_my_project(self, client: Asktable) -> None:
        with client.user.projects.with_streaming_response.retrieve_my_project() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert_matches_type(Project, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update_my_project(self, client: Asktable) -> None:
        project = client.user.projects.update_my_project()
        assert_matches_type(Project, project, path=["response"])

    @parametrize
    def test_method_update_my_project_with_all_params(self, client: Asktable) -> None:
        project = client.user.projects.update_my_project(
            llm_model_group="llm_model_group",
            name="name",
        )
        assert_matches_type(Project, project, path=["response"])

    @parametrize
    def test_raw_response_update_my_project(self, client: Asktable) -> None:
        response = client.user.projects.with_raw_response.update_my_project()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert_matches_type(Project, project, path=["response"])

    @parametrize
    def test_streaming_response_update_my_project(self, client: Asktable) -> None:
        with client.user.projects.with_streaming_response.update_my_project() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert_matches_type(Project, project, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncProjects:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve_model_groups(self, async_client: AsyncAsktable) -> None:
        project = await async_client.user.projects.retrieve_model_groups()
        assert_matches_type(ProjectRetrieveModelGroupsResponse, project, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_model_groups(self, async_client: AsyncAsktable) -> None:
        response = await async_client.user.projects.with_raw_response.retrieve_model_groups()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert_matches_type(ProjectRetrieveModelGroupsResponse, project, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_model_groups(self, async_client: AsyncAsktable) -> None:
        async with async_client.user.projects.with_streaming_response.retrieve_model_groups() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert_matches_type(ProjectRetrieveModelGroupsResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve_my_project(self, async_client: AsyncAsktable) -> None:
        project = await async_client.user.projects.retrieve_my_project()
        assert_matches_type(Project, project, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_my_project(self, async_client: AsyncAsktable) -> None:
        response = await async_client.user.projects.with_raw_response.retrieve_my_project()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert_matches_type(Project, project, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_my_project(self, async_client: AsyncAsktable) -> None:
        async with async_client.user.projects.with_streaming_response.retrieve_my_project() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert_matches_type(Project, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update_my_project(self, async_client: AsyncAsktable) -> None:
        project = await async_client.user.projects.update_my_project()
        assert_matches_type(Project, project, path=["response"])

    @parametrize
    async def test_method_update_my_project_with_all_params(self, async_client: AsyncAsktable) -> None:
        project = await async_client.user.projects.update_my_project(
            llm_model_group="llm_model_group",
            name="name",
        )
        assert_matches_type(Project, project, path=["response"])

    @parametrize
    async def test_raw_response_update_my_project(self, async_client: AsyncAsktable) -> None:
        response = await async_client.user.projects.with_raw_response.update_my_project()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert_matches_type(Project, project, path=["response"])

    @parametrize
    async def test_streaming_response_update_my_project(self, async_client: AsyncAsktable) -> None:
        async with async_client.user.projects.with_streaming_response.update_my_project() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert_matches_type(Project, project, path=["response"])

        assert cast(Any, response.is_closed) is True
