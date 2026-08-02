---
trie_version: 0.3.0
source: tests/test_ts_resolve.py
file_fingerprint: 3b869d0aa5fcb2d5a5511ef5813aebfe10c603dde2ed90c4ce7c8a8d57cfeabb
last_synced_at: '2026-07-25T01:56:18Z'
defines:
- kind: module
  qualified_name: tests/test_ts_resolve:__module__
  lines: 1-106
- kind: constant
  qualified_name: tests/test_ts_resolve:FIXTURE
  lines: 9-9
- kind: function
  qualified_name: tests/test_ts_resolve:resolver
  lines: 13-14
  signature: def resolver() -> TsResolver
- kind: function
  qualified_name: tests/test_ts_resolve:test_relative_import
  lines: 17-19
  signature: 'def test_relative_import(resolver: TsResolver)'
- kind: function
  qualified_name: tests/test_ts_resolve:test_tsconfig_alias
  lines: 22-25
  signature: 'def test_tsconfig_alias(resolver: TsResolver)'
- kind: function
  qualified_name: tests/test_ts_resolve:test_alias_to_barrel_index
  lines: 28-31
  signature: 'def test_alias_to_barrel_index(resolver: TsResolver)'
- kind: function
  qualified_name: tests/test_ts_resolve:test_workspace_package
  lines: 34-36
  signature: 'def test_workspace_package(resolver: TsResolver)'
- kind: function
  qualified_name: tests/test_ts_resolve:test_ambient_dts_resolution_is_left_to_store
  lines: 39-44
  signature: 'def test_ambient_dts_resolution_is_left_to_store(resolver: TsResolver): # The resolver doesn''t know ambient module names (they''re not files); a bare # "lang-map" specifier resolves to None here. The reference extractor binds # the specifier text directly so the store can match the ambient symbol.'
- kind: function
  qualified_name: tests/test_ts_resolve:test_external_unresolved
  lines: 47-50
  signature: 'def test_external_unresolved(resolver: TsResolver)'
- kind: function
  qualified_name: tests/test_ts_resolve:test_resolution_is_memoized
  lines: 53-57
  signature: 'def test_resolution_is_memoized(resolver: TsResolver)'
- kind: function
  qualified_name: tests/test_ts_resolve:test_config_discovery_never_descends_into_vendor_dirs
  lines: 68-87
  signature: def test_config_discovery_never_descends_into_vendor_dirs(tmp_path)
- kind: function
  qualified_name: tests/test_ts_resolve:test_extract_file_data_builds_one_resolver_per_source_root
  lines: 90-105
  signature: def test_extract_file_data_builds_one_resolver_per_source_root(tmp_path, mocker)
incoming_refs: 0
outgoing_refs: 13
---
<!-- trie:section symbol=tests/test_ts_resolve:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=e173ccd0f6f6d642c49aae6eb7d686a06ca67766db44ffe732a1bd90bdeab55b source_ref=4529f2f412cbb9efba25cb814d5ce3cedeb26e1a role=test -->
Tests for `TsResolver` covering relative imports, tsconfig path aliases, barrel index resolution, workspace packages, ambient `.d.ts` specifiers, unresolvable externals, and cache memoization.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_ts_resolve:FIXTURE fingerprint=883b5996900536d76bf6d49f99ed1a35468676b2f050a082d65e4eb092ae406f body_fp=f35505773971c8c0756a4ee9e842c67987e99b962ead6e47885b9360e30194a5 source_ref=4529f2f412cbb9efba25cb814d5ce3cedeb26e1a role=test -->
Absolute path to the `tiny_ts_repo` test fixture directory, used as the root for all resolver tests.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_ts_resolve:resolver fingerprint=e8a0cd88c003e249ecd284e7c5f80b987fd3a8b4f5ea5182804ba94c284b539b body_fp=6f44c289f71cf29614542bdb8748bb183de5d520fa7d512c73e0b0005ded844d source_ref=4529f2f412cbb9efba25cb814d5ce3cedeb26e1a role=test -->
## `def resolver() -> TsResolver`

Pytest fixture that builds and returns a `TsResolver` from the `tiny_ts_repo` fixture directory.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_ts_resolve:test_relative_import fingerprint=458d5f9236b29efca281c42f5dabdb8bf10147c1741064fd6a2baee6ac1c1b1c body_fp=f90bfb7cd2b1024a98809d8dcba03819aa771434f1f6677ba00dd01df48f2fd1 source_ref=4529f2f412cbb9efba25cb814d5ce3cedeb26e1a role=test -->
## `def test_relative_import(resolver: TsResolver)`

Assert that `TsResolver.resolve` correctly resolves a relative `./make` import to `src/store/make`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_ts_resolve:test_tsconfig_alias fingerprint=b77ee41d7d002efcca2041f14d72522a945f46a4550571063824c3a4e8f5d44d body_fp=f1db658482df577929aead6e0d8f78c9c8854f4fed322d5f5458981e73c1991b source_ref=4529f2f412cbb9efba25cb814d5ce3cedeb26e1a role=test -->
## `def test_tsconfig_alias(resolver: TsResolver)`

Verify that `TsResolver.resolve` correctly maps `tsconfig` path aliases (`@/util`, `@/base`) to their canonical `src/`-relative paths.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_ts_resolve:test_alias_to_barrel_index fingerprint=f184b19af24da638577660baf5c4a62c992565c3ba064663522b3c0bac7fef06 body_fp=09cfb7b15cb1d70449218f93e3eaf49d79eb66433526c298f920cfc1d35b95cd source_ref=4529f2f412cbb9efba25cb814d5ce3cedeb26e1a role=test -->
## `def test_alias_to_barrel_index(resolver: TsResolver)`

Assert that a tsconfig alias pointing to a directory resolves to its barrel `index` module.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_ts_resolve:test_workspace_package fingerprint=0be6e2677249942006f946111044fa7d18b89a8b7df42b09817faecad2885461 body_fp=909a7cc081ca44f5f9a4ce30fbef5c2f218d4737ebaee452b9a125ed23c8bf88 source_ref=4529f2f412cbb9efba25cb814d5ce3cedeb26e1a role=test -->
## `def test_workspace_package(resolver: TsResolver)`

Assert that `TsResolver.resolve` maps a workspace package specifier (`@oc/core`) to its index path (`packages/core/index`).
<!-- trie:end -->
<!-- trie:section symbol=tests/test_ts_resolve:test_ambient_dts_resolution_is_left_to_store fingerprint=a9a1dfcabadeedc8d5ec4445e050a1cd7ed5021b027985529304a22080c831eb body_fp=e6bdaf5479e7899eb13786e0502f88ff8887541a9f89ca09725b063a5a98d9b1 source_ref=4529f2f412cbb9efba25cb814d5ce3cedeb26e1a role=test -->
## `def test_ambient_dts_resolution_is_left_to_store(resolver: TsResolver): # The resolver doesn't know ambient module names (they're not files); a bare # "lang-map" specifier resolves to None here. The reference extractor binds # the specifier text directly so the store can match the ambient symbol.`

Assert that `TsResolver.resolve` returns `None` for ambient module specifiers that have no backing file, leaving binding to the store.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_ts_resolve:test_external_unresolved fingerprint=016684ea48b24646e8357beecab150930aaeaa91fddae97a4000fe7ebfb424bb body_fp=0d651cbaae05398b601354fff3ada0dd39f55695de57682373bfcd17f5a43d9e source_ref=4529f2f412cbb9efba25cb814d5ce3cedeb26e1a role=test -->
## `def test_external_unresolved(resolver: TsResolver)`

Assert that `TsResolver.resolve` returns `None` for unknown external packages and well-known third-party packages such as `react`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_ts_resolve:test_resolution_is_memoized fingerprint=87303a5278abe6b5e191d8259fffdcca850c7ab56b03a5254e287b3e028ab4ca body_fp=eac8f00a62eb49f666db5a0f413cbc6c5f3363ffe3e4873f03dcc28aea20fcf5 source_ref=4529f2f412cbb9efba25cb814d5ce3cedeb26e1a role=test -->
## `def test_resolution_is_memoized(resolver: TsResolver)`

Verify that `TsResolver.resolve` caches results in `resolver._cache` keyed by `(specifier, str(from_file))`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_ts_resolve:test_config_discovery_never_descends_into_vendor_dirs fingerprint=7a41720aa10df70a0760d84658409f7a92ff217b9999b2e21b3b4937fe2e83a0 body_fp=1b011f00a8a97f2463ae53d7e1a2207eecb4aec9db2a20a38cf11fd3a646d8e5 source_ref=675aecdf2fb23da1290b41b56bdea0acf34e84f9 role=test -->
## `def test_config_discovery_never_descends_into_vendor_dirs(tmp_path)`

Assert that `_iter_config_files` never traverses `node_modules`, `.git`, `build`, or `dist` vendor/hidden directories.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_ts_resolve:test_extract_file_data_builds_one_resolver_per_source_root fingerprint=730d743e35048229daa440a922e00041b45ccb69e0eeedbc2ef11a1e48826c1d body_fp=b04ef0e790f69b1712b388d2e851c04c389b9e30cc85b1844c79144b083505a4 source_ref=675aecdf2fb23da1290b41b56bdea0acf34e84f9 role=test -->
## `def test_extract_file_data_builds_one_resolver_per_source_root(tmp_path, mocker)`

Assert that `TsResolver.build` is called exactly once when `extract_file_data` processes multiple files sharing a single source root.
<!-- trie:end -->