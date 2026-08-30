---
trie_version: 0.3.0
source: tests/fixtures/xlink_project/backend/api/users.py
file_fingerprint: 51d682519489597754a943148994a9f713860e969d8df1923e9fff885cd379cc
last_synced_at: '2026-08-30T02:44:21Z'
defines:
- kind: constant
  qualified_name: tests/fixtures/xlink_project/backend/api/users:app
  lines: 4-4
- kind: function
  qualified_name: tests/fixtures/xlink_project/backend/api/users:list_users
  lines: 8-9
  signature: def list_users()
- kind: function
  qualified_name: tests/fixtures/xlink_project/backend/api/users:get_user
  lines: 13-14
  signature: 'def get_user(user_id: str)'
- kind: function
  qualified_name: tests/fixtures/xlink_project/backend/api/users:create_user
  lines: 18-19
  signature: 'def create_user(data: dict)'
- kind: function
  qualified_name: tests/fixtures/xlink_project/backend/api/users:delete_user
  lines: 23-24
  signature: 'def delete_user(user_id: str)'
incoming_refs: 5
outgoing_refs: 0
---
<!-- trie:section symbol=tests/fixtures/xlink_project/backend/api/users:app fingerprint=e420f46726c1947303a91b1e39f24b503aa1867b05425b6e48b46a4d54459432 body_fp=8cc3837d065182e76553bd631fc794574a0506a07cf0064261e8d71a13bc7e90 source_ref=8a01d3fb56ff193b1bff543483411271b8308be7 role=config -->
FastAPI application instance that mounts all `/api/users` route handlers in this module.
<!-- trie:end -->
<!-- trie:section symbol=tests/fixtures/xlink_project/backend/api/users:list_users fingerprint=21ea83739d12078e51aa68cfe6485f0c389ef8b1ee22a53bbf4cbdfab3e319b1 body_fp=8cc00d2628e6bafd40c4a90c8767af87d403bb1f960c6d9d30f644895f66da88 source_ref=8a01d3fb56ff193b1bff543483411271b8308be7 role=api -->
## `def list_users()`

FastAPI GET handler for `/api/users` that returns a hardcoded list of user dicts.
<!-- trie:end -->
<!-- trie:section symbol=tests/fixtures/xlink_project/backend/api/users:get_user fingerprint=b7eeff39727fc94b7de944708105f5d350f73271cc2f223458d9f1103f6b817a body_fp=61aa546e1a3ec9593974757b708c09f1fbd9183925e250b42097fdf6f2228e49 source_ref=8a01d3fb56ff193b1bff543483411271b8308be7 role=api -->
## `def get_user(user_id: str)`

FastAPI GET handler that returns a user record for the given `user_id`.

- `user_id`: path parameter extracted from `/api/users/{user_id}`; used as the `id` field in the response.
<!-- trie:end -->
<!-- trie:section symbol=tests/fixtures/xlink_project/backend/api/users:create_user fingerprint=f05f03b93453a59007460957ab7b96d1a5b5863817f85bd40b7fc23a78b43980 body_fp=eec1335b494d95fe942a93677effe01e55b1ef2255ee31ffa2244f2abfb1350c source_ref=8a01d3fb56ff193b1bff543483411271b8308be7 role=api -->
## `def create_user(data: dict)`

FastAPI `POST /api/users` handler that returns a new user dict with a hardcoded `id` of `2` merged with the request body.

- `data`: raw request body dict spread into the response payload.
<!-- trie:end -->
<!-- trie:section symbol=tests/fixtures/xlink_project/backend/api/users:delete_user fingerprint=5a639b669f8c472396406ef89f7e05cca52c3ce69d5ec12f524182aa391b5dc1 body_fp=3feca1e0f16c2ca74265630d44605c6a74826e1a144d917afa5cc10d64e2cc34 source_ref=8a01d3fb56ff193b1bff543483411271b8308be7 role=api -->
## `def delete_user(user_id: str)`

FastAPI DELETE handler for `/api/users/{user_id}` that returns the deleted user's ID.

- `user_id`: path parameter identifying the user to delete.
<!-- trie:end -->