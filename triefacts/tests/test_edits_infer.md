---
trie_version: 0.1.5
source: tests/test_edits_infer.py
file_fingerprint: 6fdeece8d17321d4559245f3bdb69afcba5fe2c060d0914855856b79c3f41ef0
last_synced_at: '2026-06-06T13:18:22Z'
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
<!-- trie:section symbol=tests/test_edits_infer:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=0c5f71074b6ab3acb6097bf97db398d54e8cd4c68def666d8020deefb7a1d5d9 source_ref=70a5baf39073b2a061c8be75cc64f5da1284a6d1 role=test-infrastructure -->
Tests for the `trie.edits.infer` module covering note merging and source code inference functionality.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_infer:TestMergeNotes fingerprint=536c144865fac54b0f67efce337e4540069db0d99d77a55a9d1f8ce7cfa4d0e7 body_fp=e254dc9a36dc1a8770ec14303877d9db561cdedb535fa628a6da61ad32993d99 source_ref=70a5baf39073b2a061c8be75cc64f5da1284a6d1 role=code-editing -->
Test class for `merge_notes` function behavior with various client responses and patch inputs.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_infer:TestMergeNotes.test_empty_patches fingerprint=264d07314effb6a3d3ea131dbadcf126ac7078eb4ebff4dfb240abc4cbc03d02 body_fp=519fc12941e019119ab062e40adbd2b394f06220154c04276843b33a90f00259 source_ref=70a5baf39073b2a061c8be75cc64f5da1284a6d1 role=test-infrastructure -->
Test that TestMergeNotes.test_empty_patches verifies merge_notes returns empty lists when given no patches.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_infer:TestMergeNotes.test_single_patch_preserved fingerprint=c503a6a0b86c3889717b4bc8e6546c1863424f629e6457a18e54820d070295ad body_fp=c55d34068d66937ef830c60c28a3c16969dbadba2217595dccaacfefbfb865f6 source_ref=70a5baf39073b2a061c8be75cc64f5da1284a6d1 role=code-editing -->
Tests that TestMergeNotes preserves a single patch when merging notes through the fake client.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_infer:TestMergeNotes.test_empty_response_returns_empty fingerprint=333e3f8fef5e7cb72b3c886d24b7dbd7829bee752b3a5efa8cb31bb75102133c body_fp=ab754303ea5b42928fbc093f456a823f4301e131cef088348691c599becb25d1 source_ref=70a5baf39073b2a061c8be75cc64f5da1284a6d1 role=test-infrastructure -->
Verifies TestMergeNotes.test_empty_response_returns_empty returns empty lists when FakeTrieClient provides no output notes or reasons.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_infer:TestMergeNotes.test_preserves_reasons_via_delimiter fingerprint=1836d50cfcb4e992a0a26cd20fc4b687002a516548cebcc50f8ff9fd35348c92 body_fp=6c643bab3f647a4dad47eb22ade849d1b03ad044dbec04238493e82ccb20d4e3 source_ref=70a5baf39073b2a061c8be75cc64f5da1284a6d1 role=code-editing -->
Tests that TestMergeNotes preserves original reason text when merging patch notes through a client.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_infer:TestMergeNotes.test_preserves_reasons_multiple_lines fingerprint=c546416b38c95499af23d8a8c08eb5f4656bce8dbfc6d4e2d0e76e576d00cd24 body_fp=df764882e66da6b0e57b8f1ff20f605f376f2118ca4546ac18ea11d46c7cfc01 source_ref=70a5baf39073b2a061c8be75cc64f5da1284a6d1 role=code-editing -->
Tests that TestMergeNotes.merge_notes preserves individual reasons when processing multiple patch entries.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_infer:TestMergeNotes.test_fallback_no_delimiter fingerprint=4e34c3466964b09fb2d6a35c59806e2aeb85c1be6d4a9db0516ae22c72f9150f body_fp=4279a29e24c06a9e143b831648ed4ee29594dce353764979c40a2d04b0db447b source_ref=70a5baf39073b2a061c8be75cc64f5da1284a6d1 role=code-editing -->
Tests TestMergeNotes.test_fallback_no_delimiter verifies merge_notes returns client-provided reasons when delimiter parsing fails.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_infer:TestMergeNotes.test_mixed_bullet_formats fingerprint=2192ba701494849c6e69485818a00a1e596178780e9a129691631ccfe8929f68 body_fp=acd729c09eafc5e801f2a4c5ac2595de7b77710a98087c2c8a2ff1c531752eed source_ref=70a5baf39073b2a061c8be75cc64f5da1284a6d1 role=code-editing -->
Verifies TestMergeNotes.test_mixed_bullet_formats handles multiple patches with different note/reason formats correctly.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_infer:TestInferSourceAndProse fingerprint=7a600df802688fe313b6c68cc9b80d3295e9b3f08a27b7fd1bd445a0313794b7 body_fp=e0488066e269a86453985935348b8cf32c3d813838c8ed1986fe6fbf2a0d5e88 source_ref=70a5baf39073b2a061c8be75cc64f5da1284a6d1 role=test-infrastructure -->
Test class verifying behavior of the infer_source_and_prose function.

- `test_basic_inference`: validates function returns modified source and prose based on notes
- `test_source_without_code_block`: ensures source parsing works without markdown formatting
- `test_multiline_prose`: confirms multiline prose handling preserves paragraph structure
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_infer:TestInferSourceAndProse.test_basic_inference fingerprint=6fe32699f693d902c7ba7aacab41558e2a7b2462527ebdcaebcc32039bc5013f body_fp=ace73c56fb92a3ccc63a76265d09e5d9d400a6b6462fcc5e774e431a6ddc5784 source_ref=70a5baf39073b2a061c8be75cc64f5da1284a6d1 role=code-editing -->
TestInferSourceAndProse.test_basic_inference verifies that infer_source_and_prose correctly processes source code inference with a fake client.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_infer:TestInferSourceAndProse.test_source_without_code_block fingerprint=a584d6fedcd6cfbfd37a807849e69a9c05f620aedf393e02817ac2fa4ad624cf body_fp=ee2c41e13086ab2b8b80a2d1568af9bab8bb55c612709a77b9d00bd5bfc4114f source_ref=70a5baf39073b2a061c8be75cc64f5da1284a6d1 role=test-infrastructure -->
Tests TestInferSourceAndProse.infer_source_and_prose when LLM response lacks code block formatting.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_infer:TestInferSourceAndProse.test_multiline_prose fingerprint=30ad28170ee5253cdba42ed7d90de74e8a10d3dbf65af86594b5b304ebeaaf61 body_fp=6cf7587a16fa2cd2ff2d7d367fa3a18ea837d93dd7856c2850b51a5098635214 source_ref=70a5baf39073b2a061c8be75cc64f5da1284a6d1 role=code-editing -->
Tests that TestInferSourceAndProse handles multiline prose output spanning multiple paragraphs.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_edits_infer:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=e28b9274beb27d92743f93e6809cd4a1811d1f6e40641814f79d473227e478c2 source_ref=70a5baf39073b2a061c8be75cc64f5da1284a6d1 -->
Test suite for the edits inference module, covering note merging and source/prose generation.

- `TestMergeNotes` — tests `merge_notes` function with various patch scenarios
- `TestInferSourceAndProse` — tests `infer_source_and_prose` function with different output formats
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_infer:TestMergeNotes fingerprint=536c144865fac54b0f67efce337e4540069db0d99d77a55a9d1f8ce7cfa4d0e7 body_fp=e622048f382c355185e9dce22fa297de591059643536d0ec503ee893f7ed0639 source_ref=70a5baf39073b2a061c8be75cc64f5da1284a6d1 -->
Tests merge_notes function with various patch configurations and client responses.

- `test_empty_patches`: verifies empty patch list returns empty results
- `test_single_patch_preserved`: checks single patch handling with matching client output
- `test_empty_response_returns_empty`: ensures empty client response overrides input patches
- `test_preserves_reasons_via_delimiter`: validates reason preservation in output
- `test_preserves_reasons_multiple_lines`: tests multiple patch merging with paired reasons
- `test_fallback_no_delimiter`: verifies fallback behavior when delimiters absent
- `test_mixed_bullet_formats`: tests various input formats produce expected outputs
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_infer:TestMergeNotes.test_empty_patches fingerprint=264d07314effb6a3d3ea131dbadcf126ac7078eb4ebff4dfb240abc4cbc03d02 body_fp=6b6ddba71b470077a812d1f4ff37f21b213d6c3331f88c0d5397f0e2a47b8b04 source_ref=70a5baf39073b2a061c8be75cc64f5da1284a6d1 -->
Tests that TestMergeNotes.test_empty_patches returns empty lists when given no input patches.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_infer:TestMergeNotes.test_single_patch_preserved fingerprint=c503a6a0b86c3889717b4bc8e6546c1863424f629e6457a18e54820d070295ad body_fp=b47ecfe1074a2c90a8a348caf5b1ba25f135d8dc309ec5d799014a22387a6155 source_ref=70a5baf39073b2a061c8be75cc64f5da1284a6d1 -->
Verifies TestMergeNotes merge_notes preserves a single patch note when client returns matching output.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_infer:TestMergeNotes.test_empty_response_returns_empty fingerprint=333e3f8fef5e7cb72b3c886d24b7dbd7829bee752b3a5efa8cb31bb75102133c body_fp=d7463990a7f1ca80c92c140bef5319350b2d9118748df4bdf3b16ce3c1b36c79 source_ref=70a5baf39073b2a061c8be75cc64f5da1284a6d1 -->
Verifies that TestMergeNotes.merge_notes returns empty lists when the client provides empty responses.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_infer:TestMergeNotes.test_preserves_reasons_via_delimiter fingerprint=1836d50cfcb4e992a0a26cd20fc4b687002a516548cebcc50f8ff9fd35348c92 body_fp=0b9b06504264dcd395aa9ebf1234f33b4186ea85879cd34dab83ac8de2c5bd79 source_ref=70a5baf39073b2a061c8be75cc64f5da1284a6d1 -->
Tests that TestMergeNotes preserves reasons when merging notes with matching content.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_infer:TestMergeNotes.test_preserves_reasons_multiple_lines fingerprint=c546416b38c95499af23d8a8c08eb5f4656bce8dbfc6d4e2d0e76e576d00cd24 body_fp=0cf2a4504a848279f3e64f3de696fc7ff42ccdd8108477bdcde6c3d795e18d9e source_ref=70a5baf39073b2a061c8be75cc64f5da1284a6d1 -->
Tests that TestMergeNotes.merge_notes preserves individual reasons when merging multiple patches with corresponding notes and reasons.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_infer:TestMergeNotes.test_fallback_no_delimiter fingerprint=4e34c3466964b09fb2d6a35c59806e2aeb85c1be6d4a9db0516ae22c72f9150f body_fp=3000fbd6d9c51d1640981c6da4470be11010c316ceeebe2c3040652995c883f2 source_ref=70a5baf39073b2a061c8be75cc64f5da1284a6d1 -->
Tests TestMergeNotes.merge_notes fallback behavior when client response lacks delimiter separation.

- Verifies that when client returns generic "merged" reasons, the fallback handling preserves note count
- Confirms original patch reasons are replaced with client's generic fallback values
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_infer:TestMergeNotes.test_mixed_bullet_formats fingerprint=2192ba701494849c6e69485818a00a1e596178780e9a129691631ccfe8929f68 body_fp=8979a69fcb38f4db1be3a02a1b5e2bd5be16f5612dd812cae685767279fc05f0 source_ref=70a5baf39073b2a061c8be75cc64f5da1284a6d1 -->
Tests that TestMergeNotes merges multiple patch notes and preserves corresponding reasons in order.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_infer:TestInferSourceAndProse fingerprint=7a600df802688fe313b6c68cc9b80d3295e9b3f08a27b7fd1bd445a0313794b7 body_fp=ad618f8354725da5e86cd4b659b611f278f4d5108d3dd03bb984ccf714cddad2 source_ref=70a5baf39073b2a061c8be75cc64f5da1284a6d1 -->
Test class for the `infer_source_and_prose` function with various scenarios.

- `test_basic_inference`: verifies basic source and prose inference from notes and reasons
- `test_source_without_code_block`: handles LLM output without markdown code blocks
- `test_multiline_prose`: validates prose parsing across multiple paragraphs
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_infer:TestInferSourceAndProse.test_basic_inference fingerprint=6fe32699f693d902c7ba7aacab41558e2a7b2462527ebdcaebcc32039bc5013f body_fp=907b558b59b40fa5f68221bfc8d3c7e79ce95750cd49f9d2f49282a5ddad397d source_ref=70a5baf39073b2a061c8be75cc64f5da1284a6d1 -->
Tests TestInferSourceAndProse's ability to transform source code and prose using fake client responses.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_infer:TestInferSourceAndProse.test_source_without_code_block fingerprint=a584d6fedcd6cfbfd37a807849e69a9c05f620aedf393e02817ac2fa4ad624cf body_fp=d7dc20b8dd507a6279ce7634e91f4a44a91d5e4e475608b02cfb85dd9863ce62 source_ref=70a5baf39073b2a061c8be75cc64f5da1284a6d1 -->
Tests that TestInferSourceAndProse.test_source_without_code_block handles LLM responses without markdown code blocks.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_infer:TestInferSourceAndProse.test_multiline_prose fingerprint=30ad28170ee5253cdba42ed7d90de74e8a10d3dbf65af86594b5b304ebeaaf61 body_fp=1e0bae2413a0bdc8bef687f2ec1802a2fd9ddfe6c6e1aabb162420ee2b662af3 source_ref=70a5baf39073b2a061c8be75cc64f5da1284a6d1 -->
TestInferSourceAndProse.test_multiline_prose verifies that infer_source_and_prose preserves multi-paragraph prose output from the client.
<!-- trie:end -->