---
trie_version: 0.3.0
source: tests/test_freshness.py
file_fingerprint: 5b0972275361f2c0f66c578dbb20baa908ad6738ace930c79903fa1af26236d1
last_synced_at: '2026-08-30T17:21:36Z'
description: Tests for the turn-boundary freshness gate (`trie sync --graph-only`).
defines:
- kind: module
  qualified_name: tests/test_freshness:__module__
  lines: 1-671
- kind: function
  qualified_name: tests/test_freshness:_git
  lines: 46-48
  signature: 'def _git(args: list[str], cwd: Path) -> None'
- kind: function
  qualified_name: tests/test_freshness:_init_repo
  lines: 51-54
  signature: 'def _init_repo(path: Path) -> None'
- kind: function
  qualified_name: tests/test_freshness:project
  lines: 58-79
  signature: 'def project(tmp_path: Path) -> Path'
- kind: function
  qualified_name: tests/test_freshness:test_stamp_round_trip
  lines: 87-90
  signature: 'def test_stamp_round_trip(project: Path)'
- kind: function
  qualified_name: tests/test_freshness:test_read_stamp_returns_none_when_missing
  lines: 93-94
  signature: 'def test_read_stamp_returns_none_when_missing(project: Path)'
- kind: function
  qualified_name: tests/test_freshness:test_read_stamp_returns_none_on_malformed_json
  lines: 97-100
  signature: 'def test_read_stamp_returns_none_on_malformed_json(project: Path)'
- kind: function
  qualified_name: tests/test_freshness:test_read_stamp_returns_none_on_wrong_schema
  lines: 103-106
  signature: 'def test_read_stamp_returns_none_on_wrong_schema(project: Path)'
- kind: function
  qualified_name: tests/test_freshness:test_write_stamp_is_atomic_no_partial_files_left_behind
  lines: 109-114
  signature: 'def test_write_stamp_is_atomic_no_partial_files_left_behind(project: Path)'
- kind: function
  qualified_name: tests/test_freshness:test_scan_mtimes_returns_in_scope_files_only
  lines: 122-128
  signature: 'def test_scan_mtimes_returns_in_scope_files_only(project: Path)'
- kind: function
  qualified_name: tests/test_freshness:test_scan_mtimes_changes_after_file_edit
  lines: 131-139
  signature: 'def test_scan_mtimes_changes_after_file_edit(project: Path)'
- kind: function
  qualified_name: tests/test_freshness:test_ensure_fresh_raises_outside_git
  lines: 147-161
  signature: 'def test_ensure_fresh_raises_outside_git(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_freshness:_run_before_turn
  lines: 169-175
  signature: 'def _run_before_turn(project: Path)'
- kind: function
  qualified_name: tests/test_freshness:_run_after_turn
  lines: 178-183
  signature: 'def _run_after_turn(project: Path)'
- kind: function
  qualified_name: tests/test_freshness:test_no_stamp_triggers_scan_without_llm
  lines: 186-203
  signature: 'def test_no_stamp_triggers_scan_without_llm(project: Path)'
- kind: function
  qualified_name: tests/test_freshness:test_empty_store_with_valid_stamp_self_heals
  lines: 206-240
  signature: 'def test_empty_store_with_valid_stamp_self_heals(project: Path)'
- kind: function
  qualified_name: tests/test_freshness:test_unchanged_state_is_a_noop
  lines: 243-248
  signature: 'def test_unchanged_state_is_a_noop(project: Path)'
- kind: function
  qualified_name: tests/test_freshness:test_head_moved_triggers_scan_without_llm
  lines: 251-267
  signature: 'def test_head_moved_triggers_scan_without_llm(project: Path)'
- kind: function
  qualified_name: tests/test_freshness:test_mtimes_moved_is_graph_only_and_marks_stale
  lines: 270-291
  signature: 'def test_mtimes_moved_is_graph_only_and_marks_stale(project: Path)'
- kind: function
  qualified_name: tests/test_freshness:test_unchanged_still_reports_pending_prose_staleness
  lines: 294-314
  signature: 'def test_unchanged_still_reports_pending_prose_staleness(project: Path)'
- kind: function
  qualified_name: tests/test_freshness:test_new_file_added_triggers_refresh
  lines: 317-326
  signature: 'def test_new_file_added_triggers_refresh(project: Path)'
- kind: function
  qualified_name: tests/test_freshness:test_removed_file_triggers_refresh
  lines: 329-336
  signature: 'def test_removed_file_triggers_refresh(project: Path)'
- kind: function
  qualified_name: tests/test_freshness:test_after_turn_picks_up_just_made_edit
  lines: 344-355
  signature: 'def test_after_turn_picks_up_just_made_edit(project: Path)'
- kind: function
  qualified_name: tests/test_freshness:test_after_turn_noop_when_nothing_changed
  lines: 358-364
  signature: 'def test_after_turn_noop_when_nothing_changed(project: Path)'
- kind: function
  qualified_name: tests/test_freshness:test_cli_graph_only_defaults_to_after_turn
  lines: 372-384
  signature: 'def test_cli_graph_only_defaults_to_after_turn(project: Path, monkeypatch: pytest.MonkeyPatch)'
- kind: function
  qualified_name: tests/test_freshness:test_cli_turn_flags_imply_graph_only
  lines: 387-398
  signature: 'def test_cli_turn_flags_imply_graph_only(project: Path, monkeypatch: pytest.MonkeyPatch)'
- kind: function
  qualified_name: tests/test_freshness:test_cli_graph_only_before_and_after_mutex
  lines: 401-410
  signature: 'def test_cli_graph_only_before_and_after_mutex(project: Path, monkeypatch: pytest.MonkeyPatch)'
- kind: function
  qualified_name: tests/test_freshness:test_cli_graph_only_rejects_llm_flags
  lines: 413-429
  signature: 'def test_cli_graph_only_rejects_llm_flags(project: Path, monkeypatch: pytest.MonkeyPatch)'
- kind: function
  qualified_name: tests/test_freshness:test_cli_refresh_command_is_gone
  lines: 432-442
  signature: 'def test_cli_refresh_command_is_gone(project: Path, monkeypatch: pytest.MonkeyPatch)'
- kind: function
  qualified_name: tests/test_freshness:test_cli_graph_only_reports_stale_prose_every_run
  lines: 445-470
  signature: 'def test_cli_graph_only_reports_stale_prose_every_run( project: Path, monkeypatch: pytest.MonkeyPatch )'
- kind: function
  qualified_name: tests/test_freshness:test_cli_graph_only_outside_git_fails
  lines: 473-492
  signature: 'def test_cli_graph_only_outside_git_fails(tmp_path: Path, monkeypatch: pytest.MonkeyPatch)'
- kind: function
  qualified_name: tests/test_freshness:test_full_sync_stamps_graph_freshness
  lines: 495-530
  signature: 'def test_full_sync_stamps_graph_freshness(project: Path, monkeypatch: pytest.MonkeyPatch)'
- kind: function
  qualified_name: tests/test_freshness:test_empty_store_computes_pending
  lines: 539-564
  signature: 'def test_empty_store_computes_pending(project: Path)'
- kind: function
  qualified_name: tests/test_freshness:test_head_moved_recomputes_pending
  lines: 567-650
  signature: 'def test_head_moved_recomputes_pending(project: Path)'
- kind: function
  qualified_name: tests/test_freshness:test_no_stamp_surfaces_missing_triefacts
  lines: 653-670
  signature: 'def test_no_stamp_surfaces_missing_triefacts(project: Path)'
incoming_refs: 0
outgoing_refs: 41
---
<!-- trie:section symbol=tests/test_freshness:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=ab7aae61e5f60ed8e938017caba43f98f18fdecee1f09edc37363ae841e7dc8b source_ref=a3a134b57a603882c49ea5d69c36ac88832aa352 role=test-infrastructure -->
Tests for the turn-boundary freshness gate that prevents stale graph state across git operations and file modifications.

- Exercises four freshness states: fresh (no refresh), no_stamp (full refresh), head_moved (full refresh), mtimes_moved (incremental refresh with LLM)
- Validates hard error on non-git repositories rather than silent degradation
- Tests stamp file persistence, mtime scanning, and CLI surface integration
- Uses real git repo fixtures to test actual filesystem and git interactions
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:_git fingerprint=f1eab105158bdbbcda4afb86a01403dc9d52b7dc85a1e29e9e9ed20abfc133db body_fp=e665cbaaba7bd599e8937c46e8f8e6ae3b7cba74f34c6b95634e4e9642980eb1 source_ref=a3a134b57a603882c49ea5d69c36ac88832aa352 role=test-infrastructure -->
## `def _git(args: list[str], cwd: Path) -> None`

Runs git subprocess with given arguments and working directory, configured for CI environments.

- Sets deterministic git identity via helper `_init_repo` to ensure commits succeed in sandboxes
- Raises CalledProcessError on git command failure due to `check=True`
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:_init_repo fingerprint=e6a8e59044cd4691a616ada677408e96c9c856caafae13744c548e08d2b462be body_fp=e5a05e4c976dca84ec3b6675f3120f1f9a53f8d27804bae4a72576c5018e2cc0 source_ref=a3a134b57a603882c49ea5d69c36ac88832aa352 role=test-infrastructure -->
## `def _init_repo(path: Path) -> None`

Initializes a new git repository with test-specific user configuration to ensure commits succeed in CI environments.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:project fingerprint=e01c8f727530a5c7c7c2f8e977e16ddd4243b91299298f93efeff46d49c525b1 body_fp=73b1181650e01e3f86d21514af0664d3efdbd811cd095b9b536ccc45f40cc965 source_ref=a3a134b57a603882c49ea5d69c36ac88832aa352 role=test-infrastructure -->
## `def project(tmp_path: Path) -> Path`

Creates test fixture with two-module Python project in initialized git repository with initial commit.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_stamp_round_trip fingerprint=72338228aae6b7c3fdc3d86653fb22ccd8d2e9d0edaa7dbeef3aa073ef0033c2 body_fp=df6eac85357322ccbce3cfac2685b93366d7c9667e2c4704a1fa2142b104d435 source_ref=a3a134b57a603882c49ea5d69c36ac88832aa352 role=change-detection -->
## `def test_stamp_round_trip(project: Path)`

Tests that Stamp instances can be written to and read from disk without data corruption.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_read_stamp_returns_none_when_missing fingerprint=d1423324c130c11241ddaf7f21c5be495ca2ee4be0f4e16b370cba152baa9633 body_fp=74583a3af50b1bb7cf0480ca419ed2f888e1dc5018beef57be45cd5d4219ed21 source_ref=a3a134b57a603882c49ea5d69c36ac88832aa352 role=change-detection -->
## `def test_read_stamp_returns_none_when_missing(project: Path)`

Verifies `read_stamp` returns `None` when no stamp file exists in the project.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_read_stamp_returns_none_on_malformed_json fingerprint=8794741dc828614cbf9d5e4293c991bf2ac68e37825cc9e9e666da058f8b36ee body_fp=1b55268349d118516f77e7b9d4abc322d507943ef9476cd9e8ffc9d0fd571e61 source_ref=a3a134b57a603882c49ea5d69c36ac88832aa352 role=test-infrastructure -->
## `def test_read_stamp_returns_none_on_malformed_json(project: Path)`

Tests that read_stamp returns None when the stamp file contains malformed JSON.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_read_stamp_returns_none_on_wrong_schema fingerprint=1fb296b592032801dedae599ca493d8e2c74ea94764676276317ff8f0c20edb5 body_fp=0b5e29a4d5576fd13075dd0380d1c55be599b6c8eb4f8b294eaffb5143ec63f5 source_ref=a3a134b57a603882c49ea5d69c36ac88832aa352 role=change-detection -->
## `def test_read_stamp_returns_none_on_wrong_schema(project: Path)`

Tests that `read_stamp` returns None when the stamp file contains JSON with incorrect field types.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_write_stamp_is_atomic_no_partial_files_left_behind fingerprint=c94b46ed64f02cf869ec7180ad85978df0d3147e948b402aa9937dcc93ee1df7 body_fp=541b710b35ceb2c1ee3a4ad634d4e90add504e55481dfb58eb83a27eabbebf5c source_ref=a3a134b57a603882c49ea5d69c36ac88832aa352 role=test-infrastructure -->
## `def test_write_stamp_is_atomic_no_partial_files_left_behind(project: Path)`

Verifies write_stamp performs atomic file operations without leaving temporary files.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_scan_mtimes_returns_in_scope_files_only fingerprint=760fbeb3332ac39d1c385d18b69323e6eebe70c51abb9d4fab2dc47ab28b6e1d body_fp=6c152377ca2a55625784aa4bb9a0a56bcb0396412c041b16d5bb1a0c31f17699 source_ref=a3a134b57a603882c49ea5d69c36ac88832aa352 role=test-infrastructure -->
## `def test_scan_mtimes_returns_in_scope_files_only(project: Path)`

Verifies that `scan_mtimes` returns only files matching the configured scope patterns, excluding out-of-scope files like `trie.toml`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_scan_mtimes_changes_after_file_edit fingerprint=1b67abaef026c1ee9fb5fe6819e8e6f5e8c6d3d998b2dc360702895c4af0eda1 body_fp=448cebb5a0fee2f4f4a95416fab73db25060b8af562d3400cd53a101843c638c source_ref=a3a134b57a603882c49ea5d69c36ac88832aa352 role=change-detection -->
## `def test_scan_mtimes_changes_after_file_edit(project: Path)`

Verifies that `scan_mtimes` detects file modification times changing when source files are edited.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_ensure_fresh_raises_outside_git fingerprint=9db564e3aa2e8aff5564d55a4eda79cc1430e430cc0d0716aa4c0df666b27f0b body_fp=22920ff71e62b8c7bbb40fc71da8e9cb9ba50c32d38115505b34e823f25be167 source_ref=92ccf12cb1f9c8c71edc05273f7cd4ee33c44227 role=test -->
## `def test_ensure_fresh_raises_outside_git(tmp_path: Path)`

Assert that `ensure_fresh_before_turn` raises `NotAGitRepoError` when called outside a git repository.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:_run_before_turn fingerprint=ee2fc4c5f5e1104f0286c16c360f38e74d6edb4663c9f93e12dea3aba1a58638 body_fp=a52b8685441bb610460bc79492bf56fbedf0ff9e05366c28918b8b409a34cecb source_ref=92ccf12cb1f9c8c71edc05273f7cd4ee33c44227 role=test -->
## `def _run_before_turn(project: Path)`

Runs `ensure_fresh_before_turn` with project fixtures and returns the `FreshnessResult`; no LLM client or prose sync is accepted or performed.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:_run_after_turn fingerprint=00d6efaad0512bd1d2ade3eeba137d186bc14b59b317759ba9c6c87909e9a00b body_fp=8d96dad548a1df73e78a5752637d4266fee273d7dfdaf942e42baf6e99fb5cf7 source_ref=92ccf12cb1f9c8c71edc05273f7cd4ee33c44227 role=test -->
## `def _run_after_turn(project: Path)`

Invoke `ensure_fresh_after_turn` against a real project fixture and return the `FreshnessResult`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_no_stamp_triggers_scan_without_llm fingerprint=cb9cdf287f762c8f64736553121348f1981b658ed72b7edc91dd02fdc4c78712 body_fp=53496d101894c5bd9a082aaf3f5a7945611617cf1c556a69ca936667d053dc76 source_ref=92ccf12cb1f9c8c71edc05273f7cd4ee33c44227 role=test -->
## `def test_no_stamp_triggers_scan_without_llm(project: Path)`

Assert that the first run against an empty store triggers a graph scan without LLM calls and records reason `"empty_store"`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_empty_store_with_valid_stamp_self_heals fingerprint=94e549022a7a7d1f8c1686fa0664794fd16ad08b928d15c1d8f74b44874738e9 body_fp=e3322ebdb00009e6af41a0dcbf70d78f41679fd7a6b8ae9436d920d20a828613 source_ref=92ccf12cb1f9c8c71edc05273f7cd4ee33c44227 role=test -->
## `def test_empty_store_with_valid_stamp_self_heals(project: Path)`

Assert that deleting `graph.db` while a valid stamp remains forces an `empty_store` rebuild and repopulates the graph, not a no-op `unchanged` verdict.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_unchanged_state_is_a_noop fingerprint=1d99bfa3bd8e22ce36d38b1d3835eb5cd7f4a44fc7c60498470bc8a0cf40a2ad body_fp=49edfabf19fa46077145e1ca0b7f108c3c205125a8b279be1e954f83343e36d0 source_ref=92ccf12cb1f9c8c71edc05273f7cd4ee33c44227 role=test -->
## `def test_unchanged_state_is_a_noop(project: Path)`

Assert that a second consecutive `ensure_fresh_before_turn` call returns `refreshed=False` with reason `"unchanged"`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_head_moved_triggers_scan_without_llm fingerprint=e9bda31036e11b00a69788d44fbdd2a5721d1d7f2f3ac992e1a7f8a0ea7419d7 body_fp=6c698028f6ddee6e2bd88eb460be28a8a4e9b8c4241664ed94f21ce78623f546 source_ref=92ccf12cb1f9c8c71edc05273f7cd4ee33c44227 role=test -->
## `def test_head_moved_triggers_scan_without_llm(project: Path)`

Assert that a new git commit shifts HEAD and triggers a graph-only rescan without invoking the LLM.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_mtimes_moved_is_graph_only_and_marks_stale fingerprint=a1aa84fbb9ba8fef0220f8c4ec9970533d065a12e0bf49676828939cb6f506d1 body_fp=96f7dad68690d68de6874ee588cee9861aad13bbdad1e3d1bc1bad195bb4e930 source_ref=92ccf12cb1f9c8c71edc05273f7cd4ee33c44227 role=test -->
## `def test_mtimes_moved_is_graph_only_and_marks_stale(project: Path)`

Tests that file edits trigger fast refresh that rebuilds graph without LLM and marks changed files as stale.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_unchanged_still_reports_pending_prose_staleness fingerprint=44366573627147cf032593a3de969b8f7baa4e8599056921ab0bf5a6a51eabe9 body_fp=83dc36865db845cb372e23b0732d2467fbbdbafbb2d02ad5f1ca4a79501507be source_ref=92ccf12cb1f9c8c71edc05273f7cd4ee33c44227 role=test -->
## `def test_unchanged_still_reports_pending_prose_staleness(project: Path)`

Regression test: verifies that an `unchanged` freshness result still surfaces the recorded prose staleness from the pending set, not just runs where `mtimes_moved` was detected.

- Edits `src/alpha.py`, confirms `mtimes_moved` with `src/alpha.py` in `stale_files`, then asserts the immediately following `unchanged` run still reports `src/alpha.py` as stale.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_new_file_added_triggers_refresh fingerprint=72a4d16126c9c220e45e18f140acba2cf99435c57bad3b59f76c56bdbc95df22 body_fp=b7c84e4b113825920896c1d8e6460f078a7f6b0aa7ca1d8290444cb63fb8a691 source_ref=a3a134b57a603882c49ea5d69c36ac88832aa352 role=change-detection -->
## `def test_new_file_added_triggers_refresh(project: Path)`

Verifies that creating a new in-scope file triggers freshness refresh via mtime detection.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_removed_file_triggers_refresh fingerprint=7a26a5e8a1330925f3391f5e47a09737745daef82abc9939ca1aedf5e82c41e1 body_fp=78b0ea5e28bdc8399445ca99baeb07258578087fa62334a92d3a5c5f53e017dd source_ref=a3a134b57a603882c49ea5d69c36ac88832aa352 role=change-detection -->
## `def test_removed_file_triggers_refresh(project: Path)`

Verifies that deleting an in-scope file triggers freshness gate refresh due to changed mtime map.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_after_turn_picks_up_just_made_edit fingerprint=f419a9fd19a9246b59a331ceb9c9351902e6dbad879171d26f57c9fb510e145d body_fp=b238a7370ffc74ba98aa13664c15a840f8106d1c3bab93b3737c71aeeb3b0645 source_ref=a3a134b57a603882c49ea5d69c36ac88832aa352 role=change-detection -->
## `def test_after_turn_picks_up_just_made_edit(project: Path)`

Tests that the after-turn freshness gate detects file modifications and triggers a refresh with `mtimes_moved` reason.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_after_turn_noop_when_nothing_changed fingerprint=9cfb3d3d7aec1e2b94374c89931394b3ad21096fa27413ad4e83b7f74ea4b5ca body_fp=e2cf8d38fcc1e24507d661d44c4eac49ab35a7eced36bb0e1e75740ab77a4400 source_ref=a3a134b57a603882c49ea5d69c36ac88832aa352 role=change-detection -->
## `def test_after_turn_noop_when_nothing_changed(project: Path)`

Verifies that after-turn freshness check skips refresh when no source files changed since last refresh.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_cli_graph_only_defaults_to_after_turn fingerprint=00008cbdb9e0bb77b2d191c1b1a385df374c8e01552ebb3721074eb20037c28d body_fp=541ba382e469528a3f0d30479c30867200601b7f14ffdb0c10ec7588aa7311b3 source_ref=92ccf12cb1f9c8c71edc05273f7cd4ee33c44227 role=test -->
## `def test_cli_graph_only_defaults_to_after_turn(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie sync --graph-only` exits 0 and runs the after-turn sweep without requiring an API key.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_cli_turn_flags_imply_graph_only fingerprint=cf557c9b67a84d4a261846b0742e3048dd097bb369c7a8b7fb1ee74cc0a878a0 body_fp=37e3bb5baff57f97f127a8b193064c3555c4b7678e08e5916cb02628ca45e29f source_ref=92ccf12cb1f9c8c71edc05273f7cd4ee33c44227 role=test -->
## `def test_cli_turn_flags_imply_graph_only(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie sync --after-turn` implicitly applies `--graph-only`, never triggering LLM spend.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_cli_graph_only_before_and_after_mutex fingerprint=32e6a92f89245d99c7a7577ee57a5765b342d6778b58618966fdf7e79432b265 body_fp=974e9620fdc00868e5feaa87113ea672d884d7e2299745e42ff4c7e880e7114f source_ref=92ccf12cb1f9c8c71edc05273f7cd4ee33c44227 role=test -->
## `def test_cli_graph_only_before_and_after_mutex(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie sync --before-turn --after-turn` exits with code 1 and prints "mutually exclusive".
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_cli_graph_only_rejects_llm_flags fingerprint=78ed081a2816b4ef17172a16b34c6e227bba7b71cf60031a793dafc4ebcebc2f body_fp=3f01ac07d1b776b16df79640896ef310d6f2c9b4bb8e25968ae772b5b12e70f5 source_ref=92ccf12cb1f9c8c71edc05273f7cd4ee33c44227 role=test -->
## `def test_cli_graph_only_rejects_llm_flags(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie sync --graph-only` (and `--after-turn`) exits 1 with "cannot be combined" for each LLM-mode flag (`--file`, `--budget`, `--all`, `--model`).
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_cli_refresh_command_is_gone fingerprint=9919d4b6d3d5eb931629a4952354af9aa008462f2906d2bb268173251b166b87 body_fp=eb281177f7a4c188287ba8e7a9355e19c59836bcccea3c62e47837b49fb91982 source_ref=92ccf12cb1f9c8c71edc05273f7cd4ee33c44227 role=test -->
## `def test_cli_refresh_command_is_gone(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie refresh` is no longer a valid CLI command, expecting a non-zero exit and "No such command" in output.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_cli_graph_only_reports_stale_prose_every_run fingerprint=f546446c3b76bbfba46138f41b96801ed31b47e944a3603a3525f1aa8b1ad7fa body_fp=da567452044eec37e0889977cadba6ad0528ab2da818bbba05db452f31b59842 source_ref=92ccf12cb1f9c8c71edc05273f7cd4ee33c44227 role=test -->
## `def test_cli_graph_only_reports_stale_prose_every_run( project: Path, monkeypatch: pytest.MonkeyPatch )`

Assert that `trie sync --graph-only` reports "prose stale" on every subsequent run after a file edit, not only the run that detected the mtime change.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_cli_graph_only_outside_git_fails fingerprint=358bbb4202fd20c0676a2d1f47a855e5cbf28b638b41c18a805a1ebc65dbdf62 body_fp=b847165d4023a7387e63c519ad03d8e2b2f93f0f8656a22ab06a44b1a66962ab source_ref=92ccf12cb1f9c8c71edc05273f7cd4ee33c44227 role=test -->
## `def test_cli_graph_only_outside_git_fails(tmp_path: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie sync --graph-only` exits with code 1 and mentions "git repository" when run outside a git repo.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_full_sync_stamps_graph_freshness fingerprint=794f7cc3ae6532b91812d4c02ec28df35a697ff9559d787940553afacbe5e365 body_fp=56a8b427ff28f91a04ac54c0ff06eafc3ff69d885bd04e5f3362f43b9951ce14 source_ref=ced013c93ceed35f637b33681e5bbd760c5b4287 role=test -->
## `def test_full_sync_stamps_graph_freshness(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that both bootstrap and incremental `trie sync` write a graph freshness stamp, preventing the next turn hook from triggering a redundant rebuild.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_empty_store_computes_pending fingerprint=fa260324a168be9232636e130cb6b8540e081a0941bc99b8fb2291a4e879f742 body_fp=b70ddd5bf803e4a95dab43955807b043423fb8eac381359c9ec40c4ca78defdc source_ref=705c034fae94d8aad693f09cb57505fdd17f99e0 role=test -->
## `def test_empty_store_computes_pending(project: Path)`

Regression test: verifies that the `empty_store` rebuild path calls `check_project` + `write_pending`, so missing triefacts are recorded in the pending set and surfaced on the subsequent `unchanged` run.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_head_moved_recomputes_pending fingerprint=820e77545c9c2af8a8c944ac43efaf9831da8ad73955745e8ed679bd23ee6b0f body_fp=1e4a88cfebf645bdecbbda66069ef2e95f224e6010f740d50251b689ca47928c source_ref=705c034fae94d8aad693f09cb57505fdd17f99e0 role=test -->
## `def test_head_moved_recomputes_pending(project: Path)`

Regression test: verifies that the `head_moved` freshness path rewrites the pending set rather than preserving phantom-stale entries from a prior `mtimes_moved` event.

- Primes the graph, edits `alpha.py` to force `mtimes_moved` and populate the pending set.
- Synthesises valid triefacts for both `alpha.py` and `beta.py` (matching fingerprints and body hashes), writes them, and commits — so `check_project` now sees both files as clean.
- Asserts that the subsequent `head_moved` run clears `src/alpha.py` from `stale_files` and from the persisted pending set.
- Asserts that the following `unchanged` run does not resurrect the cleared entries.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_no_stamp_surfaces_missing_triefacts fingerprint=77d25d6becbdee2c824229a50699efd7eed436b2d031870649c761aa2c0db5a9 body_fp=1276096829bf025b0ec05fb62084a80c96bacf54e9365f968f4f0e26a6830fb1 source_ref=705c034fae94d8aad693f09cb57505fdd17f99e0 role=test -->
## `def test_no_stamp_surfaces_missing_triefacts(project: Path)`

Assert that `ensure_fresh_before_turn` reports in-scope source files as stale when no stamp exists and no triefacts have been written.
<!-- trie:end -->