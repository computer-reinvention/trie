---
trie_version: 0.1.0
source: trie/scope.py
file_fingerprint: 054b9955d944f35c87b1470e69533098f2d084f385d175c520128b2371d44638
last_synced_at: '2026-05-12T18:35:21Z'
defines:
- kind: function
  qualified_name: trie/scope:discover_files
  lines: 8-35
incoming_refs: 10
outgoing_refs: 0
---
<!-- trie:section symbol=trie/scope:discover_files fingerprint=dcf6cef5f7f1965b7f70313f806c1e1e0168f483eaa0b6ac4448e2d1990c8edd body_fp=9c943935b3d58197707474678a1e254842f891b9ec1e16587b5f2c2c55c50c4a -->
## `discover_files(project_root: Path, scope: Scope) -> list[Path]`

Return sorted absolute paths of files under `project_root` that match `scope.include` glob patterns and are not excluded by `scope.exclude` patterns.

- `scope.include` / `scope.exclude`: pathlib glob patterns evaluated relative to `project_root`; `**` matches zero or more directory segments.
- Excluding a directory recursively excludes all files beneath it.
<!-- trie:end -->