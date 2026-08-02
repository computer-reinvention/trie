---
trie_version: 0.3.0
source: tests/test_registry.py
file_fingerprint: a29fa8656a110e6078dc7d7ed4a357d67312278da609535c57db08cf95078dff
last_synced_at: '2026-07-29T01:49:13Z'
defines:
- kind: module
  qualified_name: tests/test_registry:__module__
  lines: 1-72
- kind: constant
  qualified_name: tests/test_registry:FIXTURE_PY
  lines: 10-10
- kind: constant
  qualified_name: tests/test_registry:FIXTURE_TS
  lines: 11-11
- kind: function
  qualified_name: tests/test_registry:test_python_and_typescript_registered
  lines: 14-17
  signature: def test_python_and_typescript_registered()
- kind: function
  qualified_name: tests/test_registry:test_get_backend_by_name
  lines: 20-23
  signature: def test_get_backend_by_name()
- kind: function
  qualified_name: tests/test_registry:test_extension_dispatch
  lines: 26-31
  signature: def test_extension_dispatch()
- kind: function
  qualified_name: tests/test_registry:test_dts_wins_over_ts
  lines: 34-37
  signature: 'def test_dts_wins_over_ts(): # Longest-suffix-first: a .d.ts file must route via the .d.ts mapping, not .ts.'
- kind: function
  qualified_name: tests/test_registry:test_source_suffixes_longest_first
  lines: 40-45
  signature: def test_source_suffixes_longest_first()
- kind: function
  qualified_name: tests/test_registry:test_is_indexable
  lines: 48-51
  signature: def test_is_indexable()
- kind: function
  qualified_name: tests/test_registry:test_backends_satisfy_protocol
  lines: 54-56
  signature: def test_backends_satisfy_protocol()
- kind: function
  qualified_name: tests/test_registry:test_dispatch_extract_symbols_python
  lines: 59-61
  signature: def test_dispatch_extract_symbols_python()
- kind: function
  qualified_name: tests/test_registry:test_dispatch_extract_symbols_typescript
  lines: 64-66
  signature: def test_dispatch_extract_symbols_typescript()
- kind: function
  qualified_name: tests/test_registry:test_dispatch_rejects_unknown_extension
  lines: 69-71
  signature: def test_dispatch_rejects_unknown_extension()
incoming_refs: 0
outgoing_refs: 11
---
<!-- trie:section symbol=tests/test_registry:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=4deb55d6251eef8f8e787b03a21cc37b80ac1c95bfe5da3b69c2c910711544bd source_ref=d3041ed221ac8cc762a2087a6b59242c542b9989 role=test -->
Test module verifying `trie.parse.registry` backend registration, extension dispatch, suffix ordering, and symbol extraction for Python and TypeScript fixtures.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_registry:FIXTURE_PY fingerprint=2815efb76440ae36b1194e521377b9b585a04f988d4293950189ad8d21c8895c body_fp=04052ed02063d3121b61b08172622e38f971478c3cff7921dd68200f3700a013 source_ref=d3041ed221ac8cc762a2087a6b59242c542b9989 role=test -->
Path to the `tiny_repo` fixture directory used as the Python source root in tests.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_registry:FIXTURE_TS fingerprint=6e05a4a41d56d5af67d98ccf50275cb37266196a0e428de8400292da978771e2 body_fp=4be2d9d58e412ec115fdaf29b42b87483357e3a1e91e31d6e2e9a7ee1c905308 source_ref=d3041ed221ac8cc762a2087a6b59242c542b9989 role=test -->
Path constant pointing to the `tiny_ts_repo` TypeScript fixture directory used by registry tests.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_registry:test_python_and_typescript_registered fingerprint=6c24a9dbc285f02d70b650a533d922c659b2504bffa00cf4a8f1bcfbd2d1f39a body_fp=f4a0685c2ea39672af0cc25a1ee7edb4913e45384822bbd550a146bf030c56c3 source_ref=d3041ed221ac8cc762a2087a6b59242c542b9989 role=test -->
## `def test_python_and_typescript_registered()`

Assert that both `"python"` and `"typescript"` backends are present in `registry.all_backends()`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_registry:test_get_backend_by_name fingerprint=a9e2b8cbf1762d5e77864215336e616cec779d37fcc3df5c55d086a2672f6623 body_fp=7fe3dee0da949508912827c8227d673d702953fd613f8640def63c99286de057 source_ref=d3041ed221ac8cc762a2087a6b59242c542b9989 role=test -->
## `def test_get_backend_by_name()`

Verify that `registry.get_backend` resolves known language names and returns `None` for unknown ones.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_registry:test_extension_dispatch fingerprint=36fea8c0fc87bd37000ff2fe8998acbe779d0b76d0be1c6e994412a761a41e89 body_fp=d5b261b30f480f6d1bb0878a14c7468e32eaf85f91d78aa5a3fd489c76de8330 source_ref=d3041ed221ac8cc762a2087a6b59242c542b9989 role=test -->
## `def test_extension_dispatch()`

Verify `registry.get_backend_for_file` routes `.py`, `.ts`, `.tsx`, and `.d.ts` to correct backends and returns `None` for `.txt`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_registry:test_dts_wins_over_ts fingerprint=271cb6ab16556aad9b6ff5a2be66c5228ad1a3d65d5577529b74e381398d7601 body_fp=b6d1f50030d690fd2d29480b300d5280a3c750ea7c99035f024adc0b34c3cda3 source_ref=d3041ed221ac8cc762a2087a6b59242c542b9989 role=test -->
## `def test_dts_wins_over_ts(): # Longest-suffix-first: a .d.ts file must route via the .d.ts mapping, not .ts.`

Assert that `registry.get_backend_for_file` routes `.d.ts` files to the TypeScript backend via the longest-suffix match, not the shorter `.ts` mapping.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_registry:test_source_suffixes_longest_first fingerprint=6323c5556073218b13a3e07948b396e2479de815f261c1944baf41fe81ba2c19 body_fp=6d0c9755b3574a946b2059535fb74ea4e7f9952c26cd1b5b37789ce32cd0e3db source_ref=d3041ed221ac8cc762a2087a6b59242c542b9989 role=test -->
## `def test_source_suffixes_longest_first()`

Assert that `registry.source_suffixes()` returns `.d.ts` before `.ts`, ensuring longest-suffix-first matching.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_registry:test_is_indexable fingerprint=e311f4a57e233275166e0f3d9b16b370ded7d96f63639f84ae2868d70d263377 body_fp=56f3c649b85c453a78db86368080cb280e629fbb4c9142e05246885631020b6b source_ref=d3041ed221ac8cc762a2087a6b59242c542b9989 role=test -->
## `def test_is_indexable()`

Verify that `registry.is_indexable` returns `True` for `.py` and `.ts` files and `False` for `.md`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_registry:test_backends_satisfy_protocol fingerprint=0b7723ec40dbc748ca4df11d22ecbbf3a5b904b4e61a1439fc634108d86c86f3 body_fp=f5c1ff8221190c6c8d13568e735872ee15e442d38b2bfd48f82aac0c9276e272 source_ref=d3041ed221ac8cc762a2087a6b59242c542b9989 role=test -->
## `def test_backends_satisfy_protocol()`

Assert that every backend returned by `registry.all_backends()` is an instance of `LanguageBackend`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_registry:test_dispatch_extract_symbols_python fingerprint=cc4d99ddd425c0c654534dd25a0d7920f3dcdda2ec181e0b74af5726a039de06 body_fp=7a0dc7810fb28ac272b35103c788962c9fa5445a0b9e2b6c60da2fac6e14bb8d source_ref=d3041ed221ac8cc762a2087a6b59242c542b9989 role=test -->
## `def test_dispatch_extract_symbols_python()`

Verify that `registry.extract_symbols` returns at least one function-kind symbol from the Python fixture file `calculator.py`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_registry:test_dispatch_extract_symbols_typescript fingerprint=21082cde6145e9bd8e92d44ebaa65b51397c5e6a7bf62df41852f2be0babf36a body_fp=bc7b55102457fcb35a5343337bc20d80a75ccb4665365d9c0d34dd715ecd706e source_ref=d3041ed221ac8cc762a2087a6b59242c542b9989 role=test -->
## `def test_dispatch_extract_symbols_typescript()`

Verify that `registry.extract_symbols` parses a TypeScript fixture file and returns a symbol with qualified name `"src/util:double"`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_registry:test_dispatch_rejects_unknown_extension fingerprint=561e172da05906ec325b275a74f6620224fd5b2fff499790b2337a7aeb72d817 body_fp=9076fda4c860fa306196497786f8babe1ebc5583a582900133857c74e7e570a3 source_ref=d3041ed221ac8cc762a2087a6b59242c542b9989 role=test -->
## `def test_dispatch_rejects_unknown_extension()`

Assert that `registry.extract_symbols` raises `ValueError` when called with an unrecognised file extension.
<!-- trie:end -->