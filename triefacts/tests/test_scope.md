---
trie_version: 0.1.5
source: tests/test_scope.py
file_fingerprint: a51ea69b9e98556ed79b176802dbd1c3e0393f6eb0f02f61cb7a279ce4cf309e
last_synced_at: '2026-05-28T01:40:19Z'
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
<!-- trie:section symbol=tests/test_scope:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=692e35f19131cf249150c77d3472085f2ce3dc84d9e94c3a80a1e91bced3918d source_ref=bd44eb44cf2776e5fc7c1af37e5a76bd75db4836 -->
## `tests/test_scope`

Test `discover_files` against glob include/exclude patterns using a temporary filesystem.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_scope:_touch fingerprint=7f9bceb734fe3336297747674f3903c7f8df21766031b524275430cc173a776f body_fp=ea710bd092c8f9b30f3115bf19a08a29f9d4d87e4bb0f6282cb6f97debc0ba80 source_ref=bd44eb44cf2776e5fc7c1af37e5a76bd75db4836 -->
## `_touch(p: Path, content: str = "") -> None`

Create a file at `p`, making all parent directories as needed.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_scope:test_basic_include fingerprint=3b65256bb28a29e6c392926158bc659baf5204924341ac31db6ed0f585ebefcb body_fp=bf61977a2570a60e221a510f612bf4263b17724abc02601f4457c9f58328a9c9 source_ref=bd44eb44cf2776e5fc7c1af37e5a76bd75db4836 -->
## `test_basic_include(tmp_path: Path)`

Verify that `discover_files` returns only `.py` files matched by a glob include pattern, ignoring non-matching extensions.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_scope:test_exclude_directory fingerprint=383d6781483cbfb4361e7407b436bf34d3a054f1325667d91d1b2ad73266bf56 body_fp=27175e8d63a98894d882b1804832f9d85ba30ecb177ce3d108a3a444d6646496 source_ref=bd44eb44cf2776e5fc7c1af37e5a76bd75db4836 -->
## `test_exclude_directory(tmp_path: Path)`

Verify that `discover_files` omits all files under an excluded directory glob.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_scope:test_exclude_specific_file fingerprint=4baa747142f07c7592c91a847daca43be9945de037d6d99723fee7b4cf9fa802 body_fp=f3f02ce47852004577e7240dc5b00612ee260679c581eccc5766f39f053b29c9 source_ref=bd44eb44cf2776e5fc7c1af37e5a76bd75db4836 -->
## `test_exclude_specific_file(tmp_path: Path)`

Verify that `discover_files` omits a single explicitly excluded file by name.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_scope:test_multiple_includes_unioned fingerprint=b1a59d3bc1f38dd45871cd07fee5b468c794e02f9c23bb3b9276787aae828dd7 body_fp=723bcd4074a0f020190eadf5271453c4cd01e8a9f66ba998059b1be3e7ca23a8 source_ref=bd44eb44cf2776e5fc7c1af37e5a76bd75db4836 -->
## `test_multiple_includes_unioned(tmp_path: Path)`

Verify that multiple `include` patterns are unioned, matching files from all patterns while excluding unmatched types.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_scope:test_default_excludes_skip_pycache_and_venv fingerprint=dd9ea87e5daa349b9313e5c370ce2503dd3e43df48fe2c1f5bae579dcdf9d16d body_fp=04cfb8b2882115b9f4c64f410a8c71ad6c7e0b784491ee95a695b5cc49143e52 source_ref=bd44eb44cf2776e5fc7c1af37e5a76bd75db4836 -->
## `test_default_excludes_skip_pycache_and_venv(tmp_path: Path)`

Assert that a default `Scope` excludes `__pycache__` and `.venv` directories from `discover_files` results.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_scope:test_no_matches_returns_empty fingerprint=67f6bc2f9714a43836512c337cec17513dd8afc097485d46ecdf906d8bfd9830 body_fp=dc81dcc825a86563d5c458ffef2730faf1b3e37563a12f471537f870428066d8 source_ref=bd44eb44cf2776e5fc7c1af37e5a76bd75db4836 -->
## `test_no_matches_returns_empty(tmp_path: Path)`

Assert that `discover_files` returns an empty list when no files match the include pattern.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_scope:test_returns_sorted fingerprint=da766808f9eee1661e5d8114c561f3f44343332094404e982d70a8424362fdee body_fp=1a4de12b79a93cac92db4969a02a1e6458330c2d7283c48dea7d229e2f49b5d4 source_ref=bd44eb44cf2776e5fc7c1af37e5a76bd75db4836 -->
## `test_returns_sorted(tmp_path: Path)`

Assert that `discover_files` returns paths in sorted order.
<!-- trie:end -->