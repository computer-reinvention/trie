---
trie_version: 0.3.0
source: trie/intent_gate.py
file_fingerprint: f14d630e86019dd7aac53a8c5c9be7ae2a0d5115b5bdd614bfaf493c704cafe7
last_synced_at: '2026-07-29T17:55:00Z'
description: 'The intent gate: refuse commits when changed symbols carry no patch notes.'
defines:
- kind: module
  qualified_name: trie/intent_gate:__module__
  lines: 1-214
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
  signature: class TouchedSymbol
- kind: class
  qualified_name: trie/intent_gate:IntentReport
  lines: 49-57
  signature: class IntentReport
- kind: method
  qualified_name: trie/intent_gate:IntentReport.ok
  lines: 56-57
  signature: def ok(self) -> bool
- kind: function
  qualified_name: trie/intent_gate:_symbols_by_qname
  lines: 60-76
  signature: 'def _symbols_by_qname( file_path: Path, source_root: Path, *, source_text: str | None = None ) -> dict[str, str]'
- kind: function
  qualified_name: trie/intent_gate:touched_symbols
  lines: 79-142
  signature: 'def touched_symbols(project_root: Path, config: Config) -> list[TouchedSymbol]'
- kind: function
  qualified_name: trie/intent_gate:_covered_qnames
  lines: 145-181
  signature: 'def _covered_qnames(project_root: Path, config: Config, store: Store) -> set[str]'
- kind: function
  qualified_name: trie/intent_gate:_parent_qname
  lines: 184-193
  signature: 'def _parent_qname(qname: str) -> str | None'
- kind: function
  qualified_name: trie/intent_gate:evaluate
  lines: 196-213
  signature: 'def evaluate(project_root: Path, config: Config, store: Store) -> IntentReport'
incoming_refs: 7
outgoing_refs: 8
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
<!-- trie:section symbol=trie/intent_gate:TouchedSymbol fingerprint=f47713908945ae0bbddb15dc8cef7a0f34004a0e4f52bbd1c4509d9f9ea8906f body_fp=2213e62eab69c98935392bc2f70f19c573c679eb2139659ebc9e4bb98b3d6a86 source_ref=daed11eea0dee4cce5f3872141ff4d898f7cbb4e role=model -->
## `class TouchedSymbol`

Immutable dataclass representing a single symbol detected as changed relative to HEAD.

- `status`: one of `"modified"`, `"added"`, or `"removed"`
- `file`: source-root-relative path; working-tree side when the file exists
<!-- trie:end -->
<!-- trie:section symbol=trie/intent_gate:IntentReport fingerprint=f8415ea14f3efd61968cc5b48e67e178c40608aa04cb9571503fe4d76a2e170a body_fp=5926dc92a1ab4d8a4c13fb6d2640c3008a04d7088dd9d242bbdc04db8b1f1295 source_ref=daed11eea0dee4cce5f3872141ff4d898f7cbb4e role=model -->
## `class IntentReport`

Frozen dataclass holding the outcome of one intent-gate evaluation.

- `touched`: all symbols whose normalized body changed relative to HEAD.
- `uncovered`: subset of `touched` lacking any recorded intent.
- `ok`: `True` when `uncovered` is empty; commit may proceed.
<!-- trie:end -->
<!-- trie:section symbol=trie/intent_gate:IntentReport.ok fingerprint=2ecf9cf58081cf9cd1d95a08577841ef9ae8608235c81c9aae0947c56eec956f body_fp=e4b804361e14cff518e08bbd120ca0d3ee8a412b0cef1596c45c2679ccfbe8e0 source_ref=daed11eea0dee4cce5f3872141ff4d898f7cbb4e role=model -->
## `def ok(self) -> bool`

`IntentReport.ok` is `True` when no uncovered symbols exist in the report.
<!-- trie:end -->
<!-- trie:section symbol=trie/intent_gate:_symbols_by_qname fingerprint=c6345f8986e963f6e3cd9816f9c0b072d3deb7335c0416a6112113d5bdfa0066 body_fp=0810a4e23c75da35309989f4067e5f53afcc73f04cf91b2ff4c04cf9c1a57314 source_ref=daed11eea0dee4cce5f3872141ff4d898f7cbb4e role=parsing -->
## `def _symbols_by_qname( file_path: Path, source_root: Path, *, source_text: str | None = None ) -> dict[str, str]`

Extract a `{qname: body_normalized_hash}` mapping for all non-`__module__` symbols in one file, returning `{}` on any parse error.

- `source_text`: supply pre-fetched text (e.g. from git) instead of reading disk.
<!-- trie:end -->
<!-- trie:section symbol=trie/intent_gate:touched_symbols fingerprint=80adecbce951d98063193ec4b4198f25f0f8acf2650f18f45e159346cbd2ae8e body_fp=7959b166ecac3b8457733d56bc97da35ed7bb79512047c42f1df2478cedb46ec source_ref=daed11eea0dee4cce5f3872141ff4d898f7cbb4e role=domain -->
## `def touched_symbols(project_root: Path, config: Config) -> list[TouchedSymbol]`

Return all `TouchedSymbol` entries whose `body_normalized_hash` differs between HEAD and the working tree, including untracked files.

- Returns `[]` when outside a git repo, HEAD is absent, or no in-scope files changed.
- Untracked files are fetched via `ls-files --others` and merged with `diff HEAD` output.
- Only files both indexable by the parse registry and within the configured scope are evaluated.
- Removed symbols (absent from working tree) are included with status `REMOVED`.
<!-- trie:end -->
<!-- trie:section symbol=trie/intent_gate:_covered_qnames fingerprint=5dd3d8624b2ff31cce83f62ca45993c310624c36b8b83b1622f94e853332d95d body_fp=87e7dea67ff4f95d7de807fc1ff3b34e471b06278eabbd30c1b7aed3297a1757 source_ref=fb27ca1add22435480f62d8a4c69ac79f56f752e role=domain -->
## `def _covered_qnames(project_root: Path, config: Config, store: Store) -> set[str]`

Return the set of qnames that have intent recorded for the upcoming commit, drawn from pending patch notes in the store and rows already consumed into the current HEAD's uncommitted digest entry.

- `config`: used to locate the diffs directory for digest lookup.
<!-- trie:end -->
<!-- trie:section symbol=trie/intent_gate:_parent_qname fingerprint=a6d693609876b6d86f4fd27f263dd86d42d88c5f89f7d01effaf679e413262db body_fp=13b018ffdf9a1b1ff0ca385c8d0fc762f92004dd22410b00cc3204da28a56c72 source_ref=d66d954661ff3bcddb53ffe2ff4ef55136ca9381 role=util -->
## `def _parent_qname(qname: str) -> str | None`

Extract the owning-class qname from a method-shaped qname, returning `None` for module-level or non-dotted names.

- Splits only one level: `pkg/mod:Class.method` → `pkg/mod:Class`; deeper chains resolve to the top-level class within the module.
<!-- trie:end -->
<!-- trie:section symbol=trie/intent_gate:evaluate fingerprint=b8e069f6860b42b4be690a69bcc855c951435a94f9f507c90fe404f8dec58a45 body_fp=0b6432fe9d4ce4a71c857904398c2610b357410a6b7d2ba5a83a339ee5373adf source_ref=d66d954661ff3bcddb53ffe2ff4ef55136ca9381 role=domain -->
## `def evaluate(project_root: Path, config: Config, store: Store) -> IntentReport`

Compute an `IntentReport` by diffing touched symbols against covered qnames; a class-level note also covers its methods.
<!-- trie:end -->