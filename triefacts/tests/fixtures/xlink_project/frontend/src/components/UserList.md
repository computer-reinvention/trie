---
trie_version: 0.3.0
source: tests/fixtures/xlink_project/frontend/src/components/UserList.tsx
file_fingerprint: 05b37d36b93e4af8e3f258269e3c383315442fc28d78376d61bedd2172c5d681
last_synced_at: '2026-08-30T02:44:34Z'
defines:
- kind: function
  qualified_name: tests/fixtures/xlink_project/frontend/src/components/UserList:fetchUsers
  lines: 3-6
  signature: async function fetchUsers()
- kind: function
  qualified_name: tests/fixtures/xlink_project/frontend/src/components/UserList:fetchUserById
  lines: 8-11
  signature: 'async function fetchUserById(userId: string)'
- kind: function
  qualified_name: tests/fixtures/xlink_project/frontend/src/components/UserList:createUser
  lines: 13-19
  signature: 'async function createUser(data: any)'
- kind: function
  qualified_name: tests/fixtures/xlink_project/frontend/src/components/UserList:deleteUser
  lines: 21-26
  signature: 'async function deleteUser(userId: string)'
incoming_refs: 0
outgoing_refs: 4
---
<!-- trie:section symbol=tests/fixtures/xlink_project/frontend/src/components/UserList:fetchUsers fingerprint=dc56a9b803234d75d7995b863c866a725fbd3c2417a2718c22de20ea784c5427 body_fp=b87d60781a87763d8e217672285104f1dc293004cad159de42da96452e938a6c source_ref=cb60f0297244bc7ef7cca06a592479d648ef4543 role=io -->
## `async function fetchUsers()`

Fetch all users from `/api/users` and return the parsed JSON response.
<!-- trie:end -->
<!-- trie:section symbol=tests/fixtures/xlink_project/frontend/src/components/UserList:fetchUserById fingerprint=0e41874c1beb3d1d1f79d465d4e9b1d77a5357c2262c5b23ff4a1f56bb2a63c3 body_fp=62ff06817ded5bf63fae1d146d889d38a243438f9df772f084d0021029d06cd5 source_ref=cb60f0297244bc7ef7cca06a592479d648ef4543 role=io -->
## `async function fetchUserById(userId: string)`

Fetch a single user by ID from `/api/users/{userId}` and return the parsed JSON response.
<!-- trie:end -->
<!-- trie:section symbol=tests/fixtures/xlink_project/frontend/src/components/UserList:createUser fingerprint=d918a3d57f001243a07e21027003b6b76d6869b838f376140103f578d3606bfb body_fp=cb3213be1b5bd23bea719ec29e3670bcc12e2f6862efd47e126d3dfafe3aabcc source_ref=cb60f0297244bc7ef7cca06a592479d648ef4543 role=io -->
## `async function createUser(data: any)`

POST a new user to `/api/users` by serializing `data` as JSON and returning the parsed response.

- `data` — arbitrary object serialized via `JSON.stringify` as the request body.
<!-- trie:end -->
<!-- trie:section symbol=tests/fixtures/xlink_project/frontend/src/components/UserList:deleteUser fingerprint=0651d4d3032e6b684727a7ed90cb4c450b810111c59accf4a7e5aea3552d4019 body_fp=bb8f79cb873aa88eaa6bd59200455d77a9b0556f424d6df0c6d47c4abacdf729 source_ref=cb60f0297244bc7ef7cca06a592479d648ef4543 role=io -->
## `async function deleteUser(userId: string)`

Send a DELETE request to `/api/users/{userId}` and return the parsed JSON response.
<!-- trie:end -->