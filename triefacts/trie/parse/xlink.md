---
trie_version: 0.3.0
source: trie/parse/xlink.py
file_fingerprint: bb3e3143db3877d2760168722a62ee330febf1a1df1234c1537b51e13dcdb97e
last_synced_at: '2026-08-30T02:41:02Z'
description: "Cross-language edge detection: API call sites \u2194 route handlers."
defines:
- kind: module
  qualified_name: trie/parse/xlink:__module__
  lines: 1-927
- kind: constant
  qualified_name: trie/parse/xlink:logger
  lines: 39-39
- kind: constant
  qualified_name: trie/parse/xlink:_PY_LANGUAGE
  lines: 45-45
- kind: constant
  qualified_name: trie/parse/xlink:_TS_LANGUAGE
  lines: 46-46
- kind: constant
  qualified_name: trie/parse/xlink:_TSX_LANGUAGE
  lines: 47-47
- kind: constant
  qualified_name: trie/parse/xlink:_HTTP_METHODS
  lines: 50-50
- kind: constant
  qualified_name: trie/parse/xlink:_PARAM_WILDCARD
  lines: 53-53
- kind: class
  qualified_name: trie/parse/xlink:XLinkCallSite
  lines: 62-69
  signature: class XLinkCallSite
- kind: class
  qualified_name: trie/parse/xlink:XLinkEndpoint
  lines: 73-80
  signature: class XLinkEndpoint
- kind: function
  qualified_name: trie/parse/xlink:_make_ts_parser
  lines: 88-97
  signature: 'def _make_ts_parser(file_path: Path) -> Parser'
- kind: function
  qualified_name: trie/parse/xlink:_make_py_parser
  lines: 100-103
  signature: def _make_py_parser() -> Parser
- kind: function
  qualified_name: trie/parse/xlink:_node_text
  lines: 106-107
  signature: 'def _node_text(node: Node, source: bytes) -> str'
- kind: function
  qualified_name: trie/parse/xlink:_module_key_ts
  lines: 110-117
  signature: 'def _module_key_ts(file_path: Path, source_root: Path) -> str'
- kind: function
  qualified_name: trie/parse/xlink:_module_key_py
  lines: 120-123
  signature: 'def _module_key_py(file_path: Path, source_root: Path) -> str'
- kind: function
  qualified_name: trie/parse/xlink:_find_enclosing_symbol
  lines: 126-144
  signature: 'def _find_enclosing_symbol( line: int, symbols: list[tuple[str, int, int]], ) -> str | None'
- kind: function
  qualified_name: trie/parse/xlink:_string_value_from_node
  lines: 147-180
  signature: 'def _string_value_from_node(node: Node, source: bytes) -> str | None'
- kind: function
  qualified_name: trie/parse/xlink:_extract_string_arg
  lines: 183-195
  signature: 'def _extract_string_arg(node: Node, source: bytes) -> str | None'
- kind: function
  qualified_name: trie/parse/xlink:_get_arguments_node
  lines: 203-205
  signature: 'def _get_arguments_node(call_node: Node) -> Node | None'
- kind: function
  qualified_name: trie/parse/xlink:_extract_method_from_options
  lines: 208-235
  signature: 'def _extract_method_from_options(args_node: Node, source: bytes) -> str'
- kind: function
  qualified_name: trie/parse/xlink:extract_fetch_sites
  lines: 238-278
  signature: 'def extract_fetch_sites( tree: Node, source: bytes, file_symbols: list[tuple[str, int, int]], ) -> list[XLinkCallSite]'
- kind: function
  qualified_name: trie/parse/xlink:extract_axios_sites
  lines: 281-368
  signature: 'def extract_axios_sites( tree: Node, source: bytes, file_symbols: list[tuple[str, int, int]], ) -> list[XLinkCallSite]'
- kind: function
  qualified_name: trie/parse/xlink:_extract_decorator_route_info
  lines: 376-445
  signature: 'def _extract_decorator_route_info( decorator_node: Node, source: bytes, ) -> tuple[str, str] | None'
- kind: function
  qualified_name: trie/parse/xlink:_py_string_value
  lines: 448-461
  signature: 'def _py_string_value(string_node: Node, source: bytes) -> str | None'
- kind: function
  qualified_name: trie/parse/xlink:_extract_methods_kwarg
  lines: 464-479
  signature: 'def _extract_methods_kwarg(args_node: Node, source: bytes) -> list[str]'
- kind: function
  qualified_name: trie/parse/xlink:_extract_decorator_route_info_multi
  lines: 482-525
  signature: 'def _extract_decorator_route_info_multi( decorator_node: Node, source: bytes, ) -> list[tuple[str, str]]'
- kind: function
  qualified_name: trie/parse/xlink:extract_fastapi_endpoints
  lines: 528-537
  signature: 'def extract_fastapi_endpoints( tree: Node, source: bytes, file_symbols: list[tuple[str, int, int]], ) -> list[XLinkEndpoint]'
- kind: function
  qualified_name: trie/parse/xlink:extract_flask_endpoints
  lines: 540-550
  signature: 'def extract_flask_endpoints( tree: Node, source: bytes, file_symbols: list[tuple[str, int, int]], ) -> list[XLinkEndpoint]'
- kind: function
  qualified_name: trie/parse/xlink:_extract_py_decorator_endpoints
  lines: 553-590
  signature: 'def _extract_py_decorator_endpoints( tree: Node, source: bytes, file_symbols: list[tuple[str, int, int]], framework: str, ) -> list[XLinkEndpoint]'
- kind: function
  qualified_name: trie/parse/xlink:extract_express_endpoints
  lines: 593-646
  signature: 'def extract_express_endpoints( tree: Node, source: bytes, file_symbols: list[tuple[str, int, int]], ) -> list[XLinkEndpoint]'
- kind: function
  qualified_name: trie/parse/xlink:_looks_like_express_receiver
  lines: 649-658
  signature: 'def _looks_like_express_receiver(name: str) -> bool'
- kind: function
  qualified_name: trie/parse/xlink:extract_ts_call_sites
  lines: 666-679
  signature: 'def extract_ts_call_sites( file_path: Path, source_root: Path, file_symbols: list[tuple[str, int, int]], ) -> list[XLinkCallSite]'
- kind: function
  qualified_name: trie/parse/xlink:extract_ts_endpoints
  lines: 682-692
  signature: 'def extract_ts_endpoints( file_path: Path, source_root: Path, file_symbols: list[tuple[str, int, int]], ) -> list[XLinkEndpoint]'
- kind: function
  qualified_name: trie/parse/xlink:extract_py_endpoints
  lines: 695-708
  signature: 'def extract_py_endpoints( file_path: Path, source_root: Path, file_symbols: list[tuple[str, int, int]], ) -> list[XLinkEndpoint]'
- kind: function
  qualified_name: trie/parse/xlink:normalize_url
  lines: 716-745
  signature: 'def normalize_url(pattern: str) -> list[str]'
- kind: function
  qualified_name: trie/parse/xlink:_match_confidence
  lines: 748-778
  signature: 'def _match_confidence( site_segments: list[str], endpoint_segments: list[str], site_method: str, endpoint_method: str, ) -> float'
- kind: function
  qualified_name: trie/parse/xlink:match_xlinks
  lines: 781-830
  signature: 'def match_xlinks( sites: list[XLinkCallSite], endpoints: list[XLinkEndpoint], threshold: float, ) -> list[Reference]'
- kind: function
  qualified_name: trie/parse/xlink:xlink_resolve
  lines: 838-912
  signature: 'def xlink_resolve( *, store: Store, config: Config, source_root: Path, discovered_files: dict[str, Path], ) -> dict[str, list[Reference]]'
- kind: function
  qualified_name: trie/parse/xlink:_find_file_for_module
  lines: 915-926
  signature: 'def _find_file_for_module(module: str, discovered_files: dict[str, Path]) -> str | None'
incoming_refs: 0
outgoing_refs: 0
---
<!-- trie:section symbol=trie/parse/xlink:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=ef2447802b976363927fd68344d66d27eea0b5fc502a963d9de820f582db4f9c source_ref=6cc1924f0bfbef1953b86a5430f9a51bc9a1446b role=orchestration -->
Post-scan pass that detects HTTP API boundaries between languages and emits `Reference(kind="cross_language_call")` edges into the existing graph infrastructure.

Implements a three-phase pipeline:

- **Phase A (extraction):** Per-file tree-sitter AST walks extract `XLinkCallSite` records from TS/JS (`fetch`, `axios`) and `XLinkEndpoint` records from TS/JS (Express) and Python (FastAPI, Flask).
- **Phase B (matching):** Cross-file join of call sites to endpoints by normalised URL pattern and HTTP method; confidence threshold filters weak matches.
- **Phase C (insertion):** Returns grouped `Reference` objects for merging into `pending_refs` before `replace_all_edges` in `scan_project()`.

Entry point is `xlink_resolve()`; all other public symbols are extractors, normalisers, or matchers composable independently.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/xlink:logger fingerprint=5dd7c99cc7b62847d3ce6d10b09dbc7384f5f787c39dad9506343ade58408092 body_fp=5a9784722211d30bff11d6c009e775c42771bbc3c78e48a8e7bd043c0ee9d555 source_ref=6cc1924f0bfbef1953b86a5430f9a51bc9a1446b role=config -->
Module-level logger for `trie.parse.xlink`, used to emit debug messages for below-threshold xlink matches.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/xlink:_PY_LANGUAGE fingerprint=bd37d28eb9ac8c5e3d1bdde2edb3a316aa57cca1ff4896281f4aab47b471d37b body_fp=dc04bad72b7e2ab2df6b8223fecf2f6b9b4f56b53e6cf3cef61e2ec9ce27ab87 source_ref=6cc1924f0bfbef1953b86a5430f9a51bc9a1446b role=config -->
Module-level `Language` instance wrapping the tree-sitter Python grammar, shared by all Python parsers in this module.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/xlink:_TS_LANGUAGE fingerprint=43d38bc4b3f214368738a176eead748f9e87dbb3dd0e7bcb7c5eaa1644aea5cb body_fp=d6fe574f55d696af96896fe3f2c1d8af494a0642f916c10d5c41c2dc00508b1d source_ref=6cc1924f0bfbef1953b86a5430f9a51bc9a1446b role=config -->
Module-level constant holding the tree-sitter `Language` object for TypeScript, used by all TypeScript/JS parsers in this module.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/xlink:_TSX_LANGUAGE fingerprint=c5ad589203599457aa04a1169938d8c363698f6f5911beb7d29dfcaf5f5f83ff body_fp=5b5a2f0ec6b87e94e0e0b88ef2dadc410688b2fafd04aa17ff37fd25a25fd4a0 source_ref=6cc1924f0bfbef1953b86a5430f9a51bc9a1446b role=config -->
Module-level `Language` instance wrapping the tree-sitter TSX grammar, used by `_make_ts_parser` for `.tsx` and `.jsx` files.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/xlink:_HTTP_METHODS fingerprint=af32b4396fb42751052f845d45a6e0c9794b3e7b3a363e080529adb76b49476a body_fp=93ff90f2cd407cd0fb8d71368b8c086909673d718be55f19b10b1480a798059b source_ref=6cc1924f0bfbef1953b86a5430f9a51bc9a1446b role=config -->
Frozenset of uppercase HTTP method strings recognised by the xlink matcher and extractor heuristics.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/xlink:_PARAM_WILDCARD fingerprint=6e0934be923999b3d9de3a2cdd0c739fa7fa38f94c060a6d1335370207b8af17 body_fp=5b09113a37acb871a23940ffd995217d85a53380c459da938efceea47fc43c2d source_ref=6cc1924f0bfbef1953b86a5430f9a51bc9a1446b role=config -->
Sentinel string substituted for any path parameter segment during URL normalisation and template-literal interpolation.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/xlink:XLinkCallSite fingerprint=c2f804f5a713f71c6d5732bb04a157a83f39a7ea897d6afe4e25f64766f9bd61 body_fp=1399fd07fe477d359e53b63ff2b7d5d0ab22d2abec60c87be22c8e1dfaa42270 source_ref=6cc1924f0bfbef1953b86a5430f9a51bc9a1446b role=model -->
## `class XLinkCallSite`

Immutable record of a single HTTP call site found in a TS/JS source file.

- `method`: uppercase HTTP verb, or `"*"` when the method cannot be statically determined
- `pattern`: URL with path parameters replaced by `{_PARAM_}` wildcards
- `framework`: one of `"fetch"` or `"axios"`
- `line`: 1-based line number of the call expression
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/xlink:XLinkEndpoint fingerprint=a1ba00f9790a7f669cd8035e213e44bfa028e9a09910834591e97b416c09aeaf body_fp=9952c6c71dc5cf48660d8d28bd4b874a157864d0ba5ffb8e8c61836a617a4cd9 source_ref=6cc1924f0bfbef1953b86a5430f9a51bc9a1446b role=model -->
## `class XLinkEndpoint`

Frozen dataclass representing a server-side HTTP route handler detected during the extraction phase.

- `method`: HTTP verb in uppercase, or `"*"` for any-method routes (e.g. Express `app.use`)
- `pattern`: normalised URL pattern as extracted from the decorator/call; may contain framework-specific parameter syntax before normalisation
- `framework`: one of `"fastapi"`, `"flask"`, or `"express"`
- `line`: 1-based line number of the handler function definition
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/xlink:_make_ts_parser fingerprint=d09f8269a8bb5d6d8ecaef0f905d2124fe22ef038220df3ed9ecc6a294bdebe4 body_fp=bc974e43cd34beb1fe222e37bee892bbde084b3e8515cbe8c1115337e8c5549f source_ref=6cc1924f0bfbef1953b86a5430f9a51bc9a1446b role=util -->
## `def _make_ts_parser(file_path: Path) -> Parser`

Create and return a tree-sitter `Parser` configured for the given TS/JS file's dialect.

- `file_path`: selects TSX grammar for `.tsx`/`.jsx` extensions, TS grammar for all others.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/xlink:_make_py_parser fingerprint=1f7cb810ace32c9db1778e91f339ce72a2e725766d7ff8f5f2bc0bfbe66d0a1a body_fp=1799bb33a25612e1858feddf7e69aae75d18ac9c3e1492d48ad1f57b903de0c3 source_ref=6cc1924f0bfbef1953b86a5430f9a51bc9a1446b role=util -->
## `def _make_py_parser() -> Parser`

Create and return a tree-sitter `Parser` configured with the Python grammar.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/xlink:_node_text fingerprint=90272da3050ae7f74f98b5fb62c5860239cd69d3c98b9843ee7816f84677e986 body_fp=c1ec3caa5d5b59baea4d2654764ae95152f0cee0a83554a175804adf2326ffda source_ref=6cc1924f0bfbef1953b86a5430f9a51bc9a1446b role=util -->
## `def _node_text(node: Node, source: bytes) -> str`

Decode the byte span of a tree-sitter `Node` from `source` into a UTF-8 string, replacing invalid bytes.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/xlink:_module_key_ts fingerprint=4d3d1f5e254c8fc3e42d2da39bbc8ef8cb444097e5ce9d8a065cb22e198f4aa8 body_fp=dcc97fabc1af1022d34d19fa15909f8f2af53715e189921c35de727dc9e021f6 source_ref=6cc1924f0bfbef1953b86a5430f9a51bc9a1446b role=util -->
## `def _module_key_ts(file_path: Path, source_root: Path) -> str`

Compute the dot-free qname module prefix for a TS/JS file by stripping its extension from the path relative to `source_root`.

- Tries extensions in order: `.d.ts`, `.tsx`, `.ts`, `.jsx`, `.mjs`, `.cjs`, `.js`; falls back to `Path.with_suffix("")`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/xlink:_module_key_py fingerprint=3d5d3013e3269a295ce33d035eabbcb4877047b6d5e30946804c2085d62f6d1b body_fp=fea846c94ab1a8b8434dc6be6d79e74c24080cb8349fbcc933fbff63a45f8a22 source_ref=6cc1924f0bfbef1953b86a5430f9a51bc9a1446b role=util -->
## `def _module_key_py(file_path: Path, source_root: Path) -> str`

Compute the qualified-name module prefix for a Python file by stripping its extension relative to `source_root`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/xlink:_find_enclosing_symbol fingerprint=cfef3d1e83ba2b4e44e9952188f8c701c4261f4ef605cc29ffe2460308afc79d body_fp=543be7f40ca960056f6beb164b21f7a65aa81a20e08b83b8059952002cb1a63e source_ref=6cc1924f0bfbef1953b86a5430f9a51bc9a1446b role=util -->
## `def _find_enclosing_symbol( line: int, symbols: list[tuple[str, int, int]], ) -> str | None`

Return the qname of the tightest symbol whose line range contains `line`, or `None` if no symbol covers it.

- `symbols`: list of `(qname, start_line, end_line)` tuples as returned by `Store.symbols_in_file_with_lines`; need not be pre-filtered.
- Tightness is measured by smallest `end - start` span among all candidates that satisfy `start <= line <= end`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/xlink:_string_value_from_node fingerprint=7f43f9f96a5dce4f5e5b4b71508f5d5ead65b64f37122109c8e5a995e3f6f68a body_fp=5e0cd102dbde6ed1d7f59600b8136ac8d14dbb6fc0de278f080684120cb06167 source_ref=6cc1924f0bfbef1953b86a5430f9a51bc9a1446b role=parsing -->
## `def _string_value_from_node(node: Node, source: bytes) -> str | None`

Extract the string content from a tree-sitter `string` or `template_string` node, replacing `${...}` substitutions with `_PARAM_WILDCARD`.

- `node`: must be a `string`, `string_fragment`, or `template_string` node; returns `None` for any other type.
- `source`: raw file bytes used to slice node text.
- Returns the unquoted string content, or a wildcard-substituted reconstruction for template literals.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/xlink:_extract_string_arg fingerprint=3fdafc3eadb499287b5f01c08b4170aacb05390e3978a424c4955dd3b24b175d body_fp=34cf8146a951761e09c140ff1f52b1b6a20d54329c4e3f944dfc863913a6b074 source_ref=6cc1924f0bfbef1953b86a5430f9a51bc9a1446b role=parsing -->
## `def _extract_string_arg(node: Node, source: bytes) -> str | None`

Recursively extract a URL string from a call argument AST node, handling string literals, template literals, and parenthesised/wrapped expressions.

- Returns `None` if no string value can be found in the node or its descendants.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/xlink:_get_arguments_node fingerprint=8cc7bdd881f5241aeb7f89f878d4bd39738c55f6c1b6622738a81304f3b537c4 body_fp=d43320baab99644cd6328400189f53af8b243966b524eb2fccc9b1ee79c30d64 source_ref=6cc1924f0bfbef1953b86a5430f9a51bc9a1446b role=util -->
## `def _get_arguments_node(call_node: Node) -> Node | None`

Return the `arguments` child field of a tree-sitter call expression node, or `None` if absent.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/xlink:_extract_method_from_options fingerprint=5e72b884bd89fb933d52b147e13e3c6aefccaefa9a0e4f63b0e1087fe23da747 body_fp=262606b906fc0e3c810924ae27b0a49c1c6694376e320a72aa63a3d0b0941bf8 source_ref=6cc1924f0bfbef1953b86a5430f9a51bc9a1446b role=parsing -->
## `def _extract_method_from_options(args_node: Node, source: bytes) -> str`

Extract the HTTP method string from the second argument of a `fetch` call's arguments node.

- `args_node`: the `arguments` AST node of the `fetch(url, options)` call expression.
- Returns `"GET"` if fewer than two arguments exist, the second arg is not an object, no `method` key is found, or the value is not a recognised HTTP method.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/xlink:extract_fetch_sites fingerprint=efa689976384ef64ee8377ce1df00134b01a6efc572a09bada6a567e44f407bb body_fp=8ae6e0c8ad1225f138d1ba3991e4d6da8341628be4afeb50cb67eee6b00f464d source_ref=6cc1924f0bfbef1953b86a5430f9a51bc9a1446b role=parsing -->
## `def extract_fetch_sites( tree: Node, source: bytes, file_symbols: list[tuple[str, int, int]], ) -> list[XLinkCallSite]`

Walk a TS/JS AST and collect every `fetch(url)` and `fetch(url, {method: …})` call site as an `XLinkCallSite`.

- `tree` — root `Node` of the parsed TS/JS file.
- `file_symbols` — `(qname, start_line, end_line)` tuples used to attribute each call to its enclosing symbol; calls with no enclosing symbol are silently dropped.
- Handles `await fetch(…)` by unwrapping the `await_expression` before inspection.
- HTTP method defaults to `"GET"` when no options object is present; reads `{method: "POST"}` from the second argument otherwise.
- Returns only sites whose URL resolves to a static or template-literal string.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/xlink:extract_axios_sites fingerprint=52a289712ef25a0726a43973bbe25fc322e562d149e01ba2d9a4708570668ef6 body_fp=ab2f976da5c0a409a407db9da49e48f0c613046ee4a42f4d7aa92ccbc45eee60 source_ref=6cc1924f0bfbef1953b86a5430f9a51bc9a1446b role=parsing -->
## `def extract_axios_sites( tree: Node, source: bytes, file_symbols: list[tuple[str, int, int]], ) -> list[XLinkCallSite]`

Walk a TS/JS AST and collect all axios HTTP call sites into `XLinkCallSite` records.

- `tree`: root `Node` of the parsed TS/JS file.
- `source`: raw file bytes used for text extraction.
- `file_symbols`: `(qname, start_line, end_line)` tuples used to attribute each call to its enclosing symbol; calls with no enclosing symbol are silently dropped.
- Recognises both `axios.METHOD(url)` (method from property name) and `axios({url, method})` (method from config object; defaults to `"*"` if absent or unrecognised).
- Only HTTP methods in `_HTTP_METHODS` are accepted; unknown method names in the config-object form yield `"*"`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/xlink:_extract_decorator_route_info fingerprint=b8c9ce6db0d26b6e0b78e4323bda44aefd94b3ad7711bf6007c3d5c4b74eade1 body_fp=cd5fb67394c3a7e6813e1122ef73cadbc08bc9a2ca67eb361ed642f194c421be source_ref=6cc1924f0bfbef1953b86a5430f9a51bc9a1446b role=parsing -->
## `def _extract_decorator_route_info( decorator_node: Node, source: bytes, ) -> tuple[str, str] | None`

Parse a single Python decorator node and return the HTTP method and URL pattern it declares.

- Returns `None` if the decorator is not a dotted call (`app.get`, `bp.route`, etc.) or has no string URL argument.
- For `@app.route(...)` with no `methods=` kwarg, method is `"*"`.
- For `@app.route(...)` with multiple methods, returns only the **first** method; use `_extract_decorator_route_info_multi` to get all.
- `method` in the returned tuple is always uppercase or `"*"`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/xlink:_py_string_value fingerprint=d916e4591ba81872e461359052842a2eaf4f2d09e3efb95dedc0a2095ece9f60 body_fp=53d0c6960bed61c23f57caccbbb8e8a4cbcf21ff671ee414dcba845b9d7e3e68 source_ref=6cc1924f0bfbef1953b86a5430f9a51bc9a1446b role=parsing -->
## `def _py_string_value(string_node: Node, source: bytes) -> str | None`

Extract the raw string content from a Python tree-sitter string node, stripping quotes and known prefixes (`f`, `r`, `b`).

- Returns `None` if the node text is too short to contain content after stripping quotes.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/xlink:_extract_methods_kwarg fingerprint=ebd21bed8840620820c3503dfd82d7bd160616fe8357748832d244156569e79e body_fp=08aa15b72eaed25fcdc332c82b961409744964300f8df5fddb7791beacaede48 source_ref=6cc1924f0bfbef1953b86a5430f9a51bc9a1446b role=parsing -->
## `def _extract_methods_kwarg(args_node: Node, source: bytes) -> list[str]`

Scan a tree-sitter `arguments` node for a `methods=[...]` keyword argument and return all HTTP method strings uppercased.

- Returns an empty list if no `methods` keyword argument is found or if its value is not a list literal.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/xlink:_extract_decorator_route_info_multi fingerprint=6b4c4ddec0425b86ec0c7f4632c83af471e649f8e4b42246a986ba68228644ee body_fp=665344f209434406316598fd32d3dbdc1e4b6bfc4ba57001ba69a0d44e823016 source_ref=6cc1924f0bfbef1953b86a5430f9a51bc9a1446b role=parsing -->
## `def _extract_decorator_route_info_multi( decorator_node: Node, source: bytes, ) -> list[tuple[str, str]]`

Expand a single decorator node into all `(method, pattern)` pairs it declares, handling multi-method `@app.route` decorators.

- Returns `[("*", pattern)]` when no explicit method list is found on a `route()` decorator.
- Re-parses the `methods=` keyword argument via `_extract_methods_kwarg` to produce one tuple per method for `@app.route("/path", methods=["GET", "POST"])`.
- Returns an empty list when `_extract_decorator_route_info` finds no recognisable route decorator.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/xlink:extract_fastapi_endpoints fingerprint=29c250bd59a3394ebabe7ffbe254b01c36226641199c41b11654b9632b81c57c body_fp=7968e5c04f7c152cd4fc5ee89eaba76d5108278b10777e75c7ebb3cf49fd04cc source_ref=6cc1924f0bfbef1953b86a5430f9a51bc9a1446b role=parsing -->
## `def extract_fastapi_endpoints( tree: Node, source: bytes, file_symbols: list[tuple[str, int, int]], ) -> list[XLinkEndpoint]`

Delegate to `_extract_py_decorator_endpoints` with `framework="fastapi"` to extract route endpoints from a Python AST.

- `tree`: root `Node` of the tree-sitter parse tree for the file.
- `file_symbols`: `(qname, start_line, end_line)` tuples used to attribute endpoints to enclosing symbols.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/xlink:extract_flask_endpoints fingerprint=ac562f2bb6545c8982351e15dd36696b90e7f2b6cff333e28eb705d7f188532c body_fp=2b2310af6ddddcd34ab68aec851b3b76e01dd542906a7cbd239acddbbd517498 source_ref=6cc1924f0bfbef1953b86a5430f9a51bc9a1446b role=parsing -->
## `def extract_flask_endpoints( tree: Node, source: bytes, file_symbols: list[tuple[str, int, int]], ) -> list[XLinkEndpoint]`

Extract Flask decorator-based route endpoints from a Python AST, delegating to `_extract_py_decorator_endpoints` with `framework="flask"`.

- `tree`: root node of the parsed Python file's AST.
- `file_symbols`: `(qname, start_line, end_line)` tuples used to attribute each endpoint to its enclosing symbol.
- Detects `@app.route`, `@app.get` (Flask 2.0+), and `@bp.route` patterns.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/xlink:_extract_py_decorator_endpoints fingerprint=25c9ca6698c56140c5881a40ccc73db67526cf75603ecb3c609bbe809a79d5fd body_fp=44252a88b4c41b015be796702d4909755f9c96c132111b56f9ed5717f8a9056c source_ref=6cc1924f0bfbef1953b86a5430f9a51bc9a1446b role=parsing -->
## `def _extract_py_decorator_endpoints( tree: Node, source: bytes, file_symbols: list[tuple[str, int, int]], framework: str, ) -> list[XLinkEndpoint]`

Walk a Python AST and emit one `XLinkEndpoint` per (method, pattern) pair found on decorator-annotated function definitions.

- `tree`: root node of the parsed Python file.
- `framework`: propagated verbatim into each `XLinkEndpoint.framework` field.
- `file_symbols`: used by `_find_enclosing_symbol` to attribute endpoints to a qname.
- Skips decorated definitions where no symbol covers the function's start line.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/xlink:extract_express_endpoints fingerprint=6a5798fb3b9aceac9402298a28f4d16f492b948666ed0506c7774da2d1c5dc2a body_fp=fcec632ad075701807ab046e9822163bac204848872595e35e4e9cb22877249b source_ref=6cc1924f0bfbef1953b86a5430f9a51bc9a1446b role=parsing -->
## `def extract_express_endpoints( tree: Node, source: bytes, file_symbols: list[tuple[str, int, int]], ) -> list[XLinkEndpoint]`

Walk a TS/JS AST and return `XLinkEndpoint` records for every Express route call (`app.get`, `router.post`, etc.).

- `tree`: root `Node` of the parsed TS/JS source.
- `file_symbols`: `(qname, start_line, end_line)` tuples used to attribute each detected route to its enclosing symbol.
- Emits one `XLinkEndpoint` per matched call; silently skips calls whose first argument is not a string literal or whose receiver contains a `.` (filtered by `_looks_like_express_receiver`).
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/xlink:_looks_like_express_receiver fingerprint=5d1bc1eecb39723cf50a91c37d4f456c677063ed48c7c0e7ca0f06cb4a51e1b7 body_fp=caa7ae9a6299504f0e1c594a03cd921c4b8e58f0d8a9982c06376c80747c8f73 source_ref=6cc1924f0bfbef1953b86a5430f9a51bc9a1446b role=util -->
## `def _looks_like_express_receiver(name: str) -> bool`

Returns `True` if `name` contains no `.`, accepting any simple identifier as a plausible Express `app` or `router` receiver while rejecting dotted member expressions like `this.cache`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/xlink:extract_ts_call_sites fingerprint=a53e5dd5b35b9744eb6dbde1f7d25a0dae6bf8df19567c6cf27c6d267815f794 body_fp=d9fc0489726a21a60138c0f28af7962ef7a37acbaa6c6a7f501df86106d65cde source_ref=6cc1924f0bfbef1953b86a5430f9a51bc9a1446b role=parsing -->
## `def extract_ts_call_sites( file_path: Path, source_root: Path, file_symbols: list[tuple[str, int, int]], ) -> list[XLinkCallSite]`

Parse a TS/TSX/JS file and return all `fetch` and `axios` call sites as `XLinkCallSite` records.

- `file_path`: read directly from disk; grammar selected by extension (TSX/JSX vs TS).
- `file_symbols`: `(qname, start_line, end_line)` tuples used to attribute each site to its enclosing symbol.
- `source_root`: accepted but unused; present for interface consistency with other extractors.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/xlink:extract_ts_endpoints fingerprint=483ea4f27048553f9f6edeb4fe566a0ebd4290c7f6fe2cd70f24cdce557357e7 body_fp=b64ba460ac40c1ced4b0028f603c92a27c94b9d2fc05b8b087cf8f61d25145eb source_ref=6cc1924f0bfbef1953b86a5430f9a51bc9a1446b role=parsing -->
## `def extract_ts_endpoints( file_path: Path, source_root: Path, file_symbols: list[tuple[str, int, int]], ) -> list[XLinkEndpoint]`

Parse a TS/JS file and return all Express route endpoint records found within it.

- `file_symbols`: `(qname, start_line, end_line)` tuples used to attribute endpoints to enclosing symbols.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/xlink:extract_py_endpoints fingerprint=649ef57520bdbb0744d147cc488c81b0f0526098177a7229242eaef2c10240a0 body_fp=081dc10129f686cddb839c9a67330d390db3cd69746a5978ed10277521496800 source_ref=6cc1924f0bfbef1953b86a5430f9a51bc9a1446b role=parsing -->
## `def extract_py_endpoints( file_path: Path, source_root: Path, file_symbols: list[tuple[str, int, int]], ) -> list[XLinkEndpoint]`

Parse a Python file and return all FastAPI and Flask route endpoints found within it.

- `file_symbols`: `(qname, start_line, end_line)` tuples used to attribute endpoints to enclosing symbols.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/xlink:normalize_url fingerprint=83de1888b3f876f48d3050c22dff5999ae480a0dbad7784ed3052d435f67b611 body_fp=36df4ccc56ea5fcbb233cb79fdd5ed02b67012bcc80545fb2e1cd453e0b5db02 source_ref=6cc1924f0bfbef1953b86a5430f9a51bc9a1446b role=parsing -->
## `def normalize_url(pattern: str) -> list[str]`

Normalise a URL pattern string into a list of path segments suitable for cross-language route matching.

- `pattern`: any raw URL pattern from fetch calls or route decorators; empty string returns `[]`.
- Parameter tokens (`{id}`, `:id`, `<type:id>`, `{_PARAM_}`) are all replaced with `_PARAM_WILDCARD`.
- Returns lowercased, slash-stripped segments; empty segments (double slashes) are dropped.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/xlink:_match_confidence fingerprint=4264f0a0926246857d2e04f9103cb5a51a907305bfc6a3e631d7083594c52a5a body_fp=ba575ccf2ba3b209c71714b7d8b6b34a5657da68f109e932dd18645537e0691d source_ref=6cc1924f0bfbef1953b86a5430f9a51bc9a1446b role=domain -->
## `def _match_confidence( site_segments: list[str], endpoint_segments: list[str], site_method: str, endpoint_method: str, ) -> float`

Compute a confidence score for a potential match between normalised URL segments and HTTP methods.

- `site_segments` / `endpoint_segments`: pre-normalised path segments from `normalize_url`.
- `site_method` / `endpoint_method`: uppercase HTTP verb or `"*"` for wildcard; mismatch between two non-wildcard values returns `0.0`.
- Returns `0.0` for hard rejections (method mismatch, differing segment counts, or empty segments); `1.0` for all-exact segment matches; `0.95` when segments match but at least one is a parameter wildcard.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/xlink:match_xlinks fingerprint=87965632ed0fdae9f76530319c0e9f85a2ff5c8317ddbb2e7edb0bd08acde0d6 body_fp=5eae2efd557fd5aadd8aa6d5f4d5b7a48ddc1df201a0616c8f0aff5fa8b33e02 source_ref=6cc1924f0bfbef1953b86a5430f9a51bc9a1446b role=domain -->
## `def match_xlinks( sites: list[XLinkCallSite], endpoints: list[XLinkEndpoint], threshold: float, ) -> list[Reference]`

Cross-join every call site against every endpoint, returning `Reference(kind="cross_language_call")` edges for matches at or above the confidence threshold.

- `threshold` — minimum `_match_confidence` score (0.0–1.0) required to emit an edge; method mismatches always score 0.0 and are never emitted.
- Duplicate `(src_qname, handler_qname)` pairs are suppressed; only one edge per pair is produced.
- Below-threshold but non-zero matches are logged at DEBUG level.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/xlink:xlink_resolve fingerprint=f0d15b5a608c973b53255ff9ba70e04650bf0dc1ac023b5328c4107c26b67a16 body_fp=d9973afa688efd76b07fd1795af70fb549652cabc55e114aae6388ae1ff02add source_ref=6cc1924f0bfbef1953b86a5430f9a51bc9a1446b role=orchestration -->
## `def xlink_resolve( *, store: Store, config: Config, source_root: Path, discovered_files: dict[str, Path], ) -> dict[str, list[Reference]]`

Orchestrate all three xlink phases across every discovered file and return `Reference` objects grouped by source file.

- `store`: queried via `symbols_in_file_with_lines`; files with no known symbols are skipped.
- `config`: supplies `xlink.confidence_threshold` and optional `xlink.scan_paths` glob filters.
- `discovered_files`: keys are relative paths used as dict keys in the return value; values are absolute paths for parsing.
- Returns `{}` when no sites or endpoints are found, or no matches exceed the threshold.
- Return dict keys are relative file paths; values are lists of `kind="cross_language_call"` `Reference` objects whose `src_qname` belongs to that file.
- `.py` files yield only endpoints; `.ts`/`.tsx`/`.js`/`.jsx`/`.mjs`/`.cjs` files yield both call sites and Express endpoints.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/xlink:_find_file_for_module fingerprint=8d387f9f0ea920c0d3799aa3186efed8de2a5521fe50c884881f1add8b30253d body_fp=d095801c2cda4d926c21e0de9bf2e62584c22e320bdb110266ec17ca9bdd1805 source_ref=6cc1924f0bfbef1953b86a5430f9a51bc9a1446b role=util -->
## `def _find_file_for_module(module: str, discovered_files: dict[str, Path]) -> str | None`

Resolve a module key (extension-stripped path) to its full relative path in `discovered_files` by trying common extensions in order.

- `module`: extension-stripped path, e.g. `"src/components/UserList"`
- Returns the first matching key in `discovered_files`, or `None` if no known extension matches
<!-- trie:end -->