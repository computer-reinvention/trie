---
trie_version: 0.1.0
source: tests/test_scan.py
file_fingerprint: 705f746b6b19069845298144318a47905041bb77483b0de82991151c9e69e497
last_synced_at: '2026-05-12T18:27:36Z'
defines:
- kind: function
  qualified_name: tests/test_scan:project
  lines: 13-28
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
<!-- trie:section symbol=tests/test_scan:project fingerprint=3244bb3322e015de8418a9846af3f814b535348d60a14069119899f32f43ad29 body_fp=c1ea08ee2de0b6a839c8b1aae56962b2f65752837a9c60fb1be84a5e17db44c5 -->
## `project(tmp_path: Path) -> Path`

Pytest fixture that creates a minimal project root with `trie.toml` and two stub Python source files.

- **Returns** `tmp_path` configured as a ready-to-scan project root.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_scan:test_first_scan_marks_all_new fingerprint=20449e998a56b18a554998b7c2da16699db555be4d445864db75f0812640ad16 body_fp=a62265ed0852fbf9c175f416ef2adae763be364d621a8f1b2ecf3443a2fc7f84 -->
## `test_first_scan_marks_all_new(project: Path)`

Assert that an initial scan over a fresh project reports all files and symbols as new.

- Expects 2 files, 3 symbols (`alpha`, `beta_a`, `beta_b`), zero updated/unchanged counts.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_scan:test_rescan_unchanged_skips_parse fingerprint=be64ec917dd52a447d35da09df1f2c8ef6e5e811f0053b07e63ced56a9442f59 body_fp=3b776787df9b3987042691dafc1f9dc69347ad1c765657fa569fec6494322d55 -->
## `test_rescan_unchanged_skips_parse(project: Path)`

Assert that a second scan of unmodified files reports all files unchanged with no new or updated counts.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_scan:test_modified_file_is_updated fingerprint=ae98369fdef8f951260ff15b8226df69ec79e74e92af1b422819213717fa57bc body_fp=b088601a91f406ec1fd918d03649977af42466ffe615b673da094bf61efa13ab -->
## `test_modified_file_is_updated(project: Path)`

Verify that rescanning a modified file increments `files_updated` and refreshes its symbol count.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_scan:test_added_file_is_new fingerprint=7e0c261b141f74fb177b0dc4eff38e8100d011a77827403e7a25a779cc40d891 body_fp=851655b80580a724888d0e5fe21a369b6023e91ce94db91753347223ccc545c8 -->
## `test_added_file_is_new(project: Path)`

Verify that a newly created file is counted as `files_new` on the second scan.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_scan:test_removed_file_is_cleaned_up fingerprint=d62127c8837af97031670cfbbafb155f2f0a19d56a98190d0619abb94fcf2c71 body_fp=f74b69f2c5b4003fb75f5da569ea1b9effd52c1fdb798b1a539af388a332b673 -->
## `test_removed_file_is_cleaned_up(project: Path)`

Verify that deleting a source file causes scan to remove its store entry and symbols.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_scan:test_scan_populates_cross_file_edges fingerprint=f82e9c5f94d7a03c4d2b1590e68eec87aa20acc5241582ae26aa6f4f44e14831 body_fp=72a7ac5aa0fe3a37c8b5116fa0d21c44a56e454252cea45fef24e4af19a3c380 -->
## `test_scan_populates_cross_file_edges(tmp_path: Path)`

Assert that scanning a two-file project creates directed cross-file reference edges with correct kind and inverse view.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_scan:test_scan_populates_intra_file_edges fingerprint=eca28227c8e2fbcb440d94d1d5a09c9e343d54eb354525a51e831915c524cab3 body_fp=f2e1844eae11a01b70552b9eb2f1ee1335046ff3dc91bfd9c581332656aeb66d -->
## `test_scan_populates_intra_file_edges(tmp_path: Path)`

Assert that scanning a file with intra-file calls produces `name_match` edges between symbols in the same module.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_scan:test_edges_rebuilt_when_file_changes fingerprint=14895261e771f79e731ea1c272328b2d18924c0e85ae1ba6eab7068fdb0b96d4 body_fp=69caa66e2e2b7c553d059a653e9bbb3729a5085709a9fe889b73a3b33ce136a8 -->
## `test_edges_rebuilt_when_file_changes(tmp_path: Path)`

Verify that edges from a changed file are removed and rebuilt on rescan.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_scan:test_excluded_file_treated_as_removed fingerprint=3740a9a595051648f04c664560d8cb777c94c244bb6c4ee7f09d3d5ce8e57966 body_fp=decfdaad453344fd063e4b29b098124c4daee4395ea54662542354f79d6b9d26 -->
## `test_excluded_file_treated_as_removed(project: Path)`

Verify that a previously-scanned file newly excluded by scope config is removed from the store.
<!-- trie:end -->