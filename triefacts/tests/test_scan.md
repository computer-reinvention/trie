---
trie_version: 0.3.0
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
  signature: 'def project(tmp_path: Path) -> Path'
- kind: function
  qualified_name: tests/test_scan:_scan
  lines: 31-35
  signature: 'def _scan(project: Path) -> tuple[Store, object]'
- kind: function
  qualified_name: tests/test_scan:test_first_scan_marks_all_new
  lines: 38-50
  signature: 'def test_first_scan_marks_all_new(project: Path)'
- kind: function
  qualified_name: tests/test_scan:test_rescan_unchanged_skips_parse
  lines: 53-63
  signature: 'def test_rescan_unchanged_skips_parse(project: Path)'
- kind: function
  qualified_name: tests/test_scan:test_modified_file_is_updated
  lines: 66-81
  signature: 'def test_modified_file_is_updated(project: Path)'
- kind: function
  qualified_name: tests/test_scan:test_added_file_is_new
  lines: 84-96
  signature: 'def test_added_file_is_new(project: Path)'
- kind: function
  qualified_name: tests/test_scan:test_removed_file_is_cleaned_up
  lines: 99-112
  signature: 'def test_removed_file_is_cleaned_up(project: Path)'
- kind: function
  qualified_name: tests/test_scan:test_scan_populates_cross_file_edges
  lines: 115-139
  signature: 'def test_scan_populates_cross_file_edges(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_scan:test_scan_populates_intra_file_edges
  lines: 142-160
  signature: 'def test_scan_populates_intra_file_edges(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_scan:test_edges_rebuilt_when_file_changes
  lines: 163-190
  signature: 'def test_edges_rebuilt_when_file_changes(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_scan:test_excluded_file_treated_as_removed
  lines: 193-212
  signature: 'def test_excluded_file_treated_as_removed(project: Path)'
incoming_refs: 0
outgoing_refs: 4
---
<!-- trie:section symbol=tests/test_scan:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=f146cfea969e95e5c9972d26f0e0007d1246282ba4b4c013c5cfc08afc4d5964 source_ref=481caf41ed6eb1f944c4b27db6707de091ad64c3 role=test-infrastructure -->
Tests for project scanning functionality that discovers, parses, and tracks Python source files and their symbols.

- Contains pytest fixtures and test functions covering file discovery, change detection, and symbol relationship tracking
- Tests incremental scanning behavior with new, modified, and removed files
- Verifies cross-file and intra-file reference edge detection and maintenance
<!-- trie:end -->
<!-- trie:section symbol=tests/test_scan:project fingerprint=3244bb3322e015de8418a9846af3f814b535348d60a14069119899f32f43ad29 body_fp=bed2eaa280594170285791b14d05d8032fd2f541b56ffbb326fa45a439638b6a source_ref=481caf41ed6eb1f944c4b27db6707de091ad64c3 role=test-infrastructure -->
## `def project(tmp_path: Path) -> Path`

Creates a temporary project directory with trie configuration and sample Python files for testing.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_scan:_scan fingerprint=02aa825501406c55a6abf16d9c5c7e4028d2ee0794e5c14f08ba2e960e706a01 body_fp=67dfbb4642e7e18b7f6292b8dd153d4f15ad3c1388a3ade8c3fdca8f294240d6 source_ref=481caf41ed6eb1f944c4b27db6707de091ad64c3 role=test-infrastructure -->
## `def _scan(project: Path) -> tuple[Store, object]`

Helper function that loads configuration, creates a store, and scans the given project.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_scan:test_first_scan_marks_all_new fingerprint=20449e998a56b18a554998b7c2da16699db555be4d445864db75f0812640ad16 body_fp=094b11b6db52fc7edb7651063db1e4ecbcae731a3007bfc520db966356e098cf source_ref=481caf41ed6eb1f944c4b27db6707de091ad64c3 role=test-infrastructure -->
## `def test_first_scan_marks_all_new(project: Path)`

Tests that scanning a fresh project marks all discovered files and symbols as new.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_scan:test_rescan_unchanged_skips_parse fingerprint=be64ec917dd52a447d35da09df1f2c8ef6e5e811f0053b07e63ced56a9442f59 body_fp=b0a1165757c5206e70ac96b1bb2b3f31cbb114d5a2eafbfa7395748c5abefa46 source_ref=481caf41ed6eb1f944c4b27db6707de091ad64c3 role=change-detection -->
## `def test_rescan_unchanged_skips_parse(project: Path)`

Verifies that rescanning unchanged files detects no new or updated files and preserves symbol count.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_scan:test_modified_file_is_updated fingerprint=ae98369fdef8f951260ff15b8226df69ec79e74e92af1b422819213717fa57bc body_fp=e032570c6b5d37944b829454152ef0cd5d579f194949fe7775ee7985eb21a9c6 source_ref=481caf41ed6eb1f944c4b27db6707de091ad64c3 role=source-parsing -->
## `def test_modified_file_is_updated(project: Path)`

Tests that scan_project correctly identifies and updates a modified file, detecting new symbols added to the file.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_scan:test_added_file_is_new fingerprint=7e0c261b141f74fb177b0dc4eff38e8100d011a77827403e7a25a779cc40d891 body_fp=60a1c52b60d20ea102a0acca1fcc0dfb30e503ce7a9b93abce9324077863b64d source_ref=481caf41ed6eb1f944c4b27db6707de091ad64c3 role=test-infrastructure -->
## `def test_added_file_is_new(project: Path)`

Tests that adding a new file to the project is correctly detected as a new file in subsequent scans.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_scan:test_removed_file_is_cleaned_up fingerprint=d62127c8837af97031670cfbbafb155f2f0a19d56a98190d0619abb94fcf2c71 body_fp=0204bab55a4b2b36b7094a92932dfeafb9a3cff7be2fc99433421dfb165c6da8 source_ref=481caf41ed6eb1f944c4b27db6707de091ad64c3 role=change-detection -->
## `def test_removed_file_is_cleaned_up(project: Path)`

Verifies that scan_project correctly removes deleted files from the store and updates counters.

- Deletes a file between scans and asserts files_removed count and store cleanup
<!-- trie:end -->
<!-- trie:section symbol=tests/test_scan:test_scan_populates_cross_file_edges fingerprint=ee21224ba5291434c51bb572f09d348bfe9ed4a87fb6de79b25efcccf97966e1 body_fp=f0447c72bc7517c6bdfa4bf9ca5ee14b1231355d919595d9d2fb48a8c42cec20 source_ref=481caf41ed6eb1f944c4b27db6707de091ad64c3 role=test-infrastructure -->
## `def test_scan_populates_cross_file_edges(tmp_path: Path)`

Verifies that scanning creates cross-file reference edges between symbols in different files.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_scan:test_scan_populates_intra_file_edges fingerprint=30a16a88497eca0d4b18b529ff5153ee08a02cc0948460e966b6e97ce6daa1d5 body_fp=fd77fa2fd2cca5966eecfa07343c9e347db860f9a324479500552dc2e774940a source_ref=481caf41ed6eb1f944c4b27db6707de091ad64c3 role=test-infrastructure -->
## `def test_scan_populates_intra_file_edges(tmp_path: Path)`

Verifies that scanning detects function calls within the same file and stores reference edges.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_scan:test_edges_rebuilt_when_file_changes fingerprint=14895261e771f79e731ea1c272328b2d18924c0e85ae1ba6eab7068fdb0b96d4 body_fp=5ee4e6ea960e34e47f7d99e6251bebfc23298c3c615d75a0090c31a31551ace7 source_ref=481caf41ed6eb1f944c4b27db6707de091ad64c3 role=test-infrastructure -->
## `def test_edges_rebuilt_when_file_changes(tmp_path: Path)`

Verifies that dependency edges are correctly updated when a file's imports or references change.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_scan:test_excluded_file_treated_as_removed fingerprint=3740a9a595051648f04c664560d8cb777c94c244bb6c4ee7f09d3d5ce8e57966 body_fp=0f9f86a05c185b1254d46e3f4588e5bc9fedbf25ddf042ee6173a7a26c6a250b source_ref=481caf41ed6eb1f944c4b27db6707de091ad64c3 role=test-infrastructure -->
## `def test_excluded_file_treated_as_removed(project: Path)`

Tests that files excluded by updated configuration are treated as removed from the project.

- Performs initial scan, then modifies config to exclude src/alpha.py via exclude pattern
- Verifies scan result shows one removed file and store no longer contains the excluded file
<!-- trie:end -->