---
trie_version: 0.3.0
source: trie/parse/typescript.py
file_fingerprint: 3add53a5020602a06f7cb0bc46aa0cb9c0920ebf58fbd0fb3149211423670d01
last_synced_at: '2026-08-02T21:19:47Z'
description: TypeScript / TSX symbol extraction via tree-sitter.
defines:
- kind: module
  qualified_name: trie/parse/typescript:__module__
  lines: 1-788
- kind: constant
  qualified_name: trie/parse/typescript:_TS_LANGUAGE
  lines: 26-26
- kind: constant
  qualified_name: trie/parse/typescript:_TSX_LANGUAGE
  lines: 27-27
- kind: function
  qualified_name: trie/parse/typescript:_make_parser
  lines: 30-37
  signature: 'def _make_parser(file_path: Path) -> Parser'
- kind: function
  qualified_name: trie/parse/typescript:_node_text
  lines: 40-41
  signature: 'def _node_text(node: Node, source: bytes) -> str'
- kind: function
  qualified_name: trie/parse/typescript:_hash
  lines: 44-45
  signature: 'def _hash(s: str) -> str'
- kind: function
  qualified_name: trie/parse/typescript:_module_key
  lines: 48-55
  signature: 'def _module_key(file_path: Path, source_root: Path) -> str'
- kind: function
  qualified_name: trie/parse/typescript:_normalize_tokens
  lines: 58-77
  signature: 'def _normalize_tokens(node: Node | None, source: bytes) -> str'
- kind: function
  qualified_name: trie/parse/typescript:_leading_jsdoc
  lines: 80-89
  signature: 'def _leading_jsdoc(node: Node, source: bytes) -> str | None'
- kind: function
  qualified_name: trie/parse/typescript:_name_of
  lines: 92-101
  signature: 'def _name_of(node: Node, source: bytes) -> str | None'
- kind: function
  qualified_name: trie/parse/typescript:_signature_text
  lines: 104-110
  signature: 'def _signature_text(node: Node, source: bytes, body_field: str = "body") -> str'
- kind: constant
  qualified_name: trie/parse/typescript:_DECLARATION_KINDS
  lines: 115-118
- kind: function
  qualified_name: trie/parse/typescript:_is_exported
  lines: 121-122
  signature: 'def _is_exported(stmt: Node) -> bool'
- kind: function
  qualified_name: trie/parse/typescript:_unwrap
  lines: 125-133
  signature: 'def _unwrap(stmt: Node) -> Node'
- kind: function
  qualified_name: trie/parse/typescript:extract_symbols
  lines: 136-185
  signature: 'def extract_symbols( file_path: Path, source_root: Path | None = None, *, source_text: str | None = None, ) -> list[Symbol]'
- kind: function
  qualified_name: trie/parse/typescript:_dispatch_top_level
  lines: 188-232
  signature: 'def _dispatch_top_level( node: Node, stmt: Node, source: bytes, *, module_key: str, rel_file: str, exported: bool, emit, ) -> None'
- kind: function
  qualified_name: trie/parse/typescript:_build_callable
  lines: 235-270
  signature: 'def _build_callable( node: Node, outer: Node, source: bytes, module_key: str, rel_file: str, *, parent: str | None, exported: bool, name_override: str | None = None, ) -> Symbol'
- kind: function
  qualified_name: trie/parse/typescript:_build_type_decl
  lines: 273-300
  signature: 'def _build_type_decl( node: Node, outer: Node, source: bytes, module_key: str, rel_file: str, *, kind: str, exported: bool, ) -> Symbol'
- kind: function
  qualified_name: trie/parse/typescript:_walk_class
  lines: 303-357
  signature: 'def _walk_class( node: Node, outer: Node, source: bytes, module_key: str, rel_file: str, *, exported: bool, ) -> list[Symbol]'
- kind: function
  qualified_name: trie/parse/typescript:_build_property
  lines: 360-390
  signature: 'def _build_property( member: Node, source: bytes, module_key: str, rel_file: str, *, parent: str, class_private: bool, ) -> Symbol | None'
- kind: function
  qualified_name: trie/parse/typescript:_walk_enum
  lines: 393-451
  signature: 'def _walk_enum( node: Node, outer: Node, source: bytes, module_key: str, rel_file: str, *, exported: bool, ) -> list[Symbol]'
- kind: function
  qualified_name: trie/parse/typescript:_walk_lexical
  lines: 454-509
  signature: 'def _walk_lexical( node: Node, outer: Node, source: bytes, module_key: str, rel_file: str, *, exported: bool, ) -> list[tuple[Symbol, Node]]'
- kind: function
  qualified_name: trie/parse/typescript:_walk_ambient
  lines: 512-605
  signature: 'def _walk_ambient( node: Node, source: bytes, module_key: str, rel_file: str, ) -> list[tuple[Symbol, Node]]'
- kind: function
  qualified_name: trie/parse/typescript:_build_module_symbol
  lines: 608-651
  signature: 'def _build_module_symbol( root: Node, source: bytes, *, module_key: str, rel_file: str, consumed: list[tuple[int, int]], ) -> Symbol | None'
- kind: function
  qualified_name: trie/parse/typescript:_public
  lines: 657-660
  signature: 'def _public(name: str, exported: bool, *, parent_is_private: bool) -> bool'
- kind: function
  qualified_name: trie/parse/typescript:_member_name
  lines: 663-670
  signature: 'def _member_name(member: Node, source: bytes) -> str | None'
- kind: function
  qualified_name: trie/parse/typescript:_has_modifier
  lines: 673-677
  signature: 'def _has_modifier(node: Node, source: bytes, modifier: str) -> bool'
- kind: function
  qualified_name: trie/parse/typescript:_first_child_of_type
  lines: 680-684
  signature: 'def _first_child_of_type(node: Node, type_name: str) -> Node | None'
- kind: constant
  qualified_name: trie/parse/typescript:TS_SYSTEM_PROMPT
  lines: 689-708
- kind: class
  qualified_name: trie/parse/typescript:TypeScriptBackend
  lines: 711-787
  signature: class TypeScriptBackend
- kind: method
  qualified_name: trie/parse/typescript:TypeScriptBackend.__init__
  lines: 729-731
  signature: def __init__(self) -> None
- kind: method
  qualified_name: trie/parse/typescript:TypeScriptBackend.extract_file_data
  lines: 733-757
  signature: def extract_file_data(self, file_path, source_root=None, *, source_text=None)
- kind: method
  qualified_name: trie/parse/typescript:TypeScriptBackend.extract_symbols
  lines: 759-760
  signature: def extract_symbols(self, file_path, source_root=None, *, source_text=None)
- kind: method
  qualified_name: trie/parse/typescript:TypeScriptBackend.source_suffix
  lines: 762-763
  signature: def source_suffix(self) -> str
- kind: method
  qualified_name: trie/parse/typescript:TypeScriptBackend.system_prompt
  lines: 765-766
  signature: def system_prompt(self) -> str
- kind: method
  qualified_name: trie/parse/typescript:TypeScriptBackend.resolver
  lines: 768-787
  signature: def resolver(self)
incoming_refs: 25
outgoing_refs: 20
---
<!-- trie:section symbol=trie/parse/typescript:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=0884fe89300ed585eedac902eed5534fbc69a62ad5892cc6501dc12b4cf4826d source_ref=1ac465220acb62d6851652aa47760d1d3c8fec6d role=parsing -->
Implements TypeScript/TSX symbol extraction via tree-sitter, producing language-neutral `Symbol` values for `.ts`, `.tsx`, and `.d.ts` files.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript:_TS_LANGUAGE fingerprint=43d38bc4b3f214368738a176eead748f9e87dbb3dd0e7bcb7c5eaa1644aea5cb body_fp=9df2a605d0c4a0662fb3dab82bae857eec6695ff86e6e6b48489eae68b233221 source_ref=1ac465220acb62d6851652aa47760d1d3c8fec6d role=config -->
Module-level `Language` instance wrapping the tree-sitter TypeScript grammar, used by `_make_parser` for non-TSX files.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript:_TSX_LANGUAGE fingerprint=c5ad589203599457aa04a1169938d8c363698f6f5911beb7d29dfcaf5f5f83ff body_fp=63500b6fd37a52e831727da65e2b67dce39a64823975d19febf0dbad2668d042 source_ref=1ac465220acb62d6851652aa47760d1d3c8fec6d role=config -->
Module-level `Language` instance for the TSX grammar, used by `_make_parser` to configure TSX file parsing.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript:_make_parser fingerprint=6ef66fb600f59d93983e79eb86f78e9547d3c28f63cf5607ced765c261c720b4 body_fp=503577a6045cf506d26f61d7f6dd912478832ef586c3a58bbbbbf9d6e043035e source_ref=e26a1192f6add3e1cab718bb626a08a23e9d5981 role=util -->
## `def _make_parser(file_path: Path) -> Parser`

Construct a `Parser` configured with the TSX or TS language grammar based on `file_path`'s extension.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript:_node_text fingerprint=90272da3050ae7f74f98b5fb62c5860239cd69d3c98b9843ee7816f84677e986 body_fp=723d966375bd4bdc24496147f537d8f5ab9e6a465a02699eda5a343e8934f2f6 source_ref=1ac465220acb62d6851652aa47760d1d3c8fec6d role=util -->
## `def _node_text(node: Node, source: bytes) -> str`

Decode the byte span of `node` from `source` into a UTF-8 string, replacing invalid bytes.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript:_hash fingerprint=7057d302a510678c4e042810b0eb270cc10d5047cb0a03fac868582b067b5767 body_fp=6669477292c01bece7ef1f4345e604d994c8aba94e5f3aa365f05018167230e1 source_ref=1ac465220acb62d6851652aa47760d1d3c8fec6d role=util -->
## `def _hash(s: str) -> str`

Return the SHA-256 hex digest of a UTF-8-encoded string.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript:_module_key fingerprint=06c146e80c9fbcf54a049f41a7b4aabc2081d2789b6e85c2b6a989cb49476e76 body_fp=a8efd0a04abde34a61ff307dbc656ac262b0181885da5b4b4916bb99abaa6371 source_ref=e26a1192f6add3e1cab718bb626a08a23e9d5981 role=util -->
## `def _module_key(file_path: Path, source_root: Path) -> str`

Compute the qualified-name prefix for a file by stripping its TypeScript or JavaScript extension from its path relative to `source_root`, returning a slash-form string.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript:_normalize_tokens fingerprint=da1d32cd7ab0afb71037deba11a042b2a02412c61813009f1f055e5becc682b0 body_fp=e680cab1b5c47449f6092b13cc4453f3b19340569a653a13e21239b9911483da source_ref=1ac465220acb62d6851652aa47760d1d3c8fec6d role=util -->
## `def _normalize_tokens(node: Node | None, source: bytes) -> str`

Recursively collect leaf-token text from a tree-sitter node, skipping comment nodes, and return tokens joined by spaces.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript:_leading_jsdoc fingerprint=d0f185bcee607c6ecae3902b0197eb6416205e66c3a344ad85420300037919df body_fp=c2f06c3c137c4b691ba1de6924557afb3e654e5b0812a362c46379018fc411fe source_ref=1ac465220acb62d6851652aa47760d1d3c8fec6d role=util -->
## `def _leading_jsdoc(node: Node, source: bytes) -> str | None`

Return the `/** ... */` JSDoc comment immediately preceding `node`, or `None` if absent.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript:_name_of fingerprint=8d14e33bc65c3d2b45b9dd17d62333d26e4b91a20ccbe4e3fef59499607138a2 body_fp=b578ac577df477e1b5fe75997af74298f3a5eeba0f6c0fb8bd61f6a29f1c0681 source_ref=1ac465220acb62d6851652aa47760d1d3c8fec6d role=parsing -->
## `def _name_of(node: Node, source: bytes) -> str | None`

Extract the declared name from a tree-sitter declaration node, trying the `name` field then falling back to the first identifier-typed child.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript:_signature_text fingerprint=9d7ef8dff441fd63dbf400a36bdcd79715b502e3c79f0974259b2cef863f5709 body_fp=32cc72edf8f47b66cf53ddfe87101f85330f77515c6f61e7b557a2af910a0b8b source_ref=1ac465220acb62d6851652aa47760d1d3c8fec6d role=parsing -->
## `def _signature_text(node: Node, source: bytes, body_field: str = "body") -> str`

Extract the header text of a declaration node up to (but excluding) its body block, stripping trailing braces.

- `body_field`: field name used to locate the body child; defaults to `"body"`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript:_DECLARATION_KINDS fingerprint=17e6cdd788ff67e7d5266e6c19eadc588560ace250caa34d605a6f53c234240c body_fp=7bee345d9953c57261e02e9206292bbc93b6d72fa08d24b19fc823e3f34f347d source_ref=1ac465220acb62d6851652aa47760d1d3c8fec6d role=config -->
Map tree-sitter node types to their trie kind strings for declaration nodes that carry no executable body.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript:_is_exported fingerprint=3ff13f1603eedf6308c074654280063002d8b2db21efb6b6ad571c909d1d1ca5 body_fp=28fbe4bd7d1dd2b80257e7bcdac7ae9d5dfbe8eac61e0e2c594f6a4dd3882fde source_ref=1ac465220acb62d6851652aa47760d1d3c8fec6d role=util -->
## `def _is_exported(stmt: Node) -> bool`

Return `True` if `stmt` is an `export_statement` node.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript:_unwrap fingerprint=322af535a5be66568bc0271e62ea3b11b5bea4697fa31a641af125e4ca0f338f body_fp=b960ed02ed2d76d8a69fd660acb2735cc5d76365bdf9a939138917139bde1e22 source_ref=1ac465220acb62d6851652aa47760d1d3c8fec6d role=util -->
## `def _unwrap(stmt: Node) -> Node`

Unwrap an `export_statement` node to its inner declaration, returning the node itself for any other statement type.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript:extract_symbols fingerprint=2e0b9a6b20e40c45a1d4b3d82c447a40235978962d458779ebc8d92b89379720 body_fp=5727b74989201ba26c7cc7e2473eaa7667e56cb3cc6a851e48a0f63f3ac4d9c9 source_ref=1ac465220acb62d6851652aa47760d1d3c8fec6d role=parsing -->
## `def extract_symbols( file_path: Path, source_root: Path | None = None, *, source_text: str | None = None, ) -> list[Symbol]`

Parse a TypeScript/TSX file and return a deduplicated, source-ordered list of `Symbol` objects.

- `source_root`: used to compute qualified names; defaults to `file_path.parent`
- `source_text`: if provided, parses this string instead of reading the file
- Returns one `Symbol` per top-level declaration plus nested class members and a synthetic `__module__` symbol for residual code
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript:_dispatch_top_level fingerprint=4d9d2d9abed1d89ca7da7c787440b1240cf8bfee033cdacd9337a561994444b6 body_fp=761d20ccd8d661d579ed898c791a81ca179ef0440609dc083140a61cf0f0f1a2 source_ref=1ac465220acb62d6851652aa47760d1d3c8fec6d role=orchestration -->
## `def _dispatch_top_level( node: Node, stmt: Node, source: bytes, *, module_key: str, rel_file: str, exported: bool, emit, ) -> None`

Route a single unwrapped top-level AST node to the appropriate builder and call `emit` for each resulting `Symbol`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript:_build_callable fingerprint=8f47807cfe2c98a2038376a560e1ddee5878bc51d82773b6feab3bfcff3a1430 body_fp=b455171dd61f759575537ac09a3b4cd01df7720900f3d4c88842891bf61e1689 source_ref=1ac465220acb62d6851652aa47760d1d3c8fec6d role=parsing -->
## `def _build_callable( node: Node, outer: Node, source: bytes, module_key: str, rel_file: str, *, parent: str | None, exported: bool, name_override: str | None = None, ) -> Symbol`

Build a `Symbol` for a TypeScript function, method, or arrow function declaration node.

- `parent`: non-`None` sets `kind` to `"method"` and prefixes the qualified name.
- `name_override`: substitutes the name inferred from the node (used for named arrow bindings).
- Body-less declarations (signatures) fingerprint the signature text instead of the body tokens.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript:_build_type_decl fingerprint=b6d2addb616e7abb99c314f2af134db079a94ceea805c249fddd86a9304610bf body_fp=db6c953dd846eb02f3b408b8951c3b8b4d50231d7284ef224858989a14ec7c29 source_ref=1ac465220acb62d6851652aa47760d1d3c8fec6d role=parsing -->
## `def _build_type_decl( node: Node, outer: Node, source: bytes, module_key: str, rel_file: str, *, kind: str, exported: bool, ) -> Symbol`

Build a `Symbol` for a TypeScript `interface` or `type` alias declaration node.

- `kind`: `"interface"` uses header-only signature; `"type"` uses full node text as signature.
- `outer`: statement node used for line numbers and JSDoc lookup.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript:_walk_class fingerprint=57eee964fc337461271450846922c7e777dfa50c85a1eaad680d7013fa4757ba body_fp=1e7c1ce9cadc3a5829478e76ad3931ea19b39ba3b0bb4dc86ff330773eee4cb4 source_ref=1ac465220acb62d6851652aa47760d1d3c8fec6d role=parsing -->
## `def _walk_class( node: Node, outer: Node, source: bytes, module_key: str, rel_file: str, *, exported: bool, ) -> list[Symbol]`

Emit a `Symbol` for the class itself plus child `Symbol`s for each method and property member found in its body.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript:_build_property fingerprint=25af33d78bebf54bceac94eaee1888d9edec8bb83d03d007f9ef1b0308b91ec0 body_fp=dceccbe2604f5bd77bf110ca654f0329e0e619a11d1c10b002fbea3038dffe1b source_ref=1ac465220acb62d6851652aa47760d1d3c8fec6d role=parsing -->
## `def _build_property( member: Node, source: bytes, module_key: str, rel_file: str, *, parent: str, class_private: bool, ) -> Symbol | None`

Build a `property` `Symbol` from a class field/property member node, returning `None` if no name can be resolved.

- `class_private`: propagates owning-class privacy to all its members.
- `is_public` is `False` if class is private, name starts with `_`/`#`, or node carries a `private` accessibility modifier.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript:_walk_enum fingerprint=d7501b7700ebe39d5606fb10c2aa4b0e120baa2088e7efea0f647dc4478d1c4d body_fp=b5f104f1e9d265287c97e7a90301059d7d1ba2da7e3b7bcef47942dcafd05c8d source_ref=1ac465220acb62d6851652aa47760d1d3c8fec6d role=parsing -->
## `def _walk_enum( node: Node, outer: Node, source: bytes, module_key: str, rel_file: str, *, exported: bool, ) -> list[Symbol]`

Emit one `enum` `Symbol` plus one `enum_member` `Symbol` per body member for a `enum_declaration` node.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript:_walk_lexical fingerprint=680c218a0d2b4a97923551c480018696512b6f687273e1f521283ffc15432df4 body_fp=e094d9303885d6b0506c7cdbd0732182aff5a05ce9b597c974c433f24df1aead source_ref=1ac465220acb62d6851652aa47760d1d3c8fec6d role=parsing -->
## `def _walk_lexical( node: Node, outer: Node, source: bytes, module_key: str, rel_file: str, *, exported: bool, ) -> list[tuple[Symbol, Node]]`

Extract `Symbol` entries from a top-level `const`/`let`/`var` declaration node, classifying arrow/function-valued bindings as `function` and all others as `constant`; skips destructuring targets.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript:_walk_ambient fingerprint=aac55d121e7c78fa6feeb67b2b0a431421154482a27a2d4b59c904203c72127c body_fp=c211a070d3da972cff503cf767131d6bb67f65ab61ba8ae6f44c7734fe6d3d06 source_ref=1ac465220acb62d6851652aa47760d1d3c8fec6d role=parsing -->
## `def _walk_ambient( node: Node, source: bytes, module_key: str, rel_file: str, ) -> list[tuple[Symbol, Node]]`

Extract `Symbol` entries from an `ambient_declaration` node, handling both `declare module "x" { ... }` blocks and bare `declare function/const` statements.

- `declare module "x"` emits a `module` symbol keyed by the literal string name, plus nested type/function declarations keyed under that name.
- Bare declarations are attributed to `module_key` (the file's own module).
- Returns `(Symbol, Node)` pairs; returns an empty list if the inner node is absent or unrecognised.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript:_build_module_symbol fingerprint=ef3ae1cb0137211c60f839420aac00a41047816a13951bbe84a49a72a17bc6c4 body_fp=1f94fd4e685df46f44d44de8186efc73dbedad295470c4875a8924c14c672f60 source_ref=1ac465220acb62d6851652aa47760d1d3c8fec6d role=parsing -->
## `def _build_module_symbol( root: Node, source: bytes, *, module_key: str, rel_file: str, consumed: list[tuple[int, int]], ) -> Symbol | None`

Build a synthetic `__module__` `Symbol` from top-level AST nodes not claimed by any already-extracted symbol, excluding imports and comments.

- `consumed`: line ranges already owned by extracted symbols; used to skip those nodes.
- Returns `None` when no residual top-level code remains.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript:_public fingerprint=43a901961a19106b65439a7826d1f2863780b09091dc04d11f3bfc6dfd941270 body_fp=976f35fcc6c2c94cf0cdeba42d46654ea001e956889c7468d1fab93ef81f30d9 source_ref=1ac465220acb62d6851652aa47760d1d3c8fec6d role=util -->
## `def _public(name: str, exported: bool, *, parent_is_private: bool) -> bool`

Return whether a symbol is public based on its name, export status, and parent privacy.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript:_member_name fingerprint=1248ba030404db61f94f702b3e5d5f12ae616c001cc861112ca8cb4d06eeddd3 body_fp=1c93eee651922b303d83dd6ecdf6993021b01b16a0ef71039c206b5abb602acd source_ref=1ac465220acb62d6851652aa47760d1d3c8fec6d role=util -->
## `def _member_name(member: Node, source: bytes) -> str | None`

Extract the declared name from a class member node, falling back to scanning named children for identifier-typed nodes.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript:_has_modifier fingerprint=2ff0423fd2385b4a3cd176ae43842b1667835b61e5d7cbcddce309b2b06b4e01 body_fp=8b5ff17962d2843fd9b60c95cc37115435f628ec260842fcb5bc61de824dbc82 source_ref=1ac465220acb62d6851652aa47760d1d3c8fec6d role=util -->
## `def _has_modifier(node: Node, source: bytes, modifier: str) -> bool`

Return `True` if any named child of `node` is an `accessibility_modifier` matching `modifier`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript:_first_child_of_type fingerprint=2f9c592029e617284efbf38c01c0ad8701b7d8a7e20aaba09f1e0de2545c75df body_fp=e2d9186847d78a2001cb6f1dc030832df049686ccfed092177cd30e8367744bd source_ref=1ac465220acb62d6851652aa47760d1d3c8fec6d role=util -->
## `def _first_child_of_type(node: Node, type_name: str) -> Node | None`

Return the first named child of `node` whose type equals `type_name`, or `None`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript:TS_SYSTEM_PROMPT fingerprint=523395e0a833b64879f69133b4728bcddd9ad2d969d17af2dcbd23988ae67be2 body_fp=627b38ffd1b0dcc3119dae55d61a1e680ded005416cd0c7a89c57f13c9d0270a source_ref=1ac465220acb62d6851652aa47760d1d3c8fec6d role=config -->
System prompt string passed to the LLM when generating documentation for TypeScript symbols.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript:TypeScriptBackend fingerprint=037f9407f3cfca2b9a692b51de5b57005ef0cef32c3972e71e5c1108f082c722 body_fp=530bc4902bbef098088c98a634f9199db14d7aee1de6168fd62ba352362fc587 source_ref=e26a1192f6add3e1cab718bb626a08a23e9d5981 role=domain -->
## `class TypeScriptBackend`

Implements `LanguageBackend` for `.ts`, `.tsx`, `.d.ts`, `.jsx`, `.mjs`, `.cjs`, and `.js` files, wiring two-pass reference extraction (tree-sitter + optional LSP resolver), symbol extraction, and the system prompt.

- `extensions`: ordered longest-first so `.d.ts` resolves before `.ts`; JavaScript suffixes included as the TS grammar is a superset
- `extract_file_data`: delegates to `typescript_refs`; merges LSP-resolved member-dispatch edges when a resolver is available; does not support `source_text` override
- `resolver()`: returns a cached `LspResolver` for typescript-language-server, or `None` if `TRIE_DISABLE_RESOLVER=1` or the server is not on PATH
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript:TypeScriptBackend.__init__ fingerprint=b84739b0fbbdbeb6b33571852fef53390cb973b63bb786a1526af79058a93652 body_fp=e6ad022fa98f183789520889570a8f465a620f132f131fb384cc0f5cdf9d5d6c source_ref=e1c63593dc55002aae32a954ca66e5ff7d7fb810 role=domain -->
## `def __init__(self) -> None`

Initialize `TypeScriptBackend` with `_resolver` and `_resolver_built` set to their unbuilt defaults.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript:TypeScriptBackend.extract_file_data fingerprint=dc038b10128bc6c9df2eb8bf837d237120f2d33f6afad6d8ba9bbc26aec49bcd body_fp=6af3cab3b7873a807c8b5b3760e3fad0eccb890e12177e89d46c593e1c3333c6 source_ref=e26a1192f6add3e1cab718bb626a08a23e9d5981 role=orchestration -->
## `def extract_file_data(self, file_path, source_root=None, *, source_text=None)`

Extract `TypeScriptBackend` file data via `typescript_refs.extract_file_data`, then merge LSP resolver references if available; raises `NotImplementedError` if `source_text` is supplied.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript:TypeScriptBackend.extract_symbols fingerprint=af266339106949531c076cf2e82cb2565f65b39795b7b77394086774fac189f3 body_fp=4fc2eeeac232ea6e0448a8dfa5d5c43244ce0d7ee4457470f13ff8dd85b58c6c source_ref=1ac465220acb62d6851652aa47760d1d3c8fec6d role=api -->
## `def extract_symbols(self, file_path, source_root=None, *, source_text=None)`

Delegate `TypeScriptBackend.extract_symbols` to the module-level `extract_symbols` function, returning its `list[Symbol]`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript:TypeScriptBackend.source_suffix fingerprint=bf61bb997784ff6713e45a76a5457a002dd12cc7b8a0a2a6a054575fb2fdd368 body_fp=be710186137bc9cead0f819cc06f38a76e881da1a30c96bcda225d0175d872f9 source_ref=1ac465220acb62d6851652aa47760d1d3c8fec6d role=api -->
## `def source_suffix(self) -> str`

`TypeScriptBackend.source_suffix` returns the canonical source file extension `".ts"`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript:TypeScriptBackend.system_prompt fingerprint=4a9cf48bef1c51973826ab0b4182de46d91cdb98cee34a2fc01a12e68369f30a body_fp=a49347fd03bd72f80dded542ee9f1af1ccc2d7bc1fbb1f2d663dff8428c3a5a2 source_ref=1ac465220acb62d6851652aa47760d1d3c8fec6d role=api -->
## `def system_prompt(self) -> str`

Return the `TypeScriptBackend`'s documentation-generation system prompt string.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript:TypeScriptBackend.resolver fingerprint=d053fde1515981c50c6325556606271ab03040b1b3292e317e230d51dccce10e body_fp=a1342493214e8bd86a2ab40e8f69ca210fdced09d9a2acb2c85e65f667e17d3e source_ref=e1c63593dc55002aae32a954ca66e5ff7d7fb810 role=orchestration -->
## `def resolver(self)`

`TypeScriptBackend.resolver` returns a cached `LspResolver` for `typescript-language-server`, or `None` if disabled or unavailable.

- Sets `TRIE_DISABLE_RESOLVER=1` to force `None` (tree-sitter-only mode).
- Degrades to `None` when `typescript-language-server` is not on PATH.
- Result is built once and cached in `_resolver`.
<!-- trie:end -->