---
trie_version: 0.1.5
source: trie/scan.py
file_fingerprint: 1ac64e845687c0b329b8bfd3e1c0d0cb7f588d619cc78b615953aab32750b7d7
last_synced_at: '2026-05-23T23:54:19Z'
defines:
- kind: module
  qualified_name: trie/scan:__module__
  lines: 1-110
- kind: class
  qualified_name: trie/scan:ScanResult
  lines: 15-23
- kind: function
  qualified_name: trie/scan:file_fingerprint
  lines: 26-27
- kind: function
  qualified_name: trie/scan:scan_project
  lines: 30-109
incoming_refs: 17
outgoing_refs: 4
---
<!-- trie:section symbol=trie/scan:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=4498f154b575b60f099930d983c6a221a781522140c12f15fa705902d9f4b864 source_ref=ba0d38d68c99a578b6395e4b44522d5825f9668d -->
## `trie/scan.py`

Walk a project tree, parse changed files, persist symbols and edges to the store.

- `ScanResult`: frozen dataclass summarising counts from one scan run
- `file_fingerprint`: SHA-256 hex digest used to detect file changes
- `scan_project`: main entry point; idempotent, skips unchanged files by fingerprint
<!-- trie:end -->
<!-- trie:section symbol=trie/scan:ScanResult fingerprint=68500ac17e0377b57a57a8bd10eab23b03e157d3601244f237edd7ae22b31ecc body_fp=0d6f88731f60cfead8a1cfc2b73d2e6dec2a5eb3036ae5046f6df49e80b01ecc source_ref=ba0d38d68c99a578b6395e4b44522d5825f9668d -->
## `ScanResult`

Immutable summary of a single `scan_project` run.

- `files_removed`: count of DB entries deleted because they left scope or disk.
- `edges_total`: total cross-file reference edges written to the store.
<!-- trie:end -->
<!-- trie:section symbol=trie/scan:file_fingerprint fingerprint=46c7c51a18ded3953f42cbf0478b0794532566079fd73b079dc9950d2c108e07 body_fp=8194cda9949accbe1268305a968be7067051b9631f789f345442ef784dac2126 source_ref=ba0d38d68c99a578b6395e4b44522d5825f9668d -->
## `file_fingerprint(text: str) -> str`

Compute the SHA-256 hex digest of a UTF-8 encoded string.
<!-- trie:end -->
<!-- trie:section symbol=trie/scan:scan_project fingerprint=3ffa1b08322db4d58b517de9235ec606961e0e5bbd135353511354276eb3680c body_fp=779cf001870259097dd0be9c40c587d3cf1f0d4c42a69f437687b75f9d176f9d source_ref=ba0d38d68c99a578b6395e4b44522d5825f9668d -->
## `scan_project(*, project_root: Path, config: Config, store: Store) -> ScanResult`

Walk the project, parse changed files, and persist symbols and edges to the `Store`, skipping fingerprint-matched files.

- `project_root`: resolved to absolute; files outside `config.triefacts.source_root` are ignored.
- Files unchanged by fingerprint skip symbol re-persistence but still parse for reference edges.
- Out-of-scope or deleted files are removed from the `Store` with cascade deletion of their symbols.
- All edges are regenerated from scratch on every scan regardless of file change status.
<!-- trie:end -->