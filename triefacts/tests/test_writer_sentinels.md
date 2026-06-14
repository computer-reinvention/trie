---
trie_version: 0.1.5
source: tests/test_writer_sentinels.py
file_fingerprint: caa376b519aa734acc4ffb51698d2385b1f3e378043a9cc30955851334bc849d
last_synced_at: '2026-06-10T13:17:12Z'
defines:
- kind: module
  qualified_name: tests/test_writer_sentinels:__module__
  lines: 1-513
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
  qualified_name: tests/test_writer_sentinels:test_parse_dedupes_duplicate_sections_keeping_last
  lines: 93-125
- kind: function
  qualified_name: tests/test_writer_sentinels:test_roundtrip_only_prose_is_byte_identical
  lines: 131-133
- kind: function
  qualified_name: tests/test_writer_sentinels:test_roundtrip_with_front_matter_and_section_carrying_body_fp
  lines: 136-150
- kind: function
  qualified_name: tests/test_writer_sentinels:test_roundtrip_multiple_sections_with_human_prose
  lines: 153-172
- kind: function
  qualified_name: tests/test_writer_sentinels:test_legacy_section_without_body_fp_parses_and_promotes_on_render
  lines: 175-185
- kind: function
  qualified_name: tests/test_writer_sentinels:test_section_round_trips_source_ref
  lines: 188-202
- kind: function
  qualified_name: tests/test_writer_sentinels:test_section_without_source_ref_renders_without_it
  lines: 205-212
- kind: function
  qualified_name: tests/test_writer_sentinels:test_section_with_source_ref_renders_field_in_stable_position
  lines: 215-230
- kind: function
  qualified_name: tests/test_writer_sentinels:test_section_legacy_format_with_source_ref_appended_parses
  lines: 233-247
- kind: function
  qualified_name: tests/test_writer_sentinels:test_upsert_replaces_existing_section_preserves_prose
  lines: 253-276
- kind: function
  qualified_name: tests/test_writer_sentinels:test_upsert_appends_new_section_at_end
  lines: 279-287
- kind: function
  qualified_name: tests/test_writer_sentinels:test_upsert_into_empty_triefact
  lines: 290-298
- kind: function
  qualified_name: tests/test_writer_sentinels:test_remove_section
  lines: 301-318
- kind: function
  qualified_name: tests/test_writer_sentinels:test_remove_missing_section_returns_false
  lines: 321-323
- kind: function
  qualified_name: tests/test_writer_sentinels:test_section_qnames_in_order
  lines: 326-333
- kind: function
  qualified_name: tests/test_writer_sentinels:test_human_edit_between_sections_survives_regen
  lines: 339-370
- kind: function
  qualified_name: tests/test_writer_sentinels:test_front_matter_re_renders_in_insertion_order
  lines: 373-379
- kind: function
  qualified_name: tests/test_writer_sentinels:_sample_triefact
  lines: 385-417
- kind: function
  qualified_name: tests/test_writer_sentinels:test_render_for_agent_strips_internal_frontmatter
  lines: 420-428
- kind: function
  qualified_name: tests/test_writer_sentinels:test_render_for_agent_keeps_agent_frontmatter
  lines: 431-442
- kind: function
  qualified_name: tests/test_writer_sentinels:test_render_for_agent_strips_sentinels_and_fingerprints
  lines: 445-453
- kind: function
  qualified_name: tests/test_writer_sentinels:test_render_for_agent_keeps_section_bodies_and_interleaved_prose
  lines: 456-469
- kind: function
  qualified_name: tests/test_writer_sentinels:test_render_for_agent_omits_frontmatter_when_no_agent_keys
  lines: 472-490
- kind: function
  qualified_name: tests/test_writer_sentinels:test_render_for_agent_empty_input
  lines: 493-494
- kind: function
  qualified_name: tests/test_writer_sentinels:test_render_for_agent_prose_only_no_sentinels
  lines: 497-502
- kind: function
  qualified_name: tests/test_writer_sentinels:test_agent_front_matter_keys_constant
  lines: 505-512
incoming_refs: 0
outgoing_refs: 48
---
<!-- trie:section symbol=tests/test_writer_sentinels:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=b090a7da0bb84889c079565a7c4fc125a9e9a8c12ecaa519759621dd369fadfa source_ref=da68e1ccc1166d342f5b38d5c6453cf2fcfde631 role=test-infrastructure -->
Tests parsing, rendering, and mutation of TriefactFile with sentinel-wrapped sections and front matter.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_parse_empty fingerprint=d8d478032b2edcb69bfa32426a508c57ca253f274418d1d9533ca54ff39decf9 body_fp=cf48ba181f8be644cbab91be6668338ae0fefb318b809d2a3d5e78d8f8056f04 source_ref=da68e1ccc1166d342f5b38d5c6453cf2fcfde631 role=test-infrastructure -->
Verifies TriefactFile.parse returns empty front matter and chunks when given empty string input.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_parse_only_prose fingerprint=331924321c90bdde87c44e245a991131e979fb23776f4a7721c5a5572534e1e5 body_fp=8026a2a04ef47afb30a6f625921c6f5795811671ae6289a1ffb79e1c6955f11a source_ref=3349599c47ac1dba711eb916647d1db06dea96d1 role=test -->
Tests that TriefactFile.parse correctly handles plain markdown content without front matter or sections.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_parse_front_matter_only fingerprint=91f029ba0079c8e4ae6b734bc86ac1fa3370f9847fce9a27aa86e8670f840489 body_fp=3dc1ba90772a0837f8af8006310913cd0cd01a967986c21fa38d19d43ee9369b source_ref=da68e1ccc1166d342f5b38d5c6453cf2fcfde631 role=test-infrastructure -->
Tests that TriefactFile.parse correctly handles a document containing only YAML front matter with no content chunks.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_parse_front_matter_and_prose fingerprint=9e2c997d2a34eb82a33d8cfe52afc4f0c73fa88d5d72f401546d8db3d7ee99bd body_fp=b1837b9391509c6258d9b9c0bf3e1a996ab5463b20e0ad0266164c1e576336c4 source_ref=3349599c47ac1dba711eb916647d1db06dea96d1 role=test -->
Tests TriefactFile parsing of input containing both YAML front matter and prose content.

- Verifies front matter is extracted into the front_matter dict
- Confirms prose content after front matter becomes a single Prose chunk
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_parse_single_section fingerprint=7bdcd4d0a5afb4d45f87aafa45570e49e973a0a2f15cd10a5ec36a352d5ce027 body_fp=49e145db689cd4990ddbfa6f9b4dabfe8a80eb8d3ffdc65ba790883a3e92bc3a source_ref=3349599c47ac1dba711eb916647d1db06dea96d1 role=test -->
Tests TriefactFile.parse() correctly parses markdown with a single trie section between prose chunks.

- Validates that prose before and after the section becomes separate Prose chunks
- Verifies section metadata (qualified_name, fingerprint) is extracted correctly  
- Confirms section body excludes the sentinel comment markers
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_parse_multiple_sections_with_prose_between fingerprint=f6ce3fc57be98792327d599972b5ecd77f34b1e63c1092f5b2dd3cddb226c760 body_fp=b18cad4b3bde783e4107656a707bab93c781d3216b4a7b99b6ea8f118478b63f source_ref=3349599c47ac1dba711eb916647d1db06dea96d1 role=test -->
Tests TriefactFile.parse correctly parses multiple sections with prose chunks between them.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_parse_unterminated_section_raises fingerprint=063145f59bcc49bb9b1b79d2a1d6264e0e39c21c108518ba7fd457ab92caeee7 body_fp=bbde3198627eb8b16b566f67536a4712a296656bd72d4e93e30fa78833356b5c source_ref=da68e1ccc1166d342f5b38d5c6453cf2fcfde631 role=test-infrastructure -->
Verifies TriefactFile.parse raises ValueError when a trie section comment lacks a closing sentinel.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_parse_dedupes_duplicate_sections_keeping_last fingerprint=579fedea498e476686cd7ab3240c8ba5e3c4843e76c0fb7fe1b76be4fc21a743 body_fp=34b0e93d94ed51d9511da575844c62b9c90846de5254ebcbc3ce3a6a6756199c source_ref=3349599c47ac1dba711eb916647d1db06dea96d1 role=test -->
Verifies TriefactFile.parse deduplicates duplicate sections by keeping the last occurrence while preserving the first occurrence position.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_roundtrip_only_prose_is_byte_identical fingerprint=df3b26580aea061ee81a45fe4621020dde3e094d6c40ce016f480af7b900a516 body_fp=e6faeeda42fb90ccbc197c5dbb8ab2cc91dd4e12e223d478a48ef57e0d251613 source_ref=da68e1ccc1166d342f5b38d5c6453cf2fcfde631 role=test-infrastructure -->
Verifies that parsing and rendering plain markdown text without sections produces identical output.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_roundtrip_with_front_matter_and_section_carrying_body_fp fingerprint=ecddcc86d932d0ecd4e46b4786a5c522f7caf49e59c7be9e14d65843fd2a8305 body_fp=e3e31a5438af1f254cb6ceee072f9035ff624f42b76b1561f5d886490362b93e source_ref=3349599c47ac1dba711eb916647d1db06dea96d1 role=test -->
Tests that a TriefactFile with front matter and a section with body_fp roundtrips through parse/render identically.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_roundtrip_multiple_sections_with_human_prose fingerprint=747ba03c7824c21923141c4f7e0bd804cdd4ccd6161d13f903335e8f5754005f body_fp=fba5d18d784ced40bfdee112d7defd431822c22d5d994f4c29afc98a459f63f6 source_ref=3349599c47ac1dba711eb916647d1db06dea96d1 role=test -->
Verifies that TriefactFile parse-render round-trip preserves multiple sections with interleaved human prose exactly.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_legacy_section_without_body_fp_parses_and_promotes_on_render fingerprint=3d551abb1de02f543f89b4091b9bdaf94c5edcc2a03992514d4aae68b274631b body_fp=3e6eea8c167cf3ae432f092cad382a0e18fea716a8fb9c5baa241a51354c8c9c source_ref=3349599c47ac1dba711eb916647d1db06dea96d1 role=test -->
Tests that legacy sections without `body_fp=` parse correctly and gain body fingerprints when rendered.

- Verifies legacy sections parse with `body_fingerprint` as None
- Confirms renderer adds `body_fp=` field with hashed body content
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_section_round_trips_source_ref fingerprint=17d9bcaee21703293bc05f945dd9313f83664d80a0aa68880985462bcc41567d body_fp=d4c4ddc5b4c1cff833e4eecdb8859ade75f3e295e24d6196cce905ddebc0d147 source_ref=3349599c47ac1dba711eb916647d1db06dea96d1 role=test -->
Verifies that `source_ref` attribute in triefact section sentinels persists unchanged through parse-render cycles.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_section_without_source_ref_renders_without_it fingerprint=ced24b63d8df8fc990893b0c8875c8591785b2f502a0d7806e2cf5639da1c71d body_fp=0a39d0e8c9e6c7339210936372f592b390ba3f1f3329ebd1305669fcb577d15c source_ref=da68e1ccc1166d342f5b38d5c6453cf2fcfde631 role=test-infrastructure -->
Tests that TriefactFile.render omits the source_ref field when a section lacks one.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_section_with_source_ref_renders_field_in_stable_position fingerprint=f1dd7d68b85cc31ae27153e352bbdfbc8753da8c427df4782bdacc769fc35acd body_fp=127f751575a775471c36f4710633197f682142eb72aedf07b0965a911e467624 source_ref=da68e1ccc1166d342f5b38d5c6453cf2fcfde631 role=test-infrastructure -->
Verifies that TriefactFile renders section sentinel fields in deterministic order for stable output.

- Tests that fingerprint, body_fp, and source_ref appear in consistent positions
- Ensures byte-identical rendering across multiple calls with same data
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_section_legacy_format_with_source_ref_appended_parses fingerprint=b33af3cc09b68ba42953496ef544b7fc9a3bcdbbceda3c5ca7db3ccc7fca2390 body_fp=da3131b7f93cf2a1dc1bf1bfa74b4d1aca4c5b934490da3cddf4f829020ef89b source_ref=3349599c47ac1dba711eb916647d1db06dea96d1 role=test -->
Tests that TriefactFile.parse correctly handles legacy sections with source_ref but no body_fp.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_upsert_replaces_existing_section_preserves_prose fingerprint=19a03d771f37ccebe0c9d67628c683d99fa717c1c963166cafa7d0859553576e body_fp=9ccd80fa767295b29d3c1e15b7bc78892b971c579e7f02611cfe757c99b46441 source_ref=da68e1ccc1166d342f5b38d5c6453cf2fcfde631 role=test-infrastructure -->
Tests that TriefactFile.upsert_section replaces existing sections while preserving surrounding prose and other sections.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_upsert_appends_new_section_at_end fingerprint=f46e868629972d796c1d951ac91a82caf93691abf250b29a829bebca43a621e7 body_fp=68e571ba944891878ec0dd60713dcf50c8618590e07f36bd95901e3ff39bf21d source_ref=3349599c47ac1dba711eb916647d1db06dea96d1 role=test -->
Verifies that TriefactFile.upsert_section appends new sections at the end while preserving existing prose.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_upsert_into_empty_triefact fingerprint=b200e282fd6690ffd6583614228337a8a80a1e9ab19c61f402dee458246bcbdc body_fp=d261599ef8e6b11ff2c297005aa06f154034a3c27f8a79b9b93152160541bd7a source_ref=3349599c47ac1dba711eb916647d1db06dea96d1 role=test -->
Tests that TriefactFile.upsert_section correctly adds a new section to an empty triefact document and renders it with proper sentinels.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_remove_section fingerprint=78873ffb894ceac24648f6c7604b3eac9c238c94e8e3bcd401c464fc19b3808f body_fp=3a7921b751da6a9f9b6292882161457be810849f0eb6d2094d5a2aab50071809 source_ref=da68e1ccc1166d342f5b38d5c6453cf2fcfde631 role=test-infrastructure -->
Tests that TriefactFile.remove_section removes the specified section while preserving other sections and prose.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_remove_missing_section_returns_false fingerprint=c89aedc0fb3b0f51faaae6fe50764356bc95a44a39d673c4a6757783e5f28b02 body_fp=0f63721988eabc336f71be9989bcea44b76beebbac8682bfe40ead64255ea678 source_ref=da68e1ccc1166d342f5b38d5c6453cf2fcfde631 role=test-infrastructure -->
Verifies that TriefactFile.remove_section returns False when attempting to remove a non-existent section.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_section_qnames_in_order fingerprint=10e2d7e908cfea7610110e6a1aefa33470549e453459ae19945abb75daee457e body_fp=4dc710e17e6dac218ae61bf7736a4219e8ac1ec5077f70a846e5186885b8fd5b source_ref=da68e1ccc1166d342f5b38d5c6453cf2fcfde631 role=test-infrastructure -->
Verifies TriefactFile.section_qnames returns qualified names in document order, not alphabetical order.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_human_edit_between_sections_survives_regen fingerprint=637b8c3ecd5d200c81d0b607862a0c940a6aec82afe722036a94505b536cd185 body_fp=05ea61cb56bb857d4e5fe29b954b46bb0278cb5ab7fa4ce0c758e70a0b4c767f source_ref=da68e1ccc1166d342f5b38d5c6453cf2fcfde631 role=test-infrastructure -->
Verifies that human-written prose between generated sections survives when sections are regenerated with new content and fingerprints.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_front_matter_re_renders_in_insertion_order fingerprint=f3b23aacaca01c7bfb901f9c0898c65335b3e98a726c10478618ccb4e61257c4 body_fp=2804e7b6f18d9524d3c8284b5f0c2defa74a7cb3d06335c090b9fec67bd70813 source_ref=da68e1ccc1166d342f5b38d5c6453cf2fcfde631 role=test-infrastructure -->
Verifies that TriefactFile preserves front matter key ordering when rendering after parse.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:_sample_triefact fingerprint=da10c5cdf0a4dbdc27a89de7be7c634bfb5d951821a716bf2822c89925533877 body_fp=05daab7a6e7527e1ffbdce4a2855d376f8e9d2871268c7d2c22732dc98fe6eeb source_ref=da68e1ccc1166d342f5b38d5c6453cf2fcfde631 role=test-infrastructure -->
Returns a realistic triefact string with frontmatter, two sections, and prose for testing `render_for_agent`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_render_for_agent_strips_internal_frontmatter fingerprint=581537bdd2d548348dc9a84b5bde8ea693ed2a07b0aad02c8c9d939ebbbc50fe body_fp=f0d466c480d1ee8b8190f754061a12dd7ba9416cd383c09f0bd5a7b7f8fe9f9b source_ref=3349599c47ac1dba711eb916647d1db06dea96d1 role=test -->
Tests that `render_for_agent` removes internal frontmatter keys while preserving agent-relevant content.

- Verifies `trie_version`, `file_fingerprint`, and `last_synced_at` are stripped from output
- Confirms `source:` YAML key is removed without affecting prose containing "source"
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_render_for_agent_keeps_agent_frontmatter fingerprint=a1adf8b59b837a94c7f4d32da28500c17190cef92a3028be9b2fb2d8cead0fb8 body_fp=e2050204dc585ea857119f6601c976ef3c54be822c2d48d2a5bcd5a3992c5199 source_ref=3349599c47ac1dba711eb916647d1db06dea96d1 role=test -->
Verifies that `render_for_agent` preserves agent-relevant frontmatter keys while stripping internal ones.

- Checks frontmatter block presence with agent keys like `description`, `defines`, `incoming_refs`, `outgoing_refs`
- Validates specific content preservation including qualified names and reference counts
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_render_for_agent_strips_sentinels_and_fingerprints fingerprint=9a939937bb00998aac30c7d8665ef774c0e37fa8cbfa88034c2f09595f5f766a body_fp=d9876dd7afe809bdd9d1ce26d3af80e55e4791bcf65608f9862d564849c1e441 source_ref=3349599c47ac1dba711eb916647d1db06dea96d1 role=test -->
Verifies that render_for_agent removes all trie sentinel comments and their embedded fingerprint attributes.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_render_for_agent_keeps_section_bodies_and_interleaved_prose fingerprint=3797428ea3cd60e6802fb0a0a5df383b905b236b7e32df134018405c909ed757 body_fp=ccdfd82026488c51060264a177ac52fb8f9f8c4d95865c931a6e1245b8e61e69 source_ref=3349599c47ac1dba711eb916647d1db06dea96d1 role=test -->
Verifies that `render_for_agent` preserves section bodies and human-written prose between sections with proper spacing.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_render_for_agent_omits_frontmatter_when_no_agent_keys fingerprint=7a1c78399101ebecde991d331809bf4373573ac31ede0ffb0fffdeb8d4281b1f body_fp=3882567f877fa6ee4730328e995434fead11dabaab7d1f500898a508e22d426e source_ref=3349599c47ac1dba711eb916647d1db06dea96d1 role=test -->
Tests that `render_for_agent` omits the frontmatter block entirely when no agent-relevant keys exist.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_render_for_agent_empty_input fingerprint=cb071367cdb29133f48c3cb017fcdfe0b91718366df0e6889cb7019b8000b292 body_fp=677c7d0826a49444ed5846f4553390247e8407a4177308c71ee3ae3d4c05f97e source_ref=3349599c47ac1dba711eb916647d1db06dea96d1 role=test -->
Verifies that render_for_agent returns empty string when given empty input.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_render_for_agent_prose_only_no_sentinels fingerprint=15f31ad9e89445f42fad2dbafa59d52888fd7a5e00d9285756b45de6ab7361ec body_fp=7d118aaa555203e95b4b24fc8d7071a466ce31a945dbb76f9884ba6cda7faad0 source_ref=3349599c47ac1dba711eb916647d1db06dea96d1 role=test -->
Tests that `render_for_agent` passes through plain prose without frontmatter or sentinels unchanged.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_writer_sentinels:test_agent_front_matter_keys_constant fingerprint=64acc40a3816c88839dddb297dcc73231822240b25e6f37b53bd7d0d3808e85b body_fp=9f6c3bb0789d136cbba831e6fa16415b62345eab8dbe51c114dbb7a2aa4b0949 source_ref=3349599c47ac1dba711eb916647d1db06dea96d1 role=test -->
Validates that `AGENT_FRONT_MATTER_KEYS` contains exactly the expected set of frontmatter field names.
<!-- trie:end -->