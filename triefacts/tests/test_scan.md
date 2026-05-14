---
trie_version: 0.1.0
source: tests/test_scan.py
file_fingerprint: d0035bcdb5ccc4b3f9c4748e45283ac972f74f2285893cacf984dd70abeac8ce
last_synced_at: '2026-05-14T18:29:03Z'
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
<!-- trie:section symbol=tests/test_scan:project fingerprint=3244bb3322e015de8418a9846af3f814b535348d60a14069119899f32f43ad29 body_fp=304b44016cfeb8d1e272034e05a5802375f59451e1a54a4911ca102a1ad25af2 source_ref=ed904186acd6a05bbb10153e0e7543578502266f -->
## `project(tmp_path: Path) -> Path`

Pytest fixture that creates a temporary project root with `trie.toml` and two stub Python source files.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_scan:test_first_scan_marks_all_new fingerprint=20449e998a56b18a554998b7c2da16699db555be4d445864db75f0812640ad16 body_fp=869b92d561259d01151ac6ddccdaf277bb73a8a5e2441566a05cb603f37b63d4 source_ref=ed904186acd6a05bbb10153e0e7543578502266f -->
## `test_first_scan_marks_all_new(project: Path)`

Assert that a first-time scan marks all discovered files as new and persists their symbols.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_scan:test_rescan_unchanged_skips_parse fingerprint=be64ec917dd52a447d35da09df1f2c8ef6e5e811f0053b07e63ced56a9442f59 body_fp=3b776787df9b3987042691dafc1f9dc69347ad1c765657fa569fec6494322d55 source_ref=ed904186acd6a05bbb10153e0e7543578502266f -->
## `test_rescan_unchanged_skips_parse(project: Path)`

Assert that a second scan of unmodified files reports all files unchanged with no new or updated counts.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_scan:test_modified_file_is_updated fingerprint=ae98369fdef8f951260ff15b8226df69ec79e74e92af1b422819213717fa57bc body_fp=dd0bba574493cadc3cbdba779ce9d87310ec9d6caa72964c9e81c95d24740950 source_ref=ed904186acd6a05bbb10153e0e7543578502266f -->
## `test_modified_file_is_updated(project: Path)`

Verify that re-scanning a modified file increments `files_updated` and refreshes its symbol count.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_scan:test_added_file_is_new fingerprint=7e0c261b141f74fb177b0dc4eff38e8100d011a77827403e7a25a779cc40d891 body_fp=6dcf625b704c578dac7b15cfbbd93bb487c8f8bc6757d2bcfd655a133ee5eaab source_ref=ed904186acd6a05bbb10153e0e7543578502266f -->
## `test_added_file_is_new(project: Path)`

Verify that a newly created file is counted as `files_new` on the subsequent scan.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_scan:test_removed_file_is_cleaned_up fingerprint=d62127c8837af97031670cfbbafb155f2f0a19d56a98190d0619abb94fcf2c71 body_fp=7abff206b40e875d97abe5b5642f11154b9e2346b252f215ab2c359bee84e486 source_ref=ed904186acd6a05bbb10153e0e7543578502266f -->
## `test_removed_file_is_cleaned_up(project: Path)`

Verify that deleting a source file removes it and its symbols from the store on rescan.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_scan:test_scan_populates_cross_file_edges fingerprint=ee21224ba5291434c51bb572f09d348bfe9ed4a87fb6de79b25efcccf97966e1 body_fp=acaf4b8bc6056696d453e7318d1ee13e6f1b628837e35dc04aa703e8b366c8c3 source_ref=ed904186acd6a05bbb10153e0e7543578502266f -->
## `test_scan_populates_cross_file_edges(tmp_path: Path)`

Verify that scanning two files creates a cross-file reference edge from `app:run` to `lib:helper` in both directions.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_scan:test_scan_populates_intra_file_edges fingerprint=30a16a88497eca0d4b18b529ff5153ee08a02cc0948460e966b6e97ce6daa1d5 body_fp=85c2507b98fd3606848f19767d825c193b5aeeb29c006c7c3e981a62bed2d1d2 source_ref=ed904186acd6a05bbb10153e0e7543578502266f -->
## `test_scan_populates_intra_file_edges(tmp_path: Path)`

Verify that `scan_project` records call edges between symbols within the same file.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_scan:test_edges_rebuilt_when_file_changes fingerprint=14895261e771f79e731ea1c272328b2d18924c0e85ae1ba6eab7068fdb0b96d4 body_fp=9e6f4b2d720fca430666b61dc4d49913d85a62c362e03c09bb213530035d9111 source_ref=ed904186acd6a05bbb10153e0e7543578502266f -->
## `test_edges_rebuilt_when_file_changes(tmp_path: Path)`

Verify that stale cross-file edges are removed and replaced when a source file is modified on rescan.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_scan:test_excluded_file_treated_as_removed fingerprint=3740a9a595051648f04c664560d8cb777c94c244bb6c4ee7f09d3d5ce8e57966 body_fp=fc643d2d5111c0055dc899a966105d2a96c8c353815b4ad0140eac4cb175ef7f source_ref=ed904186acd6a05bbb10153e0e7543578502266f -->
## `test_excluded_file_treated_as_removed(project: Path)`

Verify that tightening the scope exclusion removes a previously-scanned file from the store.
<!-- trie:end -->