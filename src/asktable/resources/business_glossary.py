# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional

import httpx

from ..types import (
    business_glossary_list_params,
    business_glossary_create_params,
    business_glossary_update_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncPage, AsyncPage
from ..types.entry import Entry
from .._base_client import AsyncPaginator, make_request_options
from ..types.entry_with_definition import EntryWithDefinition
from ..types.business_glossary_create_response import BusinessGlossaryCreateResponse

__all__ = ["BusinessGlossaryResource", "AsyncBusinessGlossaryResource"]


class BusinessGlossaryResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BusinessGlossaryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DataMini/asktable-python#accessing-raw-response-data-eg-headers
        """
        return BusinessGlossaryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BusinessGlossaryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DataMini/asktable-python#with_streaming_response
        """
        return BusinessGlossaryResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        body: Iterable[business_glossary_create_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BusinessGlossaryCreateResponse:
        """
        创建业务术语

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/business-glossary",
            body=maybe_transform(body, Iterable[business_glossary_create_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BusinessGlossaryCreateResponse,
        )

    def retrieve(
        self,
        entry_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EntryWithDefinition:
        """
        获取某个业务术语

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not entry_id:
            raise ValueError(f"Expected a non-empty value for `entry_id` but received {entry_id!r}")
        return self._get(
            f"/business-glossary/{entry_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EntryWithDefinition,
        )

    def update(
        self,
        entry_id: str,
        *,
        aliases: Optional[List[str]] | NotGiven = NOT_GIVEN,
        definition: Optional[str] | NotGiven = NOT_GIVEN,
        payload: Optional[object] | NotGiven = NOT_GIVEN,
        term: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Entry:
        """
        更新业务术语

        Args:
          aliases: 业务术语同义词

          definition: 业务术语定义

          payload: 业务术语元数据

          term: 业务术语

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not entry_id:
            raise ValueError(f"Expected a non-empty value for `entry_id` but received {entry_id!r}")
        return self._patch(
            f"/business-glossary/{entry_id}",
            body=maybe_transform(
                {
                    "aliases": aliases,
                    "definition": definition,
                    "payload": payload,
                    "term": term,
                },
                business_glossary_update_params.BusinessGlossaryUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Entry,
        )

    def list(
        self,
        *,
        page: int | NotGiven = NOT_GIVEN,
        size: int | NotGiven = NOT_GIVEN,
        term: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[EntryWithDefinition]:
        """
        查询所有业务术语

        Args:
          page: Page number

          size: Page size

          term: 术语名称

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/business-glossary",
            page=SyncPage[EntryWithDefinition],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "size": size,
                        "term": term,
                    },
                    business_glossary_list_params.BusinessGlossaryListParams,
                ),
            ),
            model=EntryWithDefinition,
        )

    def delete(
        self,
        entry_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        删除某个业务术语

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not entry_id:
            raise ValueError(f"Expected a non-empty value for `entry_id` but received {entry_id!r}")
        return self._delete(
            f"/business-glossary/{entry_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncBusinessGlossaryResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBusinessGlossaryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DataMini/asktable-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBusinessGlossaryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBusinessGlossaryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DataMini/asktable-python#with_streaming_response
        """
        return AsyncBusinessGlossaryResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        body: Iterable[business_glossary_create_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BusinessGlossaryCreateResponse:
        """
        创建业务术语

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/business-glossary",
            body=await async_maybe_transform(body, Iterable[business_glossary_create_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BusinessGlossaryCreateResponse,
        )

    async def retrieve(
        self,
        entry_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EntryWithDefinition:
        """
        获取某个业务术语

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not entry_id:
            raise ValueError(f"Expected a non-empty value for `entry_id` but received {entry_id!r}")
        return await self._get(
            f"/business-glossary/{entry_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EntryWithDefinition,
        )

    async def update(
        self,
        entry_id: str,
        *,
        aliases: Optional[List[str]] | NotGiven = NOT_GIVEN,
        definition: Optional[str] | NotGiven = NOT_GIVEN,
        payload: Optional[object] | NotGiven = NOT_GIVEN,
        term: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Entry:
        """
        更新业务术语

        Args:
          aliases: 业务术语同义词

          definition: 业务术语定义

          payload: 业务术语元数据

          term: 业务术语

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not entry_id:
            raise ValueError(f"Expected a non-empty value for `entry_id` but received {entry_id!r}")
        return await self._patch(
            f"/business-glossary/{entry_id}",
            body=await async_maybe_transform(
                {
                    "aliases": aliases,
                    "definition": definition,
                    "payload": payload,
                    "term": term,
                },
                business_glossary_update_params.BusinessGlossaryUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Entry,
        )

    def list(
        self,
        *,
        page: int | NotGiven = NOT_GIVEN,
        size: int | NotGiven = NOT_GIVEN,
        term: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[EntryWithDefinition, AsyncPage[EntryWithDefinition]]:
        """
        查询所有业务术语

        Args:
          page: Page number

          size: Page size

          term: 术语名称

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/business-glossary",
            page=AsyncPage[EntryWithDefinition],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "size": size,
                        "term": term,
                    },
                    business_glossary_list_params.BusinessGlossaryListParams,
                ),
            ),
            model=EntryWithDefinition,
        )

    async def delete(
        self,
        entry_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        删除某个业务术语

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not entry_id:
            raise ValueError(f"Expected a non-empty value for `entry_id` but received {entry_id!r}")
        return await self._delete(
            f"/business-glossary/{entry_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class BusinessGlossaryResourceWithRawResponse:
    def __init__(self, business_glossary: BusinessGlossaryResource) -> None:
        self._business_glossary = business_glossary

        self.create = to_raw_response_wrapper(
            business_glossary.create,
        )
        self.retrieve = to_raw_response_wrapper(
            business_glossary.retrieve,
        )
        self.update = to_raw_response_wrapper(
            business_glossary.update,
        )
        self.list = to_raw_response_wrapper(
            business_glossary.list,
        )
        self.delete = to_raw_response_wrapper(
            business_glossary.delete,
        )


class AsyncBusinessGlossaryResourceWithRawResponse:
    def __init__(self, business_glossary: AsyncBusinessGlossaryResource) -> None:
        self._business_glossary = business_glossary

        self.create = async_to_raw_response_wrapper(
            business_glossary.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            business_glossary.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            business_glossary.update,
        )
        self.list = async_to_raw_response_wrapper(
            business_glossary.list,
        )
        self.delete = async_to_raw_response_wrapper(
            business_glossary.delete,
        )


class BusinessGlossaryResourceWithStreamingResponse:
    def __init__(self, business_glossary: BusinessGlossaryResource) -> None:
        self._business_glossary = business_glossary

        self.create = to_streamed_response_wrapper(
            business_glossary.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            business_glossary.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            business_glossary.update,
        )
        self.list = to_streamed_response_wrapper(
            business_glossary.list,
        )
        self.delete = to_streamed_response_wrapper(
            business_glossary.delete,
        )


class AsyncBusinessGlossaryResourceWithStreamingResponse:
    def __init__(self, business_glossary: AsyncBusinessGlossaryResource) -> None:
        self._business_glossary = business_glossary

        self.create = async_to_streamed_response_wrapper(
            business_glossary.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            business_glossary.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            business_glossary.update,
        )
        self.list = async_to_streamed_response_wrapper(
            business_glossary.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            business_glossary.delete,
        )
