---
trie_version: 0.1.9
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
- kind: function
  qualified_name: tests/test_backends_multilang:_edges
  lines: 22-23
- kind: function
  qualified_name: tests/test_backends_multilang:test_extension_is_indexable
  lines: 33-34
- kind: function
  qualified_name: tests/test_backends_multilang:test_all_backends_satisfy_protocol
  lines: 37-39
- kind: function
  qualified_name: tests/test_backends_multilang:test_go_symbols_and_calls
  lines: 45-62
- kind: function
  qualified_name: tests/test_backends_multilang:test_rust_symbols_and_calls
  lines: 68-86
- kind: function
  qualified_name: tests/test_backends_multilang:test_c_symbols_and_calls
  lines: 92-113
- kind: function
  qualified_name: tests/test_backends_multilang:test_lua_symbols_and_calls
  lines: 119-140
- kind: function
  qualified_name: tests/test_backends_multilang:test_javascript_uses_typescript_backend
  lines: 146-155
incoming_refs: 0
outgoing_refs: 4
---
<!-- trie:section symbol=tests/test_backends_multilang:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=a8f5024f83e851e708fbd18bfdf29acca1795bbc438605f63546d66972c212c0 source_ref=642fc0c9528c16e14cf88c3abba1353fafdb2b6f role=test -->
Test module for structural symbol and reference extraction across Go, Rust, C, Lua, and JavaScript/TypeScript backends, plus registry wiring checks.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_backends_multilang:_kinds fingerprint=8edd67abc4742bb96a3cf383d3a729783b0022d149a8bd6b29f72e94f69dfd60 body_fp=dbc00a13c68e73408826ddcb9a2db0c9bc7b6b76a94b1ccc190b2a31396bdf2f source_ref=642fc0c9528c16e14cf88c3abba1353fafdb2b6f role=util -->
Build a `{name: kind}` mapping from an iterable of symbol objects.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_backends_multilang:_edges fingerprint=45aff61d148ee09bca6c50df860c55afb84703f94859b8ad4429bb9bccd3f84b body_fp=50ba22a44ce634838057ba97bf5d4813ddcacca5ea582f2e86fd5897ead97519 source_ref=642fc0c9528c16e14cf88c3abba1353fafdb2b6f role=test -->
Extract a set of `(src_qname, target_qname, kind)` tuples from `fd.references` for edge-membership assertions in tests.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_backends_multilang:test_extension_is_indexable fingerprint=e63356c1eaa23624fdbf5d0a3a3e5d4ae8c3b25047d60de6e1b08d2cc6f67d87 body_fp=14b070ce87fa2dca76a2ce7254bf387e74f5588f881eab2a129b069d9db03108 source_ref=642fc0c9528c16e14cf88c3abba1353fafdb2b6f role=test -->
Assert that `registry.is_indexable` returns truthy for each supported file extension.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_backends_multilang:test_all_backends_satisfy_protocol fingerprint=0b7723ec40dbc748ca4df11d22ecbbf3a5b904b4e61a1439fc634108d86c86f3 body_fp=0d93919cd625c5b26c41c3957edd4c13e714ddf3c6db01974ffaa35997db4860 source_ref=642fc0c9528c16e14cf88c3abba1353fafdb2b6f role=test -->
Assert that every backend returned by `registry.all_backends()` is an instance of `LanguageBackend`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_backends_multilang:test_go_symbols_and_calls fingerprint=d813499c851f4e162317137b5e3abb44108d8df2ab41260e6157afa9d84b3c5b body_fp=b24dd8a5b059aa3f136529087aea1abd457290aa74bc9a3701b3052f7c50dae5 source_ref=642fc0c9528c16e14cf88c3abba1353fafdb2b6f role=test -->
Verify the Go backend correctly extracts symbol kinds (`function`, `class`, `method`, `constant`) and emits a `calls` edge from `Counter.Inc` to `Add`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_backends_multilang:test_rust_symbols_and_calls fingerprint=d92377ab00eedda80d85223948e33af47502ed374f61833e5ffae22987438940 body_fp=42a7faf770cb7a013bb77513c41f04ef7ca0501b6490f16b4891d788f3f0b28e source_ref=642fc0c9528c16e14cf88c3abba1353fafdb2b6f role=test -->
Verify the Rust backend correctly extracts symbol kinds (`function`, `class`, `method`, `interface`, `enum`) and emits a `calls` edge from `Counter.inc` to `add`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_backends_multilang:test_c_symbols_and_calls fingerprint=48d046de90e6e2b898de89355576eb5af7af1738027b1cd4c8cbd9d5fa93d455 body_fp=6ec43d9a368cb7e5a3a5440b0edecc2519eda75797505d2678a8ac20d2c3d59d source_ref=642fc0c9528c16e14cf88c3abba1353fafdb2b6f role=test -->
Verify the C backend extracts correct symbol kinds, static-linkage visibility, and call edges from a synthetic `.c` file.

- `helper`: asserts `is_public` is `False` due to `static` linkage.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_backends_multilang:test_lua_symbols_and_calls fingerprint=e96f2dfdf0050b57b5be53171826eaa389886b2ad772b8419cc26cb0cf2cd333 body_fp=b235d0bbfaf20cbe151a5cfe92f9bb4884a833b4f248b54aafbcab715083c361 source_ref=642fc0c9528c16e14cf88c3abba1353fafdb2b6f role=test -->
Verify the Lua backend correctly classifies symbols and extracts call edges from a synthetic `.lua` file.

- Asserts `local` functions are private and bare globals are public.
- Asserts module-table methods (`M.helper`) emit qualified `calls` edges.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_backends_multilang:test_javascript_uses_typescript_backend fingerprint=d4bffbc15f4e2773524a2a33ab1af421d087096032a496b4ca470b8c802de2c9 body_fp=6d81b434596f56af847c8a011ba37d297300d5d2c3030f8372eeecd81debc6d4 source_ref=642fc0c9528c16e14cf88c3abba1353fafdb2b6f role=test -->
Assert that `.js` files are routed to `TypeScriptBackend` and that it correctly extracts symbols with stripped-suffix qualified names.
<!-- trie:end -->