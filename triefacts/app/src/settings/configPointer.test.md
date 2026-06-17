---
trie_version: 0.1.9
source: app/src/settings/configPointer.test.ts
file_fingerprint: 4030c763debba1c466df0ca27cd0e9841855979cc9e95e6ed810574fdd499105
last_synced_at: '2026-06-17T16:39:31Z'
defines:
- kind: module
  qualified_name: app/src/settings/configPointer.test:__module__
  lines: 1-83
incoming_refs: 0
outgoing_refs: 0
---
<!-- trie:section symbol=app/src/settings/configPointer.test:__module__ fingerprint=fe32f9823233ab6cae054dc4e9f2ce2a52572d13e6451f5f16f22d5f87329c74 body_fp=8db8473de87038757671e9ad694a27fb33c9eeecd459a1d376ebd41ef30beaf0 source_ref=1c9b276a92773a3f557ceace4e6ce811f72acd57 role=test -->
Vitest test suite covering `getPointer`, `setPointer`, and `buildManagedDelta` from `configPointer`.

- `getPointer`: verifies scalar reads, nested dot-path traversal, missing paths, and array non-descent.
- `setPointer`: verifies top-level sets, intermediate object creation, sibling preservation, `undefined` deletion, non-object overwrite, and round-trip with `getPointer`.
- `buildManagedDelta`: verifies present-key passthrough, absent-key nulling, and exclusion of unmanaged keys.
<!-- trie:end -->