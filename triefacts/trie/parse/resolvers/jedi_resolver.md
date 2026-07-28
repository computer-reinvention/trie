---
trie_version: 0.1.9
source: trie/parse/resolvers/jedi_resolver.py
file_fingerprint: 788c53e7dd963f7d982e5c7024cd3c0bc6e08277d0173b8be0597121c8ee31b6
last_synced_at: '2026-07-28T23:14:45Z'
description: "Jedi-backed reference resolver for Python \u2014 tree-sitter's type-aware\
  \ pair."
defines:
- kind: module
  qualified_name: trie/parse/resolvers/jedi_resolver:__module__
  lines: 1-188
- kind: class
  qualified_name: trie/parse/resolvers/jedi_resolver:JediResolver
  lines: 27-122
- kind: method
  qualified_name: trie/parse/resolvers/jedi_resolver:JediResolver.__init__
  lines: 32-37
- kind: method
  qualified_name: trie/parse/resolvers/jedi_resolver:JediResolver._jedi
  lines: 39-42
- kind: method
  qualified_name: trie/parse/resolvers/jedi_resolver:JediResolver._get_project
  lines: 44-52
- kind: method
  qualified_name: trie/parse/resolvers/jedi_resolver:JediResolver.resolve_file
  lines: 54-64
- kind: method
  qualified_name: trie/parse/resolvers/jedi_resolver:JediResolver._resolve_file_inner
  lines: 66-122
- kind: function
  qualified_name: trie/parse/resolvers/jedi_resolver:_symbols_by_line
  lines: 125-136
- kind: function
  qualified_name: trie/parse/resolvers/jedi_resolver:_file_symbols_by_line
  lines: 139-154
- kind: function
  qualified_name: trie/parse/resolvers/jedi_resolver:_attribute_call_sites
  lines: 157-184
- kind: constant
  qualified_name: trie/parse/resolvers/jedi_resolver:__all__
  lines: 187-187
incoming_refs: 4
outgoing_refs: 6
---
<!-- trie:section symbol=trie/parse/resolvers/jedi_resolver:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=a9138cc118ac085045812f68fa105ea87142227ae32cb5fa04514ca9b68265fe source_ref=04d02104e5fd9e682091df4006ee1556bd8de757 role=parsing -->
Provides jedi-backed `ReferenceResolver` for Python, emitting `calls` edges from attribute call sites to in-project definition symbols.

- Errors on any single file yield `[]`, never propagate exceptions.
- Jedi is imported lazily; missing dependency degrades to no resolver.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolvers/jedi_resolver:JediResolver fingerprint=7f998d7a467eb89cc6d3a24a89dab9569cb6e8da4df1fdac6548b329faadd5e3 body_fp=70732b77b3c899d795cf637a39b11d786119a341d6e3a12867b80664b0074b0f source_ref=04d02104e5fd9e682091df4006ee1556bd8de757 role=domain -->
Resolve intra-project `calls` edges for a Python file by using jedi `goto` to trace every `<expr>.<attr>(...)` call to its definition symbol.

- `name`: resolver identifier, always `"jedi"`.
- `_project`: lazily constructed `jedi.Project`; recreated when `source_root` changes.
- `resolve_file`: returns `[]` on any error; never raises.
- `resolve_file` → `symbols`: pre-extracted symbols for the file being analysed.
- Returns deduplicated `Reference(kind="calls")` list; skips stdlib/third-party targets.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolvers/jedi_resolver:JediResolver.__init__ fingerprint=7b42641efc732ba4a9ebf352c350b033391917cc213c33c6f34e360c0a78a3b6 body_fp=ba0cc5c0ad3c5a6dec4ad22b7e3c12d015c4daf33e703c1f871d830aa4b37f8f source_ref=04d02104e5fd9e682091df4006ee1556bd8de757 role=domain -->
Initialize `JediResolver` with a tree-sitter parser and deferred jedi `Project` state.

- `_parser`: tree-sitter parser instance from `_make_parser`
- `_project`: lazily populated `jedi.Project`; `None` until first `resolve_file` call
- `_project_root`: tracks which source root the cached project was built for
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolvers/jedi_resolver:JediResolver._jedi fingerprint=168154823544dce14baeb9cf4fbb4cb400d32e18c15a22c7383de16fd2e3f034 body_fp=0f71182ea00d11891edc0bbe1ee5ea444d88076b0f6999cfe2326b4f52c0d447 source_ref=04d02104e5fd9e682091df4006ee1556bd8de757 role=util -->
Lazily import and return the `jedi` module, deferring the hard dependency until first use.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolvers/jedi_resolver:JediResolver._get_project fingerprint=9bdfa5ff3d5d830c27c455c0f8836a5d490b62c71162416ac6c74b44aa4c3fcd body_fp=eed7c223aa9bddb5906f86c41bef2c087209e54dc631cd7428c6f5885ac6361c source_ref=04d02104e5fd9e682091df4006ee1556bd8de757 role=domain -->
Return a cached `jedi.Project` for `source_root`, rebuilding it when the root changes.

- `source_root`: project source root; jedi project is rooted at its **parent** so top-level packages are importable.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolvers/jedi_resolver:JediResolver.resolve_file fingerprint=a293b41bb7d3465f3a21cdd0b525a2f3b58dcea60a324b23031771df6752559d body_fp=a1a97621ec88d674bdfb00fae13fc1fa2b535706c13ba276f02548c4530c3494 source_ref=04d02104e5fd9e682091df4006ee1556bd8de757 role=api -->
Invoke `JediResolver` reference resolution for a single file, returning `[]` on any exception instead of propagating it.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolvers/jedi_resolver:JediResolver._resolve_file_inner fingerprint=f8a465c9abbae6fbe904b85cb99ca550ce8caf482ec782a81aa14c22e5073a2c body_fp=7893a336f04940f75237962837d940b0c132e7189a32c1ad21b7acd71125a499 source_ref=04d02104e5fd9e682091df4006ee1556bd8de757 role=domain -->
Implements `JediResolver.resolve_file`'s core logic: parses `file_path`, walks attribute call sites, and uses jedi `goto` to emit `calls` `Reference` objects for in-project targets.

- `symbols`: pre-extracted symbols for `file_path`, used to map call-site lines to enclosing qnames.
- Returns deduplicated `Reference` list; skips stdlib/third-party and self-edges.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolvers/jedi_resolver:_symbols_by_line fingerprint=9784354d5e32a006e03a83ab1ac7adddd63dfec826a5d67cabc39b72851a6b10 body_fp=d6fc9f756d3ab8129b0682fbe2752ee43b545a872f9df006308f723597603182 source_ref=04d02104e5fd9e682091df4006ee1556bd8de757 role=util -->
Map each source line number to the `qualified_name` of the innermost `function`, `method`, or `class` symbol covering it.

- Wider symbols are written first; narrower symbols overwrite, ensuring innermost wins.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolvers/jedi_resolver:_file_symbols_by_line fingerprint=3afd8cb014a1372e51bdb8a1ab801402ba3323f055ad056ae0c757861e35e86e body_fp=417aff9448eb308358e83169dc37338e43a519a9a51adc2dfbd5f6d178781c6a source_ref=04d02104e5fd9e682091df4006ee1556bd8de757 role=parsing -->
Parse a target file and return a mapping from each symbol's start line to its qualified name.

- Returns `{}` on any parse error, keeping the caller's scan intact.
- Keyed by `start_line` because jedi's `goto` reports the `def`/`class` line.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolvers/jedi_resolver:_attribute_call_sites fingerprint=6edbabd97eb986a551c66aafc5b992b9455c7e90ec23eed6cf56173c9f351a9b body_fp=32c708c49b2d7d6788e6047e9de659c6cb63f1d629e874d86c277bd63f6f7377 source_ref=04d02104e5fd9e682091df4006ee1556bd8de757 role=parsing -->
Walk a tree-sitter AST and yield `(line, col, attr_name)` for every `<expr>.<attr>(...)` call site.

- `line`: 1-indexed line of the attribute identifier node.
- `col`: 0-indexed column of the attribute identifier node.
- Skips `comment` and `string` nodes during traversal.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolvers/jedi_resolver:__all__ fingerprint=af42d2ff24eb6562b28a1fc3c2e78534c7b5c7e858a9389d40bbcecb3b5d5347 body_fp=2e9e05b57021eac74fa9ac4296ffda484cfa3f85bfa07fad65942804e8fab4be source_ref=04d02104e5fd9e682091df4006ee1556bd8de757 role=util -->
Declares `JediResolver` as the sole public export of this module.
<!-- trie:end -->