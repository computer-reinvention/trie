---
trie_version: 0.1.5
source: tests/test_edits_apply.py
file_fingerprint: 19c66220dfebe979e907a3cc90b1c56b693dd7f97076bef11d320d853633637c
last_synced_at: '2026-05-28T14:59:27Z'
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
<!-- trie:section symbol=tests/test_edits_apply:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=f676f0265a8c9c5a25e8a4398e8bcd46ecac5a7ac74b7fb1d386cfc2564407fc source_ref=4eb2b3d8551abff9491e88aef8f255528549a548 -->
## `tests/test_edits_apply`

Test suite for `trie.edits.apply` utilities covering graph algorithms, file-span helpers, and patch preview.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply:TestExpandCallers fingerprint=8709885f8614a4bef39a1dc6b2c1f86712a5c0b6dfc9677a2e2bedc978514dc2 body_fp=f38d01620f1a379eab40a9f553b6859ec66f39048b0e030ff5b9ef50e0790a51 source_ref=bc54244d8829f05b1f4b35cf791afb49a820ad23 -->
## `TestExpandCallers`

Test `_expand_callers` with empty seed lists and seeds absent from the store.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply:TestExpandCallers.test_empty_seeds fingerprint=21246c66547b52c429fa89a1a656ec2530052c26f5250a447b555b9e7c85e104 body_fp=dbcd4270cafe3a9dbdee8a0e11f69b7b7b1e59992da07a84116d14a5e11cef45 source_ref=bc54244d8829f05b1f4b35cf791afb49a820ad23 -->
## `TestExpandCallers.test_empty_seeds(self)`

Assert that `_expand_callers` returns an empty set when given no seed qualnames.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply:TestExpandCallers.test_seeds_not_in_store fingerprint=61de725e945f9129f4a11e6f13e460ffffa69092ce801fd42a48e54671044a58 body_fp=247644e2ba716ecf37f9a3d470e6f9d62defa03308220315f07365f1636ed5e9 source_ref=bc54244d8829f05b1f4b35cf791afb49a820ad23 -->
## `TestExpandCallers.test_seeds_not_in_store(self)`

Assert that `_expand_callers` returns an empty set when seeds have no matching store references.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply:TestCompileCheck fingerprint=8fc2a428faa925362cd3b6f1fc47572ca2b93dd2bed641f8a90d959f6d40724c body_fp=4ffc5d96c207a27ea7b3bc93ba9f38b42cc161959462aadb4e49daa32272b093 source_ref=bc54244d8829f05b1f4b35cf791afb49a820ad23 -->
## `TestCompileCheck`

Test suite for `_compile_check`, verifying valid Python, syntax errors, and empty source.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply:TestCompileCheck.test_valid_python fingerprint=844bc15fe506d9a29d6ade29d53b5fdd624d5a345d95a1e769c75593680ff7b7 body_fp=797ded025dac0f7b959a6569fef7c6a7210d045694c4196506f42367eafa49aa source_ref=bc54244d8829f05b1f4b35cf791afb49a820ad23 -->
## `TestCompileCheck.test_valid_python(self)`

Assert that `_compile_check` returns `True` for syntactically valid Python source.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply:TestCompileCheck.test_syntax_error fingerprint=6cafc8bbe6fa50aa1da4a86891aceda978e42a6ef8642d88a09b68a81fa45380 body_fp=22b94d2692700d4b3e53f04e97a14e844dab9c001166e87201ad20d0880c7fed source_ref=bc54244d8829f05b1f4b35cf791afb49a820ad23 -->
## `TestCompileCheck.test_syntax_error(self)`

Verify that `_compile_check` returns `False` for syntactically invalid Python source.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply:TestCompileCheck.test_empty_source fingerprint=e755276c9876a3e2d1ae94c67c1306243de4462a7461d57479b960546d4ec556 body_fp=7524db65efb1c617426afff75ee670f3e5f2c6bf78eedcdfb41c0c86f3e34405 source_ref=bc54244d8829f05b1f4b35cf791afb49a820ad23 -->
## `TestCompileCheck.test_empty_source(self)`

Assert that `_compile_check` returns `True` for an empty string input.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply:TestPreviewPatches fingerprint=9aae441bda8deacd452b16ecc08df66a9180ee55d974de918be7f3414b0a5b3f body_fp=4ee06304e2a8b2c24d8d244d56a672b6bda65052e535dbcb42dbad785f32b9ae source_ref=bc54244d8829f05b1f4b35cf791afb49a820ad23 -->
## `TestPreviewPatches`

Test `preview_patches` against a fresh `Store` with no pending patches.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply:TestPreviewPatches.test_no_patches fingerprint=753db71eb29f78deba90dff6621bbe966f7ae16b284c830b173cd4fb8e8a3488 body_fp=de5bac242b05cf78d3cc43e5fcfe90bbc0289c40435c097e0f3c64d2da9718e0 source_ref=bc54244d8829f05b1f4b35cf791afb49a820ad23 -->
## `TestPreviewPatches.test_no_patches(self, tmp_path: Path)`

Verify `preview_patches` returns zero patches and zero patched symbols against an empty `Store`.
<!-- trie:end -->