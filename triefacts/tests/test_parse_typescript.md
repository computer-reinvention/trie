---
trie_version: 0.1.9
source: tests/test_parse_typescript.py
file_fingerprint: 7f31de0d9a1edc5a11457c615ceb409a97c9436be61c4787690547328daa9b33
last_synced_at: '2026-07-28T23:34:34Z'
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
- kind: function
  qualified_name: tests/test_parse_typescript:test_function_and_const_kinds
  lines: 14-23
- kind: function
  qualified_name: tests/test_parse_typescript:test_jsdoc_becomes_docstring
  lines: 26-28
- kind: function
  qualified_name: tests/test_parse_typescript:test_class_method_property_kinds
  lines: 31-37
- kind: function
  qualified_name: tests/test_parse_typescript:test_interface_type_enum_kinds
  lines: 40-44
- kind: function
  qualified_name: tests/test_parse_typescript:test_enum_members_are_child_symbols
  lines: 47-52
- kind: function
  qualified_name: tests/test_parse_typescript:test_dts_ambient_module_keyed_by_name
  lines: 55-66
- kind: function
  qualified_name: tests/test_parse_typescript:test_tsx_parses
  lines: 69-77
- kind: function
  qualified_name: tests/test_parse_typescript:test_fingerprint_stable_under_comment_change
  lines: 80-93
- kind: function
  qualified_name: tests/test_parse_typescript:test_empty_source_yields_no_symbols
  lines: 96-102
incoming_refs: 0
outgoing_refs: 9
---
<!-- trie:section symbol=tests/test_parse_typescript:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=5db8485018340352131850138b6095948dd5d2be561a756e4990aaa896fcefb5 source_ref=e20092bcb48b66edd6fadbd653a95c44c158802e role=test -->
Tests for `trie.parse.typescript.extract_symbols`, covering symbol kinds, docstrings, enum members, ambient `.d.ts` modules, TSX parsing, fingerprint stability, and empty-source edge cases.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_typescript:FIXTURE fingerprint=883b5996900536d76bf6d49f99ed1a35468676b2f050a082d65e4eb092ae406f body_fp=bd613815845213d8316eed2f29d3698be9e16ed59cd7dcff264aac3b9215b37e source_ref=e20092bcb48b66edd6fadbd653a95c44c158802e role=test -->
Absolute `Path` to the `tiny_ts_repo` fixture directory used by all tests in this module.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_typescript:_by_qname fingerprint=525ffb89263a0d6f267e3e833b93ecabb14d423ac67237ffca20826dfc546e89 body_fp=1fea8a987e258597efbbf781330a2af982084c1203ce7ff1289481ad42fffa5b source_ref=e20092bcb48b66edd6fadbd653a95c44c158802e role=util -->
Index a list of symbols by their `qualified_name` for fast lookup in tests.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_typescript:test_function_and_const_kinds fingerprint=727b65c044d6a6b473974e3034b2c9cd1c3c214f580df90cb5375b91b33a2a7d body_fp=755b4bd898c1cfb2413119db1a0541079722904d53661685aed48f43baaa0769 source_ref=e20092bcb48b66edd6fadbd653a95c44c158802e role=test -->
Verify that exported/unexported functions set `is_public` correctly and that plain vs. arrow `const` declarations produce `constant` vs. `function` kinds.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_typescript:test_jsdoc_becomes_docstring fingerprint=a02704aea2b2d4583ad30f3e29674d1c189e27e137f705457542eed80435809d body_fp=b2814072ee59448b8bf7e8e358a2fc713cddb3ae6f24c2ae294fb81117bcbe34 source_ref=e20092bcb48b66edd6fadbd653a95c44c158802e role=test -->
Assert that a JSDoc comment on a TypeScript function is captured as the symbol's `docstring` field.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_typescript:test_class_method_property_kinds fingerprint=6fd08890771750fcc1f8dffaa1d25971accedd8ccbf6ae0512be3a3e111a322b body_fp=a67eb034bf6601d0deb064c1641a3d21535c6d23bc205f661c74d0b9e573b082 source_ref=e20092bcb48b66edd6fadbd653a95c44c158802e role=test -->
Verify that `extract_symbols` correctly classifies a class, its property, and its method, and sets `parent_class` accordingly.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_typescript:test_interface_type_enum_kinds fingerprint=48cec13c21a84f3d34207df006662c46e9a3d9c91477757a3dd7ca90110bd7f5 body_fp=5b085ecc6c7d2b7a41616b09170480613756b4acee71e9d97e20d5260d30aa72 source_ref=e20092bcb48b66edd6fadbd653a95c44c158802e role=test -->
Assert that interface, type alias, and enum declarations in `base.ts` are assigned the correct `kind` values.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_typescript:test_enum_members_are_child_symbols fingerprint=26ffeb527aa0997f83ce3d87fc9e628879693b68f95c88817ca703e0f82ac4b1 body_fp=a6ad83964c70dd309450084c44e1cae487080de48d8efbc5d009ea79365f679a source_ref=e20092bcb48b66edd6fadbd653a95c44c158802e role=test -->
Verify that enum members in `base.ts` are extracted as `enum_member` symbols with correct `parent_class`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_typescript:test_dts_ambient_module_keyed_by_name fingerprint=ef270c20f11611334d49592611744691c701ac6914408cccffaf7c8bbf807ef3 body_fp=18768ef0f63cab5d2b14475faa658e9d4e4d872b9bf87ab14518930f1e2ac87b source_ref=e20092bcb48b66edd6fadbd653a95c44c158802e role=test -->
Verify that symbols extracted from a `.d.ts` ambient module declaration are keyed by the module's literal name, with inner declarations and bare `declare const` attributed correctly.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_typescript:test_tsx_parses fingerprint=bca21508cc2c0e5de0616f3520cf36858ef39615ec3579baf0cceb65566e6e8b body_fp=2e14163de6928b7a95e928aed569bfa0e9beb23ce3eb9f22faca491893eb1a68 source_ref=e20092bcb48b66edd6fadbd653a95c44c158802e role=test -->
Verify that `extract_symbols` correctly parses a `.tsx` file and classifies an arrow-const export as a `function` kind.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_typescript:test_fingerprint_stable_under_comment_change fingerprint=e74110121f031014dda971a6c319fab1095c702e8502b61b9cc90f6bc20a4aad body_fp=09582527fc48d1d00ba8a81a86c226df4abc2c8cf7772beb30ffca8a4902dfd4 source_ref=e20092bcb48b66edd6fadbd653a95c44c158802e role=test -->
Assert that `body_normalized_hash` is identical for the same function with and without inline comments.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_typescript:test_empty_source_yields_no_symbols fingerprint=9a70f1408da8f91808684a362084d0319d6ec38ddcb79243a5ad50e2a4b601fd body_fp=39e0d3bfb1f9b0596eed22fbf5634be670cb748ca3d3fc6af33c2f475d8323da source_ref=e20092bcb48b66edd6fadbd653a95c44c158802e role=test -->
Assert that `extract_symbols` returns an empty list for a TypeScript file with no source content.
<!-- trie:end -->