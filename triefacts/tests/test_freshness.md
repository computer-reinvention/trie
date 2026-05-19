---
trie_version: 0.1.1
source: tests/test_freshness.py
file_fingerprint: cad3bdaad74c6acc7a9774080260184b0f50138c37bb2d7fce5f3696d4db47b3
last_synced_at: '2026-05-19T10:38:00Z'
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
<!-- trie:section symbol=tests/test_freshness:_git fingerprint=f1eab105158bdbbcda4afb86a01403dc9d52b7dc85a1e29e9e9ed20abfc133db body_fp=0ee11f8c39b2d457dab55e5a1e746a848cef73577bbf348fe9ba4006c0e8bd32 source_ref=b86d8a882876e13376eb499682d0e2bdcb35e8db -->
## `_git(args: list[str], cwd: Path) -> None`

Run a `git` subprocess with `check=True` and captured output, ensuring CI sandboxes have deterministic identity.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_freshness:_init_repo fingerprint=e6a8e59044cd4691a616ada677408e96c9c856caafae13744c548e08d2b462be body_fp=20361d38cfa4188f6fdb06d4069c7b0a3d60aa1f5b0b044de45ba64f1dfabcfb source_ref=b86d8a882876e13376eb499682d0e2bdcb35e8db -->
## `_init_repo(path: Path) -> None`

Initialize a git repo at `path` with a fixed identity and `main` as the default branch.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_freshness:FakeClient fingerprint=72e1cfda4ef7f35341e25aa7cd44da1240024f4af92ce0191c7df39fdb8ea8e0 body_fp=d85a42be7a6bab66b30a40a40b9ea0faaa6dbece1fee6c76588dd06a520ec17b source_ref=b86d8a882876e13376eb499682d0e2bdcb35e8db -->
## `FakeClient(model_id="fake/test", full_model_id="fake/test", calls=0)`

Deterministic LLM stub that counts invocations and returns a fixed `GenerationResponse`.

- `calls`: incremented on each `generate` call; inspect to assert call counts.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_freshness:FakeClient.generate fingerprint=7328b86a4ba976097f1e8eec40c045a8090951dfeca29ef5debd39c4e6fc9a4b body_fp=e73563b2f976d6d0c2e2e1de5b1e3fa42e5d76d40c778f514118dfe6526b7a55 source_ref=b86d8a882876e13376eb499682d0e2bdcb35e8db -->
## `generate(self, _req: GenerationRequest) -> GenerationResponse`

Increment call counter and return a fixed deterministic `GenerationResponse`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_freshness:FakeClient.count_tokens fingerprint=d2e54258807160cae2cd3e384f807ff7ab8c686f8c79830c0798dd9ba6b1e027 body_fp=9d067b772e73f67b1bb1b8cb6fc3a256c95035c670c6695fa426a36018030c0b source_ref=b86d8a882876e13376eb499682d0e2bdcb35e8db -->
## `count_tokens(_req: GenerationRequest) -> int`

Return a fixed token count of 100 for any request.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_freshness:project fingerprint=e01c8f727530a5c7c7c2f8e977e16ddd4243b91299298f93efeff46d49c525b1 body_fp=5d19720f4709f70fec6b1c2f3aa457da5df5577fbf105ee60f6dbbd53ab167be source_ref=b86d8a882876e13376eb499682d0e2bdcb35e8db -->
## `project(tmp_path: Path) -> Path`

Pytest fixture providing a two-module Python project under a real git repo with one initial commit.

- Returns `tmp_path` containing `trie.toml`, `src/__init__.py`, `src/alpha.py`, `src/beta.py`, and an initialised git repo.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_freshness:test_stamp_round_trip fingerprint=72338228aae6b7c3fdc3d86653fb22ccd8d2e9d0edaa7dbeef3aa073ef0033c2 body_fp=b08d3cedc61dd2575045f0e794fec25deed79fe9b2700bcb7b3e76a1334ab787 source_ref=b86d8a882876e13376eb499682d0e2bdcb35e8db -->
## `test_stamp_round_trip(project: Path)`

Verify that `write_stamp` followed by `read_stamp` returns an identical `Stamp`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_freshness:test_read_stamp_returns_none_when_missing fingerprint=d1423324c130c11241ddaf7f21c5be495ca2ee4be0f4e16b370cba152baa9633 body_fp=1b67506ad46fc17cc576c723ae21260a74859e92a17dd64764a3483623a95ef7 source_ref=b86d8a882876e13376eb499682d0e2bdcb35e8db -->
## `test_read_stamp_returns_none_when_missing(project: Path)`

Assert `read_stamp` returns `None` when no stamp file exists.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_freshness:test_read_stamp_returns_none_on_malformed_json fingerprint=8794741dc828614cbf9d5e4293c991bf2ac68e37825cc9e9e666da058f8b36ee body_fp=cd80b7682982028a2754d80060f2f4576b054c225cf91f4ead9baeadee6a2694 source_ref=b86d8a882876e13376eb499682d0e2bdcb35e8db -->
## `test_read_stamp_returns_none_on_malformed_json(project: Path)`

Assert that `read_stamp` returns `None` when the stamp file contains invalid JSON.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_freshness:test_read_stamp_returns_none_on_wrong_schema fingerprint=1fb296b592032801dedae599ca493d8e2c74ea94764676276317ff8f0c20edb5 body_fp=2a26b3fd675ea60219f78ce916888d2a55bd13f5ae4b2ba6a2017595a0eb8dca source_ref=b86d8a882876e13376eb499682d0e2bdcb35e8db -->
## `test_read_stamp_returns_none_on_wrong_schema(project: Path)`

Assert `read_stamp` returns `None` when the stamp file contains valid JSON but a non-string `head` field.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_freshness:test_write_stamp_is_atomic_no_partial_files_left_behind fingerprint=c94b46ed64f02cf869ec7180ad85978df0d3147e948b402aa9937dcc93ee1df7 body_fp=f2738bce5ab214d4cf5eb1e40454cf64aa7135ec94c1eefa6f52c38f1b476747 source_ref=b86d8a882876e13376eb499682d0e2bdcb35e8db -->
## `test_write_stamp_is_atomic_no_partial_files_left_behind(project: Path)`

Assert that `write_stamp` leaves no `.tmp` files in the stamp directory after completing.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_freshness:test_scan_mtimes_returns_in_scope_files_only fingerprint=760fbeb3332ac39d1c385d18b69323e6eebe70c51abb9d4fab2dc47ab28b6e1d body_fp=4317d974687e69e4de79490740c71cbb447cf8669e605fe0da0dfdcfffe59614 source_ref=b86d8a882876e13376eb499682d0e2bdcb35e8db -->
## `test_scan_mtimes_returns_in_scope_files_only(project: Path)`

Assert that `scan_mtimes` returns only files matching the configured scope glob, excluding out-of-scope files like `trie.toml`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_freshness:test_scan_mtimes_changes_after_file_edit fingerprint=1b67abaef026c1ee9fb5fe6819e8e6f5e8c6d3d998b2dc360702895c4af0eda1 body_fp=d0841bee55879983ead4cdfc33d1ac4be2e49035ba631db4f9408cbb68913809 source_ref=b86d8a882876e13376eb499682d0e2bdcb35e8db -->
## `test_scan_mtimes_changes_after_file_edit(project: Path)`

Verify that editing a file updates its mtime entry while leaving unedited files unchanged.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_freshness:test_ensure_fresh_raises_outside_git fingerprint=89e3a8aaf80ce9d90638c4ddf7d07d34205a24f88d42f29522515c6ee04a3fb3 body_fp=55aed1828a80a742800aceaa965c8baa25c31d5b6046cd193119981b3cb22dba source_ref=b86d8a882876e13376eb499682d0e2bdcb35e8db -->
## `test_ensure_fresh_raises_outside_git(tmp_path: Path)`

Assert that `ensure_fresh_before_turn` raises `NotAGitRepoError` when called outside a git repository.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_freshness:_run_before_turn fingerprint=71c2b56e4469ba0325dfa70ff210926de24f2af8597adf671bb8f90d1d26a325 body_fp=e5354f13a4a1f9e975589055a03bdd8707dd2c07d6d2bee5122d0934cc8d460f source_ref=64a85b159ed99f38e7a764998d4eb3e65a3dcd28 -->
## `_run_before_turn(project: Path, client: FakeClient | None = None)`

Run the pre-turn freshness gate and return the `FreshnessResult`.

- `client`: pass a `FakeClient` instance to inspect `.calls` afterward; defaults to a fresh `FakeClient`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_freshness:_run_after_turn fingerprint=6e5e97c6c2cb478ecb5ccd03719aa403e8e124f067af83c532639b8cce7b413f body_fp=a1934b498c14b87c5109484db0633072588150015c32cc9a84cf24767bb6aacb source_ref=64a85b159ed99f38e7a764998d4eb3e65a3dcd28 -->
## `_run_after_turn(project: Path, client: FakeClient | None = None)`

Run the post-turn freshness gate against a project directory, returning the `FreshnessResult`.

- `client`: uses a fresh `FakeClient` if omitted.
<!-- trie:end -->









<!-- trie:section symbol=tests/test_freshness:test_new_file_added_triggers_refresh fingerprint=72a4d16126c9c220e45e18f140acba2cf99435c57bad3b59f76c56bdbc95df22 body_fp=ff2ff7062031fe34addffcbeba399353e369088bc54a1bc7c625099d0c9f0e6b source_ref=b86d8a882876e13376eb499682d0e2bdcb35e8db -->
## `test_new_file_added_triggers_refresh(project: Path)`

Assert that creating a new in-scope file triggers a `mtimes_moved` refresh even without a prior stamp entry.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_freshness:test_removed_file_triggers_refresh fingerprint=7a26a5e8a1330925f3391f5e47a09737745daef82abc9939ca1aedf5e82c41e1 body_fp=f5d4e0157d7b48710bf984ec14248a783dc44f8cd014e29eaadafb692890ace9 source_ref=b86d8a882876e13376eb499682d0e2bdcb35e8db -->
## `test_removed_file_triggers_refresh(project: Path)`

Assert that deleting an in-scope file causes the freshness gate to fire with reason `"mtimes_moved"`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_freshness:test_after_turn_picks_up_just_made_edit fingerprint=f419a9fd19a9246b59a331ceb9c9351902e6dbad879171d26f57c9fb510e145d body_fp=29313781da79f83f5c5f3239caffbd626e2bad19d0217f6f81b6cd804d3bdb4d source_ref=b86d8a882876e13376eb499682d0e2bdcb35e8db -->
## `test_after_turn_picks_up_just_made_edit(project: Path)`

Assert that `ensure_fresh_after_turn` detects an mtime change made during an agent's turn and triggers a refresh.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_freshness:test_after_turn_noop_when_nothing_changed fingerprint=9cfb3d3d7aec1e2b94374c89931394b3ad21096fa27413ad4e83b7f74ea4b5ca body_fp=b76b1db8734867acff8fab4d97ed75b8fe0baea54a5b2abbcb24bf36e2bd1ce2 source_ref=64a85b159ed99f38e7a764998d4eb3e65a3dcd28 -->
## `test_after_turn_noop_when_nothing_changed(project: Path)`

Assert that the after-turn gate returns `refreshed=False` with reason `"unchanged"` when no source files changed.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_freshness:test_cli_refresh_default_runs_after_turn fingerprint=dbcf0791a3b289b7c2f6d86d2eb2af4c4414a468cce91a2b2135c88d47d65e63 body_fp=bd28bc3dac92196ff09c457b7c89a3f7c3a20c6aad8f66e87a0194280e94bfec source_ref=b86d8a882876e13376eb499682d0e2bdcb35e8db -->
## `test_cli_refresh_default_runs_after_turn(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie refresh` (no flags) invokes the after-turn path and exits with code 0.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_freshness:test_cli_refresh_before_and_after_mutex fingerprint=a656ec572aa7041e39940d696a533e02cb4eb833e3cc5e278199b18bccaadb99 body_fp=71547666d2a5e53b2a8340b175aff82c7ab76eba00abf1d1d5898247343f5378 source_ref=b86d8a882876e13376eb499682d0e2bdcb35e8db -->
## `test_cli_refresh_before_and_after_mutex(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that passing both `--before-turn` and `--after-turn` to `trie refresh` exits with code 1 and reports mutual exclusivity.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_freshness:test_cli_refresh_outside_git_fails fingerprint=385e9125a386640f49e3e7864373a927f1f099cada6fdb1679eb7ec6337f7218 body_fp=a05a9c13d1012c7b75b2c1c865c5f429d781a86a1fdb6dbc67abb561e45e8be2 source_ref=b86d8a882876e13376eb499682d0e2bdcb35e8db -->
## `test_cli_refresh_outside_git_fails(tmp_path: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie refresh` exits with code 1 and mentions "git repository" when run outside a git repo.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_freshness:test_no_stamp_triggers_scan_without_llm fingerprint=376b562973de1b3f38953b030644c19a7115ae56d41dbf4795c146596f126188 body_fp=669db6949c72059f986014e43384460793755b7180e06e54130f4944c943e8ac source_ref=64a85b159ed99f38e7a764998d4eb3e65a3dcd28 -->
## `test_no_stamp_triggers_scan_without_llm(project: Path)`

Assert that a first run with no existing stamp triggers a graph scan, writes a stamp, but never calls the LLM.

- `result.refreshed`: must be `True` with `reason == "no_stamp"`.
- `result.incremental`: must be `None`; `run_incremental` must not fire.
- `client.calls`: must be `0`; no LLM spend on first contact.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_freshness:test_unchanged_state_is_a_noop fingerprint=8a432c89b41adb3a659c54709a1d0a2f7012900505ba89d3cd2081611b3e0569 body_fp=f4e316f4e843cc7a9bad11c1f9bc7b1994d05c859b70ee3a8eebb0df4bae62ba source_ref=64a85b159ed99f38e7a764998d4eb3e65a3dcd28 -->
## `test_unchanged_state_is_a_noop(project: Path)`

Assert that a second consecutive pre-turn gate call returns `refreshed=False` with reason `"unchanged"`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_freshness:test_head_moved_triggers_scan_without_llm fingerprint=53fd9c5d55e1b6f4fb91c44726d9ef3c4c5f968426c32d0ce5af677173de93be body_fp=015d80292cf467f6423a25ad5fab509af449c72afa618c26b62fe1dbf7d6547e source_ref=64a85b159ed99f38e7a764998d4eb3e65a3dcd28 -->
## `test_head_moved_triggers_scan_without_llm(project: Path)`

Assert that a new commit advancing HEAD triggers a graph rescan with `reason == "head_moved"` but zero LLM calls.

- `project`: real git repo fixture with one initial commit and a primed stamp.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_freshness:test_mtimes_moved_triggers_sync_with_llm fingerprint=60d1db01a580111a416263a2b7fb64da88ef5046f754beecf3c5b81fe7f38941 body_fp=e65d170ff8d9f47353d3db735c17690834e6ff77c0cd05274c870171d93b3323 source_ref=64a85b159ed99f38e7a764998d4eb3e65a3dcd28 -->
## `test_mtimes_moved_triggers_sync_with_llm(project: Path)`

Assert that editing a file without committing triggers an incremental LLM-backed resync with reason `"mtimes_moved"`.

- `result.incremental` is not `None`, confirming `run_incremental` ran rather than scan-only.
- HEAD in the stamp is unchanged because no commit was made.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_freshness:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=488d7737d3ec24cefb8eb28985ddda925a28a6bb935bceb38d9bed28300496b8 source_ref=1d2ba26c93a20762f516e32305df483e6603bae7 -->
## `tests/test_freshness`

Test suite for the turn-boundary freshness gate covering all four states: fresh, no_stamp, head_moved, and mtimes_moved.

- `project` fixture: real git repo with two Python source files and a `trie.toml`
- `FakeClient`: deterministic LLM stand-in that counts calls without hitting an API
- Non-git repos must raise `NotAGitRepoError` rather than degrade silently
<!-- trie:end -->