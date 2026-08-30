---
trie_version: 0.3.0
source: trie/parse/types.py
file_fingerprint: 138f241b6490d208ec0f54aefd24c478258fa57b3cd5af0761bac3b9d7f05fbf
last_synced_at: '2026-08-30T02:41:10Z'
description: Language-neutral value types for the parse layer.
defines:
- kind: module
  qualified_name: trie/parse/types:__module__
  lines: 1-107
- kind: constant
  qualified_name: trie/parse/types:KINDS
  lines: 29-40
- kind: constant
  qualified_name: trie/parse/types:SIGNATURELESS_KINDS
  lines: 48-51
- kind: constant
  qualified_name: trie/parse/types:EDGE_KINDS
  lines: 54-62
- kind: class
  qualified_name: trie/parse/types:Symbol
  lines: 66-80
  signature: class Symbol
- kind: class
  qualified_name: trie/parse/types:Reference
  lines: 84-98
  signature: class Reference
- kind: class
  qualified_name: trie/parse/types:FileData
  lines: 102-106
  signature: class FileData
incoming_refs: 0
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
<!-- trie:section symbol=trie/parse/types:EDGE_KINDS fingerprint=b20c4cf75601dc5442fa063bfeff664ca5b0754a7cd0c7d4339785e439500921 body_fp=d2cd0b7a4cd15bbd6983c3996a9ce3df1bfaaa073026bf29136d51f3fe1dc0a1 source_ref=8fbd1e072b32b551cfd893e7053f52632b54adc7 role=model -->
Defines the canonical vocabulary of typed edge kinds used in `Reference.kind` (AGM graph edges), including `cross_language_call` for API boundary edges between languages.
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