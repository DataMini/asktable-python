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
    Project,
    ProjectExportResponse,
    ProjectImportResponse,
    ProjectModelGroupsResponse,
)
```

Methods:

- <code title="post /v1/sys/projects">client.sys.projects.<a href="./src/asktable/resources/sys/projects/projects.py">create</a>(\*\*<a href="src/asktable/types/sys/project_create_params.py">params</a>) -> <a href="./src/asktable/types/sys/project.py">Project</a></code>
- <code title="get /v1/sys/projects/{project_id}">client.sys.projects.<a href="./src/asktable/resources/sys/projects/projects.py">retrieve</a>(project_id) -> <a href="./src/asktable/types/sys/project.py">Project</a></code>
- <code title="patch /v1/sys/projects/{project_id}">client.sys.projects.<a href="./src/asktable/resources/sys/projects/projects.py">update</a>(project_id, \*\*<a href="src/asktable/types/sys/project_update_params.py">params</a>) -> <a href="./src/asktable/types/sys/project.py">Project</a></code>
- <code title="get /v1/sys/projects">client.sys.projects.<a href="./src/asktable/resources/sys/projects/projects.py">list</a>(\*\*<a href="src/asktable/types/sys/project_list_params.py">params</a>) -> <a href="./src/asktable/types/sys/project.py">SyncPage[Project]</a></code>
- <code title="delete /v1/sys/projects/{project_id}">client.sys.projects.<a href="./src/asktable/resources/sys/projects/projects.py">delete</a>(project_id) -> object</code>
- <code title="post /v1/sys/projects/{project_id}/export">client.sys.projects.<a href="./src/asktable/resources/sys/projects/projects.py">export</a>(project_id) -> <a href="./src/asktable/types/sys/project_export_response.py">ProjectExportResponse</a></code>
- <code title="post /v1/sys/projects/import">client.sys.projects.<a href="./src/asktable/resources/sys/projects/projects.py">import\_</a>(\*\*<a href="src/asktable/types/sys/project_import_params.py">params</a>) -> <a href="./src/asktable/types/sys/project_import_response.py">ProjectImportResponse</a></code>
- <code title="get /v1/sys/projects/model-groups">client.sys.projects.<a href="./src/asktable/resources/sys/projects/projects.py">model_groups</a>() -> <a href="./src/asktable/types/sys/project_model_groups_response.py">ProjectModelGroupsResponse</a></code>

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

- <code title="post /v1/sys/projects/{project_id}/api-keys">client.sys.projects.api_keys.<a href="./src/asktable/resources/sys/projects/api_keys.py">create</a>(project_id, \*\*<a href="src/asktable/types/sys/projects/api_key_create_params.py">params</a>) -> <a href="./src/asktable/types/sys/projects/api_key_create_response.py">APIKeyCreateResponse</a></code>
- <code title="get /v1/sys/projects/{project_id}/api-keys">client.sys.projects.api_keys.<a href="./src/asktable/resources/sys/projects/api_keys.py">list</a>(project_id) -> <a href="./src/asktable/types/sys/projects/api_key_list_response.py">APIKeyListResponse</a></code>
- <code title="delete /v1/sys/projects/{project_id}/api-keys/{key_id}">client.sys.projects.api_keys.<a href="./src/asktable/resources/sys/projects/api_keys.py">delete</a>(key_id, \*, project_id) -> None</code>
- <code title="post /v1/sys/projects/{project_id}/tokens">client.sys.projects.api_keys.<a href="./src/asktable/resources/sys/projects/api_keys.py">create_token</a>(project_id, \*\*<a href="src/asktable/types/sys/projects/api_key_create_token_params.py">params</a>) -> <a href="./src/asktable/types/sys/projects/api_key_create_token_response.py">APIKeyCreateTokenResponse</a></code>

# Roles

Types:

```python
from asktable.types import Role
```

# Datasources

Types:

```python
from asktable.types import (
    Datasource,
    Index,
    Meta,
    DatasourceRetrieveResponse,
    DatasourceRetrieveRuntimeMetaResponse,
)
```

Methods:

- <code title="post /v1/datasources">client.datasources.<a href="./src/asktable/resources/datasources/datasources.py">create</a>(\*\*<a href="src/asktable/types/datasource_create_params.py">params</a>) -> <a href="./src/asktable/types/datasource.py">Datasource</a></code>
- <code title="get /v1/datasources/{datasource_id}">client.datasources.<a href="./src/asktable/resources/datasources/datasources.py">retrieve</a>(datasource_id) -> <a href="./src/asktable/types/datasource_retrieve_response.py">DatasourceRetrieveResponse</a></code>
- <code title="patch /v1/datasources/{datasource_id}">client.datasources.<a href="./src/asktable/resources/datasources/datasources.py">update</a>(datasource_id, \*\*<a href="src/asktable/types/datasource_update_params.py">params</a>) -> <a href="./src/asktable/types/datasource.py">Datasource</a></code>
- <code title="get /v1/datasources">client.datasources.<a href="./src/asktable/resources/datasources/datasources.py">list</a>(\*\*<a href="src/asktable/types/datasource_list_params.py">params</a>) -> <a href="./src/asktable/types/datasource.py">SyncPage[Datasource]</a></code>
- <code title="delete /v1/datasources/{datasource_id}">client.datasources.<a href="./src/asktable/resources/datasources/datasources.py">delete</a>(datasource_id) -> object</code>
- <code title="post /v1/datasources/{datasource_id}/files">client.datasources.<a href="./src/asktable/resources/datasources/datasources.py">add_file</a>(datasource_id, \*\*<a href="src/asktable/types/datasource_add_file_params.py">params</a>) -> object</code>
- <code title="delete /v1/datasources/{datasource_id}/files/{file_id}">client.datasources.<a href="./src/asktable/resources/datasources/datasources.py">delete_file</a>(file_id, \*, datasource_id) -> object</code>
- <code title="get /v1/datasources/{datasource_id}/runtime-meta">client.datasources.<a href="./src/asktable/resources/datasources/datasources.py">retrieve_runtime_meta</a>(datasource_id) -> <a href="./src/asktable/types/datasource_retrieve_runtime_meta_response.py">DatasourceRetrieveRuntimeMetaResponse</a></code>
- <code title="patch /v1/datasources/{datasource_id}/field">client.datasources.<a href="./src/asktable/resources/datasources/datasources.py">update_field</a>(datasource_id, \*\*<a href="src/asktable/types/datasource_update_field_params.py">params</a>) -> object</code>

## Meta

Methods:

- <code title="post /v1/datasources/{datasource_id}/meta">client.datasources.meta.<a href="./src/asktable/resources/datasources/meta.py">create</a>(datasource_id, \*\*<a href="src/asktable/types/datasources/meta_create_params.py">params</a>) -> object</code>
- <code title="get /v1/datasources/{datasource_id}/meta">client.datasources.meta.<a href="./src/asktable/resources/datasources/meta.py">retrieve</a>(datasource_id) -> <a href="./src/asktable/types/meta.py">Meta</a></code>
- <code title="put /v1/datasources/{datasource_id}/meta">client.datasources.meta.<a href="./src/asktable/resources/datasources/meta.py">update</a>(datasource_id, \*\*<a href="src/asktable/types/datasources/meta_update_params.py">params</a>) -> object</code>
- <code title="patch /v1/datasources/{datasource_id}/meta">client.datasources.meta.<a href="./src/asktable/resources/datasources/meta.py">annotate</a>(datasource_id, \*\*<a href="src/asktable/types/datasources/meta_annotate_params.py">params</a>) -> object</code>

## UploadParams

Types:

```python
from asktable.types.datasources import UploadParamCreateResponse
```

Methods:

- <code title="post /v1/datasources/upload_params">client.datasources.upload_params.<a href="./src/asktable/resources/datasources/upload_params.py">create</a>(\*\*<a href="src/asktable/types/datasources/upload_param_create_params.py">params</a>) -> <a href="./src/asktable/types/datasources/upload_param_create_response.py">UploadParamCreateResponse</a></code>

## Indexes

Methods:

- <code title="post /v1/datasources/{ds_id}/indexes">client.datasources.indexes.<a href="./src/asktable/resources/datasources/indexes.py">create</a>(ds_id, \*\*<a href="src/asktable/types/datasources/index_create_params.py">params</a>) -> object</code>
- <code title="get /v1/datasources/{ds_id}/indexes">client.datasources.indexes.<a href="./src/asktable/resources/datasources/indexes.py">list</a>(ds_id, \*\*<a href="src/asktable/types/datasources/index_list_params.py">params</a>) -> <a href="./src/asktable/types/index.py">SyncPage[Index]</a></code>
- <code title="delete /v1/datasources/{ds_id}/indexes/{index_id}">client.datasources.indexes.<a href="./src/asktable/resources/datasources/indexes.py">delete</a>(index_id, \*, ds_id) -> object</code>

# Auth

Types:

```python
from asktable.types import AuthCreateTokenResponse, AuthMeResponse
```

Methods:

- <code title="post /v1/auth/tokens">client.auth.<a href="./src/asktable/resources/auth.py">create_token</a>(\*\*<a href="src/asktable/types/auth_create_token_params.py">params</a>) -> <a href="./src/asktable/types/auth_create_token_response.py">AuthCreateTokenResponse</a></code>
- <code title="get /v1/auth/me">client.auth.<a href="./src/asktable/resources/auth.py">me</a>() -> <a href="./src/asktable/types/auth_me_response.py">AuthMeResponse</a></code>

# Integration

Methods:

- <code title="post /v1/integration/excel_csv_ask">client.integration.<a href="./src/asktable/resources/integration.py">excel_csv_ask</a>(\*\*<a href="src/asktable/types/integration_excel_csv_ask_params.py">params</a>) -> object</code>

# Project

Types:

```python
from asktable.types import ProjectListModelGroupsResponse
```

Methods:

- <code title="get /v1/project">client.project.<a href="./src/asktable/resources/project.py">retrieve</a>() -> <a href="./src/asktable/types/sys/project.py">Project</a></code>
- <code title="patch /v1/project">client.project.<a href="./src/asktable/resources/project.py">update</a>(\*\*<a href="src/asktable/types/project_update_params.py">params</a>) -> <a href="./src/asktable/types/sys/project.py">Project</a></code>
- <code title="get /v1/project/model-groups">client.project.<a href="./src/asktable/resources/project.py">list_model_groups</a>() -> <a href="./src/asktable/types/project_list_model_groups_response.py">ProjectListModelGroupsResponse</a></code>

# Scores

Methods:

- <code title="post /v1/score">client.scores.<a href="./src/asktable/resources/scores.py">create</a>(\*\*<a href="src/asktable/types/score_create_params.py">params</a>) -> object</code>

# Files

Methods:

- <code title="get /v1/files/{file_id}">client.files.<a href="./src/asktable/resources/files.py">retrieve</a>(file_id) -> object</code>

# Dataframes

Types:

```python
from asktable.types import DataframeRetrieveResponse
```

Methods:

- <code title="get /v1/dataframes/{dataframe_id}">client.dataframes.<a href="./src/asktable/resources/dataframes.py">retrieve</a>(dataframe_id) -> <a href="./src/asktable/types/dataframe_retrieve_response.py">DataframeRetrieveResponse</a></code>

# Polish

Types:

```python
from asktable.types import PolishCreateResponse
```

Methods:

- <code title="post /v1/polish">client.polish.<a href="./src/asktable/resources/polish.py">create</a>(\*\*<a href="src/asktable/types/polish_create_params.py">params</a>) -> <a href="./src/asktable/types/polish_create_response.py">PolishCreateResponse</a></code>

# User

## Projects

Types:

```python
from asktable.types.user import ProjectRetrieveModelGroupsResponse
```

Methods:

- <code title="get /v1/user/projects/model-groups">client.user.projects.<a href="./src/asktable/resources/user/projects.py">retrieve_model_groups</a>() -> <a href="./src/asktable/types/user/project_retrieve_model_groups_response.py">ProjectRetrieveModelGroupsResponse</a></code>
- <code title="get /v1/user/projects">client.user.projects.<a href="./src/asktable/resources/user/projects.py">retrieve_my_project</a>() -> <a href="./src/asktable/types/sys/project.py">Project</a></code>
- <code title="patch /v1/user/projects">client.user.projects.<a href="./src/asktable/resources/user/projects.py">update_my_project</a>(\*\*<a href="src/asktable/types/user/project_update_my_project_params.py">params</a>) -> <a href="./src/asktable/types/sys/project.py">Project</a></code>
