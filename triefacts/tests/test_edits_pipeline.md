---
trie_version: 0.1.9
source: tests/test_edits_pipeline.py
file_fingerprint: 22595cb1a540e07d2a01a6de15146a945299621326b20e3be889f9c386d057d8
last_synced_at: '2026-06-17T16:42:41Z'
defines:
- kind: module
  qualified_name: tests/test_edits_pipeline:__module__
  lines: 1-237
- kind: constant
  qualified_name: tests/test_edits_pipeline:PROJECT_TOML
  lines: 15-23
- kind: class
  qualified_name: tests/test_edits_pipeline:FakeTriefactClient
  lines: 26-37
- kind: method
  qualified_name: tests/test_edits_pipeline:FakeTriefactClient.run
  lines: 31-37
- kind: function
  qualified_name: tests/test_edits_pipeline:project
  lines: 41-71
- kind: function
  qualified_name: tests/test_edits_pipeline:_config
  lines: 74-77
- kind: class
  qualified_name: tests/test_edits_pipeline:TestStageNoWrites
  lines: 80-98
- kind: method
  qualified_name: tests/test_edits_pipeline:TestStageNoWrites.test_stage_does_not_touch_source
  lines: 81-90
- kind: method
  qualified_name: tests/test_edits_pipeline:TestStageNoWrites.test_empty_patches_clean_report
  lines: 92-98
- kind: class
  qualified_name: tests/test_edits_pipeline:TestCommitApplies
  lines: 101-130
- kind: method
  qualified_name: tests/test_edits_pipeline:TestCommitApplies.test_commit_writes_and_drops_patches
  lines: 102-121
- kind: method
  qualified_name: tests/test_edits_pipeline:TestCommitApplies.test_passthrough_is_noop_but_commits
  lines: 123-130
- kind: class
  qualified_name: tests/test_edits_pipeline:TestCompileGate
  lines: 133-158
- kind: method
  qualified_name: tests/test_edits_pipeline:TestCompileGate.test_broken_generation_goes_to_unresolved
  lines: 134-150
- kind: method
  qualified_name: tests/test_edits_pipeline:TestCompileGate.test_backend_failure_goes_to_unresolved
  lines: 152-158
- kind: class
  qualified_name: tests/test_edits_pipeline:TestAtomicity
  lines: 161-198
- kind: method
  qualified_name: tests/test_edits_pipeline:TestAtomicity.test_all_or_nothing_blocks_on_any_failure
  lines: 162-179
- kind: method
  qualified_name: tests/test_edits_pipeline:TestAtomicity.test_per_item_commits_the_good_one
  lines: 181-198
- kind: class
  qualified_name: tests/test_edits_pipeline:TestImportFixup
  lines: 201-236
- kind: method
  qualified_name: tests/test_edits_pipeline:TestImportFixup.test_drop_deleted_import
  lines: 202-208
- kind: method
  qualified_name: tests/test_edits_pipeline:TestImportFixup.test_remove_line_when_all_deleted
  lines: 210-215
- kind: method
  qualified_name: tests/test_edits_pipeline:TestImportFixup.test_rename_import_preserves_alias
  lines: 217-223
- kind: method
  qualified_name: tests/test_edits_pipeline:TestImportFixup.test_star_and_paren_imports_untouched
  lines: 225-230
- kind: method
  qualified_name: tests/test_edits_pipeline:TestImportFixup.test_noop_when_no_targets
  lines: 232-236
incoming_refs: 0
outgoing_refs: 33
---
<!-- trie:section symbol=tests/test_edits_pipeline:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=779d3118d360be3e6cc31619bc506e3cfef98d30e9e27ade7938a41986fc4d11 source_ref=e0282d34035b65bdf7e8d362970ae8d5376a0584 role=test -->
Tests the edits pipeline functionality including staging, committing, and import fixup operations.

- PROJECT_TOML: configuration template defining trie project structure and model settings
- FakeTriefactClient: mock client returning deterministic SectionBody for sync operations
- project: pytest fixture creating temporary project with three-module dependency chain
- TestStageNoWrites: verifies staging operations don't modify source files
- TestCommitApplies: tests successful patch application and database cleanup
- TestCompileGate: ensures broken code generation is handled as unresolved errors
- TestAtomicity: validates all-or-nothing vs per-item commit modes
- TestImportFixup: tests import statement modification for structural changes
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_pipeline:PROJECT_TOML fingerprint=ea44d5615a2611cc14e40b5b84f8141a4679269bc80e3914e4fef0417f24d38b body_fp=b7b98764eb81bf3ef9f1f482ed1f8f6147ed54d9a609a09894f8a54d83f33e9d source_ref=e0282d34035b65bdf7e8d362970ae8d5376a0584 role=test -->
TOML configuration string used as fixture data for test project setup.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_pipeline:FakeTriefactClient fingerprint=10c1d860217fcab07de3ba678d36d5663ed564e1bad97a10efd8ef14e3dec4eb body_fp=a04c0a5551995d65bda028f5916723cb44737b743d85c73468d9b9fa6efda7b1 source_ref=e0282d34035b65bdf7e8d362970ae8d5376a0584 role=test -->
Test double client that returns deterministic ModelResult with fixed prose content and usage metrics.

- `full_model_id`: Always "fake/fake"
- `run()`: Returns ModelResult with "fake prose." body and 1 input/output token usage
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_pipeline:FakeTriefactClient.run fingerprint=ddf5f4d5a413797c8ae0c5853e9d1be123cf1571583cd546aead0c3037ad7075 body_fp=1736a87e86d441fbf7c226a87fcc64371278db93fd64b5bec35da9e6b01ab2b0 source_ref=e0282d34035b65bdf7e8d362970ae8d5376a0584 role=test -->
FakeTriefactClient.run returns a deterministic ModelResult with fake prose for testing documentation generation.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_pipeline:project fingerprint=f790f2074b937f90ed8ee4a255893c84214d9160080042f169967e3d0630e0fc body_fp=34a51b2b764c5fe4cbe18f8330f810d4e7a094de0dfb8d2de4bc2b6364d24cd0 source_ref=e0282d34035b65bdf7e8d362970ae8d5376a0584 role=test -->
Creates a test project with three Python files in a dependency chain and pre-populates the trie graph database.

- Returns the temporary project root directory path
- Creates src/alpha.py → src/beta.py → src/gamma.py call chain
- Writes trie.toml configuration and .gitignore files
- Scans project and syncs all files to populate graph store with fake triefacts
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_pipeline:_config fingerprint=2212d2ec1f6d36b65a66e8e256c0410684c26b19d40509bd6f5469cf10d0fcd7 body_fp=75bc670a33c5169f6b44d9565ffd59d553fa170565a26a9c54d26ca9dcdfdb3e source_ref=e0282d34035b65bdf7e8d362970ae8d5376a0584 role=test -->
Creates test Config from project path with LSP backends disabled for unit testing.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_pipeline:TestStageNoWrites fingerprint=6d4a2bd7881aeba99043f361adf36e7441c4646b46c48dccb683a520d7946a3f body_fp=d1e187e8d7b0921ff3445a27c4ad5c63ac58f695e502a525b3961f90f9ae62b5 source_ref=e0282d34035b65bdf7e8d362970ae8d5376a0584 role=test -->
Tests that the stage function prepares edits without modifying source files.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_pipeline:TestStageNoWrites.test_stage_does_not_touch_source fingerprint=024c7341e523c2bfb1f2cf7d22016c998848746886c0640ef6a1ab2ab88001a9 body_fp=8d1245939a903726af5bc2654e4bcafd457b0e04265c2aa156c174693027879f source_ref=e0282d34035b65bdf7e8d362970ae8d5376a0584 role=test -->
Verifies that `stage()` prepares edits without modifying source files on disk.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_pipeline:TestStageNoWrites.test_empty_patches_clean_report fingerprint=866abcbbc733fc1cb730880d527d75c7f3e4e63824a8f66d3228292a64635177 body_fp=ba150e7ff054196119615cf127274837a186fb8f0bace56cab4f93c95f2e82cf source_ref=e0282d34035b65bdf7e8d362970ae8d5376a0584 role=test -->
TestStageNoWrites.test_empty_patches_clean_report verifies that staging with no patches produces a clean success report.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_pipeline:TestCommitApplies fingerprint=b29497451100629d15a5aea38952f7809423ef5ce753254a055aa8169cbf1b72 body_fp=f20a54aa40765162418515de9b7467d39a412b5f97f3885baa3275ad1506f700 source_ref=e0282d34035b65bdf7e8d362970ae8d5376a0584 role=test -->
Tests that the `stage_and_commit` function properly commits patches and updates source files.

- `test_commit_writes_and_drops_patches`: verifies patches are applied to files and removed from store
- `test_passthrough_is_noop_but_commits`: confirms passthrough backend commits without modifying source
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_pipeline:TestCommitApplies.test_commit_writes_and_drops_patches fingerprint=8b7ae630111ff4c70bb85bddd42b1eeca757681223dd768876dd844787f6c170 body_fp=38a89f00fe2595bdde1ae133724d97fa913b0bc8349732d6e2f8f2b314393dfa source_ref=e0282d34035b65bdf7e8d362970ae8d5376a0584 role=test -->
Verifies TestCommitApplies that stage_and_commit successfully applies patches, writes to source files, and removes patches from store.

- Checks that source file contains the fake edit text after commit
- Confirms patch is removed from store after successful application  
- Validates non-blocking second-order cascade warnings are generated for callers
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_pipeline:TestCommitApplies.test_passthrough_is_noop_but_commits fingerprint=62e77463634b6ec105f24c43f26547dddf186c4324a633e6bed64d7ec7db1b7d body_fp=a6a8c782beb237096a24c204b6f6d5ae3508410612af3150d6bf77662d42594f source_ref=e0282d34035b65bdf7e8d362970ae8d5376a0584 role=test -->
Tests that TestCommitApplies passthrough backend commits patches without modifying source files.

- Uses FakeBackend in "passthrough" mode to simulate no-op edits
- Verifies file content remains unchanged after commit
- Confirms report indicates successful operation
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_pipeline:TestCompileGate fingerprint=3f5660f99c485d8e3670acbc4c5df56bc58b99fe74309be7fc41370fe91efd2c body_fp=5b40d0855ee3356725df69b67c69db7e88a77adb78da6bc247a1bfc90f8c7173 source_ref=e0282d34035b65bdf7e8d362970ae8d5376a0584 role=test -->
Tests that compilation failures during edit application block commits and preserve patches for retry.

- `test_broken_generation_goes_to_unresolved`: Verifies syntax error patches go to unresolved with retry metadata
- `test_backend_failure_goes_to_unresolved`: Confirms backend failures are captured as blocking unresolved items
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_pipeline:TestCompileGate.test_broken_generation_goes_to_unresolved fingerprint=ffbaa44dc487fdf65eec3fbd540edabf1b20bd641ef5b7362800a8fdb6bde385 body_fp=fed8cc1f907e8b4d7ddfbb1526cdba9da580a8366e2a0f1d2d0a1a24c3e17078 source_ref=e0282d34035b65bdf7e8d362970ae8d5376a0584 role=test -->
Tests that syntactically broken code generation creates unresolved blocking issues without committing changes.

- Verifies source files remain untouched when generation fails
- Checks patches are preserved in store for retry
- Confirms blocking unresolved items have syntax_error_after_retry_cap code
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_pipeline:TestCompileGate.test_backend_failure_goes_to_unresolved fingerprint=e91df77007454f5894130e6b741b13ed24d467e032edc54507c46cc94912234d body_fp=4356c97558d03e942c2826c2a0792a8aa39b8da33791def7ff5ee485072a0341 source_ref=e0282d34035b65bdf7e8d362970ae8d5376a0584 role=test -->
Tests that TestCompileGate handles backend failures by marking them as blocking unresolved items.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_pipeline:TestAtomicity fingerprint=1aff288eb2948a2be49ca0cf8fc652cae3ffccdb59ab8e8c6679ec95a6077de0 body_fp=83ab7c06457299d9da54bc1f5a10d923c20a40a31a0b837516290aa3cdc63e8e source_ref=e0282d34035b65bdf7e8d362970ae8d5376a0584 role=test -->
Tests commit atomicity behavior for different failure modes in the edits pipeline.

- `all_or_nothing` mode: blocks all commits when any edit fails, preserving original source
- `per_item` mode: commits successful edits while leaving failures in unresolved state
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_pipeline:TestAtomicity.test_all_or_nothing_blocks_on_any_failure fingerprint=6c71c8c7fbe208129d9cd19b34c381d6c1a85ebcec640d2c22949ab7e37bcf0a body_fp=549eec3518d6ac967968c3015d029e2708c5a8fdec7dd72984333983bed0a076 source_ref=e0282d34035b65bdf7e8d362970ae8d5376a0584 role=test -->
Verifies TestAtomicity all-or-nothing commit mode prevents any writes when one patch fails.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_pipeline:TestAtomicity.test_per_item_commits_the_good_one fingerprint=c3b92b873963cf69b2566a4d1cc7928ffc9b3461ca72465fb0da3d398fb9ce96 body_fp=a272a3306ba145bdfeb1f851e43c2f43b6d4cd0c2e1c6b63d032395233ab01f8 source_ref=e0282d34035b65bdf7e8d362970ae8d5376a0584 role=test -->
Tests that TestAtomicity per-item commit mode applies successful patches while leaving failed ones unresolved.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_pipeline:TestImportFixup fingerprint=3582cef186a3249885ad3b14f2bf80e4ca03082ede2bc9644f630116788f2775 body_fp=2dc55933be73e9bfd1e4b6dc6b446f40fce8848fcd7640163e1bcf625a4ca37b source_ref=e0282d34035b65bdf7e8d362970ae8d5376a0584 role=test -->
Tests import cleanup logic for automatically fixing import statements after structural code changes.

- test_drop_deleted_import: removes deleted names from multi-name import statements
- test_remove_line_when_all_deleted: removes entire import line when all names deleted
- test_rename_import_preserves_alias: updates renamed imports while preserving aliases
- test_star_and_paren_imports_untouched: skips complex import formats for safety
- test_noop_when_no_targets: returns source unchanged when no modifications needed
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_pipeline:TestImportFixup.test_drop_deleted_import fingerprint=8bb781c57ba37c7fdf98cd3e57200c753612c582e214b75761e3bdbe004f9876 body_fp=6dc1caa4a748ead6f758616fc5138b4bc799d70a2347e60965c1a14c4eb98d8f source_ref=e0282d34035b65bdf7e8d362970ae8d5376a0584 role=test -->
Verifies `_fix_imports_for_structural` removes deleted symbols from multi-name import statements while preserving remaining names.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_pipeline:TestImportFixup.test_remove_line_when_all_deleted fingerprint=013447549a5af9366fb29145a242c4ea15a17e1a6e7ad0009f298c5fbe2c4f0a body_fp=70c28245a17f953de2e87b37cd8667d59e40a26afaafaaa2aecb69d470ce2498 source_ref=e0282d34035b65bdf7e8d362970ae8d5376a0584 role=test -->
Verifies that `_fix_imports_for_structural` removes entire import lines when all imported names are deleted.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_pipeline:TestImportFixup.test_rename_import_preserves_alias fingerprint=0aa5f856b59e284a795d6caa4ca2db98973663e5295efa3a4d3b24b848ca7bf5 body_fp=c923e51eaa19d2574c9e90309eeddfe4f34d586ae41d0438010363ea2538fa68 source_ref=e0282d34035b65bdf7e8d362970ae8d5376a0584 role=test -->
Verifies that TestImportFixup._fix_imports_for_structural preserves alias syntax when renaming imported symbols.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_pipeline:TestImportFixup.test_star_and_paren_imports_untouched fingerprint=77845e06e325bccaee483ad3593672fabd564fb305d6ee6eb02410f376dc1e72 body_fp=865591ec7f5cbe78d00c7421076944b4ecc5c75056a8d6c26dbcf9ac5b88be81 source_ref=e0282d34035b65bdf7e8d362970ae8d5376a0584 role=test -->
Tests that TestImportFixup._fix_imports_for_structural leaves star imports and parenthesized imports unchanged.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_pipeline:TestImportFixup.test_noop_when_no_targets fingerprint=674bc9e3aced5ca1a826ba7506c44b9f8a09d4afe8d77884ec3b5ec8d498ab3a body_fp=27d394c575fa94a627d48cb9bc539c20aa35ecad9e8db9a7bb0bc0fecfffc3d1 source_ref=e0282d34035b65bdf7e8d362970ae8d5376a0584 role=test -->
Verifies TestImportFixup behavior when no names need deletion or renaming by ensuring source remains unchanged.
<!-- trie:end -->