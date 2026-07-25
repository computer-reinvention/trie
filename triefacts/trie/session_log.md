---
trie_version: 0.1.9
source: trie/session_log.py
file_fingerprint: 5a6af89e0c3fb29baef1ba184acc9c46962d8ae0bbde29173deab1d60a0d2897
last_synced_at: '2026-07-25T00:07:10Z'
defines:
- kind: module
  qualified_name: trie/session_log:__module__
  lines: 1-124
- kind: function
  qualified_name: trie/session_log:log_path
  lines: 8-10
- kind: function
  qualified_name: trie/session_log:record_applied
  lines: 13-32
- kind: function
  qualified_name: trie/session_log:read_entries
  lines: 35-70
- kind: function
  qualified_name: trie/session_log:read_digest_cursor
  lines: 73-84
- kind: function
  qualified_name: trie/session_log:save_digest_cursor
  lines: 87-106
- kind: function
  qualified_name: trie/session_log:resolve_digest_window
  lines: 109-123
incoming_refs: 14
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
<!-- trie:section symbol=trie/session_log:read_digest_cursor fingerprint=a71ec44739e35cbe15f0b583ec21549c4d7eb710a85225e1f878d6f5f525c65c body_fp=e4547d2b718061cda33c078080211cc5cc899748f3bfce89da47fa8d0e19a5d3 source_ref=1ea9f826d5d2bedc43f59e6cdf6af8e6bce004b7 role=persistence -->
Read and validate the digest cursor from `.trie/digest_cursor.json`, returning `None` on missing file, parse error, or missing required keys.

- Returns `None` if the JSON root is not a dict or lacks any of `parent`, `since`, `covered`.
<!-- trie:end -->
<!-- trie:section symbol=trie/session_log:save_digest_cursor fingerprint=930d5541b7f2edb6f64dae7b3051ed276d1a810670ccfb9365f1b9845506b5db body_fp=cc39afe4aa6c05c104b034b71c3c7c1b6348a6ff5d396dc1ab91e07a67c2c854 source_ref=1ea9f826d5d2bedc43f59e6cdf6af8e6bce004b7 role=persistence -->
Atomically write the digest window cursor (`parent`, `since`, `covered`) to `.trie/digest_cursor.json`, swallowing `OSError` on failure.

- `parent`: SHA of the commit this cursor is anchored to.
- `since`: timestamp marking the start of the covered window.
- `covered`: timestamp marking the end of the covered window.
<!-- trie:end -->
<!-- trie:section symbol=trie/session_log:resolve_digest_window fingerprint=579c9a9f2b2dad92492984f6c8f61088fb6fda3cd3ada420cbab150933048a4c body_fp=51338fb7360524f9eee855fb93948198b7d1fd8f4a9d84628ae0625e10d92399 source_ref=1ea9f826d5d2bedc43f59e6cdf6af8e6bce004b7 role=domain -->
Determine the start timestamp of the applied-notes window for a digest write, using the persisted cursor or a fallback.

- `parent_sha`: if it matches the cursor's `parent`, returns the cursor's `since` (amend/retry path)
- `fallback_since`: returned when no cursor exists
- Returns `cursor["covered"]` for a normal next-commit advance; `None` if cursor key is absent
<!-- trie:end -->