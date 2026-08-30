---
trie_version: 0.3.0
source: backend/api/users.py
file_fingerprint: 51d682519489597754a943148994a9f713860e969d8df1923e9fff885cd379cc
last_synced_at: '2026-08-30T02:43:19Z'
defines:
- kind: constant
  qualified_name: backend/api/users:app
  lines: 4-4
- kind: function
  qualified_name: backend/api/users:list_users
  lines: 8-9
  signature: def list_users()
- kind: function
  qualified_name: backend/api/users:get_user
  lines: 13-14
  signature: 'def get_user(user_id: str)'
- kind: function
  qualified_name: backend/api/users:create_user
  lines: 18-19
  signature: 'def create_user(data: dict)'
- kind: function
  qualified_name: backend/api/users:delete_user
  lines: 23-24
  signature: 'def delete_user(user_id: str)'
incoming_refs: 0
outgoing_refs: 0
---
<!-- trie:section symbol=backend/api/users:app fingerprint=e420f46726c1947303a91b1e39f24b503aa1867b05425b6e48b46a4d54459432 body_fp=24d1b98d58d12e07ecb76528589e0dde9421741cafe5081c64af645c81f7c4ae source_ref=8a01d3fb56ff193b1bff543483411271b8308be7 role=entrypoint -->
Initializes the FastAPI application instance for the users API module.
<!-- trie:end -->
<!-- trie:section symbol=backend/api/users:list_users fingerprint=21ea83739d12078e51aa68cfe6485f0c389ef8b1ee22a53bbf4cbdfab3e319b1 body_fp=61728e1d1c887526456ed1c3918c317fe4d0eb5f33d59e0fb4c0adef85c0b366 source_ref=8a01d3fb56ff193b1bff543483411271b8308be7 role=api -->
## `def list_users()`

Returns a list of all user objects; handles GET requests to `/api/users`.
<!-- trie:end -->
<!-- trie:section symbol=backend/api/users:get_user fingerprint=b7eeff39727fc94b7de944708105f5d350f73271cc2f223458d9f1103f6b817a body_fp=8aaee1c5b8d0e89fbd0df49e65eef6c5da0b014b0d8e40a8f77ce78e42eef73c source_ref=8a01d3fb56ff193b1bff543483411271b8308be7 role=api -->
## `def get_user(user_id: str)`

FastAPI route handler that retrieves a single user by ID.

- `user_id`: path parameter extracted from the URL route.
<!-- trie:end -->
<!-- trie:section symbol=backend/api/users:create_user fingerprint=f05f03b93453a59007460957ab7b96d1a5b5863817f85bd40b7fc23a78b43980 body_fp=b905f8f9f1a0e286e7d7c340240f1960933d5caadf0ba700cd3fe9b223348802 source_ref=8a01d3fb56ff193b1bff543483411271b8308be7 role=api -->
## `def create_user(data: dict)`

Creates a new user record and returns it with an assigned ID.

- `data`: dictionary containing user attributes to merge into the response.
<!-- trie:end -->
<!-- trie:section symbol=backend/api/users:delete_user fingerprint=5a639b669f8c472396406ef89f7e05cca52c3ce69d5ec12f524182aa391b5dc1 body_fp=a5dc391106a653a2035a06c7d3a15f776bfe7dc4a1d90e2703032e888ad0fd63 source_ref=8a01d3fb56ff193b1bff543483411271b8308be7 role=api -->
## `def delete_user(user_id: str)`

Deletes a user by ID and returns a confirmation object containing the deleted user's ID.

- `user_id`: path parameter identifying the user to delete
<!-- trie:end -->