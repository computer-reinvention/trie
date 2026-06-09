---
trie_version: 0.1.5
source: tests/test_edits_apply.py
file_fingerprint: 19c66220dfebe979e907a3cc90b1c56b693dd7f97076bef11d320d853633637c
last_synced_at: '2026-06-07T03:57:22Z'
defines:
- kind: module
  qualified_name: tests/test_edits_apply:__module__
  lines: 1-60
- kind: class
  qualified_name: tests/test_edits_apply:TestExpandCallers
  lines: 13-36
- kind: method
  qualified_name: tests/test_edits_apply:TestExpandCallers.test_empty_seeds
  lines: 24-29
- kind: method
  qualified_name: tests/test_edits_apply:TestExpandCallers.test_seeds_not_in_store
  lines: 31-36
- kind: class
  qualified_name: tests/test_edits_apply:TestCompileCheck
  lines: 39-47
- kind: method
  qualified_name: tests/test_edits_apply:TestCompileCheck.test_valid_python
  lines: 40-41
- kind: method
  qualified_name: tests/test_edits_apply:TestCompileCheck.test_syntax_error
  lines: 43-44
- kind: method
  qualified_name: tests/test_edits_apply:TestCompileCheck.test_empty_source
  lines: 46-47
- kind: class
  qualified_name: tests/test_edits_apply:TestPreviewPatches
  lines: 50-59
- kind: method
  qualified_name: tests/test_edits_apply:TestPreviewPatches.test_no_patches
  lines: 51-59
incoming_refs: 0
outgoing_refs: 11
---
<!-- trie:section symbol=tests/test_edits_apply:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=8fbc44e801129d78bdba9cb48668747d1e5f6cbbd627558dcc69f8d53282d9eb source_ref=bc54244d8829f05b1f4b35cf791afb49a820ad23 role=test-infrastructure -->
Tests for `trie.edits.apply` module covering caller expansion, compilation checks, and patch previewing.

- `TestExpandCallers`: validates BFS traversal through caller edges with empty seeds and missing store entries
- `TestCompileCheck`: verifies Python syntax validation for valid code, syntax errors, and empty sources  
- `TestPreviewPatches`: confirms patch preview functionality returns zero counts for empty patch sets
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply:TestExpandCallers fingerprint=8709885f8614a4bef39a1dc6b2c1f86712a5c0b6dfc9677a2e2bedc978514dc2 body_fp=9f63c0e85a2e6a69e72604cb7272792f7bb0f0c36e22b53b5020717506614dd1 source_ref=bc54244d8829f05b1f4b35cf791afb49a820ad23 role=test -->
Tests the `_expand_callers` function with mock store implementations to verify caller expansion behavior.

- Contains nested mock classes `FakeRow` and `FakeConn` that simulate database query responses
- `test_empty_seeds`: verifies empty seed list returns empty result set
- `test_seeds_not_in_store`: verifies missing symbols return empty result set
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply:TestExpandCallers.test_empty_seeds fingerprint=21246c66547b52c429fa89a1a656ec2530052c26f5250a447b555b9e7c85e104 body_fp=5474805fa0ecdfc57d794ff47c7e017974deabe9874ab30c255cc1eca9da3f9d source_ref=bc54244d8829f05b1f4b35cf791afb49a820ad23 role=test -->
Tests that `_expand_callers` returns empty set when given empty seed list.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply:TestExpandCallers.test_seeds_not_in_store fingerprint=61de725e945f9129f4a11e6f13e460ffffa69092ce801fd42a48e54671044a58 body_fp=5f38382791ac0d6a0d9fcdf9d38dbe563de04bfb7dae8fb42b7a36f13188c1f0 source_ref=bc54244d8829f05b1f4b35cf791afb49a820ad23 role=test -->
Tests that TestExpandCallers._expand_callers returns empty set when given seeds not present in the store.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply:TestCompileCheck fingerprint=8fc2a428faa925362cd3b6f1fc47572ca2b93dd2bed641f8a90d959f6d40724c body_fp=ad88d332cd585451e49ec3b1d43a2662891c600b93b9c497e943d501dd3e2a6f source_ref=bc54244d8829f05b1f4b35cf791afb49a820ad23 role=test -->
Tests the `_compile_check` function's Python syntax validation behavior.

- `test_valid_python`: verifies valid Python code returns True
- `test_syntax_error`: verifies malformed syntax returns False  
- `test_empty_source`: verifies empty string returns True
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply:TestCompileCheck.test_valid_python fingerprint=844bc15fe506d9a29d6ade29d53b5fdd624d5a345d95a1e769c75593680ff7b7 body_fp=9964d2c65203ac216d0130a2f05d7441d2170b7395c306e22fa643596c31ea2c source_ref=bc54244d8829f05b1f4b35cf791afb49a820ad23 role=test -->
Verifies that TestCompileCheck._compile_check returns True for syntactically valid Python code.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply:TestCompileCheck.test_syntax_error fingerprint=6cafc8bbe6fa50aa1da4a86891aceda978e42a6ef8642d88a09b68a81fa45380 body_fp=5317041c574ccda6d908059ae875e929de98cc43dff232aa75f5e7b5c9579fdc source_ref=bc54244d8829f05b1f4b35cf791afb49a820ad23 role=test -->
Verifies that TestCompileCheck._compile_check returns False for syntactically invalid Python code.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply:TestCompileCheck.test_empty_source fingerprint=e755276c9876a3e2d1ae94c67c1306243de4462a7461d57479b960546d4ec556 body_fp=dce4517fd79792e70fa6ae84d9672440acc0cf6dd910ba238ecd0345d1562ade source_ref=bc54244d8829f05b1f4b35cf791afb49a820ad23 role=test -->
Verifies that TestCompileCheck._compile_check returns True for empty source code.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply:TestPreviewPatches fingerprint=9aae441bda8deacd452b16ecc08df66a9180ee55d974de918be7f3414b0a5b3f body_fp=422ad5c5b87b0380fb1d4c511bc9a4b9c3b3254b130d266d189a89d19241c657 source_ref=bc54244d8829f05b1f4b35cf791afb49a820ad23 role=test -->
Test class that validates the `preview_patches` function behavior with different patch scenarios.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply:TestPreviewPatches.test_no_patches fingerprint=753db71eb29f78deba90dff6621bbe966f7ae16b284c830b173cd4fb8e8a3488 body_fp=c61061792bd1bbeceb2df2954a471c62ff764689b5df6f9bfc63c3274756770f source_ref=bc54244d8829f05b1f4b35cf791afb49a820ad23 role=test -->
TestPreviewPatches.test_no_patches verifies preview_patches returns zero counts when no patches are available.
<!-- trie:end -->