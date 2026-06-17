---
trie_version: 0.1.9
source: app/electron/opencode-config.test.ts
file_fingerprint: 8c4f65829e6ab41418f225fd9a41759feb4c47ea483d113bafc7df5ccd24703a
last_synced_at: '2026-06-17T16:35:03Z'
defines:
- kind: module
  qualified_name: app/electron/opencode-config.test:__module__
  lines: 1-138
- kind: constant
  qualified_name: app/electron/opencode-config.test:TRIE
  lines: 4-4
incoming_refs: 0
outgoing_refs: 0
---
<!-- trie:section symbol=app/electron/opencode-config.test:__module__ fingerprint=1a9d4252551e79003d339c370fc4ef9ba9ca47b5ddde7b40aee6f58025d01443 body_fp=8cf9b1abd03547d210fa823b6946c1ed71f010f1587d8b14c5576ee9cfc90322 source_ref=22cac5b14e18082756e58daea68d8ff30cccb8ad role=test -->
Test suite for `deepMerge`, `withTrieMcp`, and `parseTolerant` from `opencode-config`.

- `deepMerge`: verifies key preservation, nested-object merging, array replacement, null-deletion, scalar-over-object replacement, immutability, and missing-key creation.
- `withTrieMcp`: verifies trie MCP injection, preservation of other servers, overwrite of stale entries, and input immutability.
- `parseTolerant`: verifies plain JSON, line/block comment stripping, trailing-comma tolerance, graceful fallback to `{}`, and correct URL `//` handling.
<!-- trie:end -->
<!-- trie:section symbol=app/electron/opencode-config.test:TRIE fingerprint=e301489591c7f54d3236aef9aee81419d2982eec3d0fa9ab8935c687eb201425 body_fp=28ec8b2fb1b7d60a6d70c71ca6dd70810cee291ce4b0be8ca53274d3f89abd71 source_ref=22cac5b14e18082756e58daea68d8ff30cccb8ad role=test -->
Shared test fixture supplying a `trieMcpBin` path and `projectDir` to `withTrieMcp` calls across all test suites.
<!-- trie:end -->