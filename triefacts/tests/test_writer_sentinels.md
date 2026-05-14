---
trie_version: 0.1.0
source: tests/test_writer_sentinels.py
file_fingerprint: e644dfe8b6ae9b4b2a3df7889ddea50b0db07fdc7d47bea43a8cf001b3704a8c
last_synced_at: '2026-05-14T19:38:37Z'
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
  qualified_name: tests/test_writer_sentinels:test_section_round_trips_source_ref
  lines: 146-160
- kind: function
  qualified_name: tests/test_writer_sentinels:test_section_without_source_ref_renders_without_it
  lines: 163-170
- kind: function
  qualified_name: tests/test_writer_sentinels:test_section_with_source_ref_renders_field_in_stable_position
  lines: 173-188
- kind: function
  qualified_name: tests/test_writer_sentinels:test_section_legacy_format_with_source_ref_appended_parses
  lines: 191-205
- kind: function
  qualified_name: tests/test_writer_sentinels:test_upsert_replaces_existing_section_preserves_prose
  lines: 211-234
- kind: function
  qualified_name: tests/test_writer_sentinels:test_upsert_appends_new_section_at_end
  lines: 237-245
- kind: function
  qualified_name: tests/test_writer_sentinels:test_upsert_into_empty_triefact
  lines: 248-256
- kind: function
  qualified_name: tests/test_writer_sentinels:test_remove_section
  lines: 259-276
- kind: function
  qualified_name: tests/test_writer_sentinels:test_remove_missing_section_returns_false
  lines: 279-281
- kind: function
  qualified_name: tests/test_writer_sentinels:test_section_qnames_in_order
  lines: 284-291
- kind: function
  qualified_name: tests/test_writer_sentinels:test_human_edit_between_sections_survives_regen
  lines: 297-328
- kind: function
  qualified_name: tests/test_writer_sentinels:test_front_matter_re_renders_in_insertion_order
  lines: 331-337
incoming_refs: 0
outgoing_refs: 38
---
<!-- trie:section symbol=tests/test_writer_sentinels:test_parse_empty fingerprint=d8d478032b2edcb69bfa32426a508c57ca253f274418d1d9533ca54ff39decf9 body_fp=0d95947135b774448a353a25eda4989fc50c0825a958d2b7f8da62fcfb6ed21e source_ref=abe160a19a920121281b497414b5215598b904f7 -->
## `test_parse_empty()`

Assert that parsing an empty string yields empty front matter and no chunks.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_writer_sentinels:test_parse_only_prose fingerprint=331924321c90bdde87c44e245a991131e979fb23776f4a7721c5a5572534e1e5 body_fp=389882879064fbccf1b0a358da344f7cd06ff7ee9314f8b971dd5de6b48a7993 source_ref=abe160a19a920121281b497414b5215598b904f7 -->
## `test_parse_only_prose()`

Assert that a plain Markdown string with no front matter parses into a single `Prose` chunk with identical text.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_writer_sentinels:test_parse_front_matter_only fingerprint=91f029ba0079c8e4ae6b734bc86ac1fa3370f9847fce9a27aa86e8670f840489 body_fp=4d065c96fbf004cbdb934e6e6cacebe86752cf70d9ac90c939dd6a38fb10ae84 source_ref=abe160a19a920121281b497414b5215598b904f7 -->
## `test_parse_front_matter_only()`

Assert that a YAML front-matter-only input parses to the correct dict with no chunks.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_writer_sentinels:test_parse_front_matter_and_prose fingerprint=9e2c997d2a34eb82a33d8cfe52afc4f0c73fa88d5d72f401546d8db3d7ee99bd body_fp=30aad2b6bc9e6a60a5e9fc77bde129787395e25d42d12ad53d3fd81d1fc14501 source_ref=abe160a19a920121281b497414b5215598b904f7 -->
## `test_parse_front_matter_and_prose()`

Assert that `TriefactFile.parse` correctly separates YAML front matter from subsequent Markdown prose into one `Prose` chunk.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_writer_sentinels:test_parse_single_section fingerprint=7bdcd4d0a5afb4d45f87aafa45570e49e973a0a2f15cd10a5ec36a352d5ce027 body_fp=eaf2d908fb9ceba2d866a71a224de619c6f9fdb157dec5b9294e313b32dddaf8 source_ref=abe160a19a920121281b497414b5215598b904f7 -->
## `test_parse_single_section()`

Verify that a file with leading prose, one sentinel-wrapped section, and a trailing newline parses into exactly three chunks with correct metadata and body.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_writer_sentinels:test_parse_multiple_sections_with_prose_between fingerprint=f6ce3fc57be98792327d599972b5ecd77f34b1e63c1092f5b2dd3cddb226c760 body_fp=1490e8c357787b0b0f245eb80bcbd359e4ef573cb4de2a40f25352dcbe24bfb1 source_ref=abe160a19a920121281b497414b5215598b904f7 -->
## `test_parse_multiple_sections_with_prose_between()`

Verify that multiple sections with intervening prose each parse into correct `Section` chunks with prose chunks preserved between them.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_writer_sentinels:test_parse_unterminated_section_raises fingerprint=063145f59bcc49bb9b1b79d2a1d6264e0e39c21c108518ba7fd457ab92caeee7 body_fp=39c8c88f3d43bd672027d9211eaf1ac90989d9003863d4a9cae315db71f9b915 source_ref=abe160a19a920121281b497414b5215598b904f7 -->
## `test_parse_unterminated_section_raises()`

Assert that `TriefactFile.parse` raises `ValueError` when a section sentinel has no closing `<!-- trie:end -->`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_writer_sentinels:test_roundtrip_only_prose_is_byte_identical fingerprint=df3b26580aea061ee81a45fe4621020dde3e094d6c40ce016f480af7b900a516 body_fp=f36d44e874648fe53a43d39f7ea5c41dee931396b0a724a23a2c4178af9176e5 source_ref=abe160a19a920121281b497414b5215598b904f7 -->
## `test_roundtrip_only_prose_is_byte_identical()`

Assert that parsing and re-rendering a prose-only triefact produces byte-identical output.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_writer_sentinels:test_roundtrip_with_front_matter_and_section_carrying_body_fp fingerprint=ecddcc86d932d0ecd4e46b4786a5c522f7caf49e59c7be9e14d65843fd2a8305 body_fp=5924084bc7848bd3ae2e800153313c8262970eb22a300d503575400e813373f2 source_ref=abe160a19a920121281b497414b5215598b904f7 -->
## `test_roundtrip_with_front_matter_and_section_carrying_body_fp()`

Verify that a triefact file with YAML front matter and a section including `body_fp=` renders byte-identically after parse.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_writer_sentinels:test_roundtrip_multiple_sections_with_human_prose fingerprint=747ba03c7824c21923141c4f7e0bd804cdd4ccd6161d13f903335e8f5754005f body_fp=2a1e657342ee8360704bcdd39d13afa9956073ec7391b579053484d14d3c52a1 source_ref=abe160a19a920121281b497414b5215598b904f7 -->
## `test_roundtrip_multiple_sections_with_human_prose()`

Verify that a file with front matter, two generated sections, and hand-written prose between them round-trips byte-identically through parse and render.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_writer_sentinels:test_legacy_section_without_body_fp_parses_and_promotes_on_render fingerprint=3d551abb1de02f543f89b4091b9bdaf94c5edcc2a03992514d4aae68b274631b body_fp=b5bd8356cf450e81f8d1ce66863d47441c66089952140852fbbdb562d730fdde source_ref=abe160a19a920121281b497414b5215598b904f7 -->
## `test_legacy_section_without_body_fp_parses_and_promotes_on_render()`

Verify that sections lacking `body_fp=` parse successfully and gain a computed `body_fp=` on render.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_writer_sentinels:test_upsert_replaces_existing_section_preserves_prose fingerprint=19a03d771f37ccebe0c9d67628c683d99fa717c1c963166cafa7d0859553576e body_fp=e853d1dae5e766382e7ea4d0239c20dac7dd3854da79f1ccec81439f9cfdd1b8 source_ref=abe160a19a920121281b497414b5215598b904f7 -->
## `test_upsert_replaces_existing_section_preserves_prose()`

Assert that upserting an existing section updates only that section while leaving all prose and sibling sections untouched.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_writer_sentinels:test_upsert_appends_new_section_at_end fingerprint=f46e868629972d796c1d951ac91a82caf93691abf250b29a829bebca43a621e7 body_fp=147c69316e095124a3b8a26eeefaff91a5b452447788a558073bfa7b64ff2e53 source_ref=abe160a19a920121281b497414b5215598b904f7 -->
## `test_upsert_appends_new_section_at_end()`

Assert that upserting a new section into a file with existing prose appends the section after the prose.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_writer_sentinels:test_upsert_into_empty_triefact fingerprint=b200e282fd6690ffd6583614228337a8a80a1e9ab19c61f402dee458246bcbdc body_fp=c8b43609fd514522e821e6795fb552a18a4a73942ada6944444fb34b3075266a source_ref=abe160a19a920121281b497414b5215598b904f7 -->
## `test_upsert_into_empty_triefact()`

Verify that upserting a section into an empty `TriefactFile` produces the correct sentinel-wrapped output with a computed `body_fp`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_writer_sentinels:test_remove_section fingerprint=78873ffb894ceac24648f6c7604b3eac9c238c94e8e3bcd401c464fc19b3808f body_fp=29304e065943e0f745a319dcb1a67f21f58bd4fc0649d89f54d5abbfa36d7167 source_ref=abe160a19a920121281b497414b5215598b904f7 -->
## `test_remove_section()`

Verify that removing an existing section deletes its sentinel and body while preserving other sections and prose.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_writer_sentinels:test_remove_missing_section_returns_false fingerprint=c89aedc0fb3b0f51faaae6fe50764356bc95a44a39d673c4a6757783e5f28b02 body_fp=1e0f228472f4d6fd580b01be5375f2efcada116f809c566ba52381d2e52c4143 source_ref=abe160a19a920121281b497414b5215598b904f7 -->
## `test_remove_missing_section_returns_false()`

Assert that `remove_section` returns `False` when the named symbol does not exist in the file.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_writer_sentinels:test_section_qnames_in_order fingerprint=10e2d7e908cfea7610110e6a1aefa33470549e453459ae19945abb75daee457e body_fp=4b0de566c7884ae4940ab5ef2bae42d261e0a148ab3ff0966c2e9cd6e12b4ccd source_ref=abe160a19a920121281b497414b5215598b904f7 -->
## `test_section_qnames_in_order()`

Assert that `section_qnames()` returns qualified names in document order.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_writer_sentinels:test_human_edit_between_sections_survives_regen fingerprint=637b8c3ecd5d200c81d0b607862a0c940a6aec82afe722036a94505b536cd185 body_fp=a5836be2dd22dfb68f9dd724df98a711d580a2214ecaea5fda6b52f26ca76c63 source_ref=abe160a19a920121281b497414b5215598b904f7 -->
## `test_human_edit_between_sections_survives_regen()`

Assert that hand-written prose between trie sections is preserved after regenerating one section via `upsert_section`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_writer_sentinels:test_front_matter_re_renders_in_insertion_order fingerprint=f3b23aacaca01c7bfb901f9c0898c65335b3e98a726c10478618ccb4e61257c4 body_fp=033fcc85046ff2419be59c18256d3288beed029a2d4c413efa766926fbb958e3 source_ref=abe160a19a920121281b497414b5215598b904f7 -->
## `test_front_matter_re_renders_in_insertion_order()`

Assert that front-matter keys render in their original insertion order after a parse–render round-trip.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_writer_sentinels:test_section_round_trips_source_ref fingerprint=17d9bcaee21703293bc05f945dd9313f83664d80a0aa68880985462bcc41567d body_fp=8e67a7b71f9d25457402d48bd4cc5794668c2ec4c6f657cefc76bfb3a6f14fde source_ref=abe160a19a920121281b497414b5215598b904f7 -->
## `test_section_round_trips_source_ref()`

Assert that `source_ref=` survives a parse → render round-trip byte-identically.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_writer_sentinels:test_section_without_source_ref_renders_without_it fingerprint=ced24b63d8df8fc990893b0c8875c8591785b2f502a0d7806e2cf5639da1c71d body_fp=32965baff16cee653fdd4a3e536a53ea808df351053967fbff07be6fa8c45368 source_ref=abe160a19a920121281b497414b5215598b904f7 -->
## `test_section_without_source_ref_renders_without_it()`

Assert that a newly upserted section with no `source_ref` renders without the `source_ref=` field but includes `fingerprint=` and `body_fp=`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_writer_sentinels:test_section_with_source_ref_renders_field_in_stable_position fingerprint=f1dd7d68b85cc31ae27153e352bbdfbc8753da8c427df4782bdacc769fc35acd body_fp=4cd6b04881564f490257d35c8fead289c3595c80bee954e0908051ba647aa9d3 source_ref=abe160a19a920121281b497414b5215598b904f7 -->
## `test_section_with_source_ref_renders_field_in_stable_position()`

Assert that sentinel fields render in stable order: `fingerprint=` before `body_fp=` before `source_ref=`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_writer_sentinels:test_section_legacy_format_with_source_ref_appended_parses fingerprint=b33af3cc09b68ba42953496ef544b7fc9a3bcdbbceda3c5ca7db3ccc7fca2390 body_fp=a791a8e9de7f3da47dcd526ac3603bc6f1be35dc97d7146c165325ceeeb1d426 source_ref=abe160a19a920121281b497414b5215598b904f7 -->
## `test_section_legacy_format_with_source_ref_appended_parses()`

Verify that a section with `source_ref=` but no `body_fp=` parses without error and exposes both fields correctly.

- `body_fingerprint` is `None` when `body_fp=` is absent from the sentinel.
- `source_ref` is correctly extracted despite the missing `body_fp=` field.
<!-- trie:end -->