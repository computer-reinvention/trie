---
trie_version: 0.3.0
source: tests/test_parse_typescript.py
file_fingerprint: 7f31de0d9a1edc5a11457c615ceb409a97c9436be61c4787690547328daa9b33
last_synced_at: '2026-07-29T00:06:48Z'
defines:
- kind: module
  qualified_name: tests/test_parse_typescript:__module__
  lines: 1-103
- kind: constant
  qualified_name: tests/test_parse_typescript:FIXTURE
  lines: 7-7
- kind: function
  qualified_name: tests/test_parse_typescript:_by_qname
  lines: 10-11
  signature: def _by_qname(symbols)
- kind: function
  qualified_name: tests/test_parse_typescript:test_function_and_const_kinds
  lines: 14-23
  signature: def test_function_and_const_kinds()
- kind: function
  qualified_name: tests/test_parse_typescript:test_jsdoc_becomes_docstring
  lines: 26-28
  signature: def test_jsdoc_becomes_docstring()
- kind: function
  qualified_name: tests/test_parse_typescript:test_class_method_property_kinds
  lines: 31-37
  signature: def test_class_method_property_kinds()
- kind: function
  qualified_name: tests/test_parse_typescript:test_interface_type_enum_kinds
  lines: 40-44
  signature: def test_interface_type_enum_kinds()
- kind: function
  qualified_name: tests/test_parse_typescript:test_enum_members_are_child_symbols
  lines: 47-52
  signature: def test_enum_members_are_child_symbols()
- kind: function
  qualified_name: tests/test_parse_typescript:test_dts_ambient_module_keyed_by_name
  lines: 55-66
  signature: def test_dts_ambient_module_keyed_by_name()
- kind: function
  qualified_name: tests/test_parse_typescript:test_tsx_parses
  lines: 69-77
  signature: def test_tsx_parses()
- kind: function
  qualified_name: tests/test_parse_typescript:test_fingerprint_stable_under_comment_change
  lines: 80-93
  signature: def test_fingerprint_stable_under_comment_change()
- kind: function
  qualified_name: tests/test_parse_typescript:test_empty_source_yields_no_symbols
  lines: 96-102
  signature: def test_empty_source_yields_no_symbols()
incoming_refs: 0
outgoing_refs: 9
---
<!-- trie:section symbol=tests/test_parse_typescript:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=5db8485018340352131850138b6095948dd5d2be561a756e4990aaa896fcefb5 source_ref=e20092bcb48b66edd6fadbd653a95c44c158802e role=test -->
Tests for `trie.parse.typescript.extract_symbols`, covering symbol kinds, docstrings, enum members, ambient `.d.ts` modules, TSX parsing, fingerprint stability, and empty-source edge cases.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_typescript:FIXTURE fingerprint=883b5996900536d76bf6d49f99ed1a35468676b2f050a082d65e4eb092ae406f body_fp=bd613815845213d8316eed2f29d3698be9e16ed59cd7dcff264aac3b9215b37e source_ref=e20092bcb48b66edd6fadbd653a95c44c158802e role=test -->
Absolute `Path` to the `tiny_ts_repo` fixture directory used by all tests in this module.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_typescript:_by_qname fingerprint=525ffb89263a0d6f267e3e833b93ecabb14d423ac67237ffca20826dfc546e89 body_fp=b30e17402ff99336a6012ca051f24aa1ec1c856286f156963eff2ebae4828b14 source_ref=e20092bcb48b66edd6fadbd653a95c44c158802e role=util -->
## `def _by_qname(symbols)`

Index a list of symbols by their `qualified_name` for fast lookup in tests.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_typescript:test_function_and_const_kinds fingerprint=727b65c044d6a6b473974e3034b2c9cd1c3c214f580df90cb5375b91b33a2a7d body_fp=cc8392de00780823a5e25f6066637c9c56fe78447fea21f10718d0e0560be3d5 source_ref=e20092bcb48b66edd6fadbd653a95c44c158802e role=test -->
## `def test_function_and_const_kinds()`

Verify that exported/unexported functions set `is_public` correctly and that plain vs. arrow `const` declarations produce `constant` vs. `function` kinds.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_typescript:test_jsdoc_becomes_docstring fingerprint=a02704aea2b2d4583ad30f3e29674d1c189e27e137f705457542eed80435809d body_fp=192e5773433a2b13069f2aff26c3309edf6473c123632f1ea72458f0989f68c6 source_ref=e20092bcb48b66edd6fadbd653a95c44c158802e role=test -->
## `def test_jsdoc_becomes_docstring()`

Assert that a JSDoc comment on a TypeScript function is captured as the symbol's `docstring` field.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_typescript:test_class_method_property_kinds fingerprint=6fd08890771750fcc1f8dffaa1d25971accedd8ccbf6ae0512be3a3e111a322b body_fp=872db9f104c6914f2a0d9c31a1d1a7247fa6d1c2b79f934763d3adebe3bf52dd source_ref=e20092bcb48b66edd6fadbd653a95c44c158802e role=test -->
## `def test_class_method_property_kinds()`

Verify that `extract_symbols` correctly classifies a class, its property, and its method, and sets `parent_class` accordingly.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_typescript:test_interface_type_enum_kinds fingerprint=48cec13c21a84f3d34207df006662c46e9a3d9c91477757a3dd7ca90110bd7f5 body_fp=c6ffed94d711e5604813a854be4370208ed6fc05921028fba6c32fc7c48da825 source_ref=e20092bcb48b66edd6fadbd653a95c44c158802e role=test -->
## `def test_interface_type_enum_kinds()`

Assert that interface, type alias, and enum declarations in `base.ts` are assigned the correct `kind` values.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_typescript:test_enum_members_are_child_symbols fingerprint=26ffeb527aa0997f83ce3d87fc9e628879693b68f95c88817ca703e0f82ac4b1 body_fp=0bbaf0746301b4285f7f615820e7bac699d8bf07ad6964b8cf4261e7d6abd92b source_ref=e20092bcb48b66edd6fadbd653a95c44c158802e role=test -->
## `def test_enum_members_are_child_symbols()`

Verify that enum members in `base.ts` are extracted as `enum_member` symbols with correct `parent_class`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_typescript:test_dts_ambient_module_keyed_by_name fingerprint=ef270c20f11611334d49592611744691c701ac6914408cccffaf7c8bbf807ef3 body_fp=7af7f4bc557838ea9e18b69c3bedd35d14f5b54b72e015e8c60a6e75aced0a89 source_ref=e20092bcb48b66edd6fadbd653a95c44c158802e role=test -->
## `def test_dts_ambient_module_keyed_by_name()`

Verify that symbols extracted from a `.d.ts` ambient module declaration are keyed by the module's literal name, with inner declarations and bare `declare const` attributed correctly.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_typescript:test_tsx_parses fingerprint=bca21508cc2c0e5de0616f3520cf36858ef39615ec3579baf0cceb65566e6e8b body_fp=7e138a28ae12da3a256b324eb8ba29e97264b2dbb4bebeb7dbddd2df8cc652a1 source_ref=e20092bcb48b66edd6fadbd653a95c44c158802e role=test -->
## `def test_tsx_parses()`

Verify that `extract_symbols` correctly parses a `.tsx` file and classifies an arrow-const export as a `function` kind.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_typescript:test_fingerprint_stable_under_comment_change fingerprint=e74110121f031014dda971a6c319fab1095c702e8502b61b9cc90f6bc20a4aad body_fp=55f5dd5a763f1bea3ff1208ec8ee903436f446e220aca133f528c1ab635d17ec source_ref=e20092bcb48b66edd6fadbd653a95c44c158802e role=test -->
## `def test_fingerprint_stable_under_comment_change()`

Assert that `body_normalized_hash` is identical for the same function with and without inline comments.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_typescript:test_empty_source_yields_no_symbols fingerprint=9a70f1408da8f91808684a362084d0319d6ec38ddcb79243a5ad50e2a4b601fd body_fp=af36481bb843f75dc1c54b5c6a78172f19f75774f3bb1f0fdecbb4fc7a7d026b source_ref=e20092bcb48b66edd6fadbd653a95c44c158802e role=test -->
## `def test_empty_source_yields_no_symbols()`

Assert that `extract_symbols` returns an empty list for a TypeScript file with no source content.
<!-- trie:end -->