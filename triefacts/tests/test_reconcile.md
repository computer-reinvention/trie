---
trie_version: 0.1.0
source: tests/test_reconcile.py
file_fingerprint: 2a74ac9442ff2a4091fcfa7273f4e9333f45408b133d1a0b1e56c226b64e22cf
last_synced_at: '2026-05-12T18:33:40Z'
defines:
- kind: function
  qualified_name: tests/test_reconcile:test_no_orphans_when_sources_exist
  lines: 21-29
- kind: function
  qualified_name: tests/test_reconcile:test_orphan_when_source_deleted
  lines: 32-41
- kind: function
  qualified_name: tests/test_reconcile:test_user_authored_triefact_left_alone
  lines: 44-50
- kind: function
  qualified_name: tests/test_reconcile:test_remove_actually_deletes
  lines: 53-63
- kind: function
  qualified_name: tests/test_reconcile:test_no_triefacts_dir_returns_empty
  lines: 66-69
- kind: function
  qualified_name: tests/test_reconcile:test_excluded_source_treated_as_orphan
  lines: 72-91
incoming_refs: 0
outgoing_refs: 12
---
<!-- trie:section symbol=tests/test_reconcile:test_no_orphans_when_sources_exist fingerprint=d31b08271a892838d6bc6f89fc5a8bb5052e1dcde8b8b02612530285e41b686f body_fp=19ade57f54b7262a1c9595ea6d981b179f0f0d5af960ce21ca1a9581e3200d53 -->
## `test_no_orphans_when_sources_exist(tmp_path: Path)`

Assert that `find_orphan_triefacts` returns an empty list when every triefact's source file exists.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_reconcile:test_orphan_when_source_deleted fingerprint=9f13272e7b95884eb5f097a5aa01e09682565328c4001d5c51e6943938cd6746 body_fp=964d907d831c18dc333b6eda85918b131854c64f248b15c1c70bfdd396c75c2d -->
## `test_orphan_when_source_deleted(tmp_path: Path)`

Verify that a triefact whose source file no longer exists is identified as an orphan.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_reconcile:test_user_authored_triefact_left_alone fingerprint=f7e0b52e0293c96a859e10c8404939b3c5d53e6a31d935c3c93b650a7aeffae7 body_fp=7e19ea8dcb5e29867d8fe0059ad94ff44cb4ebf5a1fd3d861ef7b09814631ab7 -->
## `test_user_authored_triefact_left_alone(tmp_path: Path)`

Assert that triefacts without `trie_version` front-matter are not reported as orphans.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_reconcile:test_remove_actually_deletes fingerprint=e9e70bd5366d12b0d5cb0285a42b15a9ebd2f3443133380b49c1b6e7282ac4c0 body_fp=7dada9fa181fe67a4d9180354a1eceb6a806aeb4a86ab06a116a811d60d2ff7b -->
## `test_remove_actually_deletes(tmp_path: Path)`

Verify that `remove_orphan_triefacts` deletes orphaned triefact files from disk.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_reconcile:test_no_triefacts_dir_returns_empty fingerprint=5b3994f1ca5f53fd535022d1aa83e221c8e1598daf002bf1ec066a2e19f5a396 body_fp=7d6f1e4ea0174d744764e49d32f600ac3a3c33dadbb7dd301419df27b0220764 -->
## `test_no_triefacts_dir_returns_empty(tmp_path: Path)`

Assert that `find_orphan_triefacts` returns an empty list when the triefacts directory does not exist.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_reconcile:test_excluded_source_treated_as_orphan fingerprint=51f3b95780e73d907221d3b2b525cce77bf2a2119a05633c3389661f3bd94cbe body_fp=99cfc73f03768d218169754251cb63fa9dc74a3b429d194111716e4af4aad388 -->
## `test_excluded_source_treated_as_orphan(tmp_path: Path)`

Verify that a triefact whose source file is excluded by scope config is detected as an orphan.
<!-- trie:end -->