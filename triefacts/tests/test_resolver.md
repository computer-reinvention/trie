---
trie_version: 0.1.9
source: tests/test_resolver.py
file_fingerprint: 5982bff93126b20f7a2847c08996f0c84839222f8f8e48d8e9b3fd9dfd96acfb
last_synced_at: '2026-07-28T23:35:59Z'
description: Tests for the tree-sitter + LSP resolver seam.
defines:
- kind: module
  qualified_name: tests/test_resolver:__module__
  lines: 1-226
- kind: function
  qualified_name: tests/test_resolver:_pairs
  lines: 27-28
- kind: function
  qualified_name: tests/test_resolver:_method_edges
  lines: 31-36
- kind: constant
  qualified_name: tests/test_resolver:requires_python_lsp
  lines: 39-41
- kind: constant
  qualified_name: tests/test_resolver:requires_ts_lsp
  lines: 42-44
- kind: function
  qualified_name: tests/test_resolver:test_merge_appends_new_pairs
  lines: 50-54
- kind: function
  qualified_name: tests/test_resolver:test_merge_dedupes_identical_pairs
  lines: 57-61
- kind: function
  qualified_name: tests/test_resolver:test_merge_upgrades_to_stronger_kind
  lines: 64-69
- kind: function
  qualified_name: tests/test_resolver:test_merge_does_not_downgrade_kind
  lines: 72-76
- kind: function
  qualified_name: tests/test_resolver:test_merge_drops_self_edges
  lines: 79-80
- kind: function
  qualified_name: tests/test_resolver:test_lsp_resolver_satisfies_protocol
  lines: 86-90
- kind: function
  qualified_name: tests/test_resolver:test_python_backend_satisfies_language_backend
  lines: 93-94
- kind: function
  qualified_name: tests/test_resolver:test_spec_availability_is_path_based
  lines: 97-102
- kind: function
  qualified_name: tests/test_resolver:test_python_backend_exposes_resolver
  lines: 109-110
- kind: function
  qualified_name: tests/test_resolver:test_python_resolver_recovers_self_method_call
  lines: 114-130
- kind: function
  qualified_name: tests/test_resolver:test_python_resolver_ignores_stdlib_targets
  lines: 134-146
- kind: function
  qualified_name: tests/test_resolver:test_typescript_backend_exposes_resolver
  lines: 153-156
- kind: function
  qualified_name: tests/test_resolver:test_typescript_resolver_recovers_this_method_call
  lines: 160-184
- kind: function
  qualified_name: tests/test_resolver:test_resolver_disabled_env
  lines: 190-203
- kind: function
  qualified_name: tests/test_resolver:test_resolver_never_raises_on_missing_server
  lines: 206-225
incoming_refs: 0
outgoing_refs: 25
---
<!-- trie:section symbol=tests/test_resolver:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=c4a18531148b42152e7bf5900864056c106b3b54b367c8f8133f2ed0e1ad54bf source_ref=e9008fbda0e9c04a44188365f202740e10d057a7 role=test -->
Test module covering `merge_references`, `ReferenceResolver` protocol conformance, Jedi method-dispatch recovery, and two-pass extraction fallback behaviour.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_resolver:_pairs fingerprint=86a5bc0c5946185eab31b7bdc2b8eebeae7d169cfe3038715b9f3a2e94beecb5 body_fp=d529fc3cc02dec789f4be68e32a0ce511aad4ae5588c17ea4ca7c97d97922c52 source_ref=e9008fbda0e9c04a44188365f202740e10d057a7 role=util -->
Convert a list of `Reference` objects into a set of `(src_qname, target_qname, kind)` tuples for assertion comparisons.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_resolver:_method_edges fingerprint=6f175922e363b733f69f68699887a00661f2220abf6ab0bf9cdc79deeab83b0b body_fp=8d165d81456120ac049923cfca5d51450f6596aef210fff215a67bbb6f2c078f source_ref=55b57107ee9b0e3fcfa91fc19ac6bf927bac3e31 role=util -->
Extract `(src_qname, target_qname)` pairs from `fd.references` where the kind is `"calls"` and the target's local name contains a dot (i.e., a method call).
<!-- trie:end -->
<!-- trie:section symbol=tests/test_resolver:requires_python_lsp fingerprint=e3eebd72f1acc3fa5f7f7203af046389b8270351892e3dcd7e8d1e4bf447b686 body_fp=fa4a98d74d75964b0060d5a4f8cd427a45895b928e4632f4f244a0d91d015391 source_ref=55b57107ee9b0e3fcfa91fc19ac6bf927bac3e31 role=test -->
pytest mark that skips a test when no Python language server (pyright/basedpyright) is found on PATH.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_resolver:requires_ts_lsp fingerprint=6fb7e533680cb6477ae1ef2c8943a321ab672a55196665bb5466133ded485675 body_fp=8b48cc70d05a85ebda11faaa87fcb82d52aca588c0fd6c07aca95434f367be4c source_ref=55b57107ee9b0e3fcfa91fc19ac6bf927bac3e31 role=test -->
Pytest mark that skips a test when `typescript_spec()` returns `None`, indicating `typescript-language-server` is absent from PATH.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_resolver:test_merge_appends_new_pairs fingerprint=111d6f4ce53be578747491fea9d9e4832394a11fa8b65e9bc91697c4a49bebae body_fp=627e799625ba0f3f6283d75e640707d2599b9f075d0901638a0970951a93e958 source_ref=e9008fbda0e9c04a44188365f202740e10d057a7 role=test -->
Assert that `merge_references` includes references from both base and extra lists when the target differs.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_resolver:test_merge_dedupes_identical_pairs fingerprint=0b7ae3962be6a16eaa735ffb1601c135d7567a94feed1363100d02d1b8f018ea body_fp=f2feb3bdb6b4d8741cb62a286da98bc273c8833ff0368930ba97622c0e1950eb source_ref=55b57107ee9b0e3fcfa91fc19ac6bf927bac3e31 role=test -->
Assert that `merge_references` returns exactly one entry when base and extra contain identical `Reference` pairs.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_resolver:test_merge_upgrades_to_stronger_kind fingerprint=20c29e4fb04f78ea392bebd9c1167107f44589b409199ae303a2a17c3e9fd21a body_fp=8c2a95a6687a7bd054f5d23e41d1a7c00ba3cd3e021f43c10d983fb98054357d source_ref=55b57107ee9b0e3fcfa91fc19ac6bf927bac3e31 role=test -->
Assert that `merge_references` replaces a weaker `"references"` kind with a stronger `"calls"` kind for the same src/target pair.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_resolver:test_merge_does_not_downgrade_kind fingerprint=ad85d2078f4e013a516413fe0d582753cdd112c564616c5f24152cb884988dc4 body_fp=60530e35e7f9c4442815a93a6456c155d475b1a32b3f3f4710eff4e6a48624a6 source_ref=55b57107ee9b0e3fcfa91fc19ac6bf927bac3e31 role=test -->
Assert that `merge_references` preserves a stronger existing kind when the extra list supplies a weaker kind for the same pair.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_resolver:test_merge_drops_self_edges fingerprint=f0d09048359d8d42edad25161670b197a2872d3f9598b0bb54cd72f8cf0b671f body_fp=d1b11c2f6138fe5122b03f088c6d81447f2eaf22ca7ceb451de5444c3d4434de source_ref=55b57107ee9b0e3fcfa91fc19ac6bf927bac3e31 role=test -->
Assert that `merge_references` drops references where source and target qualified name are identical.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_resolver:test_lsp_resolver_satisfies_protocol fingerprint=c4eaab111945745c706a37a952ddb1d3e01679633d50b643aad6bc9001ffe7d3 body_fp=9a575b88256115fe72f5bc596e5c5841c00e7719011d2bc36eee2c30a6b304fb source_ref=55b57107ee9b0e3fcfa91fc19ac6bf927bac3e31 role=test -->
Assert that `LspResolver` instantiated with an available spec satisfies the `ReferenceResolver` protocol; skips if no language server is on PATH.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_resolver:test_python_backend_satisfies_language_backend fingerprint=860c1ab677e3467fdb5f5c204eb62ee38cd039b4164d363f2cb0b19b0efa1186 body_fp=fb52da4b83df65b884748154a24df2fce68a6f56dbd9255ffe46d8ff703c2005 source_ref=e9008fbda0e9c04a44188365f202740e10d057a7 role=test -->
Assert that `PythonBackend` is a valid implementation of the `LanguageBackend` protocol.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_resolver:test_spec_availability_is_path_based fingerprint=55e9aabfb5c667f64e0ae24e309368992b9f667501f1fb32c15ba1e0316fdd61 body_fp=56a3ca49e57ba5165549007740f63be1f1d4c2405ddf600896057c078cf34c69 source_ref=55b57107ee9b0e3fcfa91fc19ac6bf927bac3e31 role=test -->
Assert that `python_spec()` returns a spec whose `is_available()` returns `True` and whose `command` and `language_id` fields are correctly populated; skips if no Python server is on PATH.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_resolver:test_python_backend_exposes_resolver fingerprint=4d5c254f905abde81b1696dbbdc1c058bd8ebb0cda17b89081ed9b3430cdecfb body_fp=fd5cdd2ba96dee0c39ee55077820104b3ef493b7d8179ff01b02a6601f37c69e source_ref=e9008fbda0e9c04a44188365f202740e10d057a7 role=test -->
Assert that `PythonBackend().resolver()` returns a non-`None` resolver instance by default.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_resolver:test_python_resolver_recovers_self_method_call fingerprint=d0df6974c23d17ec73f3a3c3feddcc335e64c1fd97e9d2fcdfe1328c3ecbaee8 body_fp=701ec002e067f7f500b02298071895f903ccead94c2cc0b1df1731cfe5a7aa26 source_ref=55b57107ee9b0e3fcfa91fc19ac6bf927bac3e31 role=test -->
Assert that `PythonBackend` recovers a `self.helper()` call edge (`Service.run` → `Service.helper`) via the LSP resolver.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_resolver:test_python_resolver_ignores_stdlib_targets fingerprint=c2fa0748225a612cb6d14ec2d9bab0defa53f75fe5645109e73ed99cc3e4e09b body_fp=98c078b07a0d6c4ed503c688ac1cd43f724b8737e71deba204b4d2015d5b5895 source_ref=55b57107ee9b0e3fcfa91fc19ac6bf927bac3e31 role=test -->
Assert that `LspResolver.resolve_file` returns no references whose target module is the stdlib `os` module.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_resolver:test_typescript_backend_exposes_resolver fingerprint=0de1e1c957c317a50b443d410fb8549a19927c69e344e78a62863cf59e70869c body_fp=105751e8bab7a75c20a875f61769a4f5119a725f1ff0f50aca185c83b46289a0 source_ref=55b57107ee9b0e3fcfa91fc19ac6bf927bac3e31 role=test -->
Assert that `TypeScriptBackend().resolver()` returns a non-`None` resolver when a TypeScript language server is available.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_resolver:test_typescript_resolver_recovers_this_method_call fingerprint=fde87af88ab3f188e6003ce9aba7e059b505866a0b33446e8216a70415acb9d1 body_fp=161b05c62acf55f15b70319d85ddb4f06ffda8e6a3af7070fd9140d351211a0a source_ref=55b57107ee9b0e3fcfa91fc19ac6bf927bac3e31 role=test -->
Assert that `TypeScriptBackend` resolves a `this.helper()` call inside `Service.run` to a typed `calls` edge via the LSP resolver.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_resolver:test_resolver_disabled_env fingerprint=1d457be2d771a8f522d09332a3397294e110a616550d200814383f03efe799f1 body_fp=f2b9ac8f33f623db58bae4fcbf6c435b828267e59afe5b29612eff146e4c7ad7 source_ref=55b57107ee9b0e3fcfa91fc19ac6bf927bac3e31 role=test -->
Assert that setting `TRIE_DISABLE_RESOLVER=1` causes `PythonBackend.resolver()` to return `None` and suppresses method-call edges in extracted references.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_resolver:test_resolver_never_raises_on_missing_server fingerprint=50404e63c372bc8eef081fdef7fbaff598901afa18df216c9a4d7561f7d75c66 body_fp=ee2edbcc78d57f1f9d977307e561e05014216b99549dfe432851624d2e7ce19e source_ref=55b57107ee9b0e3fcfa91fc19ac6bf927bac3e31 role=test -->
Assert that `LspResolver.resolve_file` returns an empty list without raising when the configured server binary does not exist.
<!-- trie:end -->