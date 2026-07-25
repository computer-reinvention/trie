---
trie_version: 0.1.9
source: trie/edits/pipeline.py
file_fingerprint: a9bc4da648df0417510c1b627331dd4b2c402ce8b3683ab9c492844e998c1766
last_synced_at: '2026-07-25T10:43:54Z'
description: 'The patch pipeline: an intent store, not a code generator.'
defines:
- kind: module
  qualified_name: trie/edits/pipeline:__module__
  lines: 1-202
- kind: constant
  qualified_name: trie/edits/pipeline:_SESSION_NOTE_STOPLIST
  lines: 31-31
- kind: constant
  qualified_name: trie/edits/pipeline:_SESSION_NOTE_MIN_CHARS
  lines: 32-32
- kind: function
  qualified_name: trie/edits/pipeline:session_note_ok
  lines: 35-44
- kind: function
  qualified_name: trie/edits/pipeline:_expand_callers
  lines: 47-78
- kind: function
  qualified_name: trie/edits/pipeline:preview_patches
  lines: 81-114
- kind: function
  qualified_name: trie/edits/pipeline:record_intent
  lines: 117-201
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
<!-- trie:section symbol=trie/edits/pipeline:preview_patches fingerprint=ed0ad870a7b008a2e2727be93c6bce0c9840e2e9dae58ae1d0398094c0172da6 body_fp=b84fcc72bbb9d635b1d3e88ab77dbae29f5a1e011cb1215aea1e014f544dd1a1 source_ref=93562620aac7b790c8dabcf8f01990451e22c9c3 role=domain -->
Return a read-only summary of pending patch notes and the call-graph blast radius of the symbols they touch.

- `patched_list`: sorted qualified names of symbols carrying pending notes
- `cascade_list`: sorted qualified names of upstream callers within cascade depth, excluding patched symbols
- `cascade_symbols` / `patched_symbols`: integer counts of each list
- `total_patches`: total note count across all patched symbols
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/pipeline:record_intent fingerprint=3cd5d6b04f553c0f7b4248833ec6526fb4e534fe63078d81a22d163c3c3977ac body_fp=5a2523947cb699c5ffa4e925efcb1f2aa0498cefb70ba09733e105fb2a980bf4 source_ref=93562620aac7b790c8dabcf8f01990451e22c9c3 role=orchestration -->
Archive all pending patch notes to the session log and clear the queue, without generating any code.

- `session_note`: required when `total > 1`; validated via `session_note_ok` (rejects empty, too-short, and stoplist words); returns `ok=False` with `"session_note_required"` otherwise.
- Returns a dict with `ok`, `recorded` count, `symbols` list, and a `next` advisory string.
<!-- trie:end -->