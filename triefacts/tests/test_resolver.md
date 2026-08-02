---
trie_version: 0.3.0
source: tests/test_resolver.py
file_fingerprint: 5982bff93126b20f7a2847c08996f0c84839222f8f8e48d8e9b3fd9dfd96acfb
last_synced_at: '2026-08-02T21:19:22Z'
description: Tests for the tree-sitter + LSP resolver seam.
defines:
- kind: module
  qualified_name: tests/test_resolver:__module__
  lines: 1-226
- kind: function
  qualified_name: tests/test_resolver:_pairs
  lines: 27-28
  signature: def _pairs(refs) -> set[tuple[str, str, str]]
- kind: function
  qualified_name: tests/test_resolver:_method_edges
  lines: 31-36
  signature: def _method_edges(fd) -> set[tuple[str, str]]
- kind: constant
  qualified_name: tests/test_resolver:requires_python_lsp
  lines: 39-41
- kind: constant
  qualified_name: tests/test_resolver:requires_ts_lsp
  lines: 42-44
- kind: function
  qualified_name: tests/test_resolver:test_merge_appends_new_pairs
  lines: 50-54
  signature: def test_merge_appends_new_pairs()
- kind: function
  qualified_name: tests/test_resolver:test_merge_dedupes_identical_pairs
  lines: 57-61
  signature: def test_merge_dedupes_identical_pairs()
- kind: function
  qualified_name: tests/test_resolver:test_merge_upgrades_to_stronger_kind
  lines: 64-69
  signature: def test_merge_upgrades_to_stronger_kind()
- kind: function
  qualified_name: tests/test_resolver:test_merge_does_not_downgrade_kind
  lines: 72-76
  signature: def test_merge_does_not_downgrade_kind()
- kind: function
  qualified_name: tests/test_resolver:test_merge_drops_self_edges
  lines: 79-80
  signature: def test_merge_drops_self_edges()
- kind: function
  qualified_name: tests/test_resolver:test_lsp_resolver_satisfies_protocol
  lines: 86-90
  signature: def test_lsp_resolver_satisfies_protocol()
- kind: function
  qualified_name: tests/test_resolver:test_python_backend_satisfies_language_backend
  lines: 93-94
  signature: def test_python_backend_satisfies_language_backend()
- kind: function
  qualified_name: tests/test_resolver:test_spec_availability_is_path_based
  lines: 97-102
  signature: def test_spec_availability_is_path_based()
- kind: function
  qualified_name: tests/test_resolver:test_python_backend_exposes_resolver
  lines: 109-110
  signature: def test_python_backend_exposes_resolver(enable_resolver)
- kind: function
  qualified_name: tests/test_resolver:test_python_resolver_recovers_self_method_call
  lines: 114-130
  signature: 'def test_python_resolver_recovers_self_method_call(tmp_path: Path, enable_resolver)'
- kind: function
  qualified_name: tests/test_resolver:test_python_resolver_ignores_stdlib_targets
  lines: 134-146
  signature: 'def test_python_resolver_ignores_stdlib_targets(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_resolver:test_typescript_backend_exposes_resolver
  lines: 153-156
  signature: def test_typescript_backend_exposes_resolver(enable_resolver)
- kind: function
  qualified_name: tests/test_resolver:test_typescript_resolver_recovers_this_method_call
  lines: 160-184
  signature: 'def test_typescript_resolver_recovers_this_method_call(tmp_path: Path, enable_resolver)'
- kind: function
  qualified_name: tests/test_resolver:test_resolver_disabled_env
  lines: 190-203
  signature: 'def test_resolver_disabled_env(tmp_path: Path, monkeypatch)'
- kind: function
  qualified_name: tests/test_resolver:test_resolver_never_raises_on_missing_server
  lines: 206-225
  signature: 'def test_resolver_never_raises_on_missing_server(tmp_path: Path, monkeypatch): # Point the spec at a non-existent binary; resolve_file must return [] and # the backend must fall back to tree-sitter-only extraction.'
incoming_refs: 0
outgoing_refs: 44
---
<!-- trie:section symbol=tests/test_resolver:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=c4a18531148b42152e7bf5900864056c106b3b54b367c8f8133f2ed0e1ad54bf source_ref=e9008fbda0e9c04a44188365f202740e10d057a7 role=test -->
Test module covering `merge_references`, `ReferenceResolver` protocol conformance, Jedi method-dispatch recovery, and two-pass extraction fallback behaviour.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_resolver:_pairs fingerprint=86a5bc0c5946185eab31b7bdc2b8eebeae7d169cfe3038715b9f3a2e94beecb5 body_fp=3cbde36f63cd268df4f5eba371dbc6262ab349aac2ae896b99bd355947555ce2 source_ref=e9008fbda0e9c04a44188365f202740e10d057a7 role=util -->
## `def _pairs(refs) -> set[tuple[str, str, str]]`

Convert a list of `Reference` objects into a set of `(src_qname, target_qname, kind)` tuples for assertion comparisons.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_resolver:_method_edges fingerprint=6f175922e363b733f69f68699887a00661f2220abf6ab0bf9cdc79deeab83b0b body_fp=7d0b88d3a5147edab9341c058da9f94956e5ca9469c51cf04f24296f7140be73 source_ref=55b57107ee9b0e3fcfa91fc19ac6bf927bac3e31 role=util -->
## `def _method_edges(fd) -> set[tuple[str, str]]`

Extract `(src_qname, target_qname)` pairs from `fd.references` where the kind is `"calls"` and the target's local name contains a dot (i.e., a method call).
<!-- trie:end -->
<!-- trie:section symbol=tests/test_resolver:requires_python_lsp fingerprint=e3eebd72f1acc3fa5f7f7203af046389b8270351892e3dcd7e8d1e4bf447b686 body_fp=fa4a98d74d75964b0060d5a4f8cd427a45895b928e4632f4f244a0d91d015391 source_ref=55b57107ee9b0e3fcfa91fc19ac6bf927bac3e31 role=test -->
pytest mark that skips a test when no Python language server (pyright/basedpyright) is found on PATH.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_resolver:requires_ts_lsp fingerprint=6fb7e533680cb6477ae1ef2c8943a321ab672a55196665bb5466133ded485675 body_fp=8b48cc70d05a85ebda11faaa87fcb82d52aca588c0fd6c07aca95434f367be4c source_ref=55b57107ee9b0e3fcfa91fc19ac6bf927bac3e31 role=test -->
Pytest mark that skips a test when `typescript_spec()` returns `None`, indicating `typescript-language-server` is absent from PATH.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_resolver:test_merge_appends_new_pairs fingerprint=111d6f4ce53be578747491fea9d9e4832394a11fa8b65e9bc91697c4a49bebae body_fp=e5916cbd8ae4f948a1133b04f6740c500368be9fcb805a5a57c5dbe506d156fd source_ref=55b57107ee9b0e3fcfa91fc19ac6bf927bac3e31 role=test -->
## `def test_merge_appends_new_pairs()`

Assert that `merge_references` includes references from both base and extra lists when the target differs.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_resolver:test_merge_dedupes_identical_pairs fingerprint=0b7ae3962be6a16eaa735ffb1601c135d7567a94feed1363100d02d1b8f018ea body_fp=1e1e4296253bc59e15b6940d80ec716e90a02f3e853b521008f6e39600994847 source_ref=55b57107ee9b0e3fcfa91fc19ac6bf927bac3e31 role=test -->
## `def test_merge_dedupes_identical_pairs()`

Assert that `merge_references` returns exactly one entry when base and extra contain identical `Reference` pairs.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_resolver:test_merge_upgrades_to_stronger_kind fingerprint=20c29e4fb04f78ea392bebd9c1167107f44589b409199ae303a2a17c3e9fd21a body_fp=7b3516343072d3f942b6284c140fd7b35b53efaf7d935f88a8d140147d4989ee source_ref=55b57107ee9b0e3fcfa91fc19ac6bf927bac3e31 role=test -->
## `def test_merge_upgrades_to_stronger_kind()`

Assert that `merge_references` replaces a weaker `"references"` kind with a stronger `"calls"` kind for the same src/target pair.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_resolver:test_merge_does_not_downgrade_kind fingerprint=ad85d2078f4e013a516413fe0d582753cdd112c564616c5f24152cb884988dc4 body_fp=994482338de12e20ec316fd97bf08e3d22a9d5509420ed9fde1782f695c5fbb0 source_ref=55b57107ee9b0e3fcfa91fc19ac6bf927bac3e31 role=test -->
## `def test_merge_does_not_downgrade_kind()`

Assert that `merge_references` preserves a stronger existing kind when the extra list supplies a weaker kind for the same pair.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_resolver:test_merge_drops_self_edges fingerprint=f0d09048359d8d42edad25161670b197a2872d3f9598b0bb54cd72f8cf0b671f body_fp=31a0e6790736b8d86de0e5e4f91318df7399745b008ba19eb989b2ea28f20cf7 source_ref=55b57107ee9b0e3fcfa91fc19ac6bf927bac3e31 role=test -->
## `def test_merge_drops_self_edges()`

Assert that `merge_references` drops references where source and target qualified name are identical.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_resolver:test_lsp_resolver_satisfies_protocol fingerprint=c4eaab111945745c706a37a952ddb1d3e01679633d50b643aad6bc9001ffe7d3 body_fp=df3013619a7387928c63c51367ee2401f7446a98ec27206cb643f3ca72fd5b45 source_ref=55b57107ee9b0e3fcfa91fc19ac6bf927bac3e31 role=test -->
## `def test_lsp_resolver_satisfies_protocol()`

Assert that `LspResolver` instantiated with an available spec satisfies the `ReferenceResolver` protocol; skips if no language server is on PATH.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_resolver:test_python_backend_satisfies_language_backend fingerprint=860c1ab677e3467fdb5f5c204eb62ee38cd039b4164d363f2cb0b19b0efa1186 body_fp=59af8dfffa3d60899473f023a844b979ea7cd7c523277ffff0bc276ab585235c source_ref=e9008fbda0e9c04a44188365f202740e10d057a7 role=test -->
## `def test_python_backend_satisfies_language_backend()`

Assert that `PythonBackend` is a valid implementation of the `LanguageBackend` protocol.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_resolver:test_spec_availability_is_path_based fingerprint=55e9aabfb5c667f64e0ae24e309368992b9f667501f1fb32c15ba1e0316fdd61 body_fp=1171c54976d67844b3e7508b98663f4287a87b54f27e0a186305689bb57699c3 source_ref=55b57107ee9b0e3fcfa91fc19ac6bf927bac3e31 role=test -->
## `def test_spec_availability_is_path_based()`

Assert that `python_spec()` returns a spec whose `is_available()` returns `True` and whose `command` and `language_id` fields are correctly populated; skips if no Python server is on PATH.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_resolver:test_python_backend_exposes_resolver fingerprint=4d5c254f905abde81b1696dbbdc1c058bd8ebb0cda17b89081ed9b3430cdecfb body_fp=4fdf6b033aac5d1e98a8de3197970952c84e39e16c187267bccfe6ec8d462582 source_ref=e9008fbda0e9c04a44188365f202740e10d057a7 role=test -->
## `def test_python_backend_exposes_resolver(enable_resolver)`

Assert that `PythonBackend().resolver()` returns a non-`None` resolver instance by default.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_resolver:test_python_resolver_recovers_self_method_call fingerprint=d0df6974c23d17ec73f3a3c3feddcc335e64c1fd97e9d2fcdfe1328c3ecbaee8 body_fp=d60c617226efa4c93819657f5ad6713329d9f39ad828fd8d7aa0d997d165acb0 source_ref=55b57107ee9b0e3fcfa91fc19ac6bf927bac3e31 role=test -->
## `def test_python_resolver_recovers_self_method_call(tmp_path: Path, enable_resolver)`

Assert that `PythonBackend` recovers a `self.helper()` call edge (`Service.run` → `Service.helper`) via the LSP resolver.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_resolver:test_python_resolver_ignores_stdlib_targets fingerprint=c2fa0748225a612cb6d14ec2d9bab0defa53f75fe5645109e73ed99cc3e4e09b body_fp=8c865f4d10afb35c051a1136e3e4a37d375e3d88edb8578d0bde78ad982f8ac1 source_ref=55b57107ee9b0e3fcfa91fc19ac6bf927bac3e31 role=test -->
## `def test_python_resolver_ignores_stdlib_targets(tmp_path: Path)`

Assert that `LspResolver.resolve_file` returns no references whose target module is the stdlib `os` module.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_resolver:test_typescript_backend_exposes_resolver fingerprint=0de1e1c957c317a50b443d410fb8549a19927c69e344e78a62863cf59e70869c body_fp=60264c0b8a3a19aebf14b5fe6b78a59460735f89888711d6b0b93f7aa806f3f3 source_ref=55b57107ee9b0e3fcfa91fc19ac6bf927bac3e31 role=test -->
## `def test_typescript_backend_exposes_resolver(enable_resolver)`

Assert that `TypeScriptBackend().resolver()` returns a non-`None` resolver when a TypeScript language server is available.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_resolver:test_typescript_resolver_recovers_this_method_call fingerprint=fde87af88ab3f188e6003ce9aba7e059b505866a0b33446e8216a70415acb9d1 body_fp=7b453f937629971d3dbe0f267a0b4f51b4228500935a647db123d8c8c09a772d source_ref=55b57107ee9b0e3fcfa91fc19ac6bf927bac3e31 role=test -->
## `def test_typescript_resolver_recovers_this_method_call(tmp_path: Path, enable_resolver)`

Assert that `TypeScriptBackend` resolves a `this.helper()` call inside `Service.run` to a typed `calls` edge via the LSP resolver.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_resolver:test_resolver_disabled_env fingerprint=1d457be2d771a8f522d09332a3397294e110a616550d200814383f03efe799f1 body_fp=36fbdb2acc8df5dfdca31c68174b602fef8dc615d91d20b2affe03efdd07b9eb source_ref=55b57107ee9b0e3fcfa91fc19ac6bf927bac3e31 role=test -->
## `def test_resolver_disabled_env(tmp_path: Path, monkeypatch)`

Assert that setting `TRIE_DISABLE_RESOLVER=1` causes `PythonBackend.resolver()` to return `None` and suppresses method-call edges in extracted references.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_resolver:test_resolver_never_raises_on_missing_server fingerprint=50404e63c372bc8eef081fdef7fbaff598901afa18df216c9a4d7561f7d75c66 body_fp=bb80eecda8d5b6ea631ea18e8259861184ab10adf742f2d3c0dfbef2d7b70d45 source_ref=55b57107ee9b0e3fcfa91fc19ac6bf927bac3e31 role=test -->
## `def test_resolver_never_raises_on_missing_server(tmp_path: Path, monkeypatch): # Point the spec at a non-existent binary; resolve_file must return [] and # the backend must fall back to tree-sitter-only extraction.`

Assert that `LspResolver.resolve_file` returns an empty list without raising when the configured server binary does not exist.
<!-- trie:end -->