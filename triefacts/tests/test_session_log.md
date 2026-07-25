---
trie_version: 0.1.9
source: tests/test_session_log.py
file_fingerprint: f1462fd162de34a0176f606df924905dd4117476f107c7d70f3c3c1b21f76daa
last_synced_at: '2026-07-25T00:40:34Z'
defines:
- kind: module
  qualified_name: tests/test_session_log:__module__
  lines: 1-42
- kind: function
  qualified_name: tests/test_session_log:test_digest_cursor_roundtrip_and_window
  lines: 8-41
incoming_refs: 0
outgoing_refs: 3
---
<!-- trie:section symbol=tests/test_session_log:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=df53ba958343bc7fb34389745afc37c29e5029bb8944b318ac9d2eddf5444be1 source_ref=c06e6da24ee539da6a818e5b030c87498df650c1 role=test -->
Tests roundtrip behaviour and edge cases for `read_digest_cursor`, `resolve_digest_window`, and `save_digest_cursor` from `trie.session_log`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_session_log:test_digest_cursor_roundtrip_and_window fingerprint=12241a5f0aa130a8581c4506296e922585461f7cd6c9d333d62155eb1abedff2 body_fp=81f719134b8a961ec4cb0f7f1b2b4e2657d8c1deca224b39c2ec0ae5cf512861 source_ref=c81a95bf9199f4c1cd6e24b58919fb75c1a5c86e role=test -->
Tests `read_digest_cursor`, `save_digest_cursor`, and `resolve_digest_window` covering no-cursor fallback, same/different parent resumption, `file` field persistence, and corrupt-JSON degradation.
<!-- trie:end -->