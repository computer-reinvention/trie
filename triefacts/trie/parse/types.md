---
trie_version: 0.3.0
source: trie/parse/types.py
file_fingerprint: c1b2312fa3a2602da9627318306eeb54f143b570676855c0c950874553a23fc3
last_synced_at: '2026-08-02T21:19:06Z'
description: Language-neutral value types for the parse layer.
defines:
- kind: module
  qualified_name: trie/parse/types:__module__
  lines: 1-106
- kind: constant
  qualified_name: trie/parse/types:KINDS
  lines: 29-40
- kind: constant
  qualified_name: trie/parse/types:SIGNATURELESS_KINDS
  lines: 48-51
- kind: constant
  qualified_name: trie/parse/types:EDGE_KINDS
  lines: 54-61
- kind: class
  qualified_name: trie/parse/types:Symbol
  lines: 65-79
  signature: class Symbol
- kind: class
  qualified_name: trie/parse/types:Reference
  lines: 83-97
  signature: class Reference
- kind: class
  qualified_name: trie/parse/types:FileData
  lines: 101-105
  signature: class FileData
incoming_refs: 67
outgoing_refs: 0
---
<!-- trie:section symbol=trie/parse/types:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=c29e030a893ddafae42df118c79e62c9aa6f229f78d7bee2ee5a0cdb7bad8b83 source_ref=a174d61d063c82dd1e024ea9f6b0f62628a9d783 role=model -->
Defines language-neutral parse-layer contracts: `Symbol`, `Reference`, `FileData`, `KINDS`, and `EDGE_KINDS`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/types:KINDS fingerprint=b0b623c5c21533a01b5e3c1565e367da8df846aa35f855a5c926c965fcd6fde9 body_fp=f46a309fa9bbc31c54823194230eb1f0e44463213762289f4408f7e9ef9c031b source_ref=a174d61d063c82dd1e024ea9f6b0f62628a9d783 role=config -->
Canonical tuple of all valid symbol-kind strings used across every language backend and validator.

- Values: `"function"`, `"class"`, `"method"`, `"constant"`, `"module"`, `"interface"`, `"type"`, `"enum"`, `"enum_member"`, `"property"`
- A kind is included only if the construct can be an independent reference target in the graph.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/types:SIGNATURELESS_KINDS fingerprint=1e495c627ce7c15b3472e7eb0ad4ef4eadf59004e974e2ead0e457a12e89c752 body_fp=d0e4e680cf920cf23c89076917a37143a89f8d01ca365500bf0c51b3aaa17feb source_ref=7cd6544506e6484562e542a0bd275b8894540642 role=config -->
Tuple of `KINDS` values whose `Symbol.signature` is synthetic or redundant, causing consumers to skip signature emission for these symbols.

- `"module"`: signature is a fabricated one-line summary of residual module-level code
- `"constant"`: signature is the raw assignment statement
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/types:EDGE_KINDS fingerprint=54b527669ce61dc0c826341a01825a022d7af5341d32bfc8f3d16d176a6a1f4b body_fp=b2af9e5eafc02fadbbcf992cb7d5b0dde585aeb5b01065efad48bda4c901f572 source_ref=a174d61d063c82dd1e024ea9f6b0f62628a9d783 role=config -->
Defines the canonical vocabulary of typed edge kinds used in `Reference.kind` (AGM graph edges).
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/types:Symbol fingerprint=67410b76908def7ec7521baef1e77f8fa17f7b64e4da871a7c1b3eac081c35e0 body_fp=494c2f9f3e8e23c7b9e4bf55de67a899055d9d126b75ba580098d597c7ea35d4 source_ref=a174d61d063c82dd1e024ea9f6b0f62628a9d783 role=model -->
## `class Symbol`

Immutable dataclass representing a single parsed symbol emitted by a language backend.

- `kind`: one of the `KINDS` vocabulary strings
- `file_path`: source-root-relative path, e.g. `"src/foo.py"`
- `start_line` / `end_line`: 1-indexed, end is inclusive
- `parent_class`: set only for `method`, `enum_member`, and `property` kinds; holds the container's name
- `decorators`: raw decorator lines, e.g. `("@classmethod",)`
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/types:Reference fingerprint=bc7d710ddc71b093d46034ec42adfc79d5722545fe3088df3dffe543002d1c8f body_fp=bdbdca899fefa2c44a952e260ac2a461da7150bf44863f446dc286599acfa6e2 source_ref=3e644d475721db755030fe34fb383847776db950 role=model -->
## `class Reference`

Immutable dataclass representing a single typed, outbound edge from one symbol to another within a parsed file.

- `target_qname`: resolved qualified name persisted as a string before DB lookup of `symbol_id`
- `kind`: AGM edge type from `EDGE_KINDS`; defaults to `"calls"`, ambiguous bare-identifier uses resolve to `"references"`
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/types:FileData fingerprint=d1e4f5799633450224d7f7fcf994c834a43d825b45a9734ebef2a7033ec8373e body_fp=63e057abe13eef2fc188df29b1f8d99c013c9204cfe392020dba27d1c2d97f2f source_ref=a174d61d063c82dd1e024ea9f6b0f62628a9d783 role=model -->
## `class FileData`

Immutable container holding all `Symbol`s and `Reference`s extracted from one file during a tree-sitter parse.
<!-- trie:end -->