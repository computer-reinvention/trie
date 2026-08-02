---
trie_version: 0.3.0
source: tests/test_refresh_lock.py
file_fingerprint: 02bf21e094f3591390a4551a7c19f75534baaf9e9146ef036911a1c9fedcd732
last_synced_at: '2026-07-29T17:54:40Z'
description: Tests for the refresh lock + queue.
defines:
- kind: module
  qualified_name: tests/test_refresh_lock:__module__
  lines: 1-549
- kind: function
  qualified_name: tests/test_refresh_lock:_project
  lines: 41-44
  signature: 'def _project(tmp_path: Path) -> Path'
- kind: function
  qualified_name: tests/test_refresh_lock:test_lock_path_is_under_trie_dir
  lines: 52-54
  signature: 'def test_lock_path_is_under_trie_dir(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_refresh_lock:test_acquire_succeeds_when_uncontested
  lines: 57-62
  signature: 'def test_acquire_succeeds_when_uncontested(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_refresh_lock:test_acquire_creates_lock_file_on_first_run
  lines: 65-74
  signature: 'def test_acquire_creates_lock_file_on_first_run(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_refresh_lock:test_acquire_creates_trie_dir_if_missing
  lines: 77-83
  signature: 'def test_acquire_creates_trie_dir_if_missing(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_refresh_lock:_hold_lock_subprocess
  lines: 91-114
  signature: 'def _hold_lock_subprocess(project_root_str: str, ready_path_str: str, release_path_str: str)'
- kind: function
  qualified_name: tests/test_refresh_lock:test_contention_yields_unacquired_holder
  lines: 117-150
  signature: 'def test_contention_yields_unacquired_holder(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_refresh_lock:test_consume_queued_clears_sentinel_on_holder
  lines: 158-169
  signature: 'def test_consume_queued_clears_sentinel_on_holder(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_refresh_lock:test_mark_queued_is_idempotent
  lines: 172-204
  signature: 'def test_mark_queued_is_idempotent(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_refresh_lock:_hold_and_crash
  lines: 212-225
  signature: 'def _hold_and_crash(project_root_str: str, ready_path_str: str)'
- kind: function
  qualified_name: tests/test_refresh_lock:test_lock_released_when_holder_crashes
  lines: 228-242
  signature: 'def test_lock_released_when_holder_crashes(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_refresh_lock:test_cli_graph_only_when_contended_queues_and_exits_zero
  lines: 250-326
  signature: 'def test_cli_graph_only_when_contended_queues_and_exits_zero( tmp_path: Path, monkeypatch: pytest.MonkeyPatch )'
- kind: function
  qualified_name: tests/test_refresh_lock:_make_minimal_trie_project
  lines: 337-361
  signature: 'def _make_minimal_trie_project(tmp_path: Path) -> None'
- kind: function
  qualified_name: tests/test_refresh_lock:test_cli_sync_when_contended_exits_two_with_explanation
  lines: 364-418
  signature: 'def test_cli_sync_when_contended_exits_two_with_explanation( tmp_path: Path, monkeypatch: pytest.MonkeyPatch )'
- kind: function
  qualified_name: tests/test_refresh_lock:test_cli_lock_check_when_free_exits_zero
  lines: 421-434
  signature: 'def test_cli_lock_check_when_free_exits_zero(tmp_path: Path, monkeypatch: pytest.MonkeyPatch)'
- kind: function
  qualified_name: tests/test_refresh_lock:test_cli_lock_check_when_no_trie_toml_exits_zero
  lines: 437-453
  signature: 'def test_cli_lock_check_when_no_trie_toml_exits_zero( tmp_path: Path, monkeypatch: pytest.MonkeyPatch )'
- kind: function
  qualified_name: tests/test_refresh_lock:test_cli_lock_check_when_contended_exits_two
  lines: 456-493
  signature: 'def test_cli_lock_check_when_contended_exits_two(tmp_path: Path, monkeypatch: pytest.MonkeyPatch)'
- kind: function
  qualified_name: tests/test_refresh_lock:test_cli_plan_when_contended_exits_two
  lines: 496-538
  signature: 'def test_cli_plan_when_contended_exits_two(tmp_path: Path, monkeypatch: pytest.MonkeyPatch)'
incoming_refs: 0
outgoing_refs: 30
---
<!-- trie:section symbol=tests/test_refresh_lock:__module__ fingerprint=e898e798072bf5c540959d26eaadc8cccfdbc85d6e9a0dcc06ceaa5812d960e9 body_fp=7cfb574da64cd1185c8037bdb6bf6a7055036c90da0fcac4d18d03fe3f597786 source_ref=a247889420e6c77627c6b64724dd207c13c8bf27 role=test-infrastructure -->
Tests for refresh lock serialization and queueing mechanisms using real subprocess contention.

- Validates single-holder acquisition, contention handling, and tail pass queue consumption
- Tests crash safety where OS releases flock when process dies
- Covers CLI integration for refresh (queues), sync/plan (exit 2), and lock-check commands
- Uses subprocess workers because flock is per-process, not per-thread
- Skips entirely on Windows platforms where POSIX flock is unavailable
<!-- trie:end -->
<!-- trie:section symbol=tests/test_refresh_lock:_project fingerprint=d565ca36636bbc0160570a7007ae6fc5190e0f22ea5207096d19bbfa4b36ed93 body_fp=2ca13a96895b0b04a8ce896a19a596cdff2a40dd951225af0784db378c42795b source_ref=a247889420e6c77627c6b64724dd207c13c8bf27 role=test-infrastructure -->
## `def _project(tmp_path: Path) -> Path`

Creates a minimal test project by adding a `.trie/` directory to the given path and returns the project root.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_refresh_lock:test_lock_path_is_under_trie_dir fingerprint=8bbda127ee1137d0a1b0329d924df2927395204fb7f2c846dcd845fdb4ac3ccc body_fp=5fc0b0531e5fe59abdeaf7e2b742ab1158bd09e779e93208e294c85240b24d64 source_ref=a247889420e6c77627c6b64724dd207c13c8bf27 role=test-infrastructure -->
## `def test_lock_path_is_under_trie_dir(tmp_path: Path)`

Verifies that lock_path and queued_path return paths under the `.trie/` directory with correct filenames.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_refresh_lock:test_acquire_succeeds_when_uncontested fingerprint=3e09977ec2612800854e9984cd659c84e65ce56601f3f73e419772efeb2ef874 body_fp=64c07dad9a64f773087fb98fb6f066d35b57ad0be8696855df4e0a509e9135cc source_ref=a247889420e6c77627c6b64724dd207c13c8bf27 role=test-infrastructure -->
## `def test_acquire_succeeds_when_uncontested(tmp_path: Path)`

Verifies that `try_acquire` returns a holder with `acquired=True` when no other process holds the lock.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_refresh_lock:test_acquire_creates_lock_file_on_first_run fingerprint=9cb01193c3f4a28b75060da57e928faf8dc903ce9c9406ed3576fd25e9971bc2 body_fp=0a0d052a8059230bee86c4eb47bd5093fb8b9c410a7e9d0e80513873647e5519 source_ref=a247889420e6c77627c6b64724dd207c13c8bf27 role=test-infrastructure -->
## `def test_acquire_creates_lock_file_on_first_run(tmp_path: Path)`

Verifies that the first `try_acquire` call creates the lock file and persists it after release.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_refresh_lock:test_acquire_creates_trie_dir_if_missing fingerprint=b638dca8339697dc04605a4af756a9cbb37a57427ce236d21135034bdd0c0626 body_fp=4e39f2348a1615118641b8d8c10b564f9688bb645754f34dcdd56632de912396 source_ref=a247889420e6c77627c6b64724dd207c13c8bf27 role=test-infrastructure -->
## `def test_acquire_creates_trie_dir_if_missing(tmp_path: Path)`

Verifies that try_acquire creates the `.trie/` directory when it doesn't exist on a fresh project.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_refresh_lock:_hold_lock_subprocess fingerprint=04902af6144be334b75945c33218ddbfdad31447508c80fd013a40592fe20537 body_fp=245613fdf7cf669ec00bbe3f7b62e07e4e7bfc176d07f1aa9616c9d6e9b1b8bc source_ref=a247889420e6c77627c6b64724dd207c13c8bf27 role=test-infrastructure -->
## `def _hold_lock_subprocess(project_root_str: str, ready_path_str: str, release_path_str: str)`

Acquires refresh lock in a child process, writes status to ready file, and waits for release signal.

- Used in multiprocessing tests to simulate lock contention across process boundaries
- Polls release file every 10ms with 5-second timeout to avoid busy-waiting
- Returns early if lock acquisition fails
<!-- trie:end -->
<!-- trie:section symbol=tests/test_refresh_lock:test_contention_yields_unacquired_holder fingerprint=8c9998c0eb408142f0a577629a82deea55a533a89ee0626c5ed1f126bd6f6c3a body_fp=b3510ab29153b996329fa8ad328f39ac10576dba63075527bfd11914c0852c9f source_ref=a247889420e6c77627c6b64724dd207c13c8bf27 role=test-infrastructure -->
## `def test_contention_yields_unacquired_holder(tmp_path: Path)`

Verifies that `try_acquire` returns an unacquired holder when another process holds the lock.

- Uses subprocess to simulate lock contention since flock is per-process
- Confirms second acquirer gets `acquired=False` and can mark queued
- Tests that contested holder's `consume_queued()` returns False
<!-- trie:end -->
<!-- trie:section symbol=tests/test_refresh_lock:test_consume_queued_clears_sentinel_on_holder fingerprint=f7b258443fe0b934c75164bbe0f16f8b6788adb5d9ef67efcbb8fd7a34b15da5 body_fp=c2eb30b6115de2ba1b1a82cae49d204cc3279f00cdc6ff5d69b04c2a77c15925 source_ref=a247889420e6c77627c6b64724dd207c13c8bf27 role=test-infrastructure -->
## `def test_consume_queued_clears_sentinel_on_holder(tmp_path: Path)`

Tests that RefreshLockHolder.consume_queued() returns True once and removes the sentinel file.

- Simulates external mark_queued() call by writing empty queued file
- Verifies consume_queued() returns False on subsequent calls after draining
<!-- trie:end -->
<!-- trie:section symbol=tests/test_refresh_lock:test_mark_queued_is_idempotent fingerprint=15381b0b69d987291e037a6120094d62d7e53ea5f79bd9cec54a7037b4714a0f body_fp=7c7bd4ae71e8881ede7d4b658804c88a5eed6b383f08e8145f3cb8381556f248 source_ref=a247889420e6c77627c6b64724dd207c13c8bf27 role=test-infrastructure -->
## `def test_mark_queued_is_idempotent(tmp_path: Path)`

Verifies that calling `mark_queued()` multiple times on an unacquired holder creates only one queued sentinel file.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_refresh_lock:_hold_and_crash fingerprint=0b7790c815659d7ffaaa415e127632c29b4de497a4da227b88f503be51c0bd9a body_fp=d16c15d9d64e43df4e9446afae5af391493044350a0e23c2ff577bc878b30b0f source_ref=a247889420e6c77627c6b64724dd207c13c8bf27 role=test-infrastructure -->
## `def _hold_and_crash(project_root_str: str, ready_path_str: str)`

Acquires the refresh lock, signals readiness to parent process, then exits without cleanup to test crash recovery.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_refresh_lock:test_lock_released_when_holder_crashes fingerprint=e146cba42b6a03c824c609b2039cb6f8183d8ddc97aafed57587a0bd6c9c94ec body_fp=3d3f71ab6ff7f7f0682d8bf6d2507eaa69608bfc7f8429cdacba4ad7c7a29ffb source_ref=a247889420e6c77627c6b64724dd207c13c8bf27 role=test-infrastructure -->
## `def test_lock_released_when_holder_crashes(tmp_path: Path)`

Verifies that when a lock holder process crashes without cleanup, the OS releases the flock and subsequent processes can acquire the lock normally.

- Uses `_hold_and_crash` subprocess that calls `os._exit()` to skip context manager cleanup
- Confirms the crashed process had acquired the lock before dying
- Tests that a new `try_acquire()` call succeeds after the crash
<!-- trie:end -->
<!-- trie:section symbol=tests/test_refresh_lock:test_cli_graph_only_when_contended_queues_and_exits_zero fingerprint=46f04de851e82b86b322865ed1052dd1231e682a6e2cbce9e6f2f5dc2f82c3b3 body_fp=60e98251f0da21cea8be80adf72ca976125009291b2c8d225bd47b4ce4e28274 source_ref=3b3c20241df9bcdf7a1fce82196074b5f88bde0a role=test -->
## `def test_cli_graph_only_when_contended_queues_and_exits_zero( tmp_path: Path, monkeypatch: pytest.MonkeyPatch )`

Assert that `trie sync --graph-only` exits 0, prints "queued", and writes the queued sentinel when another process holds the refresh lock.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_refresh_lock:_make_minimal_trie_project fingerprint=d26724620fc7e0de633567db6872771e9e400e24a9ff452df9c5f9a221f09e06 body_fp=008b6f12587123161616c6d6280d4e7dc7e2189980b2019ad6d7d4dda0971438 source_ref=a247889420e6c77627c6b64724dd207c13c8bf27 role=test-infrastructure -->
## `def _make_minimal_trie_project(tmp_path: Path) -> None`

Creates a minimal trie project with configuration file, source tree, and git repository for testing.

- Sets up `trie.toml` with default configuration including scope and model settings
- Creates `src/alpha.py` with a simple function definition
- Initializes git repo with user config and commits the initial files
<!-- trie:end -->
<!-- trie:section symbol=tests/test_refresh_lock:test_cli_sync_when_contended_exits_two_with_explanation fingerprint=3a772bb425b6060844eafc3672ea959d26d6424016c7d15b5504038b7dce988e body_fp=66e0cbe3295ae3fbd3d92b8ea979496146eb9de0a43ea289d83e9575d26a506f source_ref=a247889420e6c77627c6b64724dd207c13c8bf27 role=test-infrastructure -->
## `def test_cli_sync_when_contended_exits_two_with_explanation( tmp_path: Path, monkeypatch: pytest.MonkeyPatch )`

Verifies that `trie sync` exits with code 2 and prints an explanatory message when another process holds the refresh lock.

- Uses subprocess to simulate lock contention during CLI invocation
- Confirms sync exits 2 (transient error) rather than queueing like refresh command
- Validates no queued sentinel is created since sync fails explicitly rather than deferring
<!-- trie:end -->
<!-- trie:section symbol=tests/test_refresh_lock:test_cli_lock_check_when_free_exits_zero fingerprint=6c3e8123f52edb3e23a6c52e14af4b0a5eed829066380d068e64631ecbbd7022 body_fp=ebb64e979a4cc827ace10ac4b858792fe40d4afe6676e472a1d2055e8bcc9e03 source_ref=a247889420e6c77627c6b64724dd207c13c8bf27 role=test-infrastructure -->
## `def test_cli_lock_check_when_free_exits_zero(tmp_path: Path, monkeypatch: pytest.MonkeyPatch)`

Tests that `trie lock-check` exits 0 with "free" message when no process holds the refresh lock.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_refresh_lock:test_cli_lock_check_when_no_trie_toml_exits_zero fingerprint=6bed6cededf4924a0d32f1e0a8b7e5cfb94090daf833346c269f4353281f06f4 body_fp=2a1291bc7a13ccc2227419ce39d190091d669911dac0ee17e9a85aab4635da25 source_ref=a247889420e6c77627c6b64724dd207c13c8bf27 role=test-infrastructure -->
## `def test_cli_lock_check_when_no_trie_toml_exits_zero( tmp_path: Path, monkeypatch: pytest.MonkeyPatch )`

Verifies `trie lock-check` exits 0 with no-op message when no trie.toml exists.

- Tests graceful degradation for pre-commit hooks in unconfigured repositories
- Ensures lock-check doesn't error on missing configuration
<!-- trie:end -->
<!-- trie:section symbol=tests/test_refresh_lock:test_cli_lock_check_when_contended_exits_two fingerprint=5c325164beec1dde3174f126d7cbbae3f429d6fc4cf67780c3d80a8ee7996f1c body_fp=3b19d3eb942948de9cc6e3d6c7319a779606e0bb0b017650039f179667ab4d77 source_ref=a247889420e6c77627c6b64724dd207c13c8bf27 role=test-infrastructure -->
## `def test_cli_lock_check_when_contended_exits_two(tmp_path: Path, monkeypatch: pytest.MonkeyPatch)`

Tests that `trie lock-check` exits 2 when another process holds the refresh lock.

- Creates subprocess holding lock via `_hold_lock_subprocess` helper
- Invokes `trie lock-check` CLI command while lock is contested
- Verifies exit code 2 and error message mentioning "another trie process"
<!-- trie:end -->
<!-- trie:section symbol=tests/test_refresh_lock:test_cli_plan_when_contended_exits_two fingerprint=defbb4e21f11935fcee5881c43a0feb5e59cb265a6eff5b815a8ec0ffdc8dabd body_fp=33d6d2802e1ee3fd45e6ea59b42f448894b98aaf80af439d3c725a0cc9c8636f source_ref=a247889420e6c77627c6b64724dd207c13c8bf27 role=test-infrastructure -->
## `def test_cli_plan_when_contended_exits_two(tmp_path: Path, monkeypatch: pytest.MonkeyPatch)`

Tests that `trie plan` exits with code 2 when another process holds the lock.

- Creates a child process that holds the lock via `_hold_lock_subprocess`
- Verifies the contended `trie plan` command exits with status code 2
- Confirms the error message mentions "another trie process"
- Uses multiprocessing because flock is per-process, not per-thread
<!-- trie:end -->