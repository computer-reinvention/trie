---
trie_version: 0.1.0
source: trie/scan.py
file_fingerprint: 423d15c91515aed17ddac3f1d70e6dd41c5e3544d4ed609081e424d3cff8b8da
last_synced_at: '2026-05-14T17:30:52Z'
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
<!-- trie:section symbol=trie/scan:ScanResult fingerprint=68500ac17e0377b57a57a8bd10eab23b03e157d3601244f237edd7ae22b31ecc body_fp=49b1a948e4eeaee64a1c836e92122b9af405bacffb9c0c6c9cd622b8920c8672 -->
## `ScanResult(project_root, files_total, files_new, files_updated, files_unchanged, files_removed, symbols_total, edges_total)`

Frozen dataclass summarising the outcome of a single `scan_project` run.
<!-- trie:end -->

<!-- trie:section symbol=trie/scan:file_fingerprint fingerprint=46c7c51a18ded3953f42cbf0478b0794532566079fd73b079dc9950d2c108e07 body_fp=7dc9e9cac03820746c264668965717420b04916c9f995c459ba53b91f5f2591b -->
## `file_fingerprint(text: str) -> str`

Return the SHA-256 hex digest of a UTF-8 encoded string.
<!-- trie:end -->

<!-- trie:section symbol=trie/scan:scan_project fingerprint=5881d8d6a0326117b917987016497d2257550ac565e4ab31deafc05a62098652 body_fp=08179a074ada525682feae54828530e2a1e5484edb237076d36807e30ccd5675 -->
## `scan_project(*, project_root: Path, config: Config, store: Store) -> ScanResult`

Walk the project, parse changed files, persist symbols, and regenerate all edges; idempotent.

- `project_root`: resolved to an absolute path before use.
- Files whose stored fingerprint matches are skipped for symbol upsert but still parsed for references.
- DB files no longer on disk or in scope are deleted with cascade symbol removal.
- Edges are fully regenerated each scan regardless of which files changed.
<!-- trie:end -->