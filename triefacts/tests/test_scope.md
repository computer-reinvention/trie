---
trie_version: 0.1.0
source: tests/test_scope.py
file_fingerprint: a51ea69b9e98556ed79b176802dbd1c3e0393f6eb0f02f61cb7a279ce4cf309e
last_synced_at: '2026-05-14T17:29:52Z'
defines:
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
<!-- trie:section symbol=tests/test_scope:test_basic_include fingerprint=3b65256bb28a29e6c392926158bc659baf5204924341ac31db6ed0f585ebefcb body_fp=3ba57325529ac24700d24bfeb04971cc041273093600cf93df73c2d1e256c184 -->
## `test_basic_include(tmp_path: Path)`

Verify `discover_files` returns only files matching the include glob, across nested directories.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_scope:test_exclude_directory fingerprint=383d6781483cbfb4361e7407b436bf34d3a054f1325667d91d1b2ad73266bf56 body_fp=27175e8d63a98894d882b1804832f9d85ba30ecb177ce3d108a3a444d6646496 -->
## `test_exclude_directory(tmp_path: Path)`

Verify that `discover_files` omits all files under an excluded directory glob.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_scope:test_exclude_specific_file fingerprint=4baa747142f07c7592c91a847daca43be9945de037d6d99723fee7b4cf9fa802 body_fp=7f19c29e2c984457365aef353b813589b1e3452def96ff4925c34fcb4ff5a11b -->
## `test_exclude_specific_file(tmp_path: Path)`

Verify that a single explicitly named file is excluded from `discover_files` results.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_scope:test_multiple_includes_unioned fingerprint=b1a59d3bc1f38dd45871cd07fee5b468c794e02f9c23bb3b9276787aae828dd7 body_fp=cb6d1ace6b3458abd378e2f90585371ca409c642cb325603aa2ac44e8d235d3d -->
## `test_multiple_includes_unioned(tmp_path: Path)`

Verify that multiple glob patterns in `include` are unioned, matching files from all patterns while excluding unmatched types.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_scope:test_default_excludes_skip_pycache_and_venv fingerprint=dd9ea87e5daa349b9313e5c370ce2503dd3e43df48fe2c1f5bae579dcdf9d16d body_fp=1d89c71579d326c2cf94f7e3db3fd9d1b4602f62251f063435778791a086c7d3 -->
## `test_default_excludes_skip_pycache_and_venv(tmp_path: Path)`

Verify that a default `Scope` excludes `__pycache__` and `.venv` directories from discovered files.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_scope:test_no_matches_returns_empty fingerprint=67f6bc2f9714a43836512c337cec17513dd8afc097485d46ecdf906d8bfd9830 body_fp=dc81dcc825a86563d5c458ffef2730faf1b3e37563a12f471537f870428066d8 -->
## `test_no_matches_returns_empty(tmp_path: Path)`

Assert that `discover_files` returns an empty list when no files match the include pattern.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_scope:test_returns_sorted fingerprint=da766808f9eee1661e5d8114c561f3f44343332094404e982d70a8424362fdee body_fp=1a4de12b79a93cac92db4969a02a1e6458330c2d7283c48dea7d229e2f49b5d4 -->
## `test_returns_sorted(tmp_path: Path)`

Assert that `discover_files` returns paths in sorted order.
<!-- trie:end -->