---
trie_version: 0.1.5
source: trie/scan.py
file_fingerprint: 1ac64e845687c0b329b8bfd3e1c0d0cb7f588d619cc78b615953aab32750b7d7
last_synced_at: '2026-06-03T21:15:13Z'
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
incoming_refs: 18
outgoing_refs: 4
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
<!-- trie:section symbol=trie/scan:scan_project fingerprint=3ffa1b08322db4d58b517de9235ec606961e0e5bbd135353511354276eb3680c body_fp=4d16bb249a251e8fd945dbeca3a20b3fe8fe8cbb0c73c6122dd1256ea5b958d5 source_ref=ba0d38d68c99a578b6395e4b44522d5825f9668d role=change-detection -->
Walks the project, parses changed files, and persists symbols to the store with fingerprint-based change detection.

- Files whose fingerprint matches stored value are skipped without re-parsing
- Files no longer in scope or on disk are removed with cascade deletion
- Edges are regenerated from scratch on every scan due to potential symbol ID changes
<!-- trie:end -->