---
trie_version: 0.3.0
source: tests/test_references_typescript.py
file_fingerprint: 90d2d784bce8c13b080a3c66da948bb2fc2b32651e9cd830377c0e4812b9e93e
last_synced_at: '2026-07-25T00:55:45Z'
defines:
- kind: module
  qualified_name: tests/test_references_typescript:__module__
  lines: 1-71
- kind: constant
  qualified_name: tests/test_references_typescript:FIXTURE
  lines: 10-10
- kind: function
  qualified_name: tests/test_references_typescript:resolver
  lines: 14-15
  signature: def resolver() -> TsResolver
- kind: function
  qualified_name: tests/test_references_typescript:_edges
  lines: 18-20
  signature: 'def _edges(path: Path, resolver: TsResolver) -> set[tuple[str, str, str]]'
- kind: function
  qualified_name: tests/test_references_typescript:test_alias_import_edge
  lines: 23-25
  signature: 'def test_alias_import_edge(resolver: TsResolver)'
- kind: function
  qualified_name: tests/test_references_typescript:test_workspace_package_edge
  lines: 28-30
  signature: 'def test_workspace_package_edge(resolver: TsResolver)'
- kind: function
  qualified_name: tests/test_references_typescript:test_barrel_reexport_edge
  lines: 33-35
  signature: 'def test_barrel_reexport_edge(resolver: TsResolver)'
- kind: function
  qualified_name: tests/test_references_typescript:test_inherits_and_implements
  lines: 38-41
  signature: 'def test_inherits_and_implements(resolver: TsResolver)'
- kind: function
  qualified_name: tests/test_references_typescript:test_class_contains_members
  lines: 44-46
  signature: 'def test_class_contains_members(resolver: TsResolver)'
- kind: function
  qualified_name: tests/test_references_typescript:test_ambient_dts_import_edge
  lines: 49-53
  signature: 'def test_ambient_dts_import_edge(resolver: TsResolver): # `import { map } from "lang-map"` binds to the ambient module symbol keyed # by the literal name (declared in src/types/external.d.ts).'
- kind: function
  qualified_name: tests/test_references_typescript:test_unresolved_external_is_candidate_only
  lines: 56-63
  signature: 'def test_unresolved_external_is_candidate_only(resolver: TsResolver): # An import from a package the project doesn''t define still emits a # candidate edge; the store''s replace_all_edges drops it. We assert the # extractor does NOT resolve it to any project symbol.'
- kind: function
  qualified_name: tests/test_references_typescript:test_intra_file_edges
  lines: 66-70
  signature: 'def test_intra_file_edges(resolver: TsResolver)'
incoming_refs: 0
outgoing_refs: 3
---
<!-- trie:section symbol=tests/test_references_typescript:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=bbcfd5ffb418c757a0a144d2191ebff5ad7111763def11aca197616f40ecdfc5 source_ref=209154e5a359935b1903b13d1ce16920d39b6a44 role=test -->
Integration tests for the TypeScript reference extractor, validating edge types (calls, inherits, implements, contains) produced by `extract_file_data` against a tiny fixture repo.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_references_typescript:FIXTURE fingerprint=883b5996900536d76bf6d49f99ed1a35468676b2f050a082d65e4eb092ae406f body_fp=d73127cafc83f19a45b0e2cafdbdabc9bb1a4cd519456bbede979fac9b91cc2d source_ref=209154e5a359935b1903b13d1ce16920d39b6a44 role=test -->
Resolve the absolute path to the `tiny_ts_repo` fixture directory relative to this test file.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_references_typescript:resolver fingerprint=e8a0cd88c003e249ecd284e7c5f80b987fd3a8b4f5ea5182804ba94c284b539b body_fp=2f050c628ccd8497de01e5fec686b0eea0f0e26cf46ac853a8cb9e11305b19a8 source_ref=209154e5a359935b1903b13d1ce16920d39b6a44 role=test -->
## `def resolver() -> TsResolver`

Pytest fixture that builds and returns a `TsResolver` rooted at the `FIXTURE` directory.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_references_typescript:_edges fingerprint=044beb56d1617660c18dfbc98d5b3e707788ab743447415384ad5639d5611c88 body_fp=8317336f83c6fe1bcafdfb3ce4932aa43947c425f6b1c4a4808ece0c36237ba0 source_ref=209154e5a359935b1903b13d1ce16920d39b6a44 role=util -->
## `def _edges(path: Path, resolver: TsResolver) -> set[tuple[str, str, str]]`

Extract all reference edges from a TypeScript file as `(src_qname, kind, target_qname)` triples.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_references_typescript:test_alias_import_edge fingerprint=93a29111322058140848b411aae2e99c2e029693b4a67cdeed837e2b0ff6e6cc body_fp=842e430632601c432b10e801eded733f0f72cbbb1b6399a1082e43806e674c38 source_ref=209154e5a359935b1903b13d1ce16920d39b6a44 role=test -->
## `def test_alias_import_edge(resolver: TsResolver)`

Assert that an aliased import from a local module produces a `calls` edge to `src/util:double`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_references_typescript:test_workspace_package_edge fingerprint=516ea5a0f6b3e789c193421465375eebd4ef40a4886948466798f04e72f00562 body_fp=4631be49a1ec0127833ffaf6ab8b3242c5770497c8e7d2f336ff6d270366a809 source_ref=209154e5a359935b1903b13d1ce16920d39b6a44 role=test -->
## `def test_workspace_package_edge(resolver: TsResolver)`

Assert that `App.run` emits a `calls` edge to a symbol in a workspace package (`packages/core/index:greet`).
<!-- trie:end -->
<!-- trie:section symbol=tests/test_references_typescript:test_barrel_reexport_edge fingerprint=d6924f27b715a19d3b4d31ebb00ce2000adbf9ceaefcbd0d7f4becf29386dd46 body_fp=26f119a09198a99aa735775855eca2e96614945780e907b0f08bc291dd4e7265 source_ref=209154e5a359935b1903b13d1ce16920d39b6a44 role=test -->
## `def test_barrel_reexport_edge(resolver: TsResolver)`

Assert that a call through a barrel re-export resolves to the canonical `src/store/index:makeStore` target.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_references_typescript:test_inherits_and_implements fingerprint=3cdd36618205fcaca18b5a133ff15609cd2d6c5f981e6478bf00ee95e4b541de body_fp=367847de96029c2ed3a023aec7ed48a042e9dd6f07ae8204c88ed28ead955733 source_ref=209154e5a359935b1903b13d1ce16920d39b6a44 role=test -->
## `def test_inherits_and_implements(resolver: TsResolver)`

Assert that `src/app:App` emits both an `inherits` edge to `src/base:Base` and an `implements` edge to `src/base:Runnable`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_references_typescript:test_class_contains_members fingerprint=6fab4b966f83798f5eb50ad228c592c4536b04e0a94c962f31aaa946cd4d3d80 body_fp=73a8b8a9a0faae1e709d841199277e6ad05f598cfbda7e268d44b3d2cbbe2a2e source_ref=209154e5a359935b1903b13d1ce16920d39b6a44 role=test -->
## `def test_class_contains_members(resolver: TsResolver)`

Assert that `extract_file_data` emits a `contains` edge from `src/app:App` to its member `src/app:App.run`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_references_typescript:test_ambient_dts_import_edge fingerprint=cb0bc0f4a2e3283918cba3b824d1c6ee95841326f1a43460fd5c4ff6a03f2155 body_fp=d7efaaf30b9cb8968b9f0e741a1dfd5b5cda7a9854a71ffb493452f353422719 source_ref=209154e5a359935b1903b13d1ce16920d39b6a44 role=test -->
## `def test_ambient_dts_import_edge(resolver: TsResolver): # `import { map } from "lang-map"` binds to the ambient module symbol keyed # by the literal name (declared in src/types/external.d.ts).`

Assert that an import resolved via an ambient `.d.ts` declaration emits a `calls` edge to the ambient module symbol `lang-map:map`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_references_typescript:test_unresolved_external_is_candidate_only fingerprint=abe3ddcb5c7ca1a7221cf283ca982d968258892ae9ab03447936dc88b42bb393 body_fp=92f0c48c85c3c503968cd37e5b9abd99ba97275ae2af1e8fa213a7a6dec47bb7 source_ref=209154e5a359935b1903b13d1ce16920d39b6a44 role=test -->
## `def test_unresolved_external_is_candidate_only(resolver: TsResolver): # An import from a package the project doesn't define still emits a # candidate edge; the store's replace_all_edges drops it. We assert the # extractor does NOT resolve it to any project symbol.`

Assert that an import from an unknown external package emits a candidate edge but is not resolved to any in-project `src/` symbol.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_references_typescript:test_intra_file_edges fingerprint=d41f504841cdc6878df9f23a73a04afd3f5ff6b3c2bc2deb396ecb7d4e854abe body_fp=32688de07012e512d7b6a0af3c830642ca0c669e326ce3ccc4e5fd1a0069aeeb source_ref=209154e5a359935b1903b13d1ce16920d39b6a44 role=test -->
## `def test_intra_file_edges(resolver: TsResolver)`

Assert that intra-file call edges are extracted for `compute` calling `double` and `secretHelper` within `src/util.ts`.
<!-- trie:end -->