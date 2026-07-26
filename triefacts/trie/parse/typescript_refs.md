---
trie_version: 0.1.9
source: trie/parse/typescript_refs.py
file_fingerprint: 26c7bf67784e8f254ffeea4190afc1490099c7c90f5f4a8f31f3b4fe8648f443
last_synced_at: '2026-07-26T20:28:41Z'
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
- kind: method
  qualified_name: trie/parse/typescript_refs:_Bindings.__init__
  lines: 43-45
- kind: function
  qualified_name: trie/parse/typescript_refs:_collect_imports
  lines: 48-57
- kind: function
  qualified_name: trie/parse/typescript_refs:_specifier_string
  lines: 60-70
- kind: function
  qualified_name: trie/parse/typescript_refs:_absorb_import
  lines: 73-109
- kind: function
  qualified_name: trie/parse/typescript_refs:_absorb_reexport
  lines: 112-134
- kind: function
  qualified_name: trie/parse/typescript_refs:_find_node_for_symbol
  lines: 137-151
- kind: function
  qualified_name: trie/parse/typescript_refs:_collect_call_names
  lines: 154-176
- kind: function
  qualified_name: trie/parse/typescript_refs:_collect_identifiers
  lines: 179-191
- kind: function
  qualified_name: trie/parse/typescript_refs:_collect_namespace_uses
  lines: 194-210
- kind: function
  qualified_name: trie/parse/typescript_refs:_class_declaration_node
  lines: 213-220
- kind: function
  qualified_name: trie/parse/typescript_refs:_heritage
  lines: 223-242
- kind: constant
  qualified_name: trie/parse/typescript_refs:_RESOLVER_CACHE
  lines: 251-251
- kind: function
  qualified_name: trie/parse/typescript_refs:_shared_resolver
  lines: 254-260
- kind: function
  qualified_name: trie/parse/typescript_refs:extract_file_data
  lines: 263-344
- kind: function
  qualified_name: trie/parse/typescript_refs:_resolve_name
  lines: 347-352
incoming_refs: 1
outgoing_refs: 12
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
<!-- trie:section symbol=trie/parse/typescript_refs:_Bindings fingerprint=10e8e5091559c972cb022172383f8965d6eea69879770b92f784de8eb5dc22b2 body_fp=543d9083504c963a4a88330e291e75c3f2fc16ac7c80115b70c52078ff9acce4 source_ref=151b3686cf9470200bf8e00b72977ed3ea4702e5 role=model -->
Hold local-name → target qname/module-key tables built from a file's import statements.

- `symbols`: maps imported name to target qname (`key:name`); covers named and default imports.
- `namespaces`: maps `import * as ns` alias to target module key; used to resolve `ns.member` access.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript_refs:_Bindings.__init__ fingerprint=71f3ff8db7a034b2c831d80092b1e94d8ebfa75caf9ec328d40a33ee15049435 body_fp=6b73ba44f6b1110a95d37a026f78be8e121548c30dcbf24004bd9f178cdce545 source_ref=151b3686cf9470200bf8e00b72977ed3ea4702e5 role=model -->
Initialize a `_Bindings` instance with empty `symbols` and `namespaces` dicts.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript_refs:_collect_imports fingerprint=149814714cd8c6cd6a30685948928b4df63dc2a51a0e8877addd8a7523056010 body_fp=c0c4a0c91bbb9f0ea13b7763acb3a29f8176f497de9b0f56d935aec86ec8891f source_ref=151b3686cf9470200bf8e00b72977ed3ea4702e5 role=parsing -->
Walk top-level statements of `root`, delegating each import/export to `_absorb_import` or `_absorb_reexport` to populate and return a `_Bindings` instance.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript_refs:_specifier_string fingerprint=c77d378033d9ad9acbc65295584055dafdc23c78ad4776ce6b1abfaff67e7c19 body_fp=aa49f9c6e8a7b8884dc19775282f0859701f7dfc7a014c7f0bd90f859dde87e7 source_ref=1ed998c56ddb9bb463465902e353473ed681fce0 role=parsing -->
Extract the module specifier string from an import or export statement node, returning `None` if no source string is found.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript_refs:_absorb_import fingerprint=f620897a9460b03760931d690dc21ce02b0eeb7850bbafd3c352525770c009f5 body_fp=e4c5401d15586970db96fd41a95a70f50e5c8ac6e7479b545a7f979da70a3d80 source_ref=1ed998c56ddb9bb463465902e353473ed681fce0 role=parsing -->
Populate a `_Bindings` instance from a single `import_statement` node, mapping local names to resolved target qnames.

- `b`: mutated in place; `b.symbols` receives named/default imports, `b.namespaces` receives namespace (`* as ns`) imports.
- Unresolvable relative specifiers are skipped; bare unresolvable specifiers fall back to the raw specifier string as the module key.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript_refs:_absorb_reexport fingerprint=1e47ea748255e76b600b219caf02fdd1cec300346483d5372a0a2728664fcf06 body_fp=363e9a83724ae47fac9838931f745f3a032f990f49218112972baf224d362184 source_ref=1ed998c56ddb9bb463465902e353473ed681fce0 role=parsing -->
Parse an `export { x } from "..."` re-export statement and bind each exported name into `b.symbols`, enabling barrel-file references to resolve correctly.

- `b`: mutated in place; local name maps to `key:imported` qname.
- Skips the statement silently if the source specifier is absent or unresolvable.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript_refs:_find_node_for_symbol fingerprint=c39bbca1b8f50024c8c78db62e9e10c48573491fade44e899e7a17d4e2835a2d body_fp=ca328786b866eb2a66fa4327b30b1c69a997959a493d000e7346e669c62f0bce source_ref=151b3686cf9470200bf8e00b72977ed3ea4702e5 role=parsing -->
Search `root` for the AST node whose start line matches `symbol.start_line`, skipping comment nodes.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript_refs:_collect_call_names fingerprint=243cc9e202f9802c03c108470b1786d464f8749143d3104c3913efcad5b6099a body_fp=46ca8704c862e08e05ab2836d7c7458dbfc3e9cd3bd63f19c67dd636ae239cec source_ref=1ed998c56ddb9bb463465902e353473ed681fce0 role=parsing -->
Walk an AST subtree and collect all identifier names appearing in call or `new` position.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript_refs:_collect_identifiers fingerprint=2faf6e1bc61aaddec09637a0aaeadbbe0f48afec267bd063fb3aa9e5acc89e90 body_fp=ed1aa98d384a9b8a24f39be8edbcd7534ee0e1962a8d3ddc5e1ebef32a2cdcec source_ref=1ed998c56ddb9bb463465902e353473ed681fce0 role=parsing -->
Recursively collect all `identifier` and `type_identifier` text values from an AST node, skipping comments and strings.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript_refs:_collect_namespace_uses fingerprint=5f25137c9122eb652a24ce69a5c5f66f863b75089dbb46f6f8a255ed0e3380e4 body_fp=982a732dbe1df4ca3c3e27f5e22556d2d8065d9a4ae4ea1c7bb99ac59bef652c source_ref=1ed998c56ddb9bb463465902e353473ed681fce0 role=parsing -->
Walk an AST `node` and collect all `(object, property)` pairs from `member_expression` nodes, skipping comments and strings.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript_refs:_class_declaration_node fingerprint=16576b6963f3a543e451871ce6bb5dd6a747539611df2eeb27d4c8e0b7588439 body_fp=7513fb4f4665e3aafdefed7462eab2c208e1d1fd2f5bc0f5927eba1069c8745b source_ref=151b3686cf9470200bf8e00b72977ed3ea4702e5 role=parsing -->
Unwrap an `export_statement` node to return the inner `class_declaration` or `abstract_class_declaration` node, falling back to the original node.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript_refs:_heritage fingerprint=522477031d995a1849549f5cb1429a25cae46615e6474366d41144c3891516b6 body_fp=dfcf3ddc44738190b214a0ea0fdc52d96a597cee9dff857af3aa0c347ec3725c source_ref=1ed998c56ddb9bb463465902e353473ed681fce0 role=parsing -->
Extract `extends` and `implements` base-name lists from a class node's heritage clause.

- **returns** — `(extends_names, implements_names)` as lists of identifier strings
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript_refs:_RESOLVER_CACHE fingerprint=275ce029b1b0a1d0fb0460c648bd8d08630cda29ebb25c16f9bd91a50cf1974d body_fp=603dd5181cb83043f67ab405d74eb4adef3c8fcdb7d51114132ef372ce02f5ef source_ref=1ed998c56ddb9bb463465902e353473ed681fce0 role=config -->
Module-level cache mapping source-root path strings to their `TsResolver` instances, avoiding redundant config-file walks per scan.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript_refs:_shared_resolver fingerprint=af1e399dd37e68ba689d0bb594a0c8ad440da5e27709b7927f798c8e93aea62d body_fp=2e5f97b24f44aac3d13aefdc758abf6cac486df5e9066dde5d3cf1ded0edb773 source_ref=1ed998c56ddb9bb463465902e353473ed681fce0 role=util -->
Return a cached `TsResolver` for `source_root`, building and storing one on first access.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript_refs:extract_file_data fingerprint=926f2de4caf04acb2f1d8662bc28560a00323a389c505f92e3c3b702c3ffb116 body_fp=b020263c642db93c46977931ccf1b62d60cc32c13d925e377dc596a118f47d0e source_ref=1ed998c56ddb9bb463465902e353473ed681fce0 role=parsing -->
Parse a single TypeScript file into a `FileData` containing extracted symbols and resolved outbound references.

- `source_root`: defaults to the file's parent directory if omitted.
- `resolver`: obtained from a process-level cache via `_shared_resolver` if not supplied (previously built fresh via `TsResolver.build` each call).
- Deduplicates edges, keeping the highest-ranked `kind` per `(src, target)` pair.
- Returns `FileData` with `references` covering `calls`, `references`, `inherits`, `implements`, and `contains` edges.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript_refs:_resolve_name fingerprint=2c58581fed5721f3119190f21929a0888303dad0d06a545348231b049c7d6b31 body_fp=a058b6ecb4b476b30bc968b11c7b38cf7220645f6d7509cb1f249f303c6f1d0d source_ref=151b3686cf9470200bf8e00b72977ed3ea4702e5 role=util -->
Resolve a local name to a fully-qualified target qname via import bindings or file-local top-level symbols.
<!-- trie:end -->