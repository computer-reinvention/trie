---
trie_version: 0.1.9
source: trie/intent_gate.py
file_fingerprint: da9fc12eca0eda8238923359cc145943e46714bb8ddba3eb8b98981c53dcf9b8
last_synced_at: '2026-07-25T11:48:28Z'
description: 'The intent gate: refuse commits when changed symbols carry no patch
  notes.'
defines:
- kind: module
  qualified_name: trie/intent_gate:__module__
  lines: 1-192
- kind: constant
  qualified_name: trie/intent_gate:MODIFIED
  lines: 36-36
- kind: constant
  qualified_name: trie/intent_gate:ADDED
  lines: 37-37
- kind: constant
  qualified_name: trie/intent_gate:REMOVED
  lines: 38-38
- kind: class
  qualified_name: trie/intent_gate:TouchedSymbol
  lines: 42-45
- kind: class
  qualified_name: trie/intent_gate:IntentReport
  lines: 49-57
- kind: method
  qualified_name: trie/intent_gate:IntentReport.ok
  lines: 56-57
- kind: function
  qualified_name: trie/intent_gate:_symbols_by_qname
  lines: 60-76
- kind: function
  qualified_name: trie/intent_gate:touched_symbols
  lines: 79-142
- kind: function
  qualified_name: trie/intent_gate:_covered_qnames
  lines: 145-181
- kind: function
  qualified_name: trie/intent_gate:evaluate
  lines: 184-191
incoming_refs: 4
outgoing_refs: 0
---
<!-- trie:section symbol=trie/intent_gate:__module__ fingerprint=9e1250a0aa1097f31e1890d650053028fe3a4312895ea493c0d41814d805a5bb body_fp=32402d30d37d1a98d6f7a6bb0a990fff5e380fdae3ef533a129318fa9d237961 source_ref=daed11eea0dee4cce5f3872141ff4d898f7cbb4e role=domain -->
Enforces intent coverage for commits by computing which symbols changed relative to HEAD and verifying each has a recorded patch note or session-log entry.

- `MODIFIED` / `ADDED` / `REMOVED`: status constants for `TouchedSymbol.status`
<!-- trie:end -->
<!-- trie:section symbol=trie/intent_gate:MODIFIED fingerprint=afcf0e1bb755453a728a553e52d96ff4aa3f68803673bbcfe799bc395b8712f0 body_fp=bc14ee780e6e673ee6920375bca95304e5e3b4c84df6d8cd6b1a53b4c3e25cb6 source_ref=daed11eea0dee4cce5f3872141ff4d898f7cbb4e role=model -->
Status constant indicating a symbol's normalized body changed between HEAD and the working tree.
<!-- trie:end -->
<!-- trie:section symbol=trie/intent_gate:ADDED fingerprint=040ba8e17fcf9d5ebec51f428b4c73cb38ce926e52f3c4c951e650738f4d1da7 body_fp=62e99ccd9171964d65b361ef8cf5e710aade987dcc5cbf6df89760da70f930eb source_ref=daed11eea0dee4cce5f3872141ff4d898f7cbb4e role=model -->
Sentinel string constant marking a symbol as newly introduced in the working tree.
<!-- trie:end -->
<!-- trie:section symbol=trie/intent_gate:REMOVED fingerprint=4183d6ef72eec8967ba59ab12a3b1a7fc54f70c3b12eb2b0d9da60140d669d1d body_fp=e4fd5362aa9506ec7a1489d7b5a5bf91f6381a86f125e87f4b3cfcfbbe91699a source_ref=daed11eea0dee4cce5f3872141ff4d898f7cbb4e role=model -->
Sentinel string marking a symbol that existed in HEAD but is absent from the working tree.
<!-- trie:end -->
<!-- trie:section symbol=trie/intent_gate:TouchedSymbol fingerprint=f47713908945ae0bbddb15dc8cef7a0f34004a0e4f52bbd1c4509d9f9ea8906f body_fp=d0bbe65b525924417887c23bb45b2b4ab11134c3df9a493b5543c2ac8f4c9c83 source_ref=daed11eea0dee4cce5f3872141ff4d898f7cbb4e role=model -->
Immutable dataclass representing a single symbol detected as changed relative to HEAD.

- `status`: one of `"modified"`, `"added"`, or `"removed"`
- `file`: source-root-relative path; working-tree side when the file exists
<!-- trie:end -->
<!-- trie:section symbol=trie/intent_gate:IntentReport fingerprint=f8415ea14f3efd61968cc5b48e67e178c40608aa04cb9571503fe4d76a2e170a body_fp=2cafaf337acc511a1be6b7a86f26a780cec3f5e7db32a8a494ccdc0e30cc6f7c source_ref=daed11eea0dee4cce5f3872141ff4d898f7cbb4e role=model -->
Frozen dataclass holding the outcome of one intent-gate evaluation.

- `touched`: all symbols whose normalized body changed relative to HEAD.
- `uncovered`: subset of `touched` lacking any recorded intent.
- `ok`: `True` when `uncovered` is empty; commit may proceed.
<!-- trie:end -->
<!-- trie:section symbol=trie/intent_gate:IntentReport.ok fingerprint=2ecf9cf58081cf9cd1d95a08577841ef9ae8608235c81c9aae0947c56eec956f body_fp=e2a98184a36a13cfb23ed5f6119e6a647992b856851cfc2ee7b1b471fcf06f0e source_ref=daed11eea0dee4cce5f3872141ff4d898f7cbb4e role=model -->
`IntentReport.ok` is `True` when no uncovered symbols exist in the report.
<!-- trie:end -->
<!-- trie:section symbol=trie/intent_gate:_symbols_by_qname fingerprint=c6345f8986e963f6e3cd9816f9c0b072d3deb7335c0416a6112113d5bdfa0066 body_fp=e637c0d61eaa4c56e2a9b5fe81783ff2388426fb009a16402df176f919ca8ebd source_ref=daed11eea0dee4cce5f3872141ff4d898f7cbb4e role=parsing -->
Extract a `{qname: body_normalized_hash}` mapping for all non-`__module__` symbols in one file, returning `{}` on any parse error.

- `source_text`: supply pre-fetched text (e.g. from git) instead of reading disk.
<!-- trie:end -->
<!-- trie:section symbol=trie/intent_gate:touched_symbols fingerprint=80adecbce951d98063193ec4b4198f25f0f8acf2650f18f45e159346cbd2ae8e body_fp=0833afbbdad64d9c21247580d1dc76f1f199bd8c59749227d206555da3b1f741 source_ref=daed11eea0dee4cce5f3872141ff4d898f7cbb4e role=domain -->
Return all `TouchedSymbol` entries whose `body_normalized_hash` differs between HEAD and the working tree, including untracked files.

- Returns `[]` when outside a git repo, HEAD is absent, or no in-scope files changed.
- Untracked files are fetched via `ls-files --others` and merged with `diff HEAD` output.
- Only files both indexable by the parse registry and within the configured scope are evaluated.
- Removed symbols (absent from working tree) are included with status `REMOVED`.
<!-- trie:end -->
<!-- trie:section symbol=trie/intent_gate:_covered_qnames fingerprint=5dd3d8624b2ff31cce83f62ca45993c310624c36b8b83b1622f94e853332d95d body_fp=2ea03e5a8621a70e87f3098d961e1c39b00c6bd1aedcb344dc6032984db344e9 source_ref=fb27ca1add22435480f62d8a4c69ac79f56f752e role=domain -->
Return the set of qnames that have intent recorded for the upcoming commit, drawn from pending patch notes in the store and rows already consumed into the current HEAD's uncommitted digest entry.

- `config`: used to locate the diffs directory for digest lookup.
<!-- trie:end -->
<!-- trie:section symbol=trie/intent_gate:evaluate fingerprint=0ad9d38cfd26450c75c548b56ae70ac95c0dbc370be4fc595f187146ff5973bf body_fp=86516846e89b64b4caad6e5e242b4824e0ab36841f71e500f8cef65158562572 source_ref=0c60adcffc4cd3b694a3fe16398c634c7803ca05 role=domain -->
Compute an `IntentReport` by diffing touched symbols against covered qnames for the current commit window.
<!-- trie:end -->