---
trie_version: 0.1.2
source: trie/sync/reconcile.py
file_fingerprint: f08a21b3a2d39b28de540438b9631c2a6351b6e31b3d79bce8e05db59874a525
last_synced_at: '2026-05-19T10:42:11Z'
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
<!-- trie:section symbol=trie/sync/reconcile:find_orphan_triefacts fingerprint=1686ac04fded14fddb1a9d3afda81e606cd9888e30673c180ed639f49c233d10 body_fp=390f75c084a5cc5913a7b7c737b8906051a07a484037bff4bb7c67f5eff8e039 source_ref=9e576c94de69bc9bed35694ec4c6df87791394e6 -->
## `find_orphan_triefacts(*, project_root: Path, config: Config) -> list[Path]`

Return absolute paths of trie-owned triefact `.md` files whose corresponding source file no longer exists in scope.

- **trie-owned**: triefact front-matter contains a `trie_version` key; hand-authored files without it are ignored.
- **orphan**: triefact path mirrors source tree, so `triefacts/foo/bar.md` expects `foo/bar.py` in scope.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/reconcile:remove_orphan_triefacts fingerprint=18e45ead56f4ba24689540a1a7fcc01268f5f8417dad5cc26c04bae3232493fe body_fp=d133c979b6e394725235d8a77bcc02866c38e5cf37e2e0e03bd0f68490c747cb source_ref=9e576c94de69bc9bed35694ec4c6df87791394e6 -->
## `remove_orphan_triefacts(*, project_root: Path, config: Config) -> list[Path]`

Delete trie-owned triefact files whose source no longer exists; return deleted paths.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/reconcile:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=f1b7d3a7c00abca3f571f9bc76587234eb0f8ab0f6338aefbd738cdeab8321e2 source_ref=9e576c94de69bc9bed35694ec4c6df87791394e6 -->
## `reconcile`

Identify and remove trie-owned triefact files whose source symbols no longer exist.

- **`find_orphan_triefacts`**: returns absolute paths of stale trie-owned `.md` files
- **`remove_orphan_triefacts`**: deletes those files and returns their paths
<!-- trie:end -->