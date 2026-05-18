---
trie_version: 0.1.1
source: trie/scan.py
file_fingerprint: 1ac64e845687c0b329b8bfd3e1c0d0cb7f588d619cc78b615953aab32750b7d7
last_synced_at: '2026-05-16T11:46:57Z'
defines:
- kind: class
  qualified_name: trie/scan:ScanResult
  lines: 15-23
- kind: function
  qualified_name: trie/scan:file_fingerprint
  lines: 26-27
- kind: function
  qualified_name: trie/scan:scan_project
  lines: 30-109
incoming_refs: 13
outgoing_refs: 3
---
<!-- trie:section symbol=trie/scan:ScanResult fingerprint=68500ac17e0377b57a57a8bd10eab23b03e157d3601244f237edd7ae22b31ecc body_fp=507c853897dc77fdb4c3c0b6edc5da7c1de7bb31baba5626595d4a5fbdc00a47 source_ref=ba0d38d68c99a578b6395e4b44522d5825f9668d -->
## `ScanResult`

Frozen dataclass holding aggregate counts returned by a project scan.
<!-- trie:end -->

<!-- trie:section symbol=trie/scan:file_fingerprint fingerprint=46c7c51a18ded3953f42cbf0478b0794532566079fd73b079dc9950d2c108e07 body_fp=a935dd5e81a9de77d0662b7e119c330d0418c6666f35f4477e773f5eeabb4057 source_ref=ba0d38d68c99a578b6395e4b44522d5825f9668d -->
## `file_fingerprint(text: str) -> str`

Return the SHA-256 hex digest of a UTF-8-encoded string.
<!-- trie:end -->

<!-- trie:section symbol=trie/scan:scan_project fingerprint=3ffa1b08322db4d58b517de9235ec606961e0e5bbd135353511354276eb3680c body_fp=6b31b81c1e2fb6a7538e3869a587ddea07ec4df2d7a99fcfa1de690f77e3e233 source_ref=ba0d38d68c99a578b6395e4b44522d5825f9668d -->
## `scan_project(*, project_root: Path, config: Config, store: Store) -> ScanResult`

Walk the project, parse changed files, persist symbols, and regenerate all edges; idempotent.

- `project_root`: resolved to absolute path before processing.
- Files with unchanged fingerprints skip symbol re-persistence but still parse for references.
- DB files absent from the current scope are deleted with cascading symbol removal.
- `edges_total`: count of cross-file reference edges rebuilt from scratch each scan.
<!-- trie:end -->