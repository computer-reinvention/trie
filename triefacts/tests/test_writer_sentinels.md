---
trie_version: 0.3.0
source: tests/test_writer_sentinels.py
file_fingerprint: 4a95712c9b333e06bf9129995cfbae5644512f19a3c4bd059cdbb148a5239a3d
last_synced_at: '2026-08-02T21:19:12Z'
defines:
- kind: module
  qualified_name: tests/test_writer_sentinels:__module__
  lines: 1-677
- kind: function
  qualified_name: tests/test_writer_sentinels:test_parse_empty
  lines: 21-24
  signature: def test_parse_empty()
- kind: function
  qualified_name: tests/test_writer_sentinels:test_parse_only_prose
  lines: 27-32
  signature: def test_parse_only_prose()
- kind: function
  qualified_name: tests/test_writer_sentinels:test_parse_front_matter_only
  lines: 35-39
  signature: def test_parse_front_matter_only()
- kind: function
  qualified_name: tests/test_writer_sentinels:test_parse_front_matter_and_prose
  lines: 42-48
  signature: def test_parse_front_matter_and_prose()
- kind: function
  qualified_name: tests/test_writer_sentinels:test_parse_single_section
  lines: 51-70
  signature: def test_parse_single_section()
- kind: function
  qualified_name: tests/test_writer_sentinels:test_parse_multiple_sections_with_prose_between
  lines: 73-88
  signature: def test_parse_multiple_sections_with_prose_between()
- kind: function
  qualified_name: tests/test_writer_sentinels:test_parse_unterminated_section_raises
  lines: 91-94
  signature: def test_parse_unterminated_section_raises()
- kind: function
  qualified_name: tests/test_writer_sentinels:test_parse_dedupes_duplicate_sections_keeping_last
  lines: 97-129
  signature: def test_parse_dedupes_duplicate_sections_keeping_last()
- kind: function
  qualified_name: tests/test_writer_sentinels:test_roundtrip_only_prose_is_byte_identical
  lines: 135-137
  signature: def test_roundtrip_only_prose_is_byte_identical()
- kind: function
  qualified_name: tests/test_writer_sentinels:test_roundtrip_with_front_matter_and_section_carrying_body_fp
  lines: 140-154
  signature: def test_roundtrip_with_front_matter_and_section_carrying_body_fp()
- kind: function
  qualified_name: tests/test_writer_sentinels:test_roundtrip_multiple_sections_with_human_prose
  lines: 157-176
  signature: def test_roundtrip_multiple_sections_with_human_prose()
- kind: function
  qualified_name: tests/test_writer_sentinels:test_legacy_section_without_body_fp_parses_and_promotes_on_render
  lines: 179-189
  signature: def test_legacy_section_without_body_fp_parses_and_promotes_on_render()
- kind: function
  qualified_name: tests/test_writer_sentinels:test_section_round_trips_source_ref
  lines: 192-206
  signature: def test_section_round_trips_source_ref()
- kind: function
  qualified_name: tests/test_writer_sentinels:test_section_without_source_ref_renders_without_it
  lines: 209-216
  signature: def test_section_without_source_ref_renders_without_it()
- kind: function
  qualified_name: tests/test_writer_sentinels:test_section_with_source_ref_renders_field_in_stable_position
  lines: 219-234
  signature: def test_section_with_source_ref_renders_field_in_stable_position()
- kind: function
  qualified_name: tests/test_writer_sentinels:test_section_legacy_format_with_source_ref_appended_parses
  lines: 237-251
  signature: def test_section_legacy_format_with_source_ref_appended_parses()
- kind: function
  qualified_name: tests/test_writer_sentinels:test_upsert_replaces_existing_section_preserves_prose
  lines: 257-280
  signature: def test_upsert_replaces_existing_section_preserves_prose()
- kind: function
  qualified_name: tests/test_writer_sentinels:test_upsert_appends_new_section_at_end
  lines: 283-291
  signature: def test_upsert_appends_new_section_at_end()
- kind: function
  qualified_name: tests/test_writer_sentinels:test_upsert_into_empty_triefact
  lines: 294-302
  signature: def test_upsert_into_empty_triefact()
- kind: function
  qualified_name: tests/test_writer_sentinels:test_remove_section
  lines: 305-322
  signature: def test_remove_section()
- kind: function
  qualified_name: tests/test_writer_sentinels:test_remove_missing_section_returns_false
  lines: 325-327
  signature: def test_remove_missing_section_returns_false()
- kind: function
  qualified_name: tests/test_writer_sentinels:test_section_qnames_in_order
  lines: 330-337
  signature: def test_section_qnames_in_order()
- kind: function
  qualified_name: tests/test_writer_sentinels:test_human_edit_between_sections_survives_regen
  lines: 343-374
  signature: def test_human_edit_between_sections_survives_regen()
- kind: function
  qualified_name: tests/test_writer_sentinels:test_front_matter_re_renders_in_insertion_order
  lines: 377-383
  signature: def test_front_matter_re_renders_in_insertion_order()
- kind: function
  qualified_name: tests/test_writer_sentinels:_sample_triefact
  lines: 389-423
  signature: def _sample_triefact() -> str
- kind: function
  qualified_name: tests/test_writer_sentinels:test_render_for_agent_strips_internal_frontmatter
  lines: 426-434
  signature: def test_render_for_agent_strips_internal_frontmatter()
- kind: function
  qualified_name: tests/test_writer_sentinels:test_render_for_agent_keeps_agent_frontmatter
  lines: 437-448
  signature: def test_render_for_agent_keeps_agent_frontmatter()
- kind: function
  qualified_name: tests/test_writer_sentinels:test_render_for_agent_strips_sentinels_and_fingerprints
  lines: 451-459
  signature: def test_render_for_agent_strips_sentinels_and_fingerprints()
- kind: function
  qualified_name: tests/test_writer_sentinels:test_render_for_agent_keeps_section_bodies_and_interleaved_prose
  lines: 462-475
  signature: def test_render_for_agent_keeps_section_bodies_and_interleaved_prose()
- kind: function
  qualified_name: tests/test_writer_sentinels:test_render_for_agent_omits_frontmatter_when_no_agent_keys
  lines: 478-496
  signature: def test_render_for_agent_omits_frontmatter_when_no_agent_keys()
- kind: function
  qualified_name: tests/test_writer_sentinels:test_render_for_agent_empty_input
  lines: 499-500
  signature: def test_render_for_agent_empty_input()
- kind: function
  qualified_name: tests/test_writer_sentinels:test_render_for_agent_prose_only_no_sentinels
  lines: 503-508
  signature: def test_render_for_agent_prose_only_no_sentinels()
- kind: function
  qualified_name: tests/test_writer_sentinels:test_agent_front_matter_keys_constant
  lines: 511-518
  signature: 'def test_agent_front_matter_keys_constant(): # Lock down the agent-key set so changes are deliberate.'
- kind: function
  qualified_name: tests/test_writer_sentinels:test_compact_view_headers_file_and_lists_symbols
  lines: 524-532
  signature: def test_compact_view_headers_file_and_lists_symbols()
- kind: function
  qualified_name: tests/test_writer_sentinels:test_compact_view_includes_signature_and_intro
  lines: 535-543
  signature: def test_compact_view_includes_signature_and_intro()
- kind: function
  qualified_name: tests/test_writer_sentinels:test_compact_view_falls_back_to_body_heading_for_legacy_triefacts
  lines: 546-561
  signature: def test_compact_view_falls_back_to_body_heading_for_legacy_triefacts()
- kind: function
  qualified_name: tests/test_writer_sentinels:test_render_for_agent_keeps_defines_signatures
  lines: 564-569
  signature: def test_render_for_agent_keeps_defines_signatures()
- kind: function
  qualified_name: tests/test_writer_sentinels:test_squeeze_signature_collapses_multiline_to_one_line
  lines: 575-577
  signature: def test_squeeze_signature_collapses_multiline_to_one_line()
- kind: function
  qualified_name: tests/test_writer_sentinels:test_signature_heading_wraps_in_backticks
  lines: 580-581
  signature: def test_signature_heading_wraps_in_backticks()
- kind: function
  qualified_name: tests/test_writer_sentinels:test_ensure_signature_heading_prepends_when_body_has_no_heading
  lines: 584-587
  signature: def test_ensure_signature_heading_prepends_when_body_has_no_heading()
- kind: function
  qualified_name: tests/test_writer_sentinels:test_ensure_signature_heading_replaces_stale_llm_heading
  lines: 590-596
  signature: "def test_ensure_signature_heading_replaces_stale_llm_heading(): # The LLM restated the signature and dropped the keyword-only marker \u2014 # the parser-derived heading must win."
- kind: function
  qualified_name: tests/test_writer_sentinels:test_ensure_signature_heading_is_idempotent
  lines: 599-603
  signature: def test_ensure_signature_heading_is_idempotent()
- kind: function
  qualified_name: tests/test_writer_sentinels:test_ensure_signature_heading_heading_only_body
  lines: 606-608
  signature: def test_ensure_signature_heading_heading_only_body()
- kind: function
  qualified_name: tests/test_writer_sentinels:test_ensure_signature_heading_leaves_deeper_headings_alone
  lines: 611-615
  signature: 'def test_ensure_signature_heading_leaves_deeper_headings_alone(): # A `###` sub-heading is not a signature heading; prepend, don''t replace.'
- kind: function
  qualified_name: tests/test_writer_sentinels:test_ensure_signature_heading_skips_leading_blank_lines
  lines: 618-621
  signature: def test_ensure_signature_heading_skips_leading_blank_lines()
- kind: function
  qualified_name: tests/test_writer_sentinels:test_long_signatures_render_on_one_physical_yaml_line
  lines: 624-643
  signature: def test_long_signatures_render_on_one_physical_yaml_line()
- kind: function
  qualified_name: tests/test_writer_sentinels:test_compact_view_is_not_raw_source
  lines: 646-650
  signature: def test_compact_view_is_not_raw_source()
- kind: function
  qualified_name: tests/test_writer_sentinels:test_compact_view_marks_private_symbols
  lines: 653-666
  signature: def test_compact_view_marks_private_symbols()
- kind: function
  qualified_name: tests/test_writer_sentinels:test_compact_view_store_overrides_take_precedence
  lines: 669-676
  signature: def test_compact_view_store_overrides_take_precedence()
incoming_refs: 0
outgoing_refs: 115
---
<!-- trie:section symbol=tests/test_writer_sentinels:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=b090a7da0bb84889c079565a7c4fc125a9e9a8c12ecaa519759621dd369fadfa source_ref=da68e1ccc1166d342f5b38d5c6453cf2fcfde631 role=test-infrastructure -->
Tests parsing, rendering, and mutation of TriefactFile with sentinel-wrapped sections and front matter.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_parse_empty fingerprint=d8d478032b2edcb69bfa32426a508c57ca253f274418d1d9533ca54ff39decf9 body_fp=0f682520397ca965eeed419222e32981ee6d16d4537afbd1fc23d175f378b39a source_ref=da68e1ccc1166d342f5b38d5c6453cf2fcfde631 role=test-infrastructure -->
## `def test_parse_empty()`

Verifies TriefactFile.parse returns empty front matter and chunks when given empty string input.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_parse_only_prose fingerprint=331924321c90bdde87c44e245a991131e979fb23776f4a7721c5a5572534e1e5 body_fp=0f63d5b6d344761718f4be081834ccb6a601dfedfb71c519b384eacd9f752aa5 source_ref=280d1b30bec4e2d4381751fa91f7866fdb7c9a99 role=test -->
## `def test_parse_only_prose()`

Tests that `TriefactFile.parse` correctly handles plain markdown content without front matter or sections.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_parse_front_matter_only fingerprint=91f029ba0079c8e4ae6b734bc86ac1fa3370f9847fce9a27aa86e8670f840489 body_fp=955e37861e7778ca1904143c35ff1fe123d63873d4d8ee3e88caa6612a1b24ad source_ref=da68e1ccc1166d342f5b38d5c6453cf2fcfde631 role=test-infrastructure -->
## `def test_parse_front_matter_only()`

Tests that TriefactFile.parse correctly handles a document containing only YAML front matter with no content chunks.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_parse_front_matter_and_prose fingerprint=9e2c997d2a34eb82a33d8cfe52afc4f0c73fa88d5d72f401546d8db3d7ee99bd body_fp=a2f6dbc3b58cc31c101145f5884fe70be6261fb77745886f90e4d85428b57745 source_ref=280d1b30bec4e2d4381751fa91f7866fdb7c9a99 role=test -->
## `def test_parse_front_matter_and_prose()`

Tests TriefactFile parsing of input containing both YAML front matter and prose content.

- Verifies front matter is extracted into the front_matter dict
- Confirms prose content after front matter becomes a single Prose chunk
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_parse_single_section fingerprint=7bdcd4d0a5afb4d45f87aafa45570e49e973a0a2f15cd10a5ec36a352d5ce027 body_fp=4d3a0ba06d43b4b4740ffb72a96dad1463c8cdc8659c1ec85e5d1827047d7e2c source_ref=280d1b30bec4e2d4381751fa91f7866fdb7c9a99 role=test -->
## `def test_parse_single_section()`

Tests TriefactFile.parse() correctly parses markdown with a single trie section between prose chunks.

- Validates that prose before and after the section becomes separate Prose chunks
- Verifies section metadata (qualified_name, fingerprint) is extracted correctly  
- Confirms section body excludes the sentinel comment markers
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_parse_multiple_sections_with_prose_between fingerprint=f6ce3fc57be98792327d599972b5ecd77f34b1e63c1092f5b2dd3cddb226c760 body_fp=4661cd55c675faeb823a8bfd57a8c942c758aff028296b67fe5b3c52fc7cf47f source_ref=280d1b30bec4e2d4381751fa91f7866fdb7c9a99 role=test -->
## `def test_parse_multiple_sections_with_prose_between()`

Tests TriefactFile.parse correctly parses multiple sections with prose chunks between them.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_parse_unterminated_section_raises fingerprint=063145f59bcc49bb9b1b79d2a1d6264e0e39c21c108518ba7fd457ab92caeee7 body_fp=4574550efee2e2e04d5c37d60d61a1f1a69a6332a6d1bc1b1251adc2caf8943c source_ref=da68e1ccc1166d342f5b38d5c6453cf2fcfde631 role=test-infrastructure -->
## `def test_parse_unterminated_section_raises()`

Verifies TriefactFile.parse raises ValueError when a trie section comment lacks a closing sentinel.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_parse_dedupes_duplicate_sections_keeping_last fingerprint=579fedea498e476686cd7ab3240c8ba5e3c4843e76c0fb7fe1b76be4fc21a743 body_fp=b66f4ba5c09e85efb6e3479394148698600673ed9a6f00fa5f4c32fd263f08ac source_ref=280d1b30bec4e2d4381751fa91f7866fdb7c9a99 role=test -->
## `def test_parse_dedupes_duplicate_sections_keeping_last()`

Verifies TriefactFile.parse deduplicates duplicate sections by keeping the last occurrence while preserving the first occurrence position.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_roundtrip_only_prose_is_byte_identical fingerprint=df3b26580aea061ee81a45fe4621020dde3e094d6c40ce016f480af7b900a516 body_fp=fbe2a7c013af9a2ed594898368744b5f51155f49af1d379b25f63113995b80e5 source_ref=da68e1ccc1166d342f5b38d5c6453cf2fcfde631 role=test-infrastructure -->
## `def test_roundtrip_only_prose_is_byte_identical()`

Verifies that parsing and rendering plain markdown text without sections produces identical output.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_roundtrip_with_front_matter_and_section_carrying_body_fp fingerprint=ecddcc86d932d0ecd4e46b4786a5c522f7caf49e59c7be9e14d65843fd2a8305 body_fp=733fde68bd4e38003c79194493dc3575bbbb8be5ac213233f82f860be7eae266 source_ref=280d1b30bec4e2d4381751fa91f7866fdb7c9a99 role=test -->
## `def test_roundtrip_with_front_matter_and_section_carrying_body_fp()`

Tests that a TriefactFile with front matter and a section with body_fp roundtrips through parse/render identically.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_roundtrip_multiple_sections_with_human_prose fingerprint=747ba03c7824c21923141c4f7e0bd804cdd4ccd6161d13f903335e8f5754005f body_fp=2998725ea627b37346f77312bef57dc43f1e5ca9771b410d16bac9c12bd14836 source_ref=280d1b30bec4e2d4381751fa91f7866fdb7c9a99 role=test -->
## `def test_roundtrip_multiple_sections_with_human_prose()`

Verifies that TriefactFile parse-render round-trip preserves multiple sections with interleaved human prose exactly.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_legacy_section_without_body_fp_parses_and_promotes_on_render fingerprint=3d551abb1de02f543f89b4091b9bdaf94c5edcc2a03992514d4aae68b274631b body_fp=8eeb573d943df5e86178360d45df2e2e9316d17c395cb5bbe1c235ba106ae26c source_ref=280d1b30bec4e2d4381751fa91f7866fdb7c9a99 role=test -->
## `def test_legacy_section_without_body_fp_parses_and_promotes_on_render()`

Tests that legacy sections without `body_fp=` parse correctly and gain body fingerprints when rendered.

- Verifies legacy sections parse with `body_fingerprint` as None
- Confirms renderer adds `body_fp=` field with hashed body content
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_section_round_trips_source_ref fingerprint=17d9bcaee21703293bc05f945dd9313f83664d80a0aa68880985462bcc41567d body_fp=96a9c50e0aadf16ede3ebfa9ccc4ca0358c6e82c53db64f04e3413c909a94877 source_ref=280d1b30bec4e2d4381751fa91f7866fdb7c9a99 role=test -->
## `def test_section_round_trips_source_ref()`

Verifies that `source_ref` attribute in triefact section sentinels persists unchanged through parse-render cycles.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_section_without_source_ref_renders_without_it fingerprint=ced24b63d8df8fc990893b0c8875c8591785b2f502a0d7806e2cf5639da1c71d body_fp=547d0a62680c2d4ad45ca343f2c9f0af86d16ec4e0ef9e365cf45c9af615fc81 source_ref=280d1b30bec4e2d4381751fa91f7866fdb7c9a99 role=test-infrastructure -->
## `def test_section_without_source_ref_renders_without_it()`

Tests that TriefactFile.render omits the source_ref field when a section lacks one.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_section_with_source_ref_renders_field_in_stable_position fingerprint=f1dd7d68b85cc31ae27153e352bbdfbc8753da8c427df4782bdacc769fc35acd body_fp=23985d3874712fc5add7321b520bfd5554b1e1317542781f177eadd3cdd145e1 source_ref=280d1b30bec4e2d4381751fa91f7866fdb7c9a99 role=test -->
## `def test_section_with_source_ref_renders_field_in_stable_position()`

Verifies that TriefactFile renders section sentinel fields in deterministic order for stable output.

- Tests that fingerprint, body_fp, and source_ref appear in consistent positions
- Ensures byte-identical rendering across multiple calls with same data
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_section_legacy_format_with_source_ref_appended_parses fingerprint=b33af3cc09b68ba42953496ef544b7fc9a3bcdbbceda3c5ca7db3ccc7fca2390 body_fp=cad4804bd7085a79fb781779e891e0a16afde47595f7a8e8f376829a88d61f95 source_ref=280d1b30bec4e2d4381751fa91f7866fdb7c9a99 role=test -->
## `def test_section_legacy_format_with_source_ref_appended_parses()`

Tests that TriefactFile.parse correctly handles legacy sections with source_ref but no body_fp.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_upsert_replaces_existing_section_preserves_prose fingerprint=19a03d771f37ccebe0c9d67628c683d99fa717c1c963166cafa7d0859553576e body_fp=1836c3abb4bb66a4f2360e03f99dcdf64cec3d62f141a6aff12602b925860d34 source_ref=280d1b30bec4e2d4381751fa91f7866fdb7c9a99 role=test-infrastructure -->
## `def test_upsert_replaces_existing_section_preserves_prose()`

Tests that TriefactFile.upsert_section replaces existing sections while preserving surrounding prose and other sections.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_upsert_appends_new_section_at_end fingerprint=f46e868629972d796c1d951ac91a82caf93691abf250b29a829bebca43a621e7 body_fp=6a5574717aa50bfe87b51a0915482f6e0674deec0867ac8fd22b08040ece4115 source_ref=280d1b30bec4e2d4381751fa91f7866fdb7c9a99 role=test -->
## `def test_upsert_appends_new_section_at_end()`

Verifies that TriefactFile.upsert_section appends new sections at the end while preserving existing prose.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_upsert_into_empty_triefact fingerprint=b200e282fd6690ffd6583614228337a8a80a1e9ab19c61f402dee458246bcbdc body_fp=1e24f8bdfb5d93f024ba41dcf4c4207399d6e218b832d974f195d017630a8706 source_ref=280d1b30bec4e2d4381751fa91f7866fdb7c9a99 role=test -->
## `def test_upsert_into_empty_triefact()`

Tests that `TriefactFile.upsert_section` correctly adds a new section to an empty triefact document and renders it with proper sentinels.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_remove_section fingerprint=78873ffb894ceac24648f6c7604b3eac9c238c94e8e3bcd401c464fc19b3808f body_fp=f9a4a81e6805d6b070a28a6daa73129f84b9a5708ac1afa47cceb512e61eb346 source_ref=280d1b30bec4e2d4381751fa91f7866fdb7c9a99 role=test -->
## `def test_remove_section()`

Tests that `TriefactFile.remove_section` removes the specified section while preserving other sections and prose.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_remove_missing_section_returns_false fingerprint=c89aedc0fb3b0f51faaae6fe50764356bc95a44a39d673c4a6757783e5f28b02 body_fp=910784d1ee900c1ef3a098f9ab11f45721257d875af69b54add0e7dad2b8d234 source_ref=280d1b30bec4e2d4381751fa91f7866fdb7c9a99 role=test-infrastructure -->
## `def test_remove_missing_section_returns_false()`

Verifies that TriefactFile.remove_section returns False when attempting to remove a non-existent section.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_section_qnames_in_order fingerprint=10e2d7e908cfea7610110e6a1aefa33470549e453459ae19945abb75daee457e body_fp=21f3838dad804364a697ef6c82d01d4f465f009adeba30f1c8480799b5714595 source_ref=280d1b30bec4e2d4381751fa91f7866fdb7c9a99 role=test-infrastructure -->
## `def test_section_qnames_in_order()`

Verifies TriefactFile.section_qnames returns qualified names in document order, not alphabetical order.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_human_edit_between_sections_survives_regen fingerprint=637b8c3ecd5d200c81d0b607862a0c940a6aec82afe722036a94505b536cd185 body_fp=efe3f93650659a3255043f29ae3b489e3d3ca135d11dc7ae67ec9a0055d7c30d source_ref=280d1b30bec4e2d4381751fa91f7866fdb7c9a99 role=test-infrastructure -->
## `def test_human_edit_between_sections_survives_regen()`

Verifies that human-written prose between generated sections survives when sections are regenerated with new content and fingerprints.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_front_matter_re_renders_in_insertion_order fingerprint=f3b23aacaca01c7bfb901f9c0898c65335b3e98a726c10478618ccb4e61257c4 body_fp=83a9ae3af483c571da375f4f3920dac6f7a8b5620e7bce842245e5b34766b2f9 source_ref=da68e1ccc1166d342f5b38d5c6453cf2fcfde631 role=test-infrastructure -->
## `def test_front_matter_re_renders_in_insertion_order()`

Verifies that TriefactFile preserves front matter key ordering when rendering after parse.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:_sample_triefact fingerprint=905d193cfe38f78ad93efa2a556186a2b4389a13b6e7523ae7fb9af513a6ee88 body_fp=1368ac7436b28457a0552ec0a0e97400aebc58f6b606729fb645cf625b0fcef4 source_ref=ace7dae880f5ec46458f4b0e1dc9b570801c60ad role=test-infrastructure -->
## `def _sample_triefact() -> str`

Returns a realistic triefact string with frontmatter, two sections, and prose for testing `render_for_agent`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_render_for_agent_strips_internal_frontmatter fingerprint=581537bdd2d548348dc9a84b5bde8ea693ed2a07b0aad02c8c9d939ebbbc50fe body_fp=e7b6b4a55d4ce572bdcd81185b270fb2d9be66b9d69df8a261016bbea52800f5 source_ref=280d1b30bec4e2d4381751fa91f7866fdb7c9a99 role=test -->
## `def test_render_for_agent_strips_internal_frontmatter()`

Tests that `render_for_agent` removes internal frontmatter keys while preserving agent-relevant content.

- Verifies `trie_version`, `file_fingerprint`, and `last_synced_at` are stripped from output
- Confirms `source:` YAML key is removed without affecting prose containing "source"
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_render_for_agent_keeps_agent_frontmatter fingerprint=a1adf8b59b837a94c7f4d32da28500c17190cef92a3028be9b2fb2d8cead0fb8 body_fp=01c8265c6a0006f3494c0217b9cfc5b4e266da1ec29b67d4d5256c399c83a26c source_ref=280d1b30bec4e2d4381751fa91f7866fdb7c9a99 role=test -->
## `def test_render_for_agent_keeps_agent_frontmatter()`

Verifies that `render_for_agent` preserves agent-relevant frontmatter keys while stripping internal ones.

- Checks frontmatter block presence with agent keys like `description`, `defines`, `incoming_refs`, `outgoing_refs`
- Validates specific content preservation including qualified names and reference counts
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_render_for_agent_strips_sentinels_and_fingerprints fingerprint=9a939937bb00998aac30c7d8665ef774c0e37fa8cbfa88034c2f09595f5f766a body_fp=cb61138405161e8a81e30953fdd1b42407a272914727e0c90b7e1d6c7cc575b0 source_ref=280d1b30bec4e2d4381751fa91f7866fdb7c9a99 role=test -->
## `def test_render_for_agent_strips_sentinels_and_fingerprints()`

Verifies that render_for_agent removes all trie sentinel comments and their embedded fingerprint attributes.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_render_for_agent_keeps_section_bodies_and_interleaved_prose fingerprint=3797428ea3cd60e6802fb0a0a5df383b905b236b7e32df134018405c909ed757 body_fp=de721c8ceaae7951eba9359010b0affc8b76f32fe4110be238863cd47a8ace04 source_ref=280d1b30bec4e2d4381751fa91f7866fdb7c9a99 role=test -->
## `def test_render_for_agent_keeps_section_bodies_and_interleaved_prose()`

Verifies that `render_for_agent` preserves section bodies and human-written prose between sections with proper spacing.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_render_for_agent_omits_frontmatter_when_no_agent_keys fingerprint=7a1c78399101ebecde991d331809bf4373573ac31ede0ffb0fffdeb8d4281b1f body_fp=0103e786c2a7e97a79a12cb4a645e9753834d778ceabdc5ee6fd8d94a5bd0fd3 source_ref=280d1b30bec4e2d4381751fa91f7866fdb7c9a99 role=test -->
## `def test_render_for_agent_omits_frontmatter_when_no_agent_keys()`

Tests that `render_for_agent` omits the frontmatter block entirely when no agent-relevant keys exist.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_render_for_agent_empty_input fingerprint=cb071367cdb29133f48c3cb017fcdfe0b91718366df0e6889cb7019b8000b292 body_fp=4c3c6f71c193a8428f99f345f6836f9eb165d731b368551dbab5f97a7f3aab37 source_ref=280d1b30bec4e2d4381751fa91f7866fdb7c9a99 role=test -->
## `def test_render_for_agent_empty_input()`

Verifies that render_for_agent returns empty string when given empty input.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_render_for_agent_prose_only_no_sentinels fingerprint=15f31ad9e89445f42fad2dbafa59d52888fd7a5e00d9285756b45de6ab7361ec body_fp=fec357a1a329a5cde49ec6abdd76f04072d9c58371cb4960ff77b436983fbd48 source_ref=280d1b30bec4e2d4381751fa91f7866fdb7c9a99 role=test -->
## `def test_render_for_agent_prose_only_no_sentinels()`

Tests that `render_for_agent` passes through plain prose without frontmatter or sentinels unchanged.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_agent_front_matter_keys_constant fingerprint=64acc40a3816c88839dddb297dcc73231822240b25e6f37b53bd7d0d3808e85b body_fp=114b4c95e579b96c74db4b75ff5ea2875a5341d8e868044b5abab2f66ced3bda source_ref=280d1b30bec4e2d4381751fa91f7866fdb7c9a99 role=test -->
## `def test_agent_front_matter_keys_constant(): # Lock down the agent-key set so changes are deliberate.`

Validates that `AGENT_FRONT_MATTER_KEYS` contains exactly the expected set of frontmatter field names.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_compact_view_headers_file_and_lists_symbols fingerprint=23e86a5b46f7cd9d510599bb1463c4cc4d9eb80fbef9c5e006917d459ef27cfb body_fp=d4783b30f614c805afa03d79e407322c9404f040e7c60eba4824ee64ce282164 source_ref=280d1b30bec4e2d4381751fa91f7866fdb7c9a99 role=test -->
## `def test_compact_view_headers_file_and_lists_symbols()`

Assert `compact_triefact_view` emits a file-level header, agent frontmatter fields, and per-symbol subheadings with qname, kind, and line range.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_compact_view_includes_signature_and_intro fingerprint=463cca80ae40a6fcf73ad7254807bec515d42f40ba3c7083df957318bee16ba3 body_fp=e5fb2ef9d33230584e37ec293f3261bef37efd4b435910c9e51b4f8cb400d518 source_ref=ace7dae880f5ec46458f4b0e1dc9b570801c60ad role=test -->
## `def test_compact_view_includes_signature_and_intro()`

Assert that `compact_triefact_view` includes exact `signature:` lines from frontmatter `defines` entries (not body headings) and the first-sentence intro for each section body.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_compact_view_falls_back_to_body_heading_for_legacy_triefacts fingerprint=8510e847c40aeb41ec2a2723c95aa81f0bfe37cf9c993362c717dc9ca59e97a1 body_fp=557efa0153e4e810dc3a69c5741b064ce0271644faf6bcba7c403df613442949 source_ref=ace7dae880f5ec46458f4b0e1dc9b570801c60ad role=test -->
## `def test_compact_view_falls_back_to_body_heading_for_legacy_triefacts()`

Assert that `compact_triefact_view` extracts the signature from the `## \`...\`` body heading when no `signature` key exists in the `defines` frontmatter entry, without double-wrapping backticks.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_render_for_agent_keeps_defines_signatures fingerprint=1c1456e307fd7070f6fcef4d9f55dc765b04778cb5f824c55899ca77db4d836c body_fp=a0791fbba3e457c6ea4b2a764c147c3e23f44ced7a9335a858562947ca583fa4 source_ref=ace7dae880f5ec46458f4b0e1dc9b570801c60ad role=test -->
## `def test_render_for_agent_keeps_defines_signatures()`

Asserts that `render_for_agent` retains `signature` values inside `defines` entries of the agent-facing frontmatter block.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_squeeze_signature_collapses_multiline_to_one_line fingerprint=793a91c9be28f4d1c5457bfa9fc3b0a647a46c626b64d8adbc216b91e888efec body_fp=54c19657550c59b93bccd82eeadaa8ba4ef92cb2f8257be29e16254e02b32332 source_ref=ace7dae880f5ec46458f4b0e1dc9b570801c60ad role=test -->
## `def test_squeeze_signature_collapses_multiline_to_one_line()`

Verify that `squeeze_signature` collapses a multi-line signature with indented parameters into a single space-separated line.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_signature_heading_wraps_in_backticks fingerprint=43a4e23a2441c62e84683db92ee83a7499f3eefec68497742b2dc82f32ccb608 body_fp=5b9c4e70f25b376245bfa27ce4120decf1245d255bdd9006c7d5894602c3e890 source_ref=ace7dae880f5ec46458f4b0e1dc9b570801c60ad role=test -->
## `def test_signature_heading_wraps_in_backticks()`

Asserts that `signature_heading` wraps a raw signature string in a level-2 Markdown heading with backtick fencing.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_ensure_signature_heading_prepends_when_body_has_no_heading fingerprint=88b7224240ed6ee560954595f5121539af91911c0d82dbdac05ae528aa0f2628 body_fp=aa91fb95efa1ca1a817f6acc44a0bfae1b9a0a8749aa19aac6b58b67afceaecc source_ref=ace7dae880f5ec46458f4b0e1dc9b570801c60ad role=test -->
## `def test_ensure_signature_heading_prepends_when_body_has_no_heading()`

Assert that `ensure_signature_heading` prepends a `## \`sig\`` heading when the body contains no existing `##` heading.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_ensure_signature_heading_replaces_stale_llm_heading fingerprint=98b5859775ca87288db437463f24e44fed4e635906ce9a197b9ad833d271415e body_fp=af94583f8d5d1367b477929d7d4f1f09facf286c4de2584ff08d8597ade4e7da source_ref=ace7dae880f5ec46458f4b0e1dc9b570801c60ad role=test -->
## `def test_ensure_signature_heading_replaces_stale_llm_heading(): # The LLM restated the signature and dropped the keyword-only marker — # the parser-derived heading must win.`

Verify that `ensure_signature_heading` overwrites a stale LLM-generated `##` heading with the authoritative parser-derived signature, including dropped keyword-only markers.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_ensure_signature_heading_is_idempotent fingerprint=e97162ba9db65fdc1d9ae4e5b445bbeee55cd3efd9e4227ccf3941aa4f079740 body_fp=1afcba7fca5bf50036a62e13f35d199c1f4536e64751fe27e802920fb01c80c1 source_ref=ace7dae880f5ec46458f4b0e1dc9b570801c60ad role=test -->
## `def test_ensure_signature_heading_is_idempotent()`

Asserts that calling `ensure_signature_heading` twice with the same signature produces the same output as calling it once.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_ensure_signature_heading_heading_only_body fingerprint=5d794a18eee543e924ecd870bc68c26ac7215bfd9f568a06336e33cff8411bc1 body_fp=3882a525ddf106ede0df0a7383346f00fc09e8452ba940db685e7cc7476fba97 source_ref=ace7dae880f5ec46458f4b0e1dc9b570801c60ad role=test -->
## `def test_ensure_signature_heading_heading_only_body()`

Verifies that `ensure_signature_heading` replaces a body consisting solely of a stale heading with the canonical signature heading, producing no trailing content.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_ensure_signature_heading_leaves_deeper_headings_alone fingerprint=25f90a6fab28639774e0df3548696473aaf355bfe74892e00a8ab89de4dbf7e2 body_fp=2b4394b0c1a5688bf3723f2a0bde8a926151c701a9c43ea25ffad3b6ef98fcc1 source_ref=ace7dae880f5ec46458f4b0e1dc9b570801c60ad role=test -->
## `def test_ensure_signature_heading_leaves_deeper_headings_alone(): # A `###` sub-heading is not a signature heading; prepend, don't replace.`

Assert that `ensure_signature_heading` prepends a `##` signature heading without replacing a `###` sub-heading in the body.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_ensure_signature_heading_skips_leading_blank_lines fingerprint=eea300034fd2b7de35140abea4778c82bff1e270c75eac871202a51f2dd5cb48 body_fp=7dc20ceacbd204add2194571411c8adc2adb9f9d48d5510c1f34c48ca5f9c59a source_ref=ace7dae880f5ec46458f4b0e1dc9b570801c60ad role=test -->
## `def test_ensure_signature_heading_skips_leading_blank_lines()`

Verify that `ensure_signature_heading` ignores leading blank lines when detecting and replacing an existing `##` signature heading.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_long_signatures_render_on_one_physical_yaml_line fingerprint=72884cdd6e2d9a95d09fc78dcb0af01afdabf91fb30804a8958307d163a6ed60 body_fp=af033d636127d8f7ca8edc605e5821a849b4f0006832ae7e8b51eefacc3f57bd source_ref=ace7dae880f5ec46458f4b0e1dc9b570801c60ad role=test -->
## `def test_long_signatures_render_on_one_physical_yaml_line()`

Assert that `TriefactFile.render()` emits long `signature` scalars on a single physical YAML line and that the value round-trips through `TriefactFile.parse()` unchanged.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_compact_view_is_not_raw_source fingerprint=37682f46fcf91f28f61d3799b91e2aa6b8980d52bd515b74ef8ef83cf5c10fcd body_fp=a05432e3b564f27280f82b86cca71f4c5479b78efe114d0103ba598165c70914 source_ref=280d1b30bec4e2d4381751fa91f7866fdb7c9a99 role=test -->
## `def test_compact_view_is_not_raw_source()`

Assert that `compact_triefact_view` output contains neither line-numbered source (`"1: "`) nor raw trie sentinel markers.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_compact_view_marks_private_symbols fingerprint=38210f88f32837b140dc1f08f6df7a6ce3d28e90889d4cb835db007e08526868 body_fp=86b8e68dfec40fc43eff786063109859549a08e77c652f8ba0194a94fcce0611 source_ref=280d1b30bec4e2d4381751fa91f7866fdb7c9a99 role=test -->
## `def test_compact_view_marks_private_symbols()`

Assert that `compact_triefact_view` appends a `private` label to the section header for symbols whose qualified name begins with an underscore.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_compact_view_store_overrides_take_precedence fingerprint=f6461ee4b3c51cb0b1c112e79ae2766c678850fc90401b315e38d9b72a52dea3 body_fp=0d2b907a559903a89c0c05c72c0df78fffdf33c6d2b69ff15e8f50d1aa104e5b source_ref=280d1b30bec4e2d4381751fa91f7866fdb7c9a99 role=test -->
## `def test_compact_view_store_overrides_take_precedence()`

Verify that `lines_by_qname` and `kind_by_qname` overrides passed to `compact_triefact_view` supersede the values from the triefact front matter.
<!-- trie:end -->