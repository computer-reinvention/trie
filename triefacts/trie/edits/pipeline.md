---
trie_version: 0.2.1
source: trie/edits/pipeline.py
file_fingerprint: 78eacfd9837f0cbc0051e3ae2a17c8ef7b831e3ffe28b8bf79c7960defea026a
last_synced_at: '2026-07-29T23:17:31Z'
description: 'The patch pipeline: an intent store, not a code generator.'
defines:
- kind: module
  qualified_name: trie/edits/pipeline:__module__
  lines: 1-198
- kind: constant
  qualified_name: trie/edits/pipeline:_SESSION_NOTE_STOPLIST
  lines: 30-30
- kind: constant
  qualified_name: trie/edits/pipeline:_SESSION_NOTE_MIN_CHARS
  lines: 31-31
- kind: function
  qualified_name: trie/edits/pipeline:session_note_ok
  lines: 34-43
- kind: function
  qualified_name: trie/edits/pipeline:_expand_callers
  lines: 46-77
- kind: function
  qualified_name: trie/edits/pipeline:preview_patches
  lines: 80-106
- kind: function
  qualified_name: trie/edits/pipeline:record_intent
  lines: 109-180
- kind: function
  qualified_name: trie/edits/pipeline:_coverage_report
  lines: 183-197
incoming_refs: 8
outgoing_refs: 0
---
<!-- trie:section symbol=trie/edits/pipeline:__module__ fingerprint=45be29ba2393e2202b19fff81e0cee7b403b3fdc58d03f7590497dfa16ac62ef body_fp=5cda9f3d912813a1259c1b90c1e061528ea62d02bb56805d1277acdb801ce0ff source_ref=93562620aac7b790c8dabcf8f01990451e22c9c3 role=orchestration -->
Archive-backed intent pipeline: stages patch notes per symbol, validates session notes, and commits records to the session log without generating or touching source code.

- No code generation, no LLM calls, no filesystem writes to the source tree
- Session note gate: multi-symbol commits require ≥12-char non-stoplist unifying intent
- Archive feeds `trie diff`, PR digest, `read --history`, and the `trie intent` pre-commit gate
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/pipeline:_SESSION_NOTE_STOPLIST fingerprint=a09ea23a28cadabdce59b05e05933086e628e24bb9089e97fc41fae857e49340 body_fp=1fe480e5cabcef5c603d7d89a8366099d0c0d9daeebc3465452b921dc8964fcf source_ref=93562620aac7b790c8dabcf8f01990451e22c9c3 role=config -->
Set of lowercase words rejected as session notes by `session_note_ok` for being too vague to serve as meaningful intent titles.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/pipeline:_SESSION_NOTE_MIN_CHARS fingerprint=603c02b63000bf140fdc373da663206d6d7b0d889a94f1236c02e5ea5b661d6d body_fp=23d1e5f1ac4d1a1a75f7ba12436b3d7b92408dfb9b72a91ec2980eccd240cde7 source_ref=93562620aac7b790c8dabcf8f01990451e22c9c3 role=config -->
Minimum character length a session note must meet to pass `session_note_ok`.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/pipeline:session_note_ok fingerprint=550eef9d58077682531b3b572daa5c4ee8937b76a3429cb0dc3bbf679e779c7e body_fp=ef730a588b805741910bbcf96e0938f16d099f7f1c8a5dd74068ad86fc503072 source_ref=93562620aac7b790c8dabcf8f01990451e22c9c3 role=domain -->
Return `True` if `note` meets minimum length and is not a stoplist word; used to gate multi-symbol `record_intent` calls.

- `note`: stripped and lowercased before validation; `None`-safe
- Returns `False` if shorter than 12 characters or matches a stoplist entry (e.g. `"fix"`, `"wip"`, `"."`)
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/pipeline:_expand_callers fingerprint=217e5c26adaf1a370ac987fe3805925561cf96090adf5cc2321072a7345cf84b body_fp=33e074deb81966dc6dabdf0590aac1bcae680f8c1926bfc2dc858d914d6ece5a source_ref=93562620aac7b790c8dabcf8f01990451e22c9c3 role=domain -->
Expand callers of `seed_qnames` up to `cascade_depth` BFS levels, skipping hub symbols that exceed `hub_threshold` incoming edges.

- `seed_qnames`: starting qualified names; excluded from the returned set.
- `hub_threshold`: symbols with more incoming edges than this are not traversed.
- Returns callers discovered beyond the seed set.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/pipeline:preview_patches fingerprint=1a7d82a23c520c63f7790504ba706aedb20733855251d5e4062f8d352d18ae9c body_fp=a65bf5267b23a4c69816835656f26bd0025865dcbca1c66514f0aa8d400530e3 source_ref=c360ff8f7df2b3e6b0a8cda993262c2aeead5962 role=domain -->
Return a read-only summary of pending patch notes and the call-graph blast radius of the symbols they touch.

- `patched_list`: sorted qualified names of symbols carrying unapplied (unsealed) notes
- `cascade_list`: sorted qualified names of upstream callers within cascade depth, excluding patched symbols
- `cascade_symbols` / `patched_symbols`: integer counts of each list
- `total_patches`: total note count across all patched symbols
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/pipeline:record_intent fingerprint=9326b2a878fa067c28d451248da289e56c03bfb7b70c35c128aa0c0e92720465 body_fp=fb5df33de7a8db38dab798816b58692ccf26dda54cef21f015c67b4b755b8f66 source_ref=a50b31660d0129189f1eeecc691bf1931b0d789b role=domain -->
Seal pending patch notes in-place via `store.mark_patches_applied` (stamps `applied=1`), without writing to any external file or clearing rows from the patches tables.

- `session_note`: required when `total > 1`; validated via `session_note_ok` (rejects empty, too-short, and stoplist words); returns `ok=False` with `"session_note_required"` otherwise.
- Returns a dict with `ok`, `recorded` count, `symbols` list, and a `next` advisory string; on success also attempts to populate `uncovered` with qnames of touched-but-unnoted symbols via `trie.intent_gate.evaluate` (advisory only — exceptions are silently swallowed).
- When `total == 0`, still runs the coverage report and returns it (with a `next` hint if uncovered symbols exist), rather than returning an empty envelope immediately.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/pipeline:_coverage_report fingerprint=e7218a6b13aa3f6dcc8855cee725d9b597f1933c50039dd6de751a3f877b8a22 body_fp=37255c35fa9fd5e9378a9c3397439316056b27cfadc97c7094bf569633583955 source_ref=a50b31660d0129189f1eeecc691bf1931b0d789b role=domain -->
Run the intent-gate evaluation at apply time and return uncovered touched symbols so agents learn of gaps before commit.

- Returns `{"uncovered": [...]}` on violations, or `{}` on clean/error — never raises.
<!-- trie:end -->