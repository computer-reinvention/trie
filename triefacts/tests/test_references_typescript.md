---
trie_version: 0.1.9
source: tests/test_references_typescript.py
file_fingerprint: 90d2d784bce8c13b080a3c66da948bb2fc2b32651e9cd830377c0e4812b9e93e
last_synced_at: '2026-06-17T16:41:22Z'
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
- kind: function
  qualified_name: tests/test_references_typescript:_edges
  lines: 18-20
- kind: function
  qualified_name: tests/test_references_typescript:test_alias_import_edge
  lines: 23-25
- kind: function
  qualified_name: tests/test_references_typescript:test_workspace_package_edge
  lines: 28-30
- kind: function
  qualified_name: tests/test_references_typescript:test_barrel_reexport_edge
  lines: 33-35
- kind: function
  qualified_name: tests/test_references_typescript:test_inherits_and_implements
  lines: 38-41
- kind: function
  qualified_name: tests/test_references_typescript:test_class_contains_members
  lines: 44-46
- kind: function
  qualified_name: tests/test_references_typescript:test_ambient_dts_import_edge
  lines: 49-53
- kind: function
  qualified_name: tests/test_references_typescript:test_unresolved_external_is_candidate_only
  lines: 56-63
- kind: function
  qualified_name: tests/test_references_typescript:test_intra_file_edges
  lines: 66-70
incoming_refs: 0
outgoing_refs: 2
---
<!-- trie:section symbol=tests/test_references_typescript:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=bbcfd5ffb418c757a0a144d2191ebff5ad7111763def11aca197616f40ecdfc5 source_ref=209154e5a359935b1903b13d1ce16920d39b6a44 role=test -->
Integration tests for the TypeScript reference extractor, validating edge types (calls, inherits, implements, contains) produced by `extract_file_data` against a tiny fixture repo.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_references_typescript:FIXTURE fingerprint=883b5996900536d76bf6d49f99ed1a35468676b2f050a082d65e4eb092ae406f body_fp=d73127cafc83f19a45b0e2cafdbdabc9bb1a4cd519456bbede979fac9b91cc2d source_ref=209154e5a359935b1903b13d1ce16920d39b6a44 role=test -->
Resolve the absolute path to the `tiny_ts_repo` fixture directory relative to this test file.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_references_typescript:resolver fingerprint=e8a0cd88c003e249ecd284e7c5f80b987fd3a8b4f5ea5182804ba94c284b539b body_fp=c1398e900627451e8c6c6f3054c185d54877fc281a517f286582184c1f788c88 source_ref=209154e5a359935b1903b13d1ce16920d39b6a44 role=test -->
Pytest fixture that builds and returns a `TsResolver` rooted at the `FIXTURE` directory.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_references_typescript:_edges fingerprint=044beb56d1617660c18dfbc98d5b3e707788ab743447415384ad5639d5611c88 body_fp=8598a8442ac8c997615fa894b4bbfd21b2aecccd79d978fd73757bba416cbfd6 source_ref=209154e5a359935b1903b13d1ce16920d39b6a44 role=test -->
Extract all reference edges from a TypeScript file as `(src_qname, kind, target_qname)` triples.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_references_typescript:test_alias_import_edge fingerprint=93a29111322058140848b411aae2e99c2e029693b4a67cdeed837e2b0ff6e6cc body_fp=abb26cd04c1d70238596c613a53dda78a052b6e33da6ee2d52a3498201851fd2 source_ref=209154e5a359935b1903b13d1ce16920d39b6a44 role=test -->
Assert that an aliased import from a local module produces a `calls` edge to `src/util:double`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_references_typescript:test_workspace_package_edge fingerprint=516ea5a0f6b3e789c193421465375eebd4ef40a4886948466798f04e72f00562 body_fp=84e20a9ef48f51c41d8523e633322cf1e4d5ae7b7d80f74bf26a965356894315 source_ref=209154e5a359935b1903b13d1ce16920d39b6a44 role=test -->
Assert that `App.run` emits a `calls` edge to a symbol in a workspace package (`packages/core/index:greet`).
<!-- trie:end -->
<!-- trie:section symbol=tests/test_references_typescript:test_barrel_reexport_edge fingerprint=d6924f27b715a19d3b4d31ebb00ce2000adbf9ceaefcbd0d7f4becf29386dd46 body_fp=d5b2bdb166ccd4196603cccf69101bc49f58d85985c2c127b28bc6f0776ea239 source_ref=209154e5a359935b1903b13d1ce16920d39b6a44 role=test -->
Assert that a call through a barrel re-export resolves to the canonical `src/store/index:makeStore` target.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_references_typescript:test_inherits_and_implements fingerprint=3cdd36618205fcaca18b5a133ff15609cd2d6c5f981e6478bf00ee95e4b541de body_fp=fe1e9c15a1a71f88b0bc89de5255d522390fd7661d55c2b409aafac691d8a328 source_ref=209154e5a359935b1903b13d1ce16920d39b6a44 role=test -->
Assert that `src/app:App` emits both an `inherits` edge to `src/base:Base` and an `implements` edge to `src/base:Runnable`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_references_typescript:test_class_contains_members fingerprint=6fab4b966f83798f5eb50ad228c592c4536b04e0a94c962f31aaa946cd4d3d80 body_fp=55ecb70bbd0e1e26aee56cc8a9464d7ea1b16a5d5216293dc2f6035d1f507599 source_ref=209154e5a359935b1903b13d1ce16920d39b6a44 role=test -->
Assert that `extract_file_data` emits a `contains` edge from `src/app:App` to its member `src/app:App.run`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_references_typescript:test_ambient_dts_import_edge fingerprint=cb0bc0f4a2e3283918cba3b824d1c6ee95841326f1a43460fd5c4ff6a03f2155 body_fp=852748fbd143b4459cfcc03876c118085fbb1b9cfbbb5e9c0af739569f8bd480 source_ref=209154e5a359935b1903b13d1ce16920d39b6a44 role=test -->
Assert that an import resolved via an ambient `.d.ts` declaration emits a `calls` edge to the ambient module symbol `lang-map:map`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_references_typescript:test_unresolved_external_is_candidate_only fingerprint=abe3ddcb5c7ca1a7221cf283ca982d968258892ae9ab03447936dc88b42bb393 body_fp=85e21ca3c1c79e4904e7504be1dcb9b9a95af11d53c4a43a02b62eac20f282c3 source_ref=209154e5a359935b1903b13d1ce16920d39b6a44 role=test -->
Assert that an import from an unknown external package emits a candidate edge but is not resolved to any in-project `src/` symbol.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_references_typescript:test_intra_file_edges fingerprint=d41f504841cdc6878df9f23a73a04afd3f5ff6b3c2bc2deb396ecb7d4e854abe body_fp=68579832f2d7c094ff37b0959a657348b111dce07c3f586ef3c47c1ac20e623c source_ref=209154e5a359935b1903b13d1ce16920d39b6a44 role=test -->
Assert that intra-file call edges are extracted for `compute` calling `double` and `secretHelper` within `src/util.ts`.
<!-- trie:end -->