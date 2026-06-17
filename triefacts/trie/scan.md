---
trie_version: 0.1.9
source: trie/scan.py
file_fingerprint: eff8da70c2e94c57499a045e82c240e95445373c0211cf18e2e7e13b3a62f5be
last_synced_at: '2026-06-17T16:42:00Z'
defines:
- kind: module
  qualified_name: trie/scan:__module__
  lines: 1-111
- kind: class
  qualified_name: trie/scan:ScanResult
  lines: 16-24
- kind: function
  qualified_name: trie/scan:file_fingerprint
  lines: 27-28
- kind: function
  qualified_name: trie/scan:scan_project
  lines: 31-110
incoming_refs: 28
outgoing_refs: 5
---
<!-- trie:section symbol=trie/scan:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=707e1d430cd869746b7ed5377a65ba2e430bacec467f40f67f40b4d789502e8c source_ref=ba0d38d68c99a578b6395e4b44522d5825f9668d role=source-parsing -->
Scans Python projects to extract and persist symbol definitions and references with incremental updates.

- **ScanResult**: Dataclass containing scan statistics including file and symbol counts
- **file_fingerprint()**: Generates SHA256 hash of file content for change detection
- **scan_project()**: Main orchestration function that walks project files, parses changed content, and updates the symbol store
<!-- trie:end -->
<!-- trie:section symbol=trie/scan:ScanResult fingerprint=68500ac17e0377b57a57a8bd10eab23b03e157d3601244f237edd7ae22b31ecc body_fp=20fd5e5203f2e66410f8124e56f6397686bf5cb91e8503cae78b571fac7c3315 source_ref=ba0d38d68c99a578b6395e4b44522d5825f9668d role=source-parsing -->
Contains metrics from scanning a project's source files for symbols and references.

- `files_new`: newly discovered files added to the database
- `files_updated`: existing files with changed fingerprints that were re-parsed
- `files_unchanged`: existing files with matching fingerprints that were skipped
- `files_removed`: files deleted from disk or out of scope
<!-- trie:end -->
<!-- trie:section symbol=trie/scan:file_fingerprint fingerprint=46c7c51a18ded3953f42cbf0478b0794532566079fd73b079dc9950d2c108e07 body_fp=8ad89667e91e786f56931ae31d6e18fd2fdd8bb2814d50034c3454f7ea014f85 source_ref=ba0d38d68c99a578b6395e4b44522d5825f9668d role=change-detection -->
Computes SHA-256 hash of UTF-8 encoded text as hexadecimal string.
<!-- trie:end -->
<!-- trie:section symbol=trie/scan:scan_project fingerprint=90ead9905aad5fc9127629afcbb79140862b3fc57d506439b232ca1bdf572aeb body_fp=40db81afbc1ccaa96931b8c91003d1a13de4feee2c6a97e0de834fed868e2fb8 source_ref=8b4c03492f968dc6f52c71fc4bee91ebbcdcfb79 role=orchestration -->
Walks the project, parses changed files, and persists symbols to the store with fingerprint-based change detection.

- Files whose fingerprint matches stored value are skipped without re-parsing
- Only files passing `registry.is_indexable` are included in the scan scope
- Files no longer in scope or on disk are removed with cascade deletion
- Edges are regenerated from scratch on every scan due to potential symbol ID changes
<!-- trie:end -->