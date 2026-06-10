---
trie_version: 0.1.5
source: tests/test_metadata_refresh.py
file_fingerprint: 2bea858f50a5d11432e54ce0156a70e43c81025119d87ce6a8965da7a4561aa6
last_synced_at: '2026-06-10T13:17:02Z'
description: Metadata-only triefact refresh.
defines:
- kind: module
  qualified_name: tests/test_metadata_refresh:__module__
  lines: 1-321
- kind: function
  qualified_name: tests/test_metadata_refresh:project
  lines: 39-59
- kind: function
  qualified_name: tests/test_metadata_refresh:_sync_both
  lines: 62-79
- kind: function
  qualified_name: tests/test_metadata_refresh:_read_yaml_front
  lines: 82-87
- kind: function
  qualified_name: tests/test_metadata_refresh:_section_bodies
  lines: 90-104
- kind: function
  qualified_name: tests/test_metadata_refresh:test_refresh_does_not_call_the_llm
  lines: 112-128
- kind: function
  qualified_name: tests/test_metadata_refresh:test_refresh_preserves_section_bodies_byte_for_byte
  lines: 131-152
- kind: function
  qualified_name: tests/test_metadata_refresh:test_refresh_preserves_last_synced_at
  lines: 155-175
- kind: function
  qualified_name: tests/test_metadata_refresh:test_refresh_picks_up_new_edges_in_front_matter
  lines: 178-207
- kind: function
  qualified_name: tests/test_metadata_refresh:test_refresh_is_idempotent
  lines: 210-225
- kind: function
  qualified_name: tests/test_metadata_refresh:test_refresh_skips_missing_triefact
  lines: 228-238
- kind: function
  qualified_name: tests/test_metadata_refresh:test_verify_passes_after_refresh
  lines: 241-263
- kind: function
  qualified_name: tests/test_metadata_refresh:test_cli_sync_metadata_only_mutex_with_other_flags
  lines: 271-294
- kind: function
  qualified_name: tests/test_metadata_refresh:test_cli_sync_metadata_only_runs
  lines: 297-320
incoming_refs: 0
outgoing_refs: 22
---
<!-- trie:section symbol=tests/test_metadata_refresh:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=3c16a1d6c0df615766baa0df7332a78ce75269150f5a3c1e9782aea5082a767b source_ref=65204173c592bc34e87ebc59176aeb0c67ef4747 role=test-infrastructure -->
Tests metadata-only triefact refresh functionality to ensure it updates front matter without calling the LLM.

- Verifies section bodies and fingerprints remain byte-identical after refresh
- Tests that `last_synced_at` timestamp preservation indicates LLM didn't run
- Confirms refresh picks up new graph edges in `incoming_refs`/`outgoing_refs`
- Validates idempotent behavior and CLI integration with exclusive flag handling
<!-- trie:end -->
<!-- trie:section symbol=tests/test_metadata_refresh:project fingerprint=65fd0b8d1c2fe0511dfb8e02ca8712e1da978440f17e1e72a14ebc38292a6981 body_fp=5669ab3764386acfaf697a5e395ed605ef9e44dea3157eeaa5e50f32a9c24fdb source_ref=65204173c592bc34e87ebc59176aeb0c67ef4747 role=test-infrastructure -->
Creates a test project with two Python modules where beta imports from alpha.

- Returns the temporary project root directory path
- Sets up complete trie configuration in `trie.toml`
- Creates `src/alpha.py` with `alpha_fn()` function
- Creates `src/beta.py` that imports and calls `alpha_fn()`
<!-- trie:end -->
<!-- trie:section symbol=tests/test_metadata_refresh:_sync_both fingerprint=34f3862f727710588e479ae81af4b72c3d861240fedba9be071fe5ad9af64a17 body_fp=9c6ceb451bec85a6d49987a3bbaf95cac989ebdcada1a4ec37abc72137e6d260 source_ref=65204173c592bc34e87ebc59176aeb0c67ef4747 role=test-infrastructure -->
Scans and syncs both alpha.py and beta.py modules to create real triefacts on disk for testing refresh functionality.

- Returns an open Store that the caller must close
- Uses FakeTrieClient with deterministic prose output
- Creates .trie/graph.db database and performs initial sync
<!-- trie:end -->
<!-- trie:section symbol=tests/test_metadata_refresh:_read_yaml_front fingerprint=7e5679b0a04dfddc9fdfb4811524e98777352d0e45971091c9817ede8816a4a2 body_fp=ca057f42415fe59fc01fa8a5b6b430e6405c7ba30652f888dc1c09ea60cbc09f source_ref=65204173c592bc34e87ebc59176aeb0c67ef4747 role=test-infrastructure -->
Parse YAML front matter from a triefact file and return it as a dictionary.

- Raises AssertionError if no YAML front matter is found
<!-- trie:end -->
<!-- trie:section symbol=tests/test_metadata_refresh:_section_bodies fingerprint=a78be54ef29af611dbd8e6b081cebdb4f8bf91b70f60e801bb64fc6705ca735a body_fp=10b8fb5b9aed4f785d71c86828ffe6d5e6e0f679119a3065c60acbfe23234b23 source_ref=65204173c592bc34e87ebc59176aeb0c67ef4747 role=test-infrastructure -->
Extracts section bodies from a triefact file as a qualified name to content mapping.

- Returns: dict mapping symbol qualified names to their section body text between HTML comment sentinels
<!-- trie:end -->
<!-- trie:section symbol=tests/test_metadata_refresh:test_refresh_does_not_call_the_llm fingerprint=10efbe7f965fac4bfe13d5fb4ca4d3823e9bbe88e28e269add9756d9241929f6 body_fp=d8b778b27825fc6fa7d5447f12d455679da5c9d04dcdb4900ae3ccca7f5f0b8d source_ref=65204173c592bc34e87ebc59176aeb0c67ef4747 role=test -->
Verifies that `refresh_triefact_metadata` runs without requiring an LLM client, confirming metadata refresh is free and returns a `MetadataRefreshResult`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_metadata_refresh:test_refresh_preserves_section_bodies_byte_for_byte fingerprint=31af1871d315749a9c025d6b02b4438439f67bf623d93180d8dd9362c6159957 body_fp=687f939c940c3eeeecf5f5bfe252cb560569c6c7229293255da60f897e874dd4 source_ref=65204173c592bc34e87ebc59176aeb0c67ef4747 role=test -->
Verifies that refresh_triefact_metadata preserves section body content and sentinel comments unchanged.

- Captures section bodies and sentinels before metadata refresh operation
- Asserts bodies and sentinels remain byte-identical after refresh completes
<!-- trie:end -->
<!-- trie:section symbol=tests/test_metadata_refresh:test_refresh_preserves_last_synced_at fingerprint=347a26e83a5aa2b48ca7bf04dafc020f7cd666df80981ad495d005d3baaf8f53 body_fp=671916952fdd8eeea783acb39ff35992e23eabf313aa5c8b63b2d7fb14c4d8c7 source_ref=65204173c592bc34e87ebc59176aeb0c67ef4747 role=test -->
Verifies that metadata refresh preserves the `last_synced_at` timestamp from triefact front matter.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_metadata_refresh:test_refresh_picks_up_new_edges_in_front_matter fingerprint=6263b0a5f31e8703e1010346c981e743ea8bfd5e1648e1ff930951164076bc6c body_fp=50ceffdbad93cc7407eea2e5784ca78cffaf24225ac240f4f58ba916a3ed672b source_ref=65204173c592bc34e87ebc59176aeb0c67ef4747 role=test -->
Tests that metadata refresh detects new cross-module references and updates ref counts in triefact front matter.

- Adds a new module referencing an existing function after initial sync
- Verifies `incoming_refs` count increases by 1 after refresh
<!-- trie:end -->
<!-- trie:section symbol=tests/test_metadata_refresh:test_refresh_is_idempotent fingerprint=0c9ddae21b38445f7612817c1a778908943e8e78e7f37def01bdefe1c08774de body_fp=1d9a45506f319c37ad5b07382d390aa556fc57a8f95f67973978f5a783c77b90 source_ref=65204173c592bc34e87ebc59176aeb0c67ef4747 role=test -->
Tests that `refresh_triefact_metadata` is idempotent by verifying consecutive refresh calls return `changed=False` on the second call.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_metadata_refresh:test_refresh_skips_missing_triefact fingerprint=f78515fc126a5e94dc695fb2c41fc0a47424413eb197cf2c80054305065d3589 body_fp=f79a59e614738825e291135950689d4425cfcc232433be809d9b42a81de0dd20 source_ref=65204173c592bc34e87ebc59176aeb0c67ef4747 role=test -->
Tests that `refresh_triefact_metadata` returns unchanged result when triefact file doesn't exist yet.

- Creates new source file without syncing it first
- Verifies refresh returns `changed=False` for missing triefact
<!-- trie:end -->
<!-- trie:section symbol=tests/test_metadata_refresh:test_verify_passes_after_refresh fingerprint=4eaa18dfe98b605a6c3f831c8389b56cb62a3a1a6c9516dcd97cb212e9e1049d body_fp=6015a4be8533412ef8fc589ab8720867ea463be3131ec00e3d47b8418ee45140 source_ref=65204173c592bc34e87ebc59176aeb0c67ef4747 role=test -->
Tests that `trie verify` passes after metadata refresh, ensuring no drift in section fingerprints.

- Verifies project is clean before and after refreshing metadata for both test modules
- Confirms metadata refresh preserves section content that verify checks against
<!-- trie:end -->
<!-- trie:section symbol=tests/test_metadata_refresh:test_cli_sync_metadata_only_mutex_with_other_flags fingerprint=bcc16ea751d379805d3dcab93e5c08c3d015fa75936a750c7d0720dad41bc5e8 body_fp=8595072b5d03e6bbe46c76ce2fd56eebdcea3844bc893b5f9c4b768287bfab6d source_ref=65204173c592bc34e87ebc59176aeb0c67ef4747 role=test-infrastructure -->
Tests that `--metadata-only` flag is mutually exclusive with other sync command flags.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_metadata_refresh:test_cli_sync_metadata_only_runs fingerprint=638512cb71cdff8c21b134ba723f92f1951cce6873edf584fb30513f4b34677e body_fp=e55821ffff268fce8d824d8ff079d6676e210163ea18519d53e2e68cad36181a source_ref=65204173c592bc34e87ebc59176aeb0c67ef4747 role=cli-interface -->
Tests end-to-end CLI execution of `trie sync --metadata-only` after cold sync, verifying it runs without invoking the LLM.

- Patches `make_client` to fail if the LLM client is constructed during metadata-only refresh
- Asserts CLI exits cleanly and reports refresh count in output
<!-- trie:end -->