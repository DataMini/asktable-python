# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["PolicyUpdateParams", "DatasetConfig", "DatasetConfigRegexPatterns", "DatasetConfigRowsFilter"]


class PolicyUpdateParams(TypedDict, total=False):
    dataset_config: Optional[DatasetConfig]
    """数据集配置"""

    name: Optional[str]
    """名称，小写英文字母，数字和下划线组合，不超过 64 个字符"""

    permission: Optional[Literal["allow", "deny"]]
    """权限"""


class DatasetConfigRegexPatterns(TypedDict, total=False):
    fields_regex_pattern: Optional[str]
    """Field 正则表达式，空值默认全选"""

    schemas_regex_pattern: Optional[str]
    """Schema 正则表达式，空值默认全选"""

    tables_regex_pattern: Optional[str]
    """Table 正则表达式，空值默认全选"""


class DatasetConfigRowsFilter(TypedDict, total=False):
    condition: Required[str]
    """Filter condition string"""

    db_regex: Required[str]
    """Database regex pattern"""

    field_regex: Required[str]
    """Field regex pattern"""

    operator_expression: Required[str]
    """Operator expression"""

    table_regex: Required[str]
    """Table regex pattern"""

    variables: List[str]
    """Jinja2 variables in the condition"""


class DatasetConfig(TypedDict, total=False):
    datasource_ids: Required[List[str]]
    """
    数据源 ID 列表，必填。 - 描述：用于指定策略适用的数据源。可以使用通配符 _ 表示所
    有数据源。 - 示例：["ds_id_1","ds_id_2"]，["_"]。
    """

    regex_patterns: Optional[DatasetConfigRegexPatterns]
    """
    正则表达式。 - 描述：用于匹配指定数据源中 Schema（DB）、Table 和 Field 名称的三
    个正则表达式，即同时满足这三个正则表达式的 DB、Table 和 Field 才被允许访问。 -
    注意：此字段为可选项。如果未提供，则默认包含指定数据源的所有数据。
    """

    rows_filters: Optional[Dict[str, Iterable[DatasetConfigRowsFilter]]]
    """行级别过滤器。

    - 描述：指定行级别的过滤器，满足条件的行才可访问。 用户在查询数据的时候会自动对
      结果集进行过滤，也同时会影响聚合计算（比如求 COUNT、SUM）的结果。
    - 格式：
      - 按数据源组织，每个数据源对应一个过滤条件列表 `filter_condition`
      - 每个 `filter_condition` 是一个字符串，格式为
        `"<schema_name>.<table_name>.<field_name> <expression>"`。
      - 其中 `schema_name`、`table_name`、`field_name` 支持模糊匹配，比如支持
        `"*.*.*uid* = {{ user_id }}"`，来匹配所有包含 `uid` 的字段，且字段值等于
        `user_id` 的行。
    - 如何编写 `expression`：
      - `expression` 中的操作符：
        - 支持常见操作符：=, >, <, >=, <=, <>, !=, IN, NOT IN, LIKE, NOT LIKE, IS
          NULL, IS NOT NULL
      - `expression` 中的变量：
        - 变量使用两个大括号括起来（支持
          [Jinja2](https://docs.jinkan.org/docs/jinja2/) 模版），比如
          {{user_id}}，{{city_id}}，{{merchant_id}}
        - 变量的值需要在扮演角色时传递，全部使用字符串类型，比如
          "123"，"beijing"，"456"
      - `expression` 中的函数：
        - 支持内置函数 NOW() 获取当前时间，比如 "public.user.created_at > NOW() - 1
          YEAR"
      - 数值、字符串、时间等字段的 `expression` 写法：
        - 对于数值型、字符串类型的字段，可以直接填上常量或变量，都不用加引号，比如
          "public.user.age > {{age}}" ，"public.user.name = 张三 "或
          "public.user.name = {{name}} "
        - 对于日期时间型字段
          - 使用单引号括起来的日期时间字符串进行过滤，比如 "public.user.created_at >
            '2023-01-01 00:00:00 +00:00'"
          - 使用变量时，需要使用大括号括起来，比如 "public.user.created_at >
            {{start_date}}"
          - 使用内置函数 NOW() 获取当前时间，比如 "public.user.created_at > NOW() -
            1 YEAR"
    - 限制：
      - 只允许当 permission = allow 时才可以设置该选项
      - 暂不支持跨数据源的字段过滤，即需要对每个数据源单独设置过滤条件，数据源 ID 不
        允许使用通配符 \\**。
      - 暂不支持对字段使用函数计算，比如不支持 "YEAR(public.user.created_at) = 2023"
      - 暂不支持多个过滤条件的组合，，比如不支持 "uid = {{user_id}} AND city_id =
        {{city_id}}"
    """
