---
trie_version: 0.3.0
source: server/gateway.ts
file_fingerprint: f549671abc8ac14d53f48029315aad6b7a1e51eba7f3b30ec1a4f9e35f511502
last_synced_at: '2026-08-30T02:43:36Z'
defines:
- kind: constant
  qualified_name: server/gateway:app
  lines: 5-5
- kind: function
  qualified_name: server/gateway:setupGateway
  lines: 9-22
  signature: function setupGateway()
- kind: function
  qualified_name: server/gateway:checkHealth
  lines: 24-28
  signature: async function checkHealth()
incoming_refs: 0
outgoing_refs: 0
---
<!-- trie:section symbol=server/gateway:app fingerprint=a0616e0a7f40baacc3bfc2cf7369303b5637fbfd9fd05bbca76650490e6d905f body_fp=5a40ed5732b60a1241e67e5d8dfc345849a1736705377ab9281f37543728f52e source_ref=6ae5d64625b167c05be7a9fdb08add267f293139 role=model -->
Express application instance used to configure server routes.

- `setupGateway()` registers `/api/gateway/status` and `/api/gateway/users` endpoints on this instance.
<!-- trie:end -->
<!-- trie:section symbol=server/gateway:setupGateway fingerprint=9a15ef17f45f14b46e30fe223657e18cc3189b1179f0f11d17f2031b75cbd298 body_fp=267750e3ed5a3ce8547259039e47e658c2f5689ccaeed04fdae4d1a7f3dea161 source_ref=6ae5d64625b167c05be7a9fdb08add267f293139 role=entrypoint -->
## `function setupGateway()`

Registers Express routes for a gateway service: `/api/gateway/status` responds with running status; `/api/gateway/users` proxies upstream `/api/users` requests.

- Both routes attached to the shared `app` Express instance at module level.
<!-- trie:end -->
<!-- trie:section symbol=server/gateway:checkHealth fingerprint=54ddfd86464e86de0cca506df689834fcaf06fa0735ba69aace4d6793162a6d2 body_fp=10ad5e274593711520994a290f2902cb8e5e189e13b4179756082327c2e1f464 source_ref=6ae5d64625b167c05be7a9fdb08add267f293139 role=io -->
## `async function checkHealth()`

Fetches the health status from an upstream `/api/health` endpoint and returns the parsed JSON response.

- Returns parsed JSON from the health check endpoint.
<!-- trie:end -->