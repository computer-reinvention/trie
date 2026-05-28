---
trie_version: 0.1.5
source: tests/test_writer_sentinels.py
file_fingerprint: a519a84719aab5621f81b3d793504e8bff7ce051e43556066ad9548fafe30c79
last_synced_at: '2026-05-28T15:00:12Z'
defines:
- kind: module
  qualified_name: tests/test_writer_sentinels:__module__
  lines: 1-478
- kind: function
  qualified_name: tests/test_writer_sentinels:test_parse_empty
  lines: 17-20
- kind: function
  qualified_name: tests/test_writer_sentinels:test_parse_only_prose
  lines: 23-28
- kind: function
  qualified_name: tests/test_writer_sentinels:test_parse_front_matter_only
  lines: 31-35
- kind: function
  qualified_name: tests/test_writer_sentinels:test_parse_front_matter_and_prose
  lines: 38-44
- kind: function
  qualified_name: tests/test_writer_sentinels:test_parse_single_section
  lines: 47-66
- kind: function
  qualified_name: tests/test_writer_sentinels:test_parse_multiple_sections_with_prose_between
  lines: 69-84
- kind: function
  qualified_name: tests/test_writer_sentinels:test_parse_unterminated_section_raises
  lines: 87-90
- kind: function
  qualified_name: tests/test_writer_sentinels:test_roundtrip_only_prose_is_byte_identical
  lines: 96-98
- kind: function
  qualified_name: tests/test_writer_sentinels:test_roundtrip_with_front_matter_and_section_carrying_body_fp
  lines: 101-115
- kind: function
  qualified_name: tests/test_writer_sentinels:test_roundtrip_multiple_sections_with_human_prose
  lines: 118-137
- kind: function
  qualified_name: tests/test_writer_sentinels:test_legacy_section_without_body_fp_parses_and_promotes_on_render
  lines: 140-150
- kind: function
  qualified_name: tests/test_writer_sentinels:test_section_round_trips_source_ref
  lines: 153-167
- kind: function
  qualified_name: tests/test_writer_sentinels:test_section_without_source_ref_renders_without_it
  lines: 170-177
- kind: function
  qualified_name: tests/test_writer_sentinels:test_section_with_source_ref_renders_field_in_stable_position
  lines: 180-195
- kind: function
  qualified_name: tests/test_writer_sentinels:test_section_legacy_format_with_source_ref_appended_parses
  lines: 198-212
- kind: function
  qualified_name: tests/test_writer_sentinels:test_upsert_replaces_existing_section_preserves_prose
  lines: 218-241
- kind: function
  qualified_name: tests/test_writer_sentinels:test_upsert_appends_new_section_at_end
  lines: 244-252
- kind: function
  qualified_name: tests/test_writer_sentinels:test_upsert_into_empty_triefact
  lines: 255-263
- kind: function
  qualified_name: tests/test_writer_sentinels:test_remove_section
  lines: 266-283
- kind: function
  qualified_name: tests/test_writer_sentinels:test_remove_missing_section_returns_false
  lines: 286-288
- kind: function
  qualified_name: tests/test_writer_sentinels:test_section_qnames_in_order
  lines: 291-298
- kind: function
  qualified_name: tests/test_writer_sentinels:test_human_edit_between_sections_survives_regen
  lines: 304-335
- kind: function
  qualified_name: tests/test_writer_sentinels:test_front_matter_re_renders_in_insertion_order
  lines: 338-344
- kind: function
  qualified_name: tests/test_writer_sentinels:_sample_triefact
  lines: 350-382
- kind: function
  qualified_name: tests/test_writer_sentinels:test_render_for_agent_strips_internal_frontmatter
  lines: 385-393
- kind: function
  qualified_name: tests/test_writer_sentinels:test_render_for_agent_keeps_agent_frontmatter
  lines: 396-407
- kind: function
  qualified_name: tests/test_writer_sentinels:test_render_for_agent_strips_sentinels_and_fingerprints
  lines: 410-418
- kind: function
  qualified_name: tests/test_writer_sentinels:test_render_for_agent_keeps_section_bodies_and_interleaved_prose
  lines: 421-434
- kind: function
  qualified_name: tests/test_writer_sentinels:test_render_for_agent_omits_frontmatter_when_no_agent_keys
  lines: 437-455
- kind: function
  qualified_name: tests/test_writer_sentinels:test_render_for_agent_empty_input
  lines: 458-459
- kind: function
  qualified_name: tests/test_writer_sentinels:test_render_for_agent_prose_only_no_sentinels
  lines: 462-467
- kind: function
  qualified_name: tests/test_writer_sentinels:test_agent_front_matter_keys_constant
  lines: 470-477
incoming_refs: 0
outgoing_refs: 46
---
<!-- trie:section symbol=tests/test_writer_sentinels:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=566ce4860a1a33beab305409d08138002fdfa98fe8c9213ca18e2c0205624f4d source_ref=da68e1ccc1166d342f5b38d5c6453cf2fcfde631 -->
## `tests/test_writer_sentinels`

Test suite for `TriefactFile` parsing, round-trip rendering, mutation, and `render_for_agent` sentinel-stripping behaviour.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_parse_empty fingerprint=d8d478032b2edcb69bfa32426a508c57ca253f274418d1d9533ca54ff39decf9 body_fp=9d00d9df0b06c2c3b51c7cc00f7c08e3837344fc6c406b91563704ecd0946e3a source_ref=da68e1ccc1166d342f5b38d5c6453cf2fcfde631 -->
## `test_parse_empty()`

Assert that `TriefactFile.parse("")` yields empty front matter and no chunks.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_parse_only_prose fingerprint=331924321c90bdde87c44e245a991131e979fb23776f4a7721c5a5572534e1e5 body_fp=f35fdbe2daa618560abed36d182b0899cb3bff72f81fbe5f339c63aebd8b1398 source_ref=da68e1ccc1166d342f5b38d5c6453cf2fcfde631 -->
## `test_parse_only_prose()`

Assert that `TriefactFile.parse` with plain Markdown produces one `Prose` chunk and empty front matter.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_parse_front_matter_only fingerprint=91f029ba0079c8e4ae6b734bc86ac1fa3370f9847fce9a27aa86e8670f840489 body_fp=4b133942710c9c7882fd93e9d00525741bda3f993d7e7580ee5be5cb41443159 source_ref=da68e1ccc1166d342f5b38d5c6453cf2fcfde631 -->
## `test_parse_front_matter_only()`

Assert that `TriefactFile.parse` with only a YAML front-matter block yields correct `front_matter` and empty `chunks`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_parse_front_matter_and_prose fingerprint=9e2c997d2a34eb82a33d8cfe52afc4f0c73fa88d5d72f401546d8db3d7ee99bd body_fp=7c2831ce64f08c87b466f43abdec85c2323b8282ca780bf60ff63c00f90f58de source_ref=da68e1ccc1166d342f5b38d5c6453cf2fcfde631 -->
## `test_parse_front_matter_and_prose()`

Assert that `TriefactFile.parse` correctly separates YAML front matter from trailing prose into one `Prose` chunk.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_parse_single_section fingerprint=7bdcd4d0a5afb4d45f87aafa45570e49e973a0a2f15cd10a5ec36a352d5ce027 body_fp=03b738b6b114d6b38aecabd8570b6c8e4974306e30029c593361be010c9b73ec source_ref=da68e1ccc1166d342f5b38d5c6453cf2fcfde631 -->
## `test_parse_single_section()`

Verify that `TriefactFile.parse` splits a document with one sentinel-wrapped section into exactly three chunks: leading prose, a `Section`, and trailing prose.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_parse_multiple_sections_with_prose_between fingerprint=f6ce3fc57be98792327d599972b5ecd77f34b1e63c1092f5b2dd3cddb226c760 body_fp=d19437e15235810a84efa62a78199340def066f20568ffdbff3ee7b5f7f946aa source_ref=da68e1ccc1166d342f5b38d5c6453cf2fcfde631 -->
## `test_parse_multiple_sections_with_prose_between()`

Verify that `TriefactFile.parse` correctly interleaves `Section` and `Prose` chunks when prose appears between two sentinel-wrapped sections.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_parse_unterminated_section_raises fingerprint=063145f59bcc49bb9b1b79d2a1d6264e0e39c21c108518ba7fd457ab92caeee7 body_fp=cc7526f6db7437eb2ad843eaa55648ead01fe605c3e3ab22acaad629f540d9f7 source_ref=da68e1ccc1166d342f5b38d5c6453cf2fcfde631 -->
## `test_parse_unterminated_section_raises()`

Assert that `TriefactFile.parse` raises `ValueError` matching "Unterminated" when a section sentinel is never closed.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_roundtrip_only_prose_is_byte_identical fingerprint=df3b26580aea061ee81a45fe4621020dde3e094d6c40ce016f480af7b900a516 body_fp=f36d44e874648fe53a43d39f7ea5c41dee931396b0a724a23a2c4178af9176e5 source_ref=da68e1ccc1166d342f5b38d5c6453cf2fcfde631 -->
## `test_roundtrip_only_prose_is_byte_identical()`

Assert that parsing and re-rendering a prose-only triefact produces byte-identical output.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_roundtrip_with_front_matter_and_section_carrying_body_fp fingerprint=ecddcc86d932d0ecd4e46b4786a5c522f7caf49e59c7be9e14d65843fd2a8305 body_fp=028a443decfdaa7a41f959b85107670fdafb0f72fcb9ec71cabd8918c7128155 source_ref=da68e1ccc1166d342f5b38d5c6453cf2fcfde631 -->
## `test_roundtrip_with_front_matter_and_section_carrying_body_fp()`

Assert that a `TriefactFile` with front matter and a `body_fp`-carrying section renders byte-identically to its source text.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_roundtrip_multiple_sections_with_human_prose fingerprint=747ba03c7824c21923141c4f7e0bd804cdd4ccd6161d13f903335e8f5754005f body_fp=759a706c188982e231d317c694f306770087fa708d504c9830402ae05ffc1e74 source_ref=da68e1ccc1166d342f5b38d5c6453cf2fcfde631 -->
## `test_roundtrip_multiple_sections_with_human_prose()`

Assert that `TriefactFile.parse().render()` is byte-identical for a document with front matter, two sentinel sections, and interleaved hand-written prose.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_legacy_section_without_body_fp_parses_and_promotes_on_render fingerprint=3d551abb1de02f543f89b4091b9bdaf94c5edcc2a03992514d4aae68b274631b body_fp=b5bd8356cf450e81f8d1ce66863d47441c66089952140852fbbdb562d730fdde source_ref=da68e1ccc1166d342f5b38d5c6453cf2fcfde631 -->
## `test_legacy_section_without_body_fp_parses_and_promotes_on_render()`

Verify that sections lacking `body_fp=` parse successfully and gain a computed `body_fp=` on render.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_section_round_trips_source_ref fingerprint=17d9bcaee21703293bc05f945dd9313f83664d80a0aa68880985462bcc41567d body_fp=32cbce6cf2503fe6aeadc47387965fc78c398296d2c45980f35514cb85805bad source_ref=da68e1ccc1166d342f5b38d5c6453cf2fcfde631 -->
## `test_section_round_trips_source_ref()`

Assert that `source_ref=` in a section sentinel survives a `parse` → `render` round-trip unchanged.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_section_without_source_ref_renders_without_it fingerprint=ced24b63d8df8fc990893b0c8875c8591785b2f502a0d7806e2cf5639da1c71d body_fp=c118fa07373aefc2d7340ef59c5565e81432489867138012f051cc6d3798445e source_ref=da68e1ccc1166d342f5b38d5c6453cf2fcfde631 -->
## `test_section_without_source_ref_renders_without_it()`

Assert that a freshly upserted section without `source_ref` renders `fingerprint=` and `body_fp=` but omits `source_ref=`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_section_with_source_ref_renders_field_in_stable_position fingerprint=f1dd7d68b85cc31ae27153e352bbdfbc8753da8c427df4782bdacc769fc35acd body_fp=f1a8858e12b6a9c11a82d104475fc6f18a1dc187ce4e2a6a4b907548a0689ae9 source_ref=da68e1ccc1166d342f5b38d5c6453cf2fcfde631 -->
## `test_section_with_source_ref_renders_field_in_stable_position()`

Assert that sentinel fields render in stable order: `fingerprint=` < `body_fp=` < `source_ref=`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_section_legacy_format_with_source_ref_appended_parses fingerprint=b33af3cc09b68ba42953496ef544b7fc9a3bcdbbceda3c5ca7db3ccc7fca2390 body_fp=8796256702fe23f8935a2a18b2d8efbd58f6f2832f67d87c758db1c87ab4fba2 source_ref=da68e1ccc1166d342f5b38d5c6453cf2fcfde631 -->
## `test_section_legacy_format_with_source_ref_appended_parses()`

Assert that a section carrying `source_ref=` but no `body_fp=` parses without error and exposes both fields correctly.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_upsert_replaces_existing_section_preserves_prose fingerprint=19a03d771f37ccebe0c9d67628c683d99fa717c1c963166cafa7d0859553576e body_fp=6f82cd5e6effa51d9c4f0bf0745bcbb699f55bffb98bb515c1c4246f4428f48a source_ref=da68e1ccc1166d342f5b38d5c6453cf2fcfde631 -->
## `test_upsert_replaces_existing_section_preserves_prose()`

Assert that upserting a section replaces its body and fingerprint while leaving surrounding prose and other sections intact.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_upsert_appends_new_section_at_end fingerprint=f46e868629972d796c1d951ac91a82caf93691abf250b29a829bebca43a621e7 body_fp=deba981f1bdee99c691823285dd148ec4a65c12db84ca6a2a2427ea0401851bc source_ref=da68e1ccc1166d342f5b38d5c6453cf2fcfde631 -->
## `test_upsert_appends_new_section_at_end()`

Verify that upserting a new section into a `TriefactFile` appends it after existing prose.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_upsert_into_empty_triefact fingerprint=b200e282fd6690ffd6583614228337a8a80a1e9ab19c61f402dee458246bcbdc body_fp=0b601a5e67258afc7a266cf077860462cee31e3e5dcae069e0c46d207e88c685 source_ref=da68e1ccc1166d342f5b38d5c6453cf2fcfde631 -->
## `test_upsert_into_empty_triefact()`

Verify that upserting a section into an empty `TriefactFile` produces a byte-identical single-section render with correct `body_fp`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_remove_section fingerprint=78873ffb894ceac24648f6c7604b3eac9c238c94e8e3bcd401c464fc19b3808f body_fp=9e522cf171658963d78472eb8950b4d394e7e4386b5dec71b7d69f07dcf62eb0 source_ref=da68e1ccc1166d342f5b38d5c6453cf2fcfde631 -->
## `test_remove_section()`

Verify that `remove_section` deletes the target section and its body while preserving other sections and prose.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_remove_missing_section_returns_false fingerprint=c89aedc0fb3b0f51faaae6fe50764356bc95a44a39d673c4a6757783e5f28b02 body_fp=7513e0dba469f4c198d669d620796f7d981aa5c6e2a1a3fa2ce8be1ca34feeca source_ref=da68e1ccc1166d342f5b38d5c6453cf2fcfde631 -->
## `test_remove_missing_section_returns_false()`

Assert that `TriefactFile.remove_section` returns `False` when the named section does not exist.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_section_qnames_in_order fingerprint=10e2d7e908cfea7610110e6a1aefa33470549e453459ae19945abb75daee457e body_fp=b5e62791e259533d4ce8fea09cdb70467bd62a9a43b91acf789e1dc358d7f040 source_ref=da68e1ccc1166d342f5b38d5c6453cf2fcfde631 -->
## `test_section_qnames_in_order()`

Verify that `TriefactFile.section_qnames()` returns qualified names in document order.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_human_edit_between_sections_survives_regen fingerprint=637b8c3ecd5d200c81d0b607862a0c940a6aec82afe722036a94505b536cd185 body_fp=dbc0a909ffddb328ab4e0f1c54f1cec41295506d87b50aa19de43269c05a9d38 source_ref=da68e1ccc1166d342f5b38d5c6453cf2fcfde631 -->
## `test_human_edit_between_sections_survives_regen()`

Assert that hand-written prose between sentinel sections survives a `upsert_section` regeneration cycle.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_front_matter_re_renders_in_insertion_order fingerprint=f3b23aacaca01c7bfb901f9c0898c65335b3e98a726c10478618ccb4e61257c4 body_fp=4143c01088a868c595fe0e0d6e5c9fd0e1a7ade53c3e55bade0553b7372bdaea source_ref=da68e1ccc1166d342f5b38d5c6453cf2fcfde631 -->
## `test_front_matter_re_renders_in_insertion_order()`

Assert that `TriefactFile.render()` preserves front-matter key order from the original source text.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:_sample_triefact fingerprint=da10c5cdf0a4dbdc27a89de7be7c634bfb5d951821a716bf2822c89925533877 body_fp=7fc0c5e0046674fe5589eff46d2c96ed9d78184ab3a46299a4b635f67616e207 source_ref=da68e1ccc1166d342f5b38d5c6453cf2fcfde631 -->
## `_sample_triefact() -> str`

Return a realistic triefact string with mixed front-matter keys, two sentinel-wrapped sections, and interleaved prose for `render_for_agent` tests.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_render_for_agent_strips_internal_frontmatter fingerprint=581537bdd2d548348dc9a84b5bde8ea693ed2a07b0aad02c8c9d939ebbbc50fe body_fp=11c1d6d5bf4b2fd4f39d16fa77378706db25b6e45177b1490300f57beebdaec2 source_ref=da68e1ccc1166d342f5b38d5c6453cf2fcfde631 -->
## `test_render_for_agent_strips_internal_frontmatter()`

Assert that `render_for_agent` removes `trie_version`, `file_fingerprint`, `last_synced_at`, and `source` from the front matter block.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_render_for_agent_keeps_agent_frontmatter fingerprint=a1adf8b59b837a94c7f4d32da28500c17190cef92a3028be9b2fb2d8cead0fb8 body_fp=0ff465ec88a53133ba81f14383f8e53449d791fa06709e997819b668df22bb63 source_ref=da68e1ccc1166d342f5b38d5c6453cf2fcfde631 -->
## `test_render_for_agent_keeps_agent_frontmatter()`

Assert that `render_for_agent` retains all agent-relevant front-matter keys in the output YAML block.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_render_for_agent_strips_sentinels_and_fingerprints fingerprint=9a939937bb00998aac30c7d8665ef774c0e37fa8cbfa88034c2f09595f5f766a body_fp=a581556f9d3ac5da7413eb453217a908220360b38ed63c6d7d0f960cfd96fba5 source_ref=da68e1ccc1166d342f5b38d5c6453cf2fcfde631 -->
## `test_render_for_agent_strips_sentinels_and_fingerprints()`

Assert that `render_for_agent` removes all sentinel lines and fingerprint fields from the output.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_render_for_agent_keeps_section_bodies_and_interleaved_prose fingerprint=3797428ea3cd60e6802fb0a0a5df383b905b236b7e32df134018405c909ed757 body_fp=4fffb206951dea02bd3fce11d23abbcc8fb9360140d6917af583df48412bb9e1 source_ref=da68e1ccc1166d342f5b38d5c6453cf2fcfde631 -->
## `test_render_for_agent_keeps_section_bodies_and_interleaved_prose()`

Assert that `render_for_agent` preserves section bodies, interleaved prose, and blank-line separation between sections.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_render_for_agent_omits_frontmatter_when_no_agent_keys fingerprint=7a1c78399101ebecde991d331809bf4373573ac31ede0ffb0fffdeb8d4281b1f body_fp=9357db4ad27fe7739fb8621e09014ad1e8cafac7bc4d8649db507c072a503d89 source_ref=da68e1ccc1166d342f5b38d5c6453cf2fcfde631 -->
## `test_render_for_agent_omits_frontmatter_when_no_agent_keys()`

Assert that `render_for_agent` suppresses the entire front-matter block when only internal keys are present, while still emitting section bodies.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_render_for_agent_empty_input fingerprint=cb071367cdb29133f48c3cb017fcdfe0b91718366df0e6889cb7019b8000b292 body_fp=cd348fe2c505c0fa7a152f000eda77d8e3d1a9c1cc909178d74c21199f8414be source_ref=da68e1ccc1166d342f5b38d5c6453cf2fcfde631 -->
## `test_render_for_agent_empty_input()`

Assert that `render_for_agent` returns an empty string given empty input.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_render_for_agent_prose_only_no_sentinels fingerprint=15f31ad9e89445f42fad2dbafa59d52888fd7a5e00d9285756b45de6ab7361ec body_fp=81eb18c603244650c850d732a96362501aee4fa2a7ecc35dc004727b7a5772b7 source_ref=da68e1ccc1166d342f5b38d5c6453cf2fcfde631 -->
## `test_render_for_agent_prose_only_no_sentinels()`

Verify `render_for_agent` passes through plain prose with no frontmatter or sentinels unchanged.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_agent_front_matter_keys_constant fingerprint=64acc40a3816c88839dddb297dcc73231822240b25e6f37b53bd7d0d3808e85b body_fp=3ca069e2fe9131784f737930205158c643e3257f790d00e09a7a580f3da4c94d source_ref=da68e1ccc1166d342f5b38d5c6453cf2fcfde631 -->
## `test_agent_front_matter_keys_constant()`

Assert that `AGENT_FRONT_MATTER_KEYS` contains exactly `description`, `defines`, `incoming_refs`, and `outgoing_refs`.
<!-- trie:end -->