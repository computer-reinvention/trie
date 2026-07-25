---
trie_version: 0.1.9
source: tests/test_scope.py
file_fingerprint: a51ea69b9e98556ed79b176802dbd1c3e0393f6eb0f02f61cb7a279ce4cf309e
last_synced_at: '2026-07-25T10:44:27Z'
defines:
- kind: module
  qualified_name: tests/test_scope:__module__
  lines: 1-81
- kind: function
  qualified_name: tests/test_scope:_touch
  lines: 9-11
- kind: function
  qualified_name: tests/test_scope:test_basic_include
  lines: 14-20
- kind: function
  qualified_name: tests/test_scope:test_exclude_directory
  lines: 23-32
- kind: function
  qualified_name: tests/test_scope:test_exclude_specific_file
  lines: 35-43
- kind: function
  qualified_name: tests/test_scope:test_multiple_includes_unioned
  lines: 46-55
- kind: function
  qualified_name: tests/test_scope:test_default_excludes_skip_pycache_and_venv
  lines: 58-65
- kind: function
  qualified_name: tests/test_scope:test_no_matches_returns_empty
  lines: 68-71
- kind: function
  qualified_name: tests/test_scope:test_returns_sorted
  lines: 74-80
incoming_refs: 0
outgoing_refs: 14
---
<!-- trie:section symbol=tests/test_scope:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=cc0496b217d24701f3a0f5ed6071db4f679bad19d4da751b0470f8f71980f4a2 source_ref=bd44eb44cf2776e5fc7c1af37e5a76bd75db4836 role=test-infrastructure -->
Tests the file discovery functionality in `trie.scope.discover_files` with various include/exclude patterns.

- `_touch`: Creates test files with optional content in temporary directories
- `test_basic_include`: Verifies basic glob pattern inclusion for Python files
- `test_exclude_directory`: Tests directory-level exclusion patterns
- `test_exclude_specific_file`: Tests single file exclusion
- `test_multiple_includes_unioned`: Verifies multiple include patterns are combined
- `test_default_excludes_skip_pycache_and_venv`: Tests default exclusions for cache/venv directories
- `test_no_matches_returns_empty`: Verifies empty results when no files match
- `test_returns_sorted`: Ensures results are returned in sorted order
<!-- trie:end -->
<!-- trie:section symbol=tests/test_scope:_touch fingerprint=7f9bceb734fe3336297747674f3903c7f8df21766031b524275430cc173a776f body_fp=1b06eb321b892a26dc46b01da4852f864c71ad3d87452511986768e4590405b6 source_ref=bd44eb44cf2776e5fc7c1af37e5a76bd75db4836 role=test-infrastructure -->
Creates a file at the given path with optional content, creating parent directories as needed.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_scope:test_basic_include fingerprint=3b65256bb28a29e6c392926158bc659baf5204924341ac31db6ed0f585ebefcb body_fp=754aabdb44cad8fe767c95ccc2ecf3ca857fd27390ca48290a0ca4cbc77057ce source_ref=bd44eb44cf2776e5fc7c1af37e5a76bd75db4836 role=test -->
Tests that `discover_files` includes only Python files matching glob patterns and ignores non-matching extensions.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_scope:test_exclude_directory fingerprint=383d6781483cbfb4361e7407b436bf34d3a054f1325667d91d1b2ad73266bf56 body_fp=538c7549c68dc1561ad71c91ded0b3de9850729767e4b640bebe6412b7b07243 source_ref=bd44eb44cf2776e5fc7c1af37e5a76bd75db4836 role=test -->
Verifies that discover_files correctly excludes entire directories using glob patterns.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_scope:test_exclude_specific_file fingerprint=4baa747142f07c7592c91a847daca43be9945de037d6d99723fee7b4cf9fa802 body_fp=d54d480389c827af08b9fc0543d9b83ece41821c4125082f26af065d4d1ea3ef source_ref=bd44eb44cf2776e5fc7c1af37e5a76bd75db4836 role=test -->
Tests that discover_files excludes specific files matching exclude patterns while including others.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_scope:test_multiple_includes_unioned fingerprint=b1a59d3bc1f38dd45871cd07fee5b468c794e02f9c23bb3b9276787aae828dd7 body_fp=c12dc63a1327e4edf02c9ec0909fc041024c203ca9fe6ad46a4ec9f6bd8fddfd source_ref=bd44eb44cf2776e5fc7c1af37e5a76bd75db4836 role=test -->
Verifies that discover_files unions multiple include patterns to find both .py and .pyi files.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_scope:test_default_excludes_skip_pycache_and_venv fingerprint=dd9ea87e5daa349b9313e5c370ce2503dd3e43df48fe2c1f5bae579dcdf9d16d body_fp=fcbd92be1bb4be162b8676845e482c5514258b091955c85bedb92ba980c53286 source_ref=bd44eb44cf2776e5fc7c1af37e5a76bd75db4836 role=test -->
Verifies that default Scope configuration excludes `__pycache__` and `.venv` directories from file discovery.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_scope:test_no_matches_returns_empty fingerprint=67f6bc2f9714a43836512c337cec17513dd8afc097485d46ecdf906d8bfd9830 body_fp=cbde4d9ea08fa11ec5b36b987f97ba76bf45e9035d89108350a470f1b5597e06 source_ref=bd44eb44cf2776e5fc7c1af37e5a76bd75db4836 role=test -->
Verifies discover_files returns empty list when no files match the scope patterns.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_scope:test_returns_sorted fingerprint=da766808f9eee1661e5d8114c561f3f44343332094404e982d70a8424362fdee body_fp=25963d78d2447a9c11b01cff6e657e82870313870be2ab352a8bff6fb692b173 source_ref=bd44eb44cf2776e5fc7c1af37e5a76bd75db4836 role=test -->
Verifies that discover_files returns file paths in sorted order when multiple files match the scope pattern.
<!-- trie:end -->