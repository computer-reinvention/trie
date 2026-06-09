---
trie_version: 0.1.5
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
<!-- trie:section symbol=tests/test_cascade:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=5a215e1f0d0742beb90a5e926aba6bdf3f001fe19ae7274eb57ec52db1872bd6 source_ref=6da7e7637a65c81892a7c3b8c2328eb8a6d7014d role=change-detection -->
Tests the cascade computation functionality that determines which files need regeneration when source files change.

- **project**: Creates a test project with three files (lib.py, mid.py, app.py) forming a dependency chain
- **_store**: Sets up a Store with scanned project data for testing
- Tests cascade behavior at different depths, hub thresholds, and edge cases like empty changes or isolated files
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cascade:project fingerprint=e70292578e5479e74c4d74918965fb2dbdce2cb94525087be3cb484f27be59e7 body_fp=8be425d819b7cdc1883d2a77dcee1b5bcd363a5b6e8fdeb67f48937d41746a38 source_ref=6da7e7637a65c81892a7c3b8c2328eb8a6d7014d role=test-infrastructure -->
Pytest fixture that creates a test project with trie configuration and three Python files in a dependency chain.

- Creates lib.py with helper function, mid.py that imports helper, and app.py that imports mid.compute
- Sets up trie.toml with cascade configuration including depth 1 and hub threshold 20
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cascade:_store fingerprint=baaa0b7b2e6d36d567fcba260f5d9d727395f0f6c6a4aec077e0fc3cb066367e body_fp=08e12c43129ee3f9536c81448c269ca9f426bf7eb5d2094815712ce42c624c2c source_ref=6da7e7637a65c81892a7c3b8c2328eb8a6d7014d role=test-infrastructure -->
Creates and populates a Store instance by loading config and scanning the project directory.

- **Returns**: Store with scanned project symbols and dependencies
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cascade:test_cascade_returns_seed_when_empty fingerprint=83edbf63af4c75b645533bbe88225e2abc7d2c7b541318b8f4aa6c731ceae685 body_fp=972f4970c7864b96e4b9beca93b16b36c17f5d4f64b797fc3c75bdc0ab1a0967 source_ref=6da7e7637a65c81892a7c3b8c2328eb8a6d7014d role=change-detection -->
Tests that `compute_cascade` returns empty affected files when no changed files are provided.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cascade:test_cascade_includes_changed_files fingerprint=8c29abbf43fcbb39f847a3479d57d48e688cee2c891c9b675d21843b66e090e6 body_fp=7073fca96b2f3bf2b354ed68eda653c4ce92413d6f54b9fbbbfbce435a6fecb4 source_ref=6da7e7637a65c81892a7c3b8c2328eb8a6d7014d role=change-detection -->
Verifies that compute_cascade includes the originally changed files in its affected_files result.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cascade:test_cascade_depth_one_pulls_direct_callers fingerprint=7c50763a91d00b304c6f46a92582f8b8c9464b52b5990b527229a813438addeb body_fp=592e19f55d9d43a5b5771773bffd0227b15e568e750e4853b77a2b6e39960ff4 source_ref=6da7e7637a65c81892a7c3b8c2328eb8a6d7014d role=change-detection -->
Tests that cascade with depth=1 includes direct callers but not transitive ones.

- Verifies mid.py is cascaded when lib.py changes (mid:compute calls lib:helper)
- Confirms app.py is excluded at depth=1 (only references mid.compute, not lib:helper directly)
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cascade:test_cascade_depth_two_walks_two_hops fingerprint=ec77131470c458b4983e5ce0ca40d307389ac12f018ce309467e0adce1464f82 body_fp=a9a68c6204a4ecf10b6a38afef024044de1f80f74476a53b878238f1cc6133f2 source_ref=6da7e7637a65c81892a7c3b8c2328eb8a6d7014d role=change-detection -->
Tests that cascade computation with depth=2 walks two hops in dependency chain.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cascade:test_cascade_depth_zero_only_returns_seed fingerprint=23c87fe4d6c9029fd8ff1e25e810569bf5aaee9d4ab67e171f58cb698826df2c body_fp=772f2eab7fff9f266e204e61fe01a67d3e18bc5f332e8abd412e96c6053c6cc9 source_ref=6da7e7637a65c81892a7c3b8c2328eb8a6d7014d role=change-detection -->
Verifies that cascade depth zero returns only the changed file without expanding to dependencies.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cascade:test_cascade_hub_threshold_blocks_expansion fingerprint=4b7b4b4d4b113cccd4f55e335f7b0a0a368d62022dd0eefb7781e83ea2e4c1ae body_fp=db77e08a15af16dab5eeb1e500af6cdefacdcce29e382b058742e78285a57eb0 source_ref=6da7e7637a65c81892a7c3b8c2328eb8a6d7014d role=change-detection -->
Tests that hub symbol thresholds prevent cascade expansion when callers exceed the limit.

- Creates a hub symbol with 5 callers to test threshold behavior
- Verifies high threshold (100) allows cascade expansion to all 5 callers
- Verifies low threshold (2) blocks expansion while keeping the changed file
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cascade:test_cascade_files_sorted fingerprint=9842c9750bc5541c3207ef6196eeb44500036c28eeac565d7209d94173ee606e body_fp=b2ff28713ca7b3eb3c718e82cd0a3a352b2a096199e013e1ad47cc3b1bbcb868 source_ref=6da7e7637a65c81892a7c3b8c2328eb8a6d7014d role=change-detection -->
Verifies that compute_cascade returns affected_files in sorted order.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cascade:test_cascade_no_inbound_edges fingerprint=edfc538a994df5836a052a637058b734ec01c281eaa3d82ea4183cb4903d8607 body_fp=c0c7e311409ff67736d477e9d26dee0f6347ce11da406610e9b7419e967d8606 source_ref=6da7e7637a65c81892a7c3b8c2328eb8a6d7014d role=change-detection -->
Tests that compute_cascade returns only the seed file when it has no inbound dependencies.
<!-- trie:end -->











