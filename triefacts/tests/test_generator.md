---
trie_version: 0.1.5
source: tests/test_generator.py
file_fingerprint: 32d167cd301e41d5d07933657a71663079790354e205071a9411338c7dcc3c47
last_synced_at: '2026-06-03T20:56:01Z'
defines:
- kind: module
  qualified_name: tests/test_generator:__module__
  lines: 1-244
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
  lines: 232-243
incoming_refs: 0
outgoing_refs: 45
---
<!-- trie:section symbol=tests/test_generator:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=6fe9f0e72ef2c22bd0fedab8e6668a56149de0494dee24d910f5af2f5f433ce2 source_ref=a0b7070e3e72c5ee0ad4dc614ccc6fd3e72124fa -->
Test module for the symbol documentation generation system.

- Covers cold-write mode, diff-aware mode, symbol context clause generation, and client construction
- Uses temporary files and FakeTrieClient for isolated testing
- Tests prompt construction, caching behavior, and decorator propagation in symbol extraction
<!-- trie:end -->
<!-- trie:section symbol=tests/test_generator:test_cached_context_includes_source_and_filename fingerprint=05c2240c12cb32e9582df345efbc8008b1869ef148587ed7d624e7dec18248ff body_fp=877dd0513f93fa877570e3cbd0e33faca5d7cee1941037720de4e0e7b89723c8 source_ref=a0b7070e3e72c5ee0ad4dc614ccc6fd3e72124fa -->
Verifies that `build_cached_context` includes file path, source code, and Python markdown formatting.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_generator:test_request_names_symbol_and_lines fingerprint=46f5a49f9a778751dd3ad6e1c627422cef153e52157f668a1eaef9188feb2cdd body_fp=bd86c8866d06f931890e9a5f28ef250877f0d6410c6c18a9807bb91994531084 source_ref=a0b7070e3e72c5ee0ad4dc614ccc6fd3e72124fa -->
## `test_request_names_symbol_and_lines()`

Verifies that `_build_request()` includes symbol name, type, line info, and source code in the generated request string.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_generator:test_generate_section_passes_correct_prompt fingerprint=a09a74597915a7dbaf2e8dad9443472b9c50de4f532857233559b6312e0b0242 body_fp=b1a9c7f4d5e77d56a0d5aa1d9882b697683c2d471050380be7502a5ce037815a source_ref=a0b7070e3e72c5ee0ad4dc614ccc6fd3e72124fa -->
Verifies generate_section passes correct system prompt, user prompt content, and cache prefix to the client.

• Tests that symbol source and qualified name appear in user prompt
• Confirms full file source becomes cache prefix rather than part of user prompt
• Validates returned section preserves qualified name and body formatting
<!-- trie:end -->
<!-- trie:section symbol=tests/test_generator:test_generate_section_strips_surrounding_whitespace fingerprint=fa34c7d3432173d54dfb5627a5b7745459cfd563bd3fe5893b975f060f942970 body_fp=aa23be17215c60cd498ad640b5c4d02246144296f133da7496ddcde12b39bd8b source_ref=a0b7070e3e72c5ee0ad4dc614ccc6fd3e72124fa -->
Verifies that `generate_section` preserves whitespace in client output without stripping it.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_generator:test_generate_section_defaults_to_cold_mode fingerprint=6d3c4fea0b2708238cf609b462fb76b6d26c763ec9b81e37a437b48b89e6fe06 body_fp=fa5d91ce798c5853d1d376f310164c8dd9aa1c7f680f4aa7475360bfe356840d source_ref=a0b7070e3e72c5ee0ad4dc614ccc6fd3e72124fa -->
Verifies that `generate_section` defaults to cold mode when no previous context is provided.

- Asserts the returned section has mode "cold"
- Confirms cold-write prompts exclude diff-aware rubric and previous content blocks
- Verifies symbol source is included in the prompt
<!-- trie:end -->
<!-- trie:section symbol=tests/test_generator:test_generate_section_takes_diff_aware_when_both_previous_provided fingerprint=dbf6013019c2f3eb529bd975c430aef1ae67df365f20da73bbdb5952c6065bc6 body_fp=c05345b83eb69f6b9ce3996b8031b38baf4ffdd938e1f58dfb522abb00ae6fbe source_ref=a0b7070e3e72c5ee0ad4dc614ccc6fd3e72124fa -->
Verifies that `generate_section` uses diff-aware mode when both previous source and prose are provided.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_generator:test_generate_section_partial_previous_falls_back_to_cold fingerprint=0459652202d7998143824389d1faf43e19f286700b887f7a077989c2a630e183 body_fp=3824a96eaf9ca07a00e729915eca2cfab3a031906a9e5146846c8c21ad7be5a9 source_ref=a0b7070e3e72c5ee0ad4dc614ccc6fd3e72124fa -->
## `test_generate_section_partial_previous_falls_back_to_cold()`

Tests that generate_section falls back to cold mode when only one of previous_source or previous_prose is provided.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_generator:test_diff_aware_request_carries_cosmetic_preserve_instruction fingerprint=2f77db8c1c0293285179dac96d981c5008e2f5bfa87b0422f3153973b351c588 body_fp=3f4c4b30932fd90bd4de7d79ec5e06f0a2162c425dde93409337ed17ee840f84 source_ref=a0b7070e3e72c5ee0ad4dc614ccc6fd3e72124fa -->
Verifies that `_build_diff_aware_request` includes instructions to preserve prose for cosmetic source changes.

- Checks for "Cosmetic changes", "Behavioural changes", "verbatim", and "prefer preserving" text in the generated request
<!-- trie:end -->
<!-- trie:section symbol=tests/test_generator:test_symbol_context_clause_plain_method fingerprint=fb374e775dbfaa4a45b8ef03d0bcef7b7659492868d1b0c0a4b5844fd81afb2e body_fp=745ee4eb322dc9f8483218b04edc6a6e27eae304dacc38ff2ccdeef438392bc8 source_ref=a0b7070e3e72c5ee0ad4dc614ccc6fd3e72124fa -->
Tests that `_symbol_context_clause` returns "method of class Foo" for a plain instance method.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_generator:test_symbol_context_clause_property fingerprint=54d6de47c6e3e96927aded1f337c8609b132e0ff32468650056208220ce821aa body_fp=11ee99142eeb03cc4ae76663cf13b4edcca43df007b84a6f134f3a7eade54bff source_ref=a0b7070e3e72c5ee0ad4dc614ccc6fd3e72124fa -->
Verifies that `_symbol_context_clause` returns descriptive text containing "@property" and the owning class name for property methods.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_generator:test_symbol_context_clause_classmethod fingerprint=22c5653e80c176ddd79ab74b097bfa31301b8f956e51d99a7cae3bf9bb716088 body_fp=ee4d45775d9c6437f25963d3197660c485efc28962090791fa73ce903e1be705 source_ref=a0b7070e3e72c5ee0ad4dc614ccc6fd3e72124fa -->
Tests that `_symbol_context_clause` includes `@classmethod` decorator and class name for classmethod symbols.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_generator:test_symbol_context_clause_plain_function fingerprint=301be51f4a461e6280ed29118dfa342dff9dec1e27b548d9c44088a95337524e body_fp=c8e128b46597fb809362008d79a547cf268688af1812e7b579984ff0509326d4 source_ref=a0b7070e3e72c5ee0ad4dc614ccc6fd3e72124fa -->
Verifies that `_symbol_context_clause` returns "a function" for standalone function symbols.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_generator:test_symbol_source_includes_decorators fingerprint=91be4a2f56d4f3e58d93eaac26ce271547aa6630b0e321f2db96ea0e1ff512fb body_fp=00c89967cc9241c8a2b481a6114167936a49e64711be0defee4d814d805a94aa source_ref=a0b7070e3e72c5ee0ad4dc614ccc6fd3e72124fa -->
Tests that `_symbol_source` includes decorator syntax when extracting symbol source code.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_generator:test_request_method_names_class fingerprint=dc93e64d498ea570690659e840492adff12ccee49a5f51c50248b1b5238d139a body_fp=cc8ea9817c56f68827ba22b2e80955f9656533b0103b619ad1a5e8032af1bdbe source_ref=a0b7070e3e72c5ee0ad4dc614ccc6fd3e72124fa -->
Tests that `_build_request` includes class name and method type when building request for a method.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_generator:test_make_client_rejects_unknown_provider fingerprint=f872f29b5c63a1e81c80c37abf32fe8bb20662ff5ee60dcd7b0817015d657eef body_fp=26649e7a78f266657a7e19463ab657e1308e57a3db5c7f730dfd69395800a9dc source_ref=a0b7070e3e72c5ee0ad4dc614ccc6fd3e72124fa -->
Tests that `make_client` raises `NotImplementedError` for unsupported provider prefixes like "openai/".
<!-- trie:end -->
<!-- trie:section symbol=tests/test_generator:test_make_client_requires_provider_prefix fingerprint=df2b5275115453c8315d3057c0b82e0ee7f1cedc1b60219fc1624984efb88cda body_fp=d84ca136fcc7535272d7df8f117d47f0d11b676fb58da3fc251171b5122b3a43 source_ref=a0b7070e3e72c5ee0ad4dc614ccc6fd3e72124fa -->
Verifies that make_client raises ValueError when model_id lacks a provider prefix.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_generator:test_make_client_anthropic_constructs fingerprint=dfd8fc29b3ee7a03780ebe88c5f2640efe49e11ef5c5765e6252818f7a559178 body_fp=c0b54fa8c79200c301c049d0dc36e0e8c0a4c5abcea0b301f2f632badc437e5a source_ref=a0b7070e3e72c5ee0ad4dc614ccc6fd3e72124fa -->
Verifies that make_client properly constructs an Anthropic client with the correct model_id when given an "anthropic/" provider prefix.
<!-- trie:end -->