---
trie_version: 0.3.0
source: tests/test_generator.py
file_fingerprint: d7a09120417c18748856f2a0173300c2c4d19be4b7beb6e1b104a31f41169770
last_synced_at: '2026-08-02T21:19:03Z'
defines:
- kind: module
  qualified_name: tests/test_generator:__module__
  lines: 1-270
- kind: function
  qualified_name: tests/test_generator:test_cached_context_includes_source_and_filename
  lines: 23-28
  signature: def test_cached_context_includes_source_and_filename()
- kind: function
  qualified_name: tests/test_generator:test_request_names_symbol_and_lines
  lines: 31-41
  signature: 'def test_request_names_symbol_and_lines(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_generator:test_generate_section_passes_correct_prompt
  lines: 44-62
  signature: 'def test_generate_section_passes_correct_prompt(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_generator:test_generate_section_strips_surrounding_whitespace
  lines: 65-73
  signature: 'def test_generate_section_strips_surrounding_whitespace(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_generator:test_system_prompt_states_signature_is_recorded_mechanically
  lines: 76-83
  signature: def test_system_prompt_states_signature_is_recorded_mechanically()
- kind: function
  qualified_name: tests/test_generator:test_generate_section_does_not_normalize_heading_itself
  lines: 86-97
  signature: 'def test_generate_section_does_not_normalize_heading_itself(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_generator:test_generate_section_defaults_to_cold_mode
  lines: 103-118
  signature: 'def test_generate_section_defaults_to_cold_mode(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_generator:test_generate_section_takes_diff_aware_when_both_previous_provided
  lines: 121-145
  signature: 'def test_generate_section_takes_diff_aware_when_both_previous_provided(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_generator:test_generate_section_partial_previous_falls_back_to_cold
  lines: 148-165
  signature: 'def test_generate_section_partial_previous_falls_back_to_cold(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_generator:test_diff_aware_request_carries_cosmetic_preserve_instruction
  lines: 168-187
  signature: 'def test_diff_aware_request_carries_cosmetic_preserve_instruction(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_generator:test_symbol_context_clause_plain_method
  lines: 193-199
  signature: 'def test_symbol_context_clause_plain_method(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_generator:test_symbol_context_clause_property
  lines: 202-208
  signature: 'def test_symbol_context_clause_property(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_generator:test_symbol_context_clause_classmethod
  lines: 211-217
  signature: 'def test_symbol_context_clause_classmethod(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_generator:test_symbol_context_clause_plain_function
  lines: 220-225
  signature: 'def test_symbol_context_clause_plain_function(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_generator:test_symbol_source_includes_decorators
  lines: 228-234
  signature: 'def test_symbol_source_includes_decorators(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_generator:test_request_method_names_class
  lines: 237-243
  signature: 'def test_request_method_names_class(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_generator:test_make_client_rejects_unknown_provider
  lines: 246-248
  signature: def test_make_client_rejects_unknown_provider()
- kind: function
  qualified_name: tests/test_generator:test_make_client_requires_provider_prefix
  lines: 251-253
  signature: def test_make_client_requires_provider_prefix()
- kind: function
  qualified_name: tests/test_generator:test_make_client_anthropic_constructs
  lines: 256-269
  signature: 'def test_make_client_anthropic_constructs(monkeypatch: pytest.MonkeyPatch): # Don''t actually init the SDK; just verify the type and model_id propagation.'
incoming_refs: 0
outgoing_refs: 51
---
<!-- trie:section symbol=tests/test_generator:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=a4401ace0a425b6b4f614a9ece49f71bbfd39a2fd534b42438475523bb20052d source_ref=a0b7070e3e72c5ee0ad4dc614ccc6fd3e72124fa role=test-infrastructure -->
Test module for trie.sync.generator functions including symbol documentation generation and diff-aware mode.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_generator:test_cached_context_includes_source_and_filename fingerprint=05c2240c12cb32e9582df345efbc8008b1869ef148587ed7d624e7dec18248ff body_fp=4cc4549fc0deee911581381e6ee7dfd265af80e001b8d290fabc8c50ba044c04 source_ref=a0b7070e3e72c5ee0ad4dc614ccc6fd3e72124fa role=test -->
## `def test_cached_context_includes_source_and_filename()`

Verifies that `build_cached_context` returns output containing the file path, source code, and Python code block formatting.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_generator:test_request_names_symbol_and_lines fingerprint=46f5a49f9a778751dd3ad6e1c627422cef153e52157f668a1eaef9188feb2cdd body_fp=7eb36fb6694124d277a236cf84dda4cd8f7cddee1f93168018c4ef0ab061fa91 source_ref=a0b7070e3e72c5ee0ad4dc614ccc6fd3e72124fa role=test -->
## `def test_request_names_symbol_and_lines(tmp_path: Path)`

Tests that `_build_request` includes symbol name, type, line numbers, and source code in its output.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_generator:test_generate_section_passes_correct_prompt fingerprint=a09a74597915a7dbaf2e8dad9443472b9c50de4f532857233559b6312e0b0242 body_fp=bfee49d718182f714c8a8cc788b97ebc37890230aa17afb5679f9a9c31072b33 source_ref=a0b7070e3e72c5ee0ad4dc614ccc6fd3e72124fa role=test -->
## `def test_generate_section_passes_correct_prompt(tmp_path: Path)`

Verifies that `generate_section` passes the correct system prompt, user prompt, and cache prefix to the client.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_generator:test_generate_section_strips_surrounding_whitespace fingerprint=fa34c7d3432173d54dfb5627a5b7745459cfd563bd3fe5893b975f060f942970 body_fp=da521765a76795da41e08b12c249c3044b09c06524be5e2690533e1538632e16 source_ref=a0b7070e3e72c5ee0ad4dc614ccc6fd3e72124fa role=test -->
## `def test_generate_section_strips_surrounding_whitespace(tmp_path: Path)`

Verifies that `generate_section` preserves whitespace in the client's output body without stripping it.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_generator:test_system_prompt_states_signature_is_recorded_mechanically fingerprint=8e31c26ae111cc2eac5929846c58598013f70bf406c064bde0d6983ee036cabf body_fp=20ab2f399c746bff117558b9feaf6717d563b4c2cc011730dbb6a6f3b9b0f721 source_ref=493034364e287e0eaa46df3451642206cb00255e role=test -->
## `def test_system_prompt_states_signature_is_recorded_mechanically()`

Assert that `SYSTEM_PROMPT` contains the phrases `"recorded mechanically"`, `"keyword-only"`, and `"positional-only"`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_generator:test_generate_section_does_not_normalize_heading_itself fingerprint=60a49853ab5d4f49e5c2625e01f7356badaa0dcf33a4602a5377f3840b99e123 body_fp=b836fdb08eebd49770703ca274e89a2b917cce9359912d2a183ce94a396708e7 source_ref=493034364e287e0eaa46df3451642206cb00255e role=test -->
## `def test_generate_section_does_not_normalize_heading_itself(tmp_path: Path)`

Assert that `generate_section` returns the LLM body verbatim, delegating heading normalisation to the sync layer's `ensure_signature_heading`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_generator:test_generate_section_defaults_to_cold_mode fingerprint=6d3c4fea0b2708238cf609b462fb76b6d26c763ec9b81e37a437b48b89e6fe06 body_fp=8ff02e4207e117db6a17875a0585db02abd98e5952c6dd7599a7db3d8ac9a996 source_ref=a0b7070e3e72c5ee0ad4dc614ccc6fd3e72124fa role=test -->
## `def test_generate_section_defaults_to_cold_mode(tmp_path: Path)`

Tests that `generate_section` uses cold mode when no previous source or prose is provided.

- Verifies the returned section has `mode == "cold"`
- Confirms cold requests exclude diff-aware rubric and previous content blocks
- Ensures cold requests include the current symbol source block
<!-- trie:end -->
<!-- trie:section symbol=tests/test_generator:test_generate_section_takes_diff_aware_when_both_previous_provided fingerprint=dbf6013019c2f3eb529bd975c430aef1ae67df365f20da73bbdb5952c6065bc6 body_fp=925b76228fe5bed3a2211dfaaac9f3c1a1ee454acde6c8fadf72a5aa04fe18a3 source_ref=a0b7070e3e72c5ee0ad4dc614ccc6fd3e72124fa role=test -->
## `def test_generate_section_takes_diff_aware_when_both_previous_provided(tmp_path: Path)`

Verifies that `generate_section` enters diff-aware mode when both `previous_source` and `previous_prose` are provided, including expected prompt structure and content.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_generator:test_generate_section_partial_previous_falls_back_to_cold fingerprint=0459652202d7998143824389d1faf43e19f286700b887f7a077989c2a630e183 body_fp=f2ecfa8cedb6eeabcce03138e62025c7b4ed22af17f41aad175e21815f199ca9 source_ref=a0b7070e3e72c5ee0ad4dc614ccc6fd3e72124fa role=test -->
## `def test_generate_section_partial_previous_falls_back_to_cold(tmp_path: Path)`

Tests that `generate_section` falls back to cold mode when only one of previous_source or previous_prose is provided.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_generator:test_diff_aware_request_carries_cosmetic_preserve_instruction fingerprint=2f77db8c1c0293285179dac96d981c5008e2f5bfa87b0422f3153973b351c588 body_fp=486fe64f2fcbc9f62b72889dcebc33472500773e7f87673226ff7797d880e108 source_ref=a0b7070e3e72c5ee0ad4dc614ccc6fd3e72124fa role=test -->
## `def test_diff_aware_request_carries_cosmetic_preserve_instruction(tmp_path: Path)`

Verifies that diff-aware requests include instructions to preserve prose on cosmetic source changes.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_generator:test_symbol_context_clause_plain_method fingerprint=fb374e775dbfaa4a45b8ef03d0bcef7b7659492868d1b0c0a4b5844fd81afb2e body_fp=6b44902ad8f95685163a8db2a28fd7e2ed0f0c9aad6ad93ea4a4f078f264edde source_ref=a0b7070e3e72c5ee0ad4dc614ccc6fd3e72124fa role=test -->
## `def test_symbol_context_clause_plain_method(tmp_path: Path)`

Tests that `_symbol_context_clause` correctly identifies a plain method and includes the owning class name.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_generator:test_symbol_context_clause_property fingerprint=54d6de47c6e3e96927aded1f337c8609b132e0ff32468650056208220ce821aa body_fp=7b69f191c3c63a127d3456c4a6a9d5f8eb56c7f70796c66800c013922160a0be source_ref=a0b7070e3e72c5ee0ad4dc614ccc6fd3e72124fa role=test -->
## `def test_symbol_context_clause_property(tmp_path: Path)`

Tests that `_symbol_context_clause` correctly identifies and describes @property decorated methods.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_generator:test_symbol_context_clause_classmethod fingerprint=22c5653e80c176ddd79ab74b097bfa31301b8f956e51d99a7cae3bf9bb716088 body_fp=ba8438c4ef5f863eb9ac1f16c44433dc7918c6bfb95b1c8237fb3861a2326043 source_ref=a0b7070e3e72c5ee0ad4dc614ccc6fd3e72124fa role=test -->
## `def test_symbol_context_clause_classmethod(tmp_path: Path)`

Verifies that _symbol_context_clause identifies @classmethod decorators and includes the containing class name.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_generator:test_symbol_context_clause_plain_function fingerprint=301be51f4a461e6280ed29118dfa342dff9dec1e27b548d9c44088a95337524e body_fp=d87f1f361744654e2c14ce5fe42867897423b97a42503c92d9d0260bee23f283 source_ref=a0b7070e3e72c5ee0ad4dc614ccc6fd3e72124fa role=test -->
## `def test_symbol_context_clause_plain_function(tmp_path: Path)`

Tests that `_symbol_context_clause` returns "a function" for plain function symbols.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_generator:test_symbol_source_includes_decorators fingerprint=91be4a2f56d4f3e58d93eaac26ce271547aa6630b0e321f2db96ea0e1ff512fb body_fp=d4948834978c224856f8f27642fb6ffe2495bd1291d05e2c59489efe1cc5e9c4 source_ref=a0b7070e3e72c5ee0ad4dc614ccc6fd3e72124fa role=test -->
## `def test_symbol_source_includes_decorators(tmp_path: Path)`

Verifies that `_symbol_source` includes decorator lines when extracting source code for decorated methods.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_generator:test_request_method_names_class fingerprint=dc93e64d498ea570690659e840492adff12ccee49a5f51c50248b1b5238d139a body_fp=08f341cdcbbfcab03fbb223673473835123f8acbc4887fc188669da8f111e853 source_ref=a0b7070e3e72c5ee0ad4dc614ccc6fd3e72124fa role=test -->
## `def test_request_method_names_class(tmp_path: Path)`

Verifies that `_build_request` includes class name and method type when generating requests for method symbols.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_generator:test_make_client_rejects_unknown_provider fingerprint=f872f29b5c63a1e81c80c37abf32fe8bb20662ff5ee60dcd7b0817015d657eef body_fp=61be89765cc515c58f8865942ba32b0ff41f158ba57cd58821369acedf81d5b5 source_ref=a0b7070e3e72c5ee0ad4dc614ccc6fd3e72124fa role=test -->
## `def test_make_client_rejects_unknown_provider()`

Verifies that `make_client` raises `NotImplementedError` for unsupported provider prefixes like "openai".
<!-- trie:end -->
<!-- trie:section symbol=tests/test_generator:test_make_client_requires_provider_prefix fingerprint=df2b5275115453c8315d3057c0b82e0ee7f1cedc1b60219fc1624984efb88cda body_fp=0733abfb6fb82e67e4559d639a96a1c8da63fd96835f775bd3f35e08a9aa61e8 source_ref=a0b7070e3e72c5ee0ad4dc614ccc6fd3e72124fa role=test -->
## `def test_make_client_requires_provider_prefix()`

Tests that `make_client` raises ValueError when model ID lacks provider prefix.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_generator:test_make_client_anthropic_constructs fingerprint=4fe52f30339a95405b947a0295927ea8683517b40fe14a282972b09a838eaad5 body_fp=454da73c8d90f32ba9a2352d9e06c1b554235870700fe7486fb4fb925ef9e51b source_ref=6d0c79ed1a1fe9de83edbec79741f7a9a4601f56 role=test -->
## `def test_make_client_anthropic_constructs(monkeypatch: pytest.MonkeyPatch): # Don't actually init the SDK; just verify the type and model_id propagation.`

Verifies `make_client()` constructs an Anthropic client with correct model ID propagation.
<!-- trie:end -->