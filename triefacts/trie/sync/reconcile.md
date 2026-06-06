---
trie_version: 0.1.5
source: trie/sync/reconcile.py
file_fingerprint: f08a21b3a2d39b28de540438b9631c2a6351b6e31b3d79bce8e05db59874a525
last_synced_at: '2026-06-03T21:16:24Z'
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
<!-- trie:section symbol=trie/sync/reconcile:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=cc57430aa74eca9329febcca49157958b3c4e57d5e4de80bd5fdbc017147ce98 source_ref=9e576c94de69bc9bed35694ec4c6df87791394e6 role=documentation-sync -->
Identifies and removes orphaned triefact files whose corresponding source files have been deleted.

- **Orphan detection**: triefact files with `trie_version` front-matter but no matching source file
- **Hand-authored files**: Markdown files without `trie_version` are preserved
- **Path mapping**: triefact tree mirrors source tree structure (triefacts/foo/bar.md ↔ foo/bar.py)
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/reconcile:find_orphan_triefacts fingerprint=1686ac04fded14fddb1a9d3afda81e606cd9888e30673c180ed639f49c233d10 body_fp=b5bf10409ea6c2fd9ae85c8a14533c0161e1bd6f63f6bd5ee4347652ca39d7fc source_ref=9e576c94de69bc9bed35694ec4c6df87791394e6 role=change-detection -->
Finds trie-owned triefact files whose corresponding source files have been deleted.

- Only considers triefacts with `trie_version` in YAML front-matter as trie-owned
- Maps triefact paths to expected source paths by changing `.md` extension to `.py`
- Skips triefacts that cannot be read or parsed
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/reconcile:remove_orphan_triefacts fingerprint=18e45ead56f4ba24689540a1a7fcc01268f5f8417dad5cc26c04bae3232493fe body_fp=f93bcca92b2dd208bec544c5a3ed9357b6c8f0fd772d38dcfd1ebaae5efb484c source_ref=9e576c94de69bc9bed35694ec4c6df87791394e6 role=documentation-sync -->
Deletes orphan trie-owned triefact files and returns their absolute paths.

- Returns list of deleted file paths
<!-- trie:end -->