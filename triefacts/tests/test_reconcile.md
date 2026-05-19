---
trie_version: 0.1.2
source: tests/test_reconcile.py
file_fingerprint: 7dc91301502b0b1020de1ca3ad91d222d46b212ec44363ff80993f540b6444a7
last_synced_at: '2026-05-19T10:38:49Z'
defines:
- kind: module
  qualified_name: tests/test_reconcile:__module__
  lines: 1-92
- kind: function
  qualified_name: tests/test_reconcile:_setup
  lines: 9-18
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
<!-- trie:section symbol=tests/test_reconcile:test_no_orphans_when_sources_exist fingerprint=d31b08271a892838d6bc6f89fc5a8bb5052e1dcde8b8b02612530285e41b686f body_fp=19ade57f54b7262a1c9595ea6d981b179f0f0d5af960ce21ca1a9581e3200d53 source_ref=b8ce768666df722220fe0f640f91bf372ed4c931 -->
## `test_no_orphans_when_sources_exist(tmp_path: Path)`

Assert that `find_orphan_triefacts` returns an empty list when every triefact's source file exists.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_reconcile:test_orphan_when_source_deleted fingerprint=9f13272e7b95884eb5f097a5aa01e09682565328c4001d5c51e6943938cd6746 body_fp=964d907d831c18dc333b6eda85918b131854c64f248b15c1c70bfdd396c75c2d source_ref=b8ce768666df722220fe0f640f91bf372ed4c931 -->
## `test_orphan_when_source_deleted(tmp_path: Path)`

Verify that a triefact whose source file no longer exists is identified as an orphan.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_reconcile:test_user_authored_triefact_left_alone fingerprint=f7e0b52e0293c96a859e10c8404939b3c5d53e6a31d935c3c93b650a7aeffae7 body_fp=e0288b9a5411ad8509c82456ef4ede7fcb9e858145b18cd92f26d26cc630612f source_ref=b8ce768666df722220fe0f640f91bf372ed4c931 -->
## `test_user_authored_triefact_left_alone(tmp_path: Path)`

Assert that triefacts lacking `trie_version` front-matter are not identified as orphans.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_reconcile:test_remove_actually_deletes fingerprint=e9e70bd5366d12b0d5cb0285a42b15a9ebd2f3443133380b49c1b6e7282ac4c0 body_fp=7dada9fa181fe67a4d9180354a1eceb6a806aeb4a86ab06a116a811d60d2ff7b source_ref=b8ce768666df722220fe0f640f91bf372ed4c931 -->
## `test_remove_actually_deletes(tmp_path: Path)`

Verify that `remove_orphan_triefacts` deletes orphaned triefact files from disk.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_reconcile:test_no_triefacts_dir_returns_empty fingerprint=5b3994f1ca5f53fd535022d1aa83e221c8e1598daf002bf1ec066a2e19f5a396 body_fp=7d6f1e4ea0174d744764e49d32f600ac3a3c33dadbb7dd301419df27b0220764 source_ref=b8ce768666df722220fe0f640f91bf372ed4c931 -->
## `test_no_triefacts_dir_returns_empty(tmp_path: Path)`

Assert that `find_orphan_triefacts` returns an empty list when the triefacts directory does not exist.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_reconcile:test_excluded_source_treated_as_orphan fingerprint=51f3b95780e73d907221d3b2b525cce77bf2a2119a05633c3389661f3bd94cbe body_fp=c5e74327f0ae9b7996337bdbb3f75ec48d8073e2c546dfa79bf33f7d93a2fb18 source_ref=b8ce768666df722220fe0f640f91bf372ed4c931 -->
## `test_excluded_source_treated_as_orphan(tmp_path: Path)`

Assert that a triefact whose source file is excluded by scope config is detected as an orphan.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_reconcile:_setup fingerprint=9635d698397eed755ba54f18855a451e5f737f90ab053c81317de51f20a18b4a body_fp=83f575b3088b9b3cd4fbf38e8f4476ec60d5f5d8cb36818e176c0d442deaa2b7 source_ref=b8ce768666df722220fe0f640f91bf372ed4c931 -->
## `_setup(tmp_path: Path) -> Path`

Write a minimal `trie.toml` config file into `tmp_path` and return it as the project root.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_reconcile:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=c7e5a08f7855323dbbdf242cf9016583c21223b8f9917cd5eeae356c0109f651 source_ref=4ac2418a92e95cb2f64ee3d085c68c415388a0cd -->
## `tests/test_reconcile`

Tests for `find_orphan_triefacts` and `remove_orphan_triefacts`, covering missing sources, user-authored triefacts, excluded sources, and absent triefacts directories.
<!-- trie:end -->