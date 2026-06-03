---
trie_version: 0.1.5
source: tests/test_cascade.py
file_fingerprint: ce816f67f6be54e4afae60d1aa1e6ec537a6d72ad49e6d60f298f8905ef63b92
last_synced_at: '2026-06-03T21:18:12Z'
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
<!-- trie:section symbol=tests/test_cascade:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=cded565634ab5ecfaa12a2a199a850d81c76164b1d84d70e4c1ea9cad84fbfc3 source_ref=6da7e7637a65c81892a7c3b8c2328eb8a6d7014d -->
Tests the cascade computation functionality that determines which files should be re-analyzed when changes occur.

- `project` fixture creates a temporary project with lib.py → mid.py → app.py dependency chain
- Tests verify cascade depth controls, hub threshold blocking, and file ordering
- Hub threshold prevents expansion when symbols have too many callers
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cascade:project fingerprint=e70292578e5479e74c4d74918965fb2dbdce2cb94525087be3cb484f27be59e7 body_fp=143b6b99df3ff9a6e99e55b42868d8ab39fae91cb20abc04d4f2b83f6123f9c5 source_ref=6da7e7637a65c81892a7c3b8c2328eb8a6d7014d -->
Pytest fixture that creates a temporary project with trie configuration and three Python modules forming a dependency chain.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cascade:_store fingerprint=baaa0b7b2e6d36d567fcba260f5d9d727395f0f6c6a4aec077e0fc3cb066367e body_fp=477c20b0bbc05f2ff8d4bbcadf74b51d825fc7206412865109c790a96497aa84 source_ref=6da7e7637a65c81892a7c3b8c2328eb8a6d7014d -->
Creates a Store instance for the given project, loads config, scans the project, and returns the populated store.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cascade:test_cascade_returns_seed_when_empty fingerprint=83edbf63af4c75b645533bbe88225e2abc7d2c7b541318b8f4aa6c731ceae685 body_fp=e96ce550c22bf288cda142356103025b0bab749238ca6b5687fe6eb8523962c1 source_ref=6da7e7637a65c81892a7c3b8c2328eb8a6d7014d -->
Tests that `compute_cascade` returns empty affected files when no files are changed.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cascade:test_cascade_includes_changed_files fingerprint=8c29abbf43fcbb39f847a3479d57d48e688cee2c891c9b675d21843b66e090e6 body_fp=4f83488b0295d0b0da4e338a01b4deeea30d6639d9c85ac68f4af7516379b41c source_ref=6da7e7637a65c81892a7c3b8c2328eb8a6d7014d -->
Verifies that compute_cascade includes the changed files in its affected_files result.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cascade:test_cascade_depth_one_pulls_direct_callers fingerprint=7c50763a91d00b304c6f46a92582f8b8c9464b52b5990b527229a813438addeb body_fp=b7e203e28bc39087366fdc987725030d8ff8ebbfa5d914f860352d5beb7988fa source_ref=6da7e7637a65c81892a7c3b8c2328eb8a6d7014d -->
Tests that cascade depth=1 pulls in direct callers but not transitive callers.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cascade:test_cascade_depth_two_walks_two_hops fingerprint=ec77131470c458b4983e5ce0ca40d307389ac12f018ce309467e0adce1464f82 body_fp=06aab1d03bd63e221352c60323680f12501d0e9602d72c2f238300aece815d8c source_ref=6da7e7637a65c81892a7c3b8c2328eb8a6d7014d -->
Tests that cascade with depth=2 traverses two hops of dependencies from the changed file.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cascade:test_cascade_depth_zero_only_returns_seed fingerprint=23c87fe4d6c9029fd8ff1e25e810569bf5aaee9d4ab67e171f58cb698826df2c body_fp=9d54086c2e1f977620a831c765d7a3e82be439ad1cc6078369a5d571f81c43c3 source_ref=6da7e7637a65c81892a7c3b8c2328eb8a6d7014d -->
Tests that cascade with depth=0 returns only the changed file with no expansion.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cascade:test_cascade_hub_threshold_blocks_expansion fingerprint=4b7b4b4d4b113cccd4f55e335f7b0a0a368d62022dd0eefb7781e83ea2e4c1ae body_fp=b276cc2abab16f23b6806ea9a46056af517428a4f0eaa9adeb7c2a0779c67ca8 source_ref=6da7e7637a65c81892a7c3b8c2328eb8a6d7014d -->
Verifies that hub_threshold parameter controls whether cascade expansion includes files importing heavily-referenced symbols.

- Creates utility function with 5 callers to simulate a hub symbol
- Tests permissive threshold (100) includes all caller files in cascade
- Tests restrictive threshold (2) blocks cascade expansion from hub symbol
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cascade:test_cascade_files_sorted fingerprint=9842c9750bc5541c3207ef6196eeb44500036c28eeac565d7209d94173ee606e body_fp=384943c270f0dde269fcf761f6a854b71f42d1989adaa062cb6c0d93bc6ae24a source_ref=6da7e7637a65c81892a7c3b8c2328eb8a6d7014d -->
Tests that `compute_cascade` returns affected files in sorted order.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cascade:test_cascade_no_inbound_edges fingerprint=edfc538a994df5836a052a637058b734ec01c281eaa3d82ea4183cb4903d8607 body_fp=c6d2d109f5ad5f846c3e989c52cfa4348f13cec0c0e2998e7474516b93e7ff18 source_ref=6da7e7637a65c81892a7c3b8c2328eb8a6d7014d -->
Tests that cascade computation returns only seed file when it has no inbound dependencies.
<!-- trie:end -->