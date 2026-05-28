---
trie_version: 0.1.5
source: tests/test_edits_infer.py
file_fingerprint: e4459ae0f5487c93f4160f40f85d5a3736a5a587c896fbb145da811f6695fef6
last_synced_at: '2026-05-28T14:53:42Z'
defines:
- kind: module
  qualified_name: tests/test_edits_infer:__module__
  lines: 1-130
- kind: class
  qualified_name: tests/test_edits_infer:TestMergeNotes
  lines: 7-80
- kind: method
  qualified_name: tests/test_edits_infer:TestMergeNotes.test_empty_patches
  lines: 8-12
- kind: method
  qualified_name: tests/test_edits_infer:TestMergeNotes.test_single_patch_preserved
  lines: 14-22
- kind: method
  qualified_name: tests/test_edits_infer:TestMergeNotes.test_empty_response_returns_empty
  lines: 24-29
- kind: method
  qualified_name: tests/test_edits_infer:TestMergeNotes.test_preserves_reasons_via_delimiter
  lines: 31-40
- kind: method
  qualified_name: tests/test_edits_infer:TestMergeNotes.test_preserves_reasons_multiple_lines
  lines: 42-53
- kind: method
  qualified_name: tests/test_edits_infer:TestMergeNotes.test_fallback_no_delimiter
  lines: 55-66
- kind: method
  qualified_name: tests/test_edits_infer:TestMergeNotes.test_mixed_bullet_formats
  lines: 68-80
- kind: class
  qualified_name: tests/test_edits_infer:TestInferSourceAndProse
  lines: 83-129
- kind: method
  qualified_name: tests/test_edits_infer:TestInferSourceAndProse.test_basic_inference
  lines: 84-97
- kind: method
  qualified_name: tests/test_edits_infer:TestInferSourceAndProse.test_source_without_code_block
  lines: 99-113
- kind: method
  qualified_name: tests/test_edits_infer:TestInferSourceAndProse.test_multiline_prose
  lines: 115-129
incoming_refs: 0
outgoing_refs: 24
---
<!-- trie:section symbol=tests/test_edits_infer:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=c10650778195a6cc658ed4963d096bf26fb6108e54fb14f862145fc170c68cb5 source_ref=c36508a0c2c7c60d58c666723859928b6264564c -->
## `tests/test_edits_infer`

Test suite for `trie.edits.infer.infer_source_and_prose` and `merge_notes`.

- `TestMergeNotes`: covers empty, single, delimiter, multi-line, and mixed-bullet cases.
- `TestInferSourceAndProse`: covers basic inference, missing delimiter error, no code-block, and multi-line prose.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_infer:TestMergeNotes fingerprint=536c144865fac54b0f67efce337e4540069db0d99d77a55a9d1f8ce7cfa4d0e7 body_fp=5ce39247311e4f0cb41666901a9b56d5f77dfa40474cd2ea4114f9aa986e2cb7 source_ref=ee1bca5ff64260672604cc21e6e8223a33ed21f3 -->
## `TestMergeNotes`

Test suite for `merge_notes` covering empty input, delimiter parsing, multi-bullet responses, and fallback behaviour.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_infer:TestMergeNotes.test_empty_patches fingerprint=264d07314effb6a3d3ea131dbadcf126ac7078eb4ebff4dfb240abc4cbc03d02 body_fp=e43ba34814557db967d251592ee151e958806027f65d1fbd004a2992f49781c0 source_ref=ee1bca5ff64260672604cc21e6e8223a33ed21f3 -->
## `TestMergeNotes.test_empty_patches(self)`

Verify that `merge_notes` returns empty lists when given an empty patches list.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_infer:TestMergeNotes.test_single_patch_preserved fingerprint=c503a6a0b86c3889717b4bc8e6546c1863424f629e6457a18e54820d070295ad body_fp=21bbe64d554722b2dd9ffc060c01822cc584fa2f41a43939e0006a218a506904 source_ref=ee1bca5ff64260672604cc21e6e8223a33ed21f3 -->
## `TestMergeNotes.test_single_patch_preserved(self)`

Assert that `merge_notes` returns exactly one note containing the patch text when given a single patch.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_infer:TestMergeNotes.test_empty_response_returns_empty fingerprint=333e3f8fef5e7cb72b3c886d24b7dbd7829bee752b3a5efa8cb31bb75102133c body_fp=50769f191c6c9c457358e2c53135cd68e51c6218e2f6217fc8b85bc70863c1a2 source_ref=ee1bca5ff64260672604cc21e6e8223a33ed21f3 -->
## `TestMergeNotes.test_empty_response_returns_empty(self)`

Assert that `merge_notes` returns empty lists when the client generates an empty response.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_infer:TestMergeNotes.test_preserves_reasons_via_delimiter fingerprint=1836d50cfcb4e992a0a26cd20fc4b687002a516548cebcc50f8ff9fd35348c92 body_fp=e2ac6ded91f78ad5f7419ace1b719929b46dcaab2ba6a1065862a9ce821a6424 source_ref=ee1bca5ff64260672604cc21e6e8223a33ed21f3 -->
## `TestMergeNotes.test_preserves_reasons_via_delimiter(self)`

Verify that `merge_notes` correctly parses reasons from bullet lines using the `—` delimiter.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_infer:TestMergeNotes.test_preserves_reasons_multiple_lines fingerprint=c546416b38c95499af23d8a8c08eb5f4656bce8dbfc6d4e2d0e76e576d00cd24 body_fp=4ccbcf48bccf0fec939b32ddee0b59f5bd1b75f8a149413c1b54087eaaf3bd35 source_ref=ee1bca5ff64260672604cc21e6e8223a33ed21f3 -->
## `TestMergeNotes.test_preserves_reasons_multiple_lines(self)`

Verify that `merge_notes` correctly extracts reasons from multiple delimited bullet lines across mixed bullet styles.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_infer:TestMergeNotes.test_fallback_no_delimiter fingerprint=4e34c3466964b09fb2d6a35c59806e2aeb85c1be6d4a9db0516ae22c72f9150f body_fp=40d4528e0addd7d08a3c9abe664ccf995d669bc2ea39bdc470893800199870fa source_ref=ee1bca5ff64260672604cc21e6e8223a33ed21f3 -->
## `TestMergeNotes.test_fallback_no_delimiter(self)`

Verify `merge_notes` assigns `"merged"` as the reason for every note when the LLM response contains no `—` delimiter.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_infer:TestMergeNotes.test_mixed_bullet_formats fingerprint=2192ba701494849c6e69485818a00a1e596178780e9a129691631ccfe8929f68 body_fp=64d913b7442d4aae82e0518724859dba97d75877c98685956db2d14019faf9f2 source_ref=ee1bca5ff64260672604cc21e6e8223a33ed21f3 -->
## `TestMergeNotes.test_mixed_bullet_formats(self)`

Verify `merge_notes` returns correct notes and reasons when the client yields multiple note/reason pairs.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_infer:TestInferSourceAndProse fingerprint=7a600df802688fe313b6c68cc9b80d3295e9b3f08a27b7fd1bd445a0313794b7 body_fp=c97afe99897424ffdd08d8c76b796ec9fb3275d1379661903847928c18968d4f source_ref=ee1bca5ff64260672604cc21e6e8223a33ed21f3 -->
## `class TestInferSourceAndProse`

Test suite for `infer_source_and_prose`, covering delimiter parsing, code-block extraction, missing delimiters, and multiline prose.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_infer:TestInferSourceAndProse.test_basic_inference fingerprint=6fe32699f693d902c7ba7aacab41558e2a7b2462527ebdcaebcc32039bc5013f body_fp=86ff33c5b82612d56c832d25e4d03cc7bc1f1b27a03a5817875ed246e1898bbb source_ref=ee1bca5ff64260672604cc21e6e8223a33ed21f3 -->
## `TestInferSourceAndProse.test_basic_inference(self)`

Verify `infer_source_and_prose` correctly parses a well-formed LLM response containing a fenced code block and `---PROSE---` delimiter.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_infer:TestInferSourceAndProse.test_source_without_code_block fingerprint=a584d6fedcd6cfbfd37a807849e69a9c05f620aedf393e02817ac2fa4ad624cf body_fp=02ff12dbca723a0786c653e1f1fe7d9fa62e3c54ffdb429d05c3de9aa4564769 source_ref=ee1bca5ff64260672604cc21e6e8223a33ed21f3 -->
## `TestInferSourceAndProse.test_source_without_code_block(self)`

Verify `infer_source_and_prose` correctly parses LLM output when source is returned without triple-backtick fences.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_infer:TestInferSourceAndProse.test_multiline_prose fingerprint=30ad28170ee5253cdba42ed7d90de74e8a10d3dbf65af86594b5b304ebeaaf61 body_fp=8004b3062e3c7cd243bb3b5325bf561209ffc48b406df01df54005e443ddaad2 source_ref=ee1bca5ff64260672604cc21e6e8223a33ed21f3 -->
## `TestInferSourceAndProse.test_multiline_prose(self)`

Verify that `infer_source_and_prose` preserves multi-paragraph prose sections following the `---PROSE---` delimiter.
<!-- trie:end -->