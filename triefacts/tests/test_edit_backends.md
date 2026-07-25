---
trie_version: 0.1.9
source: tests/test_edit_backends.py
file_fingerprint: d1653336689a288921fc1d9d73483635d1949536f9e6c3e76d4a17b30f2f4d23
last_synced_at: '2026-07-25T08:07:27Z'
defines:
- kind: module
  qualified_name: tests/test_edit_backends:__module__
  lines: 1-140
- kind: function
  qualified_name: tests/test_edit_backends:_req
  lines: 17-31
- kind: class
  qualified_name: tests/test_edit_backends:TestFakeBackend
  lines: 34-72
- kind: method
  qualified_name: tests/test_edit_backends:TestFakeBackend.test_passthrough_echoes_source
  lines: 35-39
- kind: method
  qualified_name: tests/test_edit_backends:TestFakeBackend.test_append_changes_source
  lines: 41-45
- kind: method
  qualified_name: tests/test_edit_backends:TestFakeBackend.test_broken_returns_noncompiling
  lines: 47-51
- kind: method
  qualified_name: tests/test_edit_backends:TestFakeBackend.test_fail_returns_not_ok
  lines: 53-57
- kind: method
  qualified_name: tests/test_edit_backends:TestFakeBackend.test_per_qname_override
  lines: 59-63
- kind: method
  qualified_name: tests/test_edit_backends:TestFakeBackend.test_create_synthesizes_when_empty
  lines: 65-69
- kind: method
  qualified_name: tests/test_edit_backends:TestFakeBackend.test_satisfies_protocol
  lines: 71-72
- kind: class
  qualified_name: tests/test_edit_backends:TestLLMBackend
  lines: 75-94
- kind: method
  qualified_name: tests/test_edit_backends:TestLLMBackend.test_build_user_prompt_includes_context
  lines: 76-82
- kind: method
  qualified_name: tests/test_edit_backends:TestLLMBackend.test_create_clause_present_for_create
  lines: 84-86
- kind: method
  qualified_name: tests/test_edit_backends:TestLLMBackend.test_satisfies_protocol
  lines: 88-94
- kind: class
  qualified_name: tests/test_edit_backends:TestFactory
  lines: 97-139
- kind: method
  qualified_name: tests/test_edit_backends:TestFactory.test_default_is_record_which_never_generates
  lines: 98-109
- kind: method
  qualified_name: tests/test_edit_backends:TestFactory.test_llm_backend_still_constructible_explicitly
  lines: 111-118
- kind: method
  qualified_name: tests/test_edit_backends:TestFactory.test_opencode_not_yet_implemented
  lines: 120-123
- kind: method
  qualified_name: tests/test_edit_backends:TestFactory.test_unknown_backend_raises
  lines: 125-128
- kind: method
  qualified_name: tests/test_edit_backends:TestFactory.test_run_override_wins_over_config
  lines: 130-139
incoming_refs: 0
outgoing_refs: 9
---
<!-- trie:section symbol=tests/test_edit_backends:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=cb692600c03509dccf85b05896333b7b7ac40a859c19008db5b5ad4fb0f598f5 source_ref=2fa76b15719e20b01695bdc39b43321036358d84 role=test -->
Tests for edit backend implementations including FakeBackend, InProcessLLMBackend, and factory functions.

- Validates FakeBackend modes: passthrough, append, broken, fail with per-qname overrides
- Tests LLM prompt building with context inclusion for callees, callers, and session notes  
- Verifies backend factory creates appropriate instances based on configuration
- Includes protocol compliance checks for SymbolEditBackend interface
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edit_backends:_req fingerprint=b75d20f424a9e692b311f91963a7d4dc75b6b6d15222e942e6f6d612a63171ca body_fp=548414991dd271ccea189194a8ec8dd69f99d0a44cccb6b3988dd2d32580ea72 source_ref=2fa76b15719e20b01695bdc39b43321036358d84 role=util -->
Creates an EditRequest test fixture with default values for all required fields.

- `op`: operation type, defaults to "modify"
- `**kw`: keyword arguments that override any default field values
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edit_backends:TestFakeBackend fingerprint=dd9f57df2d5e2ec9aac79b29223e5c5903c908b36018869dc14fac59364f3972 body_fp=1050c5ca733a3602332324856a4810d86bfd186375deb4abfa45cd1bccd35ccd source_ref=2fa76b15719e20b01695bdc39b43321036358d84 role=test -->
Tests FakeBackend behavior across different modes and operations.

- `test_passthrough_echoes_source`: verifies passthrough mode returns unchanged source
- `test_append_changes_source`: confirms append mode modifies source with fake edit marker
- `test_broken_returns_noncompiling`: checks broken mode produces malformed but successful response
- `test_fail_returns_not_ok`: ensures fail mode returns error response
- `test_per_qname_override`: validates per-symbol mode overrides work correctly
- `test_create_synthesizes_when_empty`: tests create operation generates new symbol definition
- `test_satisfies_protocol`: confirms FakeBackend implements SymbolEditBackend protocol
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edit_backends:TestFakeBackend.test_passthrough_echoes_source fingerprint=9a62571534cffe461f6377030a1f10034659ec925df91951efa0fc9627d23ef9 body_fp=c1ec6cff05e994c2b475f342e001f3c7fdae5b38968d6433a4e085374faff6a0 source_ref=2fa76b15719e20b01695bdc39b43321036358d84 role=test -->
Verifies that TestFakeBackend in passthrough mode returns the original source code unchanged.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edit_backends:TestFakeBackend.test_append_changes_source fingerprint=dda07c29502cce8a7bacab850ab05d2c1ee48fb4a00a0ac7f1755f8f03fbf187 body_fp=497770fd77ab1d352df8061e7001108c901769dbcac227bfb128ee918537dc1e source_ref=2fa76b15719e20b01695bdc39b43321036358d84 role=test -->
Verifies that TestFakeBackend.test_append_changes_source creates a FakeBackend in "append" mode and confirms it modifies source code by adding "trie-fake-edit".
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edit_backends:TestFakeBackend.test_broken_returns_noncompiling fingerprint=28f2d4d4f9b24b3cf4e5316b2a0df86ee179e533de8b24f99d9568ee1ccd7af5 body_fp=cd81a1bd1b27c62476e02c42317cb90d4598df8a7b6de5c73597c679062c82fb source_ref=2fa76b15719e20b01695bdc39b43321036358d84 role=test -->
Tests that TestFakeBackend.test_broken_returns_noncompiling verifies FakeBackend("broken") returns ok with non-compiling source code.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edit_backends:TestFakeBackend.test_fail_returns_not_ok fingerprint=0149262fe7a6bc8fa242f40cb611b956e2551a6f708392fa11c0b38f79a90f7d body_fp=f09620c39ff6a9842cea1264d13e96bbce9c36787c6f7064f14ea9fc0b8440c3 source_ref=2fa76b15719e20b01695bdc39b43321036358d84 role=test -->
Tests TestFakeBackend.test_fail_returns_not_ok verifies FakeBackend with "fail" mode returns unsuccessful result with error.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edit_backends:TestFakeBackend.test_per_qname_override fingerprint=6008391541b539b360dcb1206237a924a8e2d3cbe1cf1fbf48aa357bb273d53c body_fp=56845575a122e76c108fe0a9a718fcb2e82a69a522683d1d2fbeab981eabf9df source_ref=2fa76b15719e20b01695bdc39b43321036358d84 role=test -->
Tests that TestFakeBackend respects per-symbol overrides, using fail mode for specific qname while defaulting to passthrough for others.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edit_backends:TestFakeBackend.test_create_synthesizes_when_empty fingerprint=7b614a2ffb6f5103a33963c4235d29f3a4eb6d04c4d9764ee792306d5d1aa48d body_fp=a004d0a8f68178002acdaff6eb9a74b484a69878f02493d480d0b6213298c6d5 source_ref=2fa76b15719e20b01695bdc39b43321036358d84 role=test -->
Verifies FakeBackend generates new code when creating symbols with empty source input.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edit_backends:TestFakeBackend.test_satisfies_protocol fingerprint=66f5156a47b2c7f081b0a7709d86b0771e47b50d02a517c43b6b5f76cfd33ad7 body_fp=4b4a3a80cf22074e739db9ca1037bdacd8d99b74c528cdff079c4fd58c666c18 source_ref=2fa76b15719e20b01695bdc39b43321036358d84 role=test -->
Verifies that FakeBackend implements the SymbolEditBackend protocol by checking isinstance.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edit_backends:TestLLMBackend fingerprint=fcf762df6938fe8910f4688763701f87052332c429215699a5555bca77adeb52 body_fp=ca5c1e2e29c225dc74434cf1a47efcba0f83ee0f7b3ff95f33f28f5f3bdaadb4 source_ref=2fa76b15719e20b01695bdc39b43321036358d84 role=test -->
Test class for InProcessLLMBackend functionality and prompt generation behavior.

- `test_build_user_prompt_includes_context`: Verifies prompt contains qname, callees, callers, and notes
- `test_create_clause_present_for_create`: Checks create operations include "NEW symbol" text
- `test_satisfies_protocol`: Confirms InProcessLLMBackend implements SymbolEditBackend protocol
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edit_backends:TestLLMBackend.test_build_user_prompt_includes_context fingerprint=d910e68fbe7be48c7c915632146d9dc1461099dcab0cb681df91cb7b2910f4b4 body_fp=0690864f7132e70d0e2a6aef1beecaabed46cb33037e3f782aac9aa8a73147a6 source_ref=2fa76b15719e20b01695bdc39b43321036358d84 role=test -->
Verifies that TestLLMBackend.test_build_user_prompt_includes_context builds prompts containing symbol name, callees, callers, session notes, and intent notes.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edit_backends:TestLLMBackend.test_create_clause_present_for_create fingerprint=63711f4698e7bf40ec51f51728e6b3f055479435934ff8846f9f7b73bb0196f7 body_fp=d59a4f4c891b1a6b77476389633bc9e36722de94ec8d93818fb802df15521b6a source_ref=2fa76b15719e20b01695bdc39b43321036358d84 role=test -->
Verifies that TestLLMBackend includes "NEW symbol" clause in prompt for create operations with empty source.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edit_backends:TestLLMBackend.test_satisfies_protocol fingerprint=2144b003d2e858c91cf6155e2a82ea21a62b2426462b7a8b210faccd9811d0bd body_fp=481b80149e681e2a272e29142504414fe2d2ad8b94b012dfed01ca232b061740 source_ref=2fa76b15719e20b01695bdc39b43321036358d84 role=test -->
TestLLMBackend.test_satisfies_protocol verifies InProcessLLMBackend implements the SymbolEditBackend protocol using a dummy client.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edit_backends:TestFactory fingerprint=f35ba1ed0ec7ceac904b364d1a64aaea62857aabab1fbfe691582b2885724c1c body_fp=37f384700e67f48c9b0f3396f92354ad056447cd354a87f6e87600af27efcc98 source_ref=2fb795182dcddc943fe395897c70b900cbb1b1f3 role=test -->
Tests the `make_backend` factory function behavior with different configuration and runtime parameters.

- `test_default_is_record_which_never_generates`: verifies default backend "record" raises ValueError instead of silently falling back to LLM
- `test_llm_backend_still_constructible_explicitly`: confirms InProcessLLMBackend is returned when `backend="llm"` is passed explicitly
- `test_opencode_not_yet_implemented`: checks NotImplementedError for opencode backend
- `test_unknown_backend_raises`: validates ValueError for invalid backend names
- `test_run_override_wins_over_config`: confirms runtime parameter overrides config setting
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edit_backends:TestFactory.test_default_is_record_which_never_generates fingerprint=289b999653868abf4e6c91a26a579e2ab5bd60efd01b839bf9a91fe54c03d659 body_fp=8613f45e23622dd0d944b92b7e6f5a5e771e9d3063fc1131d27de980411b8cbf source_ref=2fb795182dcddc943fe395897c70b900cbb1b1f3 role=test -->
Assert that `TestFactory` verifies `make_backend` raises `ValueError` when the default `"record"` backend is used, preventing silent degradation to LLM generation.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edit_backends:TestFactory.test_llm_backend_still_constructible_explicitly fingerprint=696305d362cac0e63c103dd99cac0b81032d9c7f2f74738c5b6878613cea648a body_fp=5ef51ba5fd83ef5678f04ec7890cbbf13739ff4b4c2d28dff52f2e26c5a1b8a5 source_ref=2fb795182dcddc943fe395897c70b900cbb1b1f3 role=test -->
Assert that `TestFactory` can construct an `InProcessLLMBackend` by passing `backend="llm"` explicitly to `make_backend`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edit_backends:TestFactory.test_opencode_not_yet_implemented fingerprint=0f78dc50048173b200eae42a221e7ac79119e4aa7919d5845f2e1d8d531bd462 body_fp=2388074d9d2246c0ad459396e588b8a091a4c73080e0cb7eea9f8413f78c3e8c source_ref=2fa76b15719e20b01695bdc39b43321036358d84 role=test -->
TestFactory.test_opencode_not_yet_implemented verifies that make_backend raises NotImplementedError when given "opencode" backend.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edit_backends:TestFactory.test_unknown_backend_raises fingerprint=09df664ff2e257532ef8263b1bce2f060913e0d3f17fe23e1d1f0b6fd3e34833 body_fp=43cc7adc0c2bf554fec2574bc0c36511f5533b55534c95b8f84c3a809a7c4254 source_ref=2fa76b15719e20b01695bdc39b43321036358d84 role=test -->
Verifies that TestFactory.make_backend raises ValueError when given an unknown backend name.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edit_backends:TestFactory.test_run_override_wins_over_config fingerprint=08555a493d90b6a995bfed27b040c72d2e0f73d44385759cfa64ecaae073b4f3 body_fp=223955b7d1ddcc5f2ddef283e691a4624c56f037af13437d565e0c0686fc9296 source_ref=2fa76b15719e20b01695bdc39b43321036358d84 role=test -->
TestFactory.test_run_override_wins_over_config verifies that make_backend runtime parameter takes precedence over Config setting.
<!-- trie:end -->