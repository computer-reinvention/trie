---
trie_version: 0.1.0
source: tests/test_writer_sentinels.py
file_fingerprint: 78bcdf1f6941eb3b9dbc31bc2eb2eac4117ee2c9e40d6919ac2ca68cf9dfee4b
last_synced_at: '2026-05-12T18:22:16Z'
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

<!-- trie:section symbol=tests/test_writer_sentinels:test_parse_only_prose fingerprint=331924321c90bdde87c44e245a991131e979fb23776f4a7721c5a5572534e1e5 body_fp=5e1f5f72adb37689bb65b15e7607a288511ac94fce2eb256b63ebe31994a3af7 -->
## `test_parse_only_prose()`

Assert that a prose-only string parses into a single `Prose` chunk with no front matter.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_writer_sentinels:test_parse_front_matter_only fingerprint=91f029ba0079c8e4ae6b734bc86ac1fa3370f9847fce9a27aa86e8670f840489 body_fp=533945a8e2a8214eea1c78af9009709887046ad676be8cef9e1642515139b747 -->
## `test_parse_front_matter_only()`

Assert that `TriefactFile.parse` correctly extracts nested YAML front matter and leaves `chunks` empty when no body follows.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_writer_sentinels:test_parse_front_matter_and_prose fingerprint=9e2c997d2a34eb82a33d8cfe52afc4f0c73fa88d5d72f401546d8db3d7ee99bd body_fp=f954ee005e01e068325eaa061f9a81a684d74cc84e0a7c513273d3da62d8ebce -->
## `test_parse_front_matter_and_prose()`

Assert that `TriefactFile.parse` correctly splits a file with both front matter and body prose into metadata and a single `Prose` chunk.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_writer_sentinels:test_parse_single_section fingerprint=7bdcd4d0a5afb4d45f87aafa45570e49e973a0a2f15cd10a5ec36a352d5ce027 body_fp=da94a6c2f9ec79f99f5f527c49eafa81f78701ca2bba7875d41f4b426f6c2dad -->
## `test_parse_single_section()`

Assert that a file with prose before a sentinel block parses into three chunks: leading prose, one `Section`, and trailing newline prose.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_writer_sentinels:test_parse_multiple_sections_with_prose_between fingerprint=f6ce3fc57be98792327d599972b5ecd77f34b1e63c1092f5b2dd3cddb226c760 body_fp=74e77f41c0d2a776e8bae5e7f44cb5c6843ede1c7daac515852f11ecd01822bb -->
## `test_parse_multiple_sections_with_prose_between()`

Verify that `TriefactFile.parse` correctly extracts multiple sections and preserves interleaved human prose as `Prose` chunks.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_writer_sentinels:test_parse_unterminated_section_raises fingerprint=063145f59bcc49bb9b1b79d2a1d6264e0e39c21c108518ba7fd457ab92caeee7 body_fp=2a862355d74808f59a1f647217769a70c7c85c9e84cf123da3c275005babd292 -->
## `test_parse_unterminated_section_raises()`

Assert that `TriefactFile.parse` raises `ValueError` matching "Unterminated" when a section sentinel has no closing `<!-- trie:end -->`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_writer_sentinels:test_roundtrip_only_prose_is_byte_identical fingerprint=df3b26580aea061ee81a45fe4621020dde3e094d6c40ce016f480af7b900a516 body_fp=44a94e7e40e08a39f9a705a470f63a8663bf32c45dac4cefca34e149c82d8687 -->
## `test_roundtrip_only_prose_is_byte_identical()`

Assert that parsing and re-rendering a prose-only triefact file produces identical bytes.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_writer_sentinels:test_roundtrip_with_front_matter_and_section_carrying_body_fp fingerprint=ecddcc86d932d0ecd4e46b4786a5c522f7caf49e59c7be9e14d65843fd2a8305 body_fp=8b4b50207c2326777ce13f85ca23b8dbd4ae3b809962c9465e5490cbae5274cc -->
## `test_roundtrip_with_front_matter_and_section_carrying_body_fp()`

Assert that a triefact file with front matter and a section including `body_fp` renders back to the original string unchanged.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_writer_sentinels:test_roundtrip_multiple_sections_with_human_prose fingerprint=747ba03c7824c21923141c4f7e0bd804cdd4ccd6161d13f903335e8f5754005f body_fp=6b584a7342483575dbedf544af64e81aee57985ba220254cc34c97933bba8222 -->
## `test_roundtrip_multiple_sections_with_human_prose()`

Verify that a file with front matter, two generated sections, and human prose between them renders back to the original text unchanged.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_writer_sentinels:test_legacy_section_without_body_fp_parses_and_promotes_on_render fingerprint=3d551abb1de02f543f89b4091b9bdaf94c5edcc2a03992514d4aae68b274631b body_fp=6f7c96827459d05724ada579852d3247c04863057cd0fde1a280649abe6ae76a -->
## `test_legacy_section_without_body_fp_parses_and_promotes_on_render()`

Verify that sections lacking `body_fp=` parse successfully and gain a computed `body_fp` on render.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_writer_sentinels:test_upsert_replaces_existing_section_preserves_prose fingerprint=19a03d771f37ccebe0c9d67628c683d99fa717c1c963166cafa7d0859553576e body_fp=34162d92fb9863b1be2e9a01438c5457ff820899154fd761dbfd45e77c3a846e -->
## `test_upsert_replaces_existing_section_preserves_prose()`

Assert that `upsert_section` replaces a named section's fingerprint and body while leaving all surrounding prose and other sections intact.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_writer_sentinels:test_upsert_appends_new_section_at_end fingerprint=f46e868629972d796c1d951ac91a82caf93691abf250b29a829bebca43a621e7 body_fp=b70248becf017e05597c2dbe9f5ca5a493891da6d1b93136a1a7cecf5debec40 -->
## `test_upsert_appends_new_section_at_end()`

Verify that upserting a new section into a file appends it after existing prose with correct sentinels and `body_fp`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_writer_sentinels:test_upsert_into_empty_triefact fingerprint=b200e282fd6690ffd6583614228337a8a80a1e9ab19c61f402dee458246bcbdc body_fp=5bf581818a055043b50c60a7f77649516c44ed1728c20ddb55b386589f7fe9a5 -->
## `test_upsert_into_empty_triefact()`

Assert that upserting a section into an empty `TriefactFile` produces the correct sentinel-wrapped output with a computed `body_fp`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_writer_sentinels:test_remove_section fingerprint=78873ffb894ceac24648f6c7604b3eac9c238c94e8e3bcd401c464fc19b3808f body_fp=61904d69a78d3d49a0ab0cc838e3e7732ac1a47a541843596523aec033fbb3ef -->
## `test_remove_section()`

Verify that removing an existing section eliminates its content while preserving all other sections and prose.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_writer_sentinels:test_remove_missing_section_returns_false fingerprint=c89aedc0fb3b0f51faaae6fe50764356bc95a44a39d673c4a6757783e5f28b02 body_fp=98663a55aba86d049d977be95aa63513dd93e23dc61c99539d85956a115827b8 -->
## `test_remove_missing_section_returns_false()`

Assert that `remove_section` returns `False` when the qualified name is absent.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_writer_sentinels:test_section_qnames_in_order fingerprint=10e2d7e908cfea7610110e6a1aefa33470549e453459ae19945abb75daee457e body_fp=273e3091e4c7499bdbcbbfe961d964cc2e8ce8c98e43078160fb50f102a4b5e7 -->
## `test_section_qnames_in_order()`

Verify that `section_qnames()` returns qualified names in document order.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_writer_sentinels:test_human_edit_between_sections_survives_regen fingerprint=637b8c3ecd5d200c81d0b607862a0c940a6aec82afe722036a94505b536cd185 body_fp=9fc73e71418ab67eb03811cbefcb769e6abe6bb4c9f51aaee076c61442679cc9 -->
## `test_human_edit_between_sections_survives_regen()`

Assert that hand-written prose between generated sections is preserved after upserting a section.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_writer_sentinels:test_front_matter_re_renders_in_insertion_order fingerprint=f3b23aacaca01c7bfb901f9c0898c65335b3e98a726c10478618ccb4e61257c4 body_fp=c0ad8e71aa0967545cdcecdf4f43fd36ec361f0d2e8be27a4ace9a89960e3575 -->
## `test_front_matter_re_renders_in_insertion_order()`

Assert that front-matter keys render in their original insertion order after a parse-render round-trip.
<!-- trie:end -->