---
trie_version: 0.3.0
source: trie/parse/typescript_refs.py
file_fingerprint: 26c7bf67784e8f254ffeea4190afc1490099c7c90f5f4a8f31f3b4fe8648f443
last_synced_at: '2026-08-02T21:19:41Z'
description: TypeScript reference (edge) extraction via tree-sitter.
defines:
- kind: module
  qualified_name: trie/parse/typescript_refs:__module__
  lines: 1-353
- kind: constant
  qualified_name: trie/parse/typescript_refs:_KIND_RANK
  lines: 25-32
- kind: class
  qualified_name: trie/parse/typescript_refs:_Bindings
  lines: 35-45
  signature: class _Bindings
- kind: method
  qualified_name: trie/parse/typescript_refs:_Bindings.__init__
  lines: 43-45
  signature: def __init__(self) -> None
- kind: function
  qualified_name: trie/parse/typescript_refs:_collect_imports
  lines: 48-57
  signature: 'def _collect_imports( root: Node, source: bytes, *, from_file: Path, resolver: TsResolver ) -> _Bindings'
- kind: function
  qualified_name: trie/parse/typescript_refs:_specifier_string
  lines: 60-70
  signature: 'def _specifier_string(stmt: Node, source: bytes) -> str | None'
- kind: function
  qualified_name: trie/parse/typescript_refs:_absorb_import
  lines: 73-109
  signature: 'def _absorb_import( stmt: Node, source: bytes, b: _Bindings, *, from_file: Path, resolver: TsResolver ) -> None'
- kind: function
  qualified_name: trie/parse/typescript_refs:_absorb_reexport
  lines: 112-134
  signature: "def _absorb_reexport( stmt: Node, source: bytes, b: _Bindings, *, from_file: Path, resolver: TsResolver ) -> None: # `export { x, y } from \"./foo\"` \u2014 bind the names so a body using them links # through the barrel. Only when there is a source specifier."
- kind: function
  qualified_name: trie/parse/typescript_refs:_find_node_for_symbol
  lines: 137-151
  signature: 'def _find_node_for_symbol(root: Node, symbol: Symbol) -> Node | None'
- kind: function
  qualified_name: trie/parse/typescript_refs:_collect_call_names
  lines: 154-176
  signature: 'def _collect_call_names(node: Node, source: bytes) -> set[str]'
- kind: function
  qualified_name: trie/parse/typescript_refs:_collect_identifiers
  lines: 179-191
  signature: 'def _collect_identifiers(node: Node, source: bytes) -> set[str]'
- kind: function
  qualified_name: trie/parse/typescript_refs:_collect_namespace_uses
  lines: 194-210
  signature: 'def _collect_namespace_uses(node: Node, source: bytes) -> set[tuple[str, str]]'
- kind: function
  qualified_name: trie/parse/typescript_refs:_class_declaration_node
  lines: 213-220
  signature: 'def _class_declaration_node(node: Node) -> Node'
- kind: function
  qualified_name: trie/parse/typescript_refs:_heritage
  lines: 223-242
  signature: 'def _heritage(class_node: Node, source: bytes) -> tuple[list[str], list[str]]'
- kind: constant
  qualified_name: trie/parse/typescript_refs:_RESOLVER_CACHE
  lines: 251-251
- kind: function
  qualified_name: trie/parse/typescript_refs:_shared_resolver
  lines: 254-260
  signature: 'def _shared_resolver(source_root: Path) -> TsResolver'
- kind: function
  qualified_name: trie/parse/typescript_refs:extract_file_data
  lines: 263-344
  signature: 'def extract_file_data( file_path: Path, source_root: Path | None = None, *, resolver: TsResolver | None = None, ) -> FileData'
- kind: function
  qualified_name: trie/parse/typescript_refs:_resolve_name
  lines: 347-352
  signature: 'def _resolve_name(name: str, bindings: _Bindings, own_top_level: dict[str, str]) -> str | None'
incoming_refs: 5
outgoing_refs: 15
---
<!-- trie:section symbol=trie/parse/typescript_refs:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=cd20018010d4382cba971cbc94f6087414807f730595d7ca16aa7054c09fef42 source_ref=151b3686cf9470200bf8e00b72977ed3ea4702e5 role=parsing -->
Extracts TypeScript symbols and resolved outbound references from a single file using tree-sitter, mapping imports to project module keys via `TsResolver`.

- Edge kinds ranked: `imports` < `references` < `calls` < `inherits` / `implements` / `contains`
- Permissive: emits candidate edges for all plausible targets; the store drops unresolved ones
- Mirrors `trie/parse/references.py` for TypeScript
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript_refs:_KIND_RANK fingerprint=0f745e9e92003789fcc3f90c77c4a3bf6f2ab5ee1c75d4fe99d4527cc09b0f98 body_fp=3cf9f90b3b92e396a52e1c0ecaa50880334c118121ac8ba69f7acf9fd8cb59b2 source_ref=151b3686cf9470200bf8e00b72977ed3ea4702e5 role=config -->
Maps edge-kind strings to integer ranks so higher-priority kinds win when deduplicating edges via `add_edge`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript_refs:_Bindings fingerprint=10e8e5091559c972cb022172383f8965d6eea69879770b92f784de8eb5dc22b2 body_fp=f8db159c001bedf4897ebcb0b2b1f5c4242bcbdbd78d1b0718345b5f154c5f1d source_ref=151b3686cf9470200bf8e00b72977ed3ea4702e5 role=model -->
## `class _Bindings`

Hold local-name → target qname/module-key tables built from a file's import statements.

- `symbols`: maps imported name to target qname (`key:name`); covers named and default imports.
- `namespaces`: maps `import * as ns` alias to target module key; used to resolve `ns.member` access.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript_refs:_Bindings.__init__ fingerprint=71f3ff8db7a034b2c831d80092b1e94d8ebfa75caf9ec328d40a33ee15049435 body_fp=269f1036000987ffc62238f0df323991a0206bf6753b1092589e3c094296d99d source_ref=151b3686cf9470200bf8e00b72977ed3ea4702e5 role=model -->
## `def __init__(self) -> None`

Initialize a `_Bindings` instance with empty `symbols` and `namespaces` dicts.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript_refs:_collect_imports fingerprint=149814714cd8c6cd6a30685948928b4df63dc2a51a0e8877addd8a7523056010 body_fp=d07ca474906c28553c13976044fb9d6f145256cf4c82e92cc3e002f524fbb576 source_ref=151b3686cf9470200bf8e00b72977ed3ea4702e5 role=parsing -->
## `def _collect_imports( root: Node, source: bytes, *, from_file: Path, resolver: TsResolver ) -> _Bindings`

Walk top-level statements of `root`, delegating each import/export to `_absorb_import` or `_absorb_reexport` to populate and return a `_Bindings` instance.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript_refs:_specifier_string fingerprint=c77d378033d9ad9acbc65295584055dafdc23c78ad4776ce6b1abfaff67e7c19 body_fp=0d50b53cf748285c1d2dcb2b15d1263aef94f85112fbaa08702ddda50cb9e7cb source_ref=1ed998c56ddb9bb463465902e353473ed681fce0 role=parsing -->
## `def _specifier_string(stmt: Node, source: bytes) -> str | None`

Extract the module specifier string from an import or export statement node, returning `None` if no source string is found.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript_refs:_absorb_import fingerprint=f620897a9460b03760931d690dc21ce02b0eeb7850bbafd3c352525770c009f5 body_fp=bf48a61e469a30d708968324d5f24af3a99d455fbeebfe99c6cedec86b40b965 source_ref=1ed998c56ddb9bb463465902e353473ed681fce0 role=parsing -->
## `def _absorb_import( stmt: Node, source: bytes, b: _Bindings, *, from_file: Path, resolver: TsResolver ) -> None`

Populate a `_Bindings` instance from a single `import_statement` node, mapping local names to resolved target qnames.

- `b`: mutated in place; `b.symbols` receives named/default imports, `b.namespaces` receives namespace (`* as ns`) imports.
- Unresolvable relative specifiers are skipped; bare unresolvable specifiers fall back to the raw specifier string as the module key.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript_refs:_absorb_reexport fingerprint=1e47ea748255e76b600b219caf02fdd1cec300346483d5372a0a2728664fcf06 body_fp=94b6ae81958ad3d748f6984d207ba5846f94c8780bfeb8cf0e6104e3b91e669f source_ref=1ed998c56ddb9bb463465902e353473ed681fce0 role=parsing -->
## `def _absorb_reexport( stmt: Node, source: bytes, b: _Bindings, *, from_file: Path, resolver: TsResolver ) -> None: # `export { x, y } from "./foo"` — bind the names so a body using them links # through the barrel. Only when there is a source specifier.`

Parse an `export { x } from "..."` re-export statement and bind each exported name into `b.symbols`, enabling barrel-file references to resolve correctly.

- `b`: mutated in place; local name maps to `key:imported` qname.
- Skips the statement silently if the source specifier is absent or unresolvable.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript_refs:_find_node_for_symbol fingerprint=c39bbca1b8f50024c8c78db62e9e10c48573491fade44e899e7a17d4e2835a2d body_fp=fc1ac47368e37c0ae19d633309ff591db94a1e67e55a823faf87a26d8289536e source_ref=151b3686cf9470200bf8e00b72977ed3ea4702e5 role=parsing -->
## `def _find_node_for_symbol(root: Node, symbol: Symbol) -> Node | None`

Search `root` for the AST node whose start line matches `symbol.start_line`, skipping comment nodes.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript_refs:_collect_call_names fingerprint=243cc9e202f9802c03c108470b1786d464f8749143d3104c3913efcad5b6099a body_fp=20285fb66aaa9b979fcd652af7ed6fa081fc730f41c3557599919c389d22ab40 source_ref=1ed998c56ddb9bb463465902e353473ed681fce0 role=parsing -->
## `def _collect_call_names(node: Node, source: bytes) -> set[str]`

Walk an AST subtree and collect all identifier names appearing in call or `new` position.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript_refs:_collect_identifiers fingerprint=2faf6e1bc61aaddec09637a0aaeadbbe0f48afec267bd063fb3aa9e5acc89e90 body_fp=81292a5c68c8a2a6628c6eee1584b3128ef6ed76343dc15ec290e75056322d3f source_ref=1ed998c56ddb9bb463465902e353473ed681fce0 role=parsing -->
## `def _collect_identifiers(node: Node, source: bytes) -> set[str]`

Recursively collect all `identifier` and `type_identifier` text values from an AST node, skipping comments and strings.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript_refs:_collect_namespace_uses fingerprint=5f25137c9122eb652a24ce69a5c5f66f863b75089dbb46f6f8a255ed0e3380e4 body_fp=90f4aa9df4126ecbed496e47e06acc786584cbfa410ab9d9d8cbdde780db29b3 source_ref=1ed998c56ddb9bb463465902e353473ed681fce0 role=parsing -->
## `def _collect_namespace_uses(node: Node, source: bytes) -> set[tuple[str, str]]`

Walk an AST `node` and collect all `(object, property)` pairs from `member_expression` nodes, skipping comments and strings.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript_refs:_class_declaration_node fingerprint=16576b6963f3a543e451871ce6bb5dd6a747539611df2eeb27d4c8e0b7588439 body_fp=39e18f9e9be83423cd6e3dafdcfdcb57ecd38565587ab0999cc7fbc8057b7ca6 source_ref=151b3686cf9470200bf8e00b72977ed3ea4702e5 role=parsing -->
## `def _class_declaration_node(node: Node) -> Node`

Unwrap an `export_statement` node to return the inner `class_declaration` or `abstract_class_declaration` node, falling back to the original node.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript_refs:_heritage fingerprint=522477031d995a1849549f5cb1429a25cae46615e6474366d41144c3891516b6 body_fp=80bde1849b214b8a48246a62ce0dbb8d137f6d4af3bff3ea99d6e004b2a6695f source_ref=1ed998c56ddb9bb463465902e353473ed681fce0 role=parsing -->
## `def _heritage(class_node: Node, source: bytes) -> tuple[list[str], list[str]]`

Extract `extends` and `implements` base-name lists from a class node's heritage clause.

- **returns** — `(extends_names, implements_names)` as lists of identifier strings
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript_refs:_RESOLVER_CACHE fingerprint=275ce029b1b0a1d0fb0460c648bd8d08630cda29ebb25c16f9bd91a50cf1974d body_fp=603dd5181cb83043f67ab405d74eb4adef3c8fcdb7d51114132ef372ce02f5ef source_ref=1ed998c56ddb9bb463465902e353473ed681fce0 role=config -->
Module-level cache mapping source-root path strings to their `TsResolver` instances, avoiding redundant config-file walks per scan.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript_refs:_shared_resolver fingerprint=af1e399dd37e68ba689d0bb594a0c8ad440da5e27709b7927f798c8e93aea62d body_fp=086bb21a3737d2cee56886331cb61bf1525935f0c0391c520848d886af86acbf source_ref=1ed998c56ddb9bb463465902e353473ed681fce0 role=util -->
## `def _shared_resolver(source_root: Path) -> TsResolver`

Return a cached `TsResolver` for `source_root`, building and storing one on first access.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript_refs:extract_file_data fingerprint=926f2de4caf04acb2f1d8662bc28560a00323a389c505f92e3c3b702c3ffb116 body_fp=e96ec8fac01d5d851b13eda8cb234ad7ff7b562e2d2572e82fb76ff3b71f6888 source_ref=1ed998c56ddb9bb463465902e353473ed681fce0 role=io -->
## `def extract_file_data( file_path: Path, source_root: Path | None = None, *, resolver: TsResolver | None = None, ) -> FileData`

Parse a single TypeScript file into a `FileData` containing extracted symbols and resolved outbound references.

- `source_root`: defaults to the file's parent directory if omitted.
- `resolver`: obtained from a process-level cache via `_shared_resolver` if not supplied (previously built fresh via `TsResolver.build` each call).
- Deduplicates edges, keeping the highest-ranked `kind` per `(src, target)` pair.
- Returns `FileData` with `references` covering `calls`, `references`, `inherits`, `implements`, and `contains` edges.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript_refs:_resolve_name fingerprint=2c58581fed5721f3119190f21929a0888303dad0d06a545348231b049c7d6b31 body_fp=16b255b30a6d6cf7c4ed771644a5d3daeb8a603d5e90e2d9697c6aa32ae7d94a source_ref=151b3686cf9470200bf8e00b72977ed3ea4702e5 role=util -->
## `def _resolve_name(name: str, bindings: _Bindings, own_top_level: dict[str, str]) -> str | None`

Resolve a local name to a fully-qualified target qname via import bindings or file-local top-level symbols.
<!-- trie:end -->