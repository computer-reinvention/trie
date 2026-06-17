---
trie_version: 0.1.9
source: app/src/settings/opencodeSchema.test.ts
file_fingerprint: fabd49c7d06dda29e1d2e051741718fe72414881eec966cd860747bcbbebf8c1
last_synced_at: '2026-06-17T16:39:35Z'
defines:
- kind: module
  qualified_name: app/src/settings/opencodeSchema.test:__module__
  lines: 1-65
incoming_refs: 0
outgoing_refs: 0
---
<!-- trie:section symbol=app/src/settings/opencodeSchema.test:__module__ fingerprint=882b1148f6e16cbd1824850a1c2c0699dea8a77553dedec404c206ea53b1a6ea body_fp=11cfbc9cc543c17cfbf975c7436193004059473782bb5b42d79c21a7a044920a source_ref=5cf1d05d7450121eb1d52c9afacc635da7a8069a role=test -->
Tests `defaultEnvVar`, `MANAGED_TOP_KEYS`, `OC_FIELDS`, and `ocFieldByPointer` from `opencodeSchema`.

- Verifies known providers map to canonical env vars and unknown providers are normalised.
- Asserts `MANAGED_TOP_KEYS` is deduplicated, contains core config keys, and excludes TUI-only/deprecated keys.
- Checks `OC_FIELDS` has unique pointers and that enum fields declare at least one option.
- Confirms `ocFieldByPointer` resolves known pointers and returns `undefined` for missing ones.
<!-- trie:end -->