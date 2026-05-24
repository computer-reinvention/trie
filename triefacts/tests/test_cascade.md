---
trie_version: 0.1.2
source: tests/test_cascade.py
file_fingerprint: ce816f67f6be54e4afae60d1aa1e6ec537a6d72ad49e6d60f298f8905ef63b92
last_synced_at: '2026-05-23T23:52:39Z'
defines:
- kind: module
  qualified_name: tests/test_cascade:__module__
  lines: 1-132
- kind: function
  qualified_name: tests/test_cascade:project
  lines: 14-33
- kind: function
  qualified_name: tests/test_cascade:_store
  lines: 36-40
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
<!-- trie:section symbol=tests/test_cascade:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=50f1b49087322b41ab4b6d7922df1f193e2bd1a8a84a8d852de3dd11d838bbbf source_ref=6da7e7637a65c81892a7c3b8c2328eb8a6d7014d -->
## `tests/test_cascade`

Test suite for `compute_cascade`, covering depth traversal, hub-threshold blocking, seed inclusion, and result ordering.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cascade:project fingerprint=e70292578e5479e74c4d74918965fb2dbdce2cb94525087be3cb484f27be59e7 body_fp=cdc235a66282879220444b3f38cc78bbf116ec3a81a5a34a1ba37d6f79c0967a source_ref=6da7e7637a65c81892a7c3b8c2328eb8a6d7014d -->
## `project(tmp_path: Path) -> Path`

Pytest fixture that creates a three-file call-chain project (`lib.py → mid.py → app.py`) with a `trie.toml` config in `tmp_path`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cascade:_store fingerprint=baaa0b7b2e6d36d567fcba260f5d9d727395f0f6c6a4aec077e0fc3cb066367e body_fp=9e6e47776ea16dc70d091e6f4d8c11a1848373f6c1c31a749081efd839848576 source_ref=6da7e7637a65c81892a7c3b8c2328eb8a6d7014d -->
## `_store(project: Path) -> Store`

Load config, initialise a `Store` at `<project>/.trie/graph.db`, scan the project into it, and return the store.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cascade:test_cascade_returns_seed_when_empty fingerprint=83edbf63af4c75b645533bbe88225e2abc7d2c7b541318b8f4aa6c731ceae685 body_fp=7e1a165a2b9b0748e323af29f1977fc1dcaf83d5f5fd7a9d0fea53d44f2363f9 source_ref=6da7e7637a65c81892a7c3b8c2328eb8a6d7014d -->
## `test_cascade_returns_seed_when_empty(tmp_path: Path)`

Assert that `compute_cascade` returns an empty affected-files list when given no changed files.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cascade:test_cascade_includes_changed_files fingerprint=8c29abbf43fcbb39f847a3479d57d48e688cee2c891c9b675d21843b66e090e6 body_fp=5731feffe31ad2626c484c04a0a31b1b9a86399be64c1f7bc058897aa3012f8c source_ref=6da7e7637a65c81892a7c3b8c2328eb8a6d7014d -->
## `test_cascade_includes_changed_files(project: Path)`

Assert that `compute_cascade` includes the changed file itself in `affected_files`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cascade:test_cascade_depth_one_pulls_direct_callers fingerprint=7c50763a91d00b304c6f46a92582f8b8c9464b52b5990b527229a813438addeb body_fp=845e40aefe7e9adb78e35cdd3599b0d031e4347b6f173eebfe6348914f0d5680 source_ref=6da7e7637a65c81892a7c3b8c2328eb8a6d7014d -->
## `test_cascade_depth_one_pulls_direct_callers(project: Path)`

Assert that `compute_cascade` with `depth=1` includes direct callers but not transitive callers.

- `mid.py` expected in both `affected_files` and `cascaded_from_change`
- `app.py` must be absent — it calls `mid.compute`, not `lib.helper` directly
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cascade:test_cascade_depth_two_walks_two_hops fingerprint=ec77131470c458b4983e5ce0ca40d307389ac12f018ce309467e0adce1464f82 body_fp=b5053a8a3c3892470396c4d4cb09c9c13263b73bcf7557af00b4524d0bff69bd source_ref=6da7e7637a65c81892a7c3b8c2328eb8a6d7014d -->
## `test_cascade_depth_two_walks_two_hops(project: Path)`

Assert that `compute_cascade` with `depth=2` propagates two hops: `lib.py` → `mid.py` → `app.py`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cascade:test_cascade_depth_zero_only_returns_seed fingerprint=23c87fe4d6c9029fd8ff1e25e810569bf5aaee9d4ab67e171f58cb698826df2c body_fp=b030e5e53ebdde9a8e8deaf6c48de5e2536c06dfe4f82edd2b049d96fd351dc4 source_ref=6da7e7637a65c81892a7c3b8c2328eb8a6d7014d -->
## `test_cascade_depth_zero_only_returns_seed(project: Path)`

Assert that `compute_cascade` with `depth=0` returns only the seed file and no cascaded files.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cascade:test_cascade_hub_threshold_blocks_expansion fingerprint=4b7b4b4d4b113cccd4f55e335f7b0a0a368d62022dd0eefb7781e83ea2e4c1ae body_fp=b6de950c8de1b2b224ba9e5c0a502027a217c11ec07ea79ead7bb015db5528c3 source_ref=6da7e7637a65c81892a7c3b8c2328eb8a6d7014d -->
## `test_cascade_hub_threshold_blocks_expansion(tmp_path: Path)`

Verify that a high `hub_threshold` expands hub symbols while a low threshold suppresses caller propagation.

- `hub_threshold=100`: all 5 callers appear in `affected_files`
- `hub_threshold=2`: seed file retained but no callers pulled in
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cascade:test_cascade_files_sorted fingerprint=9842c9750bc5541c3207ef6196eeb44500036c28eeac565d7209d94173ee606e body_fp=e8d7ff54f1e281412276915a8bf8aaae0037f5fae17a9911a590b438bc56b9a8 source_ref=6da7e7637a65c81892a7c3b8c2328eb8a6d7014d -->
## `test_cascade_files_sorted(project: Path)`

Assert that `compute_cascade` returns `affected_files` in sorted order.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cascade:test_cascade_no_inbound_edges fingerprint=edfc538a994df5836a052a637058b734ec01c281eaa3d82ea4183cb4903d8607 body_fp=f77ce243a108a9a470b39d588a80d47d59e4f9536fd461250802667f08ba6e5b source_ref=6da7e7637a65c81892a7c3b8c2328eb8a6d7014d -->
## `test_cascade_no_inbound_edges(tmp_path: Path)`

Assert that `compute_cascade` returns only the seed file when the changed symbol has no callers.
<!-- trie:end -->