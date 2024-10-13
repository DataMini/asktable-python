# Shared Types

```python
from asktable.types import AnswerModel, Message, Policy
```

# Securetunnels

Types:

```python
from asktable.types import SecureTunnel, SecuretunnelUpdateResponse, SecuretunnelListResponse
```

Methods:

- <code title="post /securetunnels">client.securetunnels.<a href="./src/asktable/resources/securetunnels/securetunnels.py">create</a>(\*\*<a href="src/asktable/types/securetunnel_create_params.py">params</a>) -> <a href="./src/asktable/types/secure_tunnel.py">SecureTunnel</a></code>
- <code title="get /securetunnels/{securetunnel_id}">client.securetunnels.<a href="./src/asktable/resources/securetunnels/securetunnels.py">retrieve</a>(securetunnel_id) -> <a href="./src/asktable/types/secure_tunnel.py">SecureTunnel</a></code>
- <code title="patch /securetunnels/{securetunnel_id}">client.securetunnels.<a href="./src/asktable/resources/securetunnels/securetunnels.py">update</a>(securetunnel_id, \*\*<a href="src/asktable/types/securetunnel_update_params.py">params</a>) -> <a href="./src/asktable/types/securetunnel_update_response.py">object</a></code>
- <code title="get /securetunnels">client.securetunnels.<a href="./src/asktable/resources/securetunnels/securetunnels.py">list</a>(\*\*<a href="src/asktable/types/securetunnel_list_params.py">params</a>) -> <a href="./src/asktable/types/securetunnel_list_response.py">SecuretunnelListResponse</a></code>
- <code title="delete /securetunnels/{securetunnel_id}">client.securetunnels.<a href="./src/asktable/resources/securetunnels/securetunnels.py">delete</a>(securetunnel_id) -> None</code>

## Links

Types:

```python
from asktable.types.securetunnels import SecureTunnelLink
```

Methods:

- <code title="get /securetunnels/{securetunnel_id}/links">client.securetunnels.links.<a href="./src/asktable/resources/securetunnels/links.py">list</a>(securetunnel_id, \*\*<a href="src/asktable/types/securetunnels/link_list_params.py">params</a>) -> <a href="./src/asktable/types/securetunnels/secure_tunnel_link.py">SecureTunnelLink</a></code>

# Roles

Types:

```python
from asktable.types import Role, RoleListResponse, RoleDeleteResponse
```

Methods:

- <code title="post /roles">client.roles.<a href="./src/asktable/resources/roles/roles.py">create</a>(\*\*<a href="src/asktable/types/role_create_params.py">params</a>) -> <a href="./src/asktable/types/role.py">Role</a></code>
- <code title="get /roles/{role_id}">client.roles.<a href="./src/asktable/resources/roles/roles.py">retrieve</a>(role_id) -> <a href="./src/asktable/types/role.py">Role</a></code>
- <code title="patch /roles/{role_id}">client.roles.<a href="./src/asktable/resources/roles/roles.py">update</a>(role_id, \*\*<a href="src/asktable/types/role_update_params.py">params</a>) -> <a href="./src/asktable/types/role.py">Role</a></code>
- <code title="get /roles">client.roles.<a href="./src/asktable/resources/roles/roles.py">list</a>(\*\*<a href="src/asktable/types/role_list_params.py">params</a>) -> <a href="./src/asktable/types/role_list_response.py">RoleListResponse</a></code>
- <code title="delete /roles/{role_id}">client.roles.<a href="./src/asktable/resources/roles/roles.py">delete</a>(role_id) -> <a href="./src/asktable/types/role_delete_response.py">object</a></code>

## Policies

Types:

```python
from asktable.types.roles import PolicyListResponse
```

Methods:

- <code title="get /roles/{role_id}/policies">client.roles.policies.<a href="./src/asktable/resources/roles/policies.py">list</a>(role_id) -> <a href="./src/asktable/types/roles/policy_list_response.py">PolicyListResponse</a></code>

## Variables

Types:

```python
from asktable.types.roles import VariableListResponse
```

Methods:

- <code title="get /roles/{role_id}/variables">client.roles.variables.<a href="./src/asktable/resources/roles/variables.py">list</a>(role_id, \*\*<a href="src/asktable/types/roles/variable_list_params.py">params</a>) -> <a href="./src/asktable/types/roles/variable_list_response.py">object</a></code>

# Policies

Types:

```python
from asktable.types import PolicyListResponse
```

Methods:

- <code title="post /policies">client.policies.<a href="./src/asktable/resources/policies.py">create</a>(\*\*<a href="src/asktable/types/policy_create_params.py">params</a>) -> <a href="./src/asktable/types/shared/policy.py">Policy</a></code>
- <code title="get /policies/{policy_id}">client.policies.<a href="./src/asktable/resources/policies.py">retrieve</a>(policy_id) -> <a href="./src/asktable/types/shared/policy.py">Policy</a></code>
- <code title="patch /policies/{policy_id}">client.policies.<a href="./src/asktable/resources/policies.py">update</a>(policy_id, \*\*<a href="src/asktable/types/policy_update_params.py">params</a>) -> <a href="./src/asktable/types/shared/policy.py">Policy</a></code>
- <code title="get /policies">client.policies.<a href="./src/asktable/resources/policies.py">list</a>(\*\*<a href="src/asktable/types/policy_list_params.py">params</a>) -> <a href="./src/asktable/types/policy_list_response.py">PolicyListResponse</a></code>
- <code title="delete /policies/{policy_id}">client.policies.<a href="./src/asktable/resources/policies.py">delete</a>(policy_id) -> None</code>

# Chats

Types:

```python
from asktable.types import Chat, ChatOut, ChatListResponse
```

Methods:

- <code title="post /chats">client.chats.<a href="./src/asktable/resources/chats/chats.py">create</a>(\*\*<a href="src/asktable/types/chat_create_params.py">params</a>) -> <a href="./src/asktable/types/chat.py">Chat</a></code>
- <code title="get /chats/{chat_id}">client.chats.<a href="./src/asktable/resources/chats/chats.py">retrieve</a>(chat_id) -> <a href="./src/asktable/types/chat_out.py">ChatOut</a></code>
- <code title="get /chats">client.chats.<a href="./src/asktable/resources/chats/chats.py">list</a>(\*\*<a href="src/asktable/types/chat_list_params.py">params</a>) -> <a href="./src/asktable/types/chat_list_response.py">ChatListResponse</a></code>
- <code title="delete /chats/{chat_id}">client.chats.<a href="./src/asktable/resources/chats/chats.py">delete</a>(chat_id) -> None</code>

## Messages

Types:

```python
from asktable.types.chats import MessageModel, MessageListResponse
```

Methods:

- <code title="post /chats/{chat_id}">client.chats.messages.<a href="./src/asktable/resources/chats/messages.py">create</a>(chat_id, \*\*<a href="src/asktable/types/chats/message_create_params.py">params</a>) -> <a href="./src/asktable/types/shared/message.py">Message</a></code>
- <code title="get /chats/{chat_id}/messages/{message_id}">client.chats.messages.<a href="./src/asktable/resources/chats/messages.py">retrieve</a>(message_id, \*, chat_id) -> <a href="./src/asktable/types/shared/message.py">Message</a></code>
- <code title="get /chats/{chat_id}/messages">client.chats.messages.<a href="./src/asktable/resources/chats/messages.py">list</a>(chat_id, \*\*<a href="src/asktable/types/chats/message_list_params.py">params</a>) -> <a href="./src/asktable/types/chats/message_list_response.py">MessageListResponse</a></code>

# Datasources

Types:

```python
from asktable.types import DataSource, DatasourceListResponse, DatasourceDeleteResponse
```

Methods:

- <code title="post /datasources">client.datasources.<a href="./src/asktable/resources/datasources/datasources.py">create</a>(\*\*<a href="src/asktable/types/datasource_create_params.py">params</a>) -> <a href="./src/asktable/types/data_source.py">DataSource</a></code>
- <code title="get /datasources/{datasource_id}">client.datasources.<a href="./src/asktable/resources/datasources/datasources.py">retrieve</a>(datasource_id) -> <a href="./src/asktable/types/data_source.py">DataSource</a></code>
- <code title="patch /datasources/{datasource_id}">client.datasources.<a href="./src/asktable/resources/datasources/datasources.py">update</a>(datasource_id, \*\*<a href="src/asktable/types/datasource_update_params.py">params</a>) -> <a href="./src/asktable/types/data_source.py">DataSource</a></code>
- <code title="get /datasources">client.datasources.<a href="./src/asktable/resources/datasources/datasources.py">list</a>(\*\*<a href="src/asktable/types/datasource_list_params.py">params</a>) -> <a href="./src/asktable/types/datasource_list_response.py">DatasourceListResponse</a></code>
- <code title="delete /datasources/{datasource_id}">client.datasources.<a href="./src/asktable/resources/datasources/datasources.py">delete</a>(datasource_id) -> <a href="./src/asktable/types/datasource_delete_response.py">object</a></code>
- <code title="post /datasources/file">client.datasources.<a href="./src/asktable/resources/datasources/datasources.py">create_from_file</a>(\*\*<a href="src/asktable/types/datasource_create_from_file_params.py">params</a>) -> <a href="./src/asktable/types/data_source.py">DataSource</a></code>

## Meta

Types:

```python
from asktable.types.datasources import Meta, MetaCreateResponse, MetaUpdateResponse
```

Methods:

- <code title="post /datasources/{datasource_id}/meta">client.datasources.meta.<a href="./src/asktable/resources/datasources/meta.py">create</a>(datasource_id) -> <a href="./src/asktable/types/datasources/meta_create_response.py">object</a></code>
- <code title="get /datasources/{datasource_id}/meta">client.datasources.meta.<a href="./src/asktable/resources/datasources/meta.py">retrieve</a>(datasource_id, \*\*<a href="src/asktable/types/datasources/meta_retrieve_params.py">params</a>) -> <a href="./src/asktable/types/datasources/meta.py">Meta</a></code>
- <code title="put /datasources/{datasource_id}/meta">client.datasources.meta.<a href="./src/asktable/resources/datasources/meta.py">update</a>(\*, path_datasource_id, \*\*<a href="src/asktable/types/datasources/meta_update_params.py">params</a>) -> <a href="./src/asktable/types/datasources/meta_update_response.py">object</a></code>

## UploadParams

Types:

```python
from asktable.types.datasources import UploadParamCreateResponse
```

Methods:

- <code title="post /datasources/upload_params">client.datasources.upload_params.<a href="./src/asktable/resources/datasources/upload_params.py">create</a>(\*\*<a href="src/asktable/types/datasources/upload_param_create_params.py">params</a>) -> <a href="./src/asktable/types/datasources/upload_param_create_response.py">object</a></code>

# Bots

Types:

```python
from asktable.types import ChatBot, BotListResponse, BotDeleteResponse, BotInviteResponse
```

Methods:

- <code title="post /bots">client.bots.<a href="./src/asktable/resources/bots.py">create</a>(\*\*<a href="src/asktable/types/bot_create_params.py">params</a>) -> <a href="./src/asktable/types/chat_bot.py">ChatBot</a></code>
- <code title="get /bots/{bot_id}">client.bots.<a href="./src/asktable/resources/bots.py">retrieve</a>(bot_id) -> <a href="./src/asktable/types/chat_bot.py">ChatBot</a></code>
- <code title="patch /bots/{bot_id}">client.bots.<a href="./src/asktable/resources/bots.py">update</a>(bot_id, \*\*<a href="src/asktable/types/bot_update_params.py">params</a>) -> <a href="./src/asktable/types/chat_bot.py">ChatBot</a></code>
- <code title="get /bots">client.bots.<a href="./src/asktable/resources/bots.py">list</a>(\*\*<a href="src/asktable/types/bot_list_params.py">params</a>) -> <a href="./src/asktable/types/bot_list_response.py">BotListResponse</a></code>
- <code title="delete /bots/{bot_id}">client.bots.<a href="./src/asktable/resources/bots.py">delete</a>(bot_id) -> <a href="./src/asktable/types/bot_delete_response.py">object</a></code>
- <code title="post /bots/{bot_id}/invite">client.bots.<a href="./src/asktable/resources/bots.py">invite</a>(bot_id, \*\*<a href="src/asktable/types/bot_invite_params.py">params</a>) -> <a href="./src/asktable/types/bot_invite_response.py">object</a></code>

# Extapis

Types:

```python
from asktable.types import ExtAPIModel, ExtapiListResponse, ExtapiDeleteResponse
```

Methods:

- <code title="post /extapis">client.extapis.<a href="./src/asktable/resources/extapis/extapis.py">create</a>(\*\*<a href="src/asktable/types/extapi_create_params.py">params</a>) -> <a href="./src/asktable/types/ext_api_model.py">ExtAPIModel</a></code>
- <code title="get /extapis/{extapi_id}">client.extapis.<a href="./src/asktable/resources/extapis/extapis.py">retrieve</a>(extapi_id) -> <a href="./src/asktable/types/ext_api_model.py">ExtAPIModel</a></code>
- <code title="post /extapis/{extapi_id}">client.extapis.<a href="./src/asktable/resources/extapis/extapis.py">update</a>(extapi_id, \*\*<a href="src/asktable/types/extapi_update_params.py">params</a>) -> <a href="./src/asktable/types/ext_api_model.py">ExtAPIModel</a></code>
- <code title="get /extapis">client.extapis.<a href="./src/asktable/resources/extapis/extapis.py">list</a>(\*\*<a href="src/asktable/types/extapi_list_params.py">params</a>) -> <a href="./src/asktable/types/extapi_list_response.py">ExtapiListResponse</a></code>
- <code title="delete /extapis/{extapi_id}">client.extapis.<a href="./src/asktable/resources/extapis/extapis.py">delete</a>(extapi_id) -> <a href="./src/asktable/types/extapi_delete_response.py">object</a></code>

## Routes

Types:

```python
from asktable.types.extapis import ExtAPIRouteModel, RouteListResponse
```

Methods:

- <code title="post /extapis/{extapi_id}/routes">client.extapis.routes.<a href="./src/asktable/resources/extapis/routes.py">create</a>(\*, path_extapi_id, \*\*<a href="src/asktable/types/extapis/route_create_params.py">params</a>) -> <a href="./src/asktable/types/extapis/ext_api_route_model.py">ExtAPIRouteModel</a></code>
- <code title="get /extapis/{extapi_id}/routes/{route_id}">client.extapis.routes.<a href="./src/asktable/resources/extapis/routes.py">retrieve</a>(route_id, \*, extapi_id) -> <a href="./src/asktable/types/extapis/ext_api_route_model.py">ExtAPIRouteModel</a></code>
- <code title="post /extapis/{extapi_id}/routes/{route_id}">client.extapis.routes.<a href="./src/asktable/resources/extapis/routes.py">update</a>(route_id, \*, extapi_id, \*\*<a href="src/asktable/types/extapis/route_update_params.py">params</a>) -> <a href="./src/asktable/types/extapis/ext_api_route_model.py">ExtAPIRouteModel</a></code>
- <code title="get /extapis/{extapi_id}/routes">client.extapis.routes.<a href="./src/asktable/resources/extapis/routes.py">list</a>(extapi_id) -> <a href="./src/asktable/types/extapis/route_list_response.py">RouteListResponse</a></code>
- <code title="delete /extapis/{extapi_id}/routes/{route_id}">client.extapis.routes.<a href="./src/asktable/resources/extapis/routes.py">delete</a>(route_id, \*, extapi_id) -> None</code>

# Auth

## Tokens

Types:

```python
from asktable.types.auth import TokenCreateResponse
```

Methods:

- <code title="post /auth/tokens">client.auth.tokens.<a href="./src/asktable/resources/auth/tokens.py">create</a>(\*\*<a href="src/asktable/types/auth/token_create_params.py">params</a>) -> <a href="./src/asktable/types/auth/token_create_response.py">object</a></code>

## Me

Types:

```python
from asktable.types.auth import MeRetrieveResponse
```

Methods:

- <code title="get /auth/me">client.auth.me.<a href="./src/asktable/resources/auth/me.py">retrieve</a>() -> <a href="./src/asktable/types/auth/me_retrieve_response.py">object</a></code>

# SingleTurn

## Q2a

Types:

```python
from asktable.types.single_turn import Q2aListResponse
```

Methods:

- <code title="post /single-turn/q2a">client.single_turn.q2a.<a href="./src/asktable/resources/single_turn/q2a.py">create</a>(\*\*<a href="src/asktable/types/single_turn/q2a_create_params.py">params</a>) -> <a href="./src/asktable/types/shared/answer_model.py">AnswerModel</a></code>
- <code title="get /single-turn/q2a">client.single_turn.q2a.<a href="./src/asktable/resources/single_turn/q2a.py">list</a>(\*\*<a href="src/asktable/types/single_turn/q2a_list_params.py">params</a>) -> <a href="./src/asktable/types/single_turn/q2a_list_response.py">Q2aListResponse</a></code>

## Q2s

Types:

```python
from asktable.types.single_turn import Q2sResponse, Q2ListResponse
```

Methods:

- <code title="post /single-turn/q2s">client.single_turn.q2s.<a href="./src/asktable/resources/single_turn/q2s.py">create</a>(\*\*<a href="src/asktable/types/single_turn/q2_create_params.py">params</a>) -> <a href="./src/asktable/types/single_turn/q2s_response.py">Q2sResponse</a></code>
- <code title="get /single-turn/q2s">client.single_turn.q2s.<a href="./src/asktable/resources/single_turn/q2s.py">list</a>(\*\*<a href="src/asktable/types/single_turn/q2_list_params.py">params</a>) -> <a href="./src/asktable/types/single_turn/q2_list_response.py">Q2ListResponse</a></code>

# Caches

Methods:

- <code title="delete /caches/{cache_id}">client.caches.<a href="./src/asktable/resources/caches.py">delete</a>(cache_id) -> None</code>

# Integration

Types:

```python
from asktable.types import AnswerDataSourceOut
```

Methods:

- <code title="post /integration/excel_csv_ask">client.integration.<a href="./src/asktable/resources/integration.py">excel_csv_ask</a>(\*\*<a href="src/asktable/types/integration_excel_csv_ask_params.py">params</a>) -> <a href="./src/asktable/types/answer_data_source_out.py">AnswerDataSourceOut</a></code>

# Sys

## Projects

Types:

```python
from asktable.types.sys import Project, ProjectListResponse, ProjectDeleteResponse
```

Methods:

- <code title="post /sys/projects">client.sys.projects.<a href="./src/asktable/resources/sys/projects/projects.py">create</a>(\*\*<a href="src/asktable/types/sys/project_create_params.py">params</a>) -> <a href="./src/asktable/types/sys/project.py">Project</a></code>
- <code title="get /sys/projects/{project_id}">client.sys.projects.<a href="./src/asktable/resources/sys/projects/projects.py">retrieve</a>(project_id) -> <a href="./src/asktable/types/sys/project.py">Project</a></code>
- <code title="patch /sys/projects/{project_id}">client.sys.projects.<a href="./src/asktable/resources/sys/projects/projects.py">update</a>(project_id, \*\*<a href="src/asktable/types/sys/project_update_params.py">params</a>) -> <a href="./src/asktable/types/sys/project.py">Project</a></code>
- <code title="get /sys/projects">client.sys.projects.<a href="./src/asktable/resources/sys/projects/projects.py">list</a>(\*\*<a href="src/asktable/types/sys/project_list_params.py">params</a>) -> <a href="./src/asktable/types/sys/project_list_response.py">ProjectListResponse</a></code>
- <code title="delete /sys/projects/{project_id}">client.sys.projects.<a href="./src/asktable/resources/sys/projects/projects.py">delete</a>(project_id) -> <a href="./src/asktable/types/sys/project_delete_response.py">object</a></code>

### APIKeys

Types:

```python
from asktable.types.sys.projects import APIKey, APIKeyCreate, APIKeyListResponse
```

Methods:

- <code title="post /sys/projects/{project_id}/api-keys">client.sys.projects.api_keys.<a href="./src/asktable/resources/sys/projects/api_keys.py">create</a>(project_id, \*\*<a href="src/asktable/types/sys/projects/api_key_create_params.py">params</a>) -> <a href="./src/asktable/types/sys/projects/api_key_create.py">APIKeyCreate</a></code>
- <code title="get /sys/projects/{project_id}/api-keys">client.sys.projects.api_keys.<a href="./src/asktable/resources/sys/projects/api_keys.py">list</a>(project_id) -> <a href="./src/asktable/types/sys/projects/api_key_list_response.py">APIKeyListResponse</a></code>
- <code title="delete /sys/projects/{project_id}/api-keys/{key_id}">client.sys.projects.api_keys.<a href="./src/asktable/resources/sys/projects/api_keys.py">delete</a>(key_id, \*, project_id) -> None</code>

### Tokens

Types:

```python
from asktable.types.sys.projects import TokenCreateResponse
```

Methods:

- <code title="post /sys/projects/{project_id}/tokens">client.sys.projects.tokens.<a href="./src/asktable/resources/sys/projects/tokens.py">create</a>(project_id, \*\*<a href="src/asktable/types/sys/projects/token_create_params.py">params</a>) -> <a href="./src/asktable/types/sys/projects/token_create_response.py">object</a></code>
