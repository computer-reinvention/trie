---
trie_version: 0.3.0
source: tests/test_roles.py
file_fingerprint: c13afcad24aa5f9f02760d3dcca28af8fc50d8285726b5e40e068f030c8a1a7b
last_synced_at: '2026-08-02T21:19:29Z'
description: 'Tests for role tagging: durable persistence, derived taxonomy, and the'
defines:
- kind: module
  qualified_name: tests/test_roles:__module__
  lines: 1-352
- kind: function
  qualified_name: tests/test_roles:test_section_role_round_trips_through_render_and_parse
  lines: 32-46
  signature: def test_section_role_round_trips_through_render_and_parse()
- kind: function
  qualified_name: tests/test_roles:test_section_without_role_omits_the_field
  lines: 49-54
  signature: def test_section_without_role_omits_the_field()
- kind: function
  qualified_name: tests/test_roles:test_set_section_role_only_changes_the_role
  lines: 57-69
  signature: def test_set_section_role_only_changes_the_role()
- kind: function
  qualified_name: tests/test_roles:test_set_section_role_missing_symbol_returns_false
  lines: 72-74
  signature: def test_set_section_role_missing_symbol_returns_false()
- kind: function
  qualified_name: tests/test_roles:_roles_project
  lines: 85-93
  signature: 'def _roles_project(tmp_path: Path) -> tuple[Path, Config]'
- kind: function
  qualified_name: tests/test_roles:test_role_carried_forward_when_body_unchanged
  lines: 96-123
  signature: 'def test_role_carried_forward_when_body_unchanged(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_roles:test_role_updates_when_body_changes
  lines: 126-147
  signature: 'def test_role_updates_when_body_changes(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_roles:test_taxonomy_save_load_round_trip
  lines: 155-165
  signature: 'def test_taxonomy_save_load_round_trip(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_roles:test_load_taxonomy_absent_returns_none
  lines: 168-170
  signature: 'def test_load_taxonomy_absent_returns_none(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_roles:test_load_taxonomy_malformed_returns_none
  lines: 173-178
  signature: 'def test_load_taxonomy_malformed_returns_none(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_roles:test_derive_taxonomy_returns_proposed_roles
  lines: 186-195
  signature: 'def test_derive_taxonomy_returns_proposed_roles(project: Path)'
- kind: function
  qualified_name: tests/test_roles:test_run_roles_only_persists_to_disk_and_db
  lines: 204-224
  signature: 'def test_run_roles_only_persists_to_disk_and_db(project: Path)'
- kind: function
  qualified_name: tests/test_roles:test_roles_survive_db_wipe_via_disk_restore
  lines: 227-247
  signature: 'def test_roles_survive_db_wipe_via_disk_restore(project: Path)'
- kind: function
  qualified_name: tests/test_roles:test_run_roles_only_only_missing_short_circuits
  lines: 250-274
  signature: 'def test_run_roles_only_only_missing_short_circuits(project: Path)'
- kind: function
  qualified_name: tests/test_roles:test_infer_role_clamps_to_vocabulary
  lines: 277-289
  signature: 'def test_infer_role_clamps_to_vocabulary(project: Path)'
- kind: function
  qualified_name: tests/test_roles:_write_config
  lines: 297-307
  signature: 'def _write_config(root: Path) -> Config'
- kind: function
  qualified_name: tests/test_roles:_git
  lines: 310-311
  signature: 'def _git(args: list[str], cwd: Path) -> None'
- kind: function
  qualified_name: tests/test_roles:project
  lines: 315-329
  signature: 'def project(tmp_path: Path) -> Path'
- kind: function
  qualified_name: tests/test_roles:_bootstrap
  lines: 332-351
  signature: 'def _bootstrap(project: Path, config: Config) -> None'
incoming_refs: 0
outgoing_refs: 72
---
<!-- trie:section symbol=tests/test_roles:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=efc37c446790b90fb19c706b6873892ebfec635682dd8fe6bdbe931e995f2a52 source_ref=808f1bab7d3a9a1f792a2c387a66fa8309013b1e role=test -->
Tests for role tagging system including persistence, taxonomy derivation, and two-pass classification workflow.

- Verifies roles survive parse-render round-trips in triefact files
- Tests taxonomy persistence and loading from disk
- Validates end-to-end role classification with LLM client integration
- Ensures roles persist through database wipes via disk restoration
<!-- trie:end -->
<!-- trie:section symbol=tests/test_roles:test_section_role_round_trips_through_render_and_parse fingerprint=745d9e4fa90fe1287f73b09cd9ffd50d9bedc247eb33eb98d87e7d6f9e4bc4af body_fp=adf132f307c930167222619e1c36d2ace80ab13c0db671b80b96891d8acf344b source_ref=5576e0e44de525aa292d4a453d27732cda9bb473 role=test -->
## `def test_section_role_round_trips_through_render_and_parse()`

Verifies that role metadata survives the TriefactFile render-and-parse cycle.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_roles:test_section_without_role_omits_the_field fingerprint=7c8d288d622ffd0a9bad3cd36efafb0788a40e5449640e3122fd188fde1adde9 body_fp=fe786b1e25b2a98e8077933ab7b2d3117cfa54e98d0634fb6e6ccb96083a0193 source_ref=5576e0e44de525aa292d4a453d27732cda9bb473 role=test -->
## `def test_section_without_role_omits_the_field()`

Verifies that TriefactFile omits role metadata from rendered output when no role is set and parses back as empty string.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_roles:test_set_section_role_only_changes_the_role fingerprint=695d4eb7feb4ada7014601a918a20009402386984d39fa69bf41e558b9e49239 body_fp=ddc0d8138fb2fc0154b3e5aa16f20e1a5a621dc21a4b910dc3f703316e785e1c source_ref=5576e0e44de525aa292d4a453d27732cda9bb473 role=test -->
## `def test_set_section_role_only_changes_the_role()`

Verifies TriefactFile.set_section_role updates only the role field, preserving body and fingerprints.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_roles:test_set_section_role_missing_symbol_returns_false fingerprint=5954fed5b1d3178d3b8decad6533114ec9835ba5959acbba5cbeb02a5581f79e body_fp=f4b346db77ce596b1ada1e0290b6ebc84185533f5749a6db578a384bb760bad5 source_ref=5576e0e44de525aa292d4a453d27732cda9bb473 role=test -->
## `def test_set_section_role_missing_symbol_returns_false()`

Verifies that TriefactFile.set_section_role returns False when attempting to set a role on a non-existent section.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_roles:_roles_project fingerprint=9e8f68c5ed4a302c61dbe8eaf51f954633190736866b87cd3e564745eb3eeaf7 body_fp=e1cb389b19902d598a2d1e928f405abd234cae14dfead9258ebb912e22b6bcd2 source_ref=5576e0e44de525aa292d4a453d27732cda9bb473 role=test -->
## `def _roles_project(tmp_path: Path) -> tuple[Path, Config]`

Create a minimal temporary project with a `trie.toml` config and a single `svc.py` source file, returning the project root and loaded `Config`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_roles:test_role_carried_forward_when_body_unchanged fingerprint=623e9ffba0ef3bb7ed651fab5127456e689388d4b4197941d8db01d14efefe0f body_fp=da930588ea89fe7562caeb39473bf8d0f8a66802d00a774f8261566ea0d8dc04 source_ref=5576e0e44de525aa292d4a453d27732cda9bb473 role=test -->
## `def test_role_carried_forward_when_body_unchanged(tmp_path: Path)`

Assert that `sync_single_file` preserves the existing role when a forced re-sync produces a byte-identical body.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_roles:test_role_updates_when_body_changes fingerprint=fda9fb3c412a76a4790f7face2bacfa1386f486c877a9de42b69474e1b0b092e body_fp=6d45365272da88298bc573202dcf9389f9df9eb69e607874777c72fe0f7fa9ee source_ref=5576e0e44de525aa292d4a453d27732cda9bb473 role=test -->
## `def test_role_updates_when_body_changes(tmp_path: Path)`

Assert that `sync_single_file` adopts the new role when the regenerated body differs from the previous version.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_roles:test_taxonomy_save_load_round_trip fingerprint=e326869a73af6f3806785732f2aa3417a941f800f27f71c22f3f0d2c5d7d39a3 body_fp=0f0deb664c8214149a3fccedfb665b556524d117810aa108dc191000f485b5b7 source_ref=808f1bab7d3a9a1f792a2c387a66fa8309013b1e role=test -->
## `def test_taxonomy_save_load_round_trip(tmp_path: Path)`

Tests that a Taxonomy saves to disk and loads back with identical role names.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_roles:test_load_taxonomy_absent_returns_none fingerprint=53ad84b65203c12c0127ce98120b967a278be874476001a593a0df7cf1d82232 body_fp=af6b883bba0ce55bf3350f03ce2a2e26e982ca05d584f3eb7c0859596cb66828 source_ref=808f1bab7d3a9a1f792a2c387a66fa8309013b1e role=test -->
## `def test_load_taxonomy_absent_returns_none(tmp_path: Path)`

Verifies that load_taxonomy returns None when no taxonomy file exists at the expected path.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_roles:test_load_taxonomy_malformed_returns_none fingerprint=9c8e0a8188bb02c61146aa686cc24e7e89b30939a2ce58461eb392c3c72c0647 body_fp=d9f1a87980b8792615a00556aeebe8892d81f2db2bc36ff0d58b63f8111e1a49 source_ref=808f1bab7d3a9a1f792a2c387a66fa8309013b1e role=test -->
## `def test_load_taxonomy_malformed_returns_none(tmp_path: Path)`

Verifies that `load_taxonomy` returns `None` when the taxonomy file contains invalid JSON.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_roles:test_derive_taxonomy_returns_proposed_roles fingerprint=73b5356359967a3fc25d18dbc4652d2437d7be9947105467be6806301b55f91d body_fp=cc157215c27e56e31504da14f8208dc2e0218eacc263e17b7e6a81453dc2c2a1 source_ref=808f1bab7d3a9a1f792a2c387a66fa8309013b1e role=test -->
## `def test_derive_taxonomy_returns_proposed_roles(project: Path)`

Tests that derive_taxonomy surveys the store and returns the client's proposed role vocabulary.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_roles:test_run_roles_only_persists_to_disk_and_db fingerprint=de59c5280b7c3ec6700517481508885f7385b34ab90122dcb6e2a1ff31184ec9 body_fp=fa8c3c253561987ef89e34844d0e028a3387d85f7311d45e802c477752ec6cfa source_ref=808f1bab7d3a9a1f792a2c387a66fa8309013b1e role=test -->
## `def test_run_roles_only_persists_to_disk_and_db(project: Path)`

Tests that role classification persists taxonomy to disk and stores symbol roles in database.

- Sets up project with fake client outputting "domain" role and taxonomy
- Verifies roles are written to triefact files and database after classification
- Confirms taxonomy file is saved to disk alongside symbol roles
<!-- trie:end -->
<!-- trie:section symbol=tests/test_roles:test_roles_survive_db_wipe_via_disk_restore fingerprint=5aeef42df47e4661a39cfd1457d3581989cce06c4e3438f817d5ccd080b1de98 body_fp=9f6b7829e741bca39fcb5e37d7a38da36a078520df34cc0ee3bc925b2b9a9780 source_ref=5576e0e44de525aa292d4a453d27732cda9bb473 role=test -->
## `def test_roles_survive_db_wipe_via_disk_restore(project: Path)`

Tests that role assignments persisted on disk are automatically restored when rebuilding the graph database without requiring LLM calls.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_roles:test_run_roles_only_only_missing_short_circuits fingerprint=0614853f9bf2e377ad550599a06ee99980281265f62f1f6bc5ad25cfbcbd48da body_fp=d0d438db7822274c4b555a6de26123065323174b59f8cee922d0c9e288e1bd78 source_ref=808f1bab7d3a9a1f792a2c387a66fa8309013b1e role=test -->
## `def test_run_roles_only_only_missing_short_circuits(project: Path)`

Verifies that `run_roles_only` with `only_missing=True` makes no LLM calls when all symbols already have roles.

- Sets up a project with pre-tagged symbols, then runs roles-only classification
- Confirms zero client calls and no taxonomy derivation when nothing is missing
<!-- trie:end -->
<!-- trie:section symbol=tests/test_roles:test_infer_role_clamps_to_vocabulary fingerprint=894f6bc97bf81e9933b280b701634b7e494a3ce997b868d37c4c92756f48a611 body_fp=8d7896aa5f52980c5bb0deef807b2ecd840d649d7838ed2bd3fd7d2187590abf source_ref=808f1bab7d3a9a1f792a2c387a66fa8309013b1e role=test -->
## `def test_infer_role_clamps_to_vocabulary(project: Path)`

Tests that roles outside the defined taxonomy are dropped to empty string rather than polluting the classification axis.

- Sets up a client that returns 'made-up-role' which isn't in the taxonomy
- Verifies that no roles are actually assigned when they fall outside the vocabulary
<!-- trie:end -->
<!-- trie:section symbol=tests/test_roles:_write_config fingerprint=255ae7d120dcf071267a6418ca10d6688ce5337c209e2eef36dd64aa5095d69c body_fp=c51de530340fdc5348ebf83af10f101b8e2ef96b90e992b11fd73e90cb601860 source_ref=808f1bab7d3a9a1f792a2c387a66fa8309013b1e role=test -->
## `def _write_config(root: Path) -> Config`

Creates a test trie.toml configuration file in the given directory and returns the loaded Config object.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_roles:_git fingerprint=9efa6f55f9332a871587d0a9f0d4447d61f49c18b4d819e91e90494d14cf2f16 body_fp=2807fb37392f13f8cb93ea8ea050c01e827618586a6764d84042729f3df2e52f source_ref=808f1bab7d3a9a1f792a2c387a66fa8309013b1e role=util -->
## `def _git(args: list[str], cwd: Path) -> None`

Executes a Git command with the given arguments in the specified working directory.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_roles:project fingerprint=35466422e00a1531350313e4f99244de12dffe97e386b720956c9dfc028c497b body_fp=9f3f397139c6d9375f855fc769b3795dae9004b60d8cede42e81fda892c38064 source_ref=808f1bab7d3a9a1f792a2c387a66fa8309013b1e role=test -->
## `def project(tmp_path: Path) -> Path`

Creates a temporary test project with Python source files and Git history.

- Returns the project root path with configured trie.toml and sample Python modules
<!-- trie:end -->
<!-- trie:section symbol=tests/test_roles:_bootstrap fingerprint=52a4f760c0a7edd8194d4cc0cccdcb82ccb6ebdba6a92470e3d87ee63650688b body_fp=7ee24bdf6583e8f31a67c23fa2169eabaec77c231e95f360961b99efc270e2b9 source_ref=808f1bab7d3a9a1f792a2c387a66fa8309013b1e role=test -->
## `def _bootstrap(project: Path, config: Config) -> None`

Generates triefacts for test fixtures with empty roles to simulate untagged trees needing role backfill.
<!-- trie:end -->