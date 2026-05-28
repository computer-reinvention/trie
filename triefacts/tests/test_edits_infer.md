---
trie_version: 0.1.5
source: tests/test_edits_infer.py
file_fingerprint: 674d55d0e379a66c2d0e1c56dd1475331d8c700c8efa26cffb98d49ce2936902
last_synced_at: '2026-05-28T01:49:06Z'
defines:
- kind: module
  qualified_name: tests/test_edits_infer:__module__
  lines: 1-166
- kind: function
  qualified_name: tests/test_edits_infer:_make_response
  lines: 9-19
- kind: class
  qualified_name: tests/test_edits_infer:TestMergeNotes
  lines: 22-97
- kind: method
  qualified_name: tests/test_edits_infer:TestMergeNotes.test_empty_patches
  lines: 23-28
- kind: method
  qualified_name: tests/test_edits_infer:TestMergeNotes.test_single_patch_preserved
  lines: 30-36
- kind: method
  qualified_name: tests/test_edits_infer:TestMergeNotes.test_empty_response_returns_empty
  lines: 38-44
- kind: method
  qualified_name: tests/test_edits_infer:TestMergeNotes.test_preserves_reasons_via_delimiter
  lines: 46-53
- kind: method
  qualified_name: tests/test_edits_infer:TestMergeNotes.test_preserves_reasons_multiple_lines
  lines: 55-68
- kind: method
  qualified_name: tests/test_edits_infer:TestMergeNotes.test_fallback_no_delimiter
  lines: 70-79
- kind: method
  qualified_name: tests/test_edits_infer:TestMergeNotes.test_mixed_bullet_formats
  lines: 81-97
- kind: class
  qualified_name: tests/test_edits_infer:TestInferSourceAndProse
  lines: 100-165
- kind: method
  qualified_name: tests/test_edits_infer:TestInferSourceAndProse.test_basic_inference
  lines: 101-116
- kind: method
  qualified_name: tests/test_edits_infer:TestInferSourceAndProse.test_unknown_delimiter_raises
  lines: 118-128
- kind: method
  qualified_name: tests/test_edits_infer:TestInferSourceAndProse.test_source_without_code_block
  lines: 130-146
- kind: method
  qualified_name: tests/test_edits_infer:TestInferSourceAndProse.test_multiline_prose
  lines: 148-165
incoming_refs: 0
outgoing_refs: 13
---
<!-- trie:section symbol=tests/test_edits_infer:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=c10650778195a6cc658ed4963d096bf26fb6108e54fb14f862145fc170c68cb5 source_ref=c36508a0c2c7c60d58c666723859928b6264564c -->
## `tests/test_edits_infer`

Test suite for `trie.edits.infer.infer_source_and_prose` and `merge_notes`.

- `TestMergeNotes`: covers empty, single, delimiter, multi-line, and mixed-bullet cases.
- `TestInferSourceAndProse`: covers basic inference, missing delimiter error, no code-block, and multi-line prose.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_infer:_make_response fingerprint=59a0874092ddad87cbc98dc0fa09532fc367ab2bdbf188d059a22b98b621f1fd body_fp=fc3dbaf222d3a8bd4f30b57b05ba065b0a73f1322267b96b7ba1028e03549902 source_ref=c36508a0c2c7c60d58c666723859928b6264564c -->
## `_make_response(text: str)`

Build a minimal `GenerationResponse`-like `SimpleNamespace` for use in tests.

- `output_tokens`: set to word count of `text`; all cache token fields fixed at `0`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_infer:TestMergeNotes fingerprint=2ac94edc9fa7ceebb838a37a1c85809a14a56616d89e348ad7682236d38a5007 body_fp=5ce39247311e4f0cb41666901a9b56d5f77dfa40474cd2ea4114f9aa986e2cb7 source_ref=c36508a0c2c7c60d58c666723859928b6264564c -->
## `TestMergeNotes`

Test suite for `merge_notes` covering empty input, delimiter parsing, multi-bullet responses, and fallback behaviour.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_infer:TestMergeNotes.test_empty_patches fingerprint=822c95235dec295a4acaf02544991397ac94bb75f77c94f2ae3a036a4e205f19 body_fp=d87bb2c22f47735c96a37ac13d0f129de13ab4c37b1b319972f7808a5d341ec9 source_ref=c36508a0c2c7c60d58c666723859928b6264564c -->
## `TestMergeNotes.test_empty_patches(self, mocker: MockerFixture)`

Verify that `merge_notes` returns empty lists when given an empty patches list.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_infer:TestMergeNotes.test_single_patch_preserved fingerprint=5fd90769ef3f48854478973ce3231ba5a9c27f3326ed49a85028c5afb79ccb43 body_fp=161044c735c6942bd76f35e3e3297c4a3c8a120a21a5af3c20d6af1a1844605d source_ref=c36508a0c2c7c60d58c666723859928b6264564c -->
## `TestMergeNotes.test_single_patch_preserved(self, mocker: MockerFixture)`

Assert that `merge_notes` returns exactly one note containing the patch text when given a single patch.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_infer:TestMergeNotes.test_empty_response_returns_empty fingerprint=18559650a44ab0864f4c4c577fb436f6e1100a970db78e7e6708fbe77297fd5c body_fp=ba658f441fb1ce5096a666b05282919731953371cc108414cb2852f2cb781185 source_ref=c36508a0c2c7c60d58c666723859928b6264564c -->
## `TestMergeNotes.test_empty_response_returns_empty(self, mocker: MockerFixture)`

Assert that `merge_notes` returns empty lists when the client generates an empty response.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_infer:TestMergeNotes.test_preserves_reasons_via_delimiter fingerprint=c6dc88181257216989a7fe0805875b7f3b800dac067009817ff245355cfc14e1 body_fp=c399635d33d4c7c12c4b429954b370add9c87daca6b3ed659b7521334c473877 source_ref=c36508a0c2c7c60d58c666723859928b6264564c -->
## `TestMergeNotes.test_preserves_reasons_via_delimiter(self, mocker: MockerFixture)`

Verify that `merge_notes` correctly parses reasons from bullet lines using the `—` delimiter.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_infer:TestMergeNotes.test_preserves_reasons_multiple_lines fingerprint=16f4002c0a4650ffafe0bc7a2c243240ed8f6d6c3bbd1ef95359d0b055adaac1 body_fp=9366131aa559aa290b5c9e085f4195c2eba6c5187d441587dd6bfb45055d1c5c source_ref=c36508a0c2c7c60d58c666723859928b6264564c -->
## `TestMergeNotes.test_preserves_reasons_multiple_lines(self, mocker: MockerFixture)`

Verify that `merge_notes` correctly extracts reasons from multiple delimited bullet lines across mixed bullet styles.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_infer:TestMergeNotes.test_fallback_no_delimiter fingerprint=7ad4d4539ae1f8e10fc9019fd8af0acdd65992e257b43aaf96b3883025d6aa74 body_fp=0676ff35d4aa1a178f7a2dfb7daa2950dfce63377bccd36de7b752ba36b0cfe8 source_ref=c36508a0c2c7c60d58c666723859928b6264564c -->
## `TestMergeNotes.test_fallback_no_delimiter(self, mocker: MockerFixture)`

Verify `merge_notes` assigns `"merged"` as the reason for every note when the LLM response contains no `—` delimiter.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_infer:TestMergeNotes.test_mixed_bullet_formats fingerprint=806cf3bd4ba4bf0df137d8b268d19e876daa99c877a552c36e7bf56e862446a8 body_fp=a0f0ee8190f839356cfe0b46bece89a589f1bdc5f0b6e463ac208e43f298acba source_ref=c36508a0c2c7c60d58c666723859928b6264564c -->
## `TestMergeNotes.test_mixed_bullet_formats(self, mocker: MockerFixture)`

Verify `merge_notes` correctly parses notes and reasons from `<bullet>`, `*`, and `-` prefixed lines.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_infer:TestInferSourceAndProse fingerprint=5b0ef9d59027434d7a368e8a7da9029faa55869a7eca072810970e0eb9a5487b body_fp=c97afe99897424ffdd08d8c76b796ec9fb3275d1379661903847928c18968d4f source_ref=c36508a0c2c7c60d58c666723859928b6264564c -->
## `class TestInferSourceAndProse`

Test suite for `infer_source_and_prose`, covering delimiter parsing, code-block extraction, missing delimiters, and multiline prose.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_infer:TestInferSourceAndProse.test_basic_inference fingerprint=5e756324f8d487e71aaa39ce72013d13ee09c32724b6dafab9d1209cac167d79 body_fp=916c42482c473f8bc3b1f9c7b4a391878140a5b70b6a9a7d389bebb3975518ab source_ref=c36508a0c2c7c60d58c666723859928b6264564c -->
## `TestInferSourceAndProse.test_basic_inference(self, mocker: MockerFixture)`

Verify `infer_source_and_prose` correctly parses a well-formed LLM response containing a fenced code block and `---PROSE---` delimiter.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_infer:TestInferSourceAndProse.test_unknown_delimiter_raises fingerprint=edae656908aca862abf6b75c4eea882128fc0fbea2c187285dc2fd195b742b99 body_fp=16a63f5ac82893ecf7af61dcccf400053d722b2234a8b2776418be5cccdae951 source_ref=c36508a0c2c7c60d58c666723859928b6264564c -->
## `TestInferSourceAndProse.test_unknown_delimiter_raises(self, mocker: MockerFixture)`

Assert `infer_source_and_prose` raises `ValueError` when the LLM response lacks the expected delimiter.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_infer:TestInferSourceAndProse.test_source_without_code_block fingerprint=149f4b5a6d579be7bebd885d62229b085098b2a20bdb63979ed5b778cf304c83 body_fp=e9eb329ee970890651baf8a915d3889559dac67211e1d1e12e0ea2d24acca152 source_ref=c36508a0c2c7c60d58c666723859928b6264564c -->
## `TestInferSourceAndProse.test_source_without_code_block(self, mocker: MockerFixture)`

Verify `infer_source_and_prose` correctly parses LLM output when source is returned without triple-backtick fences.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_infer:TestInferSourceAndProse.test_multiline_prose fingerprint=a9feaf985d7ffd7c01931b7d68a6142cf4470c1287c9dd02e986c8a23f8ccb3c body_fp=680688b4706c94540f0e647cac8c3c3529c1de7baa7d7b366aafbf7ef8eaf1df source_ref=c36508a0c2c7c60d58c666723859928b6264564c -->
## `TestInferSourceAndProse.test_multiline_prose(self, mocker: MockerFixture)`

Verify that `infer_source_and_prose` preserves multi-paragraph prose sections following the `---PROSE---` delimiter.
<!-- trie:end -->