# Shared Types

```python
from asktable.types import Policy
```

# Sys

## Projects

Types:

```python
from asktable.types.sys import Project, ProjectListResponse, ProjectDeleteResponse
```

Methods:

- <code title="post /sys/projects">client.sys.projects.<a href="./src/asktable/resources/sys/projects/projects.py">create</a>(\*\*<a href="src/asktable/types/sys/project_create_params.py">params</a>) -> <a href="./src/asktable/types/sys/project.py">Project</a></code>
- <code title="get /sys/projects/{project_id}">client.sys.projects.<a href="./src/asktable/resources/sys/projects/projects.py">retrieve</a>(project_id) -> <a href="./src/asktable/types/sys/project.py">Project</a></code>
- <code title="get /sys/projects">client.sys.projects.<a href="./src/asktable/resources/sys/projects/projects.py">list</a>(\*\*<a href="src/asktable/types/sys/project_list_params.py">params</a>) -> <a href="./src/asktable/types/sys/project_list_response.py">ProjectListResponse</a></code>
- <code title="delete /sys/projects/{project_id}">client.sys.projects.<a href="./src/asktable/resources/sys/projects/projects.py">delete</a>(project_id) -> <a href="./src/asktable/types/sys/project_delete_response.py">object</a></code>

### APIKeys

Types:

```python
from asktable.types.sys.projects import (
    APIKeyCreateResponse,
    APIKeyListResponse,
    APIKeyDeleteResponse,
)
```

Methods:

- <code title="post /sys/projects/{project_id}/api-keys">client.sys.projects.api_keys.<a href="./src/asktable/resources/sys/projects/api_keys.py">create</a>(project_id, \*\*<a href="src/asktable/types/sys/projects/api_key_create_params.py">params</a>) -> <a href="./src/asktable/types/sys/projects/api_key_create_response.py">APIKeyCreateResponse</a></code>
- <code title="get /sys/projects/{project_id}/api-keys">client.sys.projects.api_keys.<a href="./src/asktable/resources/sys/projects/api_keys.py">list</a>(project_id) -> <a href="./src/asktable/types/sys/projects/api_key_list_response.py">APIKeyListResponse</a></code>
- <code title="delete /sys/projects/{project_id}/api-keys/{key_id}">client.sys.projects.api_keys.<a href="./src/asktable/resources/sys/projects/api_keys.py">delete</a>(key_id, \*, project_id) -> <a href="./src/asktable/types/sys/projects/api_key_delete_response.py">object</a></code>

### Tokens

Types:

```python
from asktable.types.sys.projects import TokenCreateResponse
```

Methods:

- <code title="post /sys/projects/{project_id}/tokens">client.sys.projects.tokens.<a href="./src/asktable/resources/sys/projects/tokens.py">create</a>(project_id, \*\*<a href="src/asktable/types/sys/projects/token_create_params.py">params</a>) -> <a href="./src/asktable/types/sys/projects/token_create_response.py">object</a></code>

# Securetunnels

Types:

```python
from asktable.types import SecureTunnel, SecuretunnelUpdateResponse, SecuretunnelListResponse
```

Methods:

- <code title="post /securetunnels/">client.securetunnels.<a href="./src/asktable/resources/securetunnels/securetunnels.py">create</a>(\*\*<a href="src/asktable/types/securetunnel_create_params.py">params</a>) -> <a href="./src/asktable/types/secure_tunnel.py">SecureTunnel</a></code>
- <code title="get /securetunnels/{securetunnel_id}">client.securetunnels.<a href="./src/asktable/resources/securetunnels/securetunnels.py">retrieve</a>(securetunnel_id) -> <a href="./src/asktable/types/secure_tunnel.py">SecureTunnel</a></code>
- <code title="patch /securetunnels/{securetunnel_id}">client.securetunnels.<a href="./src/asktable/resources/securetunnels/securetunnels.py">update</a>(securetunnel_id, \*\*<a href="src/asktable/types/securetunnel_update_params.py">params</a>) -> <a href="./src/asktable/types/securetunnel_update_response.py">object</a></code>
- <code title="get /securetunnels/">client.securetunnels.<a href="./src/asktable/resources/securetunnels/securetunnels.py">list</a>(\*\*<a href="src/asktable/types/securetunnel_list_params.py">params</a>) -> <a href="./src/asktable/types/securetunnel_list_response.py">SecuretunnelListResponse</a></code>
- <code title="delete /securetunnels/{securetunnel_id}">client.securetunnels.<a href="./src/asktable/resources/securetunnels/securetunnels.py">delete</a>(securetunnel_id) -> None</code>

## Links

Types:

```python
from asktable.types.securetunnels import LinkListResponse
```

Methods:

- <code title="get /securetunnels/{securetunnel_id}/links">client.securetunnels.links.<a href="./src/asktable/resources/securetunnels/links.py">list</a>(securetunnel_id, \*\*<a href="src/asktable/types/securetunnels/link_list_params.py">params</a>) -> <a href="./src/asktable/types/securetunnels/link_list_response.py">LinkListResponse</a></code>

# Auth

## Roles

Types:

```python
from asktable.types.auth import Role, RoleListResponse, RoleDeleteResponse
```

Methods:

- <code title="post /auth/roles">client.auth.roles.<a href="./src/asktable/resources/auth/roles/roles.py">create</a>(\*\*<a href="src/asktable/types/auth/role_create_params.py">params</a>) -> <a href="./src/asktable/types/auth/role.py">Role</a></code>
- <code title="get /auth/roles/{role_id}">client.auth.roles.<a href="./src/asktable/resources/auth/roles/roles.py">retrieve</a>(role_id) -> <a href="./src/asktable/types/auth/role.py">Role</a></code>
- <code title="patch /auth/roles/{role_id}">client.auth.roles.<a href="./src/asktable/resources/auth/roles/roles.py">update</a>(role_id, \*\*<a href="src/asktable/types/auth/role_update_params.py">params</a>) -> <a href="./src/asktable/types/auth/role.py">Role</a></code>
- <code title="get /auth/roles">client.auth.roles.<a href="./src/asktable/resources/auth/roles/roles.py">list</a>(\*\*<a href="src/asktable/types/auth/role_list_params.py">params</a>) -> <a href="./src/asktable/types/auth/role_list_response.py">RoleListResponse</a></code>
- <code title="delete /auth/roles/{role_id}">client.auth.roles.<a href="./src/asktable/resources/auth/roles/roles.py">delete</a>(role_id) -> <a href="./src/asktable/types/auth/role_delete_response.py">object</a></code>

### Policies

Types:

```python
from asktable.types.auth.roles import PolicyListResponse
```

Methods:

- <code title="get /auth/roles/{role_id}/policies">client.auth.roles.policies.<a href="./src/asktable/resources/auth/roles/policies.py">list</a>(role_id) -> <a href="./src/asktable/types/auth/roles/policy_list_response.py">PolicyListResponse</a></code>

### Variables

Types:

```python
from asktable.types.auth.roles import VariableListResponse
```

Methods:

- <code title="get /auth/roles/{role_id}/variables">client.auth.roles.variables.<a href="./src/asktable/resources/auth/roles/variables.py">list</a>(role_id, \*\*<a href="src/asktable/types/auth/roles/variable_list_params.py">params</a>) -> <a href="./src/asktable/types/auth/roles/variable_list_response.py">object</a></code>

## Policies

Types:

```python
from asktable.types.auth import PolicyListResponse
```

Methods:

- <code title="post /auth/policies">client.auth.policies.<a href="./src/asktable/resources/auth/policies.py">create</a>(\*\*<a href="src/asktable/types/auth/policy_create_params.py">params</a>) -> <a href="./src/asktable/types/shared/policy.py">Policy</a></code>
- <code title="get /auth/policies/{policy_id}">client.auth.policies.<a href="./src/asktable/resources/auth/policies.py">retrieve</a>(policy_id) -> <a href="./src/asktable/types/shared/policy.py">Policy</a></code>
- <code title="patch /auth/policies/{policy_id}">client.auth.policies.<a href="./src/asktable/resources/auth/policies.py">update</a>(policy_id, \*\*<a href="src/asktable/types/auth/policy_update_params.py">params</a>) -> <a href="./src/asktable/types/shared/policy.py">Policy</a></code>
- <code title="get /auth/policies">client.auth.policies.<a href="./src/asktable/resources/auth/policies.py">list</a>(\*\*<a href="src/asktable/types/auth/policy_list_params.py">params</a>) -> <a href="./src/asktable/types/auth/policy_list_response.py">PolicyListResponse</a></code>
- <code title="delete /auth/policies/{policy_id}">client.auth.policies.<a href="./src/asktable/resources/auth/policies.py">delete</a>(policy_id) -> None</code>

# Chats

Types:

```python
from asktable.types import Chat, Message, ChatRetrieveResponse, ChatListResponse
```

Methods:

- <code title="post /chats/">client.chats.<a href="./src/asktable/resources/chats/chats.py">create</a>(\*\*<a href="src/asktable/types/chat_create_params.py">params</a>) -> <a href="./src/asktable/types/chat.py">Chat</a></code>
- <code title="get /chats/{chat_id}">client.chats.<a href="./src/asktable/resources/chats/chats.py">retrieve</a>(chat_id) -> <a href="./src/asktable/types/chat_retrieve_response.py">ChatRetrieveResponse</a></code>
- <code title="get /chats/">client.chats.<a href="./src/asktable/resources/chats/chats.py">list</a>(\*\*<a href="src/asktable/types/chat_list_params.py">params</a>) -> <a href="./src/asktable/types/chat_list_response.py">ChatListResponse</a></code>
- <code title="delete /chats/{chat_id}">client.chats.<a href="./src/asktable/resources/chats/chats.py">delete_conversation</a>(chat_id) -> None</code>
- <code title="post /chats/{chat_id}">client.chats.<a href="./src/asktable/resources/chats/chats.py">send</a>(chat_id, \*\*<a href="src/asktable/types/chat_send_params.py">params</a>) -> <a href="./src/asktable/types/message.py">Message</a></code>

## Messages

Types:

```python
from asktable.types.chats import MessageListResponse
```

Methods:

- <code title="get /chats/{chat_id}/messages/{message_id}">client.chats.messages.<a href="./src/asktable/resources/chats/messages.py">retrieve</a>(message_id, \*, chat_id) -> <a href="./src/asktable/types/message.py">Message</a></code>
- <code title="get /chats/{chat_id}/messages">client.chats.messages.<a href="./src/asktable/resources/chats/messages.py">list</a>(chat_id, \*\*<a href="src/asktable/types/chats/message_list_params.py">params</a>) -> <a href="./src/asktable/types/chats/message_list_response.py">MessageListResponse</a></code>

# Datasources

Types:

```python
from asktable.types import Datasource, Meta, DatasourceListResponse, DatasourceDeleteResponse
```

Methods:

- <code title="post /datasources/">client.datasources.<a href="./src/asktable/resources/datasources/datasources.py">create</a>(\*\*<a href="src/asktable/types/datasource_create_params.py">params</a>) -> <a href="./src/asktable/types/datasource.py">Datasource</a></code>
- <code title="get /datasources/{datasource_id}">client.datasources.<a href="./src/asktable/resources/datasources/datasources.py">retrieve</a>(datasource_id) -> <a href="./src/asktable/types/datasource.py">Datasource</a></code>
- <code title="patch /datasources/{datasource_id}">client.datasources.<a href="./src/asktable/resources/datasources/datasources.py">update</a>(datasource_id, \*\*<a href="src/asktable/types/datasource_update_params.py">params</a>) -> <a href="./src/asktable/types/datasource.py">Datasource</a></code>
- <code title="get /datasources/">client.datasources.<a href="./src/asktable/resources/datasources/datasources.py">list</a>(\*\*<a href="src/asktable/types/datasource_list_params.py">params</a>) -> <a href="./src/asktable/types/datasource_list_response.py">DatasourceListResponse</a></code>
- <code title="delete /datasources/{datasource_id}">client.datasources.<a href="./src/asktable/resources/datasources/datasources.py">delete</a>(datasource_id) -> <a href="./src/asktable/types/datasource_delete_response.py">object</a></code>

## Meta

Types:

```python
from asktable.types.datasources import MetaCreateResponse, MetaUpdateResponse
```

Methods:

- <code title="post /datasources/{datasource_id}/meta">client.datasources.meta.<a href="./src/asktable/resources/datasources/meta.py">create</a>(datasource_id) -> <a href="./src/asktable/types/datasources/meta_create_response.py">object</a></code>
- <code title="get /datasources/{datasource_id}/meta">client.datasources.meta.<a href="./src/asktable/resources/datasources/meta.py">retrieve</a>(datasource_id, \*\*<a href="src/asktable/types/datasources/meta_retrieve_params.py">params</a>) -> <a href="./src/asktable/types/meta.py">Meta</a></code>
- <code title="put /datasources/{datasource_id}/meta">client.datasources.meta.<a href="./src/asktable/resources/datasources/meta.py">update</a>(\*, path_datasource_id, \*\*<a href="src/asktable/types/datasources/meta_update_params.py">params</a>) -> <a href="./src/asktable/types/datasources/meta_update_response.py">object</a></code>

## UploadParams

Types:

```python
from asktable.types.datasources import UploadParamCreateResponse
```

Methods:

- <code title="post /datasources/upload_params">client.datasources.upload_params.<a href="./src/asktable/resources/datasources/upload_params.py">create</a>(\*\*<a href="src/asktable/types/datasources/upload_param_create_params.py">params</a>) -> <a href="./src/asktable/types/datasources/upload_param_create_response.py">object</a></code>

## UploadFile

Types:

```python
from asktable.types.datasources import UploadFileCreateResponse
```

Methods:

- <code title="post /datasources/upload_file">client.datasources.upload_file.<a href="./src/asktable/resources/datasources/upload_file.py">create</a>(\*\*<a href="src/asktable/types/datasources/upload_file_create_params.py">params</a>) -> <a href="./src/asktable/types/datasources/upload_file_create_response.py">object</a></code>

## DownloadURL

Types:

```python
from asktable.types.datasources import DownloadURLRetrieveResponse
```

Methods:

- <code title="get /datasources/{datasource_id}/download_url">client.datasources.download_url.<a href="./src/asktable/resources/datasources/download_url.py">retrieve</a>(datasource_id) -> <a href="./src/asktable/types/datasources/download_url_retrieve_response.py">object</a></code>

# Bots

Types:

```python
from asktable.types import ChatBot, BotListResponse, BotDeleteResponse
```

Methods:

- <code title="post /bots/">client.bots.<a href="./src/asktable/resources/bots.py">create</a>(\*\*<a href="src/asktable/types/bot_create_params.py">params</a>) -> <a href="./src/asktable/types/chat_bot.py">ChatBot</a></code>
- <code title="get /bots/{bot_id}">client.bots.<a href="./src/asktable/resources/bots.py">retrieve</a>(bot_id) -> <a href="./src/asktable/types/chat_bot.py">ChatBot</a></code>
- <code title="patch /bots/{bot_id}">client.bots.<a href="./src/asktable/resources/bots.py">update</a>(bot_id, \*\*<a href="src/asktable/types/bot_update_params.py">params</a>) -> <a href="./src/asktable/types/chat_bot.py">ChatBot</a></code>
- <code title="get /bots/">client.bots.<a href="./src/asktable/resources/bots.py">list</a>(\*\*<a href="src/asktable/types/bot_list_params.py">params</a>) -> <a href="./src/asktable/types/bot_list_response.py">BotListResponse</a></code>
- <code title="delete /bots/{bot_id}">client.bots.<a href="./src/asktable/resources/bots.py">delete</a>(bot_id) -> <a href="./src/asktable/types/bot_delete_response.py">object</a></code>

# Extapis

Types:

```python
from asktable.types import ExtAPIModel, ExtapiDeleteResponse
```

Methods:

- <code title="get /extapis/{extapi_id}">client.extapis.<a href="./src/asktable/resources/extapis/extapis.py">retrieve</a>(extapi_id) -> <a href="./src/asktable/types/ext_api_model.py">ExtAPIModel</a></code>
- <code title="post /extapis/{extapi_id}">client.extapis.<a href="./src/asktable/resources/extapis/extapis.py">update</a>(extapi_id, \*\*<a href="src/asktable/types/extapi_update_params.py">params</a>) -> <a href="./src/asktable/types/ext_api_model.py">ExtAPIModel</a></code>
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

# AtAuth

## Tokens

Types:

```python
from asktable.types.at_auth import TokenCreateResponse
```

Methods:

- <code title="post /at-auth/tokens">client.at_auth.tokens.<a href="./src/asktable/resources/at_auth/tokens.py">create</a>(\*\*<a href="src/asktable/types/at_auth/token_create_params.py">params</a>) -> <a href="./src/asktable/types/at_auth/token_create_response.py">object</a></code>

## Me

Types:

```python
from asktable.types.at_auth import MeRetrieveResponse
```

Methods:

- <code title="get /at-auth/me">client.at_auth.me.<a href="./src/asktable/resources/at_auth/me.py">retrieve</a>() -> <a href="./src/asktable/types/at_auth/me_retrieve_response.py">object</a></code>

# SingleTurn

## Q2a

Types:

```python
from asktable.types.single_turn import AnswerModel, Q2aListResponse
```

Methods:

- <code title="post /single-turn/q2a">client.single_turn.q2a.<a href="./src/asktable/resources/single_turn/q2a.py">create</a>(\*\*<a href="src/asktable/types/single_turn/q2a_create_params.py">params</a>) -> <a href="./src/asktable/types/single_turn/answer_model.py">AnswerModel</a></code>
- <code title="get /single-turn/q2a">client.single_turn.q2a.<a href="./src/asktable/resources/single_turn/q2a.py">list</a>(\*\*<a href="src/asktable/types/single_turn/q2a_list_params.py">params</a>) -> <a href="./src/asktable/types/single_turn/q2a_list_response.py">Q2aListResponse</a></code>

## Q2s

Types:

```python
from asktable.types.single_turn import Q2SResponse, Q2ListResponse
```

Methods:

- <code title="post /single-turn/q2s">client.single_turn.q2s.<a href="./src/asktable/resources/single_turn/q2s.py">create</a>(\*\*<a href="src/asktable/types/single_turn/q2_create_params.py">params</a>) -> <a href="./src/asktable/types/single_turn/q2_s_response.py">Q2SResponse</a></code>
- <code title="get /single-turn/q2s">client.single_turn.q2s.<a href="./src/asktable/resources/single_turn/q2s.py">list</a>(\*\*<a href="src/asktable/types/single_turn/q2_list_params.py">params</a>) -> <a href="./src/asktable/types/single_turn/q2_list_response.py">Q2ListResponse</a></code>

# Caches

Methods:

- <code title="delete /caches/{cache_id}">client.caches.<a href="./src/asktable/resources/caches.py">delete</a>(cache_id) -> None</code>
