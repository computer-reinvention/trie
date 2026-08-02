---
trie_version: 0.3.0
source: tests/test_index.py
file_fingerprint: 5d822ac85d723c1fbfe185633ec97d61f1850f1b37517f1d296a09ac522bf0e1
last_synced_at: '2026-08-02T21:19:20Z'
defines:
- kind: module
  qualified_name: tests/test_index:__module__
  lines: 1-113
- kind: function
  qualified_name: tests/test_index:_project
  lines: 12-68
  signature: 'def _project(tmp_path: Path) -> tuple[Config, Store]'
- kind: function
  qualified_name: tests/test_index:test_build_index_shape
  lines: 71-89
  signature: 'def test_build_index_shape(tmp_path: Path) -> None'
- kind: function
  qualified_name: tests/test_index:test_write_index_and_idempotence
  lines: 92-102
  signature: 'def test_write_index_and_idempotence(tmp_path: Path) -> None'
- kind: function
  qualified_name: tests/test_index:test_write_index_without_tree_is_noop
  lines: 105-112
  signature: 'def test_write_index_without_tree_is_noop(tmp_path: Path) -> None'
incoming_refs: 0
outgoing_refs: 15
---
<!-- trie:section symbol=tests/test_index:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=05870e363a79953e65f02fd1f109866ef83a6d2dae59c54f0a448ca52d4d6242 source_ref=5ed21ef55342be836e62e34317d6f8102cf13d1f role=test -->
Tests for `trie.index` covering `build_index` output shape, `write_index` idempotence, and no-op behaviour when no triefact tree exists.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_index:_project fingerprint=ed4f67314d1f3d94cbc44b1eab2eafd9f62f938e29079f3c2a7b42d9e2c4aece body_fp=e5e3fe9b3bb14d57fffa657ae9a4cdf9b50c9177f6d3cab6e732ec34f3334758 source_ref=5ed21ef55342be836e62e34317d6f8102cf13d1f role=test -->
## `def _project(tmp_path: Path) -> tuple[Config, Store]`

Build a minimal fake project under `tmp_path` with source files, a populated `Store`, and a triefact tree, returning the `Config` and `Store` for index tests.

- Returns an open `Store`; callers must close it after use.
- Injects a `call` edge and a `triefact_sections` row directly via SQL to satisfy index ranking and one-liner display logic.
- Creates a `triediffs` subdirectory to exercise digest-archive exclusion in index tests.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_index:test_build_index_shape fingerprint=35b264463162b8f6f45cb68d94269e12e33f7b96a9f531ef76004e248994a6a2 body_fp=d011d64f32cd44571f737e59be3493ccc90a8df16eecf9a693ebe3d1a1da7b50 source_ref=5ed21ef55342be836e62e34317d6f8102cf13d1f role=test -->
## `def test_build_index_shape(tmp_path: Path) -> None`

Verify that `build_index` produces output containing the index marker, ranked public symbols with one-liners, per-directory file TOC with descriptions, and no digest-archive or self-referential entries.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_index:test_write_index_and_idempotence fingerprint=10fa7279a9c9bba0824b473f1938e64027a76535f0efa7f697b7b1ceaf0f5dad body_fp=beffeadfa394dd4feb834cffd941122c9bf8561989004aa2d2dcdd087aa5f004 source_ref=5ed21ef55342be836e62e34317d6f8102cf13d1f role=test -->
## `def test_write_index_and_idempotence(tmp_path: Path) -> None`

Verify `write_index` writes `README.md` and produces identical output on a second invocation.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_index:test_write_index_without_tree_is_noop fingerprint=b7f8d8347cfc8ae25c0f5c9e5727bb1d46974c52edf5a1b43a667a9766eae85f body_fp=ce735b2fbc0aec521dcc803350f58456984cb87f793130407131d26b51717147 source_ref=5ed21ef55342be836e62e34317d6f8102cf13d1f role=test -->
## `def test_write_index_without_tree_is_noop(tmp_path: Path) -> None`

Assert that `write_index` returns `None` when no triefacts tree exists in the project root.
<!-- trie:end -->