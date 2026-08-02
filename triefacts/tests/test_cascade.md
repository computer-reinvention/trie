---
trie_version: 0.3.0
source: tests/test_cascade.py
file_fingerprint: ce816f67f6be54e4afae60d1aa1e6ec537a6d72ad49e6d60f298f8905ef63b92
last_synced_at: '2026-06-06T13:14:48Z'
defines:
- kind: module
  qualified_name: tests/test_cascade:__module__
  lines: 1-132
- kind: function
  qualified_name: tests/test_cascade:project
  lines: 14-33
  signature: 'def project(tmp_path: Path) -> Path'
- kind: function
  qualified_name: tests/test_cascade:_store
  lines: 36-40
  signature: 'def _store(project: Path) -> Store'
- kind: function
  qualified_name: tests/test_cascade:test_cascade_returns_seed_when_empty
  lines: 43-49
  signature: 'def test_cascade_returns_seed_when_empty(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_cascade:test_cascade_includes_changed_files
  lines: 52-55
  signature: 'def test_cascade_includes_changed_files(project: Path)'
- kind: function
  qualified_name: tests/test_cascade:test_cascade_depth_one_pulls_direct_callers
  lines: 58-65
  signature: 'def test_cascade_depth_one_pulls_direct_callers(project: Path)'
- kind: function
  qualified_name: tests/test_cascade:test_cascade_depth_two_walks_two_hops
  lines: 68-72
  signature: 'def test_cascade_depth_two_walks_two_hops(project: Path)'
- kind: function
  qualified_name: tests/test_cascade:test_cascade_depth_zero_only_returns_seed
  lines: 75-79
  signature: 'def test_cascade_depth_zero_only_returns_seed(project: Path)'
- kind: function
  qualified_name: tests/test_cascade:test_cascade_hub_threshold_blocks_expansion
  lines: 82-109
  signature: 'def test_cascade_hub_threshold_blocks_expansion(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_cascade:test_cascade_files_sorted
  lines: 112-115
  signature: 'def test_cascade_files_sorted(project: Path)'
- kind: function
  qualified_name: tests/test_cascade:test_cascade_no_inbound_edges
  lines: 118-131
  signature: 'def test_cascade_no_inbound_edges(tmp_path: Path)'
incoming_refs: 0
outgoing_refs: 13
---
<!-- trie:section symbol=tests/test_cascade:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=5a215e1f0d0742beb90a5e926aba6bdf3f001fe19ae7274eb57ec52db1872bd6 source_ref=6da7e7637a65c81892a7c3b8c2328eb8a6d7014d role=change-detection -->
Tests the cascade computation functionality that determines which files need regeneration when source files change.

- **project**: Creates a test project with three files (lib.py, mid.py, app.py) forming a dependency chain
- **_store**: Sets up a Store with scanned project data for testing
- Tests cascade behavior at different depths, hub thresholds, and edge cases like empty changes or isolated files
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cascade:project fingerprint=e70292578e5479e74c4d74918965fb2dbdce2cb94525087be3cb484f27be59e7 body_fp=8a333cbadec5d491b518ff66d8e6fa13b3de217573aa730393480ee2bb5c7c73 source_ref=6da7e7637a65c81892a7c3b8c2328eb8a6d7014d role=test-infrastructure -->
## `def project(tmp_path: Path) -> Path`

Pytest fixture that creates a test project with trie configuration and three Python files in a dependency chain.

- Creates lib.py with helper function, mid.py that imports helper, and app.py that imports mid.compute
- Sets up trie.toml with cascade configuration including depth 1 and hub threshold 20
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cascade:_store fingerprint=baaa0b7b2e6d36d567fcba260f5d9d727395f0f6c6a4aec077e0fc3cb066367e body_fp=e99144349edf9f0314d734069c2588af3e98b950a94676cf8e1236f451817da3 source_ref=6da7e7637a65c81892a7c3b8c2328eb8a6d7014d role=test-infrastructure -->
## `def _store(project: Path) -> Store`

Creates and populates a Store instance by loading config and scanning the project directory.

- **Returns**: Store with scanned project symbols and dependencies
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cascade:test_cascade_returns_seed_when_empty fingerprint=83edbf63af4c75b645533bbe88225e2abc7d2c7b541318b8f4aa6c731ceae685 body_fp=810d44d250850ab1cb47243724facec6cd28c1ff8028817ce9636b94e369fe2c source_ref=6da7e7637a65c81892a7c3b8c2328eb8a6d7014d role=change-detection -->
## `def test_cascade_returns_seed_when_empty(tmp_path: Path)`

Tests that `compute_cascade` returns empty affected files when no changed files are provided.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cascade:test_cascade_includes_changed_files fingerprint=8c29abbf43fcbb39f847a3479d57d48e688cee2c891c9b675d21843b66e090e6 body_fp=ca5bf21139e2349c340fef8dacbd6ce43f5762d918d54e98e19ce3a696eb013e source_ref=6da7e7637a65c81892a7c3b8c2328eb8a6d7014d role=change-detection -->
## `def test_cascade_includes_changed_files(project: Path)`

Verifies that compute_cascade includes the originally changed files in its affected_files result.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cascade:test_cascade_depth_one_pulls_direct_callers fingerprint=7c50763a91d00b304c6f46a92582f8b8c9464b52b5990b527229a813438addeb body_fp=b312fa0958a438e62cab364a5cde182b62eea471f73c473b83c3c6b1d6f4383f source_ref=6da7e7637a65c81892a7c3b8c2328eb8a6d7014d role=change-detection -->
## `def test_cascade_depth_one_pulls_direct_callers(project: Path)`

Tests that cascade with depth=1 includes direct callers but not transitive ones.

- Verifies mid.py is cascaded when lib.py changes (mid:compute calls lib:helper)
- Confirms app.py is excluded at depth=1 (only references mid.compute, not lib:helper directly)
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cascade:test_cascade_depth_two_walks_two_hops fingerprint=ec77131470c458b4983e5ce0ca40d307389ac12f018ce309467e0adce1464f82 body_fp=5a14c7acf4e4f3c702807a3b5ba9cac7041e43a192bafdbedfeb4cfde105a9db source_ref=6da7e7637a65c81892a7c3b8c2328eb8a6d7014d role=change-detection -->
## `def test_cascade_depth_two_walks_two_hops(project: Path)`

Tests that cascade computation with depth=2 walks two hops in dependency chain.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cascade:test_cascade_depth_zero_only_returns_seed fingerprint=23c87fe4d6c9029fd8ff1e25e810569bf5aaee9d4ab67e171f58cb698826df2c body_fp=a52f057ce05f29c56c6e43cace0c00fe5686d63e3f513ba5e78c0ff4dff3a475 source_ref=6da7e7637a65c81892a7c3b8c2328eb8a6d7014d role=change-detection -->
## `def test_cascade_depth_zero_only_returns_seed(project: Path)`

Verifies that cascade depth zero returns only the changed file without expanding to dependencies.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cascade:test_cascade_hub_threshold_blocks_expansion fingerprint=4b7b4b4d4b113cccd4f55e335f7b0a0a368d62022dd0eefb7781e83ea2e4c1ae body_fp=78cb8b7c15c501175a126c3a70283b787049f697fcc8820e32faa9550e07b66c source_ref=6da7e7637a65c81892a7c3b8c2328eb8a6d7014d role=change-detection -->
## `def test_cascade_hub_threshold_blocks_expansion(tmp_path: Path)`

Tests that hub symbol thresholds prevent cascade expansion when callers exceed the limit.

- Creates a hub symbol with 5 callers to test threshold behavior
- Verifies high threshold (100) allows cascade expansion to all 5 callers
- Verifies low threshold (2) blocks expansion while keeping the changed file
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cascade:test_cascade_files_sorted fingerprint=9842c9750bc5541c3207ef6196eeb44500036c28eeac565d7209d94173ee606e body_fp=c3937d576240e89c8f96ec5a1c49eb4a16fffa31ab58c1001aa08e6c22a7a30d source_ref=6da7e7637a65c81892a7c3b8c2328eb8a6d7014d role=change-detection -->
## `def test_cascade_files_sorted(project: Path)`

Verifies that compute_cascade returns affected_files in sorted order.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cascade:test_cascade_no_inbound_edges fingerprint=edfc538a994df5836a052a637058b734ec01c281eaa3d82ea4183cb4903d8607 body_fp=08d03cfa40a002b768319d276ceecb76ae6de7249e2a8161a8f9dc5f56979fce source_ref=6da7e7637a65c81892a7c3b8c2328eb8a6d7014d role=change-detection -->
## `def test_cascade_no_inbound_edges(tmp_path: Path)`

Tests that compute_cascade returns only the seed file when it has no inbound dependencies.
<!-- trie:end -->











