---
trie_version: 0.1.9
source: app/electron/trie-config.test.ts
file_fingerprint: dd2d18cf11f694d228ad053dd7cf3e64fd8456cad974682c15b4142e43d64ade
last_synced_at: '2026-06-17T16:35:11Z'
defines:
- kind: module
  qualified_name: app/electron/trie-config.test:__module__
  lines: 1-67
incoming_refs: 0
outgoing_refs: 0
---
<!-- trie:section symbol=app/electron/trie-config.test:__module__ fingerprint=3e0324aee98f906f327e8b75e4f045859d6a5790a7bf7024fc6ee389c158ba50 body_fp=6e96274ce1c98b35e769c4f19664a6637f142fa74264d0ff02045e623b868b41 source_ref=79308c11f935e564c71572556d3d3f23634f635e role=test -->
Vitest test suite for `trie-config` utilities: `deepMerge`, `stripUndefined`, and `isPlainObject`.

- `deepMerge`: covers nested merge, array replacement, null-key deletion, key preservation, and immutability.
- `stripUndefined`: covers recursive object stripping, array recursion, and scalar pass-through.
- `isPlainObject`: covers discrimination between plain objects, arrays, null, and primitives.
<!-- trie:end -->