---
trie_version: 0.1.0
source: trie/parse/references.py
file_fingerprint: eed188fddba8106bfbc20fc06b846e50088aab906f4d2690d3fab9228072a88f
last_synced_at: '2026-05-16T11:46:42Z'
description: Reference extraction via tree-sitter.
defines:
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
incoming_refs: 22
outgoing_refs: 9
---
<!-- trie:section symbol=trie/parse/references:Reference fingerprint=be66059ea554ea6d31cdeb5487f51707421e9c4c7858b8f82520c5a8ef2093de body_fp=5202bf2a195e34d954c9ca625ba30dd28b6a8c56cdfa4b10800b5c981cac7abb source_ref=49621fd1c7ec843b407b1123564512bc18c4a78c -->
## `Reference`

Immutable dataclass representing a single directed edge from one symbol to another.

- `src_qname`: qualified name of the referencing symbol (e.g. `src/foo:bar`)
- `target_qname`: qualified name of the resolved target; persisted as string before DB lookup
<!-- trie:end -->

<!-- trie:section symbol=trie/parse/references:FileData fingerprint=d1e4f5799633450224d7f7fcf994c834a43d825b45a9734ebef2a7033ec8373e body_fp=1f910d86b5e7e7c449ec1ef0ba6ccfb87a57874e35e03067c470ac605b262d43 source_ref=49621fd1c7ec843b407b1123564512bc18c4a78c -->
## `FileData`

Holds symbols and outbound references extracted from one file in a single tree-sitter parse.
<!-- trie:end -->

<!-- trie:section symbol=trie/parse/references:extract_file_data fingerprint=9d2cbdf6af58a3d0716ed3e066ba4a263123ac990289dd09ca5cf255a8b713a2 body_fp=a7fd2dc07268b7b5a1b968e6b316bd7cb8314ff3f5b57508b89f2eeabafdc25c source_ref=c6775babce628ee17704cd01d13e5bd434d47d37 -->
## `extract_file_data(file_path: Path, source_root: Path | None = None) -> FileData`

Parse a Python file once and return all its symbols and outbound references.

- `source_root`: used to compute qualified names; defaults to `file_path.parent`.
<!-- trie:end -->

<!-- trie:section symbol=trie/parse/references:_collect_imports fingerprint=2331c5c458cf82625623bc08d2dffc4a3ce446c63604d19b7ebc8807e7149e7a body_fp=f70b9ad79099ea3808d38a016f63343cad8b670df7403871e78676633c007c0a source_ref=c6775babce628ee17704cd01d13e5bd434d47d37 -->
## `_collect_imports(root: Node, source: bytes) -> _ImportBindings`

Build symbol and module binding tables for all import statements in the module.

- Returns `_ImportBindings` with two dicts: `symbols` (from-import name → qname) and `modules` (plain-import name → module path).
- `symbols`: maps local names from `from X import Y` to `"module/path:name"`.
- `modules`: maps local names from `import X` (or aliases) to slash-separated module paths.
- Skips relative imports.
<!-- trie:end -->

<!-- trie:section symbol=trie/parse/references:_collect_identifier_names fingerprint=14e61530854ad003a4661c28eecd812b0f64dc8512a51897f73a102d433144fc body_fp=08048a7727373f6c9e05170e261a28dd6199eb34d3285eb25cee4566593a7ac9 source_ref=49621fd1c7ec843b407b1123564512bc18c4a78c -->
## `_collect_identifier_names(node: Node, source: bytes) -> set[str]`

Return all identifier names mentioned within a node's subtree via recursive walk.

- Includes plain identifiers, attribute-expression names, and call targets.
- Skips comment nodes entirely; type-annotation identifiers are included as noise.
<!-- trie:end -->

<!-- trie:section symbol=trie/parse/references:_find_node_for_symbol fingerprint=d28e2391caa09aeaa59c30d0cd7f1a91e4021635f2a7564303231a0c2e53b80e body_fp=7152a6ecfe5ad1bf698493c82e7ebdd6a4534f5aadb64459ae98fa71a62be116 source_ref=49621fd1c7ec843b407b1123564512bc18c4a78c -->
## `_find_node_for_symbol(root: Node, symbol: Symbol) -> Node | None`

Locate the tree-sitter `function_definition` or `class_definition` node matching `symbol` by start line.

- `symbol.start_line`: 1-based line number used for matching against node start points.
- Returns the decorated-stripped node, or `None` if no match is found.
- Searches top-level children and one level into class bodies.
<!-- trie:end -->

<!-- trie:section symbol=trie/parse/references:_ImportBindings fingerprint=258ba3eed612857752238ff104e7750b9c3c96518a8d5da922d56f34c4d7d883 body_fp=fff441c60d36798d387f9ab690188c88ba037ddbcab8098818ca4cb9a92d98b1 source_ref=c6775babce628ee17704cd01d13e5bd434d47d37 -->
## `_ImportBindings(symbols: dict[str, str], modules: dict[str, str])`

Pair of binding tables produced by walking a module's import statements once.

- `symbols`: maps local name from `from X import Y` to fully-qualified target qname.
- `modules`: maps local name from `import X` to slash-separated module path; resolves only via attribute access.
<!-- trie:end -->

<!-- trie:section symbol=trie/parse/references:_absorb_from_import fingerprint=f44bc5cf3570282d83eb29c0e88f1bc4f2635353a7df45f310381378d4ffd3c5 body_fp=64ad2067ff4b8d1c1947e84f616c7c88561c00c8711e6a437b0ead35df25f6a6 source_ref=c6775babce628ee17704cd01d13e5bd434d47d37 -->
## `_absorb_from_import(child: Node, source: bytes, symbols: dict[str, str], modules: dict[str, str] | None = None) -> None`

Populate `symbols` (and optionally `modules`) from one `from X import Y` AST node.

- `modules`: when provided, also registers each imported name as a candidate module binding to handle submodule-or-value ambiguity.
<!-- trie:end -->

<!-- trie:section symbol=trie/parse/references:_absorb_plain_import fingerprint=8be0e860e35c788cf1af00254ccccfa18c31d3fabc837b9233f29d6cd7a9d8ec body_fp=b1c523fc33907937eded59e444605405fb6d12999c7b17c9b9197ef9368c8773 source_ref=c6775babce628ee17704cd01d13e5bd434d47d37 -->
## `_absorb_plain_import(child: Node, source: bytes, modules: dict[str, str]) -> None`

Populate `modules` from one `import X[, Y as alias, ...]` statement.

- `child`: tree-sitter node of type `import_statement`.
- For `import foo.bar`, registers both `"foo.bar" → "foo/bar"` and `"foo" → "foo"`.
- Aliased imports (`import foo.bar as fb`) register only the alias key.
<!-- trie:end -->

<!-- trie:section symbol=trie/parse/references:_collect_attribute_accesses fingerprint=1e2dee9c514469b945c5482fcd23f95801a61214bd30db5296208beb7f118535 body_fp=9082663b8b89b0a41017566d5dbf14a07472f06732ff68d3ca20fa56c0556138 source_ref=c6775babce628ee17704cd01d13e5bd434d47d37 -->
## `_collect_attribute_accesses(node: Node, source: bytes) -> set[tuple[str, str]]`

Return all `(base, attr)` pairs for every `<base>.<attr>` access in the subtree, including both levels of chained accesses.

- Chained `a.b.c` yields `("a", "b")` and `("a.b", "c")`.
- Skips comment and string nodes.
- Only emits pairs where the object is an identifier or attribute node.
<!-- trie:end -->

<!-- trie:section symbol=trie/parse/references:_dotted_text fingerprint=b9ce22d23f574b321e6e8dfd4266a20a0bcb3b21de9d37d399b8339f4b1beda6 body_fp=01ec259f3f5966c545903b03fe7adee1c2a1502e3369943379870b27b5660886 source_ref=c6775babce628ee17704cd01d13e5bd434d47d37 -->
## `_dotted_text(node: Node, source: bytes) -> str`

Render an `identifier` or nested `attribute` AST node as a dotted name string (e.g. `"a.b.c"`).

- Returns `""` for unrecognised node shapes (calls, subscripts, etc.).
<!-- trie:end -->