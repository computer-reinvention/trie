---
trie_version: 0.1.5
source: tests/test_reconcile.py
file_fingerprint: 6c61486e145c55ceb6940129dc0e62fcca2d88325e26ddf1de672c4ad51c8ac7
last_synced_at: '2026-06-06T13:24:03Z'
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
<!-- trie:section symbol=tests/test_reconcile:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=d855235855481fca1ffa75a5561327563d5eb76f879e2a3faf2baf102f7de6c7 source_ref=5c53604691e3b54c961be79f3f3277d0c20a70bc role=test-infrastructure -->
Tests for orphan triefact detection and removal functionality in the reconcile module.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_reconcile:_setup fingerprint=9635d698397eed755ba54f18855a451e5f737f90ab053c81317de51f20a18b4a body_fp=82a3dfccd30134ef3984eba4c93bd48732963452bd13b52840c4e33e425c7f0b source_ref=5c53604691e3b54c961be79f3f3277d0c20a70bc role=test-infrastructure -->
Creates test trie.toml config file in the given temporary directory and returns the path.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_reconcile:test_no_orphans_when_sources_exist fingerprint=d31b08271a892838d6bc6f89fc5a8bb5052e1dcde8b8b02612530285e41b686f body_fp=a805af5d05f15f8bd4fd533c7f72f6ac5fd36d767f468233666bc78ab72f5928 source_ref=5c53604691e3b54c961be79f3f3277d0c20a70bc role=documentation-sync -->
Tests that find_orphan_triefacts returns no orphans when triefact source files exist and are in scope.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_reconcile:test_orphan_when_source_deleted fingerprint=9f13272e7b95884eb5f097a5aa01e09682565328c4001d5c51e6943938cd6746 body_fp=4e7e6674104a30df75f9a9b8961b78f6184ff6f1259014be1e71a9ee355ac759 source_ref=5c53604691e3b54c961be79f3f3277d0c20a70bc role=documentation-sync -->
Verifies that find_orphan_triefacts correctly identifies orphaned triefacts when their source files no longer exist.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_reconcile:test_user_authored_triefact_left_alone fingerprint=f7e0b52e0293c96a859e10c8404939b3c5d53e6a31d935c3c93b650a7aeffae7 body_fp=f3827b68b811a9658f7118394eb2ef19427d802c94d1db4e0ce9142eeecdcee0 source_ref=5c53604691e3b54c961be79f3f3277d0c20a70bc role=documentation-sync -->
Verifies that user-authored triefacts without trie_version front-matter are not identified as orphans.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_reconcile:test_remove_actually_deletes fingerprint=e9e70bd5366d12b0d5cb0285a42b15a9ebd2f3443133380b49c1b6e7282ac4c0 body_fp=3ec85102b3445ea2306a2ce669a77a4fef2a88182f4425975fbf809852962c19 source_ref=5c53604691e3b54c961be79f3f3277d0c20a70bc role=documentation-sync -->
Verifies that remove_orphan_triefacts actually deletes orphaned triefact files from the filesystem.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_reconcile:test_no_triefacts_dir_returns_empty fingerprint=5b3994f1ca5f53fd535022d1aa83e221c8e1598daf002bf1ec066a2e19f5a396 body_fp=978acb0f36e8b4edc23f73962a66a0d73e6fffd867b9ded7e313758d9f05dda4 source_ref=5c53604691e3b54c961be79f3f3277d0c20a70bc role=documentation-sync -->
Verifies that `find_orphan_triefacts` returns an empty list when the triefacts directory does not exist.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_reconcile:test_excluded_source_treated_as_orphan fingerprint=51f3b95780e73d907221d3b2b525cce77bf2a2119a05633c3389661f3bd94cbe body_fp=b89a37bf37592f306d21845922e06dea9c12e9cddadc2ab75c49270293535743 source_ref=5c53604691e3b54c961be79f3f3277d0c20a70bc role=documentation-sync -->
Tests that triefacts become orphaned when their source files are excluded by scope configuration.
<!-- trie:end -->








