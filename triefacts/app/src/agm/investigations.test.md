---
trie_version: 0.1.9
source: app/src/agm/investigations.test.ts
file_fingerprint: 2d4760f7169bda3fdb3500317f49a8f91bf3bb2ffabd61c0bf8a49499ee401f6
last_synced_at: '2026-06-17T16:35:30Z'
defines:
- kind: module
  qualified_name: app/src/agm/investigations.test:__module__
  lines: 1-79
incoming_refs: 0
outgoing_refs: 0
---
<!-- trie:section symbol=app/src/agm/investigations.test:__module__ fingerprint=0a3a9079a06937a5f17d1841c058b1c9fffa0ba6902d9b5f68f254e001b52a58 body_fp=c9d20c08ad28eb112ba2846ddb928e3feb8e0596ee5a3186780c7dbb956e0ade source_ref=d4d6112c549dea6fb5ef4fceda0e460784c78150 role=test -->
Tests `concentration` and `InvestigationRegistry` from `./investigations`, covering confidence scoring and investigation lifecycle management.

- `concentration` suite: verifies 0 on empty map, 1 on single-symbol map, near-0 on uniform spread, and monotonic rise as attention narrows.
- `InvestigationRegistry` suite: verifies open/track, resolved-status clears active, multi-id storage, negative evidence recording, and confidence+scope update from attention mass.
<!-- trie:end -->