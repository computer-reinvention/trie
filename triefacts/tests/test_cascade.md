---
trie_version: 0.1.0
source: tests/test_cascade.py
file_fingerprint: ca44c8672eec3463c6d59a800f9ec28960007de1c8829653abda78d27fdf63ca
last_synced_at: '2026-05-14T18:23:38Z'
defines:
- kind: function
  qualified_name: tests/test_cascade:project
  lines: 14-33
- kind: function
  qualified_name: tests/test_cascade:test_cascade_returns_seed_when_empty
  lines: 43-49
- kind: function
  qualified_name: tests/test_cascade:test_cascade_includes_changed_files
  lines: 52-55
- kind: function
  qualified_name: tests/test_cascade:test_cascade_depth_one_pulls_direct_callers
  lines: 58-65
- kind: function
  qualified_name: tests/test_cascade:test_cascade_depth_two_walks_two_hops
  lines: 68-72
- kind: function
  qualified_name: tests/test_cascade:test_cascade_depth_zero_only_returns_seed
  lines: 75-79
- kind: function
  qualified_name: tests/test_cascade:test_cascade_hub_threshold_blocks_expansion
  lines: 82-109
- kind: function
  qualified_name: tests/test_cascade:test_cascade_files_sorted
  lines: 112-115
- kind: function
  qualified_name: tests/test_cascade:test_cascade_no_inbound_edges
  lines: 118-131
incoming_refs: 0
outgoing_refs: 12
---
<!-- trie:section symbol=tests/test_cascade:project fingerprint=e70292578e5479e74c4d74918965fb2dbdce2cb94525087be3cb484f27be59e7 body_fp=cbbf6c6991afffb91b7595a4ba68d9c9a3dd8677d4969b0d434506fedb366b4e -->
## `project(tmp_path: Path) -> Path`

Pytest fixture that writes a three-file Python project (`lib.py → mid.py → app.py`) with a `trie.toml` config into `tmp_path`.

- **Returns** `tmp_path` after populating it with config and source files.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_cascade:test_cascade_returns_seed_when_empty fingerprint=83edbf63af4c75b645533bbe88225e2abc7d2c7b541318b8f4aa6c731ceae685 body_fp=ee40a2300a108165509cce2813a20fc91e7220ed1b38b4082ff6b26b492d5b47 -->
## `test_cascade_returns_seed_when_empty(tmp_path: Path)`

Assert that `compute_cascade` returns an empty affected-files list when given no changed files and an empty store.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_cascade:test_cascade_includes_changed_files fingerprint=8c29abbf43fcbb39f847a3479d57d48e688cee2c891c9b675d21843b66e090e6 body_fp=5731feffe31ad2626c484c04a0a31b1b9a86399be64c1f7bc058897aa3012f8c -->
## `test_cascade_includes_changed_files(project: Path)`

Assert that `compute_cascade` includes the changed file itself in `affected_files`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_cascade:test_cascade_depth_one_pulls_direct_callers fingerprint=7c50763a91d00b304c6f46a92582f8b8c9464b52b5990b527229a813438addeb body_fp=3955c7139746b7cd5ca3bebff934e9370b19d2437102539e20b1ea8c61360aaf -->
## `test_cascade_depth_one_pulls_direct_callers(project: Path)`

Assert that `depth=1` pulls direct callers of changed symbols but not transitive callers.

- `project`: fixture providing a 3-file call chain `lib → mid → app`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_cascade:test_cascade_depth_two_walks_two_hops fingerprint=ec77131470c458b4983e5ce0ca40d307389ac12f018ce309467e0adce1464f82 body_fp=492f982695d85345f7b96345b66cd8c657aa4432f0e8ad019f092d3d5dc9d428 -->
## `test_cascade_depth_two_walks_two_hops(project: Path)`

Assert that `compute_cascade` with `depth=2` propagates through two import hops (`lib.py` → `mid.py` → `app.py`).
<!-- trie:end -->

<!-- trie:section symbol=tests/test_cascade:test_cascade_depth_zero_only_returns_seed fingerprint=23c87fe4d6c9029fd8ff1e25e810569bf5aaee9d4ab67e171f58cb698826df2c body_fp=b030e5e53ebdde9a8e8deaf6c48de5e2536c06dfe4f82edd2b049d96fd351dc4 -->
## `test_cascade_depth_zero_only_returns_seed(project: Path)`

Assert that `compute_cascade` with `depth=0` returns only the seed file and no cascaded files.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_cascade:test_cascade_hub_threshold_blocks_expansion fingerprint=4b7b4b4d4b113cccd4f55e335f7b0a0a368d62022dd0eefb7781e83ea2e4c1ae body_fp=0402c30b8d40525bc96aefbe5fa5979d36fe6eac33e7686bb76180055ea0b226 -->
## `test_cascade_hub_threshold_blocks_expansion(tmp_path: Path)`

Verify that `hub_threshold` controls whether high-fanout symbols expand their callers during cascade computation.

- `hub_threshold=100`: permissive, all 5 callers appear in results.
- `hub_threshold=2`: strict, seed file present but no callers pulled in.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_cascade:test_cascade_files_sorted fingerprint=9842c9750bc5541c3207ef6196eeb44500036c28eeac565d7209d94173ee606e body_fp=4f0c7325fa599f487a38c8533ce4880ac6b4f5d255a4941333fd9923f9ff31a1 -->
## `test_cascade_files_sorted(project: Path)`

Assert that `affected_files` in the cascade result is sorted in ascending order.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_cascade:test_cascade_no_inbound_edges fingerprint=edfc538a994df5836a052a637058b734ec01c281eaa3d82ea4183cb4903d8607 body_fp=f4b3e016a5f26b71c42eef93dd0b7f7835aa53355387456e3f7401fdc2ffa7fd -->
## `test_cascade_no_inbound_edges(tmp_path: Path)`

Assert that a file with no callers produces only itself in the cascade result with an empty `cascaded_from_change` set.
<!-- trie:end -->