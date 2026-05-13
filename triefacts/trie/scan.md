---
trie_version: 0.1.0
source: trie/scan.py
file_fingerprint: 423d15c91515aed17ddac3f1d70e6dd41c5e3544d4ed609081e424d3cff8b8da
last_synced_at: '2026-05-12T18:34:34Z'
defines:
- kind: class
  qualified_name: trie/scan:ScanResult
  lines: 14-22
- kind: function
  qualified_name: trie/scan:file_fingerprint
  lines: 25-26
- kind: function
  qualified_name: trie/scan:scan_project
  lines: 29-96
incoming_refs: 9
outgoing_refs: 3
---
<!-- trie:section symbol=trie/scan:ScanResult fingerprint=68500ac17e0377b57a57a8bd10eab23b03e157d3601244f237edd7ae22b31ecc body_fp=a477d23d32227b04d2ab8a3d01e82d3a49fecdb25a41f4822c8249fe071025ee -->
## `ScanResult(project_root, files_total, files_new, files_updated, files_unchanged, files_removed, symbols_total, edges_total)`

Frozen dataclass holding aggregate statistics returned by a project scan.
<!-- trie:end -->

<!-- trie:section symbol=trie/scan:file_fingerprint fingerprint=46c7c51a18ded3953f42cbf0478b0794532566079fd73b079dc9950d2c108e07 body_fp=c7e5992a459a4e01586a46905bc0608cae58cadecbbc3eeb73a366569c1e45a9 -->
## `file_fingerprint(text: str) -> str`

Return the SHA-256 hex digest of UTF-8–encoded text.
<!-- trie:end -->

<!-- trie:section symbol=trie/scan:scan_project fingerprint=5881d8d6a0326117b917987016497d2257550ac565e4ab31deafc05a62098652 body_fp=b0d5e55f0df30bd763e577f22315dd2884671edba6fe663bea9c2e223f64d8ed -->
## `scan_project(*, project_root: Path, config: Config, store: Store) -> ScanResult`

Walk the project, parse changed files, persist symbols, and regenerate all edges idempotently.

- `project_root`: resolved to an absolute path before use
- Files whose stored fingerprint matches are skipped but still parsed for references
- DB files no longer on disk or in scope are deleted with cascade symbol removal
- Edges are fully regenerated each scan; returns counts of new/updated/unchanged/removed files and total symbols and edges
<!-- trie:end -->