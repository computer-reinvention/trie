---
trie_version: 0.3.0
source: trie/scan.py
file_fingerprint: aaeaef853270182b1b11e7777c18260a49daedf84eaabede5d1047a45eb8fdeb
last_synced_at: '2026-08-02T21:19:42Z'
defines:
- kind: module
  qualified_name: trie/scan:__module__
  lines: 1-112
- kind: class
  qualified_name: trie/scan:ScanResult
  lines: 16-24
  signature: class ScanResult
- kind: function
  qualified_name: trie/scan:file_fingerprint
  lines: 27-28
  signature: 'def file_fingerprint(text: str) -> str'
- kind: function
  qualified_name: trie/scan:scan_project
  lines: 31-111
  signature: 'def scan_project(*, project_root: Path, config: Config, store: Store) -> ScanResult'
incoming_refs: 29
outgoing_refs: 6
---
<!-- trie:section symbol=trie/scan:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=707e1d430cd869746b7ed5377a65ba2e430bacec467f40f67f40b4d789502e8c source_ref=ba0d38d68c99a578b6395e4b44522d5825f9668d role=source-parsing -->
Scans Python projects to extract and persist symbol definitions and references with incremental updates.

- **ScanResult**: Dataclass containing scan statistics including file and symbol counts
- **file_fingerprint()**: Generates SHA256 hash of file content for change detection
- **scan_project()**: Main orchestration function that walks project files, parses changed content, and updates the symbol store
<!-- trie:end -->
<!-- trie:section symbol=trie/scan:ScanResult fingerprint=68500ac17e0377b57a57a8bd10eab23b03e157d3601244f237edd7ae22b31ecc body_fp=74c58e2cd330244d1f47b8d2d40f003b1de1f83c2de47f2bf055ba48c4146084 source_ref=ba0d38d68c99a578b6395e4b44522d5825f9668d role=source-parsing -->
## `class ScanResult`

Contains metrics from scanning a project's source files for symbols and references.

- `files_new`: newly discovered files added to the database
- `files_updated`: existing files with changed fingerprints that were re-parsed
- `files_unchanged`: existing files with matching fingerprints that were skipped
- `files_removed`: files deleted from disk or out of scope
<!-- trie:end -->
<!-- trie:section symbol=trie/scan:file_fingerprint fingerprint=46c7c51a18ded3953f42cbf0478b0794532566079fd73b079dc9950d2c108e07 body_fp=3c178d578a404c7c426d0ed746b86eee2500f39fa7da258eed7035c863987928 source_ref=ba0d38d68c99a578b6395e4b44522d5825f9668d role=change-detection -->
## `def file_fingerprint(text: str) -> str`

Computes SHA-256 hash of UTF-8 encoded text as hexadecimal string.
<!-- trie:end -->
<!-- trie:section symbol=trie/scan:scan_project fingerprint=c24bda287627db5eed11373586b8ec8aa7cc0e726d124b0f6bd173da024d44b0 body_fp=aa67c52d33f2a6e28b91c829e9d832ce4f4b8992a73568cc2bed3b37b7bab087 source_ref=a6e0afc35d0e2d84b7f14f09afe81e988fa302f6 role=orchestration -->
## `def scan_project(*, project_root: Path, config: Config, store: Store) -> ScanResult`

Walks the project, parses changed files, and persists symbols to the store with fingerprint-based change detection.

- Files whose fingerprint matches stored value are skipped without re-parsing
- Only files passing `registry.is_indexable` are included in the scan scope
- Calls `registry.apply_resolver_config(config)` before scanning to configure resolvers
- Files no longer in scope or on disk are removed with cascade deletion
- Edges are regenerated from scratch on every scan due to potential symbol ID changes
<!-- trie:end -->