---
trie_version: 0.3.0
source: tests/test_xlink.py
file_fingerprint: be630797d5cec8afaf3b289e15427aab4d10928c14e2b99e1a94e367d686906d
last_synced_at: '2026-08-30T02:42:50Z'
description: Comprehensive tests for cross-language edge detection (trie/parse/xlink.py).
defines:
- kind: module
  qualified_name: tests/test_xlink:__module__
  lines: 1-888
- kind: function
  qualified_name: tests/test_xlink:_parse_ts
  lines: 41-53
  signature: 'def _parse_ts(source: str, suffix: str = ".ts")'
- kind: function
  qualified_name: tests/test_xlink:_parse_py
  lines: 56-65
  signature: 'def _parse_py(source: str)'
- kind: function
  qualified_name: tests/test_xlink:_dummy_symbols
  lines: 68-72
  signature: 'def _dummy_symbols( names: list[str], start_line: int = 1, span: int = 100 ) -> list[tuple[str, int, int]]'
- kind: class
  qualified_name: tests/test_xlink:TestNormalizeUrl
  lines: 80-111
  signature: class TestNormalizeUrl
- kind: method
  qualified_name: tests/test_xlink:TestNormalizeUrl.test_simple_path
  lines: 81-82
  signature: def test_simple_path(self)
- kind: method
  qualified_name: tests/test_xlink:TestNormalizeUrl.test_strips_slashes
  lines: 84-85
  signature: def test_strips_slashes(self)
- kind: method
  qualified_name: tests/test_xlink:TestNormalizeUrl.test_lowercase
  lines: 87-88
  signature: def test_lowercase(self)
- kind: method
  qualified_name: tests/test_xlink:TestNormalizeUrl.test_fastapi_param
  lines: 90-92
  signature: def test_fastapi_param(self)
- kind: method
  qualified_name: tests/test_xlink:TestNormalizeUrl.test_express_param
  lines: 94-96
  signature: def test_express_param(self)
- kind: method
  qualified_name: tests/test_xlink:TestNormalizeUrl.test_flask_param
  lines: 98-100
  signature: def test_flask_param(self)
- kind: method
  qualified_name: tests/test_xlink:TestNormalizeUrl.test_template_literal_param
  lines: 102-104
  signature: def test_template_literal_param(self)
- kind: method
  qualified_name: tests/test_xlink:TestNormalizeUrl.test_empty
  lines: 106-108
  signature: def test_empty(self)
- kind: method
  qualified_name: tests/test_xlink:TestNormalizeUrl.test_deep_path
  lines: 110-111
  signature: def test_deep_path(self)
- kind: class
  qualified_name: tests/test_xlink:TestMatchConfidence
  lines: 119-156
  signature: class TestMatchConfidence
- kind: method
  qualified_name: tests/test_xlink:TestMatchConfidence.test_exact_match
  lines: 120-123
  signature: def test_exact_match(self)
- kind: method
  qualified_name: tests/test_xlink:TestMatchConfidence.test_parameterized_match
  lines: 125-128
  signature: def test_parameterized_match(self)
- kind: method
  qualified_name: tests/test_xlink:TestMatchConfidence.test_method_mismatch_rejection
  lines: 130-133
  signature: def test_method_mismatch_rejection(self)
- kind: method
  qualified_name: tests/test_xlink:TestMatchConfidence.test_wildcard_method_server
  lines: 135-138
  signature: def test_wildcard_method_server(self)
- kind: method
  qualified_name: tests/test_xlink:TestMatchConfidence.test_wildcard_method_client
  lines: 140-143
  signature: def test_wildcard_method_client(self)
- kind: method
  qualified_name: tests/test_xlink:TestMatchConfidence.test_different_segment_count
  lines: 145-148
  signature: def test_different_segment_count(self)
- kind: method
  qualified_name: tests/test_xlink:TestMatchConfidence.test_different_segments
  lines: 150-153
  signature: def test_different_segments(self)
- kind: method
  qualified_name: tests/test_xlink:TestMatchConfidence.test_empty_segments
  lines: 155-156
  signature: def test_empty_segments(self)
- kind: class
  qualified_name: tests/test_xlink:TestExtractFetchSites
  lines: 164-232
  signature: class TestExtractFetchSites
- kind: method
  qualified_name: tests/test_xlink:TestExtractFetchSites.test_simple_fetch
  lines: 165-177
  signature: def test_simple_fetch(self)
- kind: method
  qualified_name: tests/test_xlink:TestExtractFetchSites.test_fetch_with_method
  lines: 179-193
  signature: def test_fetch_with_method(self)
- kind: method
  qualified_name: tests/test_xlink:TestExtractFetchSites.test_fetch_template_literal
  lines: 195-205
  signature: def test_fetch_template_literal(self)
- kind: method
  qualified_name: tests/test_xlink:TestExtractFetchSites.test_fetch_template_literal_with_method
  lines: 207-220
  signature: def test_fetch_template_literal_with_method(self)
- kind: method
  qualified_name: tests/test_xlink:TestExtractFetchSites.test_no_symbol_attribution
  lines: 222-232
  signature: def test_no_symbol_attribution(self)
- kind: class
  qualified_name: tests/test_xlink:TestExtractAxiosSites
  lines: 240-294
  signature: class TestExtractAxiosSites
- kind: method
  qualified_name: tests/test_xlink:TestExtractAxiosSites.test_axios_get
  lines: 241-253
  signature: def test_axios_get(self)
- kind: method
  qualified_name: tests/test_xlink:TestExtractAxiosSites.test_axios_post
  lines: 255-265
  signature: def test_axios_post(self)
- kind: method
  qualified_name: tests/test_xlink:TestExtractAxiosSites.test_axios_template_literal
  lines: 267-277
  signature: def test_axios_template_literal(self)
- kind: method
  qualified_name: tests/test_xlink:TestExtractAxiosSites.test_axios_config_object
  lines: 279-294
  signature: def test_axios_config_object(self)
- kind: class
  qualified_name: tests/test_xlink:TestExtractFastapiEndpoints
  lines: 302-360
  signature: class TestExtractFastapiEndpoints
- kind: method
  qualified_name: tests/test_xlink:TestExtractFastapiEndpoints.test_get_endpoint
  lines: 303-314
  signature: def test_get_endpoint(self)
- kind: method
  qualified_name: tests/test_xlink:TestExtractFastapiEndpoints.test_post_endpoint
  lines: 316-325
  signature: def test_post_endpoint(self)
- kind: method
  qualified_name: tests/test_xlink:TestExtractFastapiEndpoints.test_parameterized_endpoint
  lines: 327-336
  signature: def test_parameterized_endpoint(self)
- kind: method
  qualified_name: tests/test_xlink:TestExtractFastapiEndpoints.test_multiple_endpoints
  lines: 338-360
  signature: def test_multiple_endpoints(self)
- kind: class
  qualified_name: tests/test_xlink:TestExtractFlaskEndpoints
  lines: 368-426
  signature: class TestExtractFlaskEndpoints
- kind: method
  qualified_name: tests/test_xlink:TestExtractFlaskEndpoints.test_route_with_methods
  lines: 369-380
  signature: def test_route_with_methods(self)
- kind: method
  qualified_name: tests/test_xlink:TestExtractFlaskEndpoints.test_flask_2_shorthand
  lines: 382-391
  signature: def test_flask_2_shorthand(self)
- kind: method
  qualified_name: tests/test_xlink:TestExtractFlaskEndpoints.test_blueprint_route
  lines: 393-402
  signature: def test_blueprint_route(self)
- kind: method
  qualified_name: tests/test_xlink:TestExtractFlaskEndpoints.test_route_without_methods
  lines: 404-414
  signature: def test_route_without_methods(self)
- kind: method
  qualified_name: tests/test_xlink:TestExtractFlaskEndpoints.test_route_multiple_methods
  lines: 416-426
  signature: def test_route_multiple_methods(self)
- kind: class
  qualified_name: tests/test_xlink:TestExtractExpressEndpoints
  lines: 434-471
  signature: class TestExtractExpressEndpoints
- kind: method
  qualified_name: tests/test_xlink:TestExtractExpressEndpoints.test_app_get
  lines: 435-447
  signature: def test_app_get(self)
- kind: method
  qualified_name: tests/test_xlink:TestExtractExpressEndpoints.test_router_get
  lines: 449-459
  signature: def test_router_get(self)
- kind: method
  qualified_name: tests/test_xlink:TestExtractExpressEndpoints.test_router_post
  lines: 461-471
  signature: def test_router_post(self)
- kind: class
  qualified_name: tests/test_xlink:TestMonorepoPattern
  lines: 479-507
  signature: class TestMonorepoPattern
- kind: method
  qualified_name: tests/test_xlink:TestMonorepoPattern.test_ts_file_with_express_and_fetch
  lines: 480-507
  signature: def test_ts_file_with_express_and_fetch(self)
- kind: class
  qualified_name: tests/test_xlink:TestMatchXlinks
  lines: 515-596
  signature: class TestMatchXlinks
- kind: method
  qualified_name: tests/test_xlink:TestMatchXlinks.test_exact_match_produces_edge
  lines: 516-527
  signature: def test_exact_match_produces_edge(self)
- kind: method
  qualified_name: tests/test_xlink:TestMatchXlinks.test_parameterized_match_above_threshold
  lines: 529-537
  signature: def test_parameterized_match_above_threshold(self)
- kind: method
  qualified_name: tests/test_xlink:TestMatchXlinks.test_method_mismatch_rejected
  lines: 539-547
  signature: def test_method_mismatch_rejected(self)
- kind: method
  qualified_name: tests/test_xlink:TestMatchXlinks.test_wildcard_method_matches
  lines: 549-557
  signature: def test_wildcard_method_matches(self)
- kind: method
  qualified_name: tests/test_xlink:TestMatchXlinks.test_no_duplicates
  lines: 559-569
  signature: def test_no_duplicates(self)
- kind: method
  qualified_name: tests/test_xlink:TestMatchXlinks.test_below_threshold_excluded
  lines: 571-581
  signature: def test_below_threshold_excluded(self)
- kind: method
  qualified_name: tests/test_xlink:TestMatchXlinks.test_multiple_matches
  lines: 583-596
  signature: def test_multiple_matches(self)
- kind: function
  qualified_name: tests/test_xlink:_make_xlink_project
  lines: 604-653
  signature: 'def _make_xlink_project(tmp_path: Path) -> Path'
- kind: function
  qualified_name: tests/test_xlink:_scan
  lines: 656-660
  signature: 'def _scan(project: Path) -> tuple[Store, object]'
- kind: class
  qualified_name: tests/test_xlink:TestIntegration
  lines: 663-751
  signature: class TestIntegration
- kind: method
  qualified_name: tests/test_xlink:TestIntegration.test_cross_language_edges_in_scan
  lines: 664-696
  signature: 'def test_cross_language_edges_in_scan(self, tmp_path: Path)'
- kind: method
  qualified_name: tests/test_xlink:TestIntegration.test_method_mismatch_prevents_edge
  lines: 698-724
  signature: 'def test_method_mismatch_prevents_edge(self, tmp_path: Path)'
- kind: method
  qualified_name: tests/test_xlink:TestIntegration.test_no_cross_language_edges_for_single_language
  lines: 726-751
  signature: 'def test_no_cross_language_edges_for_single_language(self, tmp_path: Path)'
- kind: class
  qualified_name: tests/test_xlink:TestHubThresholdCascade
  lines: 759-842
  signature: class TestHubThresholdCascade
- kind: method
  qualified_name: tests/test_xlink:TestHubThresholdCascade.test_popular_endpoint_hits_hub_threshold
  lines: 763-842
  signature: 'def test_popular_endpoint_hits_hub_threshold(self, tmp_path: Path)'
- kind: class
  qualified_name: tests/test_xlink:TestXLinkConfig
  lines: 850-875
  signature: class TestXLinkConfig
- kind: method
  qualified_name: tests/test_xlink:TestXLinkConfig.test_default_config
  lines: 851-854
  signature: def test_default_config(self)
- kind: method
  qualified_name: tests/test_xlink:TestXLinkConfig.test_from_dict_with_xlink
  lines: 856-865
  signature: def test_from_dict_with_xlink(self)
- kind: method
  qualified_name: tests/test_xlink:TestXLinkConfig.test_from_dict_without_xlink
  lines: 867-870
  signature: def test_from_dict_without_xlink(self)
- kind: method
  qualified_name: tests/test_xlink:TestXLinkConfig.test_xlink_is_frozen
  lines: 872-875
  signature: def test_xlink_is_frozen(self)
- kind: class
  qualified_name: tests/test_xlink:TestEdgeKind
  lines: 883-887
  signature: class TestEdgeKind
- kind: method
  qualified_name: tests/test_xlink:TestEdgeKind.test_cross_language_call_in_edge_kinds
  lines: 884-887
  signature: def test_cross_language_call_in_edge_kinds(self)
incoming_refs: 0
outgoing_refs: 0
---
<!-- trie:section symbol=tests/test_xlink:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=db4432db194952b93fbc1b3920fb2c27f49ed6548f4d00e7b79e4cc60b19ad79 source_ref=1e4c89db21789a50b63ab90d3697a8f1ffa322b2 role=test -->
Comprehensive test suite for `trie/parse/xlink.py`, covering cross-language HTTP edge detection between TypeScript/JS clients and Python servers.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_xlink:_parse_ts fingerprint=425a88b5c93da056f28254c9906c67bc174cf43c968c5238bbf84948323411b3 body_fp=dc50bfc94e3629c4dbd2dcafd0472a1a1ce31dd9d0ef1d44797b110fd3c10f17 source_ref=1e4c89db21789a50b63ab90d3697a8f1ffa322b2 role=util -->
## `def _parse_ts(source: str, suffix: str = ".ts")`

Parse a TypeScript/JS source string into a tree-sitter tree and return the root node and encoded bytes.

- `suffix`: selects TSX/JSX grammar for `.tsx`/`.jsx`; defaults to TypeScript grammar otherwise.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_xlink:_parse_py fingerprint=d90525cba7da834b872b725c982c0f157297915aaa6ee0a3c4bfe3d9d6d4557e body_fp=62fd78a629b2ea595a1ed106aa4d8069d8aeabca85b314517eabbcef00760a3b source_ref=1e4c89db21789a50b63ab90d3697a8f1ffa322b2 role=test -->
## `def _parse_py(source: str)`

Parse a Python source string into a tree-sitter AST and return the root node with its UTF-8-encoded bytes.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_xlink:_dummy_symbols fingerprint=baf2a26208047811cbc188f75e032f5c764321d62598523fcedd6abaa57bb227 body_fp=5497643c9628422fd9973d5c1935fb0ac56c861eff7e3c628ca9b9e5aee615a7 source_ref=1e4c89db21789a50b63ab90d3697a8f1ffa322b2 role=test -->
## `def _dummy_symbols( names: list[str], start_line: int = 1, span: int = 100 ) -> list[tuple[str, int, int]]`

Create a list of fake symbol tuples, each spanning `[start_line, start_line + span]`, for use in extractor tests.

- `names`: symbol qualified names to wrap as tuples.
- `span`: line range width; defaults to 100 to ensure extractors attribute nodes to the symbol.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_xlink:TestNormalizeUrl fingerprint=4b07d8d35fd386bb47b6f779bde52b5303e34e33733602265d78b8ac66616cce body_fp=c239de87d7d89e63b1dd184a7a9e8b7629abbb36b93cde081d9db0c491faef2e source_ref=1e4c89db21789a50b63ab90d3697a8f1ffa322b2 role=test -->
## `class TestNormalizeUrl`

Test suite for `normalize_url`, verifying segment splitting, slash stripping, lowercasing, and parameter normalisation across FastAPI (`{param}`), Express (`:param`), Flask (`<type:param>`), and template-literal (`{_PARAM_}`) styles.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_xlink:TestNormalizeUrl.test_simple_path fingerprint=d6e67fe6b6fdf09a1b8166f49747d15d7d725077c1d3d326e3b12d46fe9b0d51 body_fp=71c37cbc12df3da890e0c43a6664352ba306c6de9988a0f83002d526385cce05 source_ref=1e4c89db21789a50b63ab90d3697a8f1ffa322b2 role=test -->
## `def test_simple_path(self)`

Asserts that `normalize_url` splits a simple path into lowercase segment tokens, excluding the leading slash.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_xlink:TestNormalizeUrl.test_strips_slashes fingerprint=dfdab37ccd0d95be74d823b3e76b6a2b88d2da8ff154b649d22dd48890b714ae body_fp=1ede9c11ef4c52ffa3274e58aae35e5c9b0f34efec3941006c16e247bf139874 source_ref=1e4c89db21789a50b63ab90d3697a8f1ffa322b2 role=test -->
## `def test_strips_slashes(self)`

Asserts that `normalize_url` strips trailing slashes from a URL path.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_xlink:TestNormalizeUrl.test_lowercase fingerprint=3539d5377a7f96e06c474cdf0964b95ff7a7357df4dc3d2e123d7f1ba261a69c body_fp=b1618606e4d17b29df7f32ab2ccce22c87e4744d54875a8800b35ea8e362dcfa source_ref=1e4c89db21789a50b63ab90d3697a8f1ffa322b2 role=test -->
## `def test_lowercase(self)`

Asserts that `TestNormalizeUrl` lowercases all path segments during URL normalisation.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_xlink:TestNormalizeUrl.test_fastapi_param fingerprint=33ae7d154068e0669abc2b90504b894cb8c12b21865e5638de36e35b2a2f6be8 body_fp=a484df8a0d978eb4ff536f47ef9fd05074f11cde47caf92ca932b3bba7696764 source_ref=1e4c89db21789a50b63ab90d3697a8f1ffa322b2 role=test -->
## `def test_fastapi_param(self)`

Asserts that `TestNormalizeUrl` normalises FastAPI-style `{param}` path segments to the canonical `{_PARAM_}` placeholder.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_xlink:TestNormalizeUrl.test_express_param fingerprint=e6e0dce9a2fbfee00eea2f5349522c8d4c80e8695abc4e4f896cc7082bc0acd3 body_fp=3b93cdd21518dcb8ec53eee9a0e858df429441620ce901258622ac338f92c791 source_ref=1e4c89db21789a50b63ab90d3697a8f1ffa322b2 role=test -->
## `def test_express_param(self)`

Asserts that `normalize_url` converts Express-style colon parameters (`:userId`) to the canonical `{_PARAM_}` segment.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_xlink:TestNormalizeUrl.test_flask_param fingerprint=7fea380dd1169a0cc33e10c481206f913c4a9fa48bcc543a9d15eeb6dd024dc7 body_fp=30196a500c93f6823d5eecc55251f88a9488058ac31fe6755d0f912a959d201c source_ref=1e4c89db21789a50b63ab90d3697a8f1ffa322b2 role=test -->
## `def test_flask_param(self)`

Asserts that `normalize_url` converts Flask-style `<int:user_id>` path parameters to the canonical `{_PARAM_}` segment.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_xlink:TestNormalizeUrl.test_template_literal_param fingerprint=caca41da0723244c6465f95b97539011a5166b42e71f62a80173d737dba7abad body_fp=14fcd723fe7454913b0ea908bf14a1c83ad86dce057b14e2fa1677c2ccd0c595 source_ref=1e4c89db21789a50b63ab90d3697a8f1ffa322b2 role=test -->
## `def test_template_literal_param(self)`

Asserts that `TestNormalizeUrl` preserves the already-normalised `{_PARAM_}` placeholder token unchanged during segment splitting.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_xlink:TestNormalizeUrl.test_empty fingerprint=681cc8e3c29713db1594a25f219e97d662ae2a277f5aac8864d5a544923cc819 body_fp=dadcc388cff61e6ad306ca0b5c6e576358446679598f135c9566b9f2198b39de source_ref=1e4c89db21789a50b63ab90d3697a8f1ffa322b2 role=test -->
## `def test_empty(self)`

Asserts that `normalize_url` returns an empty list for both an empty string and a bare slash.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_xlink:TestNormalizeUrl.test_deep_path fingerprint=58b013d1208935503d75f6072fcc2586529bb7998a211fdca2b75a4152f27a85 body_fp=91e5e96581616527209d802f19a5215631a68adc99b1065e91fb1176bec1ff4d source_ref=1e4c89db21789a50b63ab90d3697a8f1ffa322b2 role=test -->
## `def test_deep_path(self)`

Asserts that `normalize_url` correctly splits a four-segment path into an ordered list of lowercase strings.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_xlink:TestMatchConfidence fingerprint=534edce8070a059d2d2fa9956ca2b5771f34be9a0bb2bb8a8450a2d0bdd416e1 body_fp=74a27206610c1989df52c31301cb21f9b25a5b26e705f9596d40ef55dad2a604 source_ref=1e4c89db21789a50b63ab90d3697a8f1ffa322b2 role=test -->
## `class TestMatchConfidence`

Test suite for `_match_confidence`, covering all confidence return values and method-matching rules.

- Verifies exact path match returns `1.0`, parameterized match returns `0.95`
- Confirms method mismatch always returns `0.0` regardless of path equality
- Confirms wildcard `"*"` on either client or server side bypasses method check
- Confirms differing segment count or segment content returns `0.0`
- Confirms empty segment lists return `0.0`
<!-- trie:end -->
<!-- trie:section symbol=tests/test_xlink:TestMatchConfidence.test_exact_match fingerprint=36acfe059c149d4bd4e6b8749294f7442cb8b5c1577b0894672ed7d7cee1cd24 body_fp=45888579aa0924bf9e01dd2e026909c61b947ac7ce1c6d301c5d928ee5d8e245 source_ref=1e4c89db21789a50b63ab90d3697a8f1ffa322b2 role=test -->
## `def test_exact_match(self)`

Asserts that `_match_confidence` returns `1.0` for identical URL segments and matching HTTP methods.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_xlink:TestMatchConfidence.test_parameterized_match fingerprint=8058a1cbfbf890fdc1d103825c7917b264d3034d1289858270d8ba4caaec0b37 body_fp=11fa7728a7c02a8a38b2c743ca546824bf3eca9714796cb9df660a21ec10af2d source_ref=1e4c89db21789a50b63ab90d3697a8f1ffa322b2 role=test -->
## `def test_parameterized_match(self)`

Asserts that `_match_confidence` returns `0.95` when one segment is a normalised parameter placeholder and the other is a named parameter.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_xlink:TestMatchConfidence.test_method_mismatch_rejection fingerprint=6d1fa9700674d9c940000a4146d5032cf36899e333d122fe74a5aed6ffc45c04 body_fp=5942302a025fac42b7caa9ecdfb5c0f0c9894d99879ef73e5e4664dcd3708fc1 source_ref=1e4c89db21789a50b63ab90d3697a8f1ffa322b2 role=test -->
## `def test_method_mismatch_rejection(self)`

Assert that `_match_confidence` returns `0.0` when client method is `GET` and server method is `POST`, even on identical URL segments.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_xlink:TestMatchConfidence.test_wildcard_method_server fingerprint=78b2ec65b57d9a462afcdd9280cbf625f7876f62425c65c67c0762925384caa1 body_fp=790a8d921142008ecb2de3ef94c0ae9633c83c77d499296322d4f70500675017 source_ref=1e4c89db21789a50b63ab90d3697a8f1ffa322b2 role=test -->
## `def test_wildcard_method_server(self)`

Assert that `_match_confidence` returns `1.0` when the server-side method is the wildcard `"*"` and segments match exactly.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_xlink:TestMatchConfidence.test_wildcard_method_client fingerprint=ef6d5e55727926e9c73252b0829830220ab2d1fadc8637898f9972b3e4eef148 body_fp=1f2aec0b8c225bc5e097e0cdab2054ebef7ce7cbd2fb27950cd7533f35e2b504 source_ref=1e4c89db21789a50b63ab90d3697a8f1ffa322b2 role=test -->
## `def test_wildcard_method_client(self)`

Asserts that `_match_confidence` returns `1.0` when the client method is `"*"` and the server method is a concrete verb.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_xlink:TestMatchConfidence.test_different_segment_count fingerprint=4d7ef6035692a895048ef10525e326cae50366a07ca24a2a141d368072374cea body_fp=fbca33e69b4899ba2a3ef4c0218270b3336d5251dff84b37d45af61eb21496b3 source_ref=1e4c89db21789a50b63ab90d3697a8f1ffa322b2 role=test -->
## `def test_different_segment_count(self)`

Asserts that `_match_confidence` returns `0.0` when the site and endpoint URL segment counts differ.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_xlink:TestMatchConfidence.test_different_segments fingerprint=bbe2b12cbd7a1a242f4da8f0d1e9d57c924314a980bbdd569f9bc641508fc301 body_fp=c70d65abe13c9d580f5951ec988e2e9dfb5b1a1282538a175e5d6b17e554cd8e source_ref=1e4c89db21789a50b63ab90d3697a8f1ffa322b2 role=test -->
## `def test_different_segments(self)`

Asserts that `_match_confidence` returns `0.0` when same-length segment lists differ in content (e.g. `users` vs `items`).
<!-- trie:end -->
<!-- trie:section symbol=tests/test_xlink:TestMatchConfidence.test_empty_segments fingerprint=023de26e2dba4f68655a49e131ef77a2efc85aadb3bf6b508598c6fe67ae0e16 body_fp=d6197f023c37e66926ea90d79651172821ea6ce7be2cb911977569a5f44e871e source_ref=1e4c89db21789a50b63ab90d3697a8f1ffa322b2 role=test -->
## `def test_empty_segments(self)`

Asserts that `_match_confidence` returns `0.0` when both segment lists are empty.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_xlink:TestExtractFetchSites fingerprint=8facf43bf7dc108b5a9a90b78148ec3180f64921235670d16a31ce0f9503109d body_fp=25b408c807c1e7b2ab30e97510e1c54ee0a32654563fe4507996e6c49ae75237 source_ref=1e4c89db21789a50b63ab90d3697a8f1ffa322b2 role=test -->
## `class TestExtractFetchSites`

Tests `extract_fetch_sites` across plain strings, template literals, explicit HTTP methods, and empty symbol attribution.

- `test_simple_fetch`: plain string URL defaults method to `GET`, framework to `"fetch"`.
- `test_fetch_with_method`: explicit `method: "POST"` in options object is captured.
- `test_fetch_template_literal`: interpolated template literal normalises to `{_PARAM_}`.
- `test_fetch_template_literal_with_method`: combines template literal URL with explicit `DELETE` method.
- `test_no_symbol_attribution`: empty symbols list causes all call sites to be skipped.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_xlink:TestExtractFetchSites.test_simple_fetch fingerprint=75c16bbede79534e5adca2b98b51ad6040d1b446f1c4b20ffc8a761745ef0dd5 body_fp=e8292328e117fcd6d8006683f9dc12e26ba286eedfc56e3718c3a9205dc75d38 source_ref=1e4c89db21789a50b63ab90d3697a8f1ffa322b2 role=test -->
## `def test_simple_fetch(self)`

Verifies that `extract_fetch_sites` extracts a single `GET` call site with correct pattern and `"fetch"` framework from a plain `fetch("/api/users")` call.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_xlink:TestExtractFetchSites.test_fetch_with_method fingerprint=e08cbfb0e1cd6fa2618178295db9d78e8e57ae41e55d130ddcdfa5e3f89dc3f8 body_fp=236cc3f4803a6a90ec97265f1c16e05fe8f7cb7d09fee41f7ab9fd53c9c24154 source_ref=1e4c89db21789a50b63ab90d3697a8f1ffa322b2 role=test -->
## `def test_fetch_with_method(self)`

Asserts that `extract_fetch_sites` correctly reads the `method: "POST"` option from a `fetch` call's second argument and records it on the extracted `XLinkCallSite`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_xlink:TestExtractFetchSites.test_fetch_template_literal fingerprint=dfc7c79d83f34cfc796183acad0997b346161814a203244f6676c4094eed1cc6 body_fp=a269ce4c24344b382e63897fe42f613cfc00667218b9873ea87684a7d80e5b43 source_ref=1e4c89db21789a50b63ab90d3697a8f1ffa322b2 role=test -->
## `def test_fetch_template_literal(self)`

Asserts that `extract_fetch_sites` normalises a template-literal interpolation in a `fetch` URL to the `{_PARAM_}` placeholder segment.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_xlink:TestExtractFetchSites.test_fetch_template_literal_with_method fingerprint=9d341fca3503f5c7c05d31b8cb17f8a77286f838d300d2d034b4aa082c1de4c8 body_fp=c5828d9b3108898b1cc6a9122cfd2d8f1bfd9d9d4ea62b29eccdd44929bb6d62 source_ref=1e4c89db21789a50b63ab90d3697a8f1ffa322b2 role=test -->
## `def test_fetch_template_literal_with_method(self)`

Asserts that `extract_fetch_sites` correctly extracts a `DELETE` call site from a `fetch` using a template-literal URL with an interpolated parameter and an explicit `method` option.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_xlink:TestExtractFetchSites.test_no_symbol_attribution fingerprint=1ca46f72b56acf6a438c86b34e0305cf03cbf9916ba51638c4b9e5d14cfb81b8 body_fp=4a67769d84dc4ead73a0bccfc02a7fe93637a7301fb90e180a0330110694fbb3 source_ref=1e4c89db21789a50b63ab90d3697a8f1ffa322b2 role=test -->
## `def test_no_symbol_attribution(self)`

Asserts that `TestExtractFetchSites` skips a `fetch` call site when no enclosing symbol can be attributed (empty symbols list yields zero results).
<!-- trie:end -->
<!-- trie:section symbol=tests/test_xlink:TestExtractAxiosSites fingerprint=119001f43005542077fc8915575c74bdd522366a84121273f1ff7065b9fc0d59 body_fp=7d500e6f37e1ac3b688757466209f72584e79980dbf3c8c16ebd1028e0a01625 source_ref=1e4c89db21789a50b63ab90d3697a8f1ffa322b2 role=test -->
## `class TestExtractAxiosSites`

Tests `extract_axios_sites` across four call patterns: `axios.get`, `axios.post`, template-literal URLs (normalised to `{_PARAM_}`), and the config-object form `axios({ url, method, data })`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_xlink:TestExtractAxiosSites.test_axios_get fingerprint=1ff7c8c906ddd575fe95fc1468ba297112a198aa0a0d0eccc07c97f10428975e body_fp=fcdb4efec3dbcff3d4a4fd07916f4c78c5b3ef39bae6aee77d4b7ccc54ecfd55 source_ref=1e4c89db21789a50b63ab90d3697a8f1ffa322b2 role=test -->
## `def test_axios_get(self)`

Asserts that `extract_axios_sites` correctly extracts an `axios.get` call with method `"GET"`, pattern `"/api/stats"`, and framework `"axios"`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_xlink:TestExtractAxiosSites.test_axios_post fingerprint=e5e0e3c60b5d26b155b83302a8f057a4317980ba31e931e6ac3826010ff30c32 body_fp=87fac23da1cf55251ed005b0b52308f699f28478cdb45fee7b1abedb0478d0ee source_ref=1e4c89db21789a50b63ab90d3697a8f1ffa322b2 role=test -->
## `def test_axios_post(self)`

Asserts that `extract_axios_sites` extracts a single `POST` call site from an `axios.post(url, data)` invocation within `TestExtractAxiosSites`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_xlink:TestExtractAxiosSites.test_axios_template_literal fingerprint=f96ec4c7672ab7db61a7f5341985c49365e8b1cfb1bee156113d65647bfea035 body_fp=6cb4a7241597800600fc124562283547e4bbddf209fcd94b406f17887c9e8ae1 source_ref=1e4c89db21789a50b63ab90d3697a8f1ffa322b2 role=test -->
## `def test_axios_template_literal(self)`

Asserts that `TestExtractAxiosSites` normalises a template-literal URL in an `axios.get` call to a `{_PARAM_}` placeholder pattern.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_xlink:TestExtractAxiosSites.test_axios_config_object fingerprint=72adf69ebc87b2f9d99c12a5ccb2e3f7afa30bd717368de4880471f56b46f3f3 body_fp=8bb36f656765cd6fc2aca9546edbf4b33a9a61c7dfdab390cefa45a86c1a229d source_ref=1e4c89db21789a50b63ab90d3697a8f1ffa322b2 role=test -->
## `def test_axios_config_object(self)`

Asserts that `TestExtractAxiosSites` correctly extracts a call site from an `axios({url, method, data})` config-object invocation, yielding method `"PUT"` and pattern `"/api/admin/bulk"`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_xlink:TestExtractFastapiEndpoints fingerprint=941190c052b1dd8ad05adb2832bdbe695886ad7dc85ea3b63264b4a470bb6fd2 body_fp=8e6dfd66068e3b35d80b573d06f43bd4bd3f4a526a2ee60d5d80d91c57c1b2c8 source_ref=1e4c89db21789a50b63ab90d3697a8f1ffa322b2 role=test -->
## `class TestExtractFastapiEndpoints`

Tests `extract_fastapi_endpoints` across GET, POST, DELETE, parameterized path, and multi-endpoint scenarios.

- Asserts `method`, `pattern`, and `framework == "fastapi"` on extracted `XLinkEndpoint` objects.
- `test_parameterized_endpoint` confirms raw path syntax (`{user_id}`) is preserved as-is.
- `test_multiple_endpoints` uses distinct per-symbol line ranges to verify correct attribution of all three decorators.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_xlink:TestExtractFastapiEndpoints.test_get_endpoint fingerprint=8f2fa1cd0d9f8cc2943fbe587f74bf6e9c6ba6f7f30428173bb1678e4da415a5 body_fp=e4d20838cbc8d0043f96b3081d3c025d93bbbadaa9053778182fd7079066526d source_ref=1e4c89db21789a50b63ab90d3697a8f1ffa322b2 role=test -->
## `def test_get_endpoint(self)`

Asserts that `extract_fastapi_endpoints` extracts one endpoint with method `GET`, pattern `/api/users`, and framework `fastapi` from a minimal `@app.get` decorated function.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_xlink:TestExtractFastapiEndpoints.test_post_endpoint fingerprint=4e2b1b210aa2c55955fc8777dcf6de31633de21c9c41958529492108dcb02c13 body_fp=acf38681869ecfefdd88013dba27681a689573e1a78f1c1ff4288964ac4c6d62 source_ref=1e4c89db21789a50b63ab90d3697a8f1ffa322b2 role=test -->
## `def test_post_endpoint(self)`

Verifies that `extract_fastapi_endpoints` correctly extracts a `POST` method from an `@app.post` decorated FastAPI endpoint.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_xlink:TestExtractFastapiEndpoints.test_parameterized_endpoint fingerprint=570ba6799d78ce64962ddb496fc9a66129d122e269e1fb15bd42cf9b50f18aa4 body_fp=3fb93352f103eb768a669f744ce7d47a86c135c3a01aba457c62e9d5b53aba59 source_ref=1e4c89db21789a50b63ab90d3697a8f1ffa322b2 role=test -->
## `def test_parameterized_endpoint(self)`

Asserts that `extract_fastapi_endpoints` preserves the raw `{user_id}` path parameter syntax in the extracted endpoint's `pattern` field.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_xlink:TestExtractFastapiEndpoints.test_multiple_endpoints fingerprint=3f4096e92e3788d3085a17a306e2bb01b6d1350f8cd358075e13592a24dcefe2 body_fp=407ee1871a5f6e87ff13674bafcffcb69272686b52b156b571630118de080fab source_ref=1e4c89db21789a50b63ab90d3697a8f1ffa322b2 role=test -->
## `def test_multiple_endpoints(self)`

Asserts `extract_fastapi_endpoints` extracts three distinct endpoints (GET, POST, DELETE) from a Python source with three decorated route functions and matching symbol spans.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_xlink:TestExtractFlaskEndpoints fingerprint=15adf1bf2cee290366cbe0a3cdbe56b093be44e57242d9fe20c9c7d034486229 body_fp=5eaaca172909490b6afdcc7df7780ab9b50c87efa0760c32ff94f33e17e839e3 source_ref=1e4c89db21789a50b63ab90d3697a8f1ffa322b2 role=test -->
## `class TestExtractFlaskEndpoints`

Test suite for `extract_flask_endpoints` covering Flask route decorator variants.

- `test_route_with_methods` — asserts method, pattern, and framework fields on a `methods=["GET"]` route
- `test_flask_2_shorthand` — verifies Flask 2-style `@app.get()` shorthand is parsed correctly
- `test_blueprint_route` — confirms `@bp.route()` blueprint decorators are recognised
- `test_route_without_methods` — asserts missing `methods=` argument produces method `"*"` (wildcard)
- `test_route_multiple_methods` — asserts `methods=["GET", "POST"]` emits two separate endpoint objects
<!-- trie:end -->
<!-- trie:section symbol=tests/test_xlink:TestExtractFlaskEndpoints.test_route_with_methods fingerprint=178dfb2970328a4fdc3ef9c7f826764ac68559f7f008a92d319ff2899aeb7f7f body_fp=a09531d3e66bbf2ab3c8b5beeb2658ea7c3f25a1eb9a9243a73cdbbcf69c7054 source_ref=1e4c89db21789a50b63ab90d3697a8f1ffa322b2 role=test -->
## `def test_route_with_methods(self)`

Verify that `extract_flask_endpoints` correctly extracts a single GET endpoint from a `@app.route` decorator with an explicit `methods=["GET"]` argument, checking method, pattern, and framework fields.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_xlink:TestExtractFlaskEndpoints.test_flask_2_shorthand fingerprint=a003b3cf48d128853ffc892ef9fca0b66f093fd6a82ddeeed31774bed30e904c body_fp=33962b831e0593a08f01f33419be10b62fde29545b34a279edf1aa7e879a7ffc source_ref=1e4c89db21789a50b63ab90d3697a8f1ffa322b2 role=test -->
## `def test_flask_2_shorthand(self)`

Asserts that `extract_flask_endpoints` recognises Flask 2 HTTP-method shorthand decorators (e.g. `@app.get`) and returns a single endpoint with method `"GET"`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_xlink:TestExtractFlaskEndpoints.test_blueprint_route fingerprint=fbab4a73584aecc377f2fa4d093bb37b6260ebb2d19409a6751a1e81af0d9291 body_fp=abb44109a8815f9cc6f640fd878c583d5faecf9f446c7a638c3c0034572d61ee source_ref=1e4c89db21789a50b63ab90d3697a8f1ffa322b2 role=test -->
## `def test_blueprint_route(self)`

Asserts that `extract_flask_endpoints` correctly extracts a PUT endpoint defined via a Flask blueprint `@bp.route` decorator.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_xlink:TestExtractFlaskEndpoints.test_route_without_methods fingerprint=43486d24e6bdd543813c7e3fb51e20c249264456066e932febad55c27e1d1eee body_fp=5df625855262722cf854fe2556cc4a2fde9f88842c682a74de6b844b8bd8dfcc source_ref=1e4c89db21789a50b63ab90d3697a8f1ffa322b2 role=test -->
## `def test_route_without_methods(self)`

Assert that `extract_flask_endpoints` assigns method `"*"` when `@app.route` is declared without a `methods=` argument.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_xlink:TestExtractFlaskEndpoints.test_route_multiple_methods fingerprint=5998b9ae90cf7e3d5732bb22abda22f02f5281b28d0dc41d2746b16bf250990a body_fp=e75e82fc4198c3d1f06c2ffa1ce0717d7d8262910235d466502c7b80e64ea5fe source_ref=1e4c89db21789a50b63ab90d3697a8f1ffa322b2 role=test -->
## `def test_route_multiple_methods(self)`

Asserts that `extract_flask_endpoints` emits one `XLinkEndpoint` per method when a Flask route declares multiple methods in its `methods` list.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_xlink:TestExtractExpressEndpoints fingerprint=83545573d272ff0aa8792b191a41f9cb0db95bb0b3ac8471a3be9d55eb49e75f body_fp=4137d8f4c8c559d7caebfd6a72411be6ef8f3b0d69ba39b6c99425ff50be5ec1 source_ref=1e4c89db21789a50b63ab90d3697a8f1ffa322b2 role=test -->
## `class TestExtractExpressEndpoints`

Tests `extract_express_endpoints` against `app.get`, `router.get`, and `router.post` call patterns, asserting correct method, pattern, and framework attribution.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_xlink:TestExtractExpressEndpoints.test_app_get fingerprint=940d34f05c3a00dcbdc7c25aa9dce881c854937af6a05ee63ff931123e7f4462 body_fp=b05dadd5103cbfa78977da8d6cbca6c1f6113395aeb546c23583966da6992c53 source_ref=1e4c89db21789a50b63ab90d3697a8f1ffa322b2 role=test -->
## `def test_app_get(self)`

Asserts that `extract_express_endpoints` extracts a single GET endpoint from an `app.get()` Express call, with correct method, pattern, and framework fields.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_xlink:TestExtractExpressEndpoints.test_router_get fingerprint=a84978030c18099088105b245c5c0390fa40cb2edabecc74d066584f0bf8f1ad body_fp=cae6b8d089275cd31e6fbcedbf0700bd2475aa131d91c323e93c7b233c47766f source_ref=1e4c89db21789a50b63ab90d3697a8f1ffa322b2 role=test -->
## `def test_router_get(self)`

Asserts that `extract_express_endpoints` detects a `router.get` call as a single GET endpoint.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_xlink:TestExtractExpressEndpoints.test_router_post fingerprint=7176d13589d1edc847717bf59840c0e594bb517bb7b25d1aba2affd591e0a388 body_fp=8c4157a58fb0716241aba5ae5ebf9cbb1c2cbe0c2c7cb593ca9caae6e26f0ac0 source_ref=1e4c89db21789a50b63ab90d3697a8f1ffa322b2 role=test -->
## `def test_router_post(self)`

Asserts that `extract_express_endpoints` correctly extracts a single POST endpoint from an Express `router.post()` call.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_xlink:TestMonorepoPattern fingerprint=5257d07b3ea661d7f1e27a71423543357ad0171d9079bd78a781eddd9124c8fd body_fp=543826f8a30175d42e7107320114338b8f1619d3c7bce6d8dcf7c11c35e158f7 source_ref=1e4c89db21789a50b63ab90d3697a8f1ffa322b2 role=test -->
## `class TestMonorepoPattern`

Test class verifying that a single TypeScript file containing both Express route definitions and `fetch` call sites is correctly parsed by both extractors simultaneously.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_xlink:TestMonorepoPattern.test_ts_file_with_express_and_fetch fingerprint=005ddaffe770107a6975935ef770d09582bb8f05c4179ea38d290359f34d2bda body_fp=ffe7adeb02ebd9cb5fa7eca6bc2a2f1aa515e5b271575be412e6de8842cbb738 source_ref=1e4c89db21789a50b63ab90d3697a8f1ffa322b2 role=test -->
## `def test_ts_file_with_express_and_fetch(self)`

Verifies that `TestMonorepoPattern` correctly extracts both Express endpoints and `fetch` call sites from a single TypeScript source file containing both patterns.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_xlink:TestMatchXlinks fingerprint=cef8d7518de52c380c79da62590ccacfd9bd4cbda00136d532db1396d2d17014 body_fp=3f5d8e332f38d8598ae574eef4c9c530b5513a87d5d60bdcf6b2a03f22f3f835 source_ref=1e4c89db21789a50b63ab90d3697a8f1ffa322b2 role=test -->
## `class TestMatchXlinks`

Tests `match_xlinks` edge production, covering exact matches, parameterised URL matching, method mismatch rejection, wildcard methods, deduplication of `(src_qname, target_qname)` pairs, confidence threshold gating, and multi-pair resolution.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_xlink:TestMatchXlinks.test_exact_match_produces_edge fingerprint=3a363791549d790c400b50d40cc8eaea0411d7487ee8e7b90c0d38c324630ca9 body_fp=39505c0a255c8e22864335b92d39a327cb72a565b551bb28d8df2f10940fa418 source_ref=1e4c89db21789a50b63ab90d3697a8f1ffa322b2 role=test -->
## `def test_exact_match_produces_edge(self)`

Asserts that `TestMatchXlinks.match_xlinks` produces exactly one `cross_language_call` reference when a GET fetch call site exactly matches a GET FastAPI endpoint at the same path.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_xlink:TestMatchXlinks.test_parameterized_match_above_threshold fingerprint=894be4b38fe5e22723266e4826cd9f06a3431e1071c7413463cfa4beee1be1cd body_fp=49dac3f587bf5f4c494c39d2c9c5c85e990b51b0b61376703c18ee43d753f5b3 source_ref=1e4c89db21789a50b63ab90d3697a8f1ffa322b2 role=test -->
## `def test_parameterized_match_above_threshold(self)`

Assert that `match_xlinks` produces one edge when a parameterized client URL matches a parameterized server pattern above the 0.7 confidence threshold.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_xlink:TestMatchXlinks.test_method_mismatch_rejected fingerprint=db67a9fa8bdda8bbdd13a640b0d57d6e253584795c23743f5503ec9a214d0a94 body_fp=c6c27bbfc20075042796d610d523cbbcc1279ebc17254b3a5184eefabb39bc55 source_ref=1e4c89db21789a50b63ab90d3697a8f1ffa322b2 role=test -->
## `def test_method_mismatch_rejected(self)`

Assert that `TestMatchXlinks.match_xlinks` returns no edges when the call site method (`POST`) differs from the endpoint method (`GET`) on the same path.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_xlink:TestMatchXlinks.test_wildcard_method_matches fingerprint=34410a438f8ce285d4a269f2be6e3ecfacea0f4c93a3b503707eb658f8f2fe02 body_fp=1760dddfbed0a9efdb9f7e1e622d2d963d6c3ffc32ec40fc884d8b9e583eb1e6 source_ref=1e4c89db21789a50b63ab90d3697a8f1ffa322b2 role=test -->
## `def test_wildcard_method_matches(self)`

Asserts that `TestMatchXlinks.test_wildcard_method_matches` produces one edge when the call site method is `"*"` and the endpoint method is `"POST"`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_xlink:TestMatchXlinks.test_no_duplicates fingerprint=1c63c4636c4477f36c95dc1286aaceb5adc237e53157d5d514dee906aafe448b body_fp=8a51257aaba836fbd5eb3de699f6c70f278f110d7477665db0c0f62e8c88d924 source_ref=1e4c89db21789a50b63ab90d3697a8f1ffa322b2 role=test -->
## `def test_no_duplicates(self)`

Asserts that `match_xlinks` deduplicates results when two call sites with the same `src_qname` (but different frameworks) both match the same endpoint, producing exactly one ref.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_xlink:TestMatchXlinks.test_below_threshold_excluded fingerprint=68619e049b432a9904489cdfdc4f56a053097735fa20c80bf6beafd2c34346fb body_fp=6267189d9d36d836cf246b6bb79ea7be8f9bd69fb558616879ed94b6969117fd source_ref=1e4c89db21789a50b63ab90d3697a8f1ffa322b2 role=test -->
## `def test_below_threshold_excluded(self)`

Asserts that `TestMatchXlinks.match_xlinks` returns no edges when `threshold` exceeds the parameterized-match confidence score of 0.95.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_xlink:TestMatchXlinks.test_multiple_matches fingerprint=c11a604b8a7662b55d597f2980adece28ace3b74a12a0ac0764fa77d70e002c3 body_fp=be3708aaff3c9ef06d0321eb3b69109b20760c14344ecf2e181e7a784f601417 source_ref=1e4c89db21789a50b63ab90d3697a8f1ffa322b2 role=test -->
## `def test_multiple_matches(self)`

Asserts that `TestMatchXlinks` produces two distinct edges when two call sites each match a different endpoint by both URL and HTTP method.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_xlink:_make_xlink_project fingerprint=ef1b187609846804270a7487ee320ee43cdc5a59ab129060d0dd25b82e30bfb6 body_fp=8fc07719a3a54a14bc1ee1ee23efe32f5c61fdf4ebec3eb6267f8206033de7f4 source_ref=1e4c89db21789a50b63ab90d3697a8f1ffa322b2 role=test -->
## `def _make_xlink_project(tmp_path: Path) -> Path`

Create a temporary mini monorepo under `tmp_path` with a FastAPI Python backend (`api/users.py`) and a TypeScript fetch-based frontend (`src/client.ts`), returning `tmp_path`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_xlink:_scan fingerprint=02aa825501406c55a6abf16d9c5c7e4028d2ee0794e5c14f08ba2e960e706a01 body_fp=234f263229cc7217dd005c6cd3f5d60331876c35979221d61ef282d191de7d23 source_ref=1e4c89db21789a50b63ab90d3697a8f1ffa322b2 role=test -->
## `def _scan(project: Path) -> tuple[Store, object]`

Load config from `project`, open a `Store` at `project/.trie/graph.db`, run `scan_project`, and return `(store, result)`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_xlink:TestIntegration fingerprint=593769c9cd995bcdbb8cf9f6cc577434c74e62f4a1e4bf3e5f22b14802b1561e body_fp=14da204ec071911f7ff0a44e5b244428541fc8327e34d0ef14794c2f2eafc3ed source_ref=1e4c89db21789a50b63ab90d3697a8f1ffa322b2 role=test -->
## `class TestIntegration`

Integration test suite that runs full `scan_project()` against temporary monorepos and asserts cross-language edge correctness in the `Store`.

- `test_cross_language_edges_in_scan`: builds a TS/Python monorepo via `_make_xlink_project`, verifies exact, parameterized, and POST `references_in`/`references_out` edges.
- `test_method_mismatch_prevents_edge`: asserts a default-GET `fetch` call does **not** produce an edge to a `@app.post` handler.
- `test_no_cross_language_edges_for_single_language`: confirms pure-Python projects still produce same-language edges and incur zero xlink overhead.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_xlink:TestIntegration.test_cross_language_edges_in_scan fingerprint=e00a1d86df9090bb55faf7df68adeb7b9c6e0ca5ea7852151d8909f336a0aa49 body_fp=10b28374bcb46e105c5a9e45f92adaf6c1382c8b20738c9f454cf2a2d060df33 source_ref=1e4c89db21789a50b63ab90d3697a8f1ffa322b2 role=test -->
## `def test_cross_language_edges_in_scan(self, tmp_path: Path)`

Assert that a full `scan_project()` run on a mini monorepo produces `cross_language_call` edges visible through `Store.references_in` and `Store.references_out` for exact, parameterised, and method-specific matches.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_xlink:TestIntegration.test_method_mismatch_prevents_edge fingerprint=b224622b3e052917e22368e45458ad2fe5420d35b7994ae5edccee17271e9d6d body_fp=25f93ba809fa3b55a6f169cfc9b2507ea92a527fe8e2703af01d6e61f7dc823a source_ref=1e4c89db21789a50b63ab90d3697a8f1ffa322b2 role=test -->
## `def test_method_mismatch_prevents_edge(self, tmp_path: Path)`

Assert that a default-GET `fetch` call site does not produce a cross-language edge to a POST-only FastAPI endpoint after a full `scan_project()` run.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_xlink:TestIntegration.test_no_cross_language_edges_for_single_language fingerprint=98ba2084245052f3d80d4b5de6771531fb5ff2ef11f25b7a3c43d23c43308990 body_fp=87822cbe9a74f8b0f25ee6e19b2c916e644a3c24f74b9abc07e2b29a834c4d2b source_ref=1e4c89db21789a50b63ab90d3697a8f1ffa322b2 role=test -->
## `def test_no_cross_language_edges_for_single_language(self, tmp_path: Path)`

Asserts that a pure-Python project produces no xlink edges while same-language reference edges remain intact.

- Scans a two-file Python project (`lib.py` + `app.py`) with no TypeScript sources present.
- Verifies `store.references_out("app:run")` contains `"lib:helper"` (same-language edge unaffected).
- Verifies `result.edges_total >= 1`, confirming normal edges are still recorded.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_xlink:TestHubThresholdCascade fingerprint=9b1399cecc892c82ac82c6b03394c3d9d2a97f90734f7d3f5614ea44a7f00141 body_fp=c4430819c4f1c259c5c6a1a98880757cf99ff3fca738dd138b5dc790f96db69a source_ref=1e4c89db21789a50b63ab90d3697a8f1ffa322b2 role=test -->
## `class TestHubThresholdCascade`

Test class verifying that cross-language edges respect `hub_symbol_threshold` and halt cascade expansion at popular endpoints.

- `test_popular_endpoint_hits_hub_threshold`: builds a temp project with a single FastAPI `GET /api/popular` handler called by `hub_threshold + 3` (8) TS fetch callers, asserts all 8 xlink edges are stored, then calls `compute_cascade` with `changed_files={"api.py"}` and confirms `clients.ts` is absent from the affected set because `popular_handler`'s inbound count exceeds the hub threshold.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_xlink:TestHubThresholdCascade.test_popular_endpoint_hits_hub_threshold fingerprint=1ea1a4cf4998ac6b75813f711f94a6e447a9a47866842f60dc23c13e3cf410ed body_fp=1cf39e6e9c78808213ea64792a0bca8786093b37d6ee29b2ea585cc51430ccd9 source_ref=1e4c89db21789a50b63ab90d3697a8f1ffa322b2 role=test -->
## `def test_popular_endpoint_hits_hub_threshold(self, tmp_path: Path)`

Verify that a FastAPI endpoint with more cross-language callers than `hub_symbol_threshold` blocks `compute_cascade` from propagating to caller files.

- Writes a project with `hub_symbol_threshold=5` and 8 TS `fetch` callers targeting one FastAPI handler.
- Asserts all 8 cross-language edges are stored via `store.references_in`.
- Asserts `compute_cascade` includes `api.py` but excludes `clients.ts`, confirming hub cutoff.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_xlink:TestXLinkConfig fingerprint=f5f310b7e69ff57b3a66be421637c356823192106d599a1552aa99b7a518d9c1 body_fp=15bbf488558fc71c490d6af4e54488536d59ada0ed74a732bc2ffda08be9dbef source_ref=1e4c89db21789a50b63ab90d3697a8f1ffa322b2 role=test -->
## `class TestXLinkConfig`

Tests `Config` and `XLink` configuration behaviour for xlink settings.

- Asserts default `confidence_threshold` is `0.7` and `scan_paths` is empty.
- Asserts `Config.from_dict` correctly populates or defaults `xlink` fields.
- Asserts `XLink` instances are frozen (mutation raises `AttributeError`).
<!-- trie:end -->
<!-- trie:section symbol=tests/test_xlink:TestXLinkConfig.test_default_config fingerprint=12b419786ba609efd289b940fc244a55a0ce299da18ceedee487ee4c62433f8e body_fp=5e2b00502fb5465d90ea0650ff2287cf365e494c9c3fc50da9d3e32d59f8a505 source_ref=1e4c89db21789a50b63ab90d3697a8f1ffa322b2 role=test -->
## `def test_default_config(self)`

Asserts that a default `Config` instance sets `xlink.confidence_threshold` to `0.7` and `xlink.scan_paths` to an empty list.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_xlink:TestXLinkConfig.test_from_dict_with_xlink fingerprint=877a75451025fd74770aee1c68da6304830e255a02dc6d10096c2e61be508525 body_fp=664b7b4462fb3047dae9296a76935b5ccee234abbdc89cf46fe7e0a34a140d0c source_ref=1e4c89db21789a50b63ab90d3697a8f1ffa322b2 role=test -->
## `def test_from_dict_with_xlink(self)`

Asserts that `Config.from_dict` correctly populates `xlink.confidence_threshold` and `xlink.scan_paths` when an `xlink` section is present in the input dict.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_xlink:TestXLinkConfig.test_from_dict_without_xlink fingerprint=cdacb6ad93177af7a40da1c8ab9a30e6566e04056367a71a10ccd23f199d8b23 body_fp=47799422662c062c70ecc49cc34af9ac3f1e22701dd4365dc3880a3654a2b180 source_ref=1e4c89db21789a50b63ab90d3697a8f1ffa322b2 role=test -->
## `def test_from_dict_without_xlink(self)`

Asserts that `Config.from_dict` with an empty dict produces default `xlink` values: `confidence_threshold` of `0.7` and an empty `scan_paths` list.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_xlink:TestXLinkConfig.test_xlink_is_frozen fingerprint=91c1ebc9dbe853c80ccbf556af45955e5509abf6a95c15956e0e24749fd0f1f0 body_fp=3f13be410d83e49954efca9dce943b9c8b23013f5766076871ef2be76ad8854d source_ref=1e4c89db21789a50b63ab90d3697a8f1ffa322b2 role=test -->
## `def test_xlink_is_frozen(self)`

Asserts that `XLink` instances are immutable by verifying attribute assignment raises `AttributeError`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_xlink:TestEdgeKind fingerprint=45f439fdd0fa6ba5f58fa4a2e3bf59e35da5e7d97e4376805a139d4dc977f815 body_fp=6b89e3715330d6a5d482e3d8fb35e8f4d12d766f8abe94d3726f9a3b6dce3feb source_ref=1e4c89db21789a50b63ab90d3697a8f1ffa322b2 role=test -->
## `class TestEdgeKind`

Test class asserting that `"cross_language_call"` is registered in `trie.parse.types.EDGE_KINDS`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_xlink:TestEdgeKind.test_cross_language_call_in_edge_kinds fingerprint=000205084c2f7453c976187baaeab6e6a04a8ccd7e74be64ca068a65b9f6a49a body_fp=ee9706fad344190064c3f0da5a2117b3407691e6796f2f35fe2e23fe64b91eac source_ref=1e4c89db21789a50b63ab90d3697a8f1ffa322b2 role=test -->
## `def test_cross_language_call_in_edge_kinds(self)`

Assert that `"cross_language_call"` is registered in `EDGE_KINDS` from `trie.parse.types`.
<!-- trie:end -->