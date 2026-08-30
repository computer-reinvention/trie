---
trie_version: 0.3.0
source: server/routes.ts
file_fingerprint: 5f7c8c547c2bd4af0a272e28fb9d392c4be47739db6b5ff2135d16d586ac647b
last_synced_at: '2026-08-30T02:43:42Z'
defines:
- kind: constant
  qualified_name: server/routes:app
  lines: 4-4
- kind: constant
  qualified_name: server/routes:router
  lines: 5-5
- kind: function
  qualified_name: server/routes:setupRoutes
  lines: 7-19
  signature: function setupRoutes()
incoming_refs: 0
outgoing_refs: 0
---
<!-- trie:section symbol=server/routes:app fingerprint=a0616e0a7f40baacc3bfc2cf7369303b5637fbfd9fd05bbca76650490e6d905f body_fp=2cc6894a4c3f2f3a203d5a6c52e3b5bb36529f1be71edec2cfce22a46c7d8853 source_ref=6cde5f7cce961957c8ac4c04e3bcbbd0c8e6697f role=config -->
Express application instance initialized for request handling.

- Used by `setupRoutes()` to register the `/api/health` GET endpoint.
<!-- trie:end -->
<!-- trie:section symbol=server/routes:router fingerprint=b3fb52320046553d049d825f033f966c3d3175f3007a387a65685c00e5c19514 body_fp=6ad9b3ffd4fa279ce26eed57a84a533322d68a1341de68a58d81b24cdf49360b source_ref=6cde5f7cce961957c8ac4c04e3bcbbd0c8e6697f role=model -->
Express Router instance for handling modular route definitions.

- Used in `setupRoutes()` to attach GET and POST handlers for `/api/products`.
<!-- trie:end -->
<!-- trie:section symbol=server/routes:setupRoutes fingerprint=2d0e6bb76fd43cf31199f44ca77c6252f42189831efa3e62e2fc1d56b1f41c0e body_fp=516f81752c12ddf7fdb99b66605454bedc4a900629e4717c2c98d05c6695b694 source_ref=6cde5f7cce961957c8ac4c04e3bcbbd0c8e6697f role=entrypoint -->
## `function setupRoutes()`

Configures Express app and router with HTTP handlers for `/api/health`, `/api/products` GET, and `/api/products` POST endpoints.

- `/api/health` GET responds with `{status: "ok"}` via the app instance.
- `/api/products` GET responds with an array of product objects via the router.
- `/api/products` POST responds with `{created: true}` via the router.
<!-- trie:end -->