---
trie_version: 0.1.9
source: tests/test_textgen.py
file_fingerprint: bec9bf659c54bb27d5fec5f57daf3647a6e8f2d642a3d04f1cbc41dc7256a865
last_synced_at: '2026-07-20T09:54:08Z'
defines:
- kind: module
  qualified_name: tests/test_textgen:__module__
  lines: 1-90
- kind: class
  qualified_name: tests/test_textgen:TestParseCode
  lines: 6-34
- kind: method
  qualified_name: tests/test_textgen:TestParseCode.test_extracts_fenced_block
  lines: 7-9
- kind: method
  qualified_name: tests/test_textgen:TestParseCode.test_fence_with_no_language
  lines: 11-13
- kind: method
  qualified_name: tests/test_textgen:TestParseCode.test_preserves_blank_lines_inside_body
  lines: 15-17
- kind: method
  qualified_name: tests/test_textgen:TestParseCode.test_stops_prose_sections_from_leaking_into_code
  lines: 19-25
- kind: method
  qualified_name: tests/test_textgen:TestParseCode.test_missing_fence_falls_back_to_raw_minus_prose
  lines: 27-31
- kind: method
  qualified_name: tests/test_textgen:TestParseCode.test_missing_fence_and_no_prose_returns_stripped_text
  lines: 33-34
- kind: class
  qualified_name: tests/test_textgen:TestParseSingleProse
  lines: 37-46
- kind: method
  qualified_name: tests/test_textgen:TestParseSingleProse.test_extracts_delimited_prose
  lines: 38-43
- kind: method
  qualified_name: tests/test_textgen:TestParseSingleProse.test_absent_prose_returns_empty
  lines: 45-46
- kind: class
  qualified_name: tests/test_textgen:TestParseQnameProse
  lines: 49-60
- kind: method
  qualified_name: tests/test_textgen:TestParseQnameProse.test_extracts_multiple_qname_sections
  lines: 50-57
- kind: method
  qualified_name: tests/test_textgen:TestParseQnameProse.test_no_sections_returns_empty_dict
  lines: 59-60
- kind: class
  qualified_name: tests/test_textgen:TestParseNewDeps
  lines: 63-80
- kind: method
  qualified_name: tests/test_textgen:TestParseNewDeps.test_extracts_package_names
  lines: 64-73
- kind: method
  qualified_name: tests/test_textgen:TestParseNewDeps.test_ignores_relative_specifiers_and_bullets
  lines: 75-77
- kind: method
  qualified_name: tests/test_textgen:TestParseNewDeps.test_absent_returns_empty
  lines: 79-80
- kind: class
  qualified_name: tests/test_textgen:TestRoundTrip
  lines: 83-89
- kind: method
  qualified_name: tests/test_textgen:TestRoundTrip.test_single_symbol_round_trips_through_format_and_parser
  lines: 84-89
incoming_refs: 0
outgoing_refs: 21
---
<!-- trie:section symbol=tests/test_textgen:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=1f6617a28d1b4734bfbf86d2156e755b7aa4b14e2260cbf051c249fa70473e1e source_ref=5d64306b1117cddff7c77af7f6a4bf9e4edd68e4 role=test -->
Test suite for `trie.edits.textgen` covering `parse_code`, `parse_single_prose`, `parse_qname_prose`, `parse_new_deps`, and round-trip behaviour.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_textgen:TestParseCode fingerprint=b65c7a9eea8034978953431748e604340e17c308b4bdea5fb3a5954490d01270 body_fp=f0e77ad0df4074136eaf810fdc75ba597f779e67e722492797f056d67f2bcc93 source_ref=5d64306b1117cddff7c77af7f6a4bf9e4edd68e4 role=test -->
Test suite for `textgen.parse_code`, covering fenced block extraction, language tag variants, blank-line preservation, prose-section isolation, and fallback behaviour when no fence is present.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_textgen:TestParseCode.test_extracts_fenced_block fingerprint=5102336f350d10a864cc7f73cb04c6d2ca4612150254b5059e51621fecee168b body_fp=be20ecea5f7384e5d2973373d4f2202ce0623dc2fde77d6429cba67f400637e4 source_ref=5d64306b1117cddff7c77af7f6a4bf9e4edd68e4 role=test -->
Assert that `TestParseCode` extracts only the fenced code block body, stripping the fence markers and surrounding prose.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_textgen:TestParseCode.test_fence_with_no_language fingerprint=dd27007cc1f016d9cd52247240d1c8699e2c252f3e14fc2456d30011105f7da8 body_fp=e3499bfb1e5052e0703b94ea4a9e3cd5454484acd29041f92834bff2fdf29aea source_ref=5d64306b1117cddff7c77af7f6a4bf9e4edd68e4 role=test -->
Assert that `TestParseCode` correctly extracts code from a fenced block with no language specifier.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_textgen:TestParseCode.test_preserves_blank_lines_inside_body fingerprint=d237c09628c0fb714389809f05291db5a2d406a5bdcd0cab63ffbe2d18e0ed67 body_fp=26e5e12f1986c6cca756b8eae6673fbf17ff103ec0955f89def5048b31d36801 source_ref=5d64306b1117cddff7c77af7f6a4bf9e4edd68e4 role=test -->
Assert that `TestParseCode` verifies `parse_code` retains internal blank lines within a fenced code block.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_textgen:TestParseCode.test_stops_prose_sections_from_leaking_into_code fingerprint=fc94432afab6a63e48e7a6b3a9d4de108143fad61a53dcbd519e7da2dc87bd76 body_fp=5aa24f211bc20ad4e5ccdd77f29509ef8695267545ca223a62bbdd7797a22bf3 source_ref=5d64306b1117cddff7c77af7f6a4bf9e4edd68e4 role=test -->
Assert that `TestParseCode.test_stops_prose_sections_from_leaking_into_code` verifies `parse_code` excludes prose delimited by `PROSE_OPEN`/`PROSE_END` from the returned code string.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_textgen:TestParseCode.test_missing_fence_falls_back_to_raw_minus_prose fingerprint=b3e848a3a7d8d91d70cb543f8a2f346cf9badad876a79fe50c5ea8c1e6efebbd body_fp=9bfba07b46c01209ac24c443e9d363eeaab90f5a7fa4c0c5dc6ba1d589fefd6c source_ref=5d64306b1117cddff7c77af7f6a4bf9e4edd68e4 role=test -->
Assert that `TestParseCode.parse_code` returns raw text minus the prose block when no fenced code block is present.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_textgen:TestParseCode.test_missing_fence_and_no_prose_returns_stripped_text fingerprint=a3099f07eca8a6628e5a680915e86e9455e5a140c845ac8df6813def26a22713 body_fp=9b3085dddeda10677643a53093d55f8a44f1722549436423d3a3f0b9f40a0d1a source_ref=5d64306b1117cddff7c77af7f6a4bf9e4edd68e4 role=test -->
Assert that `TestParseCode` strips surrounding whitespace and returns raw text when no fence or prose markers are present.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_textgen:TestParseSingleProse fingerprint=d1b34c552cb75e97c7263e97843f8c8faeec90667079a539b00f7f1ea5f0c231 body_fp=594902ad1dade74a9df9dcdbad2591091b6ee027f85784f9dc2e539eebcca7d4 source_ref=5d64306b1117cddff7c77af7f6a4bf9e4edd68e4 role=test -->
Tests `textgen.parse_single_prose` for correct extraction of delimited prose and empty-string fallback when no prose block is present.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_textgen:TestParseSingleProse.test_extracts_delimited_prose fingerprint=6455eac1ed3fa85f008dddeb862a265777b36c00aba4eed691987f1bc6905aa2 body_fp=47c07ce5b07b6c9e23f1fca014d5a5076e2fed9ae2693467194075b50e17bf12 source_ref=5d64306b1117cddff7c77af7f6a4bf9e4edd68e4 role=test -->
Assert that `TestParseSingleProse` correctly extracts prose enclosed between `PROSE_OPEN` and `PROSE_END` delimiters from a fenced-code response.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_textgen:TestParseSingleProse.test_absent_prose_returns_empty fingerprint=ab9740a6068f1333826ac1caa9eb0fcfe2b937107ec9085197d0693d0ce02c55 body_fp=3c57bbda3e51c50bef17d1b5b4afc58dd28ec791411160be86c60898926a2c08 source_ref=5d64306b1117cddff7c77af7f6a4bf9e4edd68e4 role=test -->
Assert that `TestParseSingleProse` returns an empty string when no prose delimiters are present in the input.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_textgen:TestParseQnameProse fingerprint=9c1bc0e6ea8adac6fe6e1ec53dffd75cf022c76aae14bf95e5620aea3b08069e body_fp=37e3337a6aded44008b204da7fcb676c706de93780a504b75fe3d985a509906a source_ref=5d64306b1117cddff7c77af7f6a4bf9e4edd68e4 role=test -->
Test class for `textgen.parse_qname_prose`, covering multi-section extraction and empty-dict fallback.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_textgen:TestParseQnameProse.test_extracts_multiple_qname_sections fingerprint=0192e35a42228fe5face82eb356907a84eb89a40cd8c3aff5befa604a2705e67 body_fp=6a8ebf567c7f3650a5c2dfe62f97d04dfc86338e6a04292617ff0d3f6cba65be source_ref=5d64306b1117cddff7c77af7f6a4bf9e4edd68e4 role=test -->
Asserts that `TestParseQnameProse` correctly extracts multiple qualified-name prose sections into a `dict` keyed by qname.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_textgen:TestParseQnameProse.test_no_sections_returns_empty_dict fingerprint=6bc900e7217f4a50752f5a256451cb0d7e13a1e341df8bb28f4960e955c2ea0a body_fp=413997ba2462ce4319674c25615925602770fe1232bf21fd11f0ad606649af52 source_ref=5d64306b1117cddff7c77af7f6a4bf9e4edd68e4 role=test -->
Assert that `TestParseQnameProse` returns an empty dict when no qname prose sections are present.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_textgen:TestParseNewDeps fingerprint=fe5b9ab8aa090ac9f405de3cc0946e7be63157aec2c16cbf22ba730bf008ddbd body_fp=f813982b4cd6d36aae3b96339cacad04cef751b5e45c4254c92070bea2b179e0 source_ref=5d64306b1117cddff7c77af7f6a4bf9e4edd68e4 role=test -->
Test suite for `textgen.parse_new_deps`, covering package extraction, filtering of relative specifiers and bullet prefixes, and absent-block fallback.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_textgen:TestParseNewDeps.test_extracts_package_names fingerprint=88ae3245a439ab6c313e0117b896b2833feb0f10e7cb557bdcadf03bffe48ddf body_fp=3dd2a06aab62b4d9ef18cc22a3a9f25ade517decca091af29d543bf97a5fdb4d source_ref=5d64306b1117cddff7c77af7f6a4bf9e4edd68e4 role=test -->
Assert that `TestParseNewDeps` correctly extracts bare package names from a delimited deps block.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_textgen:TestParseNewDeps.test_ignores_relative_specifiers_and_bullets fingerprint=39831d704f5745cf609678db70d00083bab9eeb8c54efe47c942bbeb84f757df body_fp=0ec1bf385b527f0a7bd427cd6a20fd70820c1831b87f044292fccd075fb44e1e source_ref=5d64306b1117cddff7c77af7f6a4bf9e4edd68e4 role=test -->
Assert that `TestParseNewDeps.test_ignores_relative_specifiers_and_bullets` verifies `parse_new_deps` strips bullet prefixes and excludes relative/dot specifiers from results.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_textgen:TestParseNewDeps.test_absent_returns_empty fingerprint=20e0f5286314682af0c0618a7fb199320c1f1a641a2e0350aac7d41b1f3295e7 body_fp=06426755bf21de5b94ef22f51326be67c6017b9f05b0d021efc475f4991ffe59 source_ref=5d64306b1117cddff7c77af7f6a4bf9e4edd68e4 role=test -->
Assert that `TestParseNewDeps` returns an empty list when no deps block is present in the input.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_textgen:TestRoundTrip fingerprint=c78edfd4f82e7ffe46e0c1cb38f745212e036793586cd0ed99a9546201391de6 body_fp=e194c3e7e2b77eebf1230a7f0b1924228ecf16e97f8fa68ad085d764bc447133 source_ref=5d64306b1117cddff7c77af7f6a4bf9e4edd68e4 role=test -->
Verifies that `parse_code` and `parse_single_prose` correctly recover code and prose from a formatted string containing both.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_textgen:TestRoundTrip.test_single_symbol_round_trips_through_format_and_parser fingerprint=0045f332ecca54a1e517ab872e5753597129520afaf7ed5802a2149af057ca1b body_fp=295d5e274acdd145956487d5881e982bb6f1d7303230eaa6628fb25cc811e9ae source_ref=5d64306b1117cddff7c77af7f6a4bf9e4edd68e4 role=test -->
Verify that `parse_code` and `parse_single_prose` each recover their original input from a formatted code-plus-prose string.
<!-- trie:end -->