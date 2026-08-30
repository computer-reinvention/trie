---
trie_version: 0.3.0
source: tests/fixtures/xlink_project/server/gateway.ts
file_fingerprint: f549671abc8ac14d53f48029315aad6b7a1e51eba7f3b30ec1a4f9e35f511502
last_synced_at: '2026-08-30T02:44:41Z'
defines:
- kind: constant
  qualified_name: tests/fixtures/xlink_project/server/gateway:app
  lines: 5-5
- kind: function
  qualified_name: tests/fixtures/xlink_project/server/gateway:setupGateway
  lines: 9-22
  signature: function setupGateway()
- kind: function
  qualified_name: tests/fixtures/xlink_project/server/gateway:checkHealth
  lines: 24-28
  signature: async function checkHealth()
incoming_refs: 0
outgoing_refs: 2
---
<!-- trie:section symbol=tests/fixtures/xlink_project/server/gateway:app fingerprint=a0616e0a7f40baacc3bfc2cf7369303b5637fbfd9fd05bbca76650490e6d905f body_fp=d009e9d9d8025cf83f4764dfe4a3ff67e3051a9ea6fe0bd4b21ebc4dede8b5a8 source_ref=6ae5d64625b167c05be7a9fdb08add267f293139 role=config -->
Express application instance created by calling `express()` and used throughout the module to register gateway route handlers.
<!-- trie:end -->
<!-- trie:section symbol=tests/fixtures/xlink_project/server/gateway:setupGateway fingerprint=9a15ef17f45f14b46e30fe223657e18cc3189b1179f0f11d17f2031b75cbd298 body_fp=148558a76c61f8c5f8545cf86bd53c334e43b531763b30a1e33f6674454bf4e8 source_ref=6ae5d64625b167c05be7a9fdb08add267f293139 role=api -->
## `function setupGateway()`

Register two Express routes on the shared `app` instance: a status endpoint and a proxying users endpoint that fetches from an upstream service.

- `GET /api/gateway/status` — responds with `{ gateway: "running" }`.
- `GET /api/gateway/users` — fetches `/api/users` upstream and streams the JSON response to the client.
<!-- trie:end -->
<!-- trie:section symbol=tests/fixtures/xlink_project/server/gateway:checkHealth fingerprint=54ddfd86464e86de0cca506df689834fcaf06fa0735ba69aace4d6793162a6d2 body_fp=025c2a1d565af0090780f602ea232534d137af3476a41ede1eefba55186800a0 source_ref=6ae5d64625b167c05be7a9fdb08add267f293139 role=io -->
## `async function checkHealth()`

Fetches `/api/health` via HTTP and returns the parsed JSON response body.
<!-- trie:end -->