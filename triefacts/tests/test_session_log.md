---
trie_version: 0.1.9
source: tests/test_session_log.py
file_fingerprint: 48032ae2bc5ef829c9ec0f5e05606895c67ced61bfc4247b11982ac8446ec107
last_synced_at: '2026-07-25T00:07:05Z'
defines:
- kind: module
  qualified_name: tests/test_session_log:__module__
  lines: 1-36
- kind: function
  qualified_name: tests/test_session_log:test_digest_cursor_roundtrip_and_window
  lines: 8-35
incoming_refs: 0
outgoing_refs: 3
---
<!-- trie:section symbol=tests/test_session_log:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=df53ba958343bc7fb34389745afc37c29e5029bb8944b318ac9d2eddf5444be1 source_ref=c06e6da24ee539da6a818e5b030c87498df650c1 role=test -->
Tests roundtrip behaviour and edge cases for `read_digest_cursor`, `resolve_digest_window`, and `save_digest_cursor` from `trie.session_log`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_session_log:test_digest_cursor_roundtrip_and_window fingerprint=32a973df4d4daaefaeebf9e8e97e49c4c8eca0a068d8486b9c30615c5bd4abfd body_fp=2124f74339b156f64918e21162a784661b788f592928ebaee510d41a8e9d767a source_ref=c06e6da24ee539da6a818e5b030c87498df650c1 role=test -->
Tests `read_digest_cursor`, `save_digest_cursor`, and `resolve_digest_window` covering no-cursor fallback, same/different parent resumption, and corrupt-JSON degradation.
<!-- trie:end -->