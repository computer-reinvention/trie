---
trie_version: 0.1.9
source: trie/session_log.py
file_fingerprint: da860a0f328894ead3de52a60e0111338e701ae3854afd9c8fcd86fe1b9d7950
last_synced_at: '2026-07-25T01:02:02Z'
defines:
- kind: module
  qualified_name: trie/session_log:__module__
  lines: 1-134
- kind: function
  qualified_name: trie/session_log:log_path
  lines: 8-10
- kind: function
  qualified_name: trie/session_log:record_applied
  lines: 13-32
- kind: function
  qualified_name: trie/session_log:read_entries
  lines: 35-74
- kind: function
  qualified_name: trie/session_log:read_digest_cursor
  lines: 77-88
- kind: function
  qualified_name: trie/session_log:save_digest_cursor
  lines: 91-116
- kind: function
  qualified_name: trie/session_log:resolve_digest_window
  lines: 119-133
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
<!-- trie:section symbol=trie/session_log:read_entries fingerprint=1643adf3dcd2becb0b493cc491175b74264235302c5257bfe7de1ce323e00535 body_fp=b566083707907568413f2ff329d7b6c793fc1c3474fbae3b93b5d99eebb7ede8 source_ref=f8a69ba53b4235ea183816cdd6b7f03c02e7b589 role=persistence -->
Read and return applied-patch records from the session log JSONL file, with optional filtering.

- `session_id`: when set, only records with a matching `session_id` field are included.
- `since`: Unix timestamp; records whose `ts` is less than or equal to this value are excluded.
- Returns an empty list if the log file does not exist or an `OSError` occurs before any records are collected; returns partial results if `OSError` occurs mid-read.
- Silently skips malformed or non-dict JSONL lines.
<!-- trie:end -->
<!-- trie:section symbol=trie/session_log:read_digest_cursor fingerprint=a71ec44739e35cbe15f0b583ec21549c4d7eb710a85225e1f878d6f5f525c65c body_fp=e4547d2b718061cda33c078080211cc5cc899748f3bfce89da47fa8d0e19a5d3 source_ref=1ea9f826d5d2bedc43f59e6cdf6af8e6bce004b7 role=persistence -->
Read and validate the digest cursor from `.trie/digest_cursor.json`, returning `None` on missing file, parse error, or missing required keys.

- Returns `None` if the JSON root is not a dict or lacks any of `parent`, `since`, `covered`.
<!-- trie:end -->
<!-- trie:section symbol=trie/session_log:save_digest_cursor fingerprint=7570d569c7be0f6243dff6cd06c8bda97afb7e70cb58ea3f8e1709f739bd37d1 body_fp=5e8f9fb6d9f12bd2563982ac050f15432b1c4f788f9c5ad9c0b57bb3216c864f source_ref=dc8a04dae43b9b9d289a9998dccba10d39826b97 role=persistence -->
Atomically write the digest window cursor (`parent`, `since`, `covered`, `file`) to `.trie/digest_cursor.json`, swallowing `OSError` on failure.

- `parent`: SHA of the commit this cursor is anchored to.
- `since`: timestamp marking the start of the covered window.
- `covered`: timestamp marking the end of the covered window.
- `file`: project-relative path of the digest file written for `parent`; enables amend/retry to overwrite rather than duplicate.
<!-- trie:end -->
<!-- trie:section symbol=trie/session_log:resolve_digest_window fingerprint=579c9a9f2b2dad92492984f6c8f61088fb6fda3cd3ada420cbab150933048a4c body_fp=51338fb7360524f9eee855fb93948198b7d1fd8f4a9d84628ae0625e10d92399 source_ref=1ea9f826d5d2bedc43f59e6cdf6af8e6bce004b7 role=domain -->
Determine the start timestamp of the applied-notes window for a digest write, using the persisted cursor or a fallback.

- `parent_sha`: if it matches the cursor's `parent`, returns the cursor's `since` (amend/retry path)
- `fallback_since`: returned when no cursor exists
- Returns `cursor["covered"]` for a normal next-commit advance; `None` if cursor key is absent
<!-- trie:end -->