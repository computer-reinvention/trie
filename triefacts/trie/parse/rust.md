---
trie_version: 0.1.9
source: trie/parse/rust.py
file_fingerprint: 2a1e34aed08d644c8be3335cdf2d76b8f5e2bcbe76b95b63b347c7fd679e6c3e
last_synced_at: '2026-07-29T00:06:25Z'
description: "Rust language backend \u2014 tree-sitter symbols + references, paired\
  \ with rust-analyzer."
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
- kind: function
  qualified_name: trie/parse/rust:_node_text
  lines: 36-37
- kind: function
  qualified_name: trie/parse/rust:_hash
  lines: 40-41
- kind: function
  qualified_name: trie/parse/rust:_module_key
  lines: 44-46
- kind: function
  qualified_name: trie/parse/rust:_signature_text
  lines: 49-52
- kind: function
  qualified_name: trie/parse/rust:_has_pub
  lines: 55-56
- kind: function
  qualified_name: trie/parse/rust:_make_symbol
  lines: 59-89
- kind: function
  qualified_name: trie/parse/rust:_type_name
  lines: 92-97
- kind: function
  qualified_name: trie/parse/rust:_impl_target
  lines: 100-112
- kind: function
  qualified_name: trie/parse/rust:extract_symbols
  lines: 115-192
- kind: function
  qualified_name: trie/parse/rust:_find_node_for_symbol
  lines: 195-217
- kind: function
  qualified_name: trie/parse/rust:_collect_call_names
  lines: 220-244
- kind: function
  qualified_name: trie/parse/rust:extract_file_data
  lines: 247-278
- kind: constant
  qualified_name: trie/parse/rust:RUST_SYSTEM_PROMPT
  lines: 281-291
- kind: class
  qualified_name: trie/parse/rust:RustBackend
  lines: 294-348
- kind: method
  qualified_name: trie/parse/rust:RustBackend.__init__
  lines: 300-302
- kind: method
  qualified_name: trie/parse/rust:RustBackend.extract_file_data
  lines: 304-324
- kind: method
  qualified_name: trie/parse/rust:RustBackend.extract_symbols
  lines: 326-327
- kind: method
  qualified_name: trie/parse/rust:RustBackend.source_suffix
  lines: 329-330
- kind: method
  qualified_name: trie/parse/rust:RustBackend.system_prompt
  lines: 332-333
- kind: method
  qualified_name: trie/parse/rust:RustBackend.resolver
  lines: 335-348
- kind: constant
  qualified_name: trie/parse/rust:__all__
  lines: 351-351
incoming_refs: 0
outgoing_refs: 6
---
<!-- trie:section symbol=trie/parse/rust:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=80e78a62374e9427ab0bb591019b67543e42be57eb21777ff2528c5289ed3d6b source_ref=691e392482cc3a6201730f4563d13b86ffadd010 role=parsing -->
Rust language backend implementing tree-sitter-based symbol extraction and reference resolution, paired with rust-analyzer via LSP.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/rust:RUST_LANGUAGE fingerprint=a15f62255f1a1e1e4b7db7679548dfbcac77c27a12c0e16b6642af8876516f16 body_fp=0e301669ded6b4f92d525c7f6ce4ba734bc9d7f439cf629b57bc38bf98f21a9e source_ref=691e392482cc3a6201730f4563d13b86ffadd010 role=config -->
Module-level `Language` instance wrapping the compiled tree-sitter Rust grammar, shared by all parsers in this module.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/rust:_make_parser fingerprint=24b97cc6800e99acc3abf123fc8c49bf1460d05b0905f19ca973b42f0b9dc018 body_fp=b5eee1f2e9bd1c332c929cbcde6b8bbc12aa06f02e08dc66e41372100060192e source_ref=691e392482cc3a6201730f4563d13b86ffadd010 role=util -->
Construct and return a `Parser` configured with `RUST_LANGUAGE`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/rust:_node_text fingerprint=90272da3050ae7f74f98b5fb62c5860239cd69d3c98b9843ee7816f84677e986 body_fp=4456e126d229197868b923da30c01984a6c98aa3a6236a84aa4e74c57880b918 source_ref=691e392482cc3a6201730f4563d13b86ffadd010 role=util -->
Decode the byte slice of `source` spanned by `node` into a UTF-8 string, replacing invalid bytes.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/rust:_hash fingerprint=7057d302a510678c4e042810b0eb270cc10d5047cb0a03fac868582b067b5767 body_fp=4d6c535ddd567d3e1fea8feeb45a70dc232492d2f3105352d59a2cda51262480 source_ref=691e392482cc3a6201730f4563d13b86ffadd010 role=util -->
Return the SHA-256 hex digest of a UTF-8-encoded string.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/rust:_module_key fingerprint=af6ee1ee42882ba9ba4e716ba32e14d2b07819ce55d6304c1c80c90e619356e9 body_fp=b396c49d12e9365cc23226652f5a29c11bd14dca6bf11001ff406315f24f65ef source_ref=691e392482cc3a6201730f4563d13b86ffadd010 role=util -->
Compute the module key for a file by returning its path relative to `source_root`, stripped of its file extension.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/rust:_signature_text fingerprint=3e7f37536210d477545d5995b8a7a8b4b95ee2117b8566740ba3bd54de76a953 body_fp=0370953fc657461b24ac5d8d958767a57db29acb261bf9e7adc93f1e9fb51cba source_ref=691e392482cc3a6201730f4563d13b86ffadd010 role=parsing -->
Extract the signature text of a node by slicing source bytes up to the body's start (or node end if bodyless).
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/rust:_has_pub fingerprint=8ed2f989853e407cb84eeb072fc0481b8b92ec8046ebf03d4b3dffce803731ff body_fp=e06d4d95c014f11345f24653b67cd787efc8769f3c18be898c5cbd0cdd84fa69 source_ref=691e392482cc3a6201730f4563d13b86ffadd010 role=util -->
Return `True` if any named child of `node` is a `visibility_modifier` (i.e. the item has a `pub` qualifier).
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/rust:_make_symbol fingerprint=7e88845c06eb1884da0b6e9ce615afcef8a41b6eadf03ff9f274d7770e41c65e body_fp=2a7fa14ff421d61264c87ef231bd4f3d14d333c26193f3184e726aeae9da2b0b source_ref=691e392482cc3a6201730f4563d13b86ffadd010 role=parsing -->
Construct and return a `Symbol` from a tree-sitter `Node` and its parsed metadata.

- `parent`: if set, qualified name becomes `parent.name`; sets `parent_class`.
- `parent_is_private`: forces `is_public=False` regardless of the node's visibility modifier.
- `docstring` is always `None` (not extracted for Rust in v1).
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/rust:_type_name fingerprint=e22f48e53ada3810952aff075ade9562b102b64abf6265b1af038692ab56fcfc body_fp=d45427c49257cf4b1abb3fea1f85975ca615118cedac7c7b7dfada833ce51185 source_ref=691e392482cc3a6201730f4563d13b86ffadd010 role=parsing -->
Return the text of the first `type_identifier` child of `node`, or `None` if absent.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/rust:_impl_target fingerprint=7a29e97690ce816aaae55ec2f2037ffbec522cede45dd3ec577aca050e0cb9cb body_fp=cc245dfeda1229dc49acac15e3ae80563214e2c8404ca02223a0a916616760de source_ref=691e392482cc3a6201730f4563d13b86ffadd010 role=parsing -->
Extract the concrete type name targeted by an `impl` block, returning the last `type_identifier` before the body.

- Returns `None` if no `type_identifier` is found.
- For `impl Trait for Type`, returns `Type` (the final identifier), not the trait name.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/rust:extract_symbols fingerprint=4077c424d3e9d1165007fa6240bca4c02bc23cdaba13ffa3ebb4af39aea140ce body_fp=9ddd6e96790724cf996ed3c0580b9e396e826ea74a3936e90e0883cf8ea3e332 source_ref=691e392482cc3a6201730f4563d13b86ffadd010 role=parsing -->
Parse a Rust source file with tree-sitter and return all top-level `Symbol` objects for functions, structs, enums, traits, type aliases, constants, statics, and impl/trait methods.

- `source_root`: used to compute the module key and relative file path; defaults to `file_path.parent`.
- `source_text`: if provided, parses this string instead of reading `file_path` from disk.
- Impl methods are attributed to the concrete type (the last `type_identifier` before the body); trait-private or `_`-prefixed type names mark child symbols as non-public.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/rust:_find_node_for_symbol fingerprint=6e3fd105cf827c47cefe99c9f7bae3dc099b458c002103265a8bd7f2ca615f12 body_fp=474e52d73fdeb2c4949a60314b0e15033db165cb247d20fa5a1e12709d4e6475 source_ref=691e392482cc3a6201730f4563d13b86ffadd010 role=parsing -->
Walk the tree-sitter `root` node depth-first to find the first declaration node whose start line matches `sym.start_line`.

- Returns `None` if no matching node is found.
- Only matches nodes of types: `function_item`, `struct_item`, `enum_item`, `trait_item`, `type_item`, `const_item`, `static_item`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/rust:_collect_call_names fingerprint=055d43880cc21b673d869c477cb87969624ee45e749e51310453dbcbdb3a46dc body_fp=0614853be493dbd45896c74b693c0e876f792a006a10a02c5e672d4d28953db7 source_ref=691e392482cc3a6201730f4563d13b86ffadd010 role=parsing -->
Recursively walk a tree-sitter `Node` and collect the callee name from every `call_expression`, skipping comment and string nodes.

- Returns bare name only: `foo()` → `"foo"`, `x.m()` → `"m"`, `Type::new()` → `"new"`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/rust:extract_file_data fingerprint=9d46e838d84e0b3bec09e1c0d4ec9a474a40bf95ba79e310f9a8934029a7e46d body_fp=8fe74c91e080a3ee7ac311ff7b34b6d610b681b0c0e79f45fbb45743720977d5 source_ref=691e392482cc3a6201730f4563d13b86ffadd010 role=parsing -->
Parse a Rust source file and return all its `Symbol`s plus intra-file `"calls"` `Reference`s between top-level symbols.

- `source_root`: defaults to the file's parent directory; used to compute qualified names and relative paths.
- References are deduplicated and only recorded for calls to top-level (non-method) symbols within the same file.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/rust:RUST_SYSTEM_PROMPT fingerprint=84828a37f69007a2b37802e549aafef6727d920e4d064fbb440b09942ef629c7 body_fp=eb5dcbf84e05927a74f78323624d4902f7e378d0f32cad36239f9c57756407d0 source_ref=691e392482cc3a6201730f4563d13b86ffadd010 role=config -->
System prompt string injected into LLM documentation requests for Rust symbols in a code-navigation graph.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/rust:RustBackend fingerprint=576add4211d9f09d3f540ca051c684f4b2ec8c93a35d178d74a769ed394e8654 body_fp=85debf5346599bf8939d267ca2fcc339ac67bf08881294b15fc4dd6b3426fa1f source_ref=691e392482cc3a6201730f4563d13b86ffadd010 role=domain -->
Implements the `LanguageBackend` interface for Rust, combining tree-sitter symbol extraction with an optional rust-analyzer LSP resolver for cross-file references.

- `extract_file_data`: raises `NotImplementedError` if `source_text` is provided; merges LSP references when a resolver is available.
- `resolver()`: lazily builds an `LspResolver` on first call; returns `None` if `TRIE_DISABLE_RESOLVER=1` or no spec is found.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/rust:RustBackend.__init__ fingerprint=b84739b0fbbdbeb6b33571852fef53390cb973b63bb786a1526af79058a93652 body_fp=e8410a6c02f04682919dc382a41fe9d610b20e614a9469f6c3e63fb346cf5b83 source_ref=691e392482cc3a6201730f4563d13b86ffadd010 role=domain -->
Initialize `RustBackend` with a deferred-resolver sentinel (`_resolver=None`, `_resolver_built=False`).
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/rust:RustBackend.extract_file_data fingerprint=b20e0b87585336f45b65241da08a639004c8728e185ae83f13add911ee485f41 body_fp=6df7faefb6c697480bb75cac58c56d563b6fc49b1ea95e5e785fe8cc775e77ed source_ref=691e392482cc3a6201730f4563d13b86ffadd010 role=orchestration -->
Extracts `FileData` for a Rust file, merging LSP-resolved references from `RustBackend.resolver()` into the tree-sitter results.

- `source_text`: not supported; raises `NotImplementedError` if provided.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/rust:RustBackend.extract_symbols fingerprint=af266339106949531c076cf2e82cb2565f65b39795b7b77394086774fac189f3 body_fp=16156661831ed8830e133d0b43bdf9ec21424c2ea5a0892c978a734e4dda42f0 source_ref=691e392482cc3a6201730f4563d13b86ffadd010 role=api -->
Delegates `RustBackend` symbol extraction to the module-level `extract_symbols` function.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/rust:RustBackend.source_suffix fingerprint=9bc7a4bf2fbf8a5f04e03d4a01379ccf5a0f44588ed350f3cd34cf50030a45eb body_fp=faa6ea057ca3c54599ab6533556fff46f4d28ad1b208182992b02874b2a972ad source_ref=691e392482cc3a6201730f4563d13b86ffadd010 role=util -->
Returns the `RustBackend` file extension string `".rs"`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/rust:RustBackend.system_prompt fingerprint=e057f15af0cfc76804574f0f4168b9b0137fefba6109f55b2a559b48a5126ff9 body_fp=1bbbade1a4c3ddb37759311d634b25a8e8c2a4282a40c1e145d8307309aa41ce source_ref=691e392482cc3a6201730f4563d13b86ffadd010 role=api -->
Returns the `RUST_SYSTEM_PROMPT` constant string for use by `RustBackend`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/rust:RustBackend.resolver fingerprint=599d606cfbfcee55e1a7b7283148e4ea4524833cea7c56e20fa39e3e494d9a30 body_fp=c01404c1089ea8e79ffc923b0141968fa9490fae35e5d097afbe18d98b0af8bb source_ref=691e392482cc3a6201730f4563d13b86ffadd010 role=config -->
Return the lazily-initialised `LspResolver` for `RustBackend`, building it once from `rust_spec()` or `None` if `TRIE_DISABLE_RESOLVER=1` or no spec is available.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/rust:__all__ fingerprint=5f25424300fb366f49caabe08fa226cfa15ddd3b4f2b2b6a23e4fe2b8569a5dc body_fp=cd196fb7d4e2ece6b692defa9fd6be31c88b6d9500dfcce40d59cf4c5578f14e source_ref=691e392482cc3a6201730f4563d13b86ffadd010 role=config -->
Declares the public API surface of the `trie.parse.rust` module.
<!-- trie:end -->