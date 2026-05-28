---
trie_version: 0.1.5
source: tests/test_reconcile.py
file_fingerprint: 6c61486e145c55ceb6940129dc0e62fcca2d88325e26ddf1de672c4ad51c8ac7
last_synced_at: '2026-05-23T23:53:42Z'
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
<!-- trie:section symbol=tests/test_reconcile:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=fb2006d040cbc083b4169f0b7fbc3392aa4cb62fe7c2af9a39aceee8accd3712 source_ref=5c53604691e3b54c961be79f3f3277d0c20a70bc -->
## `tests/test_reconcile`

Test suite for `find_orphan_triefacts` and `remove_orphan_triefacts` reconciliation logic.

- **`test_no_orphans_when_sources_exist`**: triefact with matching source file → no orphans.
- **`test_orphan_when_source_deleted`**: triefact whose source is absent → detected as orphan.
- **`test_user_authored_triefact_left_alone`**: file without `trie_version` front-matter → ignored.
- **`test_remove_actually_deletes`**: `remove_orphan_triefacts` deletes the orphan file on disk.
- **`test_no_triefacts_dir_returns_empty`**: missing triefacts directory → returns empty list.
- **`test_excluded_source_treated_as_orphan`**: source excluded by scope config → triefact is orphaned.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_reconcile:_setup fingerprint=9635d698397eed755ba54f18855a451e5f737f90ab053c81317de51f20a18b4a body_fp=8aca479b78f0b1fc29b08f897f4634b33934e9f64dde59b3a28515364a1310e5 source_ref=5c53604691e3b54c961be79f3f3277d0c20a70bc -->
## `_setup(tmp_path: Path) -> Path`

Write a standard `trie.toml` config file into `tmp_path` and return it as the project root.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_reconcile:test_no_orphans_when_sources_exist fingerprint=d31b08271a892838d6bc6f89fc5a8bb5052e1dcde8b8b02612530285e41b686f body_fp=dec98229914e192d1801f077f5756afde91e5a11d91a1e46feca768015da8e3f source_ref=5c53604691e3b54c961be79f3f3277d0c20a70bc -->
## `test_no_orphans_when_sources_exist(tmp_path: Path)`

Assert that `find_orphan_triefacts` returns an empty list when all triefact source files exist.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_reconcile:test_orphan_when_source_deleted fingerprint=9f13272e7b95884eb5f097a5aa01e09682565328c4001d5c51e6943938cd6746 body_fp=b73f5a39c357550d91fdb4de7289b643f3be78599754c6792196936903c81832 source_ref=5c53604691e3b54c961be79f3f3277d0c20a70bc -->
## `test_orphan_when_source_deleted(tmp_path: Path)`

Assert that `find_orphan_triefacts` returns a triefact whose referenced source file does not exist.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_reconcile:test_user_authored_triefact_left_alone fingerprint=f7e0b52e0293c96a859e10c8404939b3c5d53e6a31d935c3c93b650a7aeffae7 body_fp=8da2f511ff23253a9a4e22ffc8ecf0266d574dd9d1a25093b8cf76aecf6708c0 source_ref=5c53604691e3b54c961be79f3f3277d0c20a70bc -->
## `test_user_authored_triefact_left_alone(tmp_path: Path)`

Assert that triefacts without `trie_version` front-matter are not classified as orphans.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_reconcile:test_remove_actually_deletes fingerprint=e9e70bd5366d12b0d5cb0285a42b15a9ebd2f3443133380b49c1b6e7282ac4c0 body_fp=5eeb8ac1cd6a6ee88e1e9d3895cc34548e0ec76dc1de74135b5f0f158c59046f source_ref=5c53604691e3b54c961be79f3f3277d0c20a70bc -->
## `test_remove_actually_deletes(tmp_path: Path)`

Verify that `remove_orphan_triefacts` physically deletes an orphaned triefact file from disk.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_reconcile:test_no_triefacts_dir_returns_empty fingerprint=5b3994f1ca5f53fd535022d1aa83e221c8e1598daf002bf1ec066a2e19f5a396 body_fp=7d6f1e4ea0174d744764e49d32f600ac3a3c33dadbb7dd301419df27b0220764 source_ref=5c53604691e3b54c961be79f3f3277d0c20a70bc -->
## `test_no_triefacts_dir_returns_empty(tmp_path: Path)`

Assert that `find_orphan_triefacts` returns an empty list when the triefacts directory does not exist.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_reconcile:test_excluded_source_treated_as_orphan fingerprint=51f3b95780e73d907221d3b2b525cce77bf2a2119a05633c3389661f3bd94cbe body_fp=ccdbfbdad57259050fa913e3307376378ca8461d959414f3e94ff4be905baac7 source_ref=5c53604691e3b54c961be79f3f3277d0c20a70bc -->
## `test_excluded_source_treated_as_orphan(tmp_path: Path)`

Assert that a triefact whose source file is excluded by scope is reported as an orphan.
<!-- trie:end -->