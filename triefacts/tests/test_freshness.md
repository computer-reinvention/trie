---
trie_version: 0.1.5
source: tests/test_freshness.py
file_fingerprint: c21306cc630617ff74b1c882b39215fb8d4332a944959c05fd891670ae6e8333
last_synced_at: '2026-05-28T15:04:26Z'
description: Tests for the turn-boundary freshness gate.
defines:
- kind: module
  qualified_name: tests/test_freshness:__module__
  lines: 1-388
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
  lines: 173-189
- kind: function
  qualified_name: tests/test_freshness:_run_after_turn
  lines: 192-202
- kind: function
  qualified_name: tests/test_freshness:test_no_stamp_triggers_scan_without_llm
  lines: 205-218
- kind: function
  qualified_name: tests/test_freshness:test_unchanged_state_is_a_noop
  lines: 221-227
- kind: function
  qualified_name: tests/test_freshness:test_head_moved_triggers_scan_without_llm
  lines: 230-249
- kind: function
  qualified_name: tests/test_freshness:test_mtimes_moved_triggers_sync_with_llm
  lines: 252-274
- kind: function
  qualified_name: tests/test_freshness:test_new_file_added_triggers_refresh
  lines: 277-286
- kind: function
  qualified_name: tests/test_freshness:test_removed_file_triggers_refresh
  lines: 289-296
- kind: function
  qualified_name: tests/test_freshness:test_after_turn_picks_up_just_made_edit
  lines: 304-315
- kind: function
  qualified_name: tests/test_freshness:test_after_turn_noop_when_nothing_changed
  lines: 318-324
- kind: function
  qualified_name: tests/test_freshness:test_cli_refresh_default_runs_after_turn
  lines: 332-349
- kind: function
  qualified_name: tests/test_freshness:test_cli_refresh_before_and_after_mutex
  lines: 352-361
- kind: function
  qualified_name: tests/test_freshness:test_cli_refresh_outside_git_fails
  lines: 364-387
incoming_refs: 0
outgoing_refs: 36
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
<!-- trie:section symbol=tests/test_freshness:test_ensure_fresh_raises_outside_git fingerprint=8367b6046047f80f7b6b3bb2170adbb3f445edbf63f301ce34d542c7e9a78532 body_fp=55aed1828a80a742800aceaa965c8baa25c31d5b6046cd193119981b3cb22dba source_ref=b9e672c5a19ee1a8556e80890f1c8f6b75c4ca0b -->
## `test_ensure_fresh_raises_outside_git(tmp_path: Path)`

Assert that `ensure_fresh_before_turn` raises `NotAGitRepoError` when called outside a git repository.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:_run_before_turn fingerprint=af1360c956ad404ceb854af6f7e6bdfff427769e8260556070de5da747ab5d3c body_fp=ba2af7f4ea27d4c41b4bfe4b1ca91ba0f7cf2e8206e90b2be4a3ad76755ce464 source_ref=b9e672c5a19ee1a8556e80890f1c8f6b75c4ca0b -->
## `_run_before_turn(project: Path, client: FakeClient | None = None)`

Invoke `ensure_fresh_before_turn` against a test project, returning its `FreshnessResult`.

- `client`: pass a `FakeClient` instance to inspect `.calls` after the run; defaults to a fresh `FakeClient`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:_run_after_turn fingerprint=a442953cd9d0a2624b0fd4681c83c3af537c79593588ab97a22c7bd1a304db1b body_fp=0a53911fbc99351a8bf52322c7afe3f129dfc33edafa4834578d4a6abeee6f3c source_ref=b9e672c5a19ee1a8556e80890f1c8f6b75c4ca0b -->
## `_run_after_turn(project: Path, client: FakeTrieClient | None = None)`

Invoke `ensure_fresh_after_turn` against a test project, returning the `FreshnessResult`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_no_stamp_triggers_scan_without_llm fingerprint=b53a0383509dd6c81eb6710ee57bdbdb51f7358a5fc29aa5946076b4ae82c369 body_fp=940a5ae9ee99000f665b45de7ad8bfb0ccc21ff28fabd7a44a4922f5138923b4 source_ref=b9e672c5a19ee1a8556e80890f1c8f6b75c4ca0b -->
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
<!-- trie:section symbol=tests/test_freshness:test_head_moved_triggers_scan_without_llm fingerprint=7c7b6e6971abb581360e4fcb858cf34d7d6f853887f5f33cc6bf13ce11cf2f1b body_fp=b59cb22e0584a19768a2fea79ceaa43a6990c98037d098111b51aac179b576eb source_ref=b9e672c5a19ee1a8556e80890f1c8f6b75c4ca0b -->
## `test_head_moved_triggers_scan_without_llm(project: Path)`

Assert that a new commit shifting HEAD triggers a graph rescan with `reason="head_moved"` but no LLM call and no incremental run.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_mtimes_moved_triggers_sync_with_llm fingerprint=b54352bc949a81fb06d57f78672a8214131cebf4b6604abd7fe5d999d8959db7 body_fp=c1e27972522e4ea3a8359130835e093442721ecd827bba9f92a7df8ba943a6f8 source_ref=b9e672c5a19ee1a8556e80890f1c8f6b75c4ca0b -->
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
<!-- trie:section symbol=tests/test_freshness:test_cli_refresh_default_runs_after_turn fingerprint=f22dd366b40ee69587e3e3da35085658d4520cad79261e3a630c6a948ee431b3 body_fp=151b06098bd94a9f8b51c917e1bc239fb4bdce71c4c7d0ec671b744fe62a086e source_ref=83ee0c7f20ba827538abaac9ac76f3991301821c -->
## `test_cli_refresh_default_runs_after_turn(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie refresh` with no flags exits 0, exercising the after-turn path.

- `monkeypatch`: stubs `trie.cli.make_client` to avoid requiring `ANTHROPIC_API_KEY`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_cli_refresh_before_and_after_mutex fingerprint=a656ec572aa7041e39940d696a533e02cb4eb833e3cc5e278199b18bccaadb99 body_fp=71547666d2a5e53b2a8340b175aff82c7ab76eba00abf1d1d5898247343f5378 source_ref=f28a6f590f3fa498c176b6f0b528e9f44fefd5ad -->
## `test_cli_refresh_before_and_after_mutex(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that passing both `--before-turn` and `--after-turn` to `trie refresh` exits with code 1 and reports mutual exclusivity.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_cli_refresh_outside_git_fails fingerprint=ae9d7e6fe8285a8be7c1bc4818e405388a351ffe08979820a130884f7b31210d body_fp=e1136d427d702ffe7f59318115bf94d990ca68dc84aec96fcd7eb005b0b71b7d source_ref=83ee0c7f20ba827538abaac9ac76f3991301821c -->
## `test_cli_refresh_outside_git_fails(tmp_path: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie refresh` exits with code 1 and prints "git repository" when invoked outside a git repo.
<!-- trie:end -->