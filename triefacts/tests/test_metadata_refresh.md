---
trie_version: 0.1.5
source: tests/test_metadata_refresh.py
file_fingerprint: 2bea858f50a5d11432e54ce0156a70e43c81025119d87ce6a8965da7a4561aa6
last_synced_at: '2026-06-03T20:57:32Z'
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
<!-- trie:section symbol=tests/test_metadata_refresh:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=e0acd0f0c6d0faba30442e3f338ec464327730d56cca06682812c0838af3e5fd source_ref=65204173c592bc34e87ebc59176aeb0c67ef4747 -->
Tests metadata-only triefact refresh functionality that updates front matter without calling the LLM.

- Verifies `refresh_triefact_metadata` preserves section bodies byte-for-byte
- Confirms `last_synced_at` timestamp is preserved (reserved for LLM runs)
- Tests edge count updates when graph changes between syncs
- Validates idempotent behavior and CLI integration with mutex flag checking
<!-- trie:end -->
<!-- trie:section symbol=tests/test_metadata_refresh:project fingerprint=65fd0b8d1c2fe0511dfb8e02ca8712e1da978440f17e1e72a14ebc38292a6981 body_fp=c36ae8c9572e996eedcfece16091e50a6b13c986768a7d9f2825ec12311a7b37 source_ref=65204173c592bc34e87ebc59176aeb0c67ef4747 -->
Creates a temporary project with two Python modules and a cross-file import for testing metadata refresh.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_metadata_refresh:_sync_both fingerprint=34f3862f727710588e479ae81af4b72c3d861240fedba9be071fe5ad9af64a17 body_fp=0374351e47d042ac2f4542e1018c6c1eec6acace16633c985ed42bc81f442c22 source_ref=65204173c592bc34e87ebc59176aeb0c67ef4747 -->
Scans and syncs both alpha.py and beta.py modules using a fake client to create triefacts for testing.

- Returns an open Store instance that the caller must close
<!-- trie:end -->
<!-- trie:section symbol=tests/test_metadata_refresh:_read_yaml_front fingerprint=7e5679b0a04dfddc9fdfb4811524e98777352d0e45971091c9817ede8816a4a2 body_fp=8129c8357526adcf4ab3b7a965ac7508db7cdc9321270ac1464d914ae9d26d85 source_ref=65204173c592bc34e87ebc59176aeb0c67ef4747 -->
Parses YAML front matter from a triefact file, asserting its presence and returning the loaded dictionary.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_metadata_refresh:_section_bodies fingerprint=a78be54ef29af611dbd8e6b081cebdb4f8bf91b70f60e801bb64fc6705ca735a body_fp=0bb05559eae603697f5e7ebf3a407dda0030d3aafb731b13279c5cb8ad5e1bac source_ref=65204173c592bc34e87ebc59176aeb0c67ef4747 -->
Extracts symbol qualified names mapped to their section body text from a triefact file by parsing trie comment sentinels.

- Used to verify that section content remains byte-identical across metadata refreshes
<!-- trie:end -->
<!-- trie:section symbol=tests/test_metadata_refresh:test_refresh_does_not_call_the_llm fingerprint=10efbe7f965fac4bfe13d5fb4ca4d3823e9bbe88e28e269add9756d9241929f6 body_fp=d10f916c7ee56e09dc78e386a505ddf82600de641b2dbb46b642d7d28942343c source_ref=65204173c592bc34e87ebc59176aeb0c67ef4747 -->
Verifies that `refresh_triefact_metadata` operates without requiring an LLM client, confirming the metadata refresh is cost-free.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_metadata_refresh:test_refresh_preserves_section_bodies_byte_for_byte fingerprint=31af1871d315749a9c025d6b02b4438439f67bf623d93180d8dd9362c6159957 body_fp=8158449cd8a2d7fe8126fd2ceae08f4b7edcade76888a4882b43b70a826e9f9c source_ref=65204173c592bc34e87ebc59176aeb0c67ef4747 -->
Verifies that refreshing triefact metadata preserves section bodies and sentinels byte-for-byte.

- Captures section content and HTML sentinels before refresh operation
- Asserts content remains identical after metadata refresh completes
<!-- trie:end -->
<!-- trie:section symbol=tests/test_metadata_refresh:test_refresh_preserves_last_synced_at fingerprint=347a26e83a5aa2b48ca7bf04dafc020f7cd666df80981ad495d005d3baaf8f53 body_fp=c36fc7f9b6efbe1c9ed4c98b18ddde05366d81789aff386d022665eacf8293e4 source_ref=65204173c592bc34e87ebc59176aeb0c67ef4747 -->
Tests that `refresh_triefact_metadata` preserves the `last_synced_at` timestamp from the original triefact.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_metadata_refresh:test_refresh_picks_up_new_edges_in_front_matter fingerprint=6263b0a5f31e8703e1010346c981e743ea8bfd5e1648e1ff930951164076bc6c body_fp=0a84185f9ddc71d60e53dcf9f8b1aa22b932557cc5a2ca6d87dcd4d028235be4 source_ref=65204173c592bc34e87ebc59176aeb0c67ef4747 -->
Tests that metadata refresh updates reference counts when graph edges change between syncs.

- Adds a third module that imports `alpha_fn` after initial sync to increase incoming references
- Verifies `incoming_refs` count increments by one in alpha's triefact front matter after refresh
<!-- trie:end -->
<!-- trie:section symbol=tests/test_metadata_refresh:test_refresh_is_idempotent fingerprint=0c9ddae21b38445f7612817c1a778908943e8e78e7f37def01bdefe1c08774de body_fp=a4c9684629d5ceb4418ce46e713af1f613093817bf440ba5f45aba00aa6d1f52 source_ref=65204173c592bc34e87ebc59176aeb0c67ef4747 -->
Verifies that running `refresh_triefact_metadata` twice produces no changes on the second call.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_metadata_refresh:test_refresh_skips_missing_triefact fingerprint=f78515fc126a5e94dc695fb2c41fc0a47424413eb197cf2c80054305065d3589 body_fp=ab8284541ad1dae65c03a43c483d10ef28b291bd8b045508d52fbec6352a7a65 source_ref=65204173c592bc34e87ebc59176aeb0c67ef4747 -->
Tests that `refresh_triefact_metadata` is a no-op when called on a source file with no existing triefact.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_metadata_refresh:test_verify_passes_after_refresh fingerprint=4eaa18dfe98b605a6c3f831c8389b56cb62a3a1a6c9516dcd97cb212e9e1049d body_fp=1a82b36e8c897df28d9c76f366c098c44b449a4917537cf4be3ae422365f04a2 source_ref=65204173c592bc34e87ebc59176aeb0c67ef4747 -->
Verifies that `trie verify` passes after refreshing metadata to ensure no detectable fingerprint drift occurs.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_metadata_refresh:test_cli_sync_metadata_only_mutex_with_other_flags fingerprint=bcc16ea751d379805d3dcab93e5c08c3d015fa75936a750c7d0720dad41bc5e8 body_fp=645c38b359f41c7509d1c3fc16a365643b0bb85b8aaf2ecd0051e4b7e1a2a231 source_ref=65204173c592bc34e87ebc59176aeb0c67ef4747 -->
Verifies that `--metadata-only` flag is mutually exclusive with other sync command flags.

- Tests that combining `--metadata-only` with `--all`, `--dry-run`, `--budget`, `--limit`, or `--file` exits with code 1
- Ensures error message contains "cannot be combined"
<!-- trie:end -->
<!-- trie:section symbol=tests/test_metadata_refresh:test_cli_sync_metadata_only_runs fingerprint=638512cb71cdff8c21b134ba723f92f1951cce6873edf584fb30513f4b34677e body_fp=d1b28d4756eab530e9ed67f22b589ce298a078a88c634abe6d9925398e1f567d source_ref=65204173c592bc34e87ebc59176aeb0c67ef4747 -->
Tests that `trie sync --metadata-only` CLI command runs successfully and reports refresh count without invoking the LLM.

- Sets up project with existing triefacts via cold sync
- Patches make_client to fail if LLM client construction is attempted  
- Verifies command exits cleanly and outputs "refreshed metadata" message
<!-- trie:end -->