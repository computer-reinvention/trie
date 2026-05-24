---
trie_version: 0.1.2
source: tests/test_scan.py
file_fingerprint: 778ee23d148c0a3f4e1ef2b0394a351d2fc6e229982d25a1898266f040943a27
last_synced_at: '2026-05-23T23:52:05Z'
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
<!-- trie:section symbol=tests/test_scan:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=595842674f6d16ec84f9c33ba3308717b2514b6618ecd26a6f319fa549d6c63d source_ref=481caf41ed6eb1f944c4b27db6707de091ad64c3 -->
## `tests/test_scan`

Integration tests for `scan_project` covering first scan, rescan, file mutations, edge population, and scope exclusion.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_scan:project fingerprint=3244bb3322e015de8418a9846af3f814b535348d60a14069119899f32f43ad29 body_fp=870e7c1f0b0c004cbb75a4a8469435905e6192fc62011131518aa31adc27afb3 source_ref=481caf41ed6eb1f944c4b27db6707de091ad64c3 -->
## `project(tmp_path: Path) -> Path`

Pytest fixture providing a temporary project root with `trie.toml` and `src/alpha.py` (`alpha`), `src/beta.py` (`beta_a`, `beta_b`).
<!-- trie:end -->
<!-- trie:section symbol=tests/test_scan:_scan fingerprint=02aa825501406c55a6abf16d9c5c7e4028d2ee0794e5c14f08ba2e960e706a01 body_fp=e5d2c7bac78744ead4fe4e4ad91e136e4c1a4c11d636eeb0cf8554f4a9f508a2 source_ref=481caf41ed6eb1f944c4b27db6707de091ad64c3 -->
## `_scan(project: Path) -> tuple[Store, object]`

Load config, open the graph store, and run `scan_project` against a test project root.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_scan:test_first_scan_marks_all_new fingerprint=20449e998a56b18a554998b7c2da16699db555be4d445864db75f0812640ad16 body_fp=971d67ddab0ce109f9144f785289e1fe7de5e99e0bd90008e9ada26b9ce1bf24 source_ref=481caf41ed6eb1f944c4b27db6707de091ad64c3 -->
## `test_first_scan_marks_all_new(project: Path)`

Verify that an initial scan classifies all discovered files as new and persists their symbols and fingerprints.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_scan:test_rescan_unchanged_skips_parse fingerprint=be64ec917dd52a447d35da09df1f2c8ef6e5e811f0053b07e63ced56a9442f59 body_fp=ae411260412eb4c8472d8a7c8966b791d4728c8bb62d2a8ab5103fd3075a08dd source_ref=481caf41ed6eb1f944c4b27db6707de091ad64c3 -->
## `test_rescan_unchanged_skips_parse(project: Path)`

Assert that a second scan of an unmodified project reports all files unchanged and no new or updated files.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_scan:test_modified_file_is_updated fingerprint=ae98369fdef8f951260ff15b8226df69ec79e74e92af1b422819213717fa57bc body_fp=52f2bd4d1771c3aae3f2a5ea03a4cfee28d21b13a93d57e8eccf643683315cd4 source_ref=481caf41ed6eb1f944c4b27db6707de091ad64c3 -->
## `test_modified_file_is_updated(project: Path)`

Verify that rescanning after modifying a file reports it as updated and repopulates its symbols.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_scan:test_added_file_is_new fingerprint=7e0c261b141f74fb177b0dc4eff38e8100d011a77827403e7a25a779cc40d891 body_fp=1786d4dfc1d70a863a005dc6346a14d4d8e242ad0084bd9e5e226aac964f4424 source_ref=481caf41ed6eb1f944c4b27db6707de091ad64c3 -->
## `test_added_file_is_new(project: Path)`

Verify that a newly created file is counted as `files_new` on the next scan.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_scan:test_removed_file_is_cleaned_up fingerprint=d62127c8837af97031670cfbbafb155f2f0a19d56a98190d0619abb94fcf2c71 body_fp=8fba11a03f4753ce970c867d415a426fea186e4d9e69fb80b8f87e1774866e29 source_ref=481caf41ed6eb1f944c4b27db6707de091ad64c3 -->
## `test_removed_file_is_cleaned_up(project: Path)`

Assert that deleting a file causes `scan_project` to remove it and its symbols from the store.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_scan:test_scan_populates_cross_file_edges fingerprint=ee21224ba5291434c51bb572f09d348bfe9ed4a87fb6de79b25efcccf97966e1 body_fp=754f874102800a3a669625e93bf132efd04c7de98cfb0834acd044eb8a30da7d source_ref=481caf41ed6eb1f944c4b27db6707de091ad64c3 -->
## `test_scan_populates_cross_file_edges(tmp_path: Path)`

Assert that `scan_project` records outbound and inbound reference edges between symbols in different files.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_scan:test_scan_populates_intra_file_edges fingerprint=30a16a88497eca0d4b18b529ff5153ee08a02cc0948460e966b6e97ce6daa1d5 body_fp=df09cb0df7339ea318b4b9e3531e5d2d8035079f97561d413e1eecad8d99add5 source_ref=481caf41ed6eb1f944c4b27db6707de091ad64c3 -->
## `test_scan_populates_intra_file_edges(tmp_path: Path)`

Assert that `scan_project` records call edges between symbols within the same file.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_scan:test_edges_rebuilt_when_file_changes fingerprint=14895261e771f79e731ea1c272328b2d18924c0e85ae1ba6eab7068fdb0b96d4 body_fp=215bcf61c077363f88e8e19fa051db6c544c7359f6168bd00443203be94788eb source_ref=481caf41ed6eb1f944c4b27db6707de091ad64c3 -->
## `test_edges_rebuilt_when_file_changes(tmp_path: Path)`

Assert that cross-file edges are removed from the store when a modified file drops a reference.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_scan:test_excluded_file_treated_as_removed fingerprint=3740a9a595051648f04c664560d8cb777c94c244bb6c4ee7f09d3d5ce8e57966 body_fp=5f88dcd1e0c970d234669a3b54f30d984148ef755a739a1053f16de9f77286ef source_ref=481caf41ed6eb1f944c4b27db6707de091ad64c3 -->
## `test_excluded_file_treated_as_removed(project: Path)`

Verify that a file newly excluded by scope config is reported and cleaned up as removed.
<!-- trie:end -->