---
trie_version: 0.3.0
source: tests/test_backends_multilang.py
file_fingerprint: 2aee397fb038c527ff9493627123ea5d0acd63c6f666649327f5f43c629b7443
last_synced_at: '2026-07-29T01:48:58Z'
description: Symbol + tree-sitter reference extraction for the Go/Rust/C/Lua backends.
defines:
- kind: module
  qualified_name: tests/test_backends_multilang:__module__
  lines: 1-156
- kind: function
  qualified_name: tests/test_backends_multilang:_kinds
  lines: 18-19
  signature: def _kinds(symbols) -> dict[str, str]
- kind: function
  qualified_name: tests/test_backends_multilang:_edges
  lines: 22-23
  signature: def _edges(fd) -> set[tuple[str, str, str]]
- kind: function
  qualified_name: tests/test_backends_multilang:test_extension_is_indexable
  lines: 33-34
  signature: def test_extension_is_indexable(ext)
- kind: function
  qualified_name: tests/test_backends_multilang:test_all_backends_satisfy_protocol
  lines: 37-39
  signature: def test_all_backends_satisfy_protocol()
- kind: function
  qualified_name: tests/test_backends_multilang:test_go_symbols_and_calls
  lines: 45-62
  signature: 'def test_go_symbols_and_calls(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_backends_multilang:test_rust_symbols_and_calls
  lines: 68-86
  signature: 'def test_rust_symbols_and_calls(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_backends_multilang:test_c_symbols_and_calls
  lines: 92-113
  signature: 'def test_c_symbols_and_calls(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_backends_multilang:test_lua_symbols_and_calls
  lines: 119-140
  signature: 'def test_lua_symbols_and_calls(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_backends_multilang:test_javascript_uses_typescript_backend
  lines: 146-155
  signature: 'def test_javascript_uses_typescript_backend(tmp_path: Path)'
incoming_refs: 0
outgoing_refs: 15
---
<!-- trie:section symbol=tests/test_backends_multilang:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=a8f5024f83e851e708fbd18bfdf29acca1795bbc438605f63546d66972c212c0 source_ref=642fc0c9528c16e14cf88c3abba1353fafdb2b6f role=test -->
Test module for structural symbol and reference extraction across Go, Rust, C, Lua, and JavaScript/TypeScript backends, plus registry wiring checks.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_backends_multilang:_kinds fingerprint=8edd67abc4742bb96a3cf383d3a729783b0022d149a8bd6b29f72e94f69dfd60 body_fp=65ee0ab76dd5257a0ee09bf9f3b215a45f0b207a4823044e90a701a8a4244306 source_ref=642fc0c9528c16e14cf88c3abba1353fafdb2b6f role=util -->
## `def _kinds(symbols) -> dict[str, str]`

Build a `{name: kind}` mapping from an iterable of symbol objects.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_backends_multilang:_edges fingerprint=45aff61d148ee09bca6c50df860c55afb84703f94859b8ad4429bb9bccd3f84b body_fp=6f5b2cc7c26d3db3e5d0b6187ef5530d8e1c2124948097e95f3f0d5894de7d82 source_ref=642fc0c9528c16e14cf88c3abba1353fafdb2b6f role=test -->
## `def _edges(fd) -> set[tuple[str, str, str]]`

Extract a set of `(src_qname, target_qname, kind)` tuples from `fd.references` for edge-membership assertions in tests.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_backends_multilang:test_extension_is_indexable fingerprint=e63356c1eaa23624fdbf5d0a3a3e5d4ae8c3b25047d60de6e1b08d2cc6f67d87 body_fp=24e372b2d44e11a851f94aded2be5b778b84db26d1bb299a99d255560806cd9d source_ref=642fc0c9528c16e14cf88c3abba1353fafdb2b6f role=test -->
## `def test_extension_is_indexable(ext)`

Assert that `registry.is_indexable` returns truthy for each supported file extension.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_backends_multilang:test_all_backends_satisfy_protocol fingerprint=0b7723ec40dbc748ca4df11d22ecbbf3a5b904b4e61a1439fc634108d86c86f3 body_fp=e0b28d171bcb18a6513d8b2d7c7cf33d02a7e2b9cd3ea16dae74787c1ab6249d source_ref=642fc0c9528c16e14cf88c3abba1353fafdb2b6f role=test -->
## `def test_all_backends_satisfy_protocol()`

Assert that every backend returned by `registry.all_backends()` is an instance of `LanguageBackend`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_backends_multilang:test_go_symbols_and_calls fingerprint=d813499c851f4e162317137b5e3abb44108d8df2ab41260e6157afa9d84b3c5b body_fp=27d2bed25969bd08ac9af7894b446b6d847aecb594cad7043ad1dfad0ed9b2f7 source_ref=642fc0c9528c16e14cf88c3abba1353fafdb2b6f role=test -->
## `def test_go_symbols_and_calls(tmp_path: Path)`

Verify the Go backend correctly extracts symbol kinds (`function`, `class`, `method`, `constant`) and emits a `calls` edge from `Counter.Inc` to `Add`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_backends_multilang:test_rust_symbols_and_calls fingerprint=d92377ab00eedda80d85223948e33af47502ed374f61833e5ffae22987438940 body_fp=1aad909b60e62a8fc7f25d376e74d2d3291d5834279036843046ccf47dabe795 source_ref=642fc0c9528c16e14cf88c3abba1353fafdb2b6f role=test -->
## `def test_rust_symbols_and_calls(tmp_path: Path)`

Verify the Rust backend correctly extracts symbol kinds (`function`, `class`, `method`, `interface`, `enum`) and emits a `calls` edge from `Counter.inc` to `add`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_backends_multilang:test_c_symbols_and_calls fingerprint=48d046de90e6e2b898de89355576eb5af7af1738027b1cd4c8cbd9d5fa93d455 body_fp=edbda1c2a22272694e4aece36a92c9fbdf8ab7d67b1c53ffd743ef802f9630f9 source_ref=642fc0c9528c16e14cf88c3abba1353fafdb2b6f role=test -->
## `def test_c_symbols_and_calls(tmp_path: Path)`

Verify the C backend extracts correct symbol kinds, static-linkage visibility, and call edges from a synthetic `.c` file.

- `helper`: asserts `is_public` is `False` due to `static` linkage.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_backends_multilang:test_lua_symbols_and_calls fingerprint=e96f2dfdf0050b57b5be53171826eaa389886b2ad772b8419cc26cb0cf2cd333 body_fp=30302cf153bda3188481fd5a22e67e55a90177cb13a40558fe67d60ae9260570 source_ref=642fc0c9528c16e14cf88c3abba1353fafdb2b6f role=test -->
## `def test_lua_symbols_and_calls(tmp_path: Path)`

Verify the Lua backend correctly classifies symbols and extracts call edges from a synthetic `.lua` file.

- Asserts `local` functions are private and bare globals are public.
- Asserts module-table methods (`M.helper`) emit qualified `calls` edges.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_backends_multilang:test_javascript_uses_typescript_backend fingerprint=d4bffbc15f4e2773524a2a33ab1af421d087096032a496b4ca470b8c802de2c9 body_fp=9877b8e17a1e0f00ea7e77f19f00f3e12e096a1b39997dad41b492741c3431b8 source_ref=642fc0c9528c16e14cf88c3abba1353fafdb2b6f role=test -->
## `def test_javascript_uses_typescript_backend(tmp_path: Path)`

Assert that `.js` files are routed to `TypeScriptBackend` and that it correctly extracts symbols with stripped-suffix qualified names.
<!-- trie:end -->