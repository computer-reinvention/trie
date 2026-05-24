---
trie_version: 0.1.2
source: trie/parse/references.py
file_fingerprint: eed188fddba8106bfbc20fc06b846e50088aab906f4d2690d3fab9228072a88f
last_synced_at: '2026-05-23T23:50:52Z'
description: Reference extraction via tree-sitter.
defines:
- kind: module
  qualified_name: trie/parse/references:__module__
  lines: 1-371
- kind: class
  qualified_name: trie/parse/references:Reference
  lines: 50-58
- kind: class
  qualified_name: trie/parse/references:FileData
  lines: 62-66
- kind: class
  qualified_name: trie/parse/references:_ImportBindings
  lines: 70-88
- kind: function
  qualified_name: trie/parse/references:_collect_imports
  lines: 91-117
- kind: function
  qualified_name: trie/parse/references:_absorb_from_import
  lines: 120-161
- kind: function
  qualified_name: trie/parse/references:_absorb_plain_import
  lines: 164-191
- kind: function
  qualified_name: trie/parse/references:_collect_identifier_names
  lines: 194-212
- kind: function
  qualified_name: trie/parse/references:_collect_attribute_accesses
  lines: 215-253
- kind: function
  qualified_name: trie/parse/references:_dotted_text
  lines: 256-274
- kind: function
  qualified_name: trie/parse/references:_find_node_for_symbol
  lines: 277-299
- kind: function
  qualified_name: trie/parse/references:extract_file_data
  lines: 302-367
- kind: constant
  qualified_name: trie/parse/references:__all__
  lines: 370-370
incoming_refs: 22
outgoing_refs: 9
---
<!-- trie:section symbol=trie/parse/references:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=4654a04af28a14e45631c790aa4546d3436e035935b5118e321368128071f79f source_ref=c6775babce628ee17704cd01d13e5bd434d47d37 -->
## `trie/parse/references`

Extract outbound symbol references from Python source files using tree-sitter heuristics.

- `Reference`: immutable edge record linking source qname to target qname
- `FileData`: combined symbols + references from a single parse pass
- `extract_file_data`: primary public entry point; returns a `FileData`
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/references:Reference fingerprint=be66059ea554ea6d31cdeb5487f51707421e9c4c7858b8f82520c5a8ef2093de body_fp=70edc405656c71508eb145cd6a7022d922cf24620b323820679af79e0d22a86e source_ref=c6775babce628ee17704cd01d13e5bd434d47d37 -->
## `Reference(src_qname: str, target_qname: str)`

Immutable record of one directed edge from a source symbol to a target symbol.

- `target_qname`: slash/colon-qualified name (e.g. `src/foo:bar`), persisted before DB lookup.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/references:FileData fingerprint=d1e4f5799633450224d7f7fcf994c834a43d825b45a9734ebef2a7033ec8373e body_fp=f36413a273b82d3b794aafe3c69523a898e2bf96ce1610addde4c1977f35f744 source_ref=c6775babce628ee17704cd01d13e5bd434d47d37 -->
## `FileData`

Immutable container for symbols and outbound references extracted from one file in a single tree-sitter parse.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/references:_ImportBindings fingerprint=258ba3eed612857752238ff104e7750b9c3c96518a8d5da922d56f34c4d7d883 body_fp=c8b86eb02652a71ddcc7dc88b72a6063a8fd8ca79f24dd596df38df18f986502 source_ref=c6775babce628ee17704cd01d13e5bd434d47d37 -->
## `_ImportBindings(symbols: dict[str, str], modules: dict[str, str])`

Pair of binding tables produced by walking a module's import statements once.

- `symbols`: local name → fully-qualified qname (`"emit"` → `"trie/telemetry:emit"`); from `from X import Y`.
- `modules`: local name → module path (`"telemetry"` → `"trie/telemetry"`); from `import X`; resolved only via attribute access.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/references:_collect_imports fingerprint=2331c5c458cf82625623bc08d2dffc4a3ce446c63604d19b7ebc8807e7149e7a body_fp=1fa6fd95d698bb25f091be42823c287f4b9342513957436eddbf8c271d6ff2ad source_ref=c6775babce628ee17704cd01d13e5bd434d47d37 -->
## `_collect_imports(root: Node, source: bytes) -> _ImportBindings`

Walk a module's top-level import statements and build both symbol and module binding tables.

- `root`: tree-sitter root node of the parsed module
- Returns `_ImportBindings` with `symbols` (from-import locals) and `modules` (plain-import locals); relative imports are silently skipped
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/references:_absorb_from_import fingerprint=f44bc5cf3570282d83eb29c0e88f1bc4f2635353a7df45f310381378d4ffd3c5 body_fp=13453a187aaa7ddc814476c7fe9206ccbcae30de8c232ac5b3456a36ce3d69db source_ref=c6775babce628ee17704cd01d13e5bd434d47d37 -->
## `_absorb_from_import(child: Node, source: bytes, symbols: dict[str, str], modules: dict[str, str] | None = None) -> None`

Populate `symbols` (and optionally `modules`) from one `from X import Y` AST node.

- `modules`: when provided, each imported name is also registered as a candidate module binding; relative imports are silently skipped.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/references:_absorb_plain_import fingerprint=8be0e860e35c788cf1af00254ccccfa18c31d3fabc837b9233f29d6cd7a9d8ec body_fp=cb1cd63760dbc6c7e33f8de36f2b20de6d628456ff48656f6f8da7c2054d3bf9 source_ref=c6775babce628ee17704cd01d13e5bd434d47d37 -->
## `_absorb_plain_import(child: Node, source: bytes, modules: dict[str, str]) -> None`

Populate `modules` from one `import X` statement, registering dotted and head-only bindings.

- `import foo.bar` registers both `"foo.bar" → "foo/bar"` and `"foo" → "foo"`.
- `import foo.bar as fb` registers only `"fb" → "foo/bar"`.
- Relative imports (leading `.`) are skipped silently.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/references:_collect_identifier_names fingerprint=14e61530854ad003a4661c28eecd812b0f64dc8512a51897f73a102d433144fc body_fp=ec64aec364bd0f7d6fcd20ac60876095af4a1fbee40a5b34281e63a1c4e5990d source_ref=c6775babce628ee17704cd01d13e5bd434d47d37 -->
## `_collect_identifier_names(node: Node, source: bytes) -> set[str]`

Recursively walk a tree-sitter subtree and return every identifier string found, skipping comment nodes.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/references:_collect_attribute_accesses fingerprint=1e2dee9c514469b945c5482fcd23f95801a61214bd30db5296208beb7f118535 body_fp=ea72f621db53ac7e2ea312dc8d16e3837416376e50bf36564cdb5b773f44de26 source_ref=c6775babce628ee17704cd01d13e5bd434d47d37 -->
## `_collect_attribute_accesses(node: Node, source: bytes) -> set[tuple[str, str]]`

Walk a tree-sitter subtree and return all `(base, attr)` dotted-access pairs, including each level of chained accesses.

- `base`: dotted string of the object side, e.g. `"a"` or `"a.b"` for `a.b.c`
- Skips `comment` and `string` nodes; emits nothing for non-identifier/attribute object shapes
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/references:_dotted_text fingerprint=b9ce22d23f574b321e6e8dfd4266a20a0bcb3b21de9d37d399b8339f4b1beda6 body_fp=8ba2fc9700c0e7fe1e5a40768d3000ce714e711e11d6a8b3583c51c1fda0b8e2 source_ref=c6775babce628ee17704cd01d13e5bd434d47d37 -->
## `_dotted_text(node: Node, source: bytes) -> str`

Render a tree-sitter `identifier` or `attribute` subtree as a dotted string like `"a.b.c"`.

- Returns `""` for unrecognised node shapes (calls, subscripts, etc.).
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/references:_find_node_for_symbol fingerprint=d28e2391caa09aeaa59c30d0cd7f1a91e4021635f2a7564303231a0c2e53b80e body_fp=e14ee2b93bce851a8b2ebe6413f89f249df6dea420aee88dd24745da38bb1e82 source_ref=c6775babce628ee17704cd01d13e5bd434d47d37 -->
## `_find_node_for_symbol(root: Node, symbol: Symbol) -> Node | None`

Find the tree-sitter `function_definition` or `class_definition` node matching `symbol` by start line.

- Searches top-level nodes and one level deep (methods inside classes).
- Strips decorators via `_undecorate` before comparing start lines.
- Returns `None` if no matching node is found.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/references:extract_file_data fingerprint=9d2cbdf6af58a3d0716ed3e066ba4a263123ac990289dd09ca5cf255a8b713a2 body_fp=52842b94b359f22d95eb086097b5609ebdcb1a18244cc0cdfcd09bb311fb45a0 source_ref=c6775babce628ee17704cd01d13e5bd434d47d37 -->
## `extract_file_data(file_path: Path, source_root: Path | None = None) -> FileData`

Parse a Python file once and return all its symbols and outbound reference edges.

- `source_root`: used to compute qualified names; defaults to the file's parent directory.
- Candidate edges to unresolved qnames are emitted without filtering; the store drops them.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/references:__all__ fingerprint=9bc78c305b022f72da1cfdbc0b7349422140eb7e0e905460ac531538b0e5f20c body_fp=063c2c43a34233c9d55c78908e57771c82f16826c2430a60cb79347cabfa4869 source_ref=c6775babce628ee17704cd01d13e5bd434d47d37 -->
## `__all__ = ["FileData", "Reference", "extract_file_data"]`

Declares the module's public API surface.
<!-- trie:end -->