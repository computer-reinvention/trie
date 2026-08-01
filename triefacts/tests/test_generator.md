---
trie_version: 0.2.1
source: tests/test_generator.py
file_fingerprint: a172f3861479a380937df66d2c608932afbbefb7e823ebf77486050b65240a42
last_synced_at: '2026-08-01T01:51:56Z'
defines:
- kind: module
  qualified_name: tests/test_generator:__module__
  lines: 1-246
- kind: function
  qualified_name: tests/test_generator:test_cached_context_includes_source_and_filename
  lines: 23-28
- kind: function
  qualified_name: tests/test_generator:test_request_names_symbol_and_lines
  lines: 31-41
- kind: function
  qualified_name: tests/test_generator:test_generate_section_passes_correct_prompt
  lines: 44-62
- kind: function
  qualified_name: tests/test_generator:test_generate_section_strips_surrounding_whitespace
  lines: 65-73
- kind: function
  qualified_name: tests/test_generator:test_generate_section_defaults_to_cold_mode
  lines: 79-94
- kind: function
  qualified_name: tests/test_generator:test_generate_section_takes_diff_aware_when_both_previous_provided
  lines: 97-121
- kind: function
  qualified_name: tests/test_generator:test_generate_section_partial_previous_falls_back_to_cold
  lines: 124-141
- kind: function
  qualified_name: tests/test_generator:test_diff_aware_request_carries_cosmetic_preserve_instruction
  lines: 144-163
- kind: function
  qualified_name: tests/test_generator:test_symbol_context_clause_plain_method
  lines: 169-175
- kind: function
  qualified_name: tests/test_generator:test_symbol_context_clause_property
  lines: 178-184
- kind: function
  qualified_name: tests/test_generator:test_symbol_context_clause_classmethod
  lines: 187-193
- kind: function
  qualified_name: tests/test_generator:test_symbol_context_clause_plain_function
  lines: 196-201
- kind: function
  qualified_name: tests/test_generator:test_symbol_source_includes_decorators
  lines: 204-210
- kind: function
  qualified_name: tests/test_generator:test_request_method_names_class
  lines: 213-219
- kind: function
  qualified_name: tests/test_generator:test_make_client_rejects_unknown_provider
  lines: 222-224
- kind: function
  qualified_name: tests/test_generator:test_make_client_requires_provider_prefix
  lines: 227-229
- kind: function
  qualified_name: tests/test_generator:test_make_client_anthropic_constructs
  lines: 232-245
incoming_refs: 0
outgoing_refs: 46
---
<!-- trie:section symbol=tests/test_generator:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=a4401ace0a425b6b4f614a9ece49f71bbfd39a2fd534b42438475523bb20052d source_ref=a0b7070e3e72c5ee0ad4dc614ccc6fd3e72124fa role=test-infrastructure -->
Test module for trie.sync.generator functions including symbol documentation generation and diff-aware mode.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_generator:test_cached_context_includes_source_and_filename fingerprint=05c2240c12cb32e9582df345efbc8008b1869ef148587ed7d624e7dec18248ff body_fp=11818f6ecf19bbfca153802b1dc2c252ed4c60c5002943b364c3119dea50e6c4 source_ref=a0b7070e3e72c5ee0ad4dc614ccc6fd3e72124fa role=test -->
## `test_cached_context_includes_source_and_filename()`

Verifies that `build_cached_context` returns output containing the file path, source code, and Python code block formatting.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_generator:test_request_names_symbol_and_lines fingerprint=46f5a49f9a778751dd3ad6e1c627422cef153e52157f668a1eaef9188feb2cdd body_fp=9958d59872a3923a0d0058e2225ecbde139c42abffdbfbcafe35cae9388ae5db source_ref=a0b7070e3e72c5ee0ad4dc614ccc6fd3e72124fa role=test -->
Tests that `_build_request` includes symbol name, type, line numbers, and source code in its output.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_generator:test_generate_section_passes_correct_prompt fingerprint=a09a74597915a7dbaf2e8dad9443472b9c50de4f532857233559b6312e0b0242 body_fp=e793146471441b27294e8950fa5506458fd35a64800001bce50b12bc4583cd3c source_ref=a0b7070e3e72c5ee0ad4dc614ccc6fd3e72124fa role=test -->
Verifies that `generate_section` passes the correct system prompt, user prompt, and cache prefix to the client.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_generator:test_generate_section_strips_surrounding_whitespace fingerprint=fa34c7d3432173d54dfb5627a5b7745459cfd563bd3fe5893b975f060f942970 body_fp=90ac8089dfed674ecd8afda5db5895fdc2c4347bff33974964f761226e98b5b8 source_ref=a0b7070e3e72c5ee0ad4dc614ccc6fd3e72124fa role=test -->
Verifies that `generate_section` preserves whitespace in the client's output body without stripping it.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_generator:test_generate_section_defaults_to_cold_mode fingerprint=6d3c4fea0b2708238cf609b462fb76b6d26c763ec9b81e37a437b48b89e6fe06 body_fp=825ddd2faff84155bbb2f88116b340d662ad5a3e9a105a4f55d0e3dda85d0267 source_ref=a0b7070e3e72c5ee0ad4dc614ccc6fd3e72124fa role=test -->
## `test_generate_section_defaults_to_cold_mode()`

Tests that `generate_section` uses cold mode when no previous source or prose is provided.

- Verifies the returned section has `mode == "cold"`
- Confirms cold requests exclude diff-aware rubric and previous content blocks
- Ensures cold requests include the current symbol source block
<!-- trie:end -->
<!-- trie:section symbol=tests/test_generator:test_generate_section_takes_diff_aware_when_both_previous_provided fingerprint=dbf6013019c2f3eb529bd975c430aef1ae67df365f20da73bbdb5952c6065bc6 body_fp=394ac12a49defa30d51d51247f1ed0c4afe57426a4f81ea49224faa99989aea9 source_ref=a0b7070e3e72c5ee0ad4dc614ccc6fd3e72124fa role=test -->
Verifies that `generate_section` enters diff-aware mode when both `previous_source` and `previous_prose` are provided, including expected prompt structure and content.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_generator:test_generate_section_partial_previous_falls_back_to_cold fingerprint=0459652202d7998143824389d1faf43e19f286700b887f7a077989c2a630e183 body_fp=2af5b3c8573d0c93dbc7554bbf53ef535b6ea036dcf8996c996ab758cec6af74 source_ref=a0b7070e3e72c5ee0ad4dc614ccc6fd3e72124fa role=test -->
Tests that `generate_section` falls back to cold mode when only one of previous_source or previous_prose is provided.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_generator:test_diff_aware_request_carries_cosmetic_preserve_instruction fingerprint=2f77db8c1c0293285179dac96d981c5008e2f5bfa87b0422f3153973b351c588 body_fp=8d3cfc60c9d62949193f78feaa905229f841fd11e07d1f43f7b18f77fd79145a source_ref=a0b7070e3e72c5ee0ad4dc614ccc6fd3e72124fa role=test -->
## `test_diff_aware_request_carries_cosmetic_preserve_instruction()`

Verifies that diff-aware requests include instructions to preserve prose on cosmetic source changes.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_generator:test_symbol_context_clause_plain_method fingerprint=fb374e775dbfaa4a45b8ef03d0bcef7b7659492868d1b0c0a4b5844fd81afb2e body_fp=71f9cf1b63be8016978be6c9e3dc52b15a1394d975da7a1fb233130269135e87 source_ref=a0b7070e3e72c5ee0ad4dc614ccc6fd3e72124fa role=test -->
Tests that `_symbol_context_clause` correctly identifies a plain method and includes the owning class name.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_generator:test_symbol_context_clause_property fingerprint=54d6de47c6e3e96927aded1f337c8609b132e0ff32468650056208220ce821aa body_fp=20323055a84a7d411dea744d938594f0836e9aff30989d459be1b332f17db21a source_ref=a0b7070e3e72c5ee0ad4dc614ccc6fd3e72124fa role=test -->
Tests that `_symbol_context_clause` correctly identifies and describes @property decorated methods.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_generator:test_symbol_context_clause_classmethod fingerprint=22c5653e80c176ddd79ab74b097bfa31301b8f956e51d99a7cae3bf9bb716088 body_fp=496bfd8dacc4e6b9b1e00211dc727fabdecee203ae23ca374f4d2a72dbbc6356 source_ref=a0b7070e3e72c5ee0ad4dc614ccc6fd3e72124fa role=test -->
Verifies that _symbol_context_clause identifies @classmethod decorators and includes the containing class name.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_generator:test_symbol_context_clause_plain_function fingerprint=301be51f4a461e6280ed29118dfa342dff9dec1e27b548d9c44088a95337524e body_fp=f1c933637cfa2c06fcb1d3f418233d0a288ebceafd3c13044ae2ae274821fd19 source_ref=a0b7070e3e72c5ee0ad4dc614ccc6fd3e72124fa role=test -->
Tests that `_symbol_context_clause` returns "a function" for plain function symbols.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_generator:test_symbol_source_includes_decorators fingerprint=91be4a2f56d4f3e58d93eaac26ce271547aa6630b0e321f2db96ea0e1ff512fb body_fp=27a9bb7bcb867d4af6c1994fa1fe7c6d627e2e1808af2e9ed6f1cf2dd14b5db1 source_ref=a0b7070e3e72c5ee0ad4dc614ccc6fd3e72124fa role=test -->
Verifies that `_symbol_source` includes decorator lines when extracting source code for decorated methods.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_generator:test_request_method_names_class fingerprint=dc93e64d498ea570690659e840492adff12ccee49a5f51c50248b1b5238d139a body_fp=0067800094237e303d3f0bc9c24291eff46c9ea497ba1c4016233a023579376a source_ref=a0b7070e3e72c5ee0ad4dc614ccc6fd3e72124fa role=test -->
## `test_request_method_names_class`

Verifies that `_build_request` includes class name and method type when generating requests for method symbols.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_generator:test_make_client_rejects_unknown_provider fingerprint=f872f29b5c63a1e81c80c37abf32fe8bb20662ff5ee60dcd7b0817015d657eef body_fp=b02748443b105d40bfae2ceadfc2b3bfea92c431de015ed8c40cda3f0dfadef9 source_ref=a0b7070e3e72c5ee0ad4dc614ccc6fd3e72124fa role=test -->
Verifies that `make_client` raises `NotImplementedError` for unsupported provider prefixes like "openai".
<!-- trie:end -->
<!-- trie:section symbol=tests/test_generator:test_make_client_requires_provider_prefix fingerprint=df2b5275115453c8315d3057c0b82e0ee7f1cedc1b60219fc1624984efb88cda body_fp=e2919f6e00dfbb4434c6a6daf237e44aca83cb9242a0027eef0f776912eb8073 source_ref=a0b7070e3e72c5ee0ad4dc614ccc6fd3e72124fa role=test -->
Tests that `make_client` raises ValueError when model ID lacks provider prefix.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_generator:test_make_client_anthropic_constructs fingerprint=4fe52f30339a95405b947a0295927ea8683517b40fe14a282972b09a838eaad5 body_fp=86abc7c1ec68c3e7faf8c1a1f0f5c7394ddee7e4f71e0e1b206444e45abd260e source_ref=6d0c79ed1a1fe9de83edbec79741f7a9a4601f56 role=test -->
Verifies `make_client()` constructs an Anthropic client with correct model ID propagation.
<!-- trie:end -->