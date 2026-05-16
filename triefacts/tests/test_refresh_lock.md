---
trie_version: 0.1.0
source: tests/test_refresh_lock.py
file_fingerprint: b480798bd7190b19332c9dec1d8046c15a7b4aad0275b2ced76ab2f7e9167304
last_synced_at: '2026-05-16T13:17:25Z'
description: Tests for the refresh lock + queue.
defines:
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
outgoing_refs: 17
---
<!-- trie:section symbol=tests/test_refresh_lock:_project fingerprint=d565ca36636bbc0160570a7007ae6fc5190e0f22ea5207096d19bbfa4b36ed93 body_fp=eca8b2fcf3abc0a59c2218a9c60b4a76c7b9b67efea2c5f690d1e630dc431a71 source_ref=9f8c7ea4e0193e8aeb633f211fc19584648aa7a3 -->
## `_project(tmp_path: Path) -> Path`

Create the `.trie/` directory inside `tmp_path` and return `tmp_path` as the project root.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_refresh_lock:test_lock_path_is_under_trie_dir fingerprint=8bbda127ee1137d0a1b0329d924df2927395204fb7f2c846dcd845fdb4ac3ccc body_fp=9022b01f915ee41ca92a3b071995594cf2cf09ead8c8518f7a1255fb21a07092 source_ref=9f8c7ea4e0193e8aeb633f211fc19584648aa7a3 -->
## `test_lock_path_is_under_trie_dir(tmp_path: Path)`

Assert that `lock_path` and `queued_path` resolve to the expected files inside `.trie/`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_refresh_lock:test_acquire_succeeds_when_uncontested fingerprint=3e09977ec2612800854e9984cd659c84e65ce56601f3f73e419772efeb2ef874 body_fp=8a7337cbb8dc72490ec8fc271b7127af3ce17582b1f573da715363c0c6b7ecf0 source_ref=9f8c7ea4e0193e8aeb633f211fc19584648aa7a3 -->
## `test_acquire_succeeds_when_uncontested(tmp_path: Path)`

Assert that `try_acquire` on an uncontested lock yields `acquired=True` and `consume_queued()` returns `False`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_refresh_lock:test_acquire_creates_lock_file_on_first_run fingerprint=9cb01193c3f4a28b75060da57e928faf8dc903ce9c9406ed3576fd25e9971bc2 body_fp=7c6b669a9dc74e8575fb183ab9b478efd333c3f0cb232fa1823c6ae3835d71a8 source_ref=9f8c7ea4e0193e8aeb633f211fc19584648aa7a3 -->
## `test_acquire_creates_lock_file_on_first_run(tmp_path: Path)`

Assert that the first `try_acquire` creates and persists the lock file after release.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_refresh_lock:test_acquire_creates_trie_dir_if_missing fingerprint=b638dca8339697dc04605a4af756a9cbb37a57427ce236d21135034bdd0c0626 body_fp=360bf57001b90ca2e7346966412a5adea91b78e1a12dd229eca0726accb8c1e2 source_ref=9f8c7ea4e0193e8aeb633f211fc19584648aa7a3 -->
## `test_acquire_creates_trie_dir_if_missing(tmp_path: Path)`

Assert that `try_acquire` creates `.trie/` automatically when it doesn't exist before the first lock attempt.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_refresh_lock:_hold_lock_subprocess fingerprint=04902af6144be334b75945c33218ddbfdad31447508c80fd013a40592fe20537 body_fp=73d751304060ad334f2f91a8acb81bc2b9c1a52be289e7a979f468a14552b185 source_ref=9f8c7ea4e0193e8aeb633f211fc19584648aa7a3 -->
## `_hold_lock_subprocess(project_root_str: str, ready_path_str: str, release_path_str: str)`

Acquire the lock in a child process, signal readiness via a sentinel file, then wait for the parent to write a release file before exiting.

- `ready_path_str`: path to file written with `"acquired"` or `"missed"` once lock is attempted.
- `release_path_str`: path the parent creates to unblock the child; polled for up to 5 s.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_refresh_lock:test_contention_yields_unacquired_holder fingerprint=8c9998c0eb408142f0a577629a82deea55a533a89ee0626c5ed1f126bd6f6c3a body_fp=abd31e9761cd01ce39166d9588ed72395d3550d28513c7c8da42eb1e7ad2ab96 source_ref=9f8c7ea4e0193e8aeb633f211fc19584648aa7a3 -->
## `test_contention_yields_unacquired_holder(tmp_path: Path)`

Verify that `try_acquire` returns a holder with `acquired=False` when another process holds the flock.

- `mark_queued()` on the unacquired holder creates the queued sentinel file.
- `consume_queued()` on the unacquired holder returns `False`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_refresh_lock:test_consume_queued_clears_sentinel_on_holder fingerprint=f7b258443fe0b934c75164bbe0f16f8b6788adb5d9ef67efcbb8fd7a34b15da5 body_fp=53ee1b37e0922f532739b5e96037888c100f3aceaa48ea928621ad1d915f2421 source_ref=9f8c7ea4e0193e8aeb633f211fc19584648aa7a3 -->
## `test_consume_queued_clears_sentinel_on_holder(tmp_path: Path)`

Verify that `consume_queued()` returns `True` once and removes the sentinel file, with a subsequent call returning `False`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_refresh_lock:test_mark_queued_is_idempotent fingerprint=15381b0b69d987291e037a6120094d62d7e53ea5f79bd9cec54a7037b4714a0f body_fp=53bfc9c336e145c249f472b85d1a8fe59d8f0a4431292b155b6771b6189d7c27 source_ref=9f8c7ea4e0193e8aeb633f211fc19584648aa7a3 -->
## `test_mark_queued_is_idempotent(tmp_path: Path)`

Assert that calling `mark_queued()` twice on an unacquired holder leaves exactly one sentinel file.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_refresh_lock:_hold_and_crash fingerprint=0b7790c815659d7ffaaa415e127632c29b4de497a4da227b88f503be51c0bd9a body_fp=e682fa45f30da6c9102000ac1205d5f98f8a0f52583ac9d38bf37e288ad28bc0 source_ref=9f8c7ea4e0193e8aeb633f211fc19584648aa7a3 -->
## `_hold_and_crash(project_root_str: str, ready_path_str: str)`

Acquire the lock in a subprocess, signal readiness, then exit via `os._exit` without releasing, simulating a SIGKILL'd process.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_refresh_lock:test_lock_released_when_holder_crashes fingerprint=e146cba42b6a03c824c609b2039cb6f8183d8ddc97aafed57587a0bd6c9c94ec body_fp=d1ff39cc9ee70327f95877f0504fed1688c144dad90bf249913214a2c61b5f9c source_ref=9f8c7ea4e0193e8aeb633f211fc19584648aa7a3 -->
## `test_lock_released_when_holder_crashes(tmp_path: Path)`

Verify that a lock held by a process that dies via `os._exit` becomes acquirable by the next caller.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_refresh_lock:test_cli_refresh_when_contended_queues_and_exits_zero fingerprint=f6d69648eb1e68bd974e36df7869e38c8cc20bef67544657499bf1b17db256d1 body_fp=3d5bccb5140759890af2ea989313e4b4c2ccba45e10319fc9964f68b543be92c source_ref=9f8c7ea4e0193e8aeb633f211fc19584648aa7a3 -->
## `test_cli_refresh_when_contended_queues_and_exits_zero(tmp_path: Path, monkeypatch: pytest.MonkeyPatch)`

Verify that `trie refresh` exits 0 and emits "queued" when another process holds the lock.

- `monkeypatch`: stubs `trie.cli.make_client` to avoid real API client construction.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_refresh_lock:_make_minimal_trie_project fingerprint=d26724620fc7e0de633567db6872771e9e400e24a9ff452df9c5f9a221f09e06 body_fp=c3e7c95340c777221bb66ef93ac9b0d36d1c87a64f647f6660846d0c21a9b6b5 source_ref=cf7d43d9e6d5cb175d70666333156560a4f18df2 -->
## `_make_minimal_trie_project(tmp_path: Path) -> None`

Create a `trie.toml`, a minimal Python source tree, and a one-commit git repo inside `tmp_path`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_refresh_lock:test_cli_sync_when_contended_exits_two_with_explanation fingerprint=3a772bb425b6060844eafc3672ea959d26d6424016c7d15b5504038b7dce988e body_fp=a29ce56845fc536da2135e02e8b677450eb9bdb09c17ff7dd4895489a992b5f1 source_ref=cf7d43d9e6d5cb175d70666333156560a4f18df2 -->
## `test_cli_sync_when_contended_exits_two_with_explanation(tmp_path: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie sync` exits 2 with an explanatory message when another process holds the lock, without writing a queued sentinel.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_refresh_lock:test_cli_plan_when_contended_exits_two fingerprint=defbb4e21f11935fcee5881c43a0feb5e59cb265a6eff5b815a8ec0ffdc8dabd body_fp=a9a5c776b1dd4e6f508bef1ee6bb9bb09e8bac0e2cd715331bf6623e9037853d source_ref=cf7d43d9e6d5cb175d70666333156560a4f18df2 -->
## `test_cli_plan_when_contended_exits_two(tmp_path: Path, monkeypatch: pytest.MonkeyPatch)`

Assert `trie plan` exits 2 with an "another trie process" message when the lock is held.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_refresh_lock:test_cli_lock_check_when_free_exits_zero fingerprint=6c3e8123f52edb3e23a6c52e14af4b0a5eed829066380d068e64631ecbbd7022 body_fp=809b114df79a5429e923cb695ebf2e5106b6d12d9474bb4e63d05bfc4f668f67 source_ref=6a2dd0b0651c404f7e9c65e0a9a9b6c9cd9dd72c -->
## `test_cli_lock_check_when_free_exits_zero(tmp_path: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie lock-check` exits 0 and prints "free" when no process holds the lock.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_refresh_lock:test_cli_lock_check_when_no_trie_toml_exits_zero fingerprint=6bed6cededf4924a0d32f1e0a8b7e5cfb94090daf833346c269f4353281f06f4 body_fp=cd3a8b695bd0659010eeb4574ce5a5716b901bcdfd44d2945db03fb713c44781 source_ref=6a2dd0b0651c404f7e9c65e0a9a9b6c9cd9dd72c -->
## `test_cli_lock_check_when_no_trie_toml_exits_zero(tmp_path: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie lock-check` exits 0 with a "no trie.toml" message when no trie project is configured.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_refresh_lock:test_cli_lock_check_when_contended_exits_two fingerprint=5c325164beec1dde3174f126d7cbbae3f429d6fc4cf67780c3d80a8ee7996f1c body_fp=7224995907de4b88b37d24a4d3aa7023834d6407c7a31cbdbfe9a9c54591c2ae source_ref=6a2dd0b0651c404f7e9c65e0a9a9b6c9cd9dd72c -->
## `test_cli_lock_check_when_contended_exits_two(tmp_path: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie lock-check` exits 2 with an explanatory message when another process holds the lock.
<!-- trie:end -->