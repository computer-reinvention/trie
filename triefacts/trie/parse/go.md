---
trie_version: 0.1.9
source: trie/parse/go.py
file_fingerprint: d0f7dc6a234a525c3c095eefe9a8662ceb2ea587551aad14d2652f19daae7b66
last_synced_at: '2026-07-29T00:06:25Z'
description: "Go language backend \u2014 tree-sitter symbols + references, paired\
  \ with gopls."
defines:
- kind: module
  qualified_name: trie/parse/go:__module__
  lines: 1-366
- kind: constant
  qualified_name: trie/parse/go:GO_LANGUAGE
  lines: 31-31
- kind: function
  qualified_name: trie/parse/go:_make_parser
  lines: 34-37
- kind: function
  qualified_name: trie/parse/go:_node_text
  lines: 40-41
- kind: function
  qualified_name: trie/parse/go:_hash
  lines: 44-45
- kind: function
  qualified_name: trie/parse/go:_module_key
  lines: 48-50
- kind: function
  qualified_name: trie/parse/go:_signature_text
  lines: 53-57
- kind: function
  qualified_name: trie/parse/go:_is_public_go
  lines: 60-62
- kind: function
  qualified_name: trie/parse/go:_receiver_type
  lines: 65-74
- kind: function
  qualified_name: trie/parse/go:_rightmost_type_identifier
  lines: 77-84
- kind: function
  qualified_name: trie/parse/go:_make_symbol
  lines: 87-116
- kind: function
  qualified_name: trie/parse/go:extract_symbols
  lines: 119-209
- kind: function
  qualified_name: trie/parse/go:_find_node_for_symbol
  lines: 212-233
- kind: function
  qualified_name: trie/parse/go:_collect_call_names
  lines: 236-256
- kind: function
  qualified_name: trie/parse/go:extract_file_data
  lines: 259-292
- kind: constant
  qualified_name: trie/parse/go:GO_SYSTEM_PROMPT
  lines: 295-304
- kind: class
  qualified_name: trie/parse/go:GoBackend
  lines: 307-362
- kind: method
  qualified_name: trie/parse/go:GoBackend.__init__
  lines: 313-315
- kind: method
  qualified_name: trie/parse/go:GoBackend.extract_file_data
  lines: 317-338
- kind: method
  qualified_name: trie/parse/go:GoBackend.extract_symbols
  lines: 340-341
- kind: method
  qualified_name: trie/parse/go:GoBackend.source_suffix
  lines: 343-344
- kind: method
  qualified_name: trie/parse/go:GoBackend.system_prompt
  lines: 346-347
- kind: method
  qualified_name: trie/parse/go:GoBackend.resolver
  lines: 349-362
- kind: constant
  qualified_name: trie/parse/go:__all__
  lines: 365-365
incoming_refs: 0
outgoing_refs: 6
---
<!-- trie:section symbol=trie/parse/go:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=500e3e3db544d7136405b64a481dbfa9afa72818cbbfb3eb99daf75eb1cff5b0 source_ref=31fdce4c3c1c3404aed37f51a74792db9e712a33 role=parsing -->
Go language backend module providing tree-sitter-based symbol extraction and reference resolution, paired with gopls for method dispatch.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/go:GO_LANGUAGE fingerprint=c457bd466d6b15171bdeac093d9cc60637d728221a25ed6488577e8ea1a8a390 body_fp=4101e4cb875e61643197507ac4f5b7b38fb6c5e437f7af2561b6604655d3f059 source_ref=31fdce4c3c1c3404aed37f51a74792db9e712a33 role=config -->
Module-level `tree_sitter.Language` instance initialised from the `tree_sitter_go` grammar, shared by all parsers in this module.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/go:_make_parser fingerprint=4b7ecc412cec85f6a71881fe94705aba761469dd6cd0ccc05169ae3bbf0812f6 body_fp=bf52c61340ca88f8e3806a0162d93dd9210c58c2a1b4d0badab824ad6001f382 source_ref=31fdce4c3c1c3404aed37f51a74792db9e712a33 role=util -->
Create and return a `Parser` instance configured with `GO_LANGUAGE`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/go:_node_text fingerprint=90272da3050ae7f74f98b5fb62c5860239cd69d3c98b9843ee7816f84677e986 body_fp=e1aa0084372deb5bf041decb2046079b58cba73c5f77d1410b9f438012b604f2 source_ref=31fdce4c3c1c3404aed37f51a74792db9e712a33 role=util -->
Decode the byte slice of `source` spanned by `node` into a UTF-8 string.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/go:_hash fingerprint=7057d302a510678c4e042810b0eb270cc10d5047cb0a03fac868582b067b5767 body_fp=4d6c535ddd567d3e1fea8feeb45a70dc232492d2f3105352d59a2cda51262480 source_ref=31fdce4c3c1c3404aed37f51a74792db9e712a33 role=util -->
Return the SHA-256 hex digest of a UTF-8-encoded string.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/go:_module_key fingerprint=af6ee1ee42882ba9ba4e716ba32e14d2b07819ce55d6304c1c80c90e619356e9 body_fp=edc764103e8be8e487b50e836320d0f5b1d4b34636b2825eafbc95de3513805b source_ref=31fdce4c3c1c3404aed37f51a74792db9e712a33 role=util -->
Compute the module key for a file by returning its path relative to `source_root`, with the file extension stripped.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/go:_signature_text fingerprint=caeebf96a4fca6581c08bcac31d81ca582afda6da9480f204a783b2505fcc244 body_fp=aaff204f040129dc317697cbff4c6e9d32355aae53569ceb2caef5397d11e473 source_ref=31fdce4c3c1c3404aed37f51a74792db9e712a33 role=parsing -->
Extract the declaration header of a tree-sitter node as a string, stopping before the body block.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/go:_is_public_go fingerprint=2b77a07b537f87a530a80b5b35e6b9893926e31046c8c1dbefc65b7bf6834d69 body_fp=d0a232d788111a8bc8f7c68ebba4ff562b811ccbb5543977762b7f744b407c24 source_ref=31fdce4c3c1c3404aed37f51a74792db9e712a33 role=util -->
Return `True` if `name` is a Go-exported identifier (non-empty and starts with an uppercase letter).
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/go:_receiver_type fingerprint=73bca43e3ecdb61fc22159bd22dd675636e295deef5a6ba5b7339b910d48101e body_fp=065cb41ebd75e0c725ffe24bca43c9de45a689b67757ffade966dc894f2e928e source_ref=31fdce4c3c1c3404aed37f51a74792db9e712a33 role=parsing -->
Extract the receiver type name from a `method_declaration` node, handling both pointer and value receivers.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/go:_rightmost_type_identifier fingerprint=c8583d2162ecc1ff89b64518a4bf277b705562ed1997c2948ac144af49e48a0c body_fp=fd596eb5f69fbc3906c0d7396c552809a0204243b6e6cefd65f4016826e8a0a0 source_ref=31fdce4c3c1c3404aed37f51a74792db9e712a33 role=parsing -->
Recursively searches a tree-sitter node's named children in reverse to return the rightmost `type_identifier` text, or `None` if absent.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/go:_make_symbol fingerprint=cafbdc588af8bdfbab920659d15982b57335a4f033437ff3f885e19fd8834a7d body_fp=de4983c4089f8eefda3545ed476ee5b9a2828f845e9ad61b921c6e2dd939719d source_ref=31fdce4c3c1c3404aed37f51a74792db9e712a33 role=parsing -->
Construct a `Symbol` from a tree-sitter `Node`, computing its qualified name, signature, body text, hashes, and visibility.

- `parent`: receiver type name for methods; `None` for top-level declarations.
- `is_public`: `True` only when both `name` and `parent` (if present) are Go-exported (uppercase-initial).
- `docstring`: always `None` (not extracted in v1).
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/go:extract_symbols fingerprint=3ff72c6d3fda81903690a43c5a0850294968df5a04bc40217fdbe6d74824ec6f body_fp=54a23c939b6999a7308052e8282de95ea23d67bc8fa8dee5e0cda405025c902f source_ref=31fdce4c3c1c3404aed37f51a74792db9e712a33 role=parsing -->
Parse a Go source file with tree-sitter and return `Symbol` objects for all top-level functions, methods, types, interfaces, constants, and variables.

- `source_text`: if provided, parsed directly instead of reading `file_path` from disk.
- `source_root`: defaults to `file_path.parent`; used to compute relative paths and `module_key`.
- Struct type declarations emit kind `"class"`; interface declarations emit `"interface"`; other type specs emit `"type"`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/go:_find_node_for_symbol fingerprint=0224069ed8592575a6194c18c1854a946e31f220c4654521c0eb37e1dd2ff14b body_fp=261add195b7eeaed8c1e91bbd69a123a130d90a269fc64a1bce21ee167758d73 source_ref=31fdce4c3c1c3404aed37f51a74792db9e712a33 role=util -->
Walk `root` depth-first and return the first declaration node whose start line matches `sym.start_line`, or `None` if not found.

- Matches node types: `function_declaration`, `method_declaration`, `type_spec`, `const_spec`, `var_spec`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/go:_collect_call_names fingerprint=97519eb37edbaedbec2943ebc7225eeda41913fd228e59bb5b9055bff53a9f96 body_fp=59cbad23b7ddacb2316eef15a6210f428633df82ee21cf2f02a6666e7d6fb1ac source_ref=31fdce4c3c1c3404aed37f51a74792db9e712a33 role=parsing -->
Walk a tree-sitter `Node` recursively and collect all called identifier names, extracting the bare name for direct calls and the field name for selector calls.

- Skips comments and string literals to avoid false positives.
- Returns only the callee name, not the receiver; `x.M()` yields `"M"`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/go:extract_file_data fingerprint=171d78ac5a79640148c191eb968fe9df360d6dd3d297ee75a88326fd639035af body_fp=c2726043d8fc9755b75c2fa5375564130c550f067c165898272dff89614b52f9 source_ref=31fdce4c3c1c3404aed37f51a74792db9e712a33 role=parsing -->
Parse a Go file and return all extracted symbols plus deduplicated `"calls"` reference edges to top-level symbols within the same file.

- `source_root`: defaults to the file's parent directory if omitted.
- References are tree-sitter-only; method-dispatch edges require the `GoBackend` + gopls path.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/go:GO_SYSTEM_PROMPT fingerprint=49ab3ffb3bfa6358f80f6d58370c2bdb7808b3d4ae2ab8487f3a1d9c08f355a8 body_fp=7e821d7ba143342811ebbb6a3b1282489e8a684d65edf4b8103dbca8cf4bf968 source_ref=31fdce4c3c1c3404aed37f51a74792db9e712a33 role=config -->
System prompt string injected into LLM documentation requests for Go symbols, guiding per-kind (func/method/type) description style.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/go:GoBackend fingerprint=82c2bf8ac4bba16089fd8eb49f3a2cd87b4f014e2e18aff79a6c35ee0fae0895 body_fp=874635253862604199e751d66062e9fb6872557b657b5d2cb1efa57b56f1b434 source_ref=31fdce4c3c1c3404aed37f51a74792db9e712a33 role=domain -->
`LanguageBackend` implementation for Go that combines tree-sitter structural extraction with a lazily-initialised gopls `LspResolver` for method-dispatch edges.

- `extract_file_data`: raises `NotImplementedError` if `source_text` is passed; merges gopls references into tree-sitter results when a resolver is available.
- `resolver()`: builds the `LspResolver` once on first call; skips it if `TRIE_DISABLE_RESOLVER=1`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/go:GoBackend.__init__ fingerprint=b84739b0fbbdbeb6b33571852fef53390cb973b63bb786a1526af79058a93652 body_fp=bd2a0f4ae58d9d89773b76c0ed27314522977ef402f3349afb0efedebd4e47bb source_ref=31fdce4c3c1c3404aed37f51a74792db9e712a33 role=domain -->
Initialises `GoBackend` with `_resolver` set to `None` and `_resolver_built` flag set to `False`, deferring gopls resolver construction to first use.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/go:GoBackend.extract_file_data fingerprint=b20e0b87585336f45b65241da08a639004c8728e185ae83f13add911ee485f41 body_fp=a3c2acbdca455b5637c6e73215982ba111abf4dccd01a3a6c2ab4a412f12e1a7 source_ref=31fdce4c3c1c3404aed37f51a74792db9e712a33 role=orchestration -->
Extract symbols and references for a Go file via `GoBackend`, merging tree-sitter edges with gopls-resolved references when a resolver is available.

- `source_text`: not supported; raises `NotImplementedError` if supplied.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/go:GoBackend.extract_symbols fingerprint=af266339106949531c076cf2e82cb2565f65b39795b7b77394086774fac189f3 body_fp=fb055c468856f614be59846e3ff7ee5b0cb50e747ea13a9b4999d50c110b854b source_ref=31fdce4c3c1c3404aed37f51a74792db9e712a33 role=api -->
Delegates `GoBackend` symbol extraction to the module-level `extract_symbols` function.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/go:GoBackend.source_suffix fingerprint=dfe93906f787f83d8e88cf2dea2d3cf0489911aa06d7e7a33de8e3a97407b3c4 body_fp=1414ecc894ffa64bebbca5439d492e78a68d5f050c17ec2faa9fc9567b8701ec source_ref=31fdce4c3c1c3404aed37f51a74792db9e712a33 role=util -->
Returns the file extension `".go"` for `GoBackend`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/go:GoBackend.system_prompt fingerprint=1d09be814896835261426d67e0ebd501e7d4034111a09a2f2f7e6662ba58f979 body_fp=5cd3d72c6353d25215d0b22ee2fd4a802acb1b9e9b115e93759f9989788d877a source_ref=31fdce4c3c1c3404aed37f51a74792db9e712a33 role=api -->
Returns the `GO_SYSTEM_PROMPT` constant string used to guide LLM documentation of Go symbols.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/go:GoBackend.resolver fingerprint=b32248646eae7c251de744d08c0cf5961e5ac5931e8fb6f59498b6f75de029bf body_fp=0b64e5487ed2453029a0b98208ce37c21f441e92ddd12a441ab8b2860da636a4 source_ref=31fdce4c3c1c3404aed37f51a74792db9e712a33 role=domain -->
Lazily initialises and returns `GoBackend`'s `LspResolver`, or `None` if `TRIE_DISABLE_RESOLVER=1` or `go_spec()` returns `None`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/go:__all__ fingerprint=13506e3717e93887edd000b3513b65d67ce9aae0d0eb8e3863dca495f28e22c1 body_fp=5f65e08b19929c3cb3c5cbdb0147ab400e3cef11c9c872dbc297d930a5635523 source_ref=31fdce4c3c1c3404aed37f51a74792db9e712a33 role=config -->
Declares the public API of `trie/parse/go`, exporting `GO_SYSTEM_PROMPT`, `GoBackend`, `extract_file_data`, and `extract_symbols`.
<!-- trie:end -->