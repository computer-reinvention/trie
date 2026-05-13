---
trie_version: 0.1.0
source: trie/sync/reconcile.py
file_fingerprint: f08a21b3a2d39b28de540438b9631c2a6351b6e31b3d79bce8e05db59874a525
last_synced_at: '2026-05-12T18:35:18Z'
defines:
- kind: function
  qualified_name: trie/sync/reconcile:find_orphan_triefacts
  lines: 10-52
- kind: function
  qualified_name: trie/sync/reconcile:remove_orphan_triefacts
  lines: 55-60
incoming_refs: 7
outgoing_refs: 2
---
<!-- trie:section symbol=trie/sync/reconcile:find_orphan_triefacts fingerprint=1686ac04fded14fddb1a9d3afda81e606cd9888e30673c180ed639f49c233d10 body_fp=60467123235768262456a1402b58cde6621a9612b982021b52eee444c9a4b6f4 -->
## `find_orphan_triefacts(*, project_root: Path, config: Config) -> list[Path]`

Return absolute paths of trie-owned triefact `.md` files whose corresponding source `.py` file no longer exists in scope.

- **trie-owned**: triefact has a `trie_version` key in its YAML front-matter; hand-authored files without it are ignored.
- Returns an empty list if the triefacts root directory does not exist.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/reconcile:remove_orphan_triefacts fingerprint=18e45ead56f4ba24689540a1a7fcc01268f5f8417dad5cc26c04bae3232493fe body_fp=c1748bf603d18b750b173d7e3158ef2a27526ea6d44705ed0846ae0f2549873c -->
## `remove_orphan_triefacts(*, project_root: Path, config: Config) -> list[Path]`

Delete all trie-owned triefact files whose source no longer exists; return deleted paths.
<!-- trie:end -->