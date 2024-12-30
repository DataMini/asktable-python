# Shared Types

```python
from asktable.types import Policy
```

# Sys

## Projects

Types:

```python
from asktable.types.sys import (
    APIKey,
    ModelGroup,
    Project,
    ProjectDeleteResponse,
    ProjectModelGroupsResponse,
)
```

Methods:

- <code title="post /sys/projects">client.sys.projects.<a href="./src/asktable/resources/sys/projects/projects.py">create</a>(\*\*<a href="src/asktable/types/sys/project_create_params.py">params</a>) -> <a href="./src/asktable/types/sys/project.py">Project</a></code>
- <code title="get /sys/projects/{project_id}">client.sys.projects.<a href="./src/asktable/resources/sys/projects/projects.py">retrieve</a>(project_id) -> <a href="./src/asktable/types/sys/project.py">Project</a></code>
- <code title="patch /sys/projects/{project_id}">client.sys.projects.<a href="./src/asktable/resources/sys/projects/projects.py">update</a>(project_id, \*\*<a href="src/asktable/types/sys/project_update_params.py">params</a>) -> <a href="./src/asktable/types/sys/project.py">Project</a></code>
- <code title="get /sys/projects">client.sys.projects.<a href="./src/asktable/resources/sys/projects/projects.py">list</a>(\*\*<a href="src/asktable/types/sys/project_list_params.py">params</a>) -> <a href="./src/asktable/types/sys/project.py">SyncPage[Project]</a></code>
- <code title="delete /sys/projects/{project_id}">client.sys.projects.<a href="./src/asktable/resources/sys/projects/projects.py">delete</a>(project_id) -> <a href="./src/asktable/types/sys/project_delete_response.py">object</a></code>
- <code title="get /sys/projects/model-groups">client.sys.projects.<a href="./src/asktable/resources/sys/projects/projects.py">model_groups</a>() -> <a href="./src/asktable/types/sys/project_model_groups_response.py">ProjectModelGroupsResponse</a></code>

### APIKeys

Types:

```python
from asktable.types.sys.projects import (
    APIKeyCreateResponse,
    APIKeyListResponse,
    APIKeyCreateTokenResponse,
)
```

Methods:

- <code title="post /sys/projects/{project_id}/api-keys">client.sys.projects.api_keys.<a href="./src/asktable/resources/sys/projects/api_keys.py">create</a>(project_id, \*\*<a href="src/asktable/types/sys/projects/api_key_create_params.py">params</a>) -> <a href="./src/asktable/types/sys/projects/api_key_create_response.py">APIKeyCreateResponse</a></code>
- <code title="get /sys/projects/{project_id}/api-keys">client.sys.projects.api_keys.<a href="./src/asktable/resources/sys/projects/api_keys.py">list</a>(project_id) -> <a href="./src/asktable/types/sys/projects/api_key_list_response.py">APIKeyListResponse</a></code>
- <code title="delete /sys/projects/{project_id}/api-keys/{key_id}">client.sys.projects.api_keys.<a href="./src/asktable/resources/sys/projects/api_keys.py">delete</a>(key_id, \*, project_id) -> None</code>
- <code title="post /sys/projects/{project_id}/tokens">client.sys.projects.api_keys.<a href="./src/asktable/resources/sys/projects/api_keys.py">create_token</a>(project_id, \*\*<a href="src/asktable/types/sys/projects/api_key_create_token_params.py">params</a>) -> <a href="./src/asktable/types/sys/projects/api_key_create_token_response.py">object</a></code>

# Securetunnels

Types:

```python
from asktable.types import SecureTunnel, SecuretunnelListLinksResponse
```

Methods:

- <code title="post /securetunnels">client.securetunnels.<a href="./src/asktable/resources/securetunnels.py">create</a>(\*\*<a href="src/asktable/types/securetunnel_create_params.py">params</a>) -> <a href="./src/asktable/types/secure_tunnel.py">SecureTunnel</a></code>
- <code title="get /securetunnels/{securetunnel_id}">client.securetunnels.<a href="./src/asktable/resources/securetunnels.py">retrieve</a>(securetunnel_id) -> <a href="./src/asktable/types/secure_tunnel.py">SecureTunnel</a></code>
- <code title="patch /securetunnels/{securetunnel_id}">client.securetunnels.<a href="./src/asktable/resources/securetunnels.py">update</a>(securetunnel_id, \*\*<a href="src/asktable/types/securetunnel_update_params.py">params</a>) -> <a href="./src/asktable/types/secure_tunnel.py">SecureTunnel</a></code>
- <code title="get /securetunnels">client.securetunnels.<a href="./src/asktable/resources/securetunnels.py">list</a>(\*\*<a href="src/asktable/types/securetunnel_list_params.py">params</a>) -> <a href="./src/asktable/types/secure_tunnel.py">SyncPage[SecureTunnel]</a></code>
- <code title="delete /securetunnels/{securetunnel_id}">client.securetunnels.<a href="./src/asktable/resources/securetunnels.py">delete</a>(securetunnel_id) -> None</code>
- <code title="get /securetunnels/{securetunnel_id}/links">client.securetunnels.<a href="./src/asktable/resources/securetunnels.py">list_links</a>(securetunnel_id, \*\*<a href="src/asktable/types/securetunnel_list_links_params.py">params</a>) -> <a href="./src/asktable/types/securetunnel_list_links_response.py">SyncPage[SecuretunnelListLinksResponse]</a></code>

# Roles

Types:

```python
from asktable.types import (
    Role,
    RoleDeleteResponse,
    RoleGetPolicesResponse,
    RoleGetVariablesResponse,
)
```

Methods:

- <code title="post /roles">client.roles.<a href="./src/asktable/resources/roles.py">create</a>(\*\*<a href="src/asktable/types/role_create_params.py">params</a>) -> <a href="./src/asktable/types/role.py">Role</a></code>
- <code title="get /roles/{role_id}">client.roles.<a href="./src/asktable/resources/roles.py">retrieve</a>(role_id) -> <a href="./src/asktable/types/role.py">Role</a></code>
- <code title="patch /roles/{role_id}">client.roles.<a href="./src/asktable/resources/roles.py">update</a>(role_id, \*\*<a href="src/asktable/types/role_update_params.py">params</a>) -> <a href="./src/asktable/types/role.py">Role</a></code>
- <code title="get /roles">client.roles.<a href="./src/asktable/resources/roles.py">list</a>(\*\*<a href="src/asktable/types/role_list_params.py">params</a>) -> <a href="./src/asktable/types/role.py">SyncPage[Role]</a></code>
- <code title="delete /roles/{role_id}">client.roles.<a href="./src/asktable/resources/roles.py">delete</a>(role_id) -> <a href="./src/asktable/types/role_delete_response.py">object</a></code>
- <code title="get /roles/{role_id}/policies">client.roles.<a href="./src/asktable/resources/roles.py">get_polices</a>(role_id) -> <a href="./src/asktable/types/role_get_polices_response.py">RoleGetPolicesResponse</a></code>
- <code title="get /roles/{role_id}/variables">client.roles.<a href="./src/asktable/resources/roles.py">get_variables</a>(role_id, \*\*<a href="src/asktable/types/role_get_variables_params.py">params</a>) -> <a href="./src/asktable/types/role_get_variables_response.py">object</a></code>

# Policies

Methods:

- <code title="post /policies">client.policies.<a href="./src/asktable/resources/policies.py">create</a>(\*\*<a href="src/asktable/types/policy_create_params.py">params</a>) -> <a href="./src/asktable/types/shared/policy.py">Policy</a></code>
- <code title="get /policies/{policy_id}">client.policies.<a href="./src/asktable/resources/policies.py">retrieve</a>(policy_id) -> <a href="./src/asktable/types/shared/policy.py">Policy</a></code>
- <code title="patch /policies/{policy_id}">client.policies.<a href="./src/asktable/resources/policies.py">update</a>(policy_id, \*\*<a href="src/asktable/types/policy_update_params.py">params</a>) -> <a href="./src/asktable/types/shared/policy.py">Policy</a></code>
- <code title="get /policies">client.policies.<a href="./src/asktable/resources/policies.py">list</a>(\*\*<a href="src/asktable/types/policy_list_params.py">params</a>) -> <a href="./src/asktable/types/shared/policy.py">SyncPage[Policy]</a></code>
- <code title="delete /policies/{policy_id}">client.policies.<a href="./src/asktable/resources/policies.py">delete</a>(policy_id) -> None</code>

# Chats

Types:

```python
from asktable.types import (
    AIMessage,
    Chat,
    ToolMessage,
    UserMessage,
    ChatRetrieveResponse,
    ChatSendMessageResponse,
)
```

Methods:

- <code title="post /chats">client.chats.<a href="./src/asktable/resources/chats/chats.py">create</a>(\*\*<a href="src/asktable/types/chat_create_params.py">params</a>) -> <a href="./src/asktable/types/chat.py">Chat</a></code>
- <code title="get /chats/{chat_id}">client.chats.<a href="./src/asktable/resources/chats/chats.py">retrieve</a>(chat_id) -> <a href="./src/asktable/types/chat_retrieve_response.py">ChatRetrieveResponse</a></code>
- <code title="get /chats">client.chats.<a href="./src/asktable/resources/chats/chats.py">list</a>(\*\*<a href="src/asktable/types/chat_list_params.py">params</a>) -> <a href="./src/asktable/types/chat.py">SyncPage[Chat]</a></code>
- <code title="delete /chats/{chat_id}">client.chats.<a href="./src/asktable/resources/chats/chats.py">delete</a>(chat_id) -> None</code>
- <code title="post /chats/{chat_id}">client.chats.<a href="./src/asktable/resources/chats/chats.py">send_message</a>(chat_id, \*\*<a href="src/asktable/types/chat_send_message_params.py">params</a>) -> <a href="./src/asktable/types/chat_send_message_response.py">ChatSendMessageResponse</a></code>

## Messages

Types:

```python
from asktable.types.chats import (
    MessageRetrieveResponse,
    MessageListResponse,
    MessageSendMessageResponse,
)
```

Methods:

- <code title="get /chats/{chat_id}/messages/{message_id}">client.chats.messages.<a href="./src/asktable/resources/chats/messages.py">retrieve</a>(message_id, \*, chat_id) -> <a href="./src/asktable/types/chats/message_retrieve_response.py">MessageRetrieveResponse</a></code>
- <code title="get /chats/{chat_id}/messages">client.chats.messages.<a href="./src/asktable/resources/chats/messages.py">list</a>(chat_id, \*\*<a href="src/asktable/types/chats/message_list_params.py">params</a>) -> <a href="./src/asktable/types/chats/message_list_response.py">SyncPage[MessageListResponse]</a></code>
- <code title="post /chats/{chat_id}/messages">client.chats.messages.<a href="./src/asktable/resources/chats/messages.py">send_message</a>(chat_id, \*\*<a href="src/asktable/types/chats/message_send_message_params.py">params</a>) -> <a href="./src/asktable/types/chats/message_send_message_response.py">MessageSendMessageResponse</a></code>

# Datasources

Types:

```python
from asktable.types import Datasource, Index, Meta, DatasourceDeleteResponse
```

Methods:

- <code title="post /datasources">client.datasources.<a href="./src/asktable/resources/datasources/datasources.py">create</a>(\*\*<a href="src/asktable/types/datasource_create_params.py">params</a>) -> <a href="./src/asktable/types/datasource.py">Datasource</a></code>
- <code title="get /datasources/{datasource_id}">client.datasources.<a href="./src/asktable/resources/datasources/datasources.py">retrieve</a>(datasource_id) -> <a href="./src/asktable/types/datasource.py">Datasource</a></code>
- <code title="patch /datasources/{datasource_id}">client.datasources.<a href="./src/asktable/resources/datasources/datasources.py">update</a>(datasource_id, \*\*<a href="src/asktable/types/datasource_update_params.py">params</a>) -> <a href="./src/asktable/types/datasource.py">Datasource</a></code>
- <code title="get /datasources">client.datasources.<a href="./src/asktable/resources/datasources/datasources.py">list</a>(\*\*<a href="src/asktable/types/datasource_list_params.py">params</a>) -> <a href="./src/asktable/types/datasource.py">SyncPage[Datasource]</a></code>
- <code title="delete /datasources/{datasource_id}">client.datasources.<a href="./src/asktable/resources/datasources/datasources.py">delete</a>(datasource_id) -> <a href="./src/asktable/types/datasource_delete_response.py">object</a></code>
- <code title="post /datasources/file">client.datasources.<a href="./src/asktable/resources/datasources/datasources.py">create_from_file</a>(\*\*<a href="src/asktable/types/datasource_create_from_file_params.py">params</a>) -> <a href="./src/asktable/types/datasource.py">Datasource</a></code>

## Meta

Types:

```python
from asktable.types.datasources import MetaCreateResponse, MetaUpdateResponse, MetaAnnotateResponse
```

Methods:

- <code title="post /datasources/{datasource_id}/meta">client.datasources.meta.<a href="./src/asktable/resources/datasources/meta.py">create</a>(datasource_id, \*\*<a href="src/asktable/types/datasources/meta_create_params.py">params</a>) -> <a href="./src/asktable/types/datasources/meta_create_response.py">object</a></code>
- <code title="get /datasources/{datasource_id}/meta">client.datasources.meta.<a href="./src/asktable/resources/datasources/meta.py">retrieve</a>(datasource_id) -> <a href="./src/asktable/types/meta.py">Meta</a></code>
- <code title="put /datasources/{datasource_id}/meta">client.datasources.meta.<a href="./src/asktable/resources/datasources/meta.py">update</a>(datasource_id, \*\*<a href="src/asktable/types/datasources/meta_update_params.py">params</a>) -> <a href="./src/asktable/types/datasources/meta_update_response.py">object</a></code>
- <code title="patch /datasources/{datasource_id}/meta">client.datasources.meta.<a href="./src/asktable/resources/datasources/meta.py">annotate</a>(datasource_id, \*\*<a href="src/asktable/types/datasources/meta_annotate_params.py">params</a>) -> <a href="./src/asktable/types/datasources/meta_annotate_response.py">object</a></code>

## UploadParams

Types:

```python
from asktable.types.datasources import UploadParamCreateResponse
```

Methods:

- <code title="post /datasources/upload_params">client.datasources.upload_params.<a href="./src/asktable/resources/datasources/upload_params.py">create</a>(\*\*<a href="src/asktable/types/datasources/upload_param_create_params.py">params</a>) -> <a href="./src/asktable/types/datasources/upload_param_create_response.py">object</a></code>

## Indexes

Types:

```python
from asktable.types.datasources import IndexCreateResponse, IndexDeleteResponse
```

Methods:

- <code title="post /datasources/{ds_id}/indexes">client.datasources.indexes.<a href="./src/asktable/resources/datasources/indexes.py">create</a>(ds_id, \*\*<a href="src/asktable/types/datasources/index_create_params.py">params</a>) -> <a href="./src/asktable/types/datasources/index_create_response.py">object</a></code>
- <code title="get /datasources/{ds_id}/indexes">client.datasources.indexes.<a href="./src/asktable/resources/datasources/indexes.py">list</a>(ds_id, \*\*<a href="src/asktable/types/datasources/index_list_params.py">params</a>) -> <a href="./src/asktable/types/index.py">SyncPage[Index]</a></code>
- <code title="delete /datasources/{ds_id}/indexes/{index_id}">client.datasources.indexes.<a href="./src/asktable/resources/datasources/indexes.py">delete</a>(index_id, \*, ds_id) -> <a href="./src/asktable/types/datasources/index_delete_response.py">object</a></code>

# Bots

Types:

```python
from asktable.types import Chatbot, BotDeleteResponse, BotInviteResponse
```

Methods:

- <code title="post /bots">client.bots.<a href="./src/asktable/resources/bots.py">create</a>(\*\*<a href="src/asktable/types/bot_create_params.py">params</a>) -> <a href="./src/asktable/types/chatbot.py">Chatbot</a></code>
- <code title="get /bots/{bot_id}">client.bots.<a href="./src/asktable/resources/bots.py">retrieve</a>(bot_id) -> <a href="./src/asktable/types/chatbot.py">Chatbot</a></code>
- <code title="patch /bots/{bot_id}">client.bots.<a href="./src/asktable/resources/bots.py">update</a>(bot_id, \*\*<a href="src/asktable/types/bot_update_params.py">params</a>) -> <a href="./src/asktable/types/chatbot.py">Chatbot</a></code>
- <code title="get /bots">client.bots.<a href="./src/asktable/resources/bots.py">list</a>(\*\*<a href="src/asktable/types/bot_list_params.py">params</a>) -> <a href="./src/asktable/types/chatbot.py">SyncPage[Chatbot]</a></code>
- <code title="delete /bots/{bot_id}">client.bots.<a href="./src/asktable/resources/bots.py">delete</a>(bot_id) -> <a href="./src/asktable/types/bot_delete_response.py">object</a></code>
- <code title="post /bots/{bot_id}/invite">client.bots.<a href="./src/asktable/resources/bots.py">invite</a>(bot_id, \*\*<a href="src/asktable/types/bot_invite_params.py">params</a>) -> <a href="./src/asktable/types/bot_invite_response.py">object</a></code>

# Extapis

Types:

```python
from asktable.types import Extapi, ExtapiDeleteResponse
```

Methods:

- <code title="post /extapis">client.extapis.<a href="./src/asktable/resources/extapis/extapis.py">create</a>(\*\*<a href="src/asktable/types/extapi_create_params.py">params</a>) -> <a href="./src/asktable/types/extapi.py">Extapi</a></code>
- <code title="get /extapis/{extapi_id}">client.extapis.<a href="./src/asktable/resources/extapis/extapis.py">retrieve</a>(extapi_id) -> <a href="./src/asktable/types/extapi.py">Extapi</a></code>
- <code title="post /extapis/{extapi_id}">client.extapis.<a href="./src/asktable/resources/extapis/extapis.py">update</a>(extapi_id, \*\*<a href="src/asktable/types/extapi_update_params.py">params</a>) -> <a href="./src/asktable/types/extapi.py">Extapi</a></code>
- <code title="get /extapis">client.extapis.<a href="./src/asktable/resources/extapis/extapis.py">list</a>(\*\*<a href="src/asktable/types/extapi_list_params.py">params</a>) -> <a href="./src/asktable/types/extapi.py">SyncPage[Extapi]</a></code>
- <code title="delete /extapis/{extapi_id}">client.extapis.<a href="./src/asktable/resources/extapis/extapis.py">delete</a>(extapi_id) -> <a href="./src/asktable/types/extapi_delete_response.py">object</a></code>

## Routes

Types:

```python
from asktable.types.extapis import ExtapiRoute, RouteListResponse
```

Methods:

- <code title="post /extapis/{extapi_id}/routes">client.extapis.routes.<a href="./src/asktable/resources/extapis/routes.py">create</a>(\*, path_extapi_id, \*\*<a href="src/asktable/types/extapis/route_create_params.py">params</a>) -> <a href="./src/asktable/types/extapis/extapi_route.py">ExtapiRoute</a></code>
- <code title="get /extapis/{extapi_id}/routes/{route_id}">client.extapis.routes.<a href="./src/asktable/resources/extapis/routes.py">retrieve</a>(route_id, \*, extapi_id) -> <a href="./src/asktable/types/extapis/extapi_route.py">ExtapiRoute</a></code>
- <code title="post /extapis/{extapi_id}/routes/{route_id}">client.extapis.routes.<a href="./src/asktable/resources/extapis/routes.py">update</a>(route_id, \*, extapi_id, \*\*<a href="src/asktable/types/extapis/route_update_params.py">params</a>) -> <a href="./src/asktable/types/extapis/extapi_route.py">ExtapiRoute</a></code>
- <code title="get /extapis/{extapi_id}/routes">client.extapis.routes.<a href="./src/asktable/resources/extapis/routes.py">list</a>(extapi_id) -> <a href="./src/asktable/types/extapis/route_list_response.py">RouteListResponse</a></code>
- <code title="delete /extapis/{extapi_id}/routes/{route_id}">client.extapis.routes.<a href="./src/asktable/resources/extapis/routes.py">delete</a>(route_id, \*, extapi_id) -> None</code>

# Auth

Types:

```python
from asktable.types import AuthCreateTokenResponse, AuthMeResponse
```

Methods:

- <code title="post /auth/tokens">client.auth.<a href="./src/asktable/resources/auth.py">create_token</a>(\*\*<a href="src/asktable/types/auth_create_token_params.py">params</a>) -> <a href="./src/asktable/types/auth_create_token_response.py">object</a></code>
- <code title="get /auth/me">client.auth.<a href="./src/asktable/resources/auth.py">me</a>() -> <a href="./src/asktable/types/auth_me_response.py">object</a></code>

# Answers

Types:

```python
from asktable.types import AnswerResponse
```

Methods:

- <code title="post /single-turn/q2a">client.answers.<a href="./src/asktable/resources/answers.py">create</a>(\*\*<a href="src/asktable/types/answer_create_params.py">params</a>) -> <a href="./src/asktable/types/answer_response.py">AnswerResponse</a></code>
- <code title="get /single-turn/q2a">client.answers.<a href="./src/asktable/resources/answers.py">list</a>(\*\*<a href="src/asktable/types/answer_list_params.py">params</a>) -> <a href="./src/asktable/types/answer_response.py">SyncPage[AnswerResponse]</a></code>

# Sqls

Types:

```python
from asktable.types import QueryResponse
```

Methods:

- <code title="post /single-turn/q2s">client.sqls.<a href="./src/asktable/resources/sqls.py">create</a>(\*\*<a href="src/asktable/types/sql_create_params.py">params</a>) -> <a href="./src/asktable/types/query_response.py">QueryResponse</a></code>
- <code title="get /single-turn/q2s">client.sqls.<a href="./src/asktable/resources/sqls.py">list</a>(\*\*<a href="src/asktable/types/sql_list_params.py">params</a>) -> <a href="./src/asktable/types/query_response.py">SyncPage[QueryResponse]</a></code>

# Caches

Methods:

- <code title="delete /caches/{cache_id}">client.caches.<a href="./src/asktable/resources/caches.py">delete</a>(cache_id) -> None</code>

# Integration

Types:

```python
from asktable.types import FileAskResponse
```

Methods:

- <code title="post /integration/create_excel_ds">client.integration.<a href="./src/asktable/resources/integration.py">create_excel_ds</a>(\*\*<a href="src/asktable/types/integration_create_excel_ds_params.py">params</a>) -> <a href="./src/asktable/types/datasource.py">Datasource</a></code>
- <code title="post /integration/excel_csv_ask">client.integration.<a href="./src/asktable/resources/integration.py">excel_csv_ask</a>(\*\*<a href="src/asktable/types/integration_excel_csv_ask_params.py">params</a>) -> <a href="./src/asktable/types/file_ask_response.py">FileAskResponse</a></code>

# BusinessGlossary

Types:

```python
from asktable.types import (
    Entry,
    EntryWithDefinition,
    BusinessGlossaryCreateResponse,
    BusinessGlossaryDeleteResponse,
)
```

Methods:

- <code title="post /business-glossary">client.business_glossary.<a href="./src/asktable/resources/business_glossary.py">create</a>(\*\*<a href="src/asktable/types/business_glossary_create_params.py">params</a>) -> <a href="./src/asktable/types/business_glossary_create_response.py">BusinessGlossaryCreateResponse</a></code>
- <code title="get /business-glossary/{entry_id}">client.business_glossary.<a href="./src/asktable/resources/business_glossary.py">retrieve</a>(entry_id) -> <a href="./src/asktable/types/entry_with_definition.py">EntryWithDefinition</a></code>
- <code title="patch /business-glossary/{entry_id}">client.business_glossary.<a href="./src/asktable/resources/business_glossary.py">update</a>(entry_id, \*\*<a href="src/asktable/types/business_glossary_update_params.py">params</a>) -> <a href="./src/asktable/types/entry.py">Entry</a></code>
- <code title="get /business-glossary">client.business_glossary.<a href="./src/asktable/resources/business_glossary.py">list</a>(\*\*<a href="src/asktable/types/business_glossary_list_params.py">params</a>) -> <a href="./src/asktable/types/entry_with_definition.py">SyncPage[EntryWithDefinition]</a></code>
- <code title="delete /business-glossary/{entry_id}">client.business_glossary.<a href="./src/asktable/resources/business_glossary.py">delete</a>(entry_id) -> <a href="./src/asktable/types/business_glossary_delete_response.py">object</a></code>

# Preferences

Types:

```python
from asktable.types import (
    PreferenceCreateResponse,
    PreferenceRetrieveResponse,
    PreferenceUpdateResponse,
    PreferenceDeleteResponse,
)
```

Methods:

- <code title="post /preference">client.preferences.<a href="./src/asktable/resources/preferences.py">create</a>(\*\*<a href="src/asktable/types/preference_create_params.py">params</a>) -> <a href="./src/asktable/types/preference_create_response.py">PreferenceCreateResponse</a></code>
- <code title="get /preference">client.preferences.<a href="./src/asktable/resources/preferences.py">retrieve</a>() -> <a href="./src/asktable/types/preference_retrieve_response.py">PreferenceRetrieveResponse</a></code>
- <code title="patch /preference">client.preferences.<a href="./src/asktable/resources/preferences.py">update</a>(\*\*<a href="src/asktable/types/preference_update_params.py">params</a>) -> <a href="./src/asktable/types/preference_update_response.py">PreferenceUpdateResponse</a></code>
- <code title="delete /preference">client.preferences.<a href="./src/asktable/resources/preferences.py">delete</a>() -> <a href="./src/asktable/types/preference_delete_response.py">object</a></code>

# Trainings

Types:

```python
from asktable.types import TrainingCreateResponse, TrainingListResponse, TrainingDeleteResponse
```

Methods:

- <code title="post /training">client.trainings.<a href="./src/asktable/resources/trainings.py">create</a>(\*\*<a href="src/asktable/types/training_create_params.py">params</a>) -> <a href="./src/asktable/types/training_create_response.py">TrainingCreateResponse</a></code>
- <code title="get /training">client.trainings.<a href="./src/asktable/resources/trainings.py">list</a>(\*\*<a href="src/asktable/types/training_list_params.py">params</a>) -> <a href="./src/asktable/types/training_list_response.py">SyncPage[TrainingListResponse]</a></code>
- <code title="delete /training/{id}">client.trainings.<a href="./src/asktable/resources/trainings.py">delete</a>(id, \*\*<a href="src/asktable/types/training_delete_params.py">params</a>) -> <a href="./src/asktable/types/training_delete_response.py">object</a></code>

# Project

Types:

```python
from asktable.types import ProjectListModelGroupsResponse
```

Methods:

- <code title="get /project">client.project.<a href="./src/asktable/resources/project.py">retrieve</a>() -> <a href="./src/asktable/types/sys/project.py">Project</a></code>
- <code title="patch /project">client.project.<a href="./src/asktable/resources/project.py">update</a>(\*\*<a href="src/asktable/types/project_update_params.py">params</a>) -> <a href="./src/asktable/types/sys/project.py">Project</a></code>
- <code title="get /project/model-groups">client.project.<a href="./src/asktable/resources/project.py">list_model_groups</a>() -> <a href="./src/asktable/types/project_list_model_groups_response.py">ProjectListModelGroupsResponse</a></code>

# Scores

Types:

```python
from asktable.types import ScoreCreateResponse
```

Methods:

- <code title="post /score">client.scores.<a href="./src/asktable/resources/scores.py">create</a>(\*\*<a href="src/asktable/types/score_create_params.py">params</a>) -> <a href="./src/asktable/types/score_create_response.py">ScoreCreateResponse</a></code>
