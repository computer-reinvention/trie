---
trie_version: 0.1.2
source: trie/sync/reconcile.py
file_fingerprint: f08a21b3a2d39b28de540438b9631c2a6351b6e31b3d79bce8e05db59874a525
last_synced_at: '2026-05-23T23:54:45Z'
defines:
- kind: module
  qualified_name: trie/sync/reconcile:__module__
  lines: 1-61
- kind: function
  qualified_name: trie/sync/reconcile:find_orphan_triefacts
  lines: 10-52
- kind: function
  qualified_name: trie/sync/reconcile:remove_orphan_triefacts
  lines: 55-60
incoming_refs: 7
outgoing_refs: 2
---
<!-- trie:section symbol=trie/sync/reconcile:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=6653af51b1a57682f49e11bdde7158487e8343ff97d190126fca9631575a4d78 source_ref=9e576c94de69bc9bed35694ec4c6df87791394e6 -->
## `trie/sync/reconcile`

Detect and remove orphaned trie-owned triefact files whose source symbols no longer exist.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/reconcile:find_orphan_triefacts fingerprint=1686ac04fded14fddb1a9d3afda81e606cd9888e30673c180ed639f49c233d10 body_fp=f3681274c370493fb3f337205e45cada89f8397a57546f5fb5ad594fba0908c4 source_ref=9e576c94de69bc9bed35694ec4c6df87791394e6 -->
## `find_orphan_triefacts(*, project_root: Path, config: Config) -> list[Path]`

Return absolute paths of trie-owned triefact files whose corresponding source `.py` file no longer exists in scope.

- `project_root`: resolved to absolute before use
- Only `.md` files with `trie_version` in YAML front-matter are considered trie-owned; hand-authored files are skipped
- Triefact tree mirrors source tree: `triefacts/foo/bar.md` maps to `foo/bar.py`
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/reconcile:remove_orphan_triefacts fingerprint=18e45ead56f4ba24689540a1a7fcc01268f5f8417dad5cc26c04bae3232493fe body_fp=d133c979b6e394725235d8a77bcc02866c38e5cf37e2e0e03bd0f68490c747cb source_ref=9e576c94de69bc9bed35694ec4c6df87791394e6 -->
## `remove_orphan_triefacts(*, project_root: Path, config: Config) -> list[Path]`

Delete trie-owned triefact files whose source no longer exists; return deleted paths.
<!-- trie:end -->