---
trie_version: 0.1.0
source: tests/test_cascade.py
file_fingerprint: ca44c8672eec3463c6d59a800f9ec28960007de1c8829653abda78d27fdf63ca
last_synced_at: '2026-05-12T18:29:45Z'
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
<!-- trie:section symbol=tests/test_cascade:project fingerprint=e70292578e5479e74c4d74918965fb2dbdce2cb94525087be3cb484f27be59e7 body_fp=68a5614dda3538950a528988c46ddc8a83628670bf6964182027879083febc9b -->
## `project(tmp_path: Path) -> Path`

Pytest fixture that creates a minimal three-file Python project (`lib.py → mid.py → app.py`) with a `trie.toml` config in `tmp_path`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_cascade:test_cascade_returns_seed_when_empty fingerprint=83edbf63af4c75b645533bbe88225e2abc7d2c7b541318b8f4aa6c731ceae685 body_fp=27fb325be0146f25e38370417ebea50be7307685af2b7675ab8600ba8613ba7e -->
## `test_cascade_returns_seed_when_empty(tmp_path: Path)`

Assert that `compute_cascade` returns an empty `affected_files` list when given no changed files and an empty store.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_cascade:test_cascade_includes_changed_files fingerprint=8c29abbf43fcbb39f847a3479d57d48e688cee2c891c9b675d21843b66e090e6 body_fp=8593390e564a32bdb9bf70a4dc6d31e9850733fc626a942b2b53d4a01a530f91 -->
## `test_cascade_includes_changed_files(project: Path)`

Assert that `compute_cascade` includes the directly changed file in `affected_files`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_cascade:test_cascade_depth_one_pulls_direct_callers fingerprint=7c50763a91d00b304c6f46a92582f8b8c9464b52b5990b527229a813438addeb body_fp=6a53dcbff1791d4984da6bd7581be0b52bd9c9453d4b246e23ecf8183620d98d -->
## `test_cascade_depth_one_pulls_direct_callers(project: Path)`

Assert that depth-1 cascade from `lib.py` includes `mid.py` but excludes `app.py`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_cascade:test_cascade_depth_two_walks_two_hops fingerprint=ec77131470c458b4983e5ce0ca40d307389ac12f018ce309467e0adce1464f82 body_fp=f70f6345b1f61c3f05b29d39d40dea03397cbdb0010f305f151fa62043532a89 -->
## `test_cascade_depth_two_walks_two_hops(project: Path)`

Assert that `compute_cascade` with `depth=2` propagates changes across two hops (`lib.py` → `mid.py` → `app.py`).
<!-- trie:end -->

<!-- trie:section symbol=tests/test_cascade:test_cascade_depth_zero_only_returns_seed fingerprint=23c87fe4d6c9029fd8ff1e25e810569bf5aaee9d4ab67e171f58cb698826df2c body_fp=c150c24d55e9b8b5e29e6989750c39b6d4f857fc63fc4dece6e936e180d3ccf3 -->
## `test_cascade_depth_zero_only_returns_seed(project: Path)`

Assert that `depth=0` returns only the seed file with no cascaded files.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_cascade:test_cascade_hub_threshold_blocks_expansion fingerprint=4b7b4b4d4b113cccd4f55e335f7b0a0a368d62022dd0eefb7781e83ea2e4c1ae body_fp=2e929aba7facf01699bc9561b3cdc8f30fedd175b96745ac46b26806fc7d984a -->
## `test_cascade_hub_threshold_blocks_expansion(tmp_path: Path)`

Verify that a hub symbol with many callers suppresses cascade expansion when `hub_threshold` is below the caller count.

- `hub_threshold=100`: all 5 callers appear in `affected_files`.
- `hub_threshold=2`: no callers are pulled in; only the seed file remains.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_cascade:test_cascade_files_sorted fingerprint=9842c9750bc5541c3207ef6196eeb44500036c28eeac565d7209d94173ee606e body_fp=25554aa9b9d599c08144490ce9e8c46d24a40ad8fa4e95fe5e19c369842941f8 -->
## `test_cascade_files_sorted(project: Path)`

Assert that `affected_files` in the cascade result is returned in sorted order.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_cascade:test_cascade_no_inbound_edges fingerprint=edfc538a994df5836a052a637058b734ec01c281eaa3d82ea4183cb4903d8607 body_fp=c24b72b811f5348cdac7aeebe5ed7580f7e5fa2ee112b9abe56419a0d8c5ebb2 -->
## `test_cascade_no_inbound_edges(tmp_path: Path)`

Assert that a file with no callers produces only itself in cascade results with an empty `cascaded_from_change`.
<!-- trie:end -->