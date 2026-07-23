---
trie_version: 0.1.9
source: trie/session_log.py
file_fingerprint: 503e19051d12b30828ff5be35dbd4b84f77e1ef52db132981bdf584e2a7f9880
last_synced_at: '2026-07-20T23:25:39Z'
defines:
- kind: module
  qualified_name: trie/session_log:__module__
  lines: 1-71
- kind: function
  qualified_name: trie/session_log:log_path
  lines: 8-10
- kind: function
  qualified_name: trie/session_log:record_applied
  lines: 13-32
- kind: function
  qualified_name: trie/session_log:read_entries
  lines: 35-70
incoming_refs: 8
outgoing_refs: 0
---
<!-- trie:section symbol=trie/session_log:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=b9d45a60118c039a1fa1658991e797ced1fccf60585bb05a56b9ea665c59faa9 source_ref=a01edbcf00331fadfea67f6ef0636e71f4f1cfb7 role=persistence -->
Provides session log utilities for appending and reading applied-patch records in a JSONL file under `.trie/`.
<!-- trie:end -->
<!-- trie:section symbol=trie/session_log:log_path fingerprint=8d18f24ec749106cdeae86b2b7830155e5f831c6a989ebfbfd02bcf9031b4dea body_fp=3b526b3541ded48487055696f976b7136bfe994c9cf0c54c6e20f82b6fa4c16b source_ref=a01edbcf00331fadfea67f6ef0636e71f4f1cfb7 role=util -->
Return the canonical path to the session log JSONL file at `<project_root>/.trie/session_log.jsonl`.
<!-- trie:end -->
<!-- trie:section symbol=trie/session_log:record_applied fingerprint=defef7589217819c13af229a9c965abc24a585d1cd55d2cbe988182d06c268d9 body_fp=8f03409f86c38c3ae772a382c0c00a23fe8c963632c137ed87c738063a0aee22 source_ref=a01edbcf00331fadfea67f6ef0636e71f4f1cfb7 role=io -->
Append applied-patch `entries` as JSONL rows to the session log, silently swallowing all `OSError` exceptions.

- `entries`: list of dicts; each gains a `ts` (epoch float) if not already set.
<!-- trie:end -->
<!-- trie:section symbol=trie/session_log:read_entries fingerprint=f31ffaa9429a9250b06757beb44f1832f4b3e985470748f96b2e86c6b9ab1241 body_fp=866bcca0f2d41a08b4921cb70ae68512e0f60b70ee666eef9f36d9084d6e5fae source_ref=a01edbcf00331fadfea67f6ef0636e71f4f1cfb7 role=persistence -->
Read and return applied-patch records from the session log JSONL file, with optional filtering.

- `session_id`: when set, only records with a matching `session_id` field are included.
- `since`: Unix timestamp; records whose `ts` is strictly less than this value are excluded.
- Returns an empty list if the log file does not exist or an `OSError` occurs before any records are collected; returns partial results if `OSError` occurs mid-read.
- Silently skips malformed or non-dict JSONL lines.
<!-- trie:end -->