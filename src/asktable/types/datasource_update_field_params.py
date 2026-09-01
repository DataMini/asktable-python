# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["DatasourceUpdateFieldParams"]


class DatasourceUpdateFieldParams(TypedDict, total=False):
    field_name: Required[str]

    schema_name: Required[str]

    table_name: Required[str]

    identifiable_type: Optional[
        Literal["plain", "person_name", "email", "ssn", "id", "phone", "address", "company", "bank_card"]
    ]
    """identifiable type"""

    semantic_type: Optional[
        Literal[
            "PK",
            "FK",
            "Quantity",
            "Share",
            "Percentage",
            "Currency",
            "Income",
            "Discount",
            "Price",
            "GrossMargin",
            "Cost",
            "Score",
            "Duration",
            "Latitude",
            "Longitude",
            "City",
            "State",
            "Country",
            "ZipCode",
            "Email",
            "URL",
            "ImageURL",
            "AvatarURL",
            "Category",
            "Enum",
            "Name",
            "Title",
            "Description",
            "Comment",
            "SerializedJSON",
            "IPAddress",
            "CreationTimestamp",
            "CreationTime",
            "CreationDate",
            "JoinTimestamp",
            "JoinTime",
            "JoinDate",
            "CancelationTimestamp",
            "CancelationTime",
            "CancelationDate",
            "DeletionTimestamp",
            "DeletionTime",
            "DeletionDate",
            "UpdatedTimestamp",
            "UpdatedTime",
            "UpdatedDate",
            "Birthdate",
            "Source",
            "Author",
            "Owner",
            "Company",
            "Product",
            "Subscription",
        ]
    ]
    """字段语义类型，协议照抄 Metabase（值 = :type/ 前缀去除后的名字）。

    PK/FK 是关系类型，与语义共用一列（Metabase 同款）：来自同步元数据，非推断产物
    ，classifier 一律跳过。其余值由 classifier 推断或人工设置。
    """

    visibility: Optional[bool]
    """field visibility"""
