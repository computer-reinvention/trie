---
trie_version: 0.1.9
source: tests/test_edits_apply_pipeline.py
file_fingerprint: d64dc7c59f7e1b053381c3696fa00f910a3a99f031adb1920166c878f767228b
last_synced_at: '2026-07-20T13:09:41Z'
defines:
- kind: module
  qualified_name: tests/test_edits_apply_pipeline:__module__
  lines: 1-477
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
  qualified_name: tests/test_edits_apply_pipeline:_plain_edit_text
  lines: 72-81
- kind: function
  qualified_name: tests/test_edits_apply_pipeline:_make_usage
  lines: 84-96
- kind: class
  qualified_name: tests/test_edits_apply_pipeline:FakeTriefactClient
  lines: 99-120
- kind: method
  qualified_name: tests/test_edits_apply_pipeline:FakeTriefactClient.run
  lines: 105-116
- kind: method
  qualified_name: tests/test_edits_apply_pipeline:FakeTriefactClient.count_tokens
  lines: 119-120
- kind: class
  qualified_name: tests/test_edits_apply_pipeline:FakeEditClient
  lines: 123-174
- kind: method
  qualified_name: tests/test_edits_apply_pipeline:FakeEditClient.run
  lines: 132-155
- kind: method
  qualified_name: tests/test_edits_apply_pipeline:FakeEditClient.run_text
  lines: 158-170
- kind: method
  qualified_name: tests/test_edits_apply_pipeline:FakeEditClient.count_tokens
  lines: 173-174
- kind: class
  qualified_name: tests/test_edits_apply_pipeline:PassthroughClient
  lines: 177-225
- kind: method
  qualified_name: tests/test_edits_apply_pipeline:PassthroughClient.run
  lines: 183-206
- kind: method
  qualified_name: tests/test_edits_apply_pipeline:PassthroughClient.run_text
  lines: 209-221
- kind: method
  qualified_name: tests/test_edits_apply_pipeline:PassthroughClient.count_tokens
  lines: 224-225
- kind: class
  qualified_name: tests/test_edits_apply_pipeline:BrokenClient
  lines: 228-272
- kind: method
  qualified_name: tests/test_edits_apply_pipeline:BrokenClient.run
  lines: 234-255
- kind: method
  qualified_name: tests/test_edits_apply_pipeline:BrokenClient.run_text
  lines: 258-268
- kind: method
  qualified_name: tests/test_edits_apply_pipeline:BrokenClient.count_tokens
  lines: 271-272
- kind: function
  qualified_name: tests/test_edits_apply_pipeline:project
  lines: 276-329
- kind: class
  qualified_name: tests/test_edits_apply_pipeline:TestApplyPatchesEmpty
  lines: 332-352
- kind: method
  qualified_name: tests/test_edits_apply_pipeline:TestApplyPatchesEmpty.test_no_patches_returns_immediately
  lines: 333-339
- kind: method
  qualified_name: tests/test_edits_apply_pipeline:TestApplyPatchesEmpty.test_git_clean_after_empty_apply
  lines: 341-352
- kind: class
  qualified_name: tests/test_edits_apply_pipeline:TestApplyPatchesSuccess
  lines: 355-419
- kind: method
  qualified_name: tests/test_edits_apply_pipeline:TestApplyPatchesSuccess.test_applies_single_symbol
  lines: 356-367
- kind: method
  qualified_name: tests/test_edits_apply_pipeline:TestApplyPatchesSuccess.test_patches_deleted_after_success
  lines: 369-378
- kind: method
  qualified_name: tests/test_edits_apply_pipeline:TestApplyPatchesSuccess.test_no_git_commit_created
  lines: 380-394
- kind: method
  qualified_name: tests/test_edits_apply_pipeline:TestApplyPatchesSuccess.test_applies_in_topo_order
  lines: 396-403
- kind: method
  qualified_name: tests/test_edits_apply_pipeline:TestApplyPatchesSuccess.test_cascaded_no_change_skips_write
  lines: 405-419
- kind: class
  qualified_name: tests/test_edits_apply_pipeline:TestApplyPatchesFailure
  lines: 422-455
- kind: method
  qualified_name: tests/test_edits_apply_pipeline:TestApplyPatchesFailure.test_compile_error_returns_failure
  lines: 423-431
- kind: method
  qualified_name: tests/test_edits_apply_pipeline:TestApplyPatchesFailure.test_rollback_restores_files
  lines: 433-444
- kind: method
  qualified_name: tests/test_edits_apply_pipeline:TestApplyPatchesFailure.test_patches_preserved_after_rollback
  lines: 446-455
- kind: function
  qualified_name: tests/test_edits_apply_pipeline:test_apply_report_has_post_apply_actions_block
  lines: 458-476
incoming_refs: 0
outgoing_refs: 74
---
<!-- trie:section symbol=tests/test_edits_apply_pipeline:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=749ce6ff9fae10110ed0ce09ad8ceaf01562e0e5201b12a9bf0aa263eb32abec source_ref=561fe032a463723a9caeb0fc7ff996886e2079de role=test-infrastructure -->
Integration tests for the patch application pipeline, including success and failure scenarios.

- Provides fake LLM clients that simulate different edit behaviors for testing
- Tests patch application on a multi-module project with dependency chains
- Verifies git state management, rollback behavior, and patch persistence
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:PROJECT_TOML fingerprint=ea44d5615a2611cc14e40b5b84f8141a4679269bc80e3914e4fef0417f24d38b body_fp=6bc17377cf96f654791382bda48f43935de1709bffa0a7edddf2f1fc3b3ca381 source_ref=561fe032a463723a9caeb0fc7ff996886e2079de role=test-infrastructure -->
TOML configuration string for test projects with standard trie settings and anthropic model configuration.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:_git fingerprint=9efa6f55f9332a871587d0a9f0d4447d61f49c18b4d819e91e90494d14cf2f16 body_fp=afa5d09a81712692932723dba75ed50d3ac76c89dea5d9ede3460826133376cf source_ref=561fe032a463723a9caeb0fc7ff996886e2079de role=test-infrastructure -->
Execute git command in specified directory with error checking and output capture.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:_init_repo fingerprint=e6a8e59044cd4691a616ada677408e96c9c856caafae13744c548e08d2b462be body_fp=aba03cad55653bb44ec3f1480c3be12a6e06cbf0092c0e6bde928fc2f7ece7e8 source_ref=561fe032a463723a9caeb0fc7ff996886e2079de role=test-infrastructure -->
Initializes a git repository at the given path with test user configuration.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:_extract_old_source fingerprint=bcd11656d8918f3fa2184a028c94523c815515e979b154d01009499a9c24e786 body_fp=21fbe5657e27993cad0ee035379fb0c92f0c5be2988afd74c8ee3da596f62e77 source_ref=561fe032a463723a9caeb0fc7ff996886e2079de role=test-infrastructure -->
Extracts Python source code from a markdown code block within an LLM prompt string.

- Finds content between ```python and ``` markers
- Skips empty lines and strips trailing newline
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:_extract_old_prose fingerprint=8717c70ea434bf53fc16753b5930da9e782d3e0318ae3bee95b278c5667c8450 body_fp=17888bbb0e1f955c7c2992c686c866608b24433fb3111f380caa66c32a9bc2ef source_ref=561fe032a463723a9caeb0fc7ff996886e2079de role=test-infrastructure -->
Extracts documented prose from an LLM infer prompt by finding the "Old prose" section.

- Returns empty string if the prose marker is not found
- Splits content between prose marker and "Implementation notes" section
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:_is_merge_prompt fingerprint=13df75d98109396ebce3eeae9f2acd9b95400180791f4b8d1b4d6a5d780269ca body_fp=fdfaf6c19087f0e22cacc45883906e8a3e91442a43c1b5de01833e422d265592 source_ref=561fe032a463723a9caeb0fc7ff996886e2079de role=test-infrastructure -->
Determines if a prompt string is for merging patch notes by checking for a specific marker phrase.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:_plain_edit_text fingerprint=af59e23b69158e0304fff9e943c234c915d073bc7052d8c466e123e08c3abcc9 body_fp=51ef93ec59940983027d55e89beeac6ebc26fbecb4707c0e3cebbe496e622fb7 source_ref=6176a83a45d7cb5f697f12f7d4613107e399ade4 role=util -->
Render `source` and `prose` into the fenced-block + delimited-prose format that `trie.edits.textgen` parses from `TrieClient.run_text` output.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:_make_usage fingerprint=778ea16dee0036412660edb79d77aa94f191365fcd8e9c689ed41ba866b067a1 body_fp=c2ba52a602d955b98298d3fe4cd086700011488958cda0f95658315b40ecd5c1 source_ref=561fe032a463723a9caeb0fc7ff996886e2079de role=test-infrastructure -->
Creates a mock usage object with configurable token counts for testing LLM responses.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:FakeTriefactClient fingerprint=c11b80b954b967f6175c495c1c8d9749a556ac092e87dc5b8d01452a1bb1faf6 body_fp=e5dcc7625417bdae4954de71767899dfc1217a44753e2053058e8f1121bf689c source_ref=6176a83a45d7cb5f697f12f7d4613107e399ade4 role=test -->
Mock LLM client that returns static triefact documentation for testing sync operations.

- `run`: Returns fixed SectionBody with "Auto-generated prose" content
- `count_tokens`: Always returns 100 regardless of input
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:FakeTriefactClient.run fingerprint=aa2a88a9411d02e5505faa8a887e26efa9c481c5ae82a19d96ed33eb9a68478b body_fp=91fb01eae60c869436388da4e063f738b3bd6fd4e12f99f985110c0d98e34cf2 source_ref=6176a83a45d7cb5f697f12f7d4613107e399ade4 role=test -->
FakeTriefactClient.run returns a static ModelResult with auto-generated prose for testing triefact generation.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:FakeTriefactClient.count_tokens fingerprint=d2e54258807160cae2cd3e384f807ff7ab8c686f8c79830c0798dd9ba6b1e027 body_fp=10e86678d18ecc1d95267c251ac099688276c3bec2c17224bcc650c91af5766b source_ref=561fe032a463723a9caeb0fc7ff996886e2079de role=test-infrastructure -->
Returns a static token count of 100 for FakeTriefactClient prompt measurement.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:FakeEditClient fingerprint=3d5a65ba1ccde334fa72ea8ba1278c6a7a64cae762a0799db0d27f2b5f4645cb body_fp=0eac8950d45123fb0362d913470a2e358f900114c575ccb296d25f4ecdbcc200 source_ref=6176a83a45d7cb5f697f12f7d4613107e399ade4 role=test -->
## FakeEditClient

Mock LLM client that simulates patch application by appending `# patch-applied` to source code.

- Returns different responses based on output type: merge notes, batch filter decisions, or modified source
- `run_text` returns the same modification as plaintext format via `_plain_edit_text`
- Always returns fixed usage metrics and token counts
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:FakeEditClient.run fingerprint=bc56c6959c2a9044f8ebbe0632c45e1585f7a0f86c1f9a24568791f931915ab3 body_fp=ee7913fdb0a812d013c1f5cb07dbbe64058932a3ae85fe5945919fdb72eeed0a source_ref=6176a83a45d7cb5f697f12f7d4613107e399ade4 role=test -->
## FakeEditClient.run

FakeEditClient static method that simulates LLM edit responses by appending "# patch-applied" to extracted source code.

- Returns hardcoded MergeNotesOutput for merge operations
- Returns empty BatchFilterOutput for filter operations  
- Extracts old source from user prompt and appends patch comment for SymbolEdit outputs
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:FakeEditClient.run_text fingerprint=bda16ad3d341fd16fe21bbff7ab3a5ee3a89f0ddd91eca0525186d95edaadd77 body_fp=1e0a3ece93b8ff8250980ff2c5a8442aebb0fb33830815623695d7729bf2ed31 source_ref=6176a83a45d7cb5f697f12f7d4613107e399ade4 role=test -->
Return a `ModelResult` with plaintext-format output appending `# patch-applied` to the old source extracted from `user_prompt`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:FakeEditClient.count_tokens fingerprint=d2e54258807160cae2cd3e384f807ff7ab8c686f8c79830c0798dd9ba6b1e027 body_fp=8d06b42f4089a391f93079df1ba1b0d30ecc4f53973a5c78a5d78fe1dc9ac45f source_ref=561fe032a463723a9caeb0fc7ff996886e2079de role=test-infrastructure -->
Returns a fixed token count of 100 for FakeEditClient testing.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:PassthroughClient fingerprint=c73ac4a13d9df431500777d174e78440f4bfe4694f5d7ff896b7ef00885a13b4 body_fp=fd8d0d115db208f05fd8e30ef382ce09d6e59b8511d67bc49d32eb23c2204d51 source_ref=6176a83a45d7cb5f697f12f7d4613107e399ade4 role=test -->
Mock LLM client that returns unchanged source and prose for edit operations.

- For `SymbolEdit` outputs: extracts and returns the original source/prose from the prompt
- For `MergeNotesOutput`: returns static test notes and reasons
- For `BatchFilterOutput`: returns empty decisions list
- `run_text`: echoes old source/prose as plaintext code-gen format
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:PassthroughClient.run fingerprint=9346deca9763f8a2f77fea6524e9d1db47b6388696fe2a588f6f0a60583c161d body_fp=4b631dbcfb8fb04bf3d6f5c731dfd0834f12ee71cb6ad7352b8dc3b5dc8aed25 source_ref=6176a83a45d7cb5f697f12f7d4613107e399ade4 role=test -->
PassthroughClient.run returns existing source and prose unchanged, serving as a no-op test double for LLM editing operations.

- Returns static output for MergeNotesOutput and empty decisions for BatchFilterOutput
- Extracts and echoes back original source/prose from user_prompt for SymbolEdit requests
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:PassthroughClient.run_text fingerprint=76ab8821b266bf4ed35395f6a561152768172b56860bf56320af5a731ee3bb72 body_fp=9eecb7806bbf1fa5cd2c7ce6947bc7ab6cf6306ca4da45b445d857021953011a source_ref=6176a83a45d7cb5f697f12f7d4613107e399ade4 role=test -->
Static method on `PassthroughClient` that returns a `ModelResult` with the original source and prose extracted from `user_prompt`, unchanged, in plaintext code-gen format.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:PassthroughClient.count_tokens fingerprint=d2e54258807160cae2cd3e384f807ff7ab8c686f8c79830c0798dd9ba6b1e027 body_fp=9707104e956e15886709311289faaf04377c47e73f40ebaef3585e258cad4de7 source_ref=561fe032a463723a9caeb0fc7ff996886e2079de role=test-infrastructure -->
PassthroughClient.count_tokens returns a fixed token count of 100 for any prompt pair.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:BrokenClient fingerprint=0872e9b82ff67d8284ae7d1d0b638ff6ac4e0b2c04d50535c38967243b6c23e2 body_fp=52f164bc11706ccb378bfc5e795b93e70a05fb83cb807ba11b22f600f0d18144 source_ref=6176a83a45d7cb5f697f12f7d4613107e399ade4 role=test -->
Test double that mimics an LLM client returning syntactically invalid Python source code.

- `run` method: returns broken source "def broken(:" to simulate syntax errors in patch application
- `run_text` method: returns the same invalid source via the plaintext code-gen path
- `count_tokens` method: always returns 100 tokens for consistent test behavior
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:BrokenClient.run fingerprint=409a604a9de51871d52d433242c4dd9b14b28806674d3b6021a89db8fabf9e88 body_fp=7dac93f69a4c334a29aadafead495947c366dca44a40f3d828d203f08ee53a6e source_ref=6176a83a45d7cb5f697f12f7d4613107e399ade4 role=test -->
BrokenClient.run returns syntactically invalid Python source code to simulate LLM failures in tests.

- Returns standard outputs for MergeNotesOutput and BatchFilterOutput types
- Returns SymbolEdit with malformed source "def broken(:" for other output types
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:BrokenClient.run_text fingerprint=36a089ab590e5134d8988e36bdb74b0aee58a894948d201039c1289d1ddfd332 body_fp=d5831b2f92b18201ba5c948677f975f00eae6345a04088e19c890f7b829b7bee source_ref=6176a83a45d7cb5f697f12f7d4613107e399ade4 role=test -->
Return a `ModelResult` containing syntactically invalid Python source via the plaintext code-gen path, regardless of input.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:BrokenClient.count_tokens fingerprint=d2e54258807160cae2cd3e384f807ff7ab8c686f8c79830c0798dd9ba6b1e027 body_fp=515a99293ac625ac393e4417c3edc3cba6fbfdfac5013c7303e77655f449dee3 source_ref=561fe032a463723a9caeb0fc7ff996886e2079de role=test-infrastructure -->
BrokenClient class method that returns a fixed token count of 100 for any prompt pair.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:project fingerprint=26c6072a1e41f0d8332363602aa260b6b79e16528f847797cda935b864cc4be5 body_fp=fc4b3e6cff3ce59a3938edf4541d1b4b5a8e272d79c1b44319ce4bc94ce2bd18 source_ref=561fe032a463723a9caeb0fc7ff996886e2079de role=test-infrastructure -->
Creates a temporary project with three Python modules in a call chain, fully synced and committed to git.

* Returns a temporary project directory with src/alpha.py -> beta.py -> gamma.py chain
* Each module contains a single function that calls the next in sequence
* Project includes trie.toml config, .gitignore, and initialized git repository
* All modules are scanned and synced with fake triefacts before returning
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:TestApplyPatchesEmpty fingerprint=fe9d42f96f40e8e186b3dfcf3f116213343fed5a7b5704784a2be138c5e63695 body_fp=9751ccf169a21d9badfbb161c42652e4e77bbb685bce760dab213f72841ac946 source_ref=561fe032a463723a9caeb0fc7ff996886e2079de role=test -->
Tests apply_patches behavior when no patches exist in the store.

- `test_no_patches_returns_immediately` — verifies zero files/symbols processed and success status
- `test_git_clean_after_empty_apply` — confirms no working directory changes after empty patch run
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:TestApplyPatchesEmpty.test_no_patches_returns_immediately fingerprint=af1c83bd2eab932f81c972d6026fae8cfc67306e824f0f162b8c6f3fbf645270 body_fp=625a64b4f1f93fc5914c644ed47cae9e07f233c606a09473bab40224c250a2f1 source_ref=561fe032a463723a9caeb0fc7ff996886e2079de role=test -->
Verifies that TestApplyPatchesEmpty.apply_patches returns success with zero counts when no patches exist in the store.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:TestApplyPatchesEmpty.test_git_clean_after_empty_apply fingerprint=c5893657f0aed624008309b981a1fddcbad56f7dc907a8310567dda75f8b7c68 body_fp=1c977e4f923eae735e35b0e1a3d895805064fe168a03270196726716f754c588 source_ref=561fe032a463723a9caeb0fc7ff996886e2079de role=test -->
TestApplyPatchesEmpty.test_git_clean_after_empty_apply verifies that applying zero patches leaves the git working directory clean.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:TestApplyPatchesSuccess fingerprint=8484656371c70dea113a63d7c783db6a16e4f4c9ce1f821839d374d3fa0668c7 body_fp=7939f70f5a198d858aa6b9621396043f5ca0892c8dd04df32d70ec32d6c2f150 source_ref=561fe032a463723a9caeb0fc7ff996886e2079de role=test -->
Tests successful patch application scenarios for the apply_patches pipeline.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:TestApplyPatchesSuccess.test_applies_single_symbol fingerprint=41394e4b9a39f3cbfc1e37f0e7f7a97244e4bd498ba7cff518df0f2b1c54f445 body_fp=89323ce12bb703b57d74160e2e340f246570f5c923b821efc8f397bf07784013 source_ref=561fe032a463723a9caeb0fc7ff996886e2079de role=test -->
TestApplyPatchesSuccess.test_applies_single_symbol verifies that apply_patches successfully processes a single patch and returns success metadata.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:TestApplyPatchesSuccess.test_patches_deleted_after_success fingerprint=24be5af6c0b4e62f5f146b8e27210bd9d6650e7c3e129db0fcd9f87274221c7b body_fp=64837292d011c50e18ad76f9df00c557030e354ffe231705a86971ffe4f51d8c source_ref=561fe032a463723a9caeb0fc7ff996886e2079de role=test -->
Verifies TestApplyPatchesSuccess patches are removed from store after successful apply_patches execution.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:TestApplyPatchesSuccess.test_no_git_commit_created fingerprint=f2bc664e521f06056a3dce2808add1d4fbb73e45b9cce8e531978eaf89de20ad body_fp=816dad6c33c3f8e48dfb580c50a0f67ee885c43c14e007a7d7438fceb1d55ebf source_ref=561fe032a463723a9caeb0fc7ff996886e2079de role=test -->
Verifies TestApplyPatchesSuccess apply_patches does not create a git commit after applying patches.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:TestApplyPatchesSuccess.test_applies_in_topo_order fingerprint=83a3756abbd4ab057503ebffbda8d9858b92bb32acc1337a17ec8b865b053b14 body_fp=67b9cd89c725355304ad556849258cab12e4fd8a9fbfd1d86decd4c0c6f8e109 source_ref=561fe032a463723a9caeb0fc7ff996886e2079de role=test -->
Tests that `apply_patches` processes symbols in topological order by patching the deepest callee in a dependency chain.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:TestApplyPatchesSuccess.test_cascaded_no_change_skips_write fingerprint=923eb26667401b656cfd51d1f0237b3048e0ecc743f1081d52d1d7d9f0f9523b body_fp=feaa00679999d92e8c5ca59949eb2da1929da2894f8b137db1cf5934e761c34e source_ref=561fe032a463723a9caeb0fc7ff996886e2079de role=test -->
Verifies TestApplyPatchesSuccess behavior when cascaded symbols return unchanged source, ensuring files aren't unnecessarily rewritten.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:TestApplyPatchesFailure fingerprint=5ac26c9416b77970ac3457f98df492327a9ece1720de2c8afc2ece3626be42ff body_fp=dc16f9a86c1df0faacd06cfbcd45c45630fc9be224cea4450d0826872c86aa57 source_ref=561fe032a463723a9caeb0fc7ff996886e2079de role=test -->
Tests apply_patches failure handling including compile errors, file rollback, and patch preservation.

- `test_compile_error_returns_failure`: verifies apply_patches returns failure status when BrokenClient produces invalid syntax
- `test_rollback_restores_files`: confirms files are restored to committed state after compilation failure
- `test_patches_preserved_after_rollback`: ensures patches remain in database after failed application for retry
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:TestApplyPatchesFailure.test_compile_error_returns_failure fingerprint=7b976fafa7a1afc907025f2a67b3d835498e614f830138b4237e1b326f1dc85e body_fp=8ac75ddfa0a37d0e734f3fc2afab845ecb3ac4147926e2b1467961add6e1d7fe source_ref=561fe032a463723a9caeb0fc7ff996886e2079de role=test -->
Tests that `TestApplyPatchesFailure` `apply_patches` returns failure result when `BrokenClient` generates invalid Python syntax.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:TestApplyPatchesFailure.test_rollback_restores_files fingerprint=9c9c2b5d980a1af2036d0ade4a96141ba1d5d81042ef0ee3defc9ee40a3adecf body_fp=0a1e764aa690607797b03ec075440f003f9c07f36cb3efceab71dcff5ebbd85b source_ref=561fe032a463723a9caeb0fc7ff996886e2079de role=test -->
Verifies that TestApplyPatchesFailure restores files to their original state after patch application fails.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:TestApplyPatchesFailure.test_patches_preserved_after_rollback fingerprint=1a3f1e74c954f82a8471c620bf35e0f09bcfc22a8ac69d6e9d69acf38ff84ab4 body_fp=1a02b9997eec5c9d02ac592b4885bb5e842fe97ddb5ca703d291e2c26f2654d7 source_ref=561fe032a463723a9caeb0fc7ff996886e2079de role=test -->
Verifies TestApplyPatchesFailure patches remain in database after apply_patches failure for retry.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:test_apply_report_has_post_apply_actions_block fingerprint=f204e7e392f6d8f9ba887854bf1654e63a39d0d6a03bdb9cd91b5a85829c8c11 body_fp=31b373f130dc730cf3a8f186d98ff6c1683505aac253dfadb0b81081e545e19a source_ref=6176a83a45d7cb5f697f12f7d4613107e399ade4 role=test -->
Verify that `ApplyReport.to_dict()` includes a `post_apply_actions` block with deduplicated file list, dependency list, and module remarks.
<!-- trie:end -->