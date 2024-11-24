# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from asktable import Asktable, AsyncAsktable
from tests.utils import assert_matches_type
from asktable._utils import parse_datetime
from asktable.types.extapis import ExtapiRoute, RouteListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRoutes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Asktable) -> None:
        route = client.extapis.routes.create(
            path_extapi_id="extapi_id",
            id="id",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            body_extapi_id="extapi_id",
            method="GET",
            name="name",
            path="/resource",
            project_id="project_id",
        )
        assert_matches_type(ExtapiRoute, route, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Asktable) -> None:
        route = client.extapis.routes.create(
            path_extapi_id="extapi_id",
            id="id",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            body_extapi_id="extapi_id",
            method="GET",
            name="name",
            path="/resource",
            project_id="project_id",
            body_params_desc="body_params_desc",
            path_params_desc="path_params_desc",
            query_params_desc="query_params_desc",
            updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ExtapiRoute, route, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Asktable) -> None:
        response = client.extapis.routes.with_raw_response.create(
            path_extapi_id="extapi_id",
            id="id",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            body_extapi_id="extapi_id",
            method="GET",
            name="name",
            path="/resource",
            project_id="project_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route = response.parse()
        assert_matches_type(ExtapiRoute, route, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Asktable) -> None:
        with client.extapis.routes.with_streaming_response.create(
            path_extapi_id="extapi_id",
            id="id",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            body_extapi_id="extapi_id",
            method="GET",
            name="name",
            path="/resource",
            project_id="project_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            route = response.parse()
            assert_matches_type(ExtapiRoute, route, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Asktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_extapi_id` but received ''"):
            client.extapis.routes.with_raw_response.create(
                path_extapi_id="",
                id="id",
                created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
                body_extapi_id="",
                method="GET",
                name="name",
                path="/resource",
                project_id="project_id",
            )

    @parametrize
    def test_method_retrieve(self, client: Asktable) -> None:
        route = client.extapis.routes.retrieve(
            route_id="route_id",
            extapi_id="extapi_id",
        )
        assert_matches_type(ExtapiRoute, route, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Asktable) -> None:
        response = client.extapis.routes.with_raw_response.retrieve(
            route_id="route_id",
            extapi_id="extapi_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route = response.parse()
        assert_matches_type(ExtapiRoute, route, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Asktable) -> None:
        with client.extapis.routes.with_streaming_response.retrieve(
            route_id="route_id",
            extapi_id="extapi_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            route = response.parse()
            assert_matches_type(ExtapiRoute, route, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Asktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `extapi_id` but received ''"):
            client.extapis.routes.with_raw_response.retrieve(
                route_id="route_id",
                extapi_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `route_id` but received ''"):
            client.extapis.routes.with_raw_response.retrieve(
                route_id="",
                extapi_id="extapi_id",
            )

    @parametrize
    def test_method_update(self, client: Asktable) -> None:
        route = client.extapis.routes.update(
            route_id="route_id",
            extapi_id="extapi_id",
        )
        assert_matches_type(ExtapiRoute, route, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Asktable) -> None:
        route = client.extapis.routes.update(
            route_id="route_id",
            extapi_id="extapi_id",
            body_params_desc="body_params_desc",
            method="GET",
            name="name",
            path="/resource",
            path_params_desc="path_params_desc",
            query_params_desc="query_params_desc",
        )
        assert_matches_type(ExtapiRoute, route, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Asktable) -> None:
        response = client.extapis.routes.with_raw_response.update(
            route_id="route_id",
            extapi_id="extapi_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route = response.parse()
        assert_matches_type(ExtapiRoute, route, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Asktable) -> None:
        with client.extapis.routes.with_streaming_response.update(
            route_id="route_id",
            extapi_id="extapi_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            route = response.parse()
            assert_matches_type(ExtapiRoute, route, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Asktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `extapi_id` but received ''"):
            client.extapis.routes.with_raw_response.update(
                route_id="route_id",
                extapi_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `route_id` but received ''"):
            client.extapis.routes.with_raw_response.update(
                route_id="",
                extapi_id="extapi_id",
            )

    @parametrize
    def test_method_list(self, client: Asktable) -> None:
        route = client.extapis.routes.list(
            "extapi_id",
        )
        assert_matches_type(RouteListResponse, route, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Asktable) -> None:
        response = client.extapis.routes.with_raw_response.list(
            "extapi_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route = response.parse()
        assert_matches_type(RouteListResponse, route, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Asktable) -> None:
        with client.extapis.routes.with_streaming_response.list(
            "extapi_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            route = response.parse()
            assert_matches_type(RouteListResponse, route, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Asktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `extapi_id` but received ''"):
            client.extapis.routes.with_raw_response.list(
                "",
            )

    @parametrize
    def test_method_delete(self, client: Asktable) -> None:
        route = client.extapis.routes.delete(
            route_id="route_id",
            extapi_id="extapi_id",
        )
        assert route is None

    @parametrize
    def test_raw_response_delete(self, client: Asktable) -> None:
        response = client.extapis.routes.with_raw_response.delete(
            route_id="route_id",
            extapi_id="extapi_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route = response.parse()
        assert route is None

    @parametrize
    def test_streaming_response_delete(self, client: Asktable) -> None:
        with client.extapis.routes.with_streaming_response.delete(
            route_id="route_id",
            extapi_id="extapi_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            route = response.parse()
            assert route is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Asktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `extapi_id` but received ''"):
            client.extapis.routes.with_raw_response.delete(
                route_id="route_id",
                extapi_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `route_id` but received ''"):
            client.extapis.routes.with_raw_response.delete(
                route_id="",
                extapi_id="extapi_id",
            )


class TestAsyncRoutes:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncAsktable) -> None:
        route = await async_client.extapis.routes.create(
            path_extapi_id="extapi_id",
            id="id",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            body_extapi_id="extapi_id",
            method="GET",
            name="name",
            path="/resource",
            project_id="project_id",
        )
        assert_matches_type(ExtapiRoute, route, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncAsktable) -> None:
        route = await async_client.extapis.routes.create(
            path_extapi_id="extapi_id",
            id="id",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            body_extapi_id="extapi_id",
            method="GET",
            name="name",
            path="/resource",
            project_id="project_id",
            body_params_desc="body_params_desc",
            path_params_desc="path_params_desc",
            query_params_desc="query_params_desc",
            updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ExtapiRoute, route, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncAsktable) -> None:
        response = await async_client.extapis.routes.with_raw_response.create(
            path_extapi_id="extapi_id",
            id="id",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            body_extapi_id="extapi_id",
            method="GET",
            name="name",
            path="/resource",
            project_id="project_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route = await response.parse()
        assert_matches_type(ExtapiRoute, route, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncAsktable) -> None:
        async with async_client.extapis.routes.with_streaming_response.create(
            path_extapi_id="extapi_id",
            id="id",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            body_extapi_id="extapi_id",
            method="GET",
            name="name",
            path="/resource",
            project_id="project_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            route = await response.parse()
            assert_matches_type(ExtapiRoute, route, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncAsktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_extapi_id` but received ''"):
            await async_client.extapis.routes.with_raw_response.create(
                path_extapi_id="",
                id="id",
                created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
                body_extapi_id="",
                method="GET",
                name="name",
                path="/resource",
                project_id="project_id",
            )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncAsktable) -> None:
        route = await async_client.extapis.routes.retrieve(
            route_id="route_id",
            extapi_id="extapi_id",
        )
        assert_matches_type(ExtapiRoute, route, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncAsktable) -> None:
        response = await async_client.extapis.routes.with_raw_response.retrieve(
            route_id="route_id",
            extapi_id="extapi_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route = await response.parse()
        assert_matches_type(ExtapiRoute, route, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncAsktable) -> None:
        async with async_client.extapis.routes.with_streaming_response.retrieve(
            route_id="route_id",
            extapi_id="extapi_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            route = await response.parse()
            assert_matches_type(ExtapiRoute, route, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncAsktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `extapi_id` but received ''"):
            await async_client.extapis.routes.with_raw_response.retrieve(
                route_id="route_id",
                extapi_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `route_id` but received ''"):
            await async_client.extapis.routes.with_raw_response.retrieve(
                route_id="",
                extapi_id="extapi_id",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncAsktable) -> None:
        route = await async_client.extapis.routes.update(
            route_id="route_id",
            extapi_id="extapi_id",
        )
        assert_matches_type(ExtapiRoute, route, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncAsktable) -> None:
        route = await async_client.extapis.routes.update(
            route_id="route_id",
            extapi_id="extapi_id",
            body_params_desc="body_params_desc",
            method="GET",
            name="name",
            path="/resource",
            path_params_desc="path_params_desc",
            query_params_desc="query_params_desc",
        )
        assert_matches_type(ExtapiRoute, route, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncAsktable) -> None:
        response = await async_client.extapis.routes.with_raw_response.update(
            route_id="route_id",
            extapi_id="extapi_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route = await response.parse()
        assert_matches_type(ExtapiRoute, route, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncAsktable) -> None:
        async with async_client.extapis.routes.with_streaming_response.update(
            route_id="route_id",
            extapi_id="extapi_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            route = await response.parse()
            assert_matches_type(ExtapiRoute, route, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncAsktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `extapi_id` but received ''"):
            await async_client.extapis.routes.with_raw_response.update(
                route_id="route_id",
                extapi_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `route_id` but received ''"):
            await async_client.extapis.routes.with_raw_response.update(
                route_id="",
                extapi_id="extapi_id",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncAsktable) -> None:
        route = await async_client.extapis.routes.list(
            "extapi_id",
        )
        assert_matches_type(RouteListResponse, route, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncAsktable) -> None:
        response = await async_client.extapis.routes.with_raw_response.list(
            "extapi_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route = await response.parse()
        assert_matches_type(RouteListResponse, route, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncAsktable) -> None:
        async with async_client.extapis.routes.with_streaming_response.list(
            "extapi_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            route = await response.parse()
            assert_matches_type(RouteListResponse, route, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncAsktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `extapi_id` but received ''"):
            await async_client.extapis.routes.with_raw_response.list(
                "",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncAsktable) -> None:
        route = await async_client.extapis.routes.delete(
            route_id="route_id",
            extapi_id="extapi_id",
        )
        assert route is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncAsktable) -> None:
        response = await async_client.extapis.routes.with_raw_response.delete(
            route_id="route_id",
            extapi_id="extapi_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route = await response.parse()
        assert route is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncAsktable) -> None:
        async with async_client.extapis.routes.with_streaming_response.delete(
            route_id="route_id",
            extapi_id="extapi_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            route = await response.parse()
            assert route is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncAsktable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `extapi_id` but received ''"):
            await async_client.extapis.routes.with_raw_response.delete(
                route_id="route_id",
                extapi_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `route_id` but received ''"):
            await async_client.extapis.routes.with_raw_response.delete(
                route_id="",
                extapi_id="extapi_id",
            )
