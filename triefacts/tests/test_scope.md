---
trie_version: 0.3.0
source: tests/test_scope.py
file_fingerprint: a51ea69b9e98556ed79b176802dbd1c3e0393f6eb0f02f61cb7a279ce4cf309e
last_synced_at: '2026-07-29T17:55:31Z'
defines:
- kind: module
  qualified_name: tests/test_scope:__module__
  lines: 1-81
- kind: function
  qualified_name: tests/test_scope:_touch
  lines: 9-11
  signature: 'def _touch(p: Path, content: str = "") -> None'
- kind: function
  qualified_name: tests/test_scope:test_basic_include
  lines: 14-20
  signature: 'def test_basic_include(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_scope:test_exclude_directory
  lines: 23-32
  signature: 'def test_exclude_directory(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_scope:test_exclude_specific_file
  lines: 35-43
  signature: 'def test_exclude_specific_file(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_scope:test_multiple_includes_unioned
  lines: 46-55
  signature: 'def test_multiple_includes_unioned(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_scope:test_default_excludes_skip_pycache_and_venv
  lines: 58-65
  signature: 'def test_default_excludes_skip_pycache_and_venv(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_scope:test_no_matches_returns_empty
  lines: 68-71
  signature: 'def test_no_matches_returns_empty(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_scope:test_returns_sorted
  lines: 74-80
  signature: 'def test_returns_sorted(tmp_path: Path)'
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
<!-- trie:section symbol=tests/test_scope:_touch fingerprint=7f9bceb734fe3336297747674f3903c7f8df21766031b524275430cc173a776f body_fp=545250f04de913d353d3317f59d047e4b94fbe722cb9a950237280793e5eff9e source_ref=bd44eb44cf2776e5fc7c1af37e5a76bd75db4836 role=test-infrastructure -->
## `def _touch(p: Path, content: str = "") -> None`

Creates a file at the given path with optional content, creating parent directories as needed.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_scope:test_basic_include fingerprint=3b65256bb28a29e6c392926158bc659baf5204924341ac31db6ed0f585ebefcb body_fp=58637a05c3fed38f293ed3ba1df08903f6efdb11e2a9e077748b3d081174f278 source_ref=bd44eb44cf2776e5fc7c1af37e5a76bd75db4836 role=test -->
## `def test_basic_include(tmp_path: Path)`

Tests that `discover_files` includes only Python files matching glob patterns and ignores non-matching extensions.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_scope:test_exclude_directory fingerprint=383d6781483cbfb4361e7407b436bf34d3a054f1325667d91d1b2ad73266bf56 body_fp=33c21bc50703b6769dbd0e72fb65d6b93763da0849895eab164d6f6523cb48e1 source_ref=bd44eb44cf2776e5fc7c1af37e5a76bd75db4836 role=test -->
## `def test_exclude_directory(tmp_path: Path)`

Verifies that discover_files correctly excludes entire directories using glob patterns.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_scope:test_exclude_specific_file fingerprint=4baa747142f07c7592c91a847daca43be9945de037d6d99723fee7b4cf9fa802 body_fp=e5e2fe1b33fb295ccac140c0a93a66970ee259a44e09adb243b9ffd1be9fff21 source_ref=bd44eb44cf2776e5fc7c1af37e5a76bd75db4836 role=test -->
## `def test_exclude_specific_file(tmp_path: Path)`

Tests that discover_files excludes specific files matching exclude patterns while including others.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_scope:test_multiple_includes_unioned fingerprint=b1a59d3bc1f38dd45871cd07fee5b468c794e02f9c23bb3b9276787aae828dd7 body_fp=c48a7d6cf402eaf3962998f19ff43dfaefb1ac119b8466ea8bfe494d601d9a4d source_ref=bd44eb44cf2776e5fc7c1af37e5a76bd75db4836 role=test -->
## `def test_multiple_includes_unioned(tmp_path: Path)`

Verifies that discover_files unions multiple include patterns to find both .py and .pyi files.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_scope:test_default_excludes_skip_pycache_and_venv fingerprint=dd9ea87e5daa349b9313e5c370ce2503dd3e43df48fe2c1f5bae579dcdf9d16d body_fp=67af254d5a42ea474c34356aef0bf70f983e5d6eda4e664e1cf75c285b18bc2d source_ref=bd44eb44cf2776e5fc7c1af37e5a76bd75db4836 role=test -->
## `def test_default_excludes_skip_pycache_and_venv(tmp_path: Path)`

Verifies that default Scope configuration excludes `__pycache__` and `.venv` directories from file discovery.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_scope:test_no_matches_returns_empty fingerprint=67f6bc2f9714a43836512c337cec17513dd8afc097485d46ecdf906d8bfd9830 body_fp=d4cf47efe338e7c6438252333a74477181ae6f02e24377fb7ad2cf14f4dc1586 source_ref=bd44eb44cf2776e5fc7c1af37e5a76bd75db4836 role=test -->
## `def test_no_matches_returns_empty(tmp_path: Path)`

Verifies discover_files returns empty list when no files match the scope patterns.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_scope:test_returns_sorted fingerprint=da766808f9eee1661e5d8114c561f3f44343332094404e982d70a8424362fdee body_fp=ac6bb143b401d668bbca52a65d6b6a30eca29cba38d09f9aaad3f28deb4aa234 source_ref=bd44eb44cf2776e5fc7c1af37e5a76bd75db4836 role=test -->
## `def test_returns_sorted(tmp_path: Path)`

Verifies that discover_files returns file paths in sorted order when multiple files match the scope pattern.
<!-- trie:end -->