---
trie_version: 0.1.9
source: tests/test_edits_structural.py
file_fingerprint: e8332ae1082b9044a9f3d3ac570bd7dd1092f4fcc03c0985bdf210aa804e9159
last_synced_at: '2026-07-25T01:56:25Z'
defines:
- kind: module
  qualified_name: tests/test_edits_structural:__module__
  lines: 1-454
- kind: constant
  qualified_name: tests/test_edits_structural:PROJECT_TOML
  lines: 16-24
- kind: class
  qualified_name: tests/test_edits_structural:FakeTriefactClient
  lines: 27-36
- kind: method
  qualified_name: tests/test_edits_structural:FakeTriefactClient.run
  lines: 30-36
- kind: function
  qualified_name: tests/test_edits_structural:project
  lines: 40-60
- kind: function
  qualified_name: tests/test_edits_structural:class_project
  lines: 64-93
- kind: function
  qualified_name: tests/test_edits_structural:_config
  lines: 96-99
- kind: class
  qualified_name: tests/test_edits_structural:TestDelete
  lines: 102-115
- kind: method
  qualified_name: tests/test_edits_structural:TestDelete.test_delete_removes_symbol_source
  lines: 103-115
- kind: class
  qualified_name: tests/test_edits_structural:TestRename
  lines: 118-144
- kind: method
  qualified_name: tests/test_edits_structural:TestRename.test_rename_updates_definition
  lines: 119-131
- kind: method
  qualified_name: tests/test_edits_structural:TestRename.test_rename_invalid_identifier_refused
  lines: 133-144
- kind: class
  qualified_name: tests/test_edits_structural:TestCreate
  lines: 147-324
- kind: method
  qualified_name: tests/test_edits_structural:TestCreate.test_create_adds_new_symbol
  lines: 148-167
- kind: method
  qualified_name: tests/test_edits_structural:TestCreate.test_create_unreferenced_surfaces_orphan_advisory
  lines: 169-184
- kind: method
  qualified_name: tests/test_edits_structural:TestCreate.test_create_in_missing_file_creates_new_file
  lines: 186-205
- kind: method
  qualified_name: tests/test_edits_structural:TestCreate.test_create_in_missing_nested_dir_creates_dirs
  lines: 207-221
- kind: method
  qualified_name: tests/test_edits_structural:TestCreate.test_create_method_into_class
  lines: 223-241
- kind: method
  qualified_name: tests/test_edits_structural:TestCreate.test_modify_and_create_method_same_file
  lines: 243-272
- kind: method
  qualified_name: tests/test_edits_structural:TestCreate.test_create_broken_source_unresolved
  lines: 274-288
- kind: method
  qualified_name: tests/test_edits_structural:TestCreate.test_one_broken_create_does_not_poison_siblings
  lines: 290-324
- kind: class
  qualified_name: tests/test_edits_structural:TestSameFileMultiLane
  lines: 327-382
- kind: method
  qualified_name: tests/test_edits_structural:TestSameFileMultiLane.test_modify_and_create_same_file_both_land
  lines: 336-358
- kind: method
  qualified_name: tests/test_edits_structural:TestSameFileMultiLane.test_rename_and_create_same_file_both_land
  lines: 360-382
- kind: function
  qualified_name: tests/test_edits_structural:two_file_project
  lines: 386-408
- kind: class
  qualified_name: tests/test_edits_structural:TestStructuralCascade
  lines: 411-453
- kind: method
  qualified_name: tests/test_edits_structural:TestStructuralCascade.test_delete_cascades_to_caller
  lines: 414-433
- kind: method
  qualified_name: tests/test_edits_structural:TestStructuralCascade.test_rename_cascades_to_caller
  lines: 435-453
incoming_refs: 0
outgoing_refs: 59
---
<!-- trie:section symbol=tests/test_edits_structural:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=ec4390bf15b62b6613a0fe71e4d18d40ff73d943dbe459bd79fd9fcc22ef1ea5 source_ref=7ec0dea07e040aeeb4ffb2574d8059b351722a41 role=test -->
Tests structural edit operations (delete, rename, create) and their cascading effects on dependent symbols.

- **FakeTriefactClient**: Mock client returning fixed SectionBody for testing edit workflows
- **TestDelete**: Verifies symbol deletion removes source code and updates graph state
- **TestRename**: Tests symbol renaming updates definitions and validates identifier rules
- **TestCreate**: Validates new symbol creation and handles orphan/missing file cases
- **TestSameFileMultiLane**: Ensures multiple edit types on same file don't clobber each other
- **TestStructuralCascade**: Confirms delete/rename operations propagate to calling symbols
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_structural:PROJECT_TOML fingerprint=ea44d5615a2611cc14e40b5b84f8141a4679269bc80e3914e4fef0417f24d38b body_fp=9ff0adf0cd865110015300c9a86ec5079b3db04c9f235fbc57ed6b724a00a750 source_ref=7ec0dea07e040aeeb4ffb2574d8059b351722a41 role=test -->
TOML configuration string used to create test project files with trie settings.

- Contains project metadata, file scope, triefacts root, model configurations, and cascade parameters
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_structural:FakeTriefactClient fingerprint=eb21c1c8e78d2dfbdaa15ef552db52c7f8e034d8a0e48c02c7d739e2f9ea2007 body_fp=9c8baad9c45962ae43b28d29c8fb15fa3a126ebc6630e465f9ae4cf582bfbd6d source_ref=01fd81b7592a75ad72d9df519738f35a592ec6b7 role=test -->
Mock triefact client that returns fixed SectionBody output with minimal token usage for testing.

- `full_model_id`: Always returns "fake/fake"
- `run()`: Returns ModelResult with hardcoded "fake prose." body and 1 input/output token usage
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_structural:FakeTriefactClient.run fingerprint=245921977f71d8c42c7796c61eaf884795f199a0f58fd762bbeb242de7e54a6b body_fp=f1f667bb1c44fd8cc7ea44d1a7da7aaaffba3738dd2ff6507f9224481de9f7c7 source_ref=01fd81b7592a75ad72d9df519738f35a592ec6b7 role=test -->
FakeTriefactClient.run returns a fake ModelResult with hardcoded SectionBody and minimal Usage for testing.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_structural:project fingerprint=454ba7d4fb51d84562aa6b26ddbe62b83dd544935bc4f7d0a049e3dffac6c82b body_fp=b141eef4f01e37f9e57370b09fa5121a37b77bbee77a82537bd958f30e212b96 source_ref=7ec0dea07e040aeeb4ffb2574d8059b351722a41 role=test -->
Creates a pytest fixture providing a temporary project directory with a single Python source file and initialized trie store.

- Returns the project root path containing `src/gamma.py` with a `gamma_fn` function
- Scans the project and syncs the source file to populate the graph database
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_structural:class_project fingerprint=9975b7647a4660cd668e962049db5fb8fc644fa6ce8446794f3d93d353927e85 body_fp=6c4df08bcf69f133de46ca9c9a1308b7eb209aeaab1e1be3c446d4d3c7723c86 source_ref=3105a5fed65ee67fcfa8304d60b02f219c503b9a role=test -->
Pytest fixture that creates a temporary project containing a `Box` class with `__init__` and `area` methods, scanned and synced into the graph store.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_structural:_config fingerprint=2212d2ec1f6d36b65a66e8e256c0410684c26b19d40509bd6f5469cf10d0fcd7 body_fp=a9ace222b40bbaec93fded0181aea6ca255a809983bbc262c902dace9ca4711a source_ref=7ec0dea07e040aeeb4ffb2574d8059b351722a41 role=test -->
Loads project config and disables LSP backends for test isolation.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_structural:TestDelete fingerprint=13c27806a9a5f8b2f121a307fa15546a21b4af5ce6b8550f1dad42915738f51d body_fp=cf99b34e29f63f721c43c93a7db6c87b582734bc6dfe4391f598f876cd4f05d9 source_ref=7ec0dea07e040aeeb4ffb2574d8059b351722a41 role=test -->
Tests deletion of symbols from source files and the store.

Contains `test_delete_removes_symbol_source` which verifies that deleting a symbol removes it from both source code and the graph database.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_structural:TestDelete.test_delete_removes_symbol_source fingerprint=1cf737bab5a9c8d8ccf1fe4da17089b8b4b0de5375b83bfc8b4895eb655e8902 body_fp=fb6c854dec592f79691a3c5e98ca80f761471e1c1a8ba711fb1fbeb7816185aa source_ref=7ec0dea07e040aeeb4ffb2574d8059b351722a41 role=test -->
Tests that TestDelete successfully removes a symbol's source code from the file and graph after staging a delete patch.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_structural:TestRename fingerprint=c71f6160c954d711831d993aa2495a41e527eb72ededd3d04722616cccf60a5c body_fp=1db4fd3f18bdb1390801cf59f118c2b2e6b54aa53f9d4c4ed4321a33e3d7b477 source_ref=7ec0dea07e040aeeb4ffb2574d8059b351722a41 role=test -->
Tests rename operation functionality in the structural edits pipeline.

- `test_rename_updates_definition`: verifies successful rename updates symbol definition and graph state
- `test_rename_invalid_identifier_refused`: confirms invalid identifiers are rejected without modifying source
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_structural:TestRename.test_rename_updates_definition fingerprint=48eb98d06afe8eee4295ab48724871b35df290006dc027a0d485a5b40b421314 body_fp=ac8a655b7d2440c1fc53d38bf59605c066e4a37671de42a53914a94aba3f4772 source_ref=7ec0dea07e040aeeb4ffb2574d8059b351722a41 role=test -->
Tests that TestRename.test_rename_updates_definition successfully renames a symbol from gamma_fn to deepest and updates the source file definition.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_structural:TestRename.test_rename_invalid_identifier_refused fingerprint=57e59f916770158d6ba6b634fc811e72798f0dd348a236e3096c1d60d30b56d9 body_fp=c9e93069edc8f50f12c417057de0e779a8a7051a1df1f52d62aaa714b5520ad2 source_ref=7ec0dea07e040aeeb4ffb2574d8059b351722a41 role=test -->
Tests that TestRename rejects rename operations with invalid Python identifiers and leaves source unchanged.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_structural:TestCreate fingerprint=f569c02184cd2205c1d2dfd4b8aac22f5a4969d9ae8573813171eae391d6071d body_fp=88a25fc72fe52133d0f3afe6db9c424c9922207c046bac8c68c1d3b93f9b8b26 source_ref=01fd81b7592a75ad72d9df519738f35a592ec6b7 role=test -->
Tests the create symbol pipeline functionality for adding new code symbols to project files.

- `test_create_adds_new_symbol`: verifies successful symbol creation and graph absorption
- `test_create_unreferenced_surfaces_orphan_advisory`: checks orphaned symbols generate non-blocking advisories
- `test_create_in_missing_file_creates_new_file`: verifies missing target file is scaffolded on disk, not rejected
- `test_create_in_missing_nested_dir_creates_dirs`: verifies parent directories are created when needed
- `test_create_method_into_class`: verifies class-method qnames land indented inside the class body
- `test_modify_and_create_method_same_file`: verifies same-file modify+create batch both land and remain valid Python
- `test_create_broken_source_unresolved`: validates broken source generation fails gracefully
- `test_one_broken_create_does_not_poison_siblings`: verifies a broken create in a batch (per-item mode) does not block sibling creates in the same file
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_structural:TestCreate.test_create_adds_new_symbol fingerprint=ce45f65576c6133efc3cc120623a8732f17d1e2a86e4c8fb9d07f91ff6d23bc7 body_fp=4de79f7fee80af0db5807a12621a55335e2abfa68b74d7af301a3d81eca45109 source_ref=7ec0dea07e040aeeb4ffb2574d8059b351722a41 role=test -->
Tests that TestCreate successfully stages and commits a create patch, adding a new symbol to source.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_structural:TestCreate.test_create_unreferenced_surfaces_orphan_advisory fingerprint=9de47d73c65141508085a52204f32096c7926549ff7658d765df8f61d2954c0c body_fp=934bb6e75c49972c0fa6c91b536eb6d30aa6da1fbc1ea7f15f3cf9f2c9583837 source_ref=7ec0dea07e040aeeb4ffb2574d8059b351722a41 role=test -->
Tests that creating a symbol with no callers generates a non-blocking orphan_create advisory in the commit report.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_structural:TestCreate.test_create_in_missing_file_creates_new_file fingerprint=40dd7e9c8e3b351eccc4c43bd101ebec72b3c300fb103b0aede8a180f8e18836 body_fp=6883d2f144cc914e42c280cb70e63c00a98b29682718f486d80348533273728e source_ref=3105a5fed65ee67fcfa8304d60b02f219c503b9a role=test -->
Assert that `TestCreate.test_create_in_missing_file_creates_new_file` scaffolds a new source file when a create patch targets a path that does not yet exist, without raising a blocking `file_not_found` unresolved item.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_structural:TestCreate.test_create_in_missing_nested_dir_creates_dirs fingerprint=3ff41f9b142d06ab9409ba7cc2db61b2aeaf9f719102e7210b29e2a223cb3f51 body_fp=375c35327a9c167ff30a2e50447ca7c5ffb90b1a824f8eb20a549bb57f910ebd source_ref=3105a5fed65ee67fcfa8304d60b02f219c503b9a role=test -->
Verify `TestCreate` that a create patch targeting a file in a non-existent subdirectory causes `stage_and_commit` to create all intermediate parent directories and the file.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_structural:TestCreate.test_create_method_into_class fingerprint=138ea81f05cd1c54b0a8def41c87ae94eeff82771ed2d8d2d7a8fc4642239335 body_fp=59ada17876eeccb00293537d3cfcae880bda4bbfb9cee31268e94bbcd705ef84 source_ref=3105a5fed65ee67fcfa8304d60b02f219c503b9a role=test -->
Assert that a create patch with a `Class.method` qname inserts the new method inside the class body, indented as a class member.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_structural:TestCreate.test_modify_and_create_method_same_file fingerprint=a24013ec14a88522b3c4ef74cddd50bb29849e0ae0567de5cdbf57566833b47a body_fp=8e7c2d1cc81cb8e335fe1b356a5dd821836db7c80bd685d75b4089e8783b5c74 source_ref=3105a5fed65ee67fcfa8304d60b02f219c503b9a role=test -->
Verify that a same-file batch combining a method modify and a method create both land and leave the file valid Python.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_structural:TestCreate.test_create_broken_source_unresolved fingerprint=edb4eda89216f719f240104fb4339537d1fed662a7f3bc41a3ba3e0ba06a3715 body_fp=3846918c836b6bccdcbfdb7dbd9c438fc0f04003d9efee0419146e012d4f1327 source_ref=7ec0dea07e040aeeb4ffb2574d8059b351722a41 role=test -->
TestCreate.test_create_broken_source_unresolved tests that create patches fail gracefully when backend generates broken code, leaving source unchanged.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_structural:TestCreate.test_one_broken_create_does_not_poison_siblings fingerprint=cf9343fe16434441cfccc71f06336eee56d2fc80353a47104713ed0c986a126b body_fp=c0faae60e66dae6806423d0b1c63875c934d8a9efed01b19f45fa8a4799e56a2 source_ref=01fd81b7592a75ad72d9df519738f35a592ec6b7 role=test -->
Assert that a compile-failing create patch in `TestCreate` does not prevent a sibling create patch in the same file from being committed.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_structural:TestSameFileMultiLane fingerprint=ac56c203e373f07bac8a2d74a1a58a00235b88779d064c93afc3e70c2d1156bd body_fp=2505185dd0228673814047ba26ed16b41e67b7d54b49d6b9299506cdf440f572 source_ref=7ec0dea07e040aeeb4ffb2574d8059b351722a41 role=test -->
Tests that multiple edit operations on the same file don't overwrite each other's changes.

- Regression test for a bug where create operations overwrote modify/structural edits
- Each test verifies that both operations land in the final file content
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_structural:TestSameFileMultiLane.test_modify_and_create_same_file_both_land fingerprint=99b5774b3b0cb0ce8618f108477caaa16ee3d7917e9967514510623b437ff2eb body_fp=cc2bf834e36c9f1926ad65611a66752940946684026a4d3a962be3cbb5fbe46a source_ref=7ec0dea07e040aeeb4ffb2574d8059b351722a41 role=test -->
Tests that TestSameFileMultiLane can apply both modify and create patches to the same file without clobbering each other.

- Adds both a modify patch for `gamma_fn` and a create patch for a `helper` function in the same file
- Verifies both changes appear in the final file content after staging and committing
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_structural:TestSameFileMultiLane.test_rename_and_create_same_file_both_land fingerprint=e444d21f3531b6f628154b8774b7903866356a255d1b78caefe20a59f64d35c5 body_fp=78cb31cc746944aa1c548c39dfdf55f30e62a59efbf0d339a09b6e5c0b8eadb9 source_ref=7ec0dea07e040aeeb4ffb2574d8059b351722a41 role=test -->
Tests that TestSameFileMultiLane can successfully apply both rename and create patches to the same file without conflicts.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_structural:two_file_project fingerprint=a5b6ec0b277b6d65002eccf2c85472a4096dfb4363590d1d20cb6148ef25a07f body_fp=868c4b2aea1a43f589f62d1a8aff1cd8b9f76000b26661159a2e448e0389e105 source_ref=7ec0dea07e040aeeb4ffb2574d8059b351722a41 role=test -->
Creates a pytest fixture with a two-file project where caller.py imports and calls target() from callee.py.

- Returns temporary project directory with scanned graph data and synced triefacts
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_structural:TestStructuralCascade fingerprint=a447cb56043cfced69d27a79e9ae745a5747f3552616e174b40e84218b719851 body_fp=55669a0108e04ef214e5f5cb7180d6dbb1bf18822144c49b76f744a687dc826b source_ref=7ec0dea07e040aeeb4ffb2574d8059b351722a41 role=test -->
Tests that delete and rename operations automatically cascade to update caller sites.

- `test_delete_cascades_to_caller`: Verifies delete operation triggers cascade edits to remove broken imports
- `test_rename_cascades_to_caller`: Verifies rename operation triggers cascade edits to update import statements
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_structural:TestStructuralCascade.test_delete_cascades_to_caller fingerprint=76fcc20d1031ff633a476bf0a0fd34949983ce1814a8792305c35d6844a32dc6 body_fp=e7d09b56db3725298bdf8c1e063d5ee367419be225fdc0c912f6e76e3efff8ca source_ref=7ec0dea07e040aeeb4ffb2574d8059b351722a41 role=test -->
TestStructuralCascade.test_delete_cascades_to_caller tests that deleting a symbol automatically triggers cascade edits to update its callers.

- Verifies the caller receives an edit (via "trie-fake-edit" marker from FakeBackend)
- Confirms broken imports to the deleted symbol are removed
- Asserts both delete and cascade operations appear in the commit report
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_structural:TestStructuralCascade.test_rename_cascades_to_caller fingerprint=7f51747b3d0e619b3ce75c20d95d971f896264bcb2aaa9ea58104593bc905dbd body_fp=f519084130d4e7157dc2a0e289b11b1ee75095370de7dbe52feab4f3634c3669 source_ref=7ec0dea07e040aeeb4ffb2574d8059b351722a41 role=test -->
Tests that renaming a symbol cascades edits to update import statements and references in calling files.
<!-- trie:end -->