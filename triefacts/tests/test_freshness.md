---
trie_version: 0.1.5
source: tests/test_freshness.py
file_fingerprint: 95b985f174680363effb5aea5a603d54e50513bc5c3ed450e14474db3519a3f5
last_synced_at: '2026-06-06T14:18:52Z'
description: Tests for the turn-boundary freshness gate.
defines:
- kind: module
  qualified_name: tests/test_freshness:__module__
  lines: 1-461
- kind: function
  qualified_name: tests/test_freshness:_git
  lines: 45-47
- kind: function
  qualified_name: tests/test_freshness:_init_repo
  lines: 50-53
- kind: function
  qualified_name: tests/test_freshness:project
  lines: 57-78
- kind: function
  qualified_name: tests/test_freshness:test_stamp_round_trip
  lines: 86-89
- kind: function
  qualified_name: tests/test_freshness:test_read_stamp_returns_none_when_missing
  lines: 92-93
- kind: function
  qualified_name: tests/test_freshness:test_read_stamp_returns_none_on_malformed_json
  lines: 96-99
- kind: function
  qualified_name: tests/test_freshness:test_read_stamp_returns_none_on_wrong_schema
  lines: 102-105
- kind: function
  qualified_name: tests/test_freshness:test_write_stamp_is_atomic_no_partial_files_left_behind
  lines: 108-113
- kind: function
  qualified_name: tests/test_freshness:test_scan_mtimes_returns_in_scope_files_only
  lines: 121-127
- kind: function
  qualified_name: tests/test_freshness:test_scan_mtimes_changes_after_file_edit
  lines: 130-138
- kind: function
  qualified_name: tests/test_freshness:test_ensure_fresh_raises_outside_git
  lines: 146-165
- kind: function
  qualified_name: tests/test_freshness:_run_before_turn
  lines: 173-192
- kind: function
  qualified_name: tests/test_freshness:_run_after_turn
  lines: 195-205
- kind: function
  qualified_name: tests/test_freshness:test_no_stamp_triggers_scan_without_llm
  lines: 208-228
- kind: function
  qualified_name: tests/test_freshness:test_empty_store_with_valid_stamp_self_heals
  lines: 231-268
- kind: function
  qualified_name: tests/test_freshness:test_unchanged_state_is_a_noop
  lines: 271-277
- kind: function
  qualified_name: tests/test_freshness:test_head_moved_triggers_scan_without_llm
  lines: 280-299
- kind: function
  qualified_name: tests/test_freshness:test_mtimes_moved_is_graph_only_and_marks_stale
  lines: 302-326
- kind: function
  qualified_name: tests/test_freshness:test_mtimes_moved_with_sync_prose_runs_inline
  lines: 329-347
- kind: function
  qualified_name: tests/test_freshness:test_new_file_added_triggers_refresh
  lines: 350-359
- kind: function
  qualified_name: tests/test_freshness:test_removed_file_triggers_refresh
  lines: 362-369
- kind: function
  qualified_name: tests/test_freshness:test_after_turn_picks_up_just_made_edit
  lines: 377-388
- kind: function
  qualified_name: tests/test_freshness:test_after_turn_noop_when_nothing_changed
  lines: 391-397
- kind: function
  qualified_name: tests/test_freshness:test_cli_refresh_default_runs_after_turn
  lines: 405-422
- kind: function
  qualified_name: tests/test_freshness:test_cli_refresh_before_and_after_mutex
  lines: 425-434
- kind: function
  qualified_name: tests/test_freshness:test_cli_refresh_outside_git_fails
  lines: 437-460
incoming_refs: 0
outgoing_refs: 40
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
<!-- trie:section symbol=tests/test_freshness:test_ensure_fresh_raises_outside_git fingerprint=8367b6046047f80f7b6b3bb2170adbb3f445edbf63f301ce34d542c7e9a78532 body_fp=3597330e1a59a08972829bc29036ec2ce7f1d24d4183adefd8fbda3af9dc531d source_ref=a3a134b57a603882c49ea5d69c36ac88832aa352 role=test-infrastructure -->
Verifies that `ensure_fresh_before_turn` raises `NotAGitRepoError` when called outside a git repository.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:_run_before_turn fingerprint=ed973b4b217cdaa36e091d520f2727630e7c8a797fb974cc0450595c3a999e6e body_fp=d6bee366f8dbb22e63bdee996fa60ec42673ede3eb034eaffb07549d349ae496 source_ref=126b95462888a58eab7dda6efb246eabc3941e1b role=util -->
Runs ensure_fresh_before_turn with test fixtures, optionally accepting a client to inspect LLM call counts.

- `client`: if None, uses a default FakeTrieClient for deterministic testing
- `sync_prose`: passed through to enable inline prose regeneration
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:_run_after_turn fingerprint=a442953cd9d0a2624b0fd4681c83c3af537c79593588ab97a22c7bd1a304db1b body_fp=fe3a2355ed58cbeb0e6ae86d863862cfb62e013a25d3eebbcd104f1021d5aba7 source_ref=a3a134b57a603882c49ea5d69c36ac88832aa352 role=test-infrastructure -->
Test helper that runs the after-turn freshness gate with database and client setup.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_no_stamp_triggers_scan_without_llm fingerprint=c305a11f671c6277306c70f0a8453a98dc6a659feea4a77744f1e89b184c71b1 body_fp=e790c2c69d1122ec790acb2f481abefceab08863e0946e808a30aeb0fb6340c2 source_ref=a3a134b57a603882c49ea5d69c36ac88832aa352 role=change-detection -->
Verifies that first run in a fresh project triggers a graph scan without LLM calls.

- Confirms empty store guard reports "empty_store" reason instead of "no_stamp"
- Validates incremental refresh is skipped on first contact
- Ensures stamp is created and records current HEAD after refresh
- Confirms LLM client receives zero calls during scan-only rebuild
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_empty_store_with_valid_stamp_self_heals fingerprint=720d506359e244b71b9b081e43f0081ddfd35790e3fae72704e1826f293615ff body_fp=34cc7d7f54462e168ce301cc373d53079393cf80cf63cb589407b841ec15acb4 source_ref=a3a134b57a603882c49ea5d69c36ac88832aa352 role=change-detection -->
Verifies that empty-store guard overrides valid stamp to trigger scan-only rebuild when graph database is corrupted.

- Sets up valid stamp then simulates corrupted empty database
- Confirms rebuild triggers with `empty_store` reason despite matching stamp
- Validates no LLM calls during self-healing process
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_unchanged_state_is_a_noop fingerprint=8a432c89b41adb3a659c54709a1d0a2f7012900505ba89d3cd2081611b3e0569 body_fp=2bbc4e0845965beaedbc192c4f108422502d4383235035e1cefe361e85c137b5 source_ref=a3a134b57a603882c49ea5d69c36ac88832aa352 role=change-detection -->
Verifies that freshness gate returns unchanged status when no files or git state have changed since last refresh.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_head_moved_triggers_scan_without_llm fingerprint=7c7b6e6971abb581360e4fcb858cf34d7d6f853887f5f33cc6bf13ce11cf2f1b body_fp=e72a9475d1e5ddaea7daf9cf3a3877aa563da9bcdae6abd11f90cbc5a83b3689 source_ref=a3a134b57a603882c49ea5d69c36ac88832aa352 role=change-detection -->
Verifies that changing git HEAD without modifying tracked files triggers a graph rescan but skips LLM calls.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_mtimes_moved_is_graph_only_and_marks_stale fingerprint=25d6cf14f37b9181dd82b8d4af33e84a9b08791273ed2e4d65655e929fac92b6 body_fp=e2e7a243017e5811293d97a26d9fb5ebd34d0372be94c55f3bbfb80fd4b9af09 source_ref=126b95462888a58eab7dda6efb246eabc3941e1b role=test -->
Tests that file edits trigger fast refresh that rebuilds graph without LLM and marks changed files as stale.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_mtimes_moved_with_sync_prose_runs_inline fingerprint=31ad13b929a7c8fb2a78e7d8f8d70c5f09a5240e8a95dc17572ead3722a280c0 body_fp=e36e22b1d5f776ea92652c8d7ee8b990de496b24358fe63ed81254638305bb1c source_ref=126b95462888a58eab7dda6efb246eabc3941e1b role=test -->
Verifies that sync_prose=True triggers inline LLM regeneration and clears pending stale files after mtime changes.

- Modifies a file to trigger mtime_moved state
- Asserts result.incremental is not None when sync_prose=True 
- Confirms pending.stale is cleared after inline sync
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
<!-- trie:section symbol=tests/test_freshness:test_cli_refresh_default_runs_after_turn fingerprint=f22dd366b40ee69587e3e3da35085658d4520cad79261e3a630c6a948ee431b3 body_fp=e6020bd61792046e2c86b0b102dcb99d8ed0641ac19e0f9dd1030681c2f270f7 source_ref=a3a134b57a603882c49ea5d69c36ac88832aa352 role=test-infrastructure -->
Verifies that `trie refresh` CLI command without flags runs the after-turn freshness gate by default.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_cli_refresh_before_and_after_mutex fingerprint=a656ec572aa7041e39940d696a533e02cb4eb833e3cc5e278199b18bccaadb99 body_fp=ab57c10111ff30fa3bd61285f181dd1727eb5676ab27593ed5f9414ed1519afe source_ref=a3a134b57a603882c49ea5d69c36ac88832aa352 role=test-infrastructure -->
Verifies the CLI rejects both `--before-turn` and `--after-turn` flags simultaneously with exit code 1.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_cli_refresh_outside_git_fails fingerprint=ae9d7e6fe8285a8be7c1bc4818e405388a351ffe08979820a130884f7b31210d body_fp=1554a5c161ad99a6522986126777a2bcfdc93089d5d728fffea04ee5e2231a74 source_ref=a3a134b57a603882c49ea5d69c36ac88832aa352 role=change-detection -->
Verifies that `trie refresh` CLI command exits with code 1 when run outside git repository.

- Creates trie.toml config in non-git directory
- Mocks client creation to avoid API key requirements
- Asserts CLI returns exit code 1 and mentions "git repository"
<!-- trie:end -->