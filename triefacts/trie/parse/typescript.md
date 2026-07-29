---
trie_version: 0.1.9
source: trie/parse/typescript.py
file_fingerprint: 3add53a5020602a06f7cb0bc46aa0cb9c0920ebf58fbd0fb3149211423670d01
last_synced_at: '2026-07-29T00:05:51Z'
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
- kind: function
  qualified_name: trie/parse/typescript:_node_text
  lines: 40-41
- kind: function
  qualified_name: trie/parse/typescript:_hash
  lines: 44-45
- kind: function
  qualified_name: trie/parse/typescript:_module_key
  lines: 48-55
- kind: function
  qualified_name: trie/parse/typescript:_normalize_tokens
  lines: 58-77
- kind: function
  qualified_name: trie/parse/typescript:_leading_jsdoc
  lines: 80-89
- kind: function
  qualified_name: trie/parse/typescript:_name_of
  lines: 92-101
- kind: function
  qualified_name: trie/parse/typescript:_signature_text
  lines: 104-110
- kind: constant
  qualified_name: trie/parse/typescript:_DECLARATION_KINDS
  lines: 115-118
- kind: function
  qualified_name: trie/parse/typescript:_is_exported
  lines: 121-122
- kind: function
  qualified_name: trie/parse/typescript:_unwrap
  lines: 125-133
- kind: function
  qualified_name: trie/parse/typescript:extract_symbols
  lines: 136-185
- kind: function
  qualified_name: trie/parse/typescript:_dispatch_top_level
  lines: 188-232
- kind: function
  qualified_name: trie/parse/typescript:_build_callable
  lines: 235-270
- kind: function
  qualified_name: trie/parse/typescript:_build_type_decl
  lines: 273-300
- kind: function
  qualified_name: trie/parse/typescript:_walk_class
  lines: 303-357
- kind: function
  qualified_name: trie/parse/typescript:_build_property
  lines: 360-390
- kind: function
  qualified_name: trie/parse/typescript:_walk_enum
  lines: 393-451
- kind: function
  qualified_name: trie/parse/typescript:_walk_lexical
  lines: 454-509
- kind: function
  qualified_name: trie/parse/typescript:_walk_ambient
  lines: 512-605
- kind: function
  qualified_name: trie/parse/typescript:_build_module_symbol
  lines: 608-651
- kind: function
  qualified_name: trie/parse/typescript:_public
  lines: 657-660
- kind: function
  qualified_name: trie/parse/typescript:_member_name
  lines: 663-670
- kind: function
  qualified_name: trie/parse/typescript:_has_modifier
  lines: 673-677
- kind: function
  qualified_name: trie/parse/typescript:_first_child_of_type
  lines: 680-684
- kind: constant
  qualified_name: trie/parse/typescript:TS_SYSTEM_PROMPT
  lines: 689-708
- kind: class
  qualified_name: trie/parse/typescript:TypeScriptBackend
  lines: 711-787
- kind: method
  qualified_name: trie/parse/typescript:TypeScriptBackend.__init__
  lines: 729-731
- kind: method
  qualified_name: trie/parse/typescript:TypeScriptBackend.extract_file_data
  lines: 733-757
- kind: method
  qualified_name: trie/parse/typescript:TypeScriptBackend.extract_symbols
  lines: 759-760
- kind: method
  qualified_name: trie/parse/typescript:TypeScriptBackend.source_suffix
  lines: 762-763
- kind: method
  qualified_name: trie/parse/typescript:TypeScriptBackend.system_prompt
  lines: 765-766
- kind: method
  qualified_name: trie/parse/typescript:TypeScriptBackend.resolver
  lines: 768-787
incoming_refs: 18
outgoing_refs: 9
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
<!-- trie:section symbol=trie/parse/typescript:_make_parser fingerprint=6ef66fb600f59d93983e79eb86f78e9547d3c28f63cf5607ced765c261c720b4 body_fp=cb84eaa96b74f59a518db7d533bb8a7ecbb78ee145ef46570848bb2add5dc82b source_ref=e26a1192f6add3e1cab718bb626a08a23e9d5981 role=util -->
Construct a `Parser` configured with the TSX or TS language grammar based on `file_path`'s extension.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript:_node_text fingerprint=90272da3050ae7f74f98b5fb62c5860239cd69d3c98b9843ee7816f84677e986 body_fp=f7c7c49a0a058caa316ed12e0c99cff7c2b8529e560cbb1eff2a216286e0ba83 source_ref=1ac465220acb62d6851652aa47760d1d3c8fec6d role=util -->
Decode the byte span of `node` from `source` into a UTF-8 string, replacing invalid bytes.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript:_hash fingerprint=7057d302a510678c4e042810b0eb270cc10d5047cb0a03fac868582b067b5767 body_fp=4d6c535ddd567d3e1fea8feeb45a70dc232492d2f3105352d59a2cda51262480 source_ref=1ac465220acb62d6851652aa47760d1d3c8fec6d role=util -->
Return the SHA-256 hex digest of a UTF-8-encoded string.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript:_module_key fingerprint=06c146e80c9fbcf54a049f41a7b4aabc2081d2789b6e85c2b6a989cb49476e76 body_fp=e3bf206e51a147d598be98f24a310b5dee733c040fa5bdd30a7f937043e14d09 source_ref=e26a1192f6add3e1cab718bb626a08a23e9d5981 role=util -->
Compute the qualified-name prefix for a file by stripping its TypeScript or JavaScript extension from its path relative to `source_root`, returning a slash-form string.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript:_normalize_tokens fingerprint=da1d32cd7ab0afb71037deba11a042b2a02412c61813009f1f055e5becc682b0 body_fp=8339f59e79f2bb2d875958573a67f05fcf23bc689195bcb7aa42b39cb5d94ef1 source_ref=1ac465220acb62d6851652aa47760d1d3c8fec6d role=util -->
Recursively collect leaf-token text from a tree-sitter node, skipping comment nodes, and return tokens joined by spaces.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript:_leading_jsdoc fingerprint=d0f185bcee607c6ecae3902b0197eb6416205e66c3a344ad85420300037919df body_fp=6e664bb4fda1c3f4effb751ab1bca50d56f80835eb9b5818ea2419b903415e1a source_ref=1ac465220acb62d6851652aa47760d1d3c8fec6d role=util -->
Return the `/** ... */` JSDoc comment immediately preceding `node`, or `None` if absent.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript:_name_of fingerprint=8d14e33bc65c3d2b45b9dd17d62333d26e4b91a20ccbe4e3fef59499607138a2 body_fp=85881db224f056fe17549581e7b3afb79941df031715cea4ed5f61bac7d0c271 source_ref=1ac465220acb62d6851652aa47760d1d3c8fec6d role=parsing -->
Extract the declared name from a tree-sitter declaration node, trying the `name` field then falling back to the first identifier-typed child.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript:_signature_text fingerprint=9d7ef8dff441fd63dbf400a36bdcd79715b502e3c79f0974259b2cef863f5709 body_fp=10a36dbbcd97fffdbc891f3c8b91ffb5909c54ab8d2e7a2a3c4d6826d8f770bf source_ref=1ac465220acb62d6851652aa47760d1d3c8fec6d role=parsing -->
Extract the header text of a declaration node up to (but excluding) its body block, stripping trailing braces.

- `body_field`: field name used to locate the body child; defaults to `"body"`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript:_DECLARATION_KINDS fingerprint=17e6cdd788ff67e7d5266e6c19eadc588560ace250caa34d605a6f53c234240c body_fp=7bee345d9953c57261e02e9206292bbc93b6d72fa08d24b19fc823e3f34f347d source_ref=1ac465220acb62d6851652aa47760d1d3c8fec6d role=config -->
Map tree-sitter node types to their trie kind strings for declaration nodes that carry no executable body.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript:_is_exported fingerprint=3ff13f1603eedf6308c074654280063002d8b2db21efb6b6ad571c909d1d1ca5 body_fp=6634bfe5bdb4c72f1ea0c0d01c95dbd72445e237ef9627809b00b96ca342b342 source_ref=1ac465220acb62d6851652aa47760d1d3c8fec6d role=util -->
Return `True` if `stmt` is an `export_statement` node.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript:_unwrap fingerprint=322af535a5be66568bc0271e62ea3b11b5bea4697fa31a641af125e4ca0f338f body_fp=099ff62c155bf6695cfd985bcc444168a4c9688b495cb22891db34597d514be8 source_ref=1ac465220acb62d6851652aa47760d1d3c8fec6d role=util -->
Unwrap an `export_statement` node to its inner declaration, returning the node itself for any other statement type.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript:extract_symbols fingerprint=2e0b9a6b20e40c45a1d4b3d82c447a40235978962d458779ebc8d92b89379720 body_fp=2b2cb1654f0de2558c6366fb9ecc4c416fa957c9242712d6a2e7c3c3d1ca367d source_ref=1ac465220acb62d6851652aa47760d1d3c8fec6d role=parsing -->
Parse a TypeScript/TSX file and return a deduplicated, source-ordered list of `Symbol` objects.

- `source_root`: used to compute qualified names; defaults to `file_path.parent`
- `source_text`: if provided, parses this string instead of reading the file
- Returns one `Symbol` per top-level declaration plus nested class members and a synthetic `__module__` symbol for residual code
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript:_dispatch_top_level fingerprint=4d9d2d9abed1d89ca7da7c787440b1240cf8bfee033cdacd9337a561994444b6 body_fp=a03a2e280fea6bdf5ddc7a59d7db383e75cfc639f7d6df3d93ea85d5fab0ae0c source_ref=1ac465220acb62d6851652aa47760d1d3c8fec6d role=orchestration -->
Route a single unwrapped top-level AST node to the appropriate builder and call `emit` for each resulting `Symbol`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript:_build_callable fingerprint=8f47807cfe2c98a2038376a560e1ddee5878bc51d82773b6feab3bfcff3a1430 body_fp=d379e7bab0cab8a92208c3ed3ae997da38edd90a1e79d93138a3550817c71f65 source_ref=1ac465220acb62d6851652aa47760d1d3c8fec6d role=parsing -->
Build a `Symbol` for a TypeScript function, method, or arrow function declaration node.

- `parent`: non-`None` sets `kind` to `"method"` and prefixes the qualified name.
- `name_override`: substitutes the name inferred from the node (used for named arrow bindings).
- Body-less declarations (signatures) fingerprint the signature text instead of the body tokens.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript:_build_type_decl fingerprint=b6d2addb616e7abb99c314f2af134db079a94ceea805c249fddd86a9304610bf body_fp=a3d0c177d4936434539bb05704cbb189c6809371b6059c380de55401bc6e7445 source_ref=1ac465220acb62d6851652aa47760d1d3c8fec6d role=parsing -->
Build a `Symbol` for a TypeScript `interface` or `type` alias declaration node.

- `kind`: `"interface"` uses header-only signature; `"type"` uses full node text as signature.
- `outer`: statement node used for line numbers and JSDoc lookup.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript:_walk_class fingerprint=57eee964fc337461271450846922c7e777dfa50c85a1eaad680d7013fa4757ba body_fp=9b5b0e34ac29c6519f2a873803dc4f78d25782d362378453cfc0ca40e36bbff7 source_ref=1ac465220acb62d6851652aa47760d1d3c8fec6d role=parsing -->
Emit a `Symbol` for the class itself plus child `Symbol`s for each method and property member found in its body.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript:_build_property fingerprint=25af33d78bebf54bceac94eaee1888d9edec8bb83d03d007f9ef1b0308b91ec0 body_fp=be2aa5645cd1fb3e7548c068ca13e262f57aab91701232d71b3d4bd58249d3e7 source_ref=1ac465220acb62d6851652aa47760d1d3c8fec6d role=parsing -->
Build a `property` `Symbol` from a class field/property member node, returning `None` if no name can be resolved.

- `class_private`: propagates owning-class privacy to all its members.
- `is_public` is `False` if class is private, name starts with `_`/`#`, or node carries a `private` accessibility modifier.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript:_walk_enum fingerprint=d7501b7700ebe39d5606fb10c2aa4b0e120baa2088e7efea0f647dc4478d1c4d body_fp=579c48f7b98d926d36aab5b952f9520c3eccb71d2a8ae61f07f74cb97a0cdf97 source_ref=1ac465220acb62d6851652aa47760d1d3c8fec6d role=parsing -->
Emit one `enum` `Symbol` plus one `enum_member` `Symbol` per body member for a `enum_declaration` node.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript:_walk_lexical fingerprint=680c218a0d2b4a97923551c480018696512b6f687273e1f521283ffc15432df4 body_fp=76795976a86373871799537800f8e336c1fb92a57fbf7f0083078d2747183610 source_ref=1ac465220acb62d6851652aa47760d1d3c8fec6d role=parsing -->
Extract `Symbol` entries from a top-level `const`/`let`/`var` declaration node, classifying arrow/function-valued bindings as `function` and all others as `constant`; skips destructuring targets.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript:_walk_ambient fingerprint=aac55d121e7c78fa6feeb67b2b0a431421154482a27a2d4b59c904203c72127c body_fp=7114712a49a8c78356a27887977d5eaf62e65781c2543181c9f548d9bdc3f38a source_ref=1ac465220acb62d6851652aa47760d1d3c8fec6d role=parsing -->
Extract `Symbol` entries from an `ambient_declaration` node, handling both `declare module "x" { ... }` blocks and bare `declare function/const` statements.

- `declare module "x"` emits a `module` symbol keyed by the literal string name, plus nested type/function declarations keyed under that name.
- Bare declarations are attributed to `module_key` (the file's own module).
- Returns `(Symbol, Node)` pairs; returns an empty list if the inner node is absent or unrecognised.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript:_build_module_symbol fingerprint=ef3ae1cb0137211c60f839420aac00a41047816a13951bbe84a49a72a17bc6c4 body_fp=cca9db4e50282470cb313377d110d7e32f14e566f750fa384bbf7dde4e2dbebc source_ref=1ac465220acb62d6851652aa47760d1d3c8fec6d role=parsing -->
Build a synthetic `__module__` `Symbol` from top-level AST nodes not claimed by any already-extracted symbol, excluding imports and comments.

- `consumed`: line ranges already owned by extracted symbols; used to skip those nodes.
- Returns `None` when no residual top-level code remains.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript:_public fingerprint=43a901961a19106b65439a7826d1f2863780b09091dc04d11f3bfc6dfd941270 body_fp=c5936b453ef5c545275fdd50574cefea72b68dbee9a51d0b39d5e7b10b6e5a51 source_ref=1ac465220acb62d6851652aa47760d1d3c8fec6d role=util -->
Return whether a symbol is public based on its name, export status, and parent privacy.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript:_member_name fingerprint=1248ba030404db61f94f702b3e5d5f12ae616c001cc861112ca8cb4d06eeddd3 body_fp=c89009c66fe10664ed71b46d073b81b0f608642e3c36d6cc834f4a96f4127077 source_ref=1ac465220acb62d6851652aa47760d1d3c8fec6d role=util -->
Extract the declared name from a class member node, falling back to scanning named children for identifier-typed nodes.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript:_has_modifier fingerprint=2ff0423fd2385b4a3cd176ae43842b1667835b61e5d7cbcddce309b2b06b4e01 body_fp=851c91b88ffc8432b11ad069ac5b0f53449f02b6e7fab61658947d9966e777e6 source_ref=1ac465220acb62d6851652aa47760d1d3c8fec6d role=util -->
Return `True` if any named child of `node` is an `accessibility_modifier` matching `modifier`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript:_first_child_of_type fingerprint=2f9c592029e617284efbf38c01c0ad8701b7d8a7e20aaba09f1e0de2545c75df body_fp=6c66d234ea8a44cdb30e91da22732f27f589312cc0b89ab3fd8618abe6c750a9 source_ref=1ac465220acb62d6851652aa47760d1d3c8fec6d role=util -->
Return the first named child of `node` whose type equals `type_name`, or `None`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript:TS_SYSTEM_PROMPT fingerprint=523395e0a833b64879f69133b4728bcddd9ad2d969d17af2dcbd23988ae67be2 body_fp=627b38ffd1b0dcc3119dae55d61a1e680ded005416cd0c7a89c57f13c9d0270a source_ref=1ac465220acb62d6851652aa47760d1d3c8fec6d role=config -->
System prompt string passed to the LLM when generating documentation for TypeScript symbols.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript:TypeScriptBackend fingerprint=037f9407f3cfca2b9a692b51de5b57005ef0cef32c3972e71e5c1108f082c722 body_fp=bc8d102aca3e4d7956c73e681523838eaa617a6a5eee49acd039e33cea5c5b6f source_ref=e26a1192f6add3e1cab718bb626a08a23e9d5981 role=domain -->
Implements `LanguageBackend` for `.ts`, `.tsx`, `.d.ts`, `.jsx`, `.mjs`, `.cjs`, and `.js` files, wiring two-pass reference extraction (tree-sitter + optional LSP resolver), symbol extraction, and the system prompt.

- `extensions`: ordered longest-first so `.d.ts` resolves before `.ts`; JavaScript suffixes included as the TS grammar is a superset
- `extract_file_data`: delegates to `typescript_refs`; merges LSP-resolved member-dispatch edges when a resolver is available; does not support `source_text` override
- `resolver()`: returns a cached `LspResolver` for typescript-language-server, or `None` if `TRIE_DISABLE_RESOLVER=1` or the server is not on PATH
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript:TypeScriptBackend.__init__ fingerprint=b84739b0fbbdbeb6b33571852fef53390cb973b63bb786a1526af79058a93652 body_fp=779a4e01c23334eee94cbe132b8047b27c8a5ab40c03b5b4ab51dec6bbdc3b04 source_ref=e1c63593dc55002aae32a954ca66e5ff7d7fb810 role=domain -->
Initialize `TypeScriptBackend` with `_resolver` and `_resolver_built` set to their unbuilt defaults.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript:TypeScriptBackend.extract_file_data fingerprint=dc038b10128bc6c9df2eb8bf837d237120f2d33f6afad6d8ba9bbc26aec49bcd body_fp=dd91f6f1ef6d8748b4c3c103b9a1fdc56304e5dc499d8ef2761c2c1ff876c5f7 source_ref=e1c63593dc55002aae32a954ca66e5ff7d7fb810 role=orchestration -->
Extract `TypeScriptBackend` file data via `typescript_refs.extract_file_data`, then merge LSP resolver references if available; raises `NotImplementedError` if `source_text` is supplied.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript:TypeScriptBackend.extract_symbols fingerprint=af266339106949531c076cf2e82cb2565f65b39795b7b77394086774fac189f3 body_fp=5e85f9bd9b18072ccf379bf3036f775de01fa136dd04c2ccfb1cf0eadc9a8086 source_ref=1ac465220acb62d6851652aa47760d1d3c8fec6d role=api -->
Delegate `TypeScriptBackend.extract_symbols` to the module-level `extract_symbols` function, returning its `list[Symbol]`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript:TypeScriptBackend.source_suffix fingerprint=bf61bb997784ff6713e45a76a5457a002dd12cc7b8a0a2a6a054575fb2fdd368 body_fp=bd42ad83b15c990aa0a01eab4bbf4b521db872a2c6f86c0276229b3287ecb667 source_ref=1ac465220acb62d6851652aa47760d1d3c8fec6d role=api -->
`TypeScriptBackend.source_suffix` returns the canonical source file extension `".ts"`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript:TypeScriptBackend.system_prompt fingerprint=4a9cf48bef1c51973826ab0b4182de46d91cdb98cee34a2fc01a12e68369f30a body_fp=77fed3c1e333fdeed04723e2f7a6b6a9d827037581383564c020f6820f386fef source_ref=1ac465220acb62d6851652aa47760d1d3c8fec6d role=api -->
Return the `TypeScriptBackend`'s documentation-generation system prompt string.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/typescript:TypeScriptBackend.resolver fingerprint=d053fde1515981c50c6325556606271ab03040b1b3292e317e230d51dccce10e body_fp=e847455ed071013e175de3beb3215ed76414026413f6f2f8e0f7d703d28568ee source_ref=e1c63593dc55002aae32a954ca66e5ff7d7fb810 role=orchestration -->
`TypeScriptBackend.resolver` returns a cached `LspResolver` for `typescript-language-server`, or `None` if disabled or unavailable.

- Sets `TRIE_DISABLE_RESOLVER=1` to force `None` (tree-sitter-only mode).
- Degrades to `None` when `typescript-language-server` is not on PATH.
- Result is built once and cached in `_resolver`.
<!-- trie:end -->