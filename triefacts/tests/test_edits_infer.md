---
trie_version: 0.1.9
source: tests/test_edits_infer.py
file_fingerprint: 2d12a55eb51640bceeedc21cd3faa978e9053dc680c646f42e974e6690eb72e7
last_synced_at: '2026-07-20T09:53:34Z'
defines:
- kind: module
  qualified_name: tests/test_edits_infer:__module__
  lines: 1-145
- kind: class
  qualified_name: tests/test_edits_infer:TestMergeNotes
  lines: 7-95
- kind: method
  qualified_name: tests/test_edits_infer:TestMergeNotes.test_empty_patches
  lines: 8-12
- kind: method
  qualified_name: tests/test_edits_infer:TestMergeNotes.test_single_patch_preserved
  lines: 14-22
- kind: method
  qualified_name: tests/test_edits_infer:TestMergeNotes.test_empty_llm_response_falls_back_to_raw_notes
  lines: 24-35
- kind: method
  qualified_name: tests/test_edits_infer:TestMergeNotes.test_single_patch_skips_llm
  lines: 37-44
- kind: method
  qualified_name: tests/test_edits_infer:TestMergeNotes.test_preserves_reasons_via_delimiter
  lines: 46-55
- kind: method
  qualified_name: tests/test_edits_infer:TestMergeNotes.test_preserves_reasons_multiple_lines
  lines: 57-68
- kind: method
  qualified_name: tests/test_edits_infer:TestMergeNotes.test_fallback_no_delimiter
  lines: 70-81
- kind: method
  qualified_name: tests/test_edits_infer:TestMergeNotes.test_mixed_bullet_formats
  lines: 83-95
- kind: class
  qualified_name: tests/test_edits_infer:TestInferSourceAndProse
  lines: 98-144
- kind: method
  qualified_name: tests/test_edits_infer:TestInferSourceAndProse.test_basic_inference
  lines: 99-112
- kind: method
  qualified_name: tests/test_edits_infer:TestInferSourceAndProse.test_source_without_code_block
  lines: 114-128
- kind: method
  qualified_name: tests/test_edits_infer:TestInferSourceAndProse.test_multiline_prose
  lines: 130-144
incoming_refs: 0
outgoing_refs: 26
---
<!-- trie:section symbol=tests/test_edits_infer:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=e28b9274beb27d92743f93e6809cd4a1811d1f6e40641814f79d473227e478c2 source_ref=70a5baf39073b2a061c8be75cc64f5da1284a6d1 role=test-infrastructure -->
Test suite for the edits inference module, covering note merging and source/prose generation.

- `TestMergeNotes` — tests `merge_notes` function with various patch scenarios
- `TestInferSourceAndProse` — tests `infer_source_and_prose` function with different output formats
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_infer:TestMergeNotes fingerprint=34ea1fe7738105ede09581b4bd711d5d7583d2ed1f7a4d633972caf1f7b29ba3 body_fp=8c0ead6a7573ee1a98fcf9bb96886c41d2420757f2015c043dffdcfb5181b189 source_ref=8ea01afef00d5c188d9dfbde511de34766e2f2cd role=test -->
Tests merge_notes function with various patch configurations and client responses.

- `test_empty_patches`: verifies empty patch list returns empty results
- `test_single_patch_preserved`: checks single patch handling with matching client output
- `test_empty_llm_response_falls_back_to_raw_notes`: ensures empty LLM response falls back to raw input notes, not empty
- `test_single_patch_skips_llm`: verifies a single patch is returned verbatim without an LLM call
- `test_preserves_reasons_via_delimiter`: validates reason preservation in output
- `test_preserves_reasons_multiple_lines`: tests multiple patch merging with paired reasons
- `test_fallback_no_delimiter`: verifies fallback behavior when delimiters absent
- `test_mixed_bullet_formats`: tests various input formats produce expected outputs
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_infer:TestMergeNotes.test_empty_patches fingerprint=264d07314effb6a3d3ea131dbadcf126ac7078eb4ebff4dfb240abc4cbc03d02 body_fp=6b6ddba71b470077a812d1f4ff37f21b213d6c3331f88c0d5397f0e2a47b8b04 source_ref=70a5baf39073b2a061c8be75cc64f5da1284a6d1 role=test-infrastructure -->
Tests that TestMergeNotes.test_empty_patches returns empty lists when given no input patches.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_infer:TestMergeNotes.test_single_patch_preserved fingerprint=c503a6a0b86c3889717b4bc8e6546c1863424f629e6457a18e54820d070295ad body_fp=b47ecfe1074a2c90a8a348caf5b1ba25f135d8dc309ec5d799014a22387a6155 source_ref=70a5baf39073b2a061c8be75cc64f5da1284a6d1 role=code-editing -->
Verifies TestMergeNotes merge_notes preserves a single patch note when client returns matching output.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_infer:TestMergeNotes.test_empty_llm_response_falls_back_to_raw_notes fingerprint=4b08966d359031bcbd969f98b8d0f3f279fcc51ac1f2fe572564b0b275f0600d body_fp=7d3a91fc56529e99dd6e7e186223b92b0c4c66628718395653afcac06a6d4a63 source_ref=8ea01afef00d5c188d9dfbde511de34766e2f2cd role=test -->
Asserts that `TestMergeNotes` falls back to raw patch notes and reasons when the LLM returns an empty response, preventing data loss on a failed merge pass.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_infer:TestMergeNotes.test_single_patch_skips_llm fingerprint=432b05438a7b108fe01ac8f5eb6fab4555ada4c49305f27c7d314075c0fb4bc1 body_fp=d700b72e45ab9fb7796b39f7cdae9f0f90b7b70f205c913b38d8c25fdb8c9c7f source_ref=8ea01afef00d5c188d9dfbde511de34766e2f2cd role=test -->
Assert that `TestMergeNotes` returns a single patch verbatim without invoking the LLM when only one patch is provided.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_infer:TestMergeNotes.test_preserves_reasons_via_delimiter fingerprint=1836d50cfcb4e992a0a26cd20fc4b687002a516548cebcc50f8ff9fd35348c92 body_fp=0b9b06504264dcd395aa9ebf1234f33b4186ea85879cd34dab83ac8de2c5bd79 source_ref=70a5baf39073b2a061c8be75cc64f5da1284a6d1 role=test-infrastructure -->
Tests that TestMergeNotes preserves reasons when merging notes with matching content.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_infer:TestMergeNotes.test_preserves_reasons_multiple_lines fingerprint=c546416b38c95499af23d8a8c08eb5f4656bce8dbfc6d4e2d0e76e576d00cd24 body_fp=0cf2a4504a848279f3e64f3de696fc7ff42ccdd8108477bdcde6c3d795e18d9e source_ref=70a5baf39073b2a061c8be75cc64f5da1284a6d1 role=code-editing -->
Tests that TestMergeNotes.merge_notes preserves individual reasons when merging multiple patches with corresponding notes and reasons.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_infer:TestMergeNotes.test_fallback_no_delimiter fingerprint=4e34c3466964b09fb2d6a35c59806e2aeb85c1be6d4a9db0516ae22c72f9150f body_fp=3000fbd6d9c51d1640981c6da4470be11010c316ceeebe2c3040652995c883f2 source_ref=70a5baf39073b2a061c8be75cc64f5da1284a6d1 role=code-editing -->
Tests TestMergeNotes.merge_notes fallback behavior when client response lacks delimiter separation.

- Verifies that when client returns generic "merged" reasons, the fallback handling preserves note count
- Confirms original patch reasons are replaced with client's generic fallback values
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_infer:TestMergeNotes.test_mixed_bullet_formats fingerprint=2192ba701494849c6e69485818a00a1e596178780e9a129691631ccfe8929f68 body_fp=8979a69fcb38f4db1be3a02a1b5e2bd5be16f5612dd812cae685767279fc05f0 source_ref=70a5baf39073b2a061c8be75cc64f5da1284a6d1 role=code-editing -->
Tests that TestMergeNotes merges multiple patch notes and preserves corresponding reasons in order.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_infer:TestInferSourceAndProse fingerprint=7a600df802688fe313b6c68cc9b80d3295e9b3f08a27b7fd1bd445a0313794b7 body_fp=ad618f8354725da5e86cd4b659b611f278f4d5108d3dd03bb984ccf714cddad2 source_ref=70a5baf39073b2a061c8be75cc64f5da1284a6d1 role=test-infrastructure -->
Test class for the `infer_source_and_prose` function with various scenarios.

- `test_basic_inference`: verifies basic source and prose inference from notes and reasons
- `test_source_without_code_block`: handles LLM output without markdown code blocks
- `test_multiline_prose`: validates prose parsing across multiple paragraphs
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_infer:TestInferSourceAndProse.test_basic_inference fingerprint=6fe32699f693d902c7ba7aacab41558e2a7b2462527ebdcaebcc32039bc5013f body_fp=907b558b59b40fa5f68221bfc8d3c7e79ce95750cd49f9d2f49282a5ddad397d source_ref=70a5baf39073b2a061c8be75cc64f5da1284a6d1 role=code-editing -->
Tests TestInferSourceAndProse's ability to transform source code and prose using fake client responses.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_infer:TestInferSourceAndProse.test_source_without_code_block fingerprint=a584d6fedcd6cfbfd37a807849e69a9c05f620aedf393e02817ac2fa4ad624cf body_fp=d7dc20b8dd507a6279ce7634e91f4a44a91d5e4e475608b02cfb85dd9863ce62 source_ref=70a5baf39073b2a061c8be75cc64f5da1284a6d1 role=test-infrastructure -->
Tests that TestInferSourceAndProse.test_source_without_code_block handles LLM responses without markdown code blocks.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_infer:TestInferSourceAndProse.test_multiline_prose fingerprint=30ad28170ee5253cdba42ed7d90de74e8a10d3dbf65af86594b5b304ebeaaf61 body_fp=1e0bae2413a0bdc8bef687f2ec1802a2fd9ddfe6c6e1aabb162420ee2b662af3 source_ref=70a5baf39073b2a061c8be75cc64f5da1284a6d1 role=test-infrastructure -->
TestInferSourceAndProse.test_multiline_prose verifies that infer_source_and_prose preserves multi-paragraph prose output from the client.
<!-- trie:end -->