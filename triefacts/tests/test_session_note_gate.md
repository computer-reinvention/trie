---
trie_version: 0.1.5
source: tests/test_session_note_gate.py
file_fingerprint: 33c0335e0de01abd6e4b37454c3b2dab17b3136e41a2b5ff9d000aa152c679d9
last_synced_at: '2026-06-09T10:07:49Z'
defines:
- kind: module
  qualified_name: tests/test_session_note_gate:__module__
  lines: 1-129
- kind: constant
  qualified_name: tests/test_session_note_gate:PROJECT_TOML
  lines: 17-25
- kind: class
  qualified_name: tests/test_session_note_gate:FakeTriefactClient
  lines: 28-37
- kind: method
  qualified_name: tests/test_session_note_gate:FakeTriefactClient.run
  lines: 31-37
- kind: function
  qualified_name: tests/test_session_note_gate:project
  lines: 41-58
- kind: function
  qualified_name: tests/test_session_note_gate:_config
  lines: 61-64
- kind: class
  qualified_name: tests/test_session_note_gate:TestSessionNoteValidator
  lines: 67-77
- kind: method
  qualified_name: tests/test_session_note_gate:TestSessionNoteValidator.test_rejects_short_and_boilerplate
  lines: 68-74
- kind: method
  qualified_name: tests/test_session_note_gate:TestSessionNoteValidator.test_accepts_real_note
  lines: 76-77
- kind: class
  qualified_name: tests/test_session_note_gate:TestGate
  lines: 80-116
- kind: method
  qualified_name: tests/test_session_note_gate:TestGate.test_single_symbol_needs_no_note
  lines: 81-86
- kind: method
  qualified_name: tests/test_session_note_gate:TestGate.test_multi_symbol_requires_note
  lines: 88-102
- kind: method
  qualified_name: tests/test_session_note_gate:TestGate.test_multi_symbol_with_note_commits
  lines: 104-116
- kind: class
  qualified_name: tests/test_session_note_gate:TestMetaHelpers
  lines: 119-128
- kind: method
  qualified_name: tests/test_session_note_gate:TestMetaHelpers.test_set_get_clear_meta
  lines: 120-125
- kind: method
  qualified_name: tests/test_session_note_gate:TestMetaHelpers.test_get_meta_missing_db_returns_none
  lines: 127-128
incoming_refs: 0
outgoing_refs: 27
---
<!-- trie:section symbol=tests/test_session_note_gate:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=4068dc6ef68e1db94c5331eb955d3a7e17d903cc538506fecf06e5ec962b2c5c source_ref=bd0edcc7b73ff757beb7e1edebbf57e3b02a1d80 role=test -->
Tests session note validation logic and multi-symbol commit gating in the edits pipeline.

- `FakeTriefactClient`: Mock client returning fixed `SectionBody` for testing
- `project`: Fixture creating temporary project with scanned symbols and synced triefacts
- `TestSessionNoteValidator`: Tests `session_note_ok` function rejecting short/boilerplate notes
- `TestGate`: Tests commit gating requiring session notes for multi-symbol changes
- `TestMetaHelpers`: Tests activity metadata storage operations
<!-- trie:end -->
<!-- trie:section symbol=tests/test_session_note_gate:PROJECT_TOML fingerprint=ea44d5615a2611cc14e40b5b84f8141a4679269bc80e3914e4fef0417f24d38b body_fp=7b5e81630c57112d3906842d9bc5e4ecaef4d5aaf434c45dd6047e07a87fbf6f source_ref=bd0edcc7b73ff757beb7e1edebbf57e3b02a1d80 role=test -->
TOML configuration string fixture for creating test trie projects.

- Contains standard trie sections: version, scope patterns, triefacts paths, model configurations, and cascade settings
<!-- trie:end -->
<!-- trie:section symbol=tests/test_session_note_gate:FakeTriefactClient fingerprint=c22c1583950633f73a49f72533e33f452437ffe5aee920b7029a55345ae38703 body_fp=d46bb60c333818318aed4f39b50fb8a1675f76cdaa7f59d3ed9b6ac12bce4e7d source_ref=bd0edcc7b73ff757beb7e1edebbf57e3b02a1d80 role=test -->
Mock client for testing triefact generation that returns fixed SectionBody output with minimal usage stats.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_session_note_gate:FakeTriefactClient.run fingerprint=ddf5f4d5a413797c8ae0c5853e9d1be123cf1571583cd546aead0c3037ad7075 body_fp=d920f97cec27e1d9ba3ddd2ac8c0be2a1f9ff75c0836836ce7eb24fc37cf6df5 source_ref=bd0edcc7b73ff757beb7e1edebbf57e3b02a1d80 role=test -->
FakeTriefactClient.run returns a fixed ModelResult with fake prose and minimal token usage for testing.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_session_note_gate:project fingerprint=69b41fe4013d4d2cea578ac0c10a996e91c0aa573085cdcc3e0168761612f50d body_fp=59fa3c54f7eaf240fda7ec169b41cc96ff685138c6eabff70da0fdd1c9909e19 source_ref=bd0edcc7b73ff757beb7e1edebbf57e3b02a1d80 role=test -->
Creates a test project directory with Python modules, config files, and initialized trie store.

- Sets up `src/m.py` with two simple functions `a()` and `b()`
- Writes `trie.toml` configuration and `.gitignore` files
- Scans project and syncs the module file using a fake triefact client
<!-- trie:end -->
<!-- trie:section symbol=tests/test_session_note_gate:_config fingerprint=2212d2ec1f6d36b65a66e8e256c0410684c26b19d40509bd6f5469cf10d0fcd7 body_fp=80a70c2b30e624188621ee5b489011041df0c8c55b8a4cb02ec25d7c0039fdac source_ref=bd0edcc7b73ff757beb7e1edebbf57e3b02a1d80 role=test -->
Loads project config and disables LSP backends for testing.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_session_note_gate:TestSessionNoteValidator fingerprint=cb404f85d1f6477f3ad8a29f2343b5a6fdf96254a75f71a9daef8ae3041849f3 body_fp=b56ac37b23cd5b9ebf4027c6acb1e380b073de0e5c0af80f2ef53c3d2b9324c8 source_ref=bd0edcc7b73ff757beb7e1edebbf57e3b02a1d80 role=test -->
Tests session note validation logic to ensure commit messages meet quality requirements.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_session_note_gate:TestSessionNoteValidator.test_rejects_short_and_boilerplate fingerprint=b1dadfac08c2e99d945f98058b43f2f7ce8df18be7ad0d3c233b7f49d3174447 body_fp=591a8b372e27bbee6642805cdc7722d0fecc0638b51254f240f39344fea47462 source_ref=bd0edcc7b73ff757beb7e1edebbf57e3b02a1d80 role=test -->
Tests TestSessionNoteValidator rejects empty strings, whitespace-only text, generic words like "fix" and "update", single characters, and strings under 12 characters.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_session_note_gate:TestSessionNoteValidator.test_accepts_real_note fingerprint=da49169bceda82d38935b38d47a057a3cc4f02091b4975c072522a624195dd69 body_fp=31c3aaecb76fabdf8c45803b2f531e97d216fa38287e3725ade79a0cbed384b9 source_ref=bd0edcc7b73ff757beb7e1edebbf57e3b02a1d80 role=test -->
TestSessionNoteValidator.test_accepts_real_note verifies session_note_ok returns True for a meaningful commit message.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_session_note_gate:TestGate fingerprint=6de552a4142799b952c70ae3bf662b00a9e3d62fd22c59dd081c3f473594d409 body_fp=f716c1b7324f62ea0efc9c66a2116f4a337ddcd229ea239c6a3a7203806bd1e9 source_ref=bd0edcc7b73ff757beb7e1edebbf57e3b02a1d80 role=test -->
Tests session note requirements for commits involving multiple symbols in the stage_and_commit pipeline.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_session_note_gate:TestGate.test_single_symbol_needs_no_note fingerprint=fb139940deb42e9d1f296e695a7e7989a00efd0a634a60f6b310a2ca842f864d body_fp=c5f46943f16f057954775ecbd12fe4d453156708e542ff2fb63da5d842c60cde source_ref=bd0edcc7b73ff757beb7e1edebbf57e3b02a1d80 role=test -->
TestGate method verifies that committing a single symbol patch succeeds without requiring a session note.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_session_note_gate:TestGate.test_multi_symbol_requires_note fingerprint=ece120e62a594c633641566b0bbdbcfef7d9b93853719699b7d24576868ba74b body_fp=e39b796c710ce9c74dac69600b211888c1db68672859196ee05c5d3787a1a8c8 source_ref=bd0edcc7b73ff757beb7e1edebbf57e3b02a1d80 role=test -->
TestGate method verifying that committing multiple symbol patches without a session note fails with session_note_required error.

- Adds patches to two symbols (src/m:a and src/m:b) then attempts commit without session note
- Validates error code, uncommitted status, and presence of repatch with synthesized session note draft
<!-- trie:end -->
<!-- trie:section symbol=tests/test_session_note_gate:TestGate.test_multi_symbol_with_note_commits fingerprint=2cb205ef46d6de7ff35d101cba437707e42e0bf021a862ba27986728189bee48 body_fp=3e2aec45d60f8ddcc916293ae33215885064034277a4bda61070b2638f08ac18 source_ref=bd0edcc7b73ff757beb7e1edebbf57e3b02a1d80 role=test -->
TestGate.test_multi_symbol_with_note_commits verifies that multi-symbol patches commit successfully when given a session note.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_session_note_gate:TestMetaHelpers fingerprint=e1b1e1766c2b126f0b8997a11425494cbce01afea3d9210e1eb12bf2e9a9cae7 body_fp=366202eec0b3df083d18977bbb21e71c60d3902e45c0ad216410e1c7b36b45ca source_ref=bd0edcc7b73ff757beb7e1edebbf57e3b02a1d80 role=test -->
Tests the activity metadata storage functionality for setting, getting, and clearing key-value pairs.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_session_note_gate:TestMetaHelpers.test_set_get_clear_meta fingerprint=13ef723d1b17be630f148d300ff577e4c6507bae97ca11f538636d5783ec48de body_fp=ad0565872cff3c2d1d8d41f44bede930d1d31d5da0aa3180dba653693e788474 source_ref=bd0edcc7b73ff757beb7e1edebbf57e3b02a1d80 role=test -->
Tests TestMetaHelpers activity metadata storage, retrieval, and deletion operations.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_session_note_gate:TestMetaHelpers.test_get_meta_missing_db_returns_none fingerprint=afebc3958a19fea6bc944f31c7ef79fca34899c07771fa4a270061d015912cff body_fp=b844ea7cd64870144381c54d9c75c7c40ac3e58676a5786e0cbea17f82850b13 source_ref=bd0edcc7b73ff757beb7e1edebbf57e3b02a1d80 role=test -->
Verifies TestMetaHelpers.test_get_meta_missing_db_returns_none returns None when querying metadata from nonexistent database path.
<!-- trie:end -->