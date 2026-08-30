---
trie_version: 0.3.0
source: tests/fixtures/xlink_project/server/routes.ts
file_fingerprint: 5f7c8c547c2bd4af0a272e28fb9d392c4be47739db6b5ff2135d16d586ac647b
last_synced_at: '2026-08-30T02:44:46Z'
defines:
- kind: constant
  qualified_name: tests/fixtures/xlink_project/server/routes:app
  lines: 4-4
- kind: constant
  qualified_name: tests/fixtures/xlink_project/server/routes:router
  lines: 5-5
- kind: function
  qualified_name: tests/fixtures/xlink_project/server/routes:setupRoutes
  lines: 7-19
  signature: function setupRoutes()
incoming_refs: 1
outgoing_refs: 0
---
<!-- trie:section symbol=tests/fixtures/xlink_project/server/routes:app fingerprint=a0616e0a7f40baacc3bfc2cf7369303b5637fbfd9fd05bbca76650490e6d905f body_fp=20ba101811a79d93ee73459df679ca3060b7268a189fb69d8304881f9f2c6878 source_ref=6cde5f7cce961957c8ac4c04e3bcbbd0c8e6697f role=config -->
Express application instance created by calling `express()`.
<!-- trie:end -->
<!-- trie:section symbol=tests/fixtures/xlink_project/server/routes:router fingerprint=b3fb52320046553d049d825f033f966c3d3175f3007a387a65685c00e5c19514 body_fp=fa30134c21d1c3529bc7e24b3f925e8f7a5f3058fa23051068cb3708b7738528 source_ref=6cde5f7cce961957c8ac4c04e3bcbbd0c8e6697f role=api -->
Express `Router` instance used to register the `/api/products` GET and POST route handlers in `setupRoutes`.
<!-- trie:end -->
<!-- trie:section symbol=tests/fixtures/xlink_project/server/routes:setupRoutes fingerprint=2d0e6bb76fd43cf31199f44ca77c6252f42189831efa3e62e2fc1d56b1f41c0e body_fp=3b65846a3dec6216f42e6d3cd399e20b6c86a7ccd02676eedcf7461bc83008c9 source_ref=6cde5f7cce961957c8ac4c04e3bcbbd0c8e6697f role=api -->
## `function setupRoutes()`

Register three Express routes: `GET /api/health` on `app`, and `GET` + `POST /api/products` on `router`.
<!-- trie:end -->