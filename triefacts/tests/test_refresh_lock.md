---
trie_version: 0.1.5
source: tests/test_refresh_lock.py
file_fingerprint: f37035603e7cde190a1a87d214327d25c837bec535ba99a295b010093dd1e3f0
last_synced_at: '2026-05-28T01:40:15Z'
description: Tests for the refresh lock + queue.
defines:
- kind: module
  qualified_name: tests/test_refresh_lock:__module__
  lines: 1-549
- kind: function
  qualified_name: tests/test_refresh_lock:_project
  lines: 41-44
- kind: function
  qualified_name: tests/test_refresh_lock:test_lock_path_is_under_trie_dir
  lines: 52-54
- kind: function
  qualified_name: tests/test_refresh_lock:test_acquire_succeeds_when_uncontested
  lines: 57-62
- kind: function
  qualified_name: tests/test_refresh_lock:test_acquire_creates_lock_file_on_first_run
  lines: 65-74
- kind: function
  qualified_name: tests/test_refresh_lock:test_acquire_creates_trie_dir_if_missing
  lines: 77-83
- kind: function
  qualified_name: tests/test_refresh_lock:_hold_lock_subprocess
  lines: 91-114
- kind: function
  qualified_name: tests/test_refresh_lock:test_contention_yields_unacquired_holder
  lines: 117-150
- kind: function
  qualified_name: tests/test_refresh_lock:test_consume_queued_clears_sentinel_on_holder
  lines: 158-169
- kind: function
  qualified_name: tests/test_refresh_lock:test_mark_queued_is_idempotent
  lines: 172-204
- kind: function
  qualified_name: tests/test_refresh_lock:_hold_and_crash
  lines: 212-225
- kind: function
  qualified_name: tests/test_refresh_lock:test_lock_released_when_holder_crashes
  lines: 228-242
- kind: function
  qualified_name: tests/test_refresh_lock:test_cli_refresh_when_contended_queues_and_exits_zero
  lines: 250-326
- kind: function
  qualified_name: tests/test_refresh_lock:_make_minimal_trie_project
  lines: 337-361
- kind: function
  qualified_name: tests/test_refresh_lock:test_cli_sync_when_contended_exits_two_with_explanation
  lines: 364-418
- kind: function
  qualified_name: tests/test_refresh_lock:test_cli_lock_check_when_free_exits_zero
  lines: 421-434
- kind: function
  qualified_name: tests/test_refresh_lock:test_cli_lock_check_when_no_trie_toml_exits_zero
  lines: 437-453
- kind: function
  qualified_name: tests/test_refresh_lock:test_cli_lock_check_when_contended_exits_two
  lines: 456-493
- kind: function
  qualified_name: tests/test_refresh_lock:test_cli_plan_when_contended_exits_two
  lines: 496-538
incoming_refs: 0
outgoing_refs: 19
---
<!-- trie:section symbol=tests/test_refresh_lock:__module__ fingerprint=e898e798072bf5c540959d26eaadc8cccfdbc85d6e9a0dcc06ceaa5812d960e9 body_fp=023f1ff370324498657623e8120077a01e4007afdec34a512ec74f2a504b4933 source_ref=a247889420e6c77627c6b64724dd207c13c8bf27 -->
## `tests/test_refresh_lock`

Test suite for the refresh lock and queue mechanism used to serialise concurrent `trie refresh` calls.

- Skipped entirely on Windows; requires POSIX `flock` semantics.
- Contention and crash-safety tests use `spawn`-context subprocesses to avoid same-process flock reuse.
- Covers: uncontested acquire, contention yielding `acquired=False`, `mark_queued`/`consume_queued` lifecycle, crash release, and CLI exit-code contracts for `refresh`, `sync`, `plan`, and `lock-check`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_refresh_lock:_project fingerprint=d565ca36636bbc0160570a7007ae6fc5190e0f22ea5207096d19bbfa4b36ed93 body_fp=035bff1a82d554ae998f16862e577cfe6716bc3065a952caeb139e1934ca268f source_ref=a247889420e6c77627c6b64724dd207c13c8bf27 -->
## `_project(tmp_path: Path) -> Path`

Create a minimal project fixture with only a `.trie/` directory and return `tmp_path`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_refresh_lock:test_lock_path_is_under_trie_dir fingerprint=8bbda127ee1137d0a1b0329d924df2927395204fb7f2c846dcd845fdb4ac3ccc body_fp=9022b01f915ee41ca92a3b071995594cf2cf09ead8c8518f7a1255fb21a07092 source_ref=a247889420e6c77627c6b64724dd207c13c8bf27 -->
## `test_lock_path_is_under_trie_dir(tmp_path: Path)`

Assert that `lock_path` and `queued_path` resolve to the expected files inside `.trie/`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_refresh_lock:test_acquire_succeeds_when_uncontested fingerprint=3e09977ec2612800854e9984cd659c84e65ce56601f3f73e419772efeb2ef874 body_fp=733a12c4d0044c83ac66c906fe965178f045103134f814f616bc5616fdcc4048 source_ref=a247889420e6c77627c6b64724dd207c13c8bf27 -->
## `test_acquire_succeeds_when_uncontested(tmp_path: Path)`

Verify that `try_acquire` sets `acquired=True` and `consume_queued()` returns `False` when no contention exists.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_refresh_lock:test_acquire_creates_lock_file_on_first_run fingerprint=9cb01193c3f4a28b75060da57e928faf8dc903ce9c9406ed3576fd25e9971bc2 body_fp=37dbe245deb08bb67251d51ed0287e318a0ea78ebb14d159809521573b57fa95 source_ref=a247889420e6c77627c6b64724dd207c13c8bf27 -->
## `test_acquire_creates_lock_file_on_first_run(tmp_path: Path)`

Assert that the first `try_acquire` creates the lock file and that it persists after the context manager exits.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_refresh_lock:test_acquire_creates_trie_dir_if_missing fingerprint=b638dca8339697dc04605a4af756a9cbb37a57427ce236d21135034bdd0c0626 body_fp=4df341b19344806fa9c3b913fcbf8989d5ac14d54e25d5d46265ce8307a1b379 source_ref=a247889420e6c77627c6b64724dd207c13c8bf27 -->
## `test_acquire_creates_trie_dir_if_missing(tmp_path: Path)`

Assert that `try_acquire` creates the `.trie/` directory automatically when it is absent.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_refresh_lock:_hold_lock_subprocess fingerprint=04902af6144be334b75945c33218ddbfdad31447508c80fd013a40592fe20537 body_fp=340f8b62c0c96ebaadb889acc18a4dc9289085ffdda9269afb7d1be353678c57 source_ref=a247889420e6c77627c6b64724dd207c13c8bf27 -->
## `_hold_lock_subprocess(project_root_str: str, ready_path_str: str, release_path_str: str)`

Run in a child process to acquire the trie lock, signal readiness, and block until the parent authorises release.

- `ready_path_str`: file written `"acquired"` or `"missed"` to signal lock status to parent.
- `release_path_str`: parent creates this file to unblock the subprocess.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_refresh_lock:test_contention_yields_unacquired_holder fingerprint=8c9998c0eb408142f0a577629a82deea55a533a89ee0626c5ed1f126bd6f6c3a body_fp=f6eee802e836b73a13b765f9ddbe4616965a6766db85e561443987e641b8f3e9 source_ref=a247889420e6c77627c6b64724dd207c13c8bf27 -->
## `test_contention_yields_unacquired_holder(tmp_path: Path)`

Assert that `try_acquire` returns `acquired=False` without blocking when a child process holds the flock.

- `mark_queued()` on an unacquired holder writes the queued sentinel file.
- `consume_queued()` on an unacquired holder returns `False` (no-op).
<!-- trie:end -->
<!-- trie:section symbol=tests/test_refresh_lock:test_consume_queued_clears_sentinel_on_holder fingerprint=f7b258443fe0b934c75164bbe0f16f8b6788adb5d9ef67efcbb8fd7a34b15da5 body_fp=ac3eb4334f3e4e2bac50458998d8912af550bc3714be36b89fa0684bcfe139b0 source_ref=a247889420e6c77627c6b64724dd207c13c8bf27 -->
## `test_consume_queued_clears_sentinel_on_holder(tmp_path: Path)`

Verify that `consume_queued()` returns `True` exactly once and removes the queued sentinel file.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_refresh_lock:test_mark_queued_is_idempotent fingerprint=15381b0b69d987291e037a6120094d62d7e53ea5f79bd9cec54a7037b4714a0f body_fp=1f7d15d0f8585d09a696761a5fe72fb047ae62be3e316c021aa94e5957dc4269 source_ref=a247889420e6c77627c6b64724dd207c13c8bf27 -->
## `test_mark_queued_is_idempotent(tmp_path: Path)`

Assert that calling `mark_queued()` twice on an unacquired holder leaves exactly one queued sentinel file.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_refresh_lock:_hold_and_crash fingerprint=0b7790c815659d7ffaaa415e127632c29b4de497a4da227b88f503be51c0bd9a body_fp=7fce0acfbd795bcfb3a615264ec8e7632337c0726f381e896552cfd34ec7cbd8 source_ref=a247889420e6c77627c6b64724dd207c13c8bf27 -->
## `_hold_and_crash(project_root_str: str, ready_path_str: str)`

Acquire the refresh lock in a subprocess, signal readiness, then exit via `os._exit` without releasing.

- Writes `"acquired"` or `"missed"` to `ready_path_str` before exiting.
- Uses `os._exit` to skip context-manager cleanup, modelling a SIGKILL'd process.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_refresh_lock:test_lock_released_when_holder_crashes fingerprint=e146cba42b6a03c824c609b2039cb6f8183d8ddc97aafed57587a0bd6c9c94ec body_fp=92d6fd0111e0d96515ead0eb28c412a4fa254a945292a08d17ea14ad35e736e6 source_ref=a247889420e6c77627c6b64724dd207c13c8bf27 -->
## `test_lock_released_when_holder_crashes(tmp_path: Path)`

Assert that the flock is released when a holder exits via `os._exit` without running the context manager cleanup.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_refresh_lock:test_cli_refresh_when_contended_queues_and_exits_zero fingerprint=f6d69648eb1e68bd974e36df7869e38c8cc20bef67544657499bf1b17db256d1 body_fp=4b7133ce1f99545efc37b14cfb71dd4b8cff8ab58af3b65f2118080572593a4d source_ref=a247889420e6c77627c6b64724dd207c13c8bf27 -->
## `test_cli_refresh_when_contended_queues_and_exits_zero(tmp_path: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie refresh` under lock contention exits 0, prints "queued", and writes the queued sentinel file.

- Uses a spawned child process to hold the flock before invoking the CLI.
- Stubs `trie.cli.make_client` to prevent real Anthropic client construction.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_refresh_lock:_make_minimal_trie_project fingerprint=d26724620fc7e0de633567db6872771e9e400e24a9ff452df9c5f9a221f09e06 body_fp=5cbd617c107e01e6b6b5431c71751e65d9b7114a1aca8fb80c806c5c9a77013a source_ref=a247889420e6c77627c6b64724dd207c13c8bf27 -->
## `_make_minimal_trie_project(tmp_path: Path) -> None`

Create a `trie.toml`, a `src/alpha.py`, and a single-commit git repo inside `tmp_path`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_refresh_lock:test_cli_sync_when_contended_exits_two_with_explanation fingerprint=3a772bb425b6060844eafc3672ea959d26d6424016c7d15b5504038b7dce988e body_fp=a1b67095e6926d641a68bafb15074cf308787f597a1904f733efe460dd270307 source_ref=a247889420e6c77627c6b64724dd207c13c8bf27 -->
## `test_cli_sync_when_contended_exits_two_with_explanation(tmp_path: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie sync` exits 2 with an explanatory message when another process holds the lock, and leaves no queued sentinel.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_refresh_lock:test_cli_lock_check_when_free_exits_zero fingerprint=6c3e8123f52edb3e23a6c52e14af4b0a5eed829066380d068e64631ecbbd7022 body_fp=809b114df79a5429e923cb695ebf2e5106b6d12d9474bb4e63d05bfc4f668f67 source_ref=a247889420e6c77627c6b64724dd207c13c8bf27 -->
## `test_cli_lock_check_when_free_exits_zero(tmp_path: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie lock-check` exits 0 and prints "free" when no process holds the lock.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_refresh_lock:test_cli_lock_check_when_no_trie_toml_exits_zero fingerprint=6bed6cededf4924a0d32f1e0a8b7e5cfb94090daf833346c269f4353281f06f4 body_fp=a77b4e4a832ea61d51c4c4424f5770c955cdaa420885dec30db85b8081967e4a source_ref=a247889420e6c77627c6b64724dd207c13c8bf27 -->
## `test_cli_lock_check_when_no_trie_toml_exits_zero(tmp_path: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie lock-check` exits 0 and reports "no trie.toml" when no config file exists.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_refresh_lock:test_cli_lock_check_when_contended_exits_two fingerprint=5c325164beec1dde3174f126d7cbbae3f429d6fc4cf67780c3d80a8ee7996f1c body_fp=7224995907de4b88b37d24a4d3aa7023834d6407c7a31cbdbfe9a9c54591c2ae source_ref=a247889420e6c77627c6b64724dd207c13c8bf27 -->
## `test_cli_lock_check_when_contended_exits_two(tmp_path: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie lock-check` exits 2 with an explanatory message when another process holds the lock.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_refresh_lock:test_cli_plan_when_contended_exits_two fingerprint=defbb4e21f11935fcee5881c43a0feb5e59cb265a6eff5b815a8ec0ffdc8dabd body_fp=e9e273ce2406263d0213ca566a2c59c60b1a2caa28855feaa160b53162cc6522 source_ref=a247889420e6c77627c6b64724dd207c13c8bf27 -->
## `test_cli_plan_when_contended_exits_two(tmp_path: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie plan` exits 2 with an "another trie process" message when the lock is held by a child process.
<!-- trie:end -->