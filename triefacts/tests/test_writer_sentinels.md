---
trie_version: 0.1.0
source: tests/test_writer_sentinels.py
file_fingerprint: 78bcdf1f6941eb3b9dbc31bc2eb2eac4117ee2c9e40d6919ac2ca68cf9dfee4b
last_synced_at: '2026-05-14T17:51:25Z'
defines:
- kind: function
  qualified_name: tests/test_writer_sentinels:test_parse_empty
  lines: 10-13
- kind: function
  qualified_name: tests/test_writer_sentinels:test_parse_only_prose
  lines: 16-21
- kind: function
  qualified_name: tests/test_writer_sentinels:test_parse_front_matter_only
  lines: 24-28
- kind: function
  qualified_name: tests/test_writer_sentinels:test_parse_front_matter_and_prose
  lines: 31-37
- kind: function
  qualified_name: tests/test_writer_sentinels:test_parse_single_section
  lines: 40-59
- kind: function
  qualified_name: tests/test_writer_sentinels:test_parse_multiple_sections_with_prose_between
  lines: 62-77
- kind: function
  qualified_name: tests/test_writer_sentinels:test_parse_unterminated_section_raises
  lines: 80-83
- kind: function
  qualified_name: tests/test_writer_sentinels:test_roundtrip_only_prose_is_byte_identical
  lines: 89-91
- kind: function
  qualified_name: tests/test_writer_sentinels:test_roundtrip_with_front_matter_and_section_carrying_body_fp
  lines: 94-108
- kind: function
  qualified_name: tests/test_writer_sentinels:test_roundtrip_multiple_sections_with_human_prose
  lines: 111-130
- kind: function
  qualified_name: tests/test_writer_sentinels:test_legacy_section_without_body_fp_parses_and_promotes_on_render
  lines: 133-143
- kind: function
  qualified_name: tests/test_writer_sentinels:test_upsert_replaces_existing_section_preserves_prose
  lines: 149-172
- kind: function
  qualified_name: tests/test_writer_sentinels:test_upsert_appends_new_section_at_end
  lines: 175-183
- kind: function
  qualified_name: tests/test_writer_sentinels:test_upsert_into_empty_triefact
  lines: 186-194
- kind: function
  qualified_name: tests/test_writer_sentinels:test_remove_section
  lines: 197-214
- kind: function
  qualified_name: tests/test_writer_sentinels:test_remove_missing_section_returns_false
  lines: 217-219
- kind: function
  qualified_name: tests/test_writer_sentinels:test_section_qnames_in_order
  lines: 222-229
- kind: function
  qualified_name: tests/test_writer_sentinels:test_human_edit_between_sections_survives_regen
  lines: 235-266
- kind: function
  qualified_name: tests/test_writer_sentinels:test_front_matter_re_renders_in_insertion_order
  lines: 269-275
incoming_refs: 0
outgoing_refs: 31
---
<!-- trie:section symbol=tests/test_writer_sentinels:test_parse_empty fingerprint=d8d478032b2edcb69bfa32426a508c57ca253f274418d1d9533ca54ff39decf9 body_fp=34b4251823ed55374e4781200909b230e152984d7df6604868d11b34aa9935fb -->
## `test_parse_empty()`

Assert that parsing an empty string yields an empty `TriefactFile` with no front matter and no chunks.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_writer_sentinels:test_parse_only_prose fingerprint=331924321c90bdde87c44e245a991131e979fb23776f4a7721c5a5572534e1e5 body_fp=90fb2d7185595ca5688a8394c138ba9346a75de969d48544f945f85a7812cfe2 -->
## `test_parse_only_prose()`

Assert that a plain Markdown string with no sentinels parses into a single `Prose` chunk with the original text.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_writer_sentinels:test_parse_front_matter_only fingerprint=91f029ba0079c8e4ae6b734bc86ac1fa3370f9847fce9a27aa86e8670f840489 body_fp=f40c49af6de2805fdcfae3aa7fdeef6f2f16a8341eaf659d191d96096ce0fd64 -->
## `test_parse_front_matter_only()`

Assert that a YAML front-matter-only input parses to the correct dict with no content chunks.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_writer_sentinels:test_parse_front_matter_and_prose fingerprint=9e2c997d2a34eb82a33d8cfe52afc4f0c73fa88d5d72f401546d8db3d7ee99bd body_fp=5689a7e3a6a410849c9f324bf46c8efc522067ede51acef9ec2ff221d62ccd3e -->
## `test_parse_front_matter_and_prose()`

Verify that a file with YAML front matter followed by Markdown prose parses into one `Prose` chunk with correct text.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_writer_sentinels:test_parse_single_section fingerprint=7bdcd4d0a5afb4d45f87aafa45570e49e973a0a2f15cd10a5ec36a352d5ce027 body_fp=ea0765b3d7c33bcad1d0d8ac844a4bd2ee1a2a633503ffce09d42b8d65ad8376 -->
## `test_parse_single_section()`

Assert that a file with leading prose and one sentinel-wrapped section parses into exactly three chunks with correct metadata and body.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_writer_sentinels:test_parse_multiple_sections_with_prose_between fingerprint=f6ce3fc57be98792327d599972b5ecd77f34b1e63c1092f5b2dd3cddb226c760 body_fp=91a848f9073fe91bdfc97438b57a86a2069bf366cbf59f916e480b63e00bdae5 -->
## `test_parse_multiple_sections_with_prose_between()`

Verify that `TriefactFile.parse` correctly identifies multiple sections and preserves interleaved human prose chunks.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_writer_sentinels:test_parse_unterminated_section_raises fingerprint=063145f59bcc49bb9b1b79d2a1d6264e0e39c21c108518ba7fd457ab92caeee7 body_fp=2a862355d74808f59a1f647217769a70c7c85c9e84cf123da3c275005babd292 -->
## `test_parse_unterminated_section_raises()`

Assert that `TriefactFile.parse` raises `ValueError` matching "Unterminated" when a section sentinel has no closing `<!-- trie:end -->`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_writer_sentinels:test_roundtrip_only_prose_is_byte_identical fingerprint=df3b26580aea061ee81a45fe4621020dde3e094d6c40ce016f480af7b900a516 body_fp=c38f7911b1c262d574056a36887dc4f71f6852b471b5fa68a429b5e6d89b1002 -->
## `test_roundtrip_only_prose_is_byte_identical()`

Assert that parsing and re-rendering a prose-only triefact file produces byte-identical output.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_writer_sentinels:test_roundtrip_with_front_matter_and_section_carrying_body_fp fingerprint=ecddcc86d932d0ecd4e46b4786a5c522f7caf49e59c7be9e14d65843fd2a8305 body_fp=49ba7415303a3b956d04b12c47ef5f2892168ee256ac33d2901cb2b966500fec -->
## `test_roundtrip_with_front_matter_and_section_carrying_body_fp()`

Assert that a triefact file containing front matter and a section with `body_fp` renders byte-identically to its source.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_writer_sentinels:test_roundtrip_multiple_sections_with_human_prose fingerprint=747ba03c7824c21923141c4f7e0bd804cdd4ccd6161d13f903335e8f5754005f body_fp=cbce3c4c87671ee11a1502d89cf6813d2cb67b13d0fc829f6b2c021bd3b92554 -->
## `test_roundtrip_multiple_sections_with_human_prose()`

Verify that a file with front matter, two generated sections, and interleaved hand-written prose renders back byte-identically.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_writer_sentinels:test_legacy_section_without_body_fp_parses_and_promotes_on_render fingerprint=3d551abb1de02f543f89b4091b9bdaf94c5edcc2a03992514d4aae68b274631b body_fp=6f7c96827459d05724ada579852d3247c04863057cd0fde1a280649abe6ae76a -->
## `test_legacy_section_without_body_fp_parses_and_promotes_on_render()`

Verify that sections lacking `body_fp=` parse successfully and gain a computed `body_fp` on render.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_writer_sentinels:test_upsert_replaces_existing_section_preserves_prose fingerprint=19a03d771f37ccebe0c9d67628c683d99fa717c1c963166cafa7d0859553576e body_fp=3024424d8ca2f063a2c23705a289e305249fc5c9016f4a58dbbaf27917171308 -->
## `test_upsert_replaces_existing_section_preserves_prose()`

Assert that `upsert_section` replaces a target section's fingerprint and body while leaving all prose chunks and other sections unchanged.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_writer_sentinels:test_upsert_appends_new_section_at_end fingerprint=f46e868629972d796c1d951ac91a82caf93691abf250b29a829bebca43a621e7 body_fp=bc748fa2fd25397bf0d46238eb0a847716879ad8bc3e94ae56ce20118b7b0752 -->
## `test_upsert_appends_new_section_at_end()`

Assert that `upsert_section` appends a new section after existing prose when no matching section exists.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_writer_sentinels:test_upsert_into_empty_triefact fingerprint=b200e282fd6690ffd6583614228337a8a80a1e9ab19c61f402dee458246bcbdc body_fp=4ca2efd288985193a69ab35c41c7c72953b98dd11c9045eb146790eb52ff3383 -->
## `test_upsert_into_empty_triefact()`

Assert that upserting a section into an empty `TriefactFile` renders the correct sentinel-wrapped output with a computed `body_fp`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_writer_sentinels:test_remove_section fingerprint=78873ffb894ceac24648f6c7604b3eac9c238c94e8e3bcd401c464fc19b3808f body_fp=4f102122cb19342a27f16b28cac23002e52f75572b189dfe1ff4bfb4acc63f3d -->
## `test_remove_section()`

Verify that removing an existing section erases it and its body while preserving all other sections and prose.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_writer_sentinels:test_remove_missing_section_returns_false fingerprint=c89aedc0fb3b0f51faaae6fe50764356bc95a44a39d673c4a6757783e5f28b02 body_fp=1e0f228472f4d6fd580b01be5375f2efcada116f809c566ba52381d2e52c4143 -->
## `test_remove_missing_section_returns_false()`

Assert that `remove_section` returns `False` when the named symbol does not exist in the file.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_writer_sentinels:test_section_qnames_in_order fingerprint=10e2d7e908cfea7610110e6a1aefa33470549e453459ae19945abb75daee457e body_fp=ffbd980c883f5f10125b397cb62accb6ebce336715df2c00e118b4800c18b23a -->
## `test_section_qnames_in_order()`

Assert that `section_qnames()` returns qualified names in document order, not sorted order.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_writer_sentinels:test_human_edit_between_sections_survives_regen fingerprint=637b8c3ecd5d200c81d0b607862a0c940a6aec82afe722036a94505b536cd185 body_fp=342c64a2c0d31f0cea0fe8937ce239d61b909523cf2e93e5f60eaf78ec66c83e -->
## `test_human_edit_between_sections_survives_regen()`

Assert that hand-written prose between generated sections is preserved after upserting a regenerated section.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_writer_sentinels:test_front_matter_re_renders_in_insertion_order fingerprint=f3b23aacaca01c7bfb901f9c0898c65335b3e98a726c10478618ccb4e61257c4 body_fp=c0ad8e71aa0967545cdcecdf4f43fd36ec361f0d2e8be27a4ace9a89960e3575 -->
## `test_front_matter_re_renders_in_insertion_order()`

Assert that front-matter keys render in their original insertion order after a parse-render round-trip.
<!-- trie:end -->