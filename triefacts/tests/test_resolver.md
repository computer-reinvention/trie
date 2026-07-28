---
trie_version: 0.1.9
source: tests/test_resolver.py
file_fingerprint: dd824eef0142ac9a57ddfc991ff9e242afdbd3ea7ecbd155023d51f8137f4747
last_synced_at: '2026-07-28T23:14:47Z'
description: Tests for the tree-sitter + resolver seam.
defines:
- kind: module
  qualified_name: tests/test_resolver:__module__
  lines: 1-152
- kind: function
  qualified_name: tests/test_resolver:_pairs
  lines: 20-21
- kind: function
  qualified_name: tests/test_resolver:test_merge_appends_new_pairs
  lines: 27-31
- kind: function
  qualified_name: tests/test_resolver:test_merge_dedupes_identical_pairs
  lines: 34-38
- kind: function
  qualified_name: tests/test_resolver:test_merge_upgrades_to_stronger_kind
  lines: 41-47
- kind: function
  qualified_name: tests/test_resolver:test_merge_does_not_downgrade_kind
  lines: 50-54
- kind: function
  qualified_name: tests/test_resolver:test_merge_drops_self_edges
  lines: 57-59
- kind: function
  qualified_name: tests/test_resolver:test_jedi_resolver_satisfies_protocol
  lines: 65-66
- kind: function
  qualified_name: tests/test_resolver:test_python_backend_satisfies_language_backend
  lines: 69-70
- kind: function
  qualified_name: tests/test_resolver:test_python_backend_exposes_resolver
  lines: 73-74
- kind: function
  qualified_name: tests/test_resolver:test_resolver_recovers_self_method_call
  lines: 80-94
- kind: function
  qualified_name: tests/test_resolver:test_backend_merges_resolver_edges
  lines: 97-112
- kind: function
  qualified_name: tests/test_resolver:test_resolver_ignores_stdlib_targets
  lines: 115-124
- kind: function
  qualified_name: tests/test_resolver:test_resolver_disabled_env
  lines: 127-143
- kind: function
  qualified_name: tests/test_resolver:test_resolver_never_raises_on_bad_file
  lines: 146-151
incoming_refs: 0
outgoing_refs: 21
---
<!-- trie:section symbol=tests/test_resolver:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=c4a18531148b42152e7bf5900864056c106b3b54b367c8f8133f2ed0e1ad54bf source_ref=e9008fbda0e9c04a44188365f202740e10d057a7 role=test -->
Test module covering `merge_references`, `ReferenceResolver` protocol conformance, Jedi method-dispatch recovery, and two-pass extraction fallback behaviour.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_resolver:_pairs fingerprint=86a5bc0c5946185eab31b7bdc2b8eebeae7d169cfe3038715b9f3a2e94beecb5 body_fp=d529fc3cc02dec789f4be68e32a0ce511aad4ae5588c17ea4ca7c97d97922c52 source_ref=e9008fbda0e9c04a44188365f202740e10d057a7 role=util -->
Convert a list of `Reference` objects into a set of `(src_qname, target_qname, kind)` tuples for assertion comparisons.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_resolver:test_merge_appends_new_pairs fingerprint=111d6f4ce53be578747491fea9d9e4832394a11fa8b65e9bc91697c4a49bebae body_fp=627e799625ba0f3f6283d75e640707d2599b9f075d0901638a0970951a93e958 source_ref=e9008fbda0e9c04a44188365f202740e10d057a7 role=test -->
Assert that `merge_references` includes references from both base and extra lists when the target differs.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_resolver:test_merge_dedupes_identical_pairs fingerprint=7d44aeb29e98993cad0384e2b15e44a3b23a6d3f393968106131f06c5f39e894 body_fp=f2feb3bdb6b4d8741cb62a286da98bc273c8833ff0368930ba97622c0e1950eb source_ref=e9008fbda0e9c04a44188365f202740e10d057a7 role=test -->
Assert that `merge_references` returns exactly one entry when base and extra contain identical `Reference` pairs.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_resolver:test_merge_upgrades_to_stronger_kind fingerprint=512767f6c626231384476ebd4f738eaa8a2677746a40cdbaea1913467d6a5c9c body_fp=8c2a95a6687a7bd054f5d23e41d1a7c00ba3cd3e021f43c10d983fb98054357d source_ref=e9008fbda0e9c04a44188365f202740e10d057a7 role=test -->
Assert that `merge_references` replaces a weaker `"references"` kind with a stronger `"calls"` kind for the same src/target pair.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_resolver:test_merge_does_not_downgrade_kind fingerprint=44e7a40e747c87d2c5a4b058f44128223bcbba44864bd33664ff95f09785b80b body_fp=60530e35e7f9c4442815a93a6456c155d475b1a32b3f3f4710eff4e6a48624a6 source_ref=e9008fbda0e9c04a44188365f202740e10d057a7 role=test -->
Assert that `merge_references` preserves a stronger existing kind when the extra list supplies a weaker kind for the same pair.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_resolver:test_merge_drops_self_edges fingerprint=5072d01bacf7c9cc36126bfd955dbf953e966545f6fa619004cc7f9e54cadb18 body_fp=d1b11c2f6138fe5122b03f088c6d81447f2eaf22ca7ceb451de5444c3d4434de source_ref=e9008fbda0e9c04a44188365f202740e10d057a7 role=test -->
Assert that `merge_references` drops references where source and target qualified name are identical.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_resolver:test_jedi_resolver_satisfies_protocol fingerprint=fdd0111070e6ae16f3644fe217cf16a33211ee393179a14421749ac7cc7ffdcb body_fp=90b687ad160498cdcde98410a3cb1bb68350061f1d24b5925e5b5009802498ac source_ref=e9008fbda0e9c04a44188365f202740e10d057a7 role=test -->
Assert that `JediResolver` instances satisfy the `ReferenceResolver` protocol.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_resolver:test_python_backend_satisfies_language_backend fingerprint=860c1ab677e3467fdb5f5c204eb62ee38cd039b4164d363f2cb0b19b0efa1186 body_fp=fb52da4b83df65b884748154a24df2fce68a6f56dbd9255ffe46d8ff703c2005 source_ref=e9008fbda0e9c04a44188365f202740e10d057a7 role=test -->
Assert that `PythonBackend` is a valid implementation of the `LanguageBackend` protocol.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_resolver:test_python_backend_exposes_resolver fingerprint=4d5c254f905abde81b1696dbbdc1c058bd8ebb0cda17b89081ed9b3430cdecfb body_fp=fd5cdd2ba96dee0c39ee55077820104b3ef493b7d8179ff01b02a6601f37c69e source_ref=e9008fbda0e9c04a44188365f202740e10d057a7 role=test -->
Assert that `PythonBackend().resolver()` returns a non-`None` resolver instance by default.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_resolver:test_resolver_recovers_self_method_call fingerprint=b44b4b97b5cf5f0f5b1df699aeef3956b062b072626ea95714cf9046fdb4ff4e body_fp=b7e9576685dc44aa92414b038b38c721df794ca711e69629579647e428c70926 source_ref=e9008fbda0e9c04a44188365f202740e10d057a7 role=test -->
Assert that `JediResolver` resolves a `self.helper()` call inside `Service.run` to a `"calls"` edge targeting `svc:Service.helper`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_resolver:test_backend_merges_resolver_edges fingerprint=e4a6bf321a2c1bc4b99f5c8e5ff10ff7e205e4d053db14f7d31ec3aa1bb5d88b body_fp=760fc14497e88cfa7d9c8f5c11bc164fc04a2bcb5fc2cdef6c4c6639d2e00496 source_ref=e9008fbda0e9c04a44188365f202740e10d057a7 role=test -->
Assert that `PythonBackend.extract_file_data` includes a resolver-derived `calls` edge between two class methods in its returned references.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_resolver:test_resolver_ignores_stdlib_targets fingerprint=369617255aa3d429b6f86db04fb934145c763b4a49a883b40c264dcfc0d3a037 body_fp=51e00f4d2dada2eddefa0b61b0cad8507a04fa7cef47e84e548171b301195d71 source_ref=e9008fbda0e9c04a44188365f202740e10d057a7 role=test -->
Assert that `JediResolver.resolve_file` emits no edges targeting stdlib symbols that resolve outside the source root.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_resolver:test_resolver_disabled_env fingerprint=fe943f000cffa984fbe400e314dde0584cf96f02b3b8d80b1059e92b44f9247c body_fp=f2b9ac8f33f623db58bae4fcbf6c435b828267e59afe5b29612eff146e4c7ad7 source_ref=e9008fbda0e9c04a44188365f202740e10d057a7 role=test -->
Assert that setting `TRIE_DISABLE_RESOLVER=1` causes `PythonBackend.resolver()` to return `None` and suppresses method-call edges in extracted references.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_resolver:test_resolver_never_raises_on_bad_file fingerprint=53e93889d41eb6ffac639d739caca8535ff79a4a1ee87d8075fa957beca4ca93 body_fp=f8c23a8541edd606e616be535a984216b376d3736d7481b334b0e1e7ac59fc68 source_ref=e9008fbda0e9c04a44188365f202740e10d057a7 role=test -->
Assert that `JediResolver.resolve_file` returns an empty list instead of raising when given a syntactically invalid Python file.
<!-- trie:end -->