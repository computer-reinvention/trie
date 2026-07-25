---
trie_version: 0.1.9
source: trie/pending_intent.py
file_fingerprint: a847b486b8fa398450f75b4b44b0d1cdfc67e3c4aea729f513da9ed44e7c85f4
last_synced_at: '2026-07-25T11:31:00Z'
description: 'Pending intent: the between-apply-and-commit half of the intent ledger.'
defines:
- kind: module
  qualified_name: trie/pending_intent:__module__
  lines: 1-140
- kind: constant
  qualified_name: trie/pending_intent:PENDING_BASENAME
  lines: 38-38
- kind: constant
  qualified_name: trie/pending_intent:_HEADER
  lines: 40-43
- kind: constant
  qualified_name: trie/pending_intent:_ROW_RE
  lines: 46-46
- kind: constant
  qualified_name: trie/pending_intent:_SESSION_RE
  lines: 47-47
- kind: constant
  qualified_name: trie/pending_intent:_NO_SESSION
  lines: 48-48
- kind: function
  qualified_name: trie/pending_intent:pending_path
  lines: 51-52
- kind: function
  qualified_name: trie/pending_intent:_flatten
  lines: 55-57
- kind: function
  qualified_name: trie/pending_intent:append_intent
  lines: 60-98
- kind: function
  qualified_name: trie/pending_intent:read_intent
  lines: 101-134
- kind: function
  qualified_name: trie/pending_intent:consume_intent
  lines: 137-139
incoming_refs: 11
outgoing_refs: 0
---
<!-- trie:section symbol=trie/pending_intent:__module__ fingerprint=74bb84831395215666728144b8f9aa135546730c7b60eb8d432b84cefd6827ff body_fp=49dfcb25aa17681d1292cd7a12a2ff48940ab5069f7e64f1382e8f118f6baca2 source_ref=8ca0362d8210cee7171566776347842371bb23e3 role=persistence -->
Manages the pending-intent markdown file that bridges `patch apply` and the next commit's digest entry.

- `PENDING_BASENAME`: filename `.pending.md`, dot-prefixed to hide from `*.md` glob consumers
- `_HEADER`: comment block written once when the file is created
- `_ROW_RE`: parses a single bullet row into `op`, `qname`, and optional `note`
- `_SESSION_RE`: parses a session heading line into its note text
- `_NO_SESSION`: sentinel string substituted when no session note is provided
<!-- trie:end -->
<!-- trie:section symbol=trie/pending_intent:PENDING_BASENAME fingerprint=0bf121832c3c37fb7b8c7896d9e4f32a4401ecc51be74310d574299c142e9826 body_fp=f5333d3cc6e979b35e0e445c754dbd33dd491ccffb8f01732d0496d07faae031 source_ref=8ca0362d8210cee7171566776347842371bb23e3 role=config -->
Filename constant for the pending intent file written inside the digest archive directory.
<!-- trie:end -->
<!-- trie:section symbol=trie/pending_intent:_HEADER fingerprint=5e0eea81238fb26400226316e38ec29eebf1c198432601dcf803bbae395781d1 body_fp=7b4d3287e2e0e09f76bad8936b9992fa1152d1b48d7e6a5d8540a75e09c5f4e6 source_ref=8ca0362d8210cee7171566776347842371bb23e3 role=config -->
Markdown comment block written at the top of a newly created pending intent file to warn humans not to edit it.
<!-- trie:end -->
<!-- trie:section symbol=trie/pending_intent:_ROW_RE fingerprint=53ec7f9f0eb7b61dc1292417e2a8b60417a23404303c7ab431deb7e8d9e9cdee body_fp=675dbb3f77870e3fdd84d8c542561159408b1a42444327eb3b7de606100ff19b source_ref=8ca0362d8210cee7171566776347842371bb23e3 role=parsing -->
Compiled regex matching a single pending-file bullet line, capturing `op`, `qname`, and optional `note`.
<!-- trie:end -->
<!-- trie:section symbol=trie/pending_intent:_SESSION_RE fingerprint=cd06913af41027a669a1ee5f626a081993d6add74e6ee1b3cb375444756a5322 body_fp=ae5dfdf4e0d8e535536ea383b31d1c4abd3bf95ca1f1f946f9adba1a0c572160 source_ref=8ca0362d8210cee7171566776347842371bb23e3 role=parsing -->
Compiled regex matching a pending-file session heading line, capturing everything after `## ` into the named group `note`.
<!-- trie:end -->
<!-- trie:section symbol=trie/pending_intent:_NO_SESSION fingerprint=ac99ab33a9026cc314c979ba613597990262cfe5c329df9ccaf30dd128daa8f8 body_fp=d6ccd98150ac393dba3b2c9f814f843b610a400242235b4a3b1fa60612a5c115 source_ref=8ca0362d8210cee7171566776347842371bb23e3 role=config -->
Fallback session-note string written to the pending file when no session note is provided.
<!-- trie:end -->
<!-- trie:section symbol=trie/pending_intent:pending_path fingerprint=233dc9aae207e3ad8749506554c3ccb50e595f99f5ab28480a698f44b805e353 body_fp=93a13661e64e8672a38f5bb6a49be9c5cdc0cbe9a20f35f50ac25989bbd839dc source_ref=8ca0362d8210cee7171566776347842371bb23e3 role=util -->
Return the absolute `Path` to the pending intent file within the project's diffs directory.
<!-- trie:end -->
<!-- trie:section symbol=trie/pending_intent:_flatten fingerprint=d1f3e37dbff2de814055f44f4e13f095adf8d58b0205f4dec731466e52b13999 body_fp=1705e6cb9bf5edf1c2b5ad284427ced9863c5f069b42c8df300b9b26c6ae2e8e source_ref=8ca0362d8210cee7171566776347842371bb23e3 role=util -->
Collapse `text` to a single whitespace-normalised line, mirroring the gate applied to digest bullets.
<!-- trie:end -->
<!-- trie:section symbol=trie/pending_intent:append_intent fingerprint=7489f0ec995a1a4599c258380ff6b22a37c11de1dd384016dfa8c0822a619269 body_fp=5c5194276b1da7b4aba1c850a2589168691fad8ae109b1626e908a32d2ba819b source_ref=8ca0362d8210cee7171566776347842371bb23e3 role=io -->
Append intent rows under a session heading to the pending markdown file, creating it with a header if absent.

- `rows`: list of `{qname, op, notes, reasons}` dicts; notes and reasons are whitespace-collapsed before writing.
- `session_note`: written as a `##` heading; defaults to `"(no session note)"` if empty.
- Returns the `Path` of the pending file written to.
<!-- trie:end -->
<!-- trie:section symbol=trie/pending_intent:read_intent fingerprint=6b0fafa131ebf57f4a9f764cf1d9785ac43875e6f4038a2bed67423fbf47735e body_fp=a3d0226243228f413f66f4e61162acbfa60cac5b747e1d510670396d4c76251b source_ref=8ca0362d8210cee7171566776347842371bb23e3 role=parsing -->
Parse the pending intent file and return rows in digest-evidence shape.

- Returns `[]` if the file is absent or unreadable via `OSError`.
- Each row: `{qname, op, notes: [str], reasons: [], session_note}` — matches `collect_session_diff` output.
- `reasons` is always an empty list; reasons are not stored in the pending file format.
<!-- trie:end -->
<!-- trie:section symbol=trie/pending_intent:consume_intent fingerprint=d3e6c0383a5ff13eb9fd9cfc3b147df402be12e29ce6ae76cf52647e76f96a0e body_fp=cbc9cac906d4432ea38fa192d3b594c1be0e10961074d7b3c94c7352a224a465 source_ref=8ca0362d8210cee7171566776347842371bb23e3 role=io -->
Delete the `.pending.md` file after its contents have been committed into the digest archive.
<!-- trie:end -->