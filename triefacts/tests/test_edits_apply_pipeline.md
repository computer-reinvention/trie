---
trie_version: 0.1.5
source: tests/test_edits_apply_pipeline.py
file_fingerprint: 67852ab74e5c7d6d3c30a07e51a72c8c4df1f46f3ea2350e0c5c04099f0ce15a
last_synced_at: '2026-06-03T20:55:01Z'
defines:
- kind: module
  qualified_name: tests/test_edits_apply_pipeline:__module__
  lines: 1-401
- kind: constant
  qualified_name: tests/test_edits_apply_pipeline:PROJECT_TOML
  lines: 21-29
- kind: function
  qualified_name: tests/test_edits_apply_pipeline:_git
  lines: 32-33
- kind: function
  qualified_name: tests/test_edits_apply_pipeline:_init_repo
  lines: 36-39
- kind: function
  qualified_name: tests/test_edits_apply_pipeline:_extract_old_source
  lines: 42-55
- kind: function
  qualified_name: tests/test_edits_apply_pipeline:_extract_old_prose
  lines: 58-65
- kind: function
  qualified_name: tests/test_edits_apply_pipeline:_is_merge_prompt
  lines: 68-69
- kind: function
  qualified_name: tests/test_edits_apply_pipeline:_make_usage
  lines: 72-84
- kind: class
  qualified_name: tests/test_edits_apply_pipeline:FakeTriefactClient
  lines: 87-108
- kind: method
  qualified_name: tests/test_edits_apply_pipeline:FakeTriefactClient.run
  lines: 93-104
- kind: method
  qualified_name: tests/test_edits_apply_pipeline:FakeTriefactClient.count_tokens
  lines: 107-108
- kind: class
  qualified_name: tests/test_edits_apply_pipeline:FakeEditClient
  lines: 111-147
- kind: method
  qualified_name: tests/test_edits_apply_pipeline:FakeEditClient.run
  lines: 120-143
- kind: method
  qualified_name: tests/test_edits_apply_pipeline:FakeEditClient.count_tokens
  lines: 146-147
- kind: class
  qualified_name: tests/test_edits_apply_pipeline:PassthroughClient
  lines: 150-183
- kind: method
  qualified_name: tests/test_edits_apply_pipeline:PassthroughClient.run
  lines: 156-179
- kind: method
  qualified_name: tests/test_edits_apply_pipeline:PassthroughClient.count_tokens
  lines: 182-183
- kind: class
  qualified_name: tests/test_edits_apply_pipeline:BrokenClient
  lines: 186-217
- kind: method
  qualified_name: tests/test_edits_apply_pipeline:BrokenClient.run
  lines: 192-213
- kind: method
  qualified_name: tests/test_edits_apply_pipeline:BrokenClient.count_tokens
  lines: 216-217
- kind: function
  qualified_name: tests/test_edits_apply_pipeline:project
  lines: 221-274
- kind: class
  qualified_name: tests/test_edits_apply_pipeline:TestApplyPatchesEmpty
  lines: 277-297
- kind: method
  qualified_name: tests/test_edits_apply_pipeline:TestApplyPatchesEmpty.test_no_patches_returns_immediately
  lines: 278-284
- kind: method
  qualified_name: tests/test_edits_apply_pipeline:TestApplyPatchesEmpty.test_git_clean_after_empty_apply
  lines: 286-297
- kind: class
  qualified_name: tests/test_edits_apply_pipeline:TestApplyPatchesSuccess
  lines: 300-364
- kind: method
  qualified_name: tests/test_edits_apply_pipeline:TestApplyPatchesSuccess.test_applies_single_symbol
  lines: 301-312
- kind: method
  qualified_name: tests/test_edits_apply_pipeline:TestApplyPatchesSuccess.test_patches_deleted_after_success
  lines: 314-323
- kind: method
  qualified_name: tests/test_edits_apply_pipeline:TestApplyPatchesSuccess.test_no_git_commit_created
  lines: 325-339
- kind: method
  qualified_name: tests/test_edits_apply_pipeline:TestApplyPatchesSuccess.test_applies_in_topo_order
  lines: 341-348
- kind: method
  qualified_name: tests/test_edits_apply_pipeline:TestApplyPatchesSuccess.test_cascaded_no_change_skips_write
  lines: 350-364
- kind: class
  qualified_name: tests/test_edits_apply_pipeline:TestApplyPatchesFailure
  lines: 367-400
- kind: method
  qualified_name: tests/test_edits_apply_pipeline:TestApplyPatchesFailure.test_compile_error_returns_failure
  lines: 368-376
- kind: method
  qualified_name: tests/test_edits_apply_pipeline:TestApplyPatchesFailure.test_rollback_restores_files
  lines: 378-389
- kind: method
  qualified_name: tests/test_edits_apply_pipeline:TestApplyPatchesFailure.test_patches_preserved_after_rollback
  lines: 391-400
incoming_refs: 0
outgoing_refs: 71
---
<!-- trie:section symbol=tests/test_edits_apply_pipeline:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=4e16786e72cc6d0305b39539015b241bcc325e6c7264e0cc7f33bc0bf4c47d10 source_ref=561fe032a463723a9caeb0fc7ff996886e2079de -->
Tests for the patch application pipeline including success/failure cases, rollback behavior, and git integration.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:PROJECT_TOML fingerprint=ea44d5615a2611cc14e40b5b84f8141a4679269bc80e3914e4fef0417f24d38b body_fp=2bf4a0728b883a933b8fee3dd2d2b8949dbc2edf4f44f31abadd06017124fe0a source_ref=561fe032a463723a9caeb0fc7ff996886e2079de -->
TOML configuration string for test project setup with trie settings, model endpoints, and cascade parameters.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:_git fingerprint=9efa6f55f9332a871587d0a9f0d4447d61f49c18b4d819e91e90494d14cf2f16 body_fp=17441e6a8dd2ebfb20a5b487ccf6d22f385d74c8f2144f821889fd96fd65605d source_ref=561fe032a463723a9caeb0fc7ff996886e2079de -->
Executes git command with given arguments in specified directory, raising on failure.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:_init_repo fingerprint=e6a8e59044cd4691a616ada677408e96c9c856caafae13744c548e08d2b462be body_fp=2c8633b330ac119af3cf715c815ed30c0ee4ffa339c9e8be3c80e797d9ad3b13 source_ref=561fe032a463723a9caeb0fc7ff996886e2079de -->
Initialize a git repository with test user configuration at the specified path.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:_extract_old_source fingerprint=bcd11656d8918f3fa2184a028c94523c815515e979b154d01009499a9c24e786 body_fp=51d321701f7f9f9b129f6b26acac75b541ad453f6a461179ffed08236ec709f7 source_ref=561fe032a463723a9caeb0fc7ff996886e2079de -->
Extracts Python source code from a markdown-formatted code block in an LLM prompt string.

- Returns only non-empty lines within the first ```python...``` block
- Ignores nested triple backticks (``````)
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:_extract_old_prose fingerprint=8717c70ea434bf53fc16753b5930da9e782d3e0318ae3bee95b278c5667c8450 body_fp=787e08893a96bc704fc9ab499eea672aa6a60b98da60c3a38a26794f0179a65d source_ref=561fe032a463723a9caeb0fc7ff996886e2079de -->
Extracts the old prose section from an LLM infer prompt by splitting on marker text.

- Returns empty string if "Old prose (the symbol's documented purpose):" marker not found
- Splits text after marker and before "\nImplementation notes" section
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:_is_merge_prompt fingerprint=13df75d98109396ebce3eeae9f2acd9b95400180791f4b8d1b4d6a5d780269ca body_fp=755a60a9f1fd1b2023d5446b1e2db689c0ab98b2a5a48103785b96a09a664695 source_ref=561fe032a463723a9caeb0fc7ff996886e2079de -->
Checks if a prompt string contains merge notes by looking for a specific marker phrase.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:_make_usage fingerprint=778ea16dee0036412660edb79d77aa94f191365fcd8e9c689ed41ba866b067a1 body_fp=1851829f4019b056023d31323cd3401704bfdcee72c81fa6ced72f13afddc20a source_ref=561fe032a463723a9caeb0fc7ff996886e2079de -->
Creates a mock Usage object with configurable token counts for testing LLM responses.

- **overrides**: Token count overrides (defaults: input=10, output=20, cache tokens=0)
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:FakeTriefactClient fingerprint=c11b80b954b967f6175c495c1c8d9749a556ac092e87dc5b8d01452a1bb1faf6 body_fp=024dee2d336c51a533922b7190367c596d7f5b652685baf33ea9886918880b8b source_ref=561fe032a463723a9caeb0fc7ff996886e2079de -->
Mock LLM client for testing triefact generation that returns static documentation content.

- `run`: Returns a ModelResult with fixed SectionBody containing "Auto-generated prose"
- `count_tokens`: Always returns 100 tokens regardless of input
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:FakeTriefactClient.run fingerprint=aa2a88a9411d02e5505faa8a887e26efa9c481c5ae82a19d96ed33eb9a68478b body_fp=732403f11b30ed90fc318f4d51982e5b8d68a5b9f2ccf5aa3ac4891e0cc68b04 source_ref=561fe032a463723a9caeb0fc7ff996886e2079de -->
Returns a fixed ModelResult with auto-generated prose for testing sync_single_file operations.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:FakeTriefactClient.count_tokens fingerprint=d2e54258807160cae2cd3e384f807ff7ab8c686f8c79830c0798dd9ba6b1e027 body_fp=f149a09ee6be8ae277a3abd2409a9d215172d61135584b8188574a9acae1e55c source_ref=561fe032a463723a9caeb0fc7ff996886e2079de -->
Returns a fixed token count of 100 for FakeTriefactClient test scenarios.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:FakeEditClient fingerprint=ba1ad5dbebe3c61dccc3510b73f4bc25468b89efdd042035e8c3a87f70648e4a body_fp=57e924c07e5ce9ecefea8fe1aec86e8550dc5088ce6be9be6d81afc5d5bd7348 source_ref=561fe032a463723a9caeb0fc7ff996886e2079de -->
Simulates an LLM client for testing patch application, returning different outputs based on the requested output type.

- Returns merge notes for `MergeNotesOutput` requests
- Returns empty decisions for `BatchFilterOutput` requests  
- Appends "# patch-applied" comment to source for `SymbolEdit` requests
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:FakeEditClient.run fingerprint=bc56c6959c2a9044f8ebbe0632c45e1585f7a0f86c1f9a24568791f931915ab3 body_fp=4b00f71f51da9cf9ae25b14ac37780364e729c04c16ba54f46690bdb8c5e11bb source_ref=561fe032a463723a9caeb0fc7ff996886e2079de -->
Simulates LLM edits by appending "# patch-applied" to extracted source code and returning mock results based on output type.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:FakeEditClient.count_tokens fingerprint=d2e54258807160cae2cd3e384f807ff7ab8c686f8c79830c0798dd9ba6b1e027 body_fp=9f7850a1da90c91a033b32a6f787e86da31334cc8ed7cbee8ce1bc4333015af0 source_ref=561fe032a463723a9caeb0fc7ff996886e2079de -->
Returns a fixed token count of 100 for any prompt pair in FakeEditClient.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:PassthroughClient fingerprint=9eb0398197bdc8a26374b3cad67013ac0a65a4dd5c8bce789d33ee816958af59 body_fp=8462e9d48c20154bb9e2beccf7b7a3442fff29daf8f7b247173286c525bef436 source_ref=561fe032a463723a9caeb0fc7ff996886e2079de -->
Fake LLM client that returns unchanged source and prose for symbol edits.

- **model_id**: Returns "fake/passthrough"
- **run**: Returns unmodified source and prose extracted from user prompt for SymbolEdit requests
- **count_tokens**: Always returns 100
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:PassthroughClient.run fingerprint=9346deca9763f8a2f77fea6524e9d1db47b6388696fe2a588f6f0a60583c161d body_fp=9ca4f76a89bc6ccfe34b66d8d98fed60cd934b38952af8a293b3da65b23ec34d source_ref=561fe032a463723a9caeb0fc7ff996886e2079de -->
PassthroughClient static method that returns unchanged source and prose from user prompt for SymbolEdit requests.

- Returns fixed MergeNotesOutput or BatchFilterOutput for respective output types
- Extracts and echoes back original source/prose for other requests
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:PassthroughClient.count_tokens fingerprint=d2e54258807160cae2cd3e384f807ff7ab8c686f8c79830c0798dd9ba6b1e027 body_fp=8827dd3b74db57f24c24271ed4d569cb42c7113e269d15a91957076058e2a1f4 source_ref=561fe032a463723a9caeb0fc7ff996886e2079de -->
PassthroughClient.count_tokens returns a fixed token count of 100 for any prompts.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:BrokenClient fingerprint=32e4f66b0c2045144a69b17fb195fb3d3cef0cd43e6f7f810f0df232ee6e8510 body_fp=a0bfd460c89e695eb0de916dae4d20d970bd268fcbe5505f9b970b83728fb330 source_ref=561fe032a463723a9caeb0fc7ff996886e2079de -->
Mock LLM client that returns syntactically invalid Python source for testing error handling in patch application.

- Returns `SymbolEdit` with malformed source code `"def broken(:"`
- Handles `MergeNotesOutput` and `BatchFilterOutput` normally with dummy data
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:BrokenClient.run fingerprint=409a604a9de51871d52d433242c4dd9b14b28806674d3b6021a89db8fabf9e88 body_fp=f6b41bc8e3f3bde79a41a1b06ec72e0372bc199bd24cf37121d389c1515652fc source_ref=561fe032a463723a9caeb0fc7ff996886e2079de -->
Returns a ModelResult with syntactically invalid Python source for testing error handling in the BrokenClient class.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:BrokenClient.count_tokens fingerprint=d2e54258807160cae2cd3e384f807ff7ab8c686f8c79830c0798dd9ba6b1e027 body_fp=be78454b39108fea38ad642e6dc5ccf7e19334c8d19ba243cc04cc0f2ec61f5a source_ref=561fe032a463723a9caeb0fc7ff996886e2079de -->
BrokenClient static method that returns a fixed token count of 100 for any prompt input.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:project fingerprint=26c6072a1e41f0d8332363602aa260b6b79e16528f847797cda935b864cc4be5 body_fp=9375913ac73278665cee069bddd30f7c5df73f53c3ea42eb46daa29eb763f833 source_ref=561fe032a463723a9caeb0fc7ff996886e2079de -->
Creates a pytest fixture that provides a fully configured test project with three Python modules and git repository.

- Sets up alpha.py → beta.py → gamma.py call chain with documentation
- Scans project and syncs all symbols using FakeTriefactClient
- Initializes git repository with initial commit
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:TestApplyPatchesEmpty fingerprint=fe9d42f96f40e8e186b3dfcf3f116213343fed5a7b5704784a2be138c5e63695 body_fp=805e60cd54933c2b9b0fdd140a0793119d1540200d993faabc53447e02004c5f source_ref=561fe032a463723a9caeb0fc7ff996886e2079de -->
## TestApplyPatchesEmpty

Tests apply_patches behavior when no patches exist in the database.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:TestApplyPatchesEmpty.test_no_patches_returns_immediately fingerprint=af1c83bd2eab932f81c972d6026fae8cfc67306e824f0f162b8c6f3fbf645270 body_fp=4801682e45406be898d8bb66d39d132cbafa018df0cd507a9cf7535053753589 source_ref=561fe032a463723a9caeb0fc7ff996886e2079de -->
Verifies TestApplyPatchesEmpty.test_no_patches_returns_immediately returns success status with zero counts when no patches exist in the store.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:TestApplyPatchesEmpty.test_git_clean_after_empty_apply fingerprint=c5893657f0aed624008309b981a1fddcbad56f7dc907a8310567dda75f8b7c68 body_fp=77937fb2e6fd49ecef4c47efdec6c13d2cc84d824fb93d542334ae5d6c8cd4f4 source_ref=561fe032a463723a9caeb0fc7ff996886e2079de -->
Verifies that TestApplyPatchesEmpty.test_git_clean_after_empty_apply leaves the git working directory clean when applying empty patches.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:TestApplyPatchesSuccess fingerprint=8484656371c70dea113a63d7c783db6a16e4f4c9ce1f821839d374d3fa0668c7 body_fp=77269f080a3ab58453d54e377700f1d89a6a2d5c8b1c3d7618401c6a5aa3e3b8 source_ref=561fe032a463723a9caeb0fc7ff996886e2079de -->
Tests successful patch application scenarios for the apply_patches function.

- test_applies_single_symbol: verifies patches are applied and result indicates success
- test_patches_deleted_after_success: confirms patches are removed from store after successful application
- test_no_git_commit_created: ensures apply_patches doesn't create git commits
- test_applies_in_topo_order: tests that patches are applied in topological dependency order
- test_cascaded_no_change_skips_write: verifies files aren't written when cascaded updates produce identical source
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:TestApplyPatchesSuccess.test_applies_single_symbol fingerprint=41394e4b9a39f3cbfc1e37f0e7f7a97244e4bd498ba7cff518df0f2b1c54f445 body_fp=ef699ee9467aa106da194e91022813161d8251aaa72ff1f94a5ef6867c039da7 source_ref=561fe032a463723a9caeb0fc7ff996886e2079de -->
TestApplyPatchesSuccess test method that verifies apply_patches successfully processes a single patch and returns successful result metrics.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:TestApplyPatchesSuccess.test_patches_deleted_after_success fingerprint=24be5af6c0b4e62f5f146b8e27210bd9d6650e7c3e129db0fcd9f87274221c7b body_fp=9b3601ad8e8d1348a561a1d4b9b06af7b6fef8d69ba0c7fd30eade690707d518 source_ref=561fe032a463723a9caeb0fc7ff996886e2079de -->
Verifies TestApplyPatchesSuccess patches are removed from database after successful application.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:TestApplyPatchesSuccess.test_no_git_commit_created fingerprint=f2bc664e521f06056a3dce2808add1d4fbb73e45b9cce8e531978eaf89de20ad body_fp=d86a8526440530f17584dfbba06e9d5310e8af4ced3f3f998135829b72c9bcbe source_ref=561fe032a463723a9caeb0fc7ff996886e2079de -->
Verifies that TestApplyPatchesSuccess apply_patches does not create git commits during patch application.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:TestApplyPatchesSuccess.test_applies_in_topo_order fingerprint=83a3756abbd4ab057503ebffbda8d9858b92bb32acc1337a17ec8b865b053b14 body_fp=e59b374dab46d2c3cdd39c054f7be50bbcfb10e86ec4fddafc509956a3926516 source_ref=561fe032a463723a9caeb0fc7ff996886e2079de -->
TestApplyPatchesSuccess.test_applies_in_topo_order verifies that patches are applied to symbols in topological dependency order.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:TestApplyPatchesSuccess.test_cascaded_no_change_skips_write fingerprint=923eb26667401b656cfd51d1f0237b3048e0ecc743f1081d52d1d7d9f0f9523b body_fp=2e9dc16d39897d8193cfc13259b8d0c9e1a3e1c12b1276643aa4a0480c6d7b43 source_ref=561fe032a463723a9caeb0fc7ff996886e2079de -->
## TestApplyPatchesSuccess.test_cascaded_no_change_skips_write

Verifies that applying patches with PassthroughClient leaves source files unchanged when edits produce identical content.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:TestApplyPatchesFailure fingerprint=5ac26c9416b77970ac3457f98df492327a9ece1720de2c8afc2ece3626be42ff body_fp=45d083d641822ede4533379d3892c593711ac89944d9334da9f54bd7258dde35 source_ref=561fe032a463723a9caeb0fc7ff996886e2079de -->
## TestApplyPatchesFailure

Tests apply_patches error handling and recovery when patch application fails.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:TestApplyPatchesFailure.test_compile_error_returns_failure fingerprint=7b976fafa7a1afc907025f2a67b3d835498e614f830138b4237e1b326f1dc85e body_fp=4db80809cb9a8f00a8158bb7a66c836b20af27f25b815697d5408e389804ee74 source_ref=561fe032a463723a9caeb0fc7ff996886e2079de -->
Tests that apply_patches returns failure status when BrokenClient generates syntactically invalid code.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:TestApplyPatchesFailure.test_rollback_restores_files fingerprint=9c9c2b5d980a1af2036d0ade4a96141ba1d5d81042ef0ee3defc9ee40a3adecf body_fp=a413d43f6f67953363834a5bb9a3f02dfcf7904de294221db6520b0ffb63414b source_ref=561fe032a463723a9caeb0fc7ff996886e2079de -->
Verifies TestApplyPatchesFailure rollback restores files to original state after patch application fails.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:TestApplyPatchesFailure.test_patches_preserved_after_rollback fingerprint=1a3f1e74c954f82a8471c620bf35e0f09bcfc22a8ac69d6e9d69acf38ff84ab4 body_fp=a6ba09e37d68579669456b9a4f1757d5e5c0f60895e1447ad04ddaa548cb16ea source_ref=561fe032a463723a9caeb0fc7ff996886e2079de -->
Verifies that TestApplyPatchesFailure preserves patches in the database after a failed apply operation for retry.
<!-- trie:end -->