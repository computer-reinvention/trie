---
trie_version: 0.1.9
source: tests/test_session_log.py
file_fingerprint: 1bc0accf50d5f8d212989d3ffb27e95355421dd0ee833dd1d91270753a0d14e7
last_synced_at: '2026-07-25T00:24:00Z'
defines:
- kind: module
  qualified_name: tests/test_session_log:__module__
  lines: 1-40
- kind: function
  qualified_name: tests/test_session_log:test_digest_cursor_roundtrip_and_window
  lines: 8-39
incoming_refs: 0
outgoing_refs: 3
---
<!-- trie:section symbol=tests/test_session_log:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=df53ba958343bc7fb34389745afc37c29e5029bb8944b318ac9d2eddf5444be1 source_ref=c06e6da24ee539da6a818e5b030c87498df650c1 role=test -->
Tests roundtrip behaviour and edge cases for `read_digest_cursor`, `resolve_digest_window`, and `save_digest_cursor` from `trie.session_log`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_session_log:test_digest_cursor_roundtrip_and_window fingerprint=5fccc8d387f67d645bdcc34c4160d29d9e19d870cbd421d7e2043349d77c05b5 body_fp=81f719134b8a961ec4cb0f7f1b2b4e2657d8c1deca224b39c2ec0ae5cf512861 source_ref=a2b7cf005c443eaf1acd114642c1f2dcf55726a9 role=test -->
Tests `read_digest_cursor`, `save_digest_cursor`, and `resolve_digest_window` covering no-cursor fallback, same/different parent resumption, `file` field persistence, and corrupt-JSON degradation.
<!-- trie:end -->