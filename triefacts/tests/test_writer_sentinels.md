---
trie_version: 0.1.0
source: tests/test_writer_sentinels.py
file_fingerprint: 78bcdf1f6941eb3b9dbc31bc2eb2eac4117ee2c9e40d6919ac2ca68cf9dfee4b
last_synced_at: '2026-05-14T17:19:36Z'
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
<!-- trie:section symbol=tests/test_writer_sentinels:test_parse_empty fingerprint=d8d478032b2edcb69bfa32426a508c57ca253f274418d1d9533ca54ff39decf9 body_fp=0d95947135b774448a353a25eda4989fc50c0825a958d2b7f8da62fcfb6ed21e -->
## `test_parse_empty()`

Assert that parsing an empty string yields empty front matter and no chunks.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_writer_sentinels:test_parse_only_prose fingerprint=331924321c90bdde87c44e245a991131e979fb23776f4a7721c5a5572534e1e5 body_fp=1f88397bf5d387117d7ec9630f50ff8c0dcd0c3349b08ac132a46824c8e06e24 -->
## `test_parse_only_prose()`

Assert that a plain Markdown string with no sentinels parses into a single `Prose` chunk with identical text.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_writer_sentinels:test_parse_front_matter_only fingerprint=91f029ba0079c8e4ae6b734bc86ac1fa3370f9847fce9a27aa86e8670f840489 body_fp=4d065c96fbf004cbdb934e6e6cacebe86752cf70d9ac90c939dd6a38fb10ae84 -->
## `test_parse_front_matter_only()`

Assert that a YAML front-matter-only input parses to the correct dict with no chunks.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_writer_sentinels:test_parse_front_matter_and_prose fingerprint=9e2c997d2a34eb82a33d8cfe52afc4f0c73fa88d5d72f401546d8db3d7ee99bd body_fp=44ecd75451d644a7c54ed8d5345013a37aff2c2b7b2d3c9779df1bd1d55b3fb3 -->
## `test_parse_front_matter_and_prose()`

Verify that a file with both YAML front matter and prose body parses into correct front matter dict and a single `Prose` chunk.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_writer_sentinels:test_parse_single_section fingerprint=7bdcd4d0a5afb4d45f87aafa45570e49e973a0a2f15cd10a5ec36a352d5ce027 body_fp=26f0674ecebcc72daf0ff9ef9a29f4b4397c050a609796c5c7c760d1227f8e02 -->
## `test_parse_single_section()`

Assert that a single sentinel-wrapped section parses into exactly three chunks: leading prose, a `Section`, and trailing prose.

- `Section.body` excludes the opening and closing sentinel lines.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_writer_sentinels:test_parse_multiple_sections_with_prose_between fingerprint=f6ce3fc57be98792327d599972b5ecd77f34b1e63c1092f5b2dd3cddb226c760 body_fp=93eedd0099ae5086d716972461b24321093a12f8a9e0083a27cae0d701ed10ba -->
## `test_parse_multiple_sections_with_prose_between()`

Assert that `TriefactFile.parse` correctly identifies multiple sections and preserves prose chunks between them.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_writer_sentinels:test_parse_unterminated_section_raises fingerprint=063145f59bcc49bb9b1b79d2a1d6264e0e39c21c108518ba7fd457ab92caeee7 body_fp=ba3787efa0fe033ea568747840f1432e3fd4922c9faa90f99c4e883afca458fd -->
## `test_parse_unterminated_section_raises()`

Assert that `TriefactFile.parse` raises `ValueError` matching "Unterminated" when a section sentinel lacks a closing `<!-- trie:end -->`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_writer_sentinels:test_roundtrip_only_prose_is_byte_identical fingerprint=df3b26580aea061ee81a45fe4621020dde3e094d6c40ce016f480af7b900a516 body_fp=f36d44e874648fe53a43d39f7ea5c41dee931396b0a724a23a2c4178af9176e5 -->
## `test_roundtrip_only_prose_is_byte_identical()`

Assert that parsing and re-rendering a prose-only triefact produces byte-identical output.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_writer_sentinels:test_roundtrip_with_front_matter_and_section_carrying_body_fp fingerprint=ecddcc86d932d0ecd4e46b4786a5c522f7caf49e59c7be9e14d65843fd2a8305 body_fp=9b2dcb5ce6d6fbdcc4bc45341875e394d15318ba30c956beaea9708016ef58df -->
## `test_roundtrip_with_front_matter_and_section_carrying_body_fp()`

Assert that a `TriefactFile` with front matter and a section including `body_fp` renders byte-identically to its source text.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_writer_sentinels:test_roundtrip_multiple_sections_with_human_prose fingerprint=747ba03c7824c21923141c4f7e0bd804cdd4ccd6161d13f903335e8f5754005f body_fp=939967bf6555d1736933e2ac3dbdef71b16704f2ceeb5ee83f282cdd6dbe23cb -->
## `test_roundtrip_multiple_sections_with_human_prose()`

Assert that a file with front matter, two generated sections, and hand-written prose between them renders byte-identically after parsing.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_writer_sentinels:test_legacy_section_without_body_fp_parses_and_promotes_on_render fingerprint=3d551abb1de02f543f89b4091b9bdaf94c5edcc2a03992514d4aae68b274631b body_fp=2859f22abeb1bfb0d865f891cf595ff74de80694ba801713253a267cfed48731 -->
## `test_legacy_section_without_body_fp_parses_and_promotes_on_render()`

Assert that sections lacking `body_fp=` parse without error and gain a computed `body_fp` on render.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_writer_sentinels:test_upsert_replaces_existing_section_preserves_prose fingerprint=19a03d771f37ccebe0c9d67628c683d99fa717c1c963166cafa7d0859553576e body_fp=c947f0a3b3c3848d5729cbe076d3f7806a8f5c5a8c6904082a15c09f09f6180f -->
## `test_upsert_replaces_existing_section_preserves_prose()`

Assert that `upsert_section` replaces the target section's fingerprint and body while leaving all prose chunks and other sections intact.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_writer_sentinels:test_upsert_appends_new_section_at_end fingerprint=f46e868629972d796c1d951ac91a82caf93691abf250b29a829bebca43a621e7 body_fp=a2d934c164bc9ab5998f5675b4072df04a9dbfc48786fdf4e1fb68ca27227d67 -->
## `test_upsert_appends_new_section_at_end()`

Assert that `upsert_section` appends a new section after existing prose, with correct sentinel and `body_fp`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_writer_sentinels:test_upsert_into_empty_triefact fingerprint=b200e282fd6690ffd6583614228337a8a80a1e9ab19c61f402dee458246bcbdc body_fp=cd990fd03f4be9ea3ffbc5840d61f6d0df9bb940b3ffc5b2d81ee3eae1ddf6dd -->
## `test_upsert_into_empty_triefact()`

Verify that upserting a section into an empty `TriefactFile` produces a correctly formatted sentinel block with `body_fp`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_writer_sentinels:test_remove_section fingerprint=78873ffb894ceac24648f6c7604b3eac9c238c94e8e3bcd401c464fc19b3808f body_fp=cd613a7dba643838068313a658da9946bd6c5a2479d7bef1b1d0fafe9a25751e -->
## `test_remove_section()`

Verify that removing an existing section by qualified name erases its sentinel block while preserving surrounding prose and other sections.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_writer_sentinels:test_remove_missing_section_returns_false fingerprint=c89aedc0fb3b0f51faaae6fe50764356bc95a44a39d673c4a6757783e5f28b02 body_fp=1e0f228472f4d6fd580b01be5375f2efcada116f809c566ba52381d2e52c4143 -->
## `test_remove_missing_section_returns_false()`

Assert that `remove_section` returns `False` when the named symbol does not exist in the file.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_writer_sentinels:test_section_qnames_in_order fingerprint=10e2d7e908cfea7610110e6a1aefa33470549e453459ae19945abb75daee457e body_fp=ffbd980c883f5f10125b397cb62accb6ebce336715df2c00e118b4800c18b23a -->
## `test_section_qnames_in_order()`

Assert that `section_qnames()` returns qualified names in document order, not sorted order.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_writer_sentinels:test_human_edit_between_sections_survives_regen fingerprint=637b8c3ecd5d200c81d0b607862a0c940a6aec82afe722036a94505b536cd185 body_fp=c8103f239dbdb60699d9b27106e30942c5035b936bcfb111064b06d79e04c647 -->
## `test_human_edit_between_sections_survives_regen()`

Assert that hand-written prose between generated sections is preserved after `upsert_section` regenerates one of them.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_writer_sentinels:test_front_matter_re_renders_in_insertion_order fingerprint=f3b23aacaca01c7bfb901f9c0898c65335b3e98a726c10478618ccb4e61257c4 body_fp=8ecb33e8ec078f74fbb8180b3536deaf15b43e04d38fb9e6072b8769e9f5bf7d -->
## `test_front_matter_re_renders_in_insertion_order()`

Assert that front matter keys render in their original insertion order after a parse/render round-trip.
<!-- trie:end -->