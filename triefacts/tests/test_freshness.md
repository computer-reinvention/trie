---
trie_version: 0.1.5
source: tests/test_freshness.py
file_fingerprint: faa5046abb75e84c069ee5698da7624da737f20196239af4e9ab670125e196d3
last_synced_at: '2026-05-28T01:39:37Z'
description: Tests for the turn-boundary freshness gate.
defines:
- kind: module
  qualified_name: tests/test_freshness:__module__
  lines: 1-406
- kind: function
  qualified_name: tests/test_freshness:_git
  lines: 46-48
- kind: function
  qualified_name: tests/test_freshness:_init_repo
  lines: 51-54
- kind: class
  qualified_name: tests/test_freshness:FakeClient
  lines: 58-77
- kind: method
  qualified_name: tests/test_freshness:FakeClient.generate
  lines: 66-74
- kind: method
  qualified_name: tests/test_freshness:FakeClient.count_tokens
  lines: 76-77
- kind: function
  qualified_name: tests/test_freshness:project
  lines: 81-102
- kind: function
  qualified_name: tests/test_freshness:test_stamp_round_trip
  lines: 110-113
- kind: function
  qualified_name: tests/test_freshness:test_read_stamp_returns_none_when_missing
  lines: 116-117
- kind: function
  qualified_name: tests/test_freshness:test_read_stamp_returns_none_on_malformed_json
  lines: 120-123
- kind: function
  qualified_name: tests/test_freshness:test_read_stamp_returns_none_on_wrong_schema
  lines: 126-129
- kind: function
  qualified_name: tests/test_freshness:test_write_stamp_is_atomic_no_partial_files_left_behind
  lines: 132-137
- kind: function
  qualified_name: tests/test_freshness:test_scan_mtimes_returns_in_scope_files_only
  lines: 145-151
- kind: function
  qualified_name: tests/test_freshness:test_scan_mtimes_changes_after_file_edit
  lines: 154-162
- kind: function
  qualified_name: tests/test_freshness:test_ensure_fresh_raises_outside_git
  lines: 170-189
- kind: function
  qualified_name: tests/test_freshness:_run_before_turn
  lines: 197-213
- kind: function
  qualified_name: tests/test_freshness:_run_after_turn
  lines: 216-226
- kind: function
  qualified_name: tests/test_freshness:test_no_stamp_triggers_scan_without_llm
  lines: 229-242
- kind: function
  qualified_name: tests/test_freshness:test_unchanged_state_is_a_noop
  lines: 245-251
- kind: function
  qualified_name: tests/test_freshness:test_head_moved_triggers_scan_without_llm
  lines: 254-273
- kind: function
  qualified_name: tests/test_freshness:test_mtimes_moved_triggers_sync_with_llm
  lines: 276-298
- kind: function
  qualified_name: tests/test_freshness:test_new_file_added_triggers_refresh
  lines: 301-310
- kind: function
  qualified_name: tests/test_freshness:test_removed_file_triggers_refresh
  lines: 313-320
- kind: function
  qualified_name: tests/test_freshness:test_after_turn_picks_up_just_made_edit
  lines: 328-339
- kind: function
  qualified_name: tests/test_freshness:test_after_turn_noop_when_nothing_changed
  lines: 342-348
- kind: function
  qualified_name: tests/test_freshness:test_cli_refresh_default_runs_after_turn
  lines: 356-370
- kind: function
  qualified_name: tests/test_freshness:test_cli_refresh_before_and_after_mutex
  lines: 373-382
- kind: function
  qualified_name: tests/test_freshness:test_cli_refresh_outside_git_fails
  lines: 385-405
incoming_refs: 0
outgoing_refs: 31
---
<!-- trie:section symbol=tests/test_freshness:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=8ca7adf074d35afa6a41fbee0a37dd3aaef596de402632b07b851880ad5d754f source_ref=f28a6f590f3fa498c176b6f0b528e9f44fefd5ad -->
## `tests/test_freshness`

Test suite for the turn-boundary freshness gate covering all four states: `fresh`, `no_stamp`, `head_moved`, and `mtimes_moved`.

- `NotAGitRepoError` must be raised outside a git repo, never silently degraded.
- Uses a real git repo and real filesystem; no mocking of git or mtime logic.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:_git fingerprint=f1eab105158bdbbcda4afb86a01403dc9d52b7dc85a1e29e9e9ed20abfc133db body_fp=3417a2770c175eb404b8a50b82061520cda8bfe8547c5ec351b38c5aaf4d0645 source_ref=f28a6f590f3fa498c176b6f0b528e9f44fefd5ad -->
## `_git(args: list[str], cwd: Path) -> None`

Run a `git` subprocess in `cwd` with `check=True`, capturing output.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:_init_repo fingerprint=e6a8e59044cd4691a616ada677408e96c9c856caafae13744c548e08d2b462be body_fp=d6d3ec902e1b8d0bf9ec40f369b2be10bf38c68630a39d86dfa50baf2aaf04d2 source_ref=f28a6f590f3fa498c176b6f0b528e9f44fefd5ad -->
## `_init_repo(path: Path) -> None`

Initialise a git repo at `path` with a fixed test identity on branch `main`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:FakeClient fingerprint=72e1cfda4ef7f35341e25aa7cd44da1240024f4af92ce0191c7df39fdb8ea8e0 body_fp=e037dc09b0be25d465c938b812648ab48f4390ac9c9c6b954c5a7de12752e01f source_ref=f28a6f590f3fa498c176b6f0b528e9f44fefd5ad -->
## `FakeClient`

Deterministic LLM test double that counts `generate` calls and satisfies telemetry requirements.

- `calls`: incremented on each `generate` invocation; inspect after test runs.
- `count_tokens`: always returns 100.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:FakeClient.generate fingerprint=7328b86a4ba976097f1e8eec40c045a8090951dfeca29ef5debd39c4e6fc9a4b body_fp=b4d8f76a204a697a7f1541ef55d5c3c02d87dd2a3042b3456cc5ad13da7c67ed source_ref=f28a6f590f3fa498c176b6f0b528e9f44fefd5ad -->
## `FakeClient.generate(self, _req: GenerationRequest) -> GenerationResponse`

Increment `FakeClient.calls` and return a fixed `GenerationResponse` with deterministic token counts.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:FakeClient.count_tokens fingerprint=d2e54258807160cae2cd3e384f807ff7ab8c686f8c79830c0798dd9ba6b1e027 body_fp=d8d333632e478448f38bba2d838461dbe596c5410c31dd57bac064a4fb6776f7 source_ref=f28a6f590f3fa498c176b6f0b528e9f44fefd5ad -->
## `FakeClient.count_tokens(self, _req: GenerationRequest) -> int`

Always returns 100 for any `FakeClient` token-count request.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:project fingerprint=e01c8f727530a5c7c7c2f8e977e16ddd4243b91299298f93efeff46d49c525b1 body_fp=23b6562bcf1ae5cd48fedb589ebba91f83c6adae54b0c6aed94a2610e749069a source_ref=f28a6f590f3fa498c176b6f0b528e9f44fefd5ad -->
## `project(tmp_path: Path) -> Path`

Pytest fixture providing a real git repo with `trie.toml`, `src/alpha.py`, and `src/beta.py` under one initial commit.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_stamp_round_trip fingerprint=72338228aae6b7c3fdc3d86653fb22ccd8d2e9d0edaa7dbeef3aa073ef0033c2 body_fp=b08d3cedc61dd2575045f0e794fec25deed79fe9b2700bcb7b3e76a1334ab787 source_ref=f28a6f590f3fa498c176b6f0b528e9f44fefd5ad -->
## `test_stamp_round_trip(project: Path)`

Verify that `write_stamp` followed by `read_stamp` returns an identical `Stamp`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_read_stamp_returns_none_when_missing fingerprint=d1423324c130c11241ddaf7f21c5be495ca2ee4be0f4e16b370cba152baa9633 body_fp=574e8a285f40d005e377b423a33134a2b0574e86b542900573ef8d52cc1e2a98 source_ref=f28a6f590f3fa498c176b6f0b528e9f44fefd5ad -->
## `test_read_stamp_returns_none_when_missing(project: Path)`

Assert that `read_stamp` returns `None` when no stamp file exists.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_read_stamp_returns_none_on_malformed_json fingerprint=8794741dc828614cbf9d5e4293c991bf2ac68e37825cc9e9e666da058f8b36ee body_fp=cd80b7682982028a2754d80060f2f4576b054c225cf91f4ead9baeadee6a2694 source_ref=f28a6f590f3fa498c176b6f0b528e9f44fefd5ad -->
## `test_read_stamp_returns_none_on_malformed_json(project: Path)`

Assert that `read_stamp` returns `None` when the stamp file contains invalid JSON.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_read_stamp_returns_none_on_wrong_schema fingerprint=1fb296b592032801dedae599ca493d8e2c74ea94764676276317ff8f0c20edb5 body_fp=264c9d0445c9b8d7afc9be27e30783854a353faab99971991c75e3507b2cc561 source_ref=f28a6f590f3fa498c176b6f0b528e9f44fefd5ad -->
## `test_read_stamp_returns_none_on_wrong_schema(project: Path)`

Assert `read_stamp` returns `None` when the stamp file has a valid JSON but wrong field types.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_write_stamp_is_atomic_no_partial_files_left_behind fingerprint=c94b46ed64f02cf869ec7180ad85978df0d3147e948b402aa9937dcc93ee1df7 body_fp=0f9d0d6114d4d614dd83830131264a0a6b06f28eaffceedfd2fa583d4e43f1cd source_ref=f28a6f590f3fa498c176b6f0b528e9f44fefd5ad -->
## `test_write_stamp_is_atomic_no_partial_files_left_behind(project: Path)`

Assert that `write_stamp` leaves no `.tmp` files behind after its atomic rename.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_scan_mtimes_returns_in_scope_files_only fingerprint=760fbeb3332ac39d1c385d18b69323e6eebe70c51abb9d4fab2dc47ab28b6e1d body_fp=01a779ae512c03dd354714a3831b9aaeffb70883197e80f46a6e1aecc47efafe source_ref=f28a6f590f3fa498c176b6f0b528e9f44fefd5ad -->
## `test_scan_mtimes_returns_in_scope_files_only(project: Path)`

Assert that `scan_mtimes` returns only files matching the scope glob, excluding out-of-scope files like `trie.toml`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_scan_mtimes_changes_after_file_edit fingerprint=1b67abaef026c1ee9fb5fe6819e8e6f5e8c6d3d998b2dc360702895c4af0eda1 body_fp=eaeb734ecc68d5bf17d5750332a7f2945099d9ef86ab698a047c884504cb11c9 source_ref=f28a6f590f3fa498c176b6f0b528e9f44fefd5ad -->
## `test_scan_mtimes_changes_after_file_edit(project: Path)`

Verify that editing one file updates only its mtime entry, leaving unedited files unchanged.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_ensure_fresh_raises_outside_git fingerprint=89e3a8aaf80ce9d90638c4ddf7d07d34205a24f88d42f29522515c6ee04a3fb3 body_fp=55aed1828a80a742800aceaa965c8baa25c31d5b6046cd193119981b3cb22dba source_ref=f28a6f590f3fa498c176b6f0b528e9f44fefd5ad -->
## `test_ensure_fresh_raises_outside_git(tmp_path: Path)`

Assert that `ensure_fresh_before_turn` raises `NotAGitRepoError` when called outside a git repository.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:_run_before_turn fingerprint=71c2b56e4469ba0325dfa70ff210926de24f2af8597adf671bb8f90d1d26a325 body_fp=ba2af7f4ea27d4c41b4bfe4b1ca91ba0f7cf2e8206e90b2be4a3ad76755ce464 source_ref=f28a6f590f3fa498c176b6f0b528e9f44fefd5ad -->
## `_run_before_turn(project: Path, client: FakeClient | None = None)`

Invoke `ensure_fresh_before_turn` against a test project, returning its `FreshnessResult`.

- `client`: pass a `FakeClient` instance to inspect `.calls` after the run; defaults to a fresh `FakeClient`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:_run_after_turn fingerprint=6e5e97c6c2cb478ecb5ccd03719aa403e8e124f067af83c532639b8cce7b413f body_fp=c5ad441fa45d6ca9b5183108d5368f8ccd3a9454902b8947b7477c08ff9e3d64 source_ref=f28a6f590f3fa498c176b6f0b528e9f44fefd5ad -->
## `_run_after_turn(project: Path, client: FakeClient | None = None)`

Invoke `ensure_fresh_after_turn` against a test project, returning the `FreshnessResult`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_no_stamp_triggers_scan_without_llm fingerprint=376b562973de1b3f38953b030644c19a7115ae56d41dbf4795c146596f126188 body_fp=940a5ae9ee99000f665b45de7ad8bfb0ccc21ff28fabd7a44a4922f5138923b4 source_ref=f28a6f590f3fa498c176b6f0b528e9f44fefd5ad -->
## `test_no_stamp_triggers_scan_without_llm(project: Path)`

Assert that `ensure_fresh_before_turn` rescans the graph on first run without invoking the LLM.

- `result.incremental` must be `None`; `no_stamp` never calls `run_incremental`.
- LLM call count must remain zero; prose regen requires explicit `trie sync`.
- Written stamp's `head` must match `result.head`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_unchanged_state_is_a_noop fingerprint=8a432c89b41adb3a659c54709a1d0a2f7012900505ba89d3cd2081611b3e0569 body_fp=c8578e0ff11b2199c53de7404ea28933ef3a58f063b2b255e08c460bba214006 source_ref=f28a6f590f3fa498c176b6f0b528e9f44fefd5ad -->
## `test_unchanged_state_is_a_noop(project: Path)`

Assert that a second consecutive `ensure_fresh_before_turn` call returns `refreshed=False` with reason `"unchanged"`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_head_moved_triggers_scan_without_llm fingerprint=53fd9c5d55e1b6f4fb91c44726d9ef3c4c5f968426c32d0ce5af677173de93be body_fp=b59cb22e0584a19768a2fea79ceaa43a6990c98037d098111b51aac179b576eb source_ref=f28a6f590f3fa498c176b6f0b528e9f44fefd5ad -->
## `test_head_moved_triggers_scan_without_llm(project: Path)`

Assert that a new commit shifting HEAD triggers a graph rescan with `reason="head_moved"` but no LLM call and no incremental run.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_mtimes_moved_triggers_sync_with_llm fingerprint=60d1db01a580111a416263a2b7fb64da88ef5046f754beecf3c5b81fe7f38941 body_fp=c1e27972522e4ea3a8359130835e093442721ecd827bba9f92a7df8ba943a6f8 source_ref=f28a6f590f3fa498c176b6f0b528e9f44fefd5ad -->
## `test_mtimes_moved_triggers_sync_with_llm(project: Path)`

Assert that editing a file without committing triggers `run_incremental` (LLM path) with reason `"mtimes_moved"` while HEAD stays unchanged.

- `result.incremental` must be non-`None`; its presence confirms `run_incremental` ran rather than scan-only.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_new_file_added_triggers_refresh fingerprint=72a4d16126c9c220e45e18f140acba2cf99435c57bad3b59f76c56bdbc95df22 body_fp=d6b7679a697af4510013e15c20a3905b752de1bc582e3677ff2b7e7711fea8ac source_ref=f28a6f590f3fa498c176b6f0b528e9f44fefd5ad -->
## `test_new_file_added_triggers_refresh(project: Path)`

Assert that adding a new in-scope file with no prior stamp entry triggers an `mtimes_moved` refresh.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_removed_file_triggers_refresh fingerprint=7a26a5e8a1330925f3391f5e47a09737745daef82abc9939ca1aedf5e82c41e1 body_fp=3eacd6ef73c7c8193d26422f8d9f3421843e79e4f10c6ecc84290f4b9eb7447d source_ref=f28a6f590f3fa498c176b6f0b528e9f44fefd5ad -->
## `test_removed_file_triggers_refresh(project: Path)`

Assert that deleting an in-scope file causes the freshness gate to report `mtimes_moved` and trigger a refresh.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_after_turn_picks_up_just_made_edit fingerprint=f419a9fd19a9246b59a331ceb9c9351902e6dbad879171d26f57c9fb510e145d body_fp=e536c174efc0ad20bddfe406c2400716d97dd61836fb05dfcf53f789138b540a source_ref=f28a6f590f3fa498c176b6f0b528e9f44fefd5ad -->
## `test_after_turn_picks_up_just_made_edit(project: Path)`

Assert that `ensure_fresh_after_turn` detects a modified source file and returns `reason == "mtimes_moved"`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_after_turn_noop_when_nothing_changed fingerprint=9cfb3d3d7aec1e2b94374c89931394b3ad21096fa27413ad4e83b7f74ea4b5ca body_fp=f945350e80f307cf28de29b8ffbde51c3cd95488ec3c4fed2752627b492ea882 source_ref=f28a6f590f3fa498c176b6f0b528e9f44fefd5ad -->
## `test_after_turn_noop_when_nothing_changed(project: Path)`

Assert that `ensure_fresh_after_turn` returns `refreshed=False` with reason `"unchanged"` when no source files changed during the turn.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_cli_refresh_default_runs_after_turn fingerprint=dbcf0791a3b289b7c2f6d86d2eb2af4c4414a468cce91a2b2135c88d47d65e63 body_fp=fcb3f386bd2643de805c99019fe5ef386b0a1e6de1939c8d3f3f9de3056746cf source_ref=f28a6f590f3fa498c176b6f0b528e9f44fefd5ad -->
## `test_cli_refresh_default_runs_after_turn(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie refresh` with no flags exits 0 and runs the after-turn path.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_cli_refresh_before_and_after_mutex fingerprint=a656ec572aa7041e39940d696a533e02cb4eb833e3cc5e278199b18bccaadb99 body_fp=71547666d2a5e53b2a8340b175aff82c7ab76eba00abf1d1d5898247343f5378 source_ref=f28a6f590f3fa498c176b6f0b528e9f44fefd5ad -->
## `test_cli_refresh_before_and_after_mutex(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that passing both `--before-turn` and `--after-turn` to `trie refresh` exits with code 1 and reports mutual exclusivity.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_cli_refresh_outside_git_fails fingerprint=385e9125a386640f49e3e7864373a927f1f099cada6fdb1679eb7ec6337f7218 body_fp=a05a9c13d1012c7b75b2c1c865c5f429d781a86a1fdb6dbc67abb561e45e8be2 source_ref=f28a6f590f3fa498c176b6f0b528e9f44fefd5ad -->
## `test_cli_refresh_outside_git_fails(tmp_path: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie refresh` exits with code 1 and mentions "git repository" when run outside a git repo.
<!-- trie:end -->