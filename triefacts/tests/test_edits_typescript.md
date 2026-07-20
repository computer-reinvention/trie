---
trie_version: 0.1.9
source: tests/test_edits_typescript.py
file_fingerprint: 9069425acf51933eced5d554f8c325699ba72597642ecbd392b92b095e12d043
last_synced_at: '2026-07-20T09:54:31Z'
description: TypeScript parity for the edit/patch pipeline.
defines:
- kind: module
  qualified_name: tests/test_edits_typescript:__module__
  lines: 1-341
- kind: constant
  qualified_name: tests/test_edits_typescript:FIXTURE
  lines: 24-24
- kind: function
  qualified_name: tests/test_edits_typescript:test_python_fence_and_edit_prompt
  lines: 30-33
- kind: function
  qualified_name: tests/test_edits_typescript:test_typescript_fence_and_edit_prompt
  lines: 36-43
- kind: function
  qualified_name: tests/test_edits_typescript:test_registry_routes_fence_by_extension
  lines: 46-49
- kind: function
  qualified_name: tests/test_edits_typescript:test_edit_backend_uses_ts_prompt_for_ts_file
  lines: 55-62
- kind: function
  qualified_name: tests/test_edits_typescript:test_infer_helpers_use_ts_prompt_for_ts_file
  lines: 65-69
- kind: function
  qualified_name: tests/test_edits_typescript:test_build_user_prompt_fences_ts_source
  lines: 72-90
- kind: function
  qualified_name: tests/test_edits_typescript:test_python_validate_syntax
  lines: 96-99
- kind: function
  qualified_name: tests/test_edits_typescript:test_compile_check_routes_python_by_path
  lines: 102-108
- kind: class
  qualified_name: tests/test_edits_typescript:_FakeProc
  lines: 114-118
- kind: method
  qualified_name: tests/test_edits_typescript:_FakeProc.__init__
  lines: 115-118
- kind: function
  qualified_name: tests/test_edits_typescript:ts_backend_with_fake_tsc
  lines: 122-126
- kind: function
  qualified_name: tests/test_edits_typescript:test_ts_gate_rejects_syntax_error
  lines: 129-133
- kind: function
  qualified_name: tests/test_edits_typescript:test_ts_gate_accepts_when_only_type_errors
  lines: 136-143
- kind: function
  qualified_name: tests/test_edits_typescript:test_ts_gate_accepts_clean
  lines: 146-149
- kind: function
  qualified_name: tests/test_edits_typescript:test_ts_gate_degrades_to_accept_without_tsc
  lines: 152-157
- kind: function
  qualified_name: tests/test_edits_typescript:test_resolve_create_target_existing_ts_file
  lines: 163-165
- kind: function
  qualified_name: tests/test_edits_typescript:test_resolve_create_target_existing_py_file
  lines: 168-171
- kind: function
  qualified_name: tests/test_edits_typescript:test_resolve_create_target_new_file_infers_from_sibling
  lines: 174-181
- kind: class
  qualified_name: tests/test_edits_typescript:_RaisingClient
  lines: 187-191
- kind: method
  qualified_name: tests/test_edits_typescript:_RaisingClient.run
  lines: 190-191
- kind: function
  qualified_name: tests/test_edits_typescript:test_merge_notes_single_patch_skips_llm
  lines: 194-201
- kind: function
  qualified_name: tests/test_edits_typescript:test_merge_notes_degrades_on_llm_failure
  lines: 204-215
- kind: class
  qualified_name: tests/test_edits_typescript:_FakeDetail
  lines: 221-224
- kind: method
  qualified_name: tests/test_edits_typescript:_FakeDetail.__init__
  lines: 222-224
- kind: function
  qualified_name: tests/test_edits_typescript:test_insert_into_parent_brace_language
  lines: 227-239
- kind: function
  qualified_name: tests/test_edits_typescript:test_insert_into_parent_indentation_language
  lines: 242-249
- kind: function
  qualified_name: tests/test_edits_typescript:test_place_new_symbol_routes_method_into_class
  lines: 252-265
- kind: function
  qualified_name: tests/test_edits_typescript:test_symboledit_validates_large_tsx_source
  lines: 271-303
- kind: function
  qualified_name: tests/test_edits_typescript:test_truncated_structured_output_fails_validation
  lines: 306-321
- kind: function
  qualified_name: tests/test_edits_typescript:test_edit_backend_uses_larger_token_budget_and_retries
  lines: 324-340
incoming_refs: 0
outgoing_refs: 9
---
<!-- trie:section symbol=tests/test_edits_typescript:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=d56f7c51e0dabaa0ab9330d886a204f92e478c66099e94071ae0b50493394269 source_ref=e4f12d614c731fa103cda0f0037748b2ca924a5b role=test -->
Test suite verifying TypeScript parity across the edit/patch pipeline: language-aware prompts, syntax gate, file resolution, and symbol placement.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_typescript:FIXTURE fingerprint=883b5996900536d76bf6d49f99ed1a35468676b2f050a082d65e4eb092ae406f body_fp=eec690bf3f0b5921e8cbd3d5e442456db342345ba1d008b49da6a69cd2c52239 source_ref=e4f12d614c731fa103cda0f0037748b2ca924a5b role=config -->
Absolute `Path` pointing to the `fixtures/tiny_ts_repo` directory used as a test TypeScript repository.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_typescript:test_python_fence_and_edit_prompt fingerprint=d7a1f8bb6cc677f9e65ca1342841b0e77ab6f15156e9bde5aa3ee328d00db20a body_fp=57b0a6ca3cc974091618490ce1b0e179ebcc4742ec45841a085cc33b45c67d57 source_ref=e4f12d614c731fa103cda0f0037748b2ca924a5b role=test -->
Assert that `PythonBackend` returns `"python"` from `code_fence()` and includes `"Python"` in `edit_system_prompt()`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_typescript:test_typescript_fence_and_edit_prompt fingerprint=6ef07e5776e72164831e5e154f4f465dc472bda716074377a2f6eec53a18167b body_fp=0e569383e33014e0805f21212e69725e5cefced0030e2941817c4b6440500d7b source_ref=e4f12d614c731fa103cda0f0037748b2ca924a5b role=test -->
Assert that `TypeScriptBackend` returns `"typescript"` from `code_fence()` and that `edit_system_prompt()` references TypeScript, `tsc`, and import-exclusion instructions.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_typescript:test_registry_routes_fence_by_extension fingerprint=51f7dfa105da7d13ee93c41182fa5a54501325fa48301e0c11ff1d9b909dafb4 body_fp=19ec790c53150ce1a296a28b1af5efdb0743fef5c935931fa96f4dd4e4061005 source_ref=e4f12d614c731fa103cda0f0037748b2ca924a5b role=test -->
Assert that `registry.get_backend_for_file` returns the correct backend by file extension for `.ts`, `.tsx`, and `.py` files.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_typescript:test_edit_backend_uses_ts_prompt_for_ts_file fingerprint=dca6c5be61226cff99a16a5b1a7ec9865ffc7e327337de311774eaf21aabda1f body_fp=5ca4d0ac5d7b6080e46746c4956d4d0c67d751bc939329c8b8a7f12a29002fce source_ref=e4f12d614c731fa103cda0f0037748b2ca924a5b role=test -->
Verify that `_fence_for` and `_system_prompt_for` return TypeScript values for `.ts` paths and fall back to Python when path is `None`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_typescript:test_infer_helpers_use_ts_prompt_for_ts_file fingerprint=1d041650c8ea8063ae7781b5dc553df1ce2078324f09634b00eb0f01b2dcd4a4 body_fp=1046ece9172f06c7ed0d781b69e63e2ebd8e47f8ebc385b57a09c2813b2549f6 source_ref=e4f12d614c731fa103cda0f0037748b2ca924a5b role=test -->
Assert that `trie.edits.infer._fence_for` and `_system_prompt_for` return TypeScript-specific values for a `.tsx` file path.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_typescript:test_build_user_prompt_fences_ts_source fingerprint=0d8255555f16a00b5b34733c82d46afe6bd4eeafc95134018497498efff17fd9 body_fp=f9d295d18d2f498aa5b6d45db06390dfb9d982cc19501023d71c567f3ee5dfbf source_ref=e4f12d614c731fa103cda0f0037748b2ca924a5b role=test -->
Assert that `build_user_prompt` wraps a `.ts` file's source in a `typescript` code fence, not a `python` one.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_typescript:test_python_validate_syntax fingerprint=eafdc9eef673b9f3a8699f1161ff814690b4cdb4f0952875209f6aadd3ab55d0 body_fp=c3f3ef260538876e38a08d49c1f50329629c38e327b161e0df5504709337a1fd source_ref=e4f12d614c731fa103cda0f0037748b2ca924a5b role=test -->
Assert that `PythonBackend.validate_syntax` accepts valid Python source and rejects a syntax error.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_typescript:test_compile_check_routes_python_by_path fingerprint=67e79266b68b11866ce464d021dd2a8eec47d8f7d4d559f7646271c14b69adc1 body_fp=0fec165587422a28c4149bf245269ac893640837eeef5e888a0943180b9d3691 source_ref=e4f12d614c731fa103cda0f0037748b2ca924a5b role=test -->
Verify that `_compile_check` accepts valid Python, rejects invalid Python, and defaults to Python behaviour when no path is given.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_typescript:_FakeProc fingerprint=1f0f95922ffeacb4580d981ef0febe816b5e8e06c2ed05e0a0855b0553ac7060 body_fp=f3a9b8e59f40e08fa1bc25007086b76c2959ba744a61ecde177ed639c5cb4ce4 source_ref=e4f12d614c731fa103cda0f0037748b2ca924a5b role=test -->
Minimal `subprocess.CompletedProcess` stand-in for stubbing `subprocess.run` in TS gate tests.

- `returncode`: set to `2` when `out` is non-empty, `0` otherwise
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_typescript:_FakeProc.__init__ fingerprint=35be59392dd3867070ae29515cb0bb56ef38d6c576d0c9702454d21a9f93b022 body_fp=94e6380226509b40ab684356a42c194ba68f211d39d60599356644ebde78d24c source_ref=e4f12d614c731fa103cda0f0037748b2ca924a5b role=test -->
Initialise `_FakeProc` with `stdout` set to `out`, `stderr` as empty string, and `returncode` 2 if `out` is truthy else 0.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_typescript:ts_backend_with_fake_tsc fingerprint=48e44f7b2adfe9bf2277f1501a6f4e78accdf82474c8165efade7da3fde44733 body_fp=53ae73f0ba0bd28824c3d4225c143cff99cda4ba166e9ae892d7090587516363 source_ref=e4f12d614c731fa103cda0f0037748b2ca924a5b role=test -->
Pytest fixture that returns a `TypeScriptBackend` instance with `_find_tsc` stubbed to return `["tsc"]`, enabling hermetic `validate_syntax` decision tests.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_typescript:test_ts_gate_rejects_syntax_error fingerprint=29cb8524eafa3330b436d0c95f835e0e182268d23287e189331ca08c1092a0bd body_fp=3ede5494ffea1c1d7b90c5954a7988377aa9a7a56171b675566a35f594623a86 source_ref=e4f12d614c731fa103cda0f0037748b2ca924a5b role=test -->
Assert that `TypeScriptBackend.validate_syntax` returns `False` when `tsc` emits a TS1xxx syntax error.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_typescript:test_ts_gate_accepts_when_only_type_errors fingerprint=0431aa20a8edac54644e9e36fbe44ce76e67df26858a451d19792ec9f6851670 body_fp=8ae50ccfb42d8c20f074885c5ec1c6470ee3cf33b28d0f3ff28dfb0f4f973082 source_ref=e4f12d614c731fa103cda0f0037748b2ca924a5b role=test -->
Assert that `TypeScriptBackend.validate_syntax` accepts code when `tsc` emits only TS2xxx (type/resolution) errors, not TS1xxx syntax errors.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_typescript:test_ts_gate_accepts_clean fingerprint=71a32909916bd7fb63a07ede4aaa3226fe0b621a181fe52e758e28eea481b1e1 body_fp=f01b06d582934f3981d583cbc9f4a528c44b7152b30a7db7dfa2e614f3724b65 source_ref=e4f12d614c731fa103cda0f0037748b2ca924a5b role=test -->
Assert that `TypeScriptBackend.validate_syntax` returns `True` when `tsc` emits no output.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_typescript:test_ts_gate_degrades_to_accept_without_tsc fingerprint=7b4f456909766e705d7a2e18e8e9c45a98c6095739d98111d4a8cc12f4fbbdc8 body_fp=d77cf112286f9700b908384d468ae211920c47fd5f672c54b285f1dbf473a5f9 source_ref=e4f12d614c731fa103cda0f0037748b2ca924a5b role=test -->
Assert that `TypeScriptBackend.validate_syntax` returns `True` for broken TS when `tsc` is unavailable, confirming the gate degrades to accept rather than hard-blocking.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_typescript:test_resolve_create_target_existing_ts_file fingerprint=e583b37ce1d665313742607ef28563916033d2f9e81b2143fe52a411a7cb91cc body_fp=5487c00f50be993b09f58544044f1d8949f492f672cad9d12ade47260584ce0e source_ref=e4f12d614c731fa103cda0f0037748b2ca924a5b role=test -->
Assert that `registry.resolve_create_target` returns `"src/app.ts"` for a new symbol in an existing `.ts` fixture file.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_typescript:test_resolve_create_target_existing_py_file fingerprint=dba1fb05b607d4b42bcfc051751c1f1a11c42d00ff12d5d9f35e73e50bf1cabc body_fp=8dc6e86dc987a88e691e9b85b198210ff2b127f26fa91d8cd5f2530932935a36 source_ref=e4f12d614c731fa103cda0f0037748b2ca924a5b role=test -->
Assert that `registry.resolve_create_target` returns `"pkg/mod.py"` when the target module already exists as a `.py` file.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_typescript:test_resolve_create_target_new_file_infers_from_sibling fingerprint=9064aeb9d4641222b64c55548df962c1c37c5c6c23014b8aa7869937c2bc7917 body_fp=2fe192245a269e04f3fca3a55ed79bbb304f65ac35750bdadd9266ee571e1bdc source_ref=e4f12d614c731fa103cda0f0037748b2ca924a5b role=test -->
Assert that `registry.resolve_create_target` infers a `.ts`/`.tsx` extension for a new module in a directory containing existing `.tsx` siblings.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_typescript:_RaisingClient fingerprint=e25e86efa650ebf1b7361a3c475a204f25b2e81f720a2f08050c02efa626fa1a body_fp=1cb7c9767edf69ea06bffbf47ea2a7cbccc651b518e94235b50c4fee9c9d90b4 source_ref=e4f12d614c731fa103cda0f0037748b2ca924a5b role=test -->
Test stub that replaces a real `TrieClient`; its `run` method always raises `RuntimeError` to simulate LLM or schema failure.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_typescript:_RaisingClient.run fingerprint=faf3ddb3d016ace7b6cc29b7124720276cdb51ef172145e4238b4358cf9ec621 body_fp=751a13b57af95428c8ed024aadbbc0582a19dddc16f34c4aeb036ec40b939494 source_ref=e4f12d614c731fa103cda0f0037748b2ca924a5b role=test -->
Always raises `RuntimeError` to simulate an LLM/schema failure in `_RaisingClient`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_typescript:test_merge_notes_single_patch_skips_llm fingerprint=b64da136122c4c0a627048bbb209c9a0bc8a0c578ffb20414c27626a3ec86e59 body_fp=52158e396b6f3408b364a3c49fbd02f7d87a864475ff5834734c96914d8a20a8 source_ref=e4f12d614c731fa103cda0f0037748b2ca924a5b role=test -->
Assert that `merge_notes` returns the single patch's note and reason verbatim without invoking the LLM client.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_typescript:test_merge_notes_degrades_on_llm_failure fingerprint=620fbdfe5ac2b966bfa395e229a9d31c67bd98278e7b1ce3441dd9a0422627c2 body_fp=270ca24cd782855aadb948ee118cf3ea018c6f316b959d73931cadf5cf7ac29c source_ref=e4f12d614c731fa103cda0f0037748b2ca924a5b role=test -->
Assert that `merge_notes` falls back to raw patch notes and reasons when the LLM client raises, instead of aborting.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_typescript:_FakeDetail fingerprint=21390ed101b71c6115a9ea20219d9ed046e54cffc9e52a978bd5c0fcbe698343 body_fp=0123795db76ef96ff3ca95055d9a3e8862c9fcc91a8ef54e4901449f688c1c5e source_ref=e4f12d614c731fa103cda0f0037748b2ca924a5b role=test -->
Minimal test stub mimicking a symbol-detail object with `start_line` and `end_line` attributes for use in `_insert_into_parent` and `_place_new_symbol` tests.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_typescript:_FakeDetail.__init__ fingerprint=217ab7c20c452acce501d135392887771971d01aa070617abe0d37f2b779f6b3 body_fp=9c75bcc0a919b7a6f1aefcb52d75eddab404a2817b09b24ca28a573cb9018f48 source_ref=e4f12d614c731fa103cda0f0037748b2ca924a5b role=test -->
Initialises a `_FakeDetail` instance with `start_line` and `end_line` attributes used as a symbol-detail stub in insertion tests.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_typescript:test_insert_into_parent_brace_language fingerprint=28873839b4e3f0dbb64c409ede8ba751016a448635cb2c659d4c01d0ba1ff0ca body_fp=293a2d22f4af8d3373ad5fd01c9be3fc8213f2aebde2ca4ff7d7acdc9d4267f0 source_ref=e4f12d614c731fa103cda0f0037748b2ca924a5b role=test -->
Verify that `_insert_into_parent` places a new brace-language method inside the class body, before the closing brace, with member-level indentation.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_typescript:test_insert_into_parent_indentation_language fingerprint=989eb8c5cc677a4a2e6c81e7cbc1b1c3d7815a1111eac9b19346752a09a36768 body_fp=3f93d44d133718d862ab81578a5ec3bb823066b11a551b19b33aa4a81dea1105 source_ref=e4f12d614c731fa103cda0f0037748b2ca924a5b role=test -->
Verify that `_insert_into_parent` re-indents a new Python method to member level inside its parent class body.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_typescript:test_place_new_symbol_routes_method_into_class fingerprint=fd098eb5fa461d4621d611bfa831dc4e7193472dbc13f207b14bd34c9c575b36 body_fp=7a6a2762b91e76541c066f46e3e385915659c81f0a9c025baec83d1e91feb81b source_ref=e4f12d614c731fa103cda0f0037748b2ca924a5b role=test -->
Verify that `_place_new_symbol` inserts a new method inside the parent class body, before the closing brace.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_typescript:test_symboledit_validates_large_tsx_source fingerprint=84f8a6ef8b591498c0ee435a3a22054dac0cdd5b035994e48295b8d6a37d7e86 body_fp=e579266cc56c699b06c9c04d598ae1be13d8dc4dfb7169bf60dfcb15d5a9b639 source_ref=e4f12d614c731fa103cda0f0037748b2ca924a5b role=test -->
Assert that `SymbolEdit` validates a >20 KB TSX string containing JSX, backticks, regex, escaped quotes, and unicode — both as a direct object and via `model_validate_json`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_typescript:test_truncated_structured_output_fails_validation fingerprint=1eeab6524a15cd9d34c47a233fddc4381440790d81618a551b8781eb0a90201e body_fp=cb3ee94d0b26a4b5a2a7b9a1f8dd74ba15287fc97f597dc819578acae9e93283 source_ref=e4f12d614c731fa103cda0f0037748b2ca924a5b role=test -->
Assert that `SymbolEdit.model_validate_json` raises `ValidationError` when given a mid-string-truncated JSON payload, reproducing the token-cap failure mode.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_typescript:test_edit_backend_uses_larger_token_budget_and_retries fingerprint=c9e32756c348cc3c9fcc068f473a6ca8b9508a2f81f90e5ed96a04bbad76f960 body_fp=720039e632fc45103a09f374dfddc4b9bb03df32e35247980263339f27e494b2 source_ref=e4f12d614c731fa103cda0f0037748b2ca924a5b role=test -->
Assert that `Config.edits.max_output_tokens` is ≥ 8192, `output_retries` is ≥ 2, and that `make_backend` wires both values onto the returned backend instance.
<!-- trie:end -->