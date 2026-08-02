---
trie_version: 0.3.0
source: trie/sync/reconcile.py
file_fingerprint: 15269bf1d27fc9114af81e8025120fb83339d0fd4f276125f5c8f669ffa61c8f
last_synced_at: '2026-07-29T01:49:09Z'
defines:
- kind: module
  qualified_name: trie/sync/reconcile:__module__
  lines: 1-90
- kind: function
  qualified_name: trie/sync/reconcile:_candidate_sources
  lines: 11-35
  signature: 'def _candidate_sources(rel_triefact: Path) -> list[str]'
- kind: function
  qualified_name: trie/sync/reconcile:find_orphan_triefacts
  lines: 38-81
  signature: 'def find_orphan_triefacts(*, project_root: Path, config: Config) -> list[Path]'
- kind: function
  qualified_name: trie/sync/reconcile:remove_orphan_triefacts
  lines: 84-89
  signature: 'def remove_orphan_triefacts(*, project_root: Path, config: Config) -> list[Path]'
incoming_refs: 7
outgoing_refs: 4
---
<!-- trie:section symbol=trie/sync/reconcile:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=cc57430aa74eca9329febcca49157958b3c4e57d5e4de80bd5fdbc017147ce98 source_ref=9e576c94de69bc9bed35694ec4c6df87791394e6 role=documentation-sync -->
Identifies and removes orphaned triefact files whose corresponding source files have been deleted.

- **Orphan detection**: triefact files with `trie_version` front-matter but no matching source file
- **Hand-authored files**: Markdown files without `trie_version` are preserved
- **Path mapping**: triefact tree mirrors source tree structure (triefacts/foo/bar.md ↔ foo/bar.py)
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/reconcile:_candidate_sources fingerprint=ab4fba00a1149cf1e318daa88838fc8ce38dafae53ae8c5fbb199435f23fa290 body_fp=6ad4412899c62712240ab92126c452dcb6b32ea24100ae24a52e79261b30784b source_ref=34572815885e59ee28141404795d314f02ecc8ee role=util -->
## `def _candidate_sources(rel_triefact: Path) -> list[str]`

Return all possible source file paths that a given `.md` triefact path could mirror, one candidate per registered language suffix.

- `rel_triefact`: relative path of the triefact file within the triefacts root tree.
- Handles compound suffixes (e.g. `.d.ts`) by matching the inner part already embedded in the base name.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/reconcile:find_orphan_triefacts fingerprint=0e4cc91871606dd92c23936031b133dd7d2096d4a9efd2a3ff288bb7dd63cea2 body_fp=76404a2e48c85430a6f82ea7ad499f5d6e70af1677bd75c8e0ff9cacd3f51537 source_ref=34572815885e59ee28141404795d314f02ecc8ee role=domain -->
## `def find_orphan_triefacts(*, project_root: Path, config: Config) -> list[Path]`

Finds trie-owned triefact files whose corresponding source files have been deleted.

- Only considers triefacts with `trie_version` in YAML front-matter as trie-owned
- Maps triefact paths to candidate source paths across all registered language suffixes, not just `.py`
- Skips triefacts that cannot be read or parsed
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/reconcile:remove_orphan_triefacts fingerprint=18e45ead56f4ba24689540a1a7fcc01268f5f8417dad5cc26c04bae3232493fe body_fp=d6edd3c85ed9196cffc216ebdaf5fed9c8467a5f7f87882c321299b4f15a1157 source_ref=9e576c94de69bc9bed35694ec4c6df87791394e6 role=documentation-sync -->
## `def remove_orphan_triefacts(*, project_root: Path, config: Config) -> list[Path]`

Deletes orphan trie-owned triefact files and returns their absolute paths.

- Returns list of deleted file paths
<!-- trie:end -->