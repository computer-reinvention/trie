---
trie_version: 0.3.0
source: trie/parse/rust.py
file_fingerprint: 2a1e34aed08d644c8be3335cdf2d76b8f5e2bcbe76b95b63b347c7fd679e6c3e
last_synced_at: '2026-08-02T21:19:43Z'
description: "Rust language backend \u2014 tree-sitter symbols + references, paired with rust-analyzer."
defines:
- kind: module
  qualified_name: trie/parse/rust:__module__
  lines: 1-352
- kind: constant
  qualified_name: trie/parse/rust:RUST_LANGUAGE
  lines: 27-27
- kind: function
  qualified_name: trie/parse/rust:_make_parser
  lines: 30-33
  signature: def _make_parser() -> Parser
- kind: function
  qualified_name: trie/parse/rust:_node_text
  lines: 36-37
  signature: 'def _node_text(node: Node, source: bytes) -> str'
- kind: function
  qualified_name: trie/parse/rust:_hash
  lines: 40-41
  signature: 'def _hash(s: str) -> str'
- kind: function
  qualified_name: trie/parse/rust:_module_key
  lines: 44-46
  signature: 'def _module_key(file_path: Path, source_root: Path) -> str'
- kind: function
  qualified_name: trie/parse/rust:_signature_text
  lines: 49-52
  signature: 'def _signature_text(node: Node, source: bytes) -> str'
- kind: function
  qualified_name: trie/parse/rust:_has_pub
  lines: 55-56
  signature: 'def _has_pub(node: Node, source: bytes) -> bool'
- kind: function
  qualified_name: trie/parse/rust:_make_symbol
  lines: 59-89
  signature: 'def _make_symbol( node: Node, source: bytes, *, module_key: str, rel_file: str, name: str, kind: str, parent: str | None = None, parent_is_private: bool = False, ) -> Symbol'
- kind: function
  qualified_name: trie/parse/rust:_type_name
  lines: 92-97
  signature: 'def _type_name(node: Node, source: bytes) -> str | None'
- kind: function
  qualified_name: trie/parse/rust:_impl_target
  lines: 100-112
  signature: 'def _impl_target(impl_node: Node, source: bytes) -> str | None'
- kind: function
  qualified_name: trie/parse/rust:extract_symbols
  lines: 115-192
  signature: 'def extract_symbols( file_path: Path, source_root: Path | None = None, *, source_text: str | None = None, ) -> list[Symbol]'
- kind: function
  qualified_name: trie/parse/rust:_find_node_for_symbol
  lines: 195-217
  signature: 'def _find_node_for_symbol(root: Node, sym: Symbol) -> Node | None'
- kind: function
  qualified_name: trie/parse/rust:_collect_call_names
  lines: 220-244
  signature: 'def _collect_call_names(node: Node, source: bytes) -> set[str]'
- kind: function
  qualified_name: trie/parse/rust:extract_file_data
  lines: 247-278
  signature: 'def extract_file_data(file_path: Path, source_root: Path | None = None) -> FileData'
- kind: constant
  qualified_name: trie/parse/rust:RUST_SYSTEM_PROMPT
  lines: 281-291
- kind: class
  qualified_name: trie/parse/rust:RustBackend
  lines: 294-348
  signature: class RustBackend
- kind: method
  qualified_name: trie/parse/rust:RustBackend.__init__
  lines: 300-302
  signature: def __init__(self) -> None
- kind: method
  qualified_name: trie/parse/rust:RustBackend.extract_file_data
  lines: 304-324
  signature: def extract_file_data(self, file_path, source_root=None, *, source_text=None)
- kind: method
  qualified_name: trie/parse/rust:RustBackend.extract_symbols
  lines: 326-327
  signature: def extract_symbols(self, file_path, source_root=None, *, source_text=None)
- kind: method
  qualified_name: trie/parse/rust:RustBackend.source_suffix
  lines: 329-330
  signature: def source_suffix(self) -> str
- kind: method
  qualified_name: trie/parse/rust:RustBackend.system_prompt
  lines: 332-333
  signature: def system_prompt(self) -> str
- kind: method
  qualified_name: trie/parse/rust:RustBackend.resolver
  lines: 335-348
  signature: def resolver(self)
- kind: constant
  qualified_name: trie/parse/rust:__all__
  lines: 351-351
incoming_refs: 0
outgoing_refs: 13
---
<!-- trie:section symbol=trie/parse/rust:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=80e78a62374e9427ab0bb591019b67543e42be57eb21777ff2528c5289ed3d6b source_ref=691e392482cc3a6201730f4563d13b86ffadd010 role=parsing -->
Rust language backend implementing tree-sitter-based symbol extraction and reference resolution, paired with rust-analyzer via LSP.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/rust:RUST_LANGUAGE fingerprint=a15f62255f1a1e1e4b7db7679548dfbcac77c27a12c0e16b6642af8876516f16 body_fp=0e301669ded6b4f92d525c7f6ce4ba734bc9d7f439cf629b57bc38bf98f21a9e source_ref=691e392482cc3a6201730f4563d13b86ffadd010 role=config -->
Module-level `Language` instance wrapping the compiled tree-sitter Rust grammar, shared by all parsers in this module.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/rust:_make_parser fingerprint=24b97cc6800e99acc3abf123fc8c49bf1460d05b0905f19ca973b42f0b9dc018 body_fp=db8376cc7b3b9caa4f7f6948e2e824048ee38b48536417f099035f731520bb12 source_ref=691e392482cc3a6201730f4563d13b86ffadd010 role=util -->
## `def _make_parser() -> Parser`

Construct and return a `Parser` configured with `RUST_LANGUAGE`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/rust:_node_text fingerprint=90272da3050ae7f74f98b5fb62c5860239cd69d3c98b9843ee7816f84677e986 body_fp=4faa7e80c6ae3aa156c18b4b9b9947dce11f95c41d271b6b752b3dd6d23059ae source_ref=691e392482cc3a6201730f4563d13b86ffadd010 role=util -->
## `def _node_text(node: Node, source: bytes) -> str`

Decode the byte slice of `source` spanned by `node` into a UTF-8 string, replacing invalid bytes.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/rust:_hash fingerprint=7057d302a510678c4e042810b0eb270cc10d5047cb0a03fac868582b067b5767 body_fp=6669477292c01bece7ef1f4345e604d994c8aba94e5f3aa365f05018167230e1 source_ref=691e392482cc3a6201730f4563d13b86ffadd010 role=util -->
## `def _hash(s: str) -> str`

Return the SHA-256 hex digest of a UTF-8-encoded string.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/rust:_module_key fingerprint=af6ee1ee42882ba9ba4e716ba32e14d2b07819ce55d6304c1c80c90e619356e9 body_fp=921f2d267d681a30f6add2e168144fda3f0b8b769da0e901a508627518273758 source_ref=691e392482cc3a6201730f4563d13b86ffadd010 role=util -->
## `def _module_key(file_path: Path, source_root: Path) -> str`

Compute the module key for a file by returning its path relative to `source_root`, stripped of its file extension.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/rust:_signature_text fingerprint=3e7f37536210d477545d5995b8a7a8b4b95ee2117b8566740ba3bd54de76a953 body_fp=e84e5f45fc21d0284b5fcf86ac52045021e120b4997221591da5af84089f373a source_ref=691e392482cc3a6201730f4563d13b86ffadd010 role=parsing -->
## `def _signature_text(node: Node, source: bytes) -> str`

Extract the signature text of a node by slicing source bytes up to the body's start (or node end if bodyless).
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/rust:_has_pub fingerprint=8ed2f989853e407cb84eeb072fc0481b8b92ec8046ebf03d4b3dffce803731ff body_fp=b34f6921610db8d79963dc2c73253ea516c757a3ff0287f7d8d07ab0b37daa58 source_ref=691e392482cc3a6201730f4563d13b86ffadd010 role=util -->
## `def _has_pub(node: Node, source: bytes) -> bool`

Return `True` if any named child of `node` is a `visibility_modifier` (i.e. the item has a `pub` qualifier).
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/rust:_make_symbol fingerprint=7e88845c06eb1884da0b6e9ce615afcef8a41b6eadf03ff9f274d7770e41c65e body_fp=6bc19e8387fda965ab5ab182f9d5c495dc5cf1498fb39d31a8ed7d9f3168cef0 source_ref=691e392482cc3a6201730f4563d13b86ffadd010 role=parsing -->
## `def _make_symbol( node: Node, source: bytes, *, module_key: str, rel_file: str, name: str, kind: str, parent: str | None = None, parent_is_private: bool = False, ) -> Symbol`

Construct and return a `Symbol` from a tree-sitter `Node` and its parsed metadata.

- `parent`: if set, qualified name becomes `parent.name`; sets `parent_class`.
- `parent_is_private`: forces `is_public=False` regardless of the node's visibility modifier.
- `docstring` is always `None` (not extracted for Rust in v1).
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/rust:_type_name fingerprint=e22f48e53ada3810952aff075ade9562b102b64abf6265b1af038692ab56fcfc body_fp=8c0cf14dcc124668d016002cb88db2f9995af35f109d2c74cdd4c0b8f6ab7ea5 source_ref=691e392482cc3a6201730f4563d13b86ffadd010 role=parsing -->
## `def _type_name(node: Node, source: bytes) -> str | None`

Return the text of the first `type_identifier` child of `node`, or `None` if absent.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/rust:_impl_target fingerprint=7a29e97690ce816aaae55ec2f2037ffbec522cede45dd3ec577aca050e0cb9cb body_fp=241a339f4d44c269e5fa2d009ca26d5adfe62e1cdb1da3132d0efec67a02c2ce source_ref=691e392482cc3a6201730f4563d13b86ffadd010 role=parsing -->
## `def _impl_target(impl_node: Node, source: bytes) -> str | None`

Extract the concrete type name targeted by an `impl` block, returning the last `type_identifier` before the body.

- Returns `None` if no `type_identifier` is found.
- For `impl Trait for Type`, returns `Type` (the final identifier), not the trait name.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/rust:extract_symbols fingerprint=4077c424d3e9d1165007fa6240bca4c02bc23cdaba13ffa3ebb4af39aea140ce body_fp=8a5fb779f158972ecd1004edd691608a9fd888ce35a10d1fcb482b0cbc345e88 source_ref=691e392482cc3a6201730f4563d13b86ffadd010 role=parsing -->
## `def extract_symbols( file_path: Path, source_root: Path | None = None, *, source_text: str | None = None, ) -> list[Symbol]`

Parse a Rust source file with tree-sitter and return all top-level `Symbol` objects for functions, structs, enums, traits, type aliases, constants, statics, and impl/trait methods.

- `source_root`: used to compute the module key and relative file path; defaults to `file_path.parent`.
- `source_text`: if provided, parses this string instead of reading `file_path` from disk.
- Impl methods are attributed to the concrete type (the last `type_identifier` before the body); trait-private or `_`-prefixed type names mark child symbols as non-public.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/rust:_find_node_for_symbol fingerprint=6e3fd105cf827c47cefe99c9f7bae3dc099b458c002103265a8bd7f2ca615f12 body_fp=3bafdb165f35af59610fa1b116c1207ab37b72c7efe9120b37a1a10509a189d1 source_ref=691e392482cc3a6201730f4563d13b86ffadd010 role=parsing -->
## `def _find_node_for_symbol(root: Node, sym: Symbol) -> Node | None`

Walk the tree-sitter `root` node depth-first to find the first declaration node whose start line matches `sym.start_line`.

- Returns `None` if no matching node is found.
- Only matches nodes of types: `function_item`, `struct_item`, `enum_item`, `trait_item`, `type_item`, `const_item`, `static_item`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/rust:_collect_call_names fingerprint=055d43880cc21b673d869c477cb87969624ee45e749e51310453dbcbdb3a46dc body_fp=48476d99dfad4aed71ea929930f56493240e82970cf9c1e7e56f8fa96e7f16a4 source_ref=691e392482cc3a6201730f4563d13b86ffadd010 role=parsing -->
## `def _collect_call_names(node: Node, source: bytes) -> set[str]`

Recursively walk a tree-sitter `Node` and collect the callee name from every `call_expression`, skipping comment and string nodes.

- Returns bare name only: `foo()` → `"foo"`, `x.m()` → `"m"`, `Type::new()` → `"new"`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/rust:extract_file_data fingerprint=9d46e838d84e0b3bec09e1c0d4ec9a474a40bf95ba79e310f9a8934029a7e46d body_fp=32a7968e26cd688eaaa0f2bd976ff697bd5b7aa5263f9ea27b8d8d51bbc177da source_ref=691e392482cc3a6201730f4563d13b86ffadd010 role=parsing -->
## `def extract_file_data(file_path: Path, source_root: Path | None = None) -> FileData`

Parse a Rust source file and return all its `Symbol`s plus intra-file `"calls"` `Reference`s between top-level symbols.

- `source_root`: defaults to the file's parent directory; used to compute qualified names and relative paths.
- References are deduplicated and only recorded for calls to top-level (non-method) symbols within the same file.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/rust:RUST_SYSTEM_PROMPT fingerprint=84828a37f69007a2b37802e549aafef6727d920e4d064fbb440b09942ef629c7 body_fp=eb5dcbf84e05927a74f78323624d4902f7e378d0f32cad36239f9c57756407d0 source_ref=691e392482cc3a6201730f4563d13b86ffadd010 role=config -->
System prompt string injected into LLM documentation requests for Rust symbols in a code-navigation graph.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/rust:RustBackend fingerprint=576add4211d9f09d3f540ca051c684f4b2ec8c93a35d178d74a769ed394e8654 body_fp=2c9af9384eab920d453933a22e78e3958358cf2f21496d7afd2b820b6de4fe0d source_ref=691e392482cc3a6201730f4563d13b86ffadd010 role=domain -->
## `class RustBackend`

Implements the `LanguageBackend` interface for Rust, combining tree-sitter symbol extraction with an optional rust-analyzer LSP resolver for cross-file references.

- `extract_file_data`: raises `NotImplementedError` if `source_text` is provided; merges LSP references when a resolver is available.
- `resolver()`: lazily builds an `LspResolver` on first call; returns `None` if `TRIE_DISABLE_RESOLVER=1` or no spec is found.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/rust:RustBackend.__init__ fingerprint=b84739b0fbbdbeb6b33571852fef53390cb973b63bb786a1526af79058a93652 body_fp=781cb3fb52e96f9a07537acc6e55e5914d56c661efb63645cc6f3c934d82721a source_ref=691e392482cc3a6201730f4563d13b86ffadd010 role=domain -->
## `def __init__(self) -> None`

Initialize `RustBackend` with a deferred-resolver sentinel (`_resolver=None`, `_resolver_built=False`).
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/rust:RustBackend.extract_file_data fingerprint=b20e0b87585336f45b65241da08a639004c8728e185ae83f13add911ee485f41 body_fp=87696ebfcbdf006c68b01a74e2f316e804facb2c7e085275017a3f9020dde40f source_ref=691e392482cc3a6201730f4563d13b86ffadd010 role=orchestration -->
## `def extract_file_data(self, file_path, source_root=None, *, source_text=None)`

Extracts `FileData` for a Rust file, merging LSP-resolved references from `RustBackend.resolver()` into the tree-sitter results.

- `source_text`: not supported; raises `NotImplementedError` if provided.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/rust:RustBackend.extract_symbols fingerprint=af266339106949531c076cf2e82cb2565f65b39795b7b77394086774fac189f3 body_fp=07b62ec97b6118f06899ceb2303b93dfb788991c6e708108049628dce83c3b83 source_ref=691e392482cc3a6201730f4563d13b86ffadd010 role=api -->
## `def extract_symbols(self, file_path, source_root=None, *, source_text=None)`

Delegates `RustBackend` symbol extraction to the module-level `extract_symbols` function.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/rust:RustBackend.source_suffix fingerprint=9bc7a4bf2fbf8a5f04e03d4a01379ccf5a0f44588ed350f3cd34cf50030a45eb body_fp=15d267bf8b4105b92f25d4937713c381a960bd6e104bc42fa91cda744fb000cf source_ref=691e392482cc3a6201730f4563d13b86ffadd010 role=util -->
## `def source_suffix(self) -> str`

Returns the `RustBackend` file extension string `".rs"`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/rust:RustBackend.system_prompt fingerprint=e057f15af0cfc76804574f0f4168b9b0137fefba6109f55b2a559b48a5126ff9 body_fp=51cbbf858f4aa90c82b9ecfb943f6a2c7af76fc4e5cb63fc99b10716e5c9e7b8 source_ref=691e392482cc3a6201730f4563d13b86ffadd010 role=api -->
## `def system_prompt(self) -> str`

Returns the `RUST_SYSTEM_PROMPT` constant string for use by `RustBackend`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/rust:RustBackend.resolver fingerprint=599d606cfbfcee55e1a7b7283148e4ea4524833cea7c56e20fa39e3e494d9a30 body_fp=601872a6c23678c3809f693bf39ce9c901261f8d7e5e9568f80b21d4e6624aca source_ref=691e392482cc3a6201730f4563d13b86ffadd010 role=config -->
## `def resolver(self)`

Return the lazily-initialised `LspResolver` for `RustBackend`, building it once from `rust_spec()` or `None` if `TRIE_DISABLE_RESOLVER=1` or no spec is available.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/rust:__all__ fingerprint=5f25424300fb366f49caabe08fa226cfa15ddd3b4f2b2b6a23e4fe2b8569a5dc body_fp=cd196fb7d4e2ece6b692defa9fd6be31c88b6d9500dfcce40d59cf4c5578f14e source_ref=691e392482cc3a6201730f4563d13b86ffadd010 role=config -->
Declares the public API surface of the `trie.parse.rust` module.
<!-- trie:end -->