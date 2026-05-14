---
trie_version: 0.1.0
source: tests/test_scan.py
file_fingerprint: d0035bcdb5ccc4b3f9c4748e45283ac972f74f2285893cacf984dd70abeac8ce
last_synced_at: '2026-05-14T17:25:13Z'
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
<!-- trie:section symbol=tests/test_scan:project fingerprint=3244bb3322e015de8418a9846af3f814b535348d60a14069119899f32f43ad29 body_fp=defb1d3dc0fee31cfdd5ea5ee19e3feb76937e5e336cad2cc96e58022c0f865f -->
## `project(tmp_path: Path) -> Path`

Pytest fixture that creates a minimal trie project with `trie.toml` and two stub Python source files.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_scan:test_first_scan_marks_all_new fingerprint=20449e998a56b18a554998b7c2da16699db555be4d445864db75f0812640ad16 body_fp=49b17be66a29852c205e1fdbbe3f0d2f7fd284b200daa65f20eca56eda9d51bd -->
## `test_first_scan_marks_all_new(project: Path)`

Assert that scanning a fresh project marks all files and symbols as new with correct counts.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_scan:test_rescan_unchanged_skips_parse fingerprint=be64ec917dd52a447d35da09df1f2c8ef6e5e811f0053b07e63ced56a9442f59 body_fp=3d0e3e5c6f6f97f500be6b551060f59bcbb2aa22bf0e6c08c1a89427ec3aa4f6 -->
## `test_rescan_unchanged_skips_parse(project: Path)`

Assert that a second scan of an unmodified project reports all files unchanged with zero new or updated counts.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_scan:test_modified_file_is_updated fingerprint=ae98369fdef8f951260ff15b8226df69ec79e74e92af1b422819213717fa57bc body_fp=d380006fec23f8292a0423d2f65269238a9deddf7b6ff7c63f43f070c09e1e45 -->
## `test_modified_file_is_updated(project: Path)`

Verify that re-scanning after modifying a file reports it as updated and reflects new symbol count.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_scan:test_added_file_is_new fingerprint=7e0c261b141f74fb177b0dc4eff38e8100d011a77827403e7a25a779cc40d891 body_fp=5f467a70fc710bc9894aa00218783668988495e8870efda70eef936e044bede5 -->
## `test_added_file_is_new(project: Path)`

Verify that a newly created source file is counted as `files_new` on the subsequent scan.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_scan:test_removed_file_is_cleaned_up fingerprint=d62127c8837af97031670cfbbafb155f2f0a19d56a98190d0619abb94fcf2c71 body_fp=7abff206b40e875d97abe5b5642f11154b9e2346b252f215ab2c359bee84e486 -->
## `test_removed_file_is_cleaned_up(project: Path)`

Verify that deleting a source file removes it and its symbols from the store on rescan.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_scan:test_scan_populates_cross_file_edges fingerprint=ee21224ba5291434c51bb572f09d348bfe9ed4a87fb6de79b25efcccf97966e1 body_fp=acaf4b8bc6056696d453e7318d1ee13e6f1b628837e35dc04aa703e8b366c8c3 -->
## `test_scan_populates_cross_file_edges(tmp_path: Path)`

Verify that scanning two files creates a cross-file reference edge from `app:run` to `lib:helper` in both directions.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_scan:test_scan_populates_intra_file_edges fingerprint=30a16a88497eca0d4b18b529ff5153ee08a02cc0948460e966b6e97ce6daa1d5 body_fp=85c2507b98fd3606848f19767d825c193b5aeeb29c006c7c3e981a62bed2d1d2 -->
## `test_scan_populates_intra_file_edges(tmp_path: Path)`

Verify that `scan_project` records call edges between symbols within the same file.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_scan:test_edges_rebuilt_when_file_changes fingerprint=14895261e771f79e731ea1c272328b2d18924c0e85ae1ba6eab7068fdb0b96d4 body_fp=1e8e3391b600c6088511c12b5535e11133e221b37181ef0827bc11948b245a37 -->
## `test_edges_rebuilt_when_file_changes(tmp_path: Path)`

Verify that stale cross-file edges are removed and replaced when a source file is rescanned after modification.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_scan:test_excluded_file_treated_as_removed fingerprint=3740a9a595051648f04c664560d8cb777c94c244bb6c4ee7f09d3d5ce8e57966 body_fp=5588ff1001d329c8a64ccceaaf4164b9103b5835aa22c1d2044b4c894d823ce1 -->
## `test_excluded_file_treated_as_removed(project: Path)`

Verify that a file excluded from scope on rescan is removed from the store.
<!-- trie:end -->