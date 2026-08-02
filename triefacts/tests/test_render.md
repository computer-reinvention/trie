---
trie_version: 0.3.0
source: tests/test_render.py
file_fingerprint: 4b917240dec8c6ef0a19228c8a90e6ece0d66fe4687b0cd7fdf492ec69406de8
last_synced_at: '2026-08-01T01:14:43Z'
description: "Tests for trie/render.py \u2014 the plain-text envelope renderer that is the"
defines:
- kind: module
  qualified_name: tests/test_render:__module__
  lines: 1-73
- kind: function
  qualified_name: tests/test_render:test_symbol_records_render_compact
  lines: 9-30
  signature: def test_symbol_records_render_compact()
- kind: function
  qualified_name: tests/test_render:test_call_chains_render_as_arrows
  lines: 33-37
  signature: def test_call_chains_render_as_arrows()
- kind: function
  qualified_name: tests/test_render:test_prose_fields_render_verbatim
  lines: 40-44
  signature: def test_prose_fields_render_verbatim()
- kind: function
  qualified_name: tests/test_render:test_story_suppresses_duplicate_caller_records
  lines: 47-57
  signature: def test_story_suppresses_duplicate_caller_records()
- kind: function
  qualified_name: tests/test_render:test_error_envelope_renders_code_message_suggestion
  lines: 60-65
  signature: def test_error_envelope_renders_code_message_suggestion()
- kind: function
  qualified_name: tests/test_render:test_empty_list_and_scalars
  lines: 68-72
  signature: def test_empty_list_and_scalars()
incoming_refs: 0
outgoing_refs: 6
---
<!-- trie:section symbol=tests/test_render:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=be0f5859968b76c64bab01d7528630686eb7ae9fbcb8c04e3b9d1f8009f70465 source_ref=319f3a50fc74e12bbbdbf39eb6f035c8efbfc9e0 role=test -->
Tests for `trie/render.py`, verifying plain-text envelope rendering across symbols, call chains, prose fields, error envelopes, and edge cases.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_render:test_symbol_records_render_compact fingerprint=1e89ad6f6035f3e2011e061f3f569b9f01d5e40b5a2445932825001285f6a65e body_fp=d75fefc763202e80130e70e186d1cb3696ced55c4cbdf9a55e863035a32dca42 source_ref=319f3a50fc74e12bbbdbf39eb6f035c8efbfc9e0 role=test -->
## `def test_symbol_records_render_compact()`

Assert that `render_envelope` formats a symbol hit as a single-line header, a collapsed signature, and a one-liner with no escaped newlines.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_render:test_call_chains_render_as_arrows fingerprint=5ec32246818ca431a0dd86b86805827556f3058838e701e0373f530e43c5eed6 body_fp=a6a5e42b8c9ceac3b174527a8470b1e71be8b100381ef4267ade1abeb67c9590 source_ref=319f3a50fc74e12bbbdbf39eb6f035c8efbfc9e0 role=test -->
## `def test_call_chains_render_as_arrows()`

Assert that `render_envelope` formats `paths` lists as numbered, arrow-separated chains with no raw bracket characters.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_render:test_prose_fields_render_verbatim fingerprint=f46df1407fa767084c9644a2ea00e45cd6ebaf7b4a8591f783a46b8e7fbc72e2 body_fp=ada5a03aa8a77f36683a2d61f905371c8818382a3eae2e6fbc8b3995ada794b0 source_ref=319f3a50fc74e12bbbdbf39eb6f035c8efbfc9e0 role=test -->
## `def test_prose_fields_render_verbatim()`

Assert that `render_envelope` emits `usage_story` prose unchanged, preserving Markdown formatting and newlines.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_render:test_story_suppresses_duplicate_caller_records fingerprint=fbe4853eb405bcc354fe284854fe3d1a5f118c339d26b1270eafca195470ae1f body_fp=1b194fbdcb43c0dcbe793e7135d6891d091bddc7d3a829fc8b6dd0693c50c432 source_ref=319f3a50fc74e12bbbdbf39eb6f035c8efbfc9e0 role=test -->
## `def test_story_suppresses_duplicate_caller_records()`

Assert that `render_envelope` omits raw `callers` records when a `usage_story` already contains the same symbol reference.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_render:test_error_envelope_renders_code_message_suggestion fingerprint=9e9462ee91e942f57de63e051bdefa3c9ae944dd7f8984f432f971bc8d3a747c body_fp=2e18b29af3fe5d5a7118953bddd2702e311aca2474d925d4e4bd5766561c3f1e source_ref=319f3a50fc74e12bbbdbf39eb6f035c8efbfc9e0 role=test -->
## `def test_error_envelope_renders_code_message_suggestion()`

Assert that `render_envelope` formats an error envelope with `"error {code}: {message}"` on the first line and the suggestion text on a subsequent line.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_render:test_empty_list_and_scalars fingerprint=ff0cc2163e63655dd819d1a2afcdafef1bb91ce07117072f0188a14f7adf3c8e body_fp=cc5b449df33f2fbd98fffe4d2a48fa1e9ae6142663b2b469b21e393d6534f2eb source_ref=319f3a50fc74e12bbbdbf39eb6f035c8efbfc9e0 role=test -->
## `def test_empty_list_and_scalars()`

Assert that `render_envelope` renders empty lists as `(none)` and scalar values as their string representations.
<!-- trie:end -->