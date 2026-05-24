---
trie_version: 0.1.2
source: tests/test_generator.py
file_fingerprint: 1c349858cb1cd8641a0ac04802fe6caf6e818b2161049f3fc584a81cbaaf7bd5
last_synced_at: '2026-05-23T23:49:46Z'
defines:
- kind: module
  qualified_name: tests/test_generator:__module__
  lines: 1-263
- kind: class
  qualified_name: tests/test_generator:FakeClient
  lines: 24-39
- kind: method
  qualified_name: tests/test_generator:FakeClient.generate
  lines: 31-39
- kind: function
  qualified_name: tests/test_generator:test_cached_context_includes_source_and_filename
  lines: 42-47
- kind: function
  qualified_name: tests/test_generator:test_request_names_symbol_and_lines
  lines: 50-60
- kind: function
  qualified_name: tests/test_generator:test_generate_section_passes_correct_prompt
  lines: 63-79
- kind: function
  qualified_name: tests/test_generator:test_generate_section_strips_surrounding_whitespace
  lines: 82-90
- kind: function
  qualified_name: tests/test_generator:test_generate_section_defaults_to_cold_mode
  lines: 96-112
- kind: function
  qualified_name: tests/test_generator:test_generate_section_takes_diff_aware_when_both_previous_provided
  lines: 115-140
- kind: function
  qualified_name: tests/test_generator:test_generate_section_partial_previous_falls_back_to_cold
  lines: 143-160
- kind: function
  qualified_name: tests/test_generator:test_diff_aware_request_carries_cosmetic_preserve_instruction
  lines: 163-182
- kind: function
  qualified_name: tests/test_generator:test_symbol_context_clause_plain_method
  lines: 188-194
- kind: function
  qualified_name: tests/test_generator:test_symbol_context_clause_property
  lines: 197-203
- kind: function
  qualified_name: tests/test_generator:test_symbol_context_clause_classmethod
  lines: 206-212
- kind: function
  qualified_name: tests/test_generator:test_symbol_context_clause_plain_function
  lines: 215-220
- kind: function
  qualified_name: tests/test_generator:test_symbol_source_includes_decorators
  lines: 223-229
- kind: function
  qualified_name: tests/test_generator:test_request_method_names_class
  lines: 232-238
- kind: function
  qualified_name: tests/test_generator:test_make_client_rejects_unknown_provider
  lines: 241-243
- kind: function
  qualified_name: tests/test_generator:test_make_client_requires_provider_prefix
  lines: 246-248
- kind: function
  qualified_name: tests/test_generator:test_make_client_anthropic_constructs
  lines: 251-262
incoming_refs: 0
outgoing_refs: 41
---
<!-- trie:section symbol=tests/test_generator:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=eaad7292f020c0af04054a66d3b9ef285c5da761b1adc7d70f65fe8d403b2429 source_ref=c80f563c9f68629703e12e4a8bf14c857da4393c -->
## `tests/test_generator`

Tests for `trie.sync.generator` covering cold and diff-aware generation, prompt shape, symbol context clauses, and `make_client` validation.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_generator:FakeClient fingerprint=ebec988fe34a3959e1dc4041622df9100811f16c13ee31cd51550585e35d2deb body_fp=91ef08882c8a53ff1468ba4ac7b2599e4fca8225aa2d52c733a0dbfbf90dd293 source_ref=c80f563c9f68629703e12e4a8bf14c857da4393c -->
## `FakeClient`

Test double that records the last `GenerationRequest` and returns a fixed `GenerationResponse`.

- `response_text`: canned markdown returned by `generate`; override to test stripping logic
- `last_request`: populated on each `generate` call; inspect to assert prompt contents
<!-- trie:end -->
<!-- trie:section symbol=tests/test_generator:FakeClient.generate fingerprint=42d29f746c846f08569316c39868e14083913bde3de32fbf80aea806431cee3a body_fp=d95df2b2c7ac02fab2b15eb6e527bd80e7cb69962879c5af5f8d50b3c98d9eb2 source_ref=c80f563c9f68629703e12e4a8bf14c857da4393c -->
## `FakeClient.generate(self, req: GenerationRequest) -> GenerationResponse`

Record the request on `FakeClient.last_request` and return a canned `GenerationResponse` with fixed token counts.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_generator:test_cached_context_includes_source_and_filename fingerprint=05c2240c12cb32e9582df345efbc8008b1869ef148587ed7d624e7dec18248ff body_fp=f365d5283eacec035bf0a6ae124b59826c7b4c99781cc81d2c015f8d3e5e40cd source_ref=c80f563c9f68629703e12e4a8bf14c857da4393c -->
## `test_cached_context_includes_source_and_filename()`

Assert that `build_cached_context` output contains the filename, source code, and a Python code fence.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_generator:test_request_names_symbol_and_lines fingerprint=46f5a49f9a778751dd3ad6e1c627422cef153e52157f668a1eaef9188feb2cdd body_fp=520552e795e20583d91bc63b35414844944a801a18b351c99c764b7e9974bbe9 source_ref=c80f563c9f68629703e12e4a8bf14c857da4393c -->
## `test_request_names_symbol_and_lines(tmp_path: Path)`

Assert that `_build_request` output includes the symbol's qualified name, kind, line range, and source block.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_generator:test_generate_section_passes_correct_prompt fingerprint=795a74eedf9662289e987121ee0a7ceaf9d5554910b2acadc3934d7556b5cfb2 body_fp=5974728f174c989c998229a3778a5082599dd4d72c70edf8364d544b4b5af48c source_ref=c80f563c9f68629703e12e4a8bf14c857da4393c -->
## `test_generate_section_passes_correct_prompt(tmp_path: Path)`

Verify `generate_section` sends the correct system prompt, cached context, request body, and returns a properly populated section with token counts.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_generator:test_generate_section_strips_surrounding_whitespace fingerprint=3bd204788338622df5251a6832f74b175b6480c415c0f2fdd8185cf4a015a702 body_fp=fe0ab25771251b420a845daae3b515a43637efe4856b156a254c678db4772a00 source_ref=c80f563c9f68629703e12e4a8bf14c857da4393c -->
## `test_generate_section_strips_surrounding_whitespace(tmp_path: Path)`

Assert that `generate_section` strips leading and trailing whitespace from the model response before storing it in `sec.body`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_generator:test_generate_section_defaults_to_cold_mode fingerprint=454aec60eb91bd0f24db44120768d8c3dfd3b7863cdff0f6465af7e6ff1da97f body_fp=eb7214ab769ab58fe23d7b20f5f19b5e61c0da2c766dfa36b62d37101aac72a8 source_ref=c80f563c9f68629703e12e4a8bf14c857da4393c -->
## `test_generate_section_defaults_to_cold_mode(tmp_path: Path)`

Assert that `generate_section` uses cold mode and omits diff-aware blocks when no previous context is supplied.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_generator:test_generate_section_takes_diff_aware_when_both_previous_provided fingerprint=a2536c30f982eb42aa8d6453cd210febc16a749d8be271026de0eb0f9cfbca03 body_fp=5cb9433fd33de571cd1b6e24263487e500038418df7bc972300dc8baa02ba916 source_ref=c80f563c9f68629703e12e4a8bf14c857da4393c -->
## `test_generate_section_takes_diff_aware_when_both_previous_provided(tmp_path: Path)`

Assert that supplying both `previous_source` and `previous_prose` to `generate_section` produces a `diff_aware` mode section with all expected diff blocks in the request.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_generator:test_generate_section_partial_previous_falls_back_to_cold fingerprint=bae0eee8799c408516e32b3602c833564d121d2f6cbf84724790e3c67c875667 body_fp=e208fc57466024ea6b044940fb1e598512983485adcee4600f041e8cf9644a08 source_ref=c80f563c9f68629703e12e4a8bf14c857da4393c -->
## `test_generate_section_partial_previous_falls_back_to_cold(tmp_path: Path)`

Assert that supplying only one of `previous_source` or `previous_prose` to `generate_section` produces `mode == "cold"`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_generator:test_diff_aware_request_carries_cosmetic_preserve_instruction fingerprint=2f77db8c1c0293285179dac96d981c5008e2f5bfa87b0422f3153973b351c588 body_fp=9a72431e244ea92848fbd47dc01c59eff25e98cd84bef68142e849e9a410da1b source_ref=c80f563c9f68629703e12e4a8bf14c857da4393c -->
## `test_diff_aware_request_carries_cosmetic_preserve_instruction(tmp_path: Path)`

Assert that `_build_diff_aware_request` output contains rubric language instructing the model to preserve prose verbatim on cosmetic-only source changes.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_generator:test_symbol_context_clause_plain_method fingerprint=fb374e775dbfaa4a45b8ef03d0bcef7b7659492868d1b0c0a4b5844fd81afb2e body_fp=44282634fd0690b7c983a993136762587303871ccfe8cdea1f6fbf92eed2fe7f source_ref=c80f563c9f68629703e12e4a8bf14c857da4393c -->
## `test_symbol_context_clause_plain_method(tmp_path: Path)`

Assert that `_symbol_context_clause` returns a string containing "method of class" and the owner class name for a plain method.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_generator:test_symbol_context_clause_property fingerprint=54d6de47c6e3e96927aded1f337c8609b132e0ff32468650056208220ce821aa body_fp=5c3f9e194e2a3f787f9e1f7a88b68b8a714c046b3f2d66ea728a3d4403296d90 source_ref=c80f563c9f68629703e12e4a8bf14c857da4393c -->
## `test_symbol_context_clause_property(tmp_path: Path)`

Assert that `_symbol_context_clause` includes `@property` and the owning class name for a property symbol.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_generator:test_symbol_context_clause_classmethod fingerprint=22c5653e80c176ddd79ab74b097bfa31301b8f956e51d99a7cae3bf9bb716088 body_fp=3492b378164bd2c949e4b8a5794bd73fa27b23f5b695095b83a16cbc2dbbc518 source_ref=c80f563c9f68629703e12e4a8bf14c857da4393c -->
## `test_symbol_context_clause_classmethod(tmp_path: Path)`

Assert that `_symbol_context_clause` includes `@classmethod` and the owning class name for a classmethod symbol.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_generator:test_symbol_context_clause_plain_function fingerprint=301be51f4a461e6280ed29118dfa342dff9dec1e27b548d9c44088a95337524e body_fp=acff6aee8795d4c1b7425f0624a93bd4b010dc2da6e150ed99d01e735793dd06 source_ref=c80f563c9f68629703e12e4a8bf14c857da4393c -->
## `test_symbol_context_clause_plain_function(tmp_path: Path)`

Assert that `_symbol_context_clause` returns exactly `"a function"` for a module-level function symbol.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_generator:test_symbol_source_includes_decorators fingerprint=91be4a2f56d4f3e58d93eaac26ce271547aa6630b0e321f2db96ea0e1ff512fb body_fp=0018ba8c282bfa5547794973b77df488d8a9503e85a64aae461c96572047c758 source_ref=c80f563c9f68629703e12e4a8bf14c857da4393c -->
## `test_symbol_source_includes_decorators(tmp_path: Path)`

Assert that `_symbol_source` returns source text containing the decorator and `def` line for a `@property` method.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_generator:test_request_method_names_class fingerprint=dc93e64d498ea570690659e840492adff12ccee49a5f51c50248b1b5238d139a body_fp=5a22dab9ef6aef96492f7263d299ab45fb335028cd731927be919f355d8cf1e3 source_ref=c80f563c9f68629703e12e4a8bf14c857da4393c -->
## `test_request_method_names_class(tmp_path: Path)`

Assert that `_build_request` includes the owning class name and the word "method" for a class method symbol.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_generator:test_make_client_rejects_unknown_provider fingerprint=f872f29b5c63a1e81c80c37abf32fe8bb20662ff5ee60dcd7b0817015d657eef body_fp=a095f2fb142874717d69b3bac4b6c4ce54abed5cde4262ca8938af5c6743ab31 source_ref=c80f563c9f68629703e12e4a8bf14c857da4393c -->
## `test_make_client_rejects_unknown_provider()`

Assert that `make_client` raises `NotImplementedError` for an unrecognised provider prefix.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_generator:test_make_client_requires_provider_prefix fingerprint=df2b5275115453c8315d3057c0b82e0ee7f1cedc1b60219fc1624984efb88cda body_fp=f9dbac98d75ff20a7a0a66bbd75f7e32bfd04665daaa91125544d51d9b3f2678 source_ref=c80f563c9f68629703e12e4a8bf14c857da4393c -->
## `test_make_client_requires_provider_prefix()`

Assert that `make_client` raises `ValueError` when given a model string without a `provider/` prefix.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_generator:test_make_client_anthropic_constructs fingerprint=abb7663559910baa08ced366ecfdf3a45b7765fa1724004772179456482b1b31 body_fp=49fbdda949bc06d7772494b62d50083cfb24e401d158f9754c3e6e463628f97f source_ref=c80f563c9f68629703e12e4a8bf14c857da4393c -->
## `test_make_client_anthropic_constructs(monkeypatch: pytest.MonkeyPatch)`

Verify that `make_client` constructs an Anthropic client and propagates `model_id` correctly without invoking the real SDK.
<!-- trie:end -->