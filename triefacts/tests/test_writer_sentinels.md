---
trie_version: 0.1.2
source: tests/test_writer_sentinels.py
file_fingerprint: e45d38ba1c000324ac0fc0b8f299335bd208a9fd00d5a3a7476092b9b833250f
last_synced_at: '2026-05-19T15:19:30Z'
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

<!-- trie:section symbol=tests/test_writer_sentinels:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=9064b4852698027b4bceedc72d80d00d6d8969e04cba97dd248fa467f58431b7 source_ref=d943306388f3b2cb323b1e0a1db4933439815f46 -->
## `tests/test_writer_sentinels`

Test suite for `TriefactFile` parsing, rendering, mutation, and round-trip fidelity.

- Covers sentinel parsing, front-matter, prose preservation, upsert, remove, and field ordering.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_writer_sentinels:_sample_triefact fingerprint=da10c5cdf0a4dbdc27a89de7be7c634bfb5d951821a716bf2822c89925533877 body_fp=766d020a12f9bc9b5f8801f77abc02f45227af4f49d39abcb2f7322c5b2d2edc source_ref=343ba48556b010f8d0e6a5b3d9397d89575c65f0 -->
## `_sample_triefact() -> str`

Return a realistic triefact string with mixed front-matter keys, two sentinel-wrapped sections, and interleaved hand-written prose for use in `render_for_agent` tests.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_writer_sentinels:test_render_for_agent_strips_internal_frontmatter fingerprint=581537bdd2d548348dc9a84b5bde8ea693ed2a07b0aad02c8c9d939ebbbc50fe body_fp=ab39232c52df4388614dca9d76cf612c3525e390ae9e91ba639bdaa0cd4d7382 source_ref=343ba48556b010f8d0e6a5b3d9397d89575c65f0 -->
## `test_render_for_agent_strips_internal_frontmatter()`

Assert that `render_for_agent` removes internal-only front-matter keys from triefact output.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_writer_sentinels:test_render_for_agent_keeps_agent_frontmatter fingerprint=a1adf8b59b837a94c7f4d32da28500c17190cef92a3028be9b2fb2d8cead0fb8 body_fp=0ff465ec88a53133ba81f14383f8e53449d791fa06709e997819b668df22bb63 source_ref=343ba48556b010f8d0e6a5b3d9397d89575c65f0 -->
## `test_render_for_agent_keeps_agent_frontmatter()`

Assert that `render_for_agent` retains all agent-relevant front-matter keys in the output YAML block.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_writer_sentinels:test_render_for_agent_strips_sentinels_and_fingerprints fingerprint=9a939937bb00998aac30c7d8665ef774c0e37fa8cbfa88034c2f09595f5f766a body_fp=78c879d649b3e78c6008cdba4ff87110ce0f9613eb2487560cc6c86f8a2fcefe source_ref=343ba48556b010f8d0e6a5b3d9397d89575c65f0 -->
## `test_render_for_agent_strips_sentinels_and_fingerprints()`

Assert that `render_for_agent` removes all sentinel comments and fingerprint fields from output.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_writer_sentinels:test_render_for_agent_keeps_section_bodies_and_interleaved_prose fingerprint=3797428ea3cd60e6802fb0a0a5df383b905b236b7e32df134018405c909ed757 body_fp=c94648993afc377004ccd872f87f152a23e38a4e3233ee47971ee38eb83e7362 source_ref=343ba48556b010f8d0e6a5b3d9397d89575c65f0 -->
## `test_render_for_agent_keeps_section_bodies_and_interleaved_prose()`

Assert that `render_for_agent` preserves both section bodies, interleaved prose, and blank-line separation between sections.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_writer_sentinels:test_render_for_agent_omits_frontmatter_when_no_agent_keys fingerprint=7a1c78399101ebecde991d331809bf4373573ac31ede0ffb0fffdeb8d4281b1f body_fp=3ac3877da856b6612a50d69520756f2b038f25b091f0531a6027e184d89c160c source_ref=343ba48556b010f8d0e6a5b3d9397d89575c65f0 -->
## `test_render_for_agent_omits_frontmatter_when_no_agent_keys()`

Assert that `render_for_agent` drops the entire front-matter block when all keys are internal-only, while preserving section bodies.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_writer_sentinels:test_render_for_agent_empty_input fingerprint=cb071367cdb29133f48c3cb017fcdfe0b91718366df0e6889cb7019b8000b292 body_fp=ef16d8ff90c8a6b8a72da3f9aee5e722e8af41dcce4e9f637b9ae589a68a5a22 source_ref=343ba48556b010f8d0e6a5b3d9397d89575c65f0 -->
## `test_render_for_agent_empty_input()`

Assert that `render_for_agent("")` returns an empty string.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_writer_sentinels:test_render_for_agent_prose_only_no_sentinels fingerprint=15f31ad9e89445f42fad2dbafa59d52888fd7a5e00d9285756b45de6ab7361ec body_fp=cd2574973f8272ae05b600e59b0aa8120e1e548769d9364f293db698646fb717 source_ref=343ba48556b010f8d0e6a5b3d9397d89575c65f0 -->
## `test_render_for_agent_prose_only_no_sentinels()`

Assert that `render_for_agent` passes through plain prose with no frontmatter or sentinels unchanged.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_writer_sentinels:test_agent_front_matter_keys_constant fingerprint=64acc40a3816c88839dddb297dcc73231822240b25e6f37b53bd7d0d3808e85b body_fp=1948c10abb1005d7c211224915e72785d7a13fe95d81ac6752d86706d744d7c7 source_ref=343ba48556b010f8d0e6a5b3d9397d89575c65f0 -->
## `test_agent_front_matter_keys_constant()`

Assert that `AGENT_FRONT_MATTER_KEYS` contains exactly the four expected agent-facing front-matter key names.
<!-- trie:end -->