---
trie_version: 0.1.9
source: trie/parse/types.py
file_fingerprint: 8b94352b6a4b9a947016ac1013cd439c1acf154f4f15852a43951f17786ea35f
last_synced_at: '2026-07-26T20:27:48Z'
description: Language-neutral value types for the parse layer.
defines:
- kind: module
  qualified_name: trie/parse/types:__module__
  lines: 1-95
- kind: constant
  qualified_name: trie/parse/types:KINDS
  lines: 29-40
- kind: constant
  qualified_name: trie/parse/types:EDGE_KINDS
  lines: 43-50
- kind: class
  qualified_name: trie/parse/types:Symbol
  lines: 54-68
- kind: class
  qualified_name: trie/parse/types:Reference
  lines: 72-86
- kind: class
  qualified_name: trie/parse/types:FileData
  lines: 90-94
incoming_refs: 25
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
<!-- trie:section symbol=trie/parse/types:EDGE_KINDS fingerprint=54b527669ce61dc0c826341a01825a022d7af5341d32bfc8f3d16d176a6a1f4b body_fp=b2af9e5eafc02fadbbcf992cb7d5b0dde585aeb5b01065efad48bda4c901f572 source_ref=a174d61d063c82dd1e024ea9f6b0f62628a9d783 role=config -->
Defines the canonical vocabulary of typed edge kinds used in `Reference.kind` (AGM graph edges).
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/types:Symbol fingerprint=67410b76908def7ec7521baef1e77f8fa17f7b64e4da871a7c1b3eac081c35e0 body_fp=9464ce990c32daecb7f2fa159e207efbdd4f8e2357df3998221d53a2e10a543f source_ref=a174d61d063c82dd1e024ea9f6b0f62628a9d783 role=model -->
Immutable dataclass representing a single parsed symbol emitted by a language backend.

- `kind`: one of the `KINDS` vocabulary strings
- `file_path`: source-root-relative path, e.g. `"src/foo.py"`
- `start_line` / `end_line`: 1-indexed, end is inclusive
- `parent_class`: set only for `method`, `enum_member`, and `property` kinds; holds the container's name
- `decorators`: raw decorator lines, e.g. `("@classmethod",)`
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/types:Reference fingerprint=bc7d710ddc71b093d46034ec42adfc79d5722545fe3088df3dffe543002d1c8f body_fp=d06cd34ed7dccc3dce51777542e285c629996a9a0aae73243be0b9cc1a845152 source_ref=3e644d475721db755030fe34fb383847776db950 role=model -->
Immutable dataclass representing a single typed, outbound edge from one symbol to another within a parsed file.

- `target_qname`: resolved qualified name persisted as a string before DB lookup of `symbol_id`
- `kind`: AGM edge type from `EDGE_KINDS`; defaults to `"calls"`, ambiguous bare-identifier uses resolve to `"references"`
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/types:FileData fingerprint=d1e4f5799633450224d7f7fcf994c834a43d825b45a9734ebef2a7033ec8373e body_fp=c4758d4fc86ac6a2025a651a4ab24fcda7e5958a35951717bbf6423a214d37b6 source_ref=a174d61d063c82dd1e024ea9f6b0f62628a9d783 role=model -->
Immutable container holding all `Symbol`s and `Reference`s extracted from one file during a tree-sitter parse.
<!-- trie:end -->