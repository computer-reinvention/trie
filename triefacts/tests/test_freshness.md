---
trie_version: 0.2.0
source: tests/test_freshness.py
file_fingerprint: 8cb71cd6fd365057153d6d3bec2ab111f317036a443a17d7f8eb66b2f96f8c6f
last_synced_at: '2026-07-29T18:38:37Z'
description: Tests for the turn-boundary freshness gate (`trie sync --graph-only`).
defines:
- kind: module
  qualified_name: tests/test_freshness:__module__
  lines: 1-531
- kind: function
  qualified_name: tests/test_freshness:_git
  lines: 46-48
- kind: function
  qualified_name: tests/test_freshness:_init_repo
  lines: 51-54
- kind: function
  qualified_name: tests/test_freshness:project
  lines: 58-79
- kind: function
  qualified_name: tests/test_freshness:test_stamp_round_trip
  lines: 87-90
- kind: function
  qualified_name: tests/test_freshness:test_read_stamp_returns_none_when_missing
  lines: 93-94
- kind: function
  qualified_name: tests/test_freshness:test_read_stamp_returns_none_on_malformed_json
  lines: 97-100
- kind: function
  qualified_name: tests/test_freshness:test_read_stamp_returns_none_on_wrong_schema
  lines: 103-106
- kind: function
  qualified_name: tests/test_freshness:test_write_stamp_is_atomic_no_partial_files_left_behind
  lines: 109-114
- kind: function
  qualified_name: tests/test_freshness:test_scan_mtimes_returns_in_scope_files_only
  lines: 122-128
- kind: function
  qualified_name: tests/test_freshness:test_scan_mtimes_changes_after_file_edit
  lines: 131-139
- kind: function
  qualified_name: tests/test_freshness:test_ensure_fresh_raises_outside_git
  lines: 147-161
- kind: function
  qualified_name: tests/test_freshness:_run_before_turn
  lines: 169-175
- kind: function
  qualified_name: tests/test_freshness:_run_after_turn
  lines: 178-183
- kind: function
  qualified_name: tests/test_freshness:test_no_stamp_triggers_scan_without_llm
  lines: 186-203
- kind: function
  qualified_name: tests/test_freshness:test_empty_store_with_valid_stamp_self_heals
  lines: 206-240
- kind: function
  qualified_name: tests/test_freshness:test_unchanged_state_is_a_noop
  lines: 243-248
- kind: function
  qualified_name: tests/test_freshness:test_head_moved_triggers_scan_without_llm
  lines: 251-267
- kind: function
  qualified_name: tests/test_freshness:test_mtimes_moved_is_graph_only_and_marks_stale
  lines: 270-291
- kind: function
  qualified_name: tests/test_freshness:test_unchanged_still_reports_pending_prose_staleness
  lines: 294-314
- kind: function
  qualified_name: tests/test_freshness:test_new_file_added_triggers_refresh
  lines: 317-326
- kind: function
  qualified_name: tests/test_freshness:test_removed_file_triggers_refresh
  lines: 329-336
- kind: function
  qualified_name: tests/test_freshness:test_after_turn_picks_up_just_made_edit
  lines: 344-355
- kind: function
  qualified_name: tests/test_freshness:test_after_turn_noop_when_nothing_changed
  lines: 358-364
- kind: function
  qualified_name: tests/test_freshness:test_cli_graph_only_defaults_to_after_turn
  lines: 372-384
- kind: function
  qualified_name: tests/test_freshness:test_cli_turn_flags_imply_graph_only
  lines: 387-398
- kind: function
  qualified_name: tests/test_freshness:test_cli_graph_only_before_and_after_mutex
  lines: 401-410
- kind: function
  qualified_name: tests/test_freshness:test_cli_graph_only_rejects_llm_flags
  lines: 413-429
- kind: function
  qualified_name: tests/test_freshness:test_cli_refresh_command_is_gone
  lines: 432-442
- kind: function
  qualified_name: tests/test_freshness:test_cli_graph_only_reports_stale_prose_every_run
  lines: 445-470
- kind: function
  qualified_name: tests/test_freshness:test_cli_graph_only_outside_git_fails
  lines: 473-492
- kind: function
  qualified_name: tests/test_freshness:test_full_sync_stamps_graph_freshness
  lines: 495-530
incoming_refs: 0
outgoing_refs: 36
---
<!-- trie:section symbol=tests/test_freshness:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=ab7aae61e5f60ed8e938017caba43f98f18fdecee1f09edc37363ae841e7dc8b source_ref=a3a134b57a603882c49ea5d69c36ac88832aa352 role=test-infrastructure -->
Tests for the turn-boundary freshness gate that prevents stale graph state across git operations and file modifications.

- Exercises four freshness states: fresh (no refresh), no_stamp (full refresh), head_moved (full refresh), mtimes_moved (incremental refresh with LLM)
- Validates hard error on non-git repositories rather than silent degradation
- Tests stamp file persistence, mtime scanning, and CLI surface integration
- Uses real git repo fixtures to test actual filesystem and git interactions
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:_git fingerprint=f1eab105158bdbbcda4afb86a01403dc9d52b7dc85a1e29e9e9ed20abfc133db body_fp=b599c87c9cf9939b627cf09020370322f153deae52534d62f042da8b763d920a source_ref=a3a134b57a603882c49ea5d69c36ac88832aa352 role=test-infrastructure -->
Runs git subprocess with given arguments and working directory, configured for CI environments.

- Sets deterministic git identity via helper `_init_repo` to ensure commits succeed in sandboxes
- Raises CalledProcessError on git command failure due to `check=True`
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:_init_repo fingerprint=e6a8e59044cd4691a616ada677408e96c9c856caafae13744c548e08d2b462be body_fp=6e6ecceaeefc0552cfc094c102403c3364dd271f6ddadb98073b20a1b8d4c8e2 source_ref=a3a134b57a603882c49ea5d69c36ac88832aa352 role=test-infrastructure -->
Initializes a new git repository with test-specific user configuration to ensure commits succeed in CI environments.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:project fingerprint=e01c8f727530a5c7c7c2f8e977e16ddd4243b91299298f93efeff46d49c525b1 body_fp=2f90714cf65b6b1e5d4f9e62fe0f45d5ec74ad883b47a75c923204a8c397a07c source_ref=a3a134b57a603882c49ea5d69c36ac88832aa352 role=test-infrastructure -->
Creates test fixture with two-module Python project in initialized git repository with initial commit.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_stamp_round_trip fingerprint=72338228aae6b7c3fdc3d86653fb22ccd8d2e9d0edaa7dbeef3aa073ef0033c2 body_fp=a1011bf2ccc456fd50893d94db6bc3c4838ac8caa46dc43668b746c2fb18410f source_ref=a3a134b57a603882c49ea5d69c36ac88832aa352 role=change-detection -->
Tests that Stamp instances can be written to and read from disk without data corruption.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_read_stamp_returns_none_when_missing fingerprint=d1423324c130c11241ddaf7f21c5be495ca2ee4be0f4e16b370cba152baa9633 body_fp=0940eb17e9e3d6db39ac59ae6c26a7904e4bd129860bc5c35d7d7ad5ad7a4a85 source_ref=a3a134b57a603882c49ea5d69c36ac88832aa352 role=change-detection -->
Verifies `read_stamp` returns `None` when no stamp file exists in the project.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_read_stamp_returns_none_on_malformed_json fingerprint=8794741dc828614cbf9d5e4293c991bf2ac68e37825cc9e9e666da058f8b36ee body_fp=4737d5dcbb5eb8efcb0877b2b1ccb5a965d4e830b0105c6a8b856e03fcc3b55e source_ref=a3a134b57a603882c49ea5d69c36ac88832aa352 role=test-infrastructure -->
Tests that read_stamp returns None when the stamp file contains malformed JSON.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_read_stamp_returns_none_on_wrong_schema fingerprint=1fb296b592032801dedae599ca493d8e2c74ea94764676276317ff8f0c20edb5 body_fp=4e8ae1f26629364cae954bc1b65281cb91ab22daab3617077babe9125c43e768 source_ref=a3a134b57a603882c49ea5d69c36ac88832aa352 role=change-detection -->
Tests that `read_stamp` returns None when the stamp file contains JSON with incorrect field types.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_write_stamp_is_atomic_no_partial_files_left_behind fingerprint=c94b46ed64f02cf869ec7180ad85978df0d3147e948b402aa9937dcc93ee1df7 body_fp=270b5d6274d2b66fab6720da39bebe2129c92bb9eb118065ed1c9a44828c965d source_ref=a3a134b57a603882c49ea5d69c36ac88832aa352 role=test-infrastructure -->
Verifies write_stamp performs atomic file operations without leaving temporary files.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_scan_mtimes_returns_in_scope_files_only fingerprint=760fbeb3332ac39d1c385d18b69323e6eebe70c51abb9d4fab2dc47ab28b6e1d body_fp=9f7bb09846b8602725b5fe58ee080def038c84a1717d448b5dbe32018e90db0c source_ref=a3a134b57a603882c49ea5d69c36ac88832aa352 role=test-infrastructure -->
Verifies that `scan_mtimes` returns only files matching the configured scope patterns, excluding out-of-scope files like `trie.toml`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_scan_mtimes_changes_after_file_edit fingerprint=1b67abaef026c1ee9fb5fe6819e8e6f5e8c6d3d998b2dc360702895c4af0eda1 body_fp=e20cb2e13f6cf713bc6570001243a316a3e1dc35d42789d044aa7783af7f4ed4 source_ref=a3a134b57a603882c49ea5d69c36ac88832aa352 role=change-detection -->
Verifies that `scan_mtimes` detects file modification times changing when source files are edited.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_ensure_fresh_raises_outside_git fingerprint=9db564e3aa2e8aff5564d55a4eda79cc1430e430cc0d0716aa4c0df666b27f0b body_fp=794250b6ed1ee5a4cdf9e496913f69331b3535ef46de1f7a5abb85455dc7b45e source_ref=92ccf12cb1f9c8c71edc05273f7cd4ee33c44227 role=test -->
Assert that `ensure_fresh_before_turn` raises `NotAGitRepoError` when called outside a git repository.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:_run_before_turn fingerprint=ee2fc4c5f5e1104f0286c16c360f38e74d6edb4663c9f93e12dea3aba1a58638 body_fp=dbf2e3102acc7eeab0c6ac909760b0d5f56094852dd2872f3c18688df6e81322 source_ref=92ccf12cb1f9c8c71edc05273f7cd4ee33c44227 role=test -->
Runs `ensure_fresh_before_turn` with project fixtures and returns the `FreshnessResult`; no LLM client or prose sync is accepted or performed.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:_run_after_turn fingerprint=00d6efaad0512bd1d2ade3eeba137d186bc14b59b317759ba9c6c87909e9a00b body_fp=74cd531770172135f52e7613ad65558ba915c13dbdde469eccc2621bf0a42f97 source_ref=92ccf12cb1f9c8c71edc05273f7cd4ee33c44227 role=test -->
Invoke `ensure_fresh_after_turn` against a real project fixture and return the `FreshnessResult`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_no_stamp_triggers_scan_without_llm fingerprint=cb9cdf287f762c8f64736553121348f1981b658ed72b7edc91dd02fdc4c78712 body_fp=4084cba01a07be2e08adc84d62e95acc7d3b1c0f2e3a04a488a17c44bad551d2 source_ref=92ccf12cb1f9c8c71edc05273f7cd4ee33c44227 role=test -->
Assert that the first run against an empty store triggers a graph scan without LLM calls and records reason `"empty_store"`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_empty_store_with_valid_stamp_self_heals fingerprint=94e549022a7a7d1f8c1686fa0664794fd16ad08b928d15c1d8f74b44874738e9 body_fp=903ebb50d4d933f166448731c753788452e33ee6252e45d41c3856530d816c28 source_ref=92ccf12cb1f9c8c71edc05273f7cd4ee33c44227 role=test -->
Assert that deleting `graph.db` while a valid stamp remains forces an `empty_store` rebuild and repopulates the graph, not a no-op `unchanged` verdict.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_unchanged_state_is_a_noop fingerprint=1d99bfa3bd8e22ce36d38b1d3835eb5cd7f4a44fc7c60498470bc8a0cf40a2ad body_fp=250e1c7163eaac341181d43c908e16b4e0f7483365a8cff4639d3bac0bdf424c source_ref=92ccf12cb1f9c8c71edc05273f7cd4ee33c44227 role=test -->
Assert that a second consecutive `ensure_fresh_before_turn` call returns `refreshed=False` with reason `"unchanged"`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_head_moved_triggers_scan_without_llm fingerprint=e9bda31036e11b00a69788d44fbdd2a5721d1d7f2f3ac992e1a7f8a0ea7419d7 body_fp=3bba216892919314f4bf622c182c0dcbf3459653b5b78c8e55c88c2a18252ba3 source_ref=92ccf12cb1f9c8c71edc05273f7cd4ee33c44227 role=test -->
Assert that a new git commit shifts HEAD and triggers a graph-only rescan without invoking the LLM.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_mtimes_moved_is_graph_only_and_marks_stale fingerprint=a1aa84fbb9ba8fef0220f8c4ec9970533d065a12e0bf49676828939cb6f506d1 body_fp=e2e7a243017e5811293d97a26d9fb5ebd34d0372be94c55f3bbfb80fd4b9af09 source_ref=92ccf12cb1f9c8c71edc05273f7cd4ee33c44227 role=test -->
Tests that file edits trigger fast refresh that rebuilds graph without LLM and marks changed files as stale.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_unchanged_still_reports_pending_prose_staleness fingerprint=44366573627147cf032593a3de969b8f7baa4e8599056921ab0bf5a6a51eabe9 body_fp=623d7f6572b81144de59e49d2f30136a95604687fef9ac4c55f7818a218217c9 source_ref=92ccf12cb1f9c8c71edc05273f7cd4ee33c44227 role=test -->
Regression test: verifies that an `unchanged` freshness result still surfaces the recorded prose staleness from the pending set, not just runs where `mtimes_moved` was detected.

- Edits `src/alpha.py`, confirms `mtimes_moved` with `src/alpha.py` in `stale_files`, then asserts the immediately following `unchanged` run still reports `src/alpha.py` as stale.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_new_file_added_triggers_refresh fingerprint=72a4d16126c9c220e45e18f140acba2cf99435c57bad3b59f76c56bdbc95df22 body_fp=48075a2e3ec369fdbb3e2efbe21cd8c7468f55fe64365e81c1b07014244d9775 source_ref=a3a134b57a603882c49ea5d69c36ac88832aa352 role=change-detection -->
Verifies that creating a new in-scope file triggers freshness refresh via mtime detection.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_removed_file_triggers_refresh fingerprint=7a26a5e8a1330925f3391f5e47a09737745daef82abc9939ca1aedf5e82c41e1 body_fp=900041c8cd23d2bf73ded15685dced65f57c79d5b0db338c2ee11e5c3cf214c6 source_ref=a3a134b57a603882c49ea5d69c36ac88832aa352 role=change-detection -->
Verifies that deleting an in-scope file triggers freshness gate refresh due to changed mtime map.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_after_turn_picks_up_just_made_edit fingerprint=f419a9fd19a9246b59a331ceb9c9351902e6dbad879171d26f57c9fb510e145d body_fp=44d8b70a4bf2b83805694de8c55a04ba2205994042dcfdc39c17ef2f16ef4b77 source_ref=a3a134b57a603882c49ea5d69c36ac88832aa352 role=change-detection -->
Tests that the after-turn freshness gate detects file modifications and triggers a refresh with `mtimes_moved` reason.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_after_turn_noop_when_nothing_changed fingerprint=9cfb3d3d7aec1e2b94374c89931394b3ad21096fa27413ad4e83b7f74ea4b5ca body_fp=d57f912acced439c679d5fb8e310c40101a6543b779c104506dc05beaa8d244c source_ref=a3a134b57a603882c49ea5d69c36ac88832aa352 role=change-detection -->
Verifies that after-turn freshness check skips refresh when no source files changed since last refresh.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_cli_graph_only_defaults_to_after_turn fingerprint=00008cbdb9e0bb77b2d191c1b1a385df374c8e01552ebb3721074eb20037c28d body_fp=d64cadd350b488020b7523b410246c9506c0759fd163811b077bfff10c6cdc8a source_ref=92ccf12cb1f9c8c71edc05273f7cd4ee33c44227 role=test -->
Assert that `trie sync --graph-only` exits 0 and runs the after-turn sweep without requiring an API key.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_cli_turn_flags_imply_graph_only fingerprint=cf557c9b67a84d4a261846b0742e3048dd097bb369c7a8b7fb1ee74cc0a878a0 body_fp=56a1950dde86be4b178e180dc52aa0c785be9cc4f573ee8c2580f7b78c8d38bf source_ref=92ccf12cb1f9c8c71edc05273f7cd4ee33c44227 role=test -->
Assert that `trie sync --after-turn` implicitly applies `--graph-only`, never triggering LLM spend.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_cli_graph_only_before_and_after_mutex fingerprint=32e6a92f89245d99c7a7577ee57a5765b342d6778b58618966fdf7e79432b265 body_fp=f93344de5386031e1b8079c62384eb3ec9550b76bd06066c17d4ca32f9ae4d67 source_ref=92ccf12cb1f9c8c71edc05273f7cd4ee33c44227 role=test -->
Assert that `trie sync --before-turn --after-turn` exits with code 1 and prints "mutually exclusive".
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_cli_graph_only_rejects_llm_flags fingerprint=78ed081a2816b4ef17172a16b34c6e227bba7b71cf60031a793dafc4ebcebc2f body_fp=e3553501d7cfa1f3839af39ba25175716f5de8975fdaaac397b677bada3b5dd8 source_ref=92ccf12cb1f9c8c71edc05273f7cd4ee33c44227 role=test -->
Assert that `trie sync --graph-only` (and `--after-turn`) exits 1 with "cannot be combined" for each LLM-mode flag (`--file`, `--budget`, `--all`, `--model`).
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_cli_refresh_command_is_gone fingerprint=9919d4b6d3d5eb931629a4952354af9aa008462f2906d2bb268173251b166b87 body_fp=de99a2c45fe42e1565a7dc2a7241ee2a41bce754397c895f7a403361b67dd01e source_ref=92ccf12cb1f9c8c71edc05273f7cd4ee33c44227 role=test -->
Assert that `trie refresh` is no longer a valid CLI command, expecting a non-zero exit and "No such command" in output.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_cli_graph_only_reports_stale_prose_every_run fingerprint=f546446c3b76bbfba46138f41b96801ed31b47e944a3603a3525f1aa8b1ad7fa body_fp=5441f957ddb20e6a7b420a2e82e20886509771d1f5eea01667b8925fce7e5ed8 source_ref=92ccf12cb1f9c8c71edc05273f7cd4ee33c44227 role=test -->
Assert that `trie sync --graph-only` reports "prose stale" on every subsequent run after a file edit, not only the run that detected the mtime change.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_cli_graph_only_outside_git_fails fingerprint=358bbb4202fd20c0676a2d1f47a855e5cbf28b638b41c18a805a1ebc65dbdf62 body_fp=24fb4d4fd95c329e756c74e8405712e9255230b660ff54f2bd2d22d1e6916966 source_ref=92ccf12cb1f9c8c71edc05273f7cd4ee33c44227 role=test -->
Assert that `trie sync --graph-only` exits with code 1 and mentions "git repository" when run outside a git repo.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_full_sync_stamps_graph_freshness fingerprint=794f7cc3ae6532b91812d4c02ec28df35a697ff9559d787940553afacbe5e365 body_fp=26fd57522757d9133d640cefbe60770f29c0b8aad18a4389a470e04452294129 source_ref=ced013c93ceed35f637b33681e5bbd760c5b4287 role=test -->
Assert that both bootstrap and incremental `trie sync` write a graph freshness stamp, preventing the next turn hook from triggering a redundant rebuild.
<!-- trie:end -->