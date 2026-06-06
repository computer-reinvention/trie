---
trie_version: 0.1.5
source: tests/test_roles.py
file_fingerprint: ff86cc085fcd8cb0287a107ab29a87127a6330b72afa35c176e26f4d9c1e8e1c
last_synced_at: '2026-06-06T13:44:36Z'
description: 'Tests for role tagging: durable persistence, derived taxonomy, and the'
defines:
- kind: module
  qualified_name: tests/test_roles:__module__
  lines: 1-279
- kind: function
  qualified_name: tests/test_roles:test_section_role_round_trips_through_render_and_parse
  lines: 32-46
- kind: function
  qualified_name: tests/test_roles:test_section_without_role_omits_the_field
  lines: 49-54
- kind: function
  qualified_name: tests/test_roles:test_set_section_role_only_changes_the_role
  lines: 57-69
- kind: function
  qualified_name: tests/test_roles:test_set_section_role_missing_symbol_returns_false
  lines: 72-74
- kind: function
  qualified_name: tests/test_roles:test_taxonomy_save_load_round_trip
  lines: 82-92
- kind: function
  qualified_name: tests/test_roles:test_load_taxonomy_absent_returns_none
  lines: 95-97
- kind: function
  qualified_name: tests/test_roles:test_load_taxonomy_malformed_returns_none
  lines: 100-105
- kind: function
  qualified_name: tests/test_roles:test_derive_taxonomy_returns_proposed_roles
  lines: 113-122
- kind: function
  qualified_name: tests/test_roles:test_run_roles_only_persists_to_disk_and_db
  lines: 131-151
- kind: function
  qualified_name: tests/test_roles:test_roles_survive_db_wipe_via_disk_restore
  lines: 154-174
- kind: function
  qualified_name: tests/test_roles:test_run_roles_only_only_missing_short_circuits
  lines: 177-201
- kind: function
  qualified_name: tests/test_roles:test_infer_role_clamps_to_vocabulary
  lines: 204-216
- kind: function
  qualified_name: tests/test_roles:_write_config
  lines: 224-234
- kind: function
  qualified_name: tests/test_roles:_git
  lines: 237-238
- kind: function
  qualified_name: tests/test_roles:project
  lines: 242-256
- kind: function
  qualified_name: tests/test_roles:_bootstrap
  lines: 259-278
incoming_refs: 0
outgoing_refs: 40
---
<!-- trie:section symbol=tests/test_roles:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=efc37c446790b90fb19c706b6873892ebfec635682dd8fe6bdbe931e995f2a52 source_ref=808f1bab7d3a9a1f792a2c387a66fa8309013b1e role=test -->
Tests for role tagging system including persistence, taxonomy derivation, and two-pass classification workflow.

- Verifies roles survive parse-render round-trips in triefact files
- Tests taxonomy persistence and loading from disk
- Validates end-to-end role classification with LLM client integration
- Ensures roles persist through database wipes via disk restoration
<!-- trie:end -->
<!-- trie:section symbol=tests/test_roles:test_section_role_round_trips_through_render_and_parse fingerprint=745d9e4fa90fe1287f73b09cd9ffd50d9bedc247eb33eb98d87e7d6f9e4bc4af body_fp=6c81d14f3fa5dc2a1c7133f90a3a4f0e8ff2a218cb1422f7c9f831ba239b5589 source_ref=808f1bab7d3a9a1f792a2c387a66fa8309013b1e role=test -->
## `test_section_role_round_trips_through_render_and_parse`

Verifies that role metadata survives the TriefactFile render-and-parse cycle.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_roles:test_section_without_role_omits_the_field fingerprint=7c8d288d622ffd0a9bad3cd36efafb0788a40e5449640e3122fd188fde1adde9 body_fp=0fc71d235c56e39d3dcfe0727d72d1730beb7500df88b77e948428b42d0cc987 source_ref=808f1bab7d3a9a1f792a2c387a66fa8309013b1e role=test -->
Verifies that TriefactFile omits role metadata from rendered output when no role is set and parses back as empty string.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_roles:test_set_section_role_only_changes_the_role fingerprint=695d4eb7feb4ada7014601a918a20009402386984d39fa69bf41e558b9e49239 body_fp=8413f5e0b6d1c5f74955348a5986bda86819f7c777431404b65c0cd38dd23efe source_ref=808f1bab7d3a9a1f792a2c387a66fa8309013b1e role=test -->
## `test_set_section_role_only_changes_the_role`

Verifies TriefactFile.set_section_role updates only the role field, preserving body and fingerprints.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_roles:test_set_section_role_missing_symbol_returns_false fingerprint=5954fed5b1d3178d3b8decad6533114ec9835ba5959acbba5cbeb02a5581f79e body_fp=9bc37ef158e4cb2779c26920a0c234efa98111be9b313d2eb98777a30571710f source_ref=808f1bab7d3a9a1f792a2c387a66fa8309013b1e role=test -->
Verifies that TriefactFile.set_section_role returns False when attempting to set a role on a non-existent section.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_roles:test_taxonomy_save_load_round_trip fingerprint=e326869a73af6f3806785732f2aa3417a941f800f27f71c22f3f0d2c5d7d39a3 body_fp=763a4834d6c2599eabbeef71d29c2dfa8bb6610af61969f82d14bda748e8004a source_ref=808f1bab7d3a9a1f792a2c387a66fa8309013b1e role=test -->
## `test_taxonomy_save_load_round_trip`

Tests that a Taxonomy saves to disk and loads back with identical role names.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_roles:test_load_taxonomy_absent_returns_none fingerprint=53ad84b65203c12c0127ce98120b967a278be874476001a593a0df7cf1d82232 body_fp=f09940d601f535b9b8756206b7e7dd21ad213282768db4df5fdfe15749accc51 source_ref=808f1bab7d3a9a1f792a2c387a66fa8309013b1e role=test -->
Verifies that load_taxonomy returns None when no taxonomy file exists at the expected path.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_roles:test_load_taxonomy_malformed_returns_none fingerprint=9c8e0a8188bb02c61146aa686cc24e7e89b30939a2ce58461eb392c3c72c0647 body_fp=47735af36db634a3f3fdf0cca0d8034928fe5f9ec557469570cba8194c32a733 source_ref=808f1bab7d3a9a1f792a2c387a66fa8309013b1e role=test -->
## `test_load_taxonomy_malformed_returns_none`

Verifies that `load_taxonomy` returns `None` when the taxonomy file contains invalid JSON.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_roles:test_derive_taxonomy_returns_proposed_roles fingerprint=73b5356359967a3fc25d18dbc4652d2437d7be9947105467be6806301b55f91d body_fp=87d328a6797418eb94fd80794f755f7b8a58edaaa032debe01c5b48eee3da9aa source_ref=808f1bab7d3a9a1f792a2c387a66fa8309013b1e role=test -->
## `test_derive_taxonomy_returns_proposed_roles`

Tests that derive_taxonomy surveys the store and returns the client's proposed role vocabulary.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_roles:test_run_roles_only_persists_to_disk_and_db fingerprint=de59c5280b7c3ec6700517481508885f7385b34ab90122dcb6e2a1ff31184ec9 body_fp=b9de1b42449bb78f718a281dd8e58be7fb1e80a45b05243d622a03a8f978b68d source_ref=808f1bab7d3a9a1f792a2c387a66fa8309013b1e role=test -->
## `test_run_roles_only_persists_to_disk_and_db`

Tests that role classification persists taxonomy to disk and stores symbol roles in database.

- Sets up project with fake client outputting "domain" role and taxonomy
- Verifies roles are written to triefact files and database after classification
- Confirms taxonomy file is saved to disk alongside symbol roles
<!-- trie:end -->
<!-- trie:section symbol=tests/test_roles:test_roles_survive_db_wipe_via_disk_restore fingerprint=5aeef42df47e4661a39cfd1457d3581989cce06c4e3438f817d5ccd080b1de98 body_fp=31565456b241c483dea8517cda7ba96de129a7e6cbdaa54c5a45c64b8a666d50 source_ref=808f1bab7d3a9a1f792a2c387a66fa8309013b1e role=test -->
## `test_roles_survive_db_wipe_via_disk_restore`

Tests that role assignments persisted on disk are automatically restored when rebuilding the graph database without requiring LLM calls.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_roles:test_run_roles_only_only_missing_short_circuits fingerprint=0614853f9bf2e377ad550599a06ee99980281265f62f1f6bc5ad25cfbcbd48da body_fp=4017962491db7e886c57e5090d97c0d3e0dd551ea409470ef2c932a67ac99ad6 source_ref=808f1bab7d3a9a1f792a2c387a66fa8309013b1e role=test -->
## `test_run_roles_only_only_missing_short_circuits`

Verifies that `run_roles_only` with `only_missing=True` makes no LLM calls when all symbols already have roles.

- Sets up a project with pre-tagged symbols, then runs roles-only classification
- Confirms zero client calls and no taxonomy derivation when nothing is missing
<!-- trie:end -->
<!-- trie:section symbol=tests/test_roles:test_infer_role_clamps_to_vocabulary fingerprint=894f6bc97bf81e9933b280b701634b7e494a3ce997b868d37c4c92756f48a611 body_fp=aabda6126925eb89b1820c90ceb8e3ecf53524b0e2c0f2e792fadd74045248f3 source_ref=808f1bab7d3a9a1f792a2c387a66fa8309013b1e role=test -->
## `test_infer_role_clamps_to_vocabulary`

Tests that roles outside the defined taxonomy are dropped to empty string rather than polluting the classification axis.

- Sets up a client that returns 'made-up-role' which isn't in the taxonomy
- Verifies that no roles are actually assigned when they fall outside the vocabulary
<!-- trie:end -->
<!-- trie:section symbol=tests/test_roles:_write_config fingerprint=255ae7d120dcf071267a6418ca10d6688ce5337c209e2eef36dd64aa5095d69c body_fp=f60bde9870368e2502f8be2d98cbd4554983e041272beee2592da87c67f4c513 source_ref=808f1bab7d3a9a1f792a2c387a66fa8309013b1e role=test -->
## `_write_config`

Creates a test trie.toml configuration file in the given directory and returns the loaded Config object.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_roles:_git fingerprint=9efa6f55f9332a871587d0a9f0d4447d61f49c18b4d819e91e90494d14cf2f16 body_fp=8228cf941d7df4e86a6e99cb09c0b7e20c92d31d5fdecf7b1f594b9a2ece30b7 source_ref=808f1bab7d3a9a1f792a2c387a66fa8309013b1e role=util -->
Executes a Git command with the given arguments in the specified working directory.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_roles:project fingerprint=35466422e00a1531350313e4f99244de12dffe97e386b720956c9dfc028c497b body_fp=5fc31e307240b68e4dd26bf8ee3d08d880114a72f46f1dd84bc5b7548edbbbbd source_ref=808f1bab7d3a9a1f792a2c387a66fa8309013b1e role=test -->
## `project`

Creates a temporary test project with Python source files and Git history.

- Returns the project root path with configured trie.toml and sample Python modules
<!-- trie:end -->
<!-- trie:section symbol=tests/test_roles:_bootstrap fingerprint=52a4f760c0a7edd8194d4cc0cccdcb82ccb6ebdba6a92470e3d87ee63650688b body_fp=96bbd02cf1d65f78285a25fcc682a70a1f7fa5676bf1b3067b784a6b9d575555 source_ref=808f1bab7d3a9a1f792a2c387a66fa8309013b1e role=test -->
## `_bootstrap`

Generates triefacts for test fixtures with empty roles to simulate untagged trees needing role backfill.
<!-- trie:end -->