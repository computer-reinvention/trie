---
trie_version: 0.1.9
source: tests/test_ts_resolve.py
file_fingerprint: 9e72105cf525ec878b50c655514edd58ec8cf00f3d0c403e64d38452216f2826
last_synced_at: '2026-07-25T00:55:43Z'
defines:
- kind: module
  qualified_name: tests/test_ts_resolve:__module__
  lines: 1-58
- kind: constant
  qualified_name: tests/test_ts_resolve:FIXTURE
  lines: 9-9
- kind: function
  qualified_name: tests/test_ts_resolve:resolver
  lines: 13-14
- kind: function
  qualified_name: tests/test_ts_resolve:test_relative_import
  lines: 17-19
- kind: function
  qualified_name: tests/test_ts_resolve:test_tsconfig_alias
  lines: 22-25
- kind: function
  qualified_name: tests/test_ts_resolve:test_alias_to_barrel_index
  lines: 28-31
- kind: function
  qualified_name: tests/test_ts_resolve:test_workspace_package
  lines: 34-36
- kind: function
  qualified_name: tests/test_ts_resolve:test_ambient_dts_resolution_is_left_to_store
  lines: 39-44
- kind: function
  qualified_name: tests/test_ts_resolve:test_external_unresolved
  lines: 47-50
- kind: function
  qualified_name: tests/test_ts_resolve:test_resolution_is_memoized
  lines: 53-57
incoming_refs: 0
outgoing_refs: 1
---
<!-- trie:section symbol=tests/test_ts_resolve:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=e173ccd0f6f6d642c49aae6eb7d686a06ca67766db44ffe732a1bd90bdeab55b source_ref=4529f2f412cbb9efba25cb814d5ce3cedeb26e1a role=test -->
Tests for `TsResolver` covering relative imports, tsconfig path aliases, barrel index resolution, workspace packages, ambient `.d.ts` specifiers, unresolvable externals, and cache memoization.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_ts_resolve:FIXTURE fingerprint=883b5996900536d76bf6d49f99ed1a35468676b2f050a082d65e4eb092ae406f body_fp=f35505773971c8c0756a4ee9e842c67987e99b962ead6e47885b9360e30194a5 source_ref=4529f2f412cbb9efba25cb814d5ce3cedeb26e1a role=test -->
Absolute path to the `tiny_ts_repo` test fixture directory, used as the root for all resolver tests.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_ts_resolve:resolver fingerprint=e8a0cd88c003e249ecd284e7c5f80b987fd3a8b4f5ea5182804ba94c284b539b body_fp=b689ec19c9a2be109b16b705504b07e95adc1915aa331c1f4dc48b4a1731760b source_ref=4529f2f412cbb9efba25cb814d5ce3cedeb26e1a role=test -->
Pytest fixture that builds and returns a `TsResolver` from the `tiny_ts_repo` fixture directory.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_ts_resolve:test_relative_import fingerprint=458d5f9236b29efca281c42f5dabdb8bf10147c1741064fd6a2baee6ac1c1b1c body_fp=c90bb97f800e2b16601361f91123bcacc6ae0224c71355d0b48647bb91d01897 source_ref=4529f2f412cbb9efba25cb814d5ce3cedeb26e1a role=test -->
Assert that `TsResolver.resolve` correctly resolves a relative `./make` import to `src/store/make`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_ts_resolve:test_tsconfig_alias fingerprint=b77ee41d7d002efcca2041f14d72522a945f46a4550571063824c3a4e8f5d44d body_fp=badc541ca1d3b8ab8eb1bab740274a7b3cdb3057b3c3e3c2d47e8a05696a77f2 source_ref=4529f2f412cbb9efba25cb814d5ce3cedeb26e1a role=test -->
Verify that `TsResolver.resolve` correctly maps `tsconfig` path aliases (`@/util`, `@/base`) to their canonical `src/`-relative paths.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_ts_resolve:test_alias_to_barrel_index fingerprint=f184b19af24da638577660baf5c4a62c992565c3ba064663522b3c0bac7fef06 body_fp=3f0394b4acf23debd52d6834fa7333d7aaddeac4940357b1ae2ab551758c8358 source_ref=4529f2f412cbb9efba25cb814d5ce3cedeb26e1a role=test -->
Assert that a tsconfig alias pointing to a directory resolves to its barrel `index` module.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_ts_resolve:test_workspace_package fingerprint=0be6e2677249942006f946111044fa7d18b89a8b7df42b09817faecad2885461 body_fp=9d7ecd544823d79045445e0aec1324e2127042e24ac8ff00c8c5d3677e1fdb5a source_ref=4529f2f412cbb9efba25cb814d5ce3cedeb26e1a role=test -->
Assert that `TsResolver.resolve` maps a workspace package specifier (`@oc/core`) to its index path (`packages/core/index`).
<!-- trie:end -->
<!-- trie:section symbol=tests/test_ts_resolve:test_ambient_dts_resolution_is_left_to_store fingerprint=a9a1dfcabadeedc8d5ec4445e050a1cd7ed5021b027985529304a22080c831eb body_fp=a60b3d6cb3fa42d696904ac4e85ec068586f557ac9192d7e5052d810b4f40854 source_ref=4529f2f412cbb9efba25cb814d5ce3cedeb26e1a role=test -->
Assert that `TsResolver.resolve` returns `None` for ambient module specifiers that have no backing file, leaving binding to the store.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_ts_resolve:test_external_unresolved fingerprint=016684ea48b24646e8357beecab150930aaeaa91fddae97a4000fe7ebfb424bb body_fp=c9a99642bfc4d3777324533aa1f3d468ba2a6381b9d7bcd291f222e82e3c49ac source_ref=4529f2f412cbb9efba25cb814d5ce3cedeb26e1a role=test -->
Assert that `TsResolver.resolve` returns `None` for unknown external packages and well-known third-party packages such as `react`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_ts_resolve:test_resolution_is_memoized fingerprint=87303a5278abe6b5e191d8259fffdcca850c7ab56b03a5254e287b3e028ab4ca body_fp=8e28cba64e5e411c6ab3505f1947142e5795a22565cf9eb0b26cfc6a98590151 source_ref=4529f2f412cbb9efba25cb814d5ce3cedeb26e1a role=test -->
Verify that `TsResolver.resolve` caches results in `resolver._cache` keyed by `(specifier, str(from_file))`.
<!-- trie:end -->