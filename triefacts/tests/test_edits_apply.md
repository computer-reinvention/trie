---
trie_version: 0.1.5
source: tests/test_edits_apply.py
file_fingerprint: 19c66220dfebe979e907a3cc90b1c56b693dd7f97076bef11d320d853633637c
last_synced_at: '2026-06-03T21:19:03Z'
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
<!-- trie:section symbol=tests/test_edits_apply:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=86a62df40a6cc4845ed1750ba600a4a65185ede056209199784587d660a6c4d3 source_ref=bc54244d8829f05b1f4b35cf791afb49a820ad23 -->
Test module for `trie.edits.apply` functionality, covering caller expansion, compilation checking, and patch preview operations.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply:TestExpandCallers fingerprint=8709885f8614a4bef39a1dc6b2c1f86712a5c0b6dfc9677a2e2bedc978514dc2 body_fp=56e506ee4397f43ce33af0e006ab31b6b8f2514df5be1a06a9456cd4f4723ac4 source_ref=bc54244d8829f05b1f4b35cf791afb49a820ad23 -->
Tests the `_expand_callers` function behavior with mock stores and database connections.

- `FakeRow`: Mock database row that returns None on fetchone()
- `FakeConn`: Mock database connection that returns FakeRow instances
- `test_empty_seeds`: Verifies empty seed list returns empty set
- `test_seeds_not_in_store`: Verifies missing symbols return empty set
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply:TestExpandCallers.test_empty_seeds fingerprint=21246c66547b52c429fa89a1a656ec2530052c26f5250a447b555b9e7c85e104 body_fp=e2f224a408666d1b54b35ed0e143dc607be8baa8d1374b2a476ea165b4201b2b source_ref=bc54244d8829f05b1f4b35cf791afb49a820ad23 -->
Verifies TestExpandCallers._expand_callers returns empty set when given empty seed list.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply:TestExpandCallers.test_seeds_not_in_store fingerprint=61de725e945f9129f4a11e6f13e460ffffa69092ce801fd42a48e54671044a58 body_fp=fa604efdce8f42e8a5137b989c10e0dbc2d15a9f4c96333a2257aaae19a39357 source_ref=bc54244d8829f05b1f4b35cf791afb49a820ad23 -->
Tests TestExpandCallers._expand_callers behavior when given seed qualified names that don't exist in the store.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply:TestCompileCheck fingerprint=8fc2a428faa925362cd3b6f1fc47572ca2b93dd2bed641f8a90d959f6d40724c body_fp=50cc1a9d22ede1dd9ce1bbaba1c1e52cc9940389a1e23c94403e412a83281ba8 source_ref=bc54244d8829f05b1f4b35cf791afb49a820ad23 -->
Tests the `_compile_check` function with various Python source code inputs.

- `test_valid_python`: verifies valid Python code returns True
- `test_syntax_error`: verifies syntactically invalid code returns False  
- `test_empty_source`: verifies empty string returns True
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply:TestCompileCheck.test_valid_python fingerprint=844bc15fe506d9a29d6ade29d53b5fdd624d5a345d95a1e769c75593680ff7b7 body_fp=b81962f26676fbb890c4f01fe65f70c62cd65bfdd2c121512416a6e084030105 source_ref=bc54244d8829f05b1f4b35cf791afb49a820ad23 -->
Verifies TestCompileCheck._compile_check returns True for syntactically valid Python code.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply:TestCompileCheck.test_syntax_error fingerprint=6cafc8bbe6fa50aa1da4a86891aceda978e42a6ef8642d88a09b68a81fa45380 body_fp=89de9d4a458a77c711e1ae60e584a066f0cb8d6f9f9675e3c16d70aab0de0efc source_ref=bc54244d8829f05b1f4b35cf791afb49a820ad23 -->
TestCompileCheck.test_syntax_error verifies that _compile_check returns False for syntactically invalid Python code.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply:TestCompileCheck.test_empty_source fingerprint=e755276c9876a3e2d1ae94c67c1306243de4462a7461d57479b960546d4ec556 body_fp=baff6a25e5b68d79e45d49711b85b9ea7dbd325366ba5610f562686078a44e1b source_ref=bc54244d8829f05b1f4b35cf791afb49a820ad23 -->
Tests that TestCompileCheck._compile_check returns True for empty source code strings.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply:TestPreviewPatches fingerprint=9aae441bda8deacd452b16ecc08df66a9180ee55d974de918be7f3414b0a5b3f body_fp=534f55c947e18dff27de67dbfb07126daf8c6aefa3043418002d69f32bb0e66b source_ref=bc54244d8829f05b1f4b35cf791afb49a820ad23 -->
Test class for the `preview_patches` function, verifying patch preview functionality in different scenarios.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply:TestPreviewPatches.test_no_patches fingerprint=753db71eb29f78deba90dff6621bbe966f7ae16b284c830b173cd4fb8e8a3488 body_fp=2600aeafc044c7711b670d59d01b66d8e193b976af80d3aefd38b8e17dcba2ac source_ref=bc54244d8829f05b1f4b35cf791afb49a820ad23 -->
Tests `preview_patches` with empty store returns zero patches and symbols.
<!-- trie:end -->