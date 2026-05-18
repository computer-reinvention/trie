---
trie_version: 0.1.1
source: trie/scope.py
file_fingerprint: 054b9955d944f35c87b1470e69533098f2d084f385d175c520128b2371d44638
last_synced_at: '2026-05-14T17:31:38Z'
defines:
- kind: function
  qualified_name: trie/scope:discover_files
  lines: 8-35
incoming_refs: 11
outgoing_refs: 0
---
<!-- trie:section symbol=trie/scope:discover_files fingerprint=dcf6cef5f7f1965b7f70313f806c1e1e0168f483eaa0b6ac4448e2d1990c8edd body_fp=e763e815959dc5c04a73ddbe611d9f29496cae6a52eb4f763a2aa984524001be source_ref=f8a23f982fb02a3a1ba2e235a94683e1984a2cd4 -->
## `discover_files(project_root: Path, scope: Scope) -> list[Path]`

Return sorted absolute paths of files under `project_root` matching `scope.include` glob patterns minus any matched by `scope.exclude`.

- `scope.include` / `scope.exclude`: pathlib glob patterns relative to `project_root`; `**` matches zero or more directory segments.
- Excluded directories recursively exclude all files beneath them.
<!-- trie:end -->