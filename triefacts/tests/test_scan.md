---
trie_version: 0.1.5
source: tests/test_scan.py
file_fingerprint: 778ee23d148c0a3f4e1ef2b0394a351d2fc6e229982d25a1898266f040943a27
last_synced_at: '2026-06-03T21:00:30Z'
defines:
- kind: module
  qualified_name: tests/test_scan:__module__
  lines: 1-213
- kind: function
  qualified_name: tests/test_scan:project
  lines: 13-28
- kind: function
  qualified_name: tests/test_scan:_scan
  lines: 31-35
- kind: function
  qualified_name: tests/test_scan:test_first_scan_marks_all_new
  lines: 38-50
- kind: function
  qualified_name: tests/test_scan:test_rescan_unchanged_skips_parse
  lines: 53-63
- kind: function
  qualified_name: tests/test_scan:test_modified_file_is_updated
  lines: 66-81
- kind: function
  qualified_name: tests/test_scan:test_added_file_is_new
  lines: 84-96
- kind: function
  qualified_name: tests/test_scan:test_removed_file_is_cleaned_up
  lines: 99-112
- kind: function
  qualified_name: tests/test_scan:test_scan_populates_cross_file_edges
  lines: 115-139
- kind: function
  qualified_name: tests/test_scan:test_scan_populates_intra_file_edges
  lines: 142-160
- kind: function
  qualified_name: tests/test_scan:test_edges_rebuilt_when_file_changes
  lines: 163-190
- kind: function
  qualified_name: tests/test_scan:test_excluded_file_treated_as_removed
  lines: 193-212
incoming_refs: 0
outgoing_refs: 3
---
<!-- trie:section symbol=tests/test_scan:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=f146cfea969e95e5c9972d26f0e0007d1246282ba4b4c013c5cfc08afc4d5964 source_ref=481caf41ed6eb1f944c4b27db6707de091ad64c3 role=test-infrastructure -->
Tests for project scanning functionality that discovers, parses, and tracks Python source files and their symbols.

- Contains pytest fixtures and test functions covering file discovery, change detection, and symbol relationship tracking
- Tests incremental scanning behavior with new, modified, and removed files
- Verifies cross-file and intra-file reference edge detection and maintenance
<!-- trie:end -->
<!-- trie:section symbol=tests/test_scan:project fingerprint=3244bb3322e015de8418a9846af3f814b535348d60a14069119899f32f43ad29 body_fp=df3f1f590e9534b4be5a1d7a3c91916a41abe2557aae8fd9b1b7b9fca12a86aa source_ref=481caf41ed6eb1f944c4b27db6707de091ad64c3 role=test-infrastructure -->
Creates a temporary project directory with trie configuration and sample Python files for testing.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_scan:_scan fingerprint=02aa825501406c55a6abf16d9c5c7e4028d2ee0794e5c14f08ba2e960e706a01 body_fp=7cfb93e9b7d197284e29e40c9d751fd1baf8d127392b0cfddaf67ac253bf4a0e source_ref=481caf41ed6eb1f944c4b27db6707de091ad64c3 role=test-infrastructure -->
Helper function that loads configuration, creates a store, and scans the given project.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_scan:test_first_scan_marks_all_new fingerprint=20449e998a56b18a554998b7c2da16699db555be4d445864db75f0812640ad16 body_fp=80e68bf378ea6265764d29b93ff1236b3028d97c8d91194abea0ab2b73da082f source_ref=481caf41ed6eb1f944c4b27db6707de091ad64c3 role=test-infrastructure -->
Tests that scanning a fresh project marks all discovered files and symbols as new.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_scan:test_rescan_unchanged_skips_parse fingerprint=be64ec917dd52a447d35da09df1f2c8ef6e5e811f0053b07e63ced56a9442f59 body_fp=a36e25d189f0a4b5c9dbc33050c2b4e3ca3eb52e21d9257fd4a87225039f8e6e source_ref=481caf41ed6eb1f944c4b27db6707de091ad64c3 role=change-detection -->
Verifies that rescanning unchanged files detects no new or updated files and preserves symbol count.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_scan:test_modified_file_is_updated fingerprint=ae98369fdef8f951260ff15b8226df69ec79e74e92af1b422819213717fa57bc body_fp=94da008cb5e11ad9b58bc51e431b8682c678fd23f3c02969723e7a83a2c86e11 source_ref=481caf41ed6eb1f944c4b27db6707de091ad64c3 role=source-parsing -->
Tests that scan_project correctly identifies and updates a modified file, detecting new symbols added to the file.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_scan:test_added_file_is_new fingerprint=7e0c261b141f74fb177b0dc4eff38e8100d011a77827403e7a25a779cc40d891 body_fp=d99a6f8a28923dbcb1e9e82f3a7938b10a7c54330870587891d768f57c8e42c3 source_ref=481caf41ed6eb1f944c4b27db6707de091ad64c3 role=test-infrastructure -->
Tests that adding a new file to the project is correctly detected as a new file in subsequent scans.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_scan:test_removed_file_is_cleaned_up fingerprint=d62127c8837af97031670cfbbafb155f2f0a19d56a98190d0619abb94fcf2c71 body_fp=6eb901666076ccde7393c0e0df0abccb333bbd7fe50bcc3899aeb1b680d3a4f3 source_ref=481caf41ed6eb1f944c4b27db6707de091ad64c3 role=change-detection -->
Verifies that scan_project correctly removes deleted files from the store and updates counters.

- Deletes a file between scans and asserts files_removed count and store cleanup
<!-- trie:end -->
<!-- trie:section symbol=tests/test_scan:test_scan_populates_cross_file_edges fingerprint=ee21224ba5291434c51bb572f09d348bfe9ed4a87fb6de79b25efcccf97966e1 body_fp=3d6a14412762be66a0e9a55ac2c5a7b48a4918f80da9b8b6a07feb81e28155b5 source_ref=481caf41ed6eb1f944c4b27db6707de091ad64c3 role=test-infrastructure -->
Verifies that scanning creates cross-file reference edges between symbols in different files.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_scan:test_scan_populates_intra_file_edges fingerprint=30a16a88497eca0d4b18b529ff5153ee08a02cc0948460e966b6e97ce6daa1d5 body_fp=16fbe01b58311ab0ef4af81a3228c9a409cdd739d5b39d19fb1dff7ddb0f1f42 source_ref=481caf41ed6eb1f944c4b27db6707de091ad64c3 role=test-infrastructure -->
Verifies that scanning detects function calls within the same file and stores reference edges.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_scan:test_edges_rebuilt_when_file_changes fingerprint=14895261e771f79e731ea1c272328b2d18924c0e85ae1ba6eab7068fdb0b96d4 body_fp=477670eb743a587c9e0cebe4322cf092e5375f816e4a81be853665c5b2b028da source_ref=481caf41ed6eb1f944c4b27db6707de091ad64c3 role=test-infrastructure -->
Verifies that dependency edges are correctly updated when a file's imports or references change.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_scan:test_excluded_file_treated_as_removed fingerprint=3740a9a595051648f04c664560d8cb777c94c244bb6c4ee7f09d3d5ce8e57966 body_fp=29c2a2e590886f381b4c317e7cc73a8fa46fb9323e8985613d2d4126ecacc333 source_ref=481caf41ed6eb1f944c4b27db6707de091ad64c3 role=test-infrastructure -->
Tests that files excluded by updated configuration are treated as removed from the project.

- Performs initial scan, then modifies config to exclude src/alpha.py via exclude pattern
- Verifies scan result shows one removed file and store no longer contains the excluded file
<!-- trie:end -->