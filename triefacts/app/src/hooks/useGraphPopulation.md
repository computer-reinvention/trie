---
trie_version: 0.1.9
source: app/src/hooks/useGraphPopulation.ts
file_fingerprint: 03d6f33406251f0501b095065bdd7fc8ff594549be82644640af3620bba9534d
last_synced_at: '2026-06-17T16:39:12Z'
defines:
- kind: function
  qualified_name: app/src/hooks/useGraphPopulation:useGraphPopulation
  lines: 17-89
incoming_refs: 1
outgoing_refs: 8
---
<!-- trie:section symbol=app/src/hooks/useGraphPopulation:useGraphPopulation fingerprint=f0256faa9d378420dd0a44e7b40ae9397448c2a168b15f4feffdf3edbacb098e body_fp=dc3db69ffcb8dd2845856fd826647205b9d2c96bd48b3f4e1433d7bd48cd992a source_ref=5343691b960c748afdbe70bff8f95e0bd2a2fce2 role=orchestration -->
Fetch the system model and all edges from the graph API on mount, populate graph and AGM stores, and return a `repopulate` callback for forced re-fetches.

- `opencodePort` — skips fetch and effect when `null`; acts as the key dep for re-running
- `repopulate` — calls `populate()` without a cancellation ref; used by the startup-refresh flow after a rebuild
- Empty model response is treated as a non-fatal transient state; loading spinner is left active
<!-- trie:end -->