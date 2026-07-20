---
trie_version: 0.1.9
source: tests/test_registry.py
file_fingerprint: a29fa8656a110e6078dc7d7ed4a357d67312278da609535c57db08cf95078dff
last_synced_at: '2026-07-20T09:55:17Z'
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
- kind: function
  qualified_name: tests/test_registry:test_get_backend_by_name
  lines: 20-23
- kind: function
  qualified_name: tests/test_registry:test_extension_dispatch
  lines: 26-31
- kind: function
  qualified_name: tests/test_registry:test_dts_wins_over_ts
  lines: 34-37
- kind: function
  qualified_name: tests/test_registry:test_source_suffixes_longest_first
  lines: 40-45
- kind: function
  qualified_name: tests/test_registry:test_is_indexable
  lines: 48-51
- kind: function
  qualified_name: tests/test_registry:test_backends_satisfy_protocol
  lines: 54-56
- kind: function
  qualified_name: tests/test_registry:test_dispatch_extract_symbols_python
  lines: 59-61
- kind: function
  qualified_name: tests/test_registry:test_dispatch_extract_symbols_typescript
  lines: 64-66
- kind: function
  qualified_name: tests/test_registry:test_dispatch_rejects_unknown_extension
  lines: 69-71
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
<!-- trie:section symbol=tests/test_registry:test_python_and_typescript_registered fingerprint=6c24a9dbc285f02d70b650a533d922c659b2504bffa00cf4a8f1bcfbd2d1f39a body_fp=3f2361ad5c3bd216e39152ff2ddbeeca552715e362b9f2f26a1e08aa291339be source_ref=d3041ed221ac8cc762a2087a6b59242c542b9989 role=test -->
Assert that both `"python"` and `"typescript"` backends are present in `registry.all_backends()`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_registry:test_get_backend_by_name fingerprint=a9e2b8cbf1762d5e77864215336e616cec779d37fcc3df5c55d086a2672f6623 body_fp=5124583f558448fbc2824c93c1b6ae1fe67c9ebc901c4ffc727c0624a7a95dd1 source_ref=d3041ed221ac8cc762a2087a6b59242c542b9989 role=test -->
Verify that `registry.get_backend` resolves known language names and returns `None` for unknown ones.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_registry:test_extension_dispatch fingerprint=36fea8c0fc87bd37000ff2fe8998acbe779d0b76d0be1c6e994412a761a41e89 body_fp=bc5ae3c88e143a185528c86eeb427222717b99f7c73f8d93ff6e90b7fd102bef source_ref=d3041ed221ac8cc762a2087a6b59242c542b9989 role=test -->
Verify `registry.get_backend_for_file` routes `.py`, `.ts`, `.tsx`, and `.d.ts` to correct backends and returns `None` for `.txt`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_registry:test_dts_wins_over_ts fingerprint=271cb6ab16556aad9b6ff5a2be66c5228ad1a3d65d5577529b74e381398d7601 body_fp=0fa2031eef9946980f7f57473e98989411a1d68ce07488cd9e18cc38d570cbd4 source_ref=d3041ed221ac8cc762a2087a6b59242c542b9989 role=test -->
Assert that `registry.get_backend_for_file` routes `.d.ts` files to the TypeScript backend via the longest-suffix match, not the shorter `.ts` mapping.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_registry:test_source_suffixes_longest_first fingerprint=6323c5556073218b13a3e07948b396e2479de815f261c1944baf41fe81ba2c19 body_fp=481c2b012d39580e63cb3522324f4f72ca0dbde1728d31e9ca3bcf868d47d9a9 source_ref=d3041ed221ac8cc762a2087a6b59242c542b9989 role=test -->
Assert that `registry.source_suffixes()` returns `.d.ts` before `.ts`, ensuring longest-suffix-first matching.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_registry:test_is_indexable fingerprint=e311f4a57e233275166e0f3d9b16b370ded7d96f63639f84ae2868d70d263377 body_fp=15970a1d7a5a5b29a5452621311823c4d3dc88ddd14935ae03d40d05784b6437 source_ref=d3041ed221ac8cc762a2087a6b59242c542b9989 role=test -->
Verify that `registry.is_indexable` returns `True` for `.py` and `.ts` files and `False` for `.md`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_registry:test_backends_satisfy_protocol fingerprint=0b7723ec40dbc748ca4df11d22ecbbf3a5b904b4e61a1439fc634108d86c86f3 body_fp=0d93919cd625c5b26c41c3957edd4c13e714ddf3c6db01974ffaa35997db4860 source_ref=d3041ed221ac8cc762a2087a6b59242c542b9989 role=test -->
Assert that every backend returned by `registry.all_backends()` is an instance of `LanguageBackend`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_registry:test_dispatch_extract_symbols_python fingerprint=cc4d99ddd425c0c654534dd25a0d7920f3dcdda2ec181e0b74af5726a039de06 body_fp=81b5eda257945b0635b713e445d3a2e0777535ac5b23cb4005cf8904418547f6 source_ref=d3041ed221ac8cc762a2087a6b59242c542b9989 role=test -->
Verify that `registry.extract_symbols` returns at least one function-kind symbol from the Python fixture file `calculator.py`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_registry:test_dispatch_extract_symbols_typescript fingerprint=21082cde6145e9bd8e92d44ebaa65b51397c5e6a7bf62df41852f2be0babf36a body_fp=9182cdd1d513e14c4faf0cc0a2119dce982c66024d72e11f14c7d85b82cb1490 source_ref=d3041ed221ac8cc762a2087a6b59242c542b9989 role=test -->
Verify that `registry.extract_symbols` parses a TypeScript fixture file and returns a symbol with qualified name `"src/util:double"`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_registry:test_dispatch_rejects_unknown_extension fingerprint=561e172da05906ec325b275a74f6620224fd5b2fff499790b2337a7aeb72d817 body_fp=e5738c30ba29949140510f0f6606a69b32fbe8017328c888e8db3fc21fc5fc7d source_ref=d3041ed221ac8cc762a2087a6b59242c542b9989 role=test -->
Assert that `registry.extract_symbols` raises `ValueError` when called with an unrecognised file extension.
<!-- trie:end -->