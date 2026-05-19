---
trie_version: 0.1.2
source: tests/test_generator.py
file_fingerprint: dbef242b0f1cc34b984a3dbda4ad2f44f44ee8dbaf7414679e5fbad7f1319677
last_synced_at: '2026-05-19T10:38:03Z'
defines:
- kind: module
  qualified_name: tests/test_generator:__module__
  lines: 1-200
- kind: class
  qualified_name: tests/test_generator:FakeClient
  lines: 22-37
- kind: method
  qualified_name: tests/test_generator:FakeClient.generate
  lines: 29-37
- kind: function
  qualified_name: tests/test_generator:test_cached_context_includes_source_and_filename
  lines: 40-45
- kind: function
  qualified_name: tests/test_generator:test_request_names_symbol_and_lines
  lines: 48-55
- kind: function
  qualified_name: tests/test_generator:test_generate_section_passes_correct_prompt
  lines: 58-74
- kind: function
  qualified_name: tests/test_generator:test_generate_section_strips_surrounding_whitespace
  lines: 77-85
- kind: function
  qualified_name: tests/test_generator:test_generate_section_defaults_to_cold_mode
  lines: 91-105
- kind: function
  qualified_name: tests/test_generator:test_generate_section_takes_diff_aware_when_both_previous_provided
  lines: 108-133
- kind: function
  qualified_name: tests/test_generator:test_generate_section_partial_previous_falls_back_to_cold
  lines: 136-153
- kind: function
  qualified_name: tests/test_generator:test_diff_aware_request_carries_cosmetic_preserve_instruction
  lines: 156-175
- kind: function
  qualified_name: tests/test_generator:test_make_client_rejects_unknown_provider
  lines: 178-180
- kind: function
  qualified_name: tests/test_generator:test_make_client_requires_provider_prefix
  lines: 183-185
- kind: function
  qualified_name: tests/test_generator:test_make_client_anthropic_constructs
  lines: 188-199
incoming_refs: 0
outgoing_refs: 27
---
<!-- trie:section symbol=tests/test_generator:FakeClient fingerprint=ebec988fe34a3959e1dc4041622df9100811f16c13ee31cd51550585e35d2deb body_fp=74530d2aba79774fff56d45877b77496f7a72fc5d13b88903bf93929185fba25 source_ref=eeeca93821a9947c85cab65d8b6299b8fa518f6f -->
## `FakeClient`

Test double that records the last `GenerationRequest` and returns a canned `GenerationResponse`.

- `response_text`: default Markdown body returned by `generate`.
- `last_request`: populated on each `generate` call for assertion in tests.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_generator:FakeClient.generate fingerprint=42d29f746c846f08569316c39868e14083913bde3de32fbf80aea806431cee3a body_fp=a3eb9ca7beb24153a300b50cda44a264c032ecc7dee0b71ab59a8837eb139405 source_ref=eeeca93821a9947c85cab65d8b6299b8fa518f6f -->
## `generate(self, req: GenerationRequest) -> GenerationResponse`

Record the request and return a canned `GenerationResponse` with fixed token counts.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_generator:test_cached_context_includes_source_and_filename fingerprint=05c2240c12cb32e9582df345efbc8008b1869ef148587ed7d624e7dec18248ff body_fp=10652a150e475f8d02f4d1ada0514c8db5a4cf0d9d2c3b5c307dcfc1bf852634 source_ref=eeeca93821a9947c85cab65d8b6299b8fa518f6f -->
## `test_cached_context_includes_source_and_filename()`

Assert that `build_cached_context` embeds the file path and source code in a Python fenced block.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_generator:test_request_names_symbol_and_lines fingerprint=abfebb44b13552570306f37907d56c0e6acd08c47016a54dda802ef88ba398b4 body_fp=b86489d1da21bf01617b5aa870fec6b626f5fd7ea69a8f829eb0e4cbea9dea57 source_ref=eeeca93821a9947c85cab65d8b6299b8fa518f6f -->
## `test_request_names_symbol_and_lines(tmp_path: Path)`

Assert that `_build_request` output includes the symbol's qualified name, kind, and line references.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_generator:test_generate_section_passes_correct_prompt fingerprint=795a74eedf9662289e987121ee0a7ceaf9d5554910b2acadc3934d7556b5cfb2 body_fp=c0e56e0724312192a5a6b8ff70a49bd1e8614e2c053a94f363dfd54800faefed source_ref=eeeca93821a9947c85cab65d8b6299b8fa518f6f -->
## `test_generate_section_passes_correct_prompt(tmp_path: Path)`

Verify that `generate_section` sends the correct system prompt, cached context, and request text, and returns a properly populated section.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_generator:test_generate_section_strips_surrounding_whitespace fingerprint=3bd204788338622df5251a6832f74b175b6480c415c0f2fdd8185cf4a015a702 body_fp=4705ceb63b5c49a590426da6f78c16134bb47cd8eda85addb0c2f58bb9128108 source_ref=eeeca93821a9947c85cab65d8b6299b8fa518f6f -->
## `test_generate_section_strips_surrounding_whitespace(tmp_path: Path)`

Verify that `generate_section` strips leading and trailing whitespace from the model response body.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_generator:test_make_client_rejects_unknown_provider fingerprint=f872f29b5c63a1e81c80c37abf32fe8bb20662ff5ee60dcd7b0817015d657eef body_fp=a095f2fb142874717d69b3bac4b6c4ce54abed5cde4262ca8938af5c6743ab31 source_ref=eeeca93821a9947c85cab65d8b6299b8fa518f6f -->
## `test_make_client_rejects_unknown_provider()`

Assert that `make_client` raises `NotImplementedError` for an unrecognised provider prefix.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_generator:test_make_client_requires_provider_prefix fingerprint=df2b5275115453c8315d3057c0b82e0ee7f1cedc1b60219fc1624984efb88cda body_fp=85a0e13f0cc2b4206ba96968830e3cdcb939062a9e9d128ffa1c4fcfe3480bd9 source_ref=eeeca93821a9947c85cab65d8b6299b8fa518f6f -->
## `test_make_client_requires_provider_prefix()`

Assert `make_client` raises `ValueError` when given a model string without a provider prefix.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_generator:test_make_client_anthropic_constructs fingerprint=abb7663559910baa08ced366ecfdf3a45b7765fa1724004772179456482b1b31 body_fp=0acad8fdf05c348c0f0bd375a079c4a1c8a854ede75b712451f04b1c8b6de9fa source_ref=eeeca93821a9947c85cab65d8b6299b8fa518f6f -->
## `test_make_client_anthropic_constructs(monkeypatch: pytest.MonkeyPatch)`

Verify that `make_client` with an Anthropic prefix constructs the SDK client and propagates the model ID correctly.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_generator:test_generate_section_defaults_to_cold_mode fingerprint=1586ca05e09be0e3d19dacd1eee74a3f1651f6da563b0153a2db9d1fb49a2cac body_fp=eeba0526efb61f1c96c74649a3bd8fcad950f2cbd07577a7fc85ca81fbc266ad source_ref=eeeca93821a9947c85cab65d8b6299b8fa518f6f -->
## `test_generate_section_defaults_to_cold_mode(tmp_path: Path)`

Assert that `generate_section` sets `mode == "cold"` and omits diff-aware blocks when no previous data is supplied.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_generator:test_generate_section_takes_diff_aware_when_both_previous_provided fingerprint=a2536c30f982eb42aa8d6453cd210febc16a749d8be271026de0eb0f9cfbca03 body_fp=bb9385e07495c6e97854daf9f0541c1b504970513fa320711cfff9b4cfe079ff source_ref=eeeca93821a9947c85cab65d8b6299b8fa518f6f -->
## `test_generate_section_takes_diff_aware_when_both_previous_provided(tmp_path: Path)`

Assert that supplying both `previous_source` and `previous_prose` produces a diff-aware request with `mode == "diff_aware"` and all expected XML blocks.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_generator:test_generate_section_partial_previous_falls_back_to_cold fingerprint=bae0eee8799c408516e32b3602c833564d121d2f6cbf84724790e3c67c875667 body_fp=32c8e7b5bf9163b190705681431217acb97e81f4a1244bf09a36a5a921e1aac4 source_ref=eeeca93821a9947c85cab65d8b6299b8fa518f6f -->
## `test_generate_section_partial_previous_falls_back_to_cold(tmp_path: Path)`

Assert that supplying only one of `previous_source` or `previous_prose` produces `mode == "cold"`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_generator:test_diff_aware_request_carries_cosmetic_preserve_instruction fingerprint=2f77db8c1c0293285179dac96d981c5008e2f5bfa87b0422f3153973b351c588 body_fp=598ae565edf7b11c051ab7d68e867a4e5bedbd7580247320b586a97d1a820f0d source_ref=eeeca93821a9947c85cab65d8b6299b8fa518f6f -->
## `test_diff_aware_request_carries_cosmetic_preserve_instruction(tmp_path: Path)`

Assert that the diff-aware request rubric contains cosmetic-preserve and verbatim language.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_generator:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=fdf460c25a8f7c55eb275cc7c1c71b40023012e1783d6e9b6f544d0902768c39 source_ref=eeeca93821a9947c85cab65d8b6299b8fa518f6f -->
## `tests/test_generator`

Test suite for `trie.sync.generator` covering prompt construction, diff-aware mode, cold mode fallback, and model client factory.
<!-- trie:end -->