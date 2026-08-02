---
trie_version: 0.3.0
source: tests/test_reconcile.py
file_fingerprint: 6c61486e145c55ceb6940129dc0e62fcca2d88325e26ddf1de672c4ad51c8ac7
last_synced_at: '2026-06-17T16:43:09Z'
defines:
- kind: module
  qualified_name: tests/test_reconcile:__module__
  lines: 1-92
- kind: function
  qualified_name: tests/test_reconcile:_setup
  lines: 9-18
  signature: 'def _setup(tmp_path: Path) -> Path'
- kind: function
  qualified_name: tests/test_reconcile:test_no_orphans_when_sources_exist
  lines: 21-29
  signature: 'def test_no_orphans_when_sources_exist(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_reconcile:test_orphan_when_source_deleted
  lines: 32-41
  signature: 'def test_orphan_when_source_deleted(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_reconcile:test_user_authored_triefact_left_alone
  lines: 44-50
  signature: 'def test_user_authored_triefact_left_alone(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_reconcile:test_remove_actually_deletes
  lines: 53-63
  signature: 'def test_remove_actually_deletes(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_reconcile:test_no_triefacts_dir_returns_empty
  lines: 66-69
  signature: 'def test_no_triefacts_dir_returns_empty(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_reconcile:test_excluded_source_treated_as_orphan
  lines: 72-91
  signature: 'def test_excluded_source_treated_as_orphan(tmp_path: Path)'
incoming_refs: 0
outgoing_refs: 18
---
<!-- trie:section symbol=tests/test_reconcile:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=d855235855481fca1ffa75a5561327563d5eb76f879e2a3faf2baf102f7de6c7 source_ref=5c53604691e3b54c961be79f3f3277d0c20a70bc role=test-infrastructure -->
Tests for orphan triefact detection and removal functionality in the reconcile module.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_reconcile:_setup fingerprint=9635d698397eed755ba54f18855a451e5f737f90ab053c81317de51f20a18b4a body_fp=c4c0d4c83c813ba4830e71b2ba7fbab75872ea50e966dafb675070c6d7612b0b source_ref=5c53604691e3b54c961be79f3f3277d0c20a70bc role=test-infrastructure -->
## `def _setup(tmp_path: Path) -> Path`

Creates test trie.toml config file in the given temporary directory and returns the path.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_reconcile:test_no_orphans_when_sources_exist fingerprint=d31b08271a892838d6bc6f89fc5a8bb5052e1dcde8b8b02612530285e41b686f body_fp=24cd15287f90f99b3830af76400a815be0b7a6b3abb5dc0318a5acd609c84ce2 source_ref=5c53604691e3b54c961be79f3f3277d0c20a70bc role=test -->
## `def test_no_orphans_when_sources_exist(tmp_path: Path)`

Tests that `find_orphan_triefacts` returns no orphans when triefact source files exist and are in scope.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_reconcile:test_orphan_when_source_deleted fingerprint=9f13272e7b95884eb5f097a5aa01e09682565328c4001d5c51e6943938cd6746 body_fp=458674b924b97fd393adf07b0b1a8dc37e2ff3bf201ea76636199273b102c56a source_ref=5c53604691e3b54c961be79f3f3277d0c20a70bc role=test -->
## `def test_orphan_when_source_deleted(tmp_path: Path)`

Verifies that find_orphan_triefacts correctly identifies orphaned triefacts when their source files no longer exist.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_reconcile:test_user_authored_triefact_left_alone fingerprint=f7e0b52e0293c96a859e10c8404939b3c5d53e6a31d935c3c93b650a7aeffae7 body_fp=4e00a0a658f80baf21b2454e5e901d323cb54679a57fc0bad9b8081e3db2c3c4 source_ref=5c53604691e3b54c961be79f3f3277d0c20a70bc role=test -->
## `def test_user_authored_triefact_left_alone(tmp_path: Path)`

Verifies that user-authored triefacts without trie_version front-matter are not identified as orphans.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_reconcile:test_remove_actually_deletes fingerprint=e9e70bd5366d12b0d5cb0285a42b15a9ebd2f3443133380b49c1b6e7282ac4c0 body_fp=c4020274c5379f405d511a0449a501940e64130dfab29efb544013cf08d36e22 source_ref=5c53604691e3b54c961be79f3f3277d0c20a70bc role=test -->
## `def test_remove_actually_deletes(tmp_path: Path)`

Verifies that remove_orphan_triefacts actually deletes orphaned triefact files from the filesystem.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_reconcile:test_no_triefacts_dir_returns_empty fingerprint=5b3994f1ca5f53fd535022d1aa83e221c8e1598daf002bf1ec066a2e19f5a396 body_fp=59beb53f5bb12b56527ed7c1017261f8ecdc265cab1a0eda4e89a5b15c4ae736 source_ref=5c53604691e3b54c961be79f3f3277d0c20a70bc role=test -->
## `def test_no_triefacts_dir_returns_empty(tmp_path: Path)`

Verifies that `find_orphan_triefacts` returns an empty list when the triefacts directory does not exist.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_reconcile:test_excluded_source_treated_as_orphan fingerprint=51f3b95780e73d907221d3b2b525cce77bf2a2119a05633c3389661f3bd94cbe body_fp=dfd56b33c7a602310c7a7d6785b50cd5f25789087e5b3665586b568770516211 source_ref=5c53604691e3b54c961be79f3f3277d0c20a70bc role=test -->
## `def test_excluded_source_treated_as_orphan(tmp_path: Path)`

Tests that triefacts become orphaned when their source files are excluded by scope configuration.
<!-- trie:end -->