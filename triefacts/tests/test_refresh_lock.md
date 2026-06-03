---
trie_version: 0.1.5
source: tests/test_refresh_lock.py
file_fingerprint: f37035603e7cde190a1a87d214327d25c837bec535ba99a295b010093dd1e3f0
last_synced_at: '2026-06-03T21:00:00Z'
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
<!-- trie:section symbol=tests/test_refresh_lock:__module__ fingerprint=e898e798072bf5c540959d26eaadc8cccfdbc85d6e9a0dcc06ceaa5812d960e9 body_fp=7cfb574da64cd1185c8037bdb6bf6a7055036c90da0fcac4d18d03fe3f597786 source_ref=a247889420e6c77627c6b64724dd207c13c8bf27 -->
Tests for refresh lock serialization and queueing mechanisms using real subprocess contention.

- Validates single-holder acquisition, contention handling, and tail pass queue consumption
- Tests crash safety where OS releases flock when process dies
- Covers CLI integration for refresh (queues), sync/plan (exit 2), and lock-check commands
- Uses subprocess workers because flock is per-process, not per-thread
- Skips entirely on Windows platforms where POSIX flock is unavailable
<!-- trie:end -->
<!-- trie:section symbol=tests/test_refresh_lock:_project fingerprint=d565ca36636bbc0160570a7007ae6fc5190e0f22ea5207096d19bbfa4b36ed93 body_fp=1fdaf1d48fa2d30724d54b8e6f2889d50247c0c51e7f40a0a48526a60e246a5c source_ref=a247889420e6c77627c6b64724dd207c13c8bf27 -->
Creates a minimal test project by adding a `.trie/` directory to the given path and returns the project root.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_refresh_lock:test_lock_path_is_under_trie_dir fingerprint=8bbda127ee1137d0a1b0329d924df2927395204fb7f2c846dcd845fdb4ac3ccc body_fp=41e2529a571bd717b0415f94dc65d456b861c48f36ab872dbf78ea4794b8e09e source_ref=a247889420e6c77627c6b64724dd207c13c8bf27 -->
Verifies that lock_path and queued_path return paths under the `.trie/` directory with correct filenames.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_refresh_lock:test_acquire_succeeds_when_uncontested fingerprint=3e09977ec2612800854e9984cd659c84e65ce56601f3f73e419772efeb2ef874 body_fp=3af0f1a3a9f486b1ab104807e99c948bd4edc0b8b26dfeb177a8dd8946a71048 source_ref=a247889420e6c77627c6b64724dd207c13c8bf27 -->
Verifies that `try_acquire` returns a holder with `acquired=True` when no other process holds the lock.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_refresh_lock:test_acquire_creates_lock_file_on_first_run fingerprint=9cb01193c3f4a28b75060da57e928faf8dc903ce9c9406ed3576fd25e9971bc2 body_fp=1174fa3606f58f81112c1d9421a22b5a7b8f6bb2abcdf020dea9fc491e322c47 source_ref=a247889420e6c77627c6b64724dd207c13c8bf27 -->
Verifies that the first `try_acquire` call creates the lock file and persists it after release.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_refresh_lock:test_acquire_creates_trie_dir_if_missing fingerprint=b638dca8339697dc04605a4af756a9cbb37a57427ce236d21135034bdd0c0626 body_fp=1e48aee6ee3e53d92f980703638553d14aad57c4189bb5f8dba901fd57b987c7 source_ref=a247889420e6c77627c6b64724dd207c13c8bf27 -->
Verifies that try_acquire creates the `.trie/` directory when it doesn't exist on a fresh project.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_refresh_lock:_hold_lock_subprocess fingerprint=04902af6144be334b75945c33218ddbfdad31447508c80fd013a40592fe20537 body_fp=c87526c8e930b7b47fd3d274a85aa06ad2bee7ca24a7d61f621470b0701bc072 source_ref=a247889420e6c77627c6b64724dd207c13c8bf27 -->
Acquires refresh lock in a child process, writes status to ready file, and waits for release signal.

- Used in multiprocessing tests to simulate lock contention across process boundaries
- Polls release file every 10ms with 5-second timeout to avoid busy-waiting
- Returns early if lock acquisition fails
<!-- trie:end -->
<!-- trie:section symbol=tests/test_refresh_lock:test_contention_yields_unacquired_holder fingerprint=8c9998c0eb408142f0a577629a82deea55a533a89ee0626c5ed1f126bd6f6c3a body_fp=1f26ec7a37ad8d1d925176dfcf478d19920e55ad28f15ea931e60f5e2d8ea1ba source_ref=a247889420e6c77627c6b64724dd207c13c8bf27 -->
Verifies that `try_acquire` returns an unacquired holder when another process holds the lock.

- Uses subprocess to simulate lock contention since flock is per-process
- Confirms second acquirer gets `acquired=False` and can mark queued
- Tests that contested holder's `consume_queued()` returns False
<!-- trie:end -->
<!-- trie:section symbol=tests/test_refresh_lock:test_consume_queued_clears_sentinel_on_holder fingerprint=f7b258443fe0b934c75164bbe0f16f8b6788adb5d9ef67efcbb8fd7a34b15da5 body_fp=057830bd951b7a0ff3b37c24560213be9128405801c7220d3738e39da312542d source_ref=a247889420e6c77627c6b64724dd207c13c8bf27 -->
Tests that RefreshLockHolder.consume_queued() returns True once and removes the sentinel file.

- Simulates external mark_queued() call by writing empty queued file
- Verifies consume_queued() returns False on subsequent calls after draining
<!-- trie:end -->
<!-- trie:section symbol=tests/test_refresh_lock:test_mark_queued_is_idempotent fingerprint=15381b0b69d987291e037a6120094d62d7e53ea5f79bd9cec54a7037b4714a0f body_fp=ff0bf6e5d5166abb4ca5b6bf1c1eda9bf1f54a3a8838e0967056e2ba45d6679d source_ref=a247889420e6c77627c6b64724dd207c13c8bf27 -->
Verifies that calling `mark_queued()` multiple times on an unacquired holder creates only one queued sentinel file.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_refresh_lock:_hold_and_crash fingerprint=0b7790c815659d7ffaaa415e127632c29b4de497a4da227b88f503be51c0bd9a body_fp=e9ebedbd56d1314cfd8a933595e49a1f5e9b95458aa5a8b32fdb2860d4731d38 source_ref=a247889420e6c77627c6b64724dd207c13c8bf27 -->
Acquires the refresh lock, signals readiness to parent process, then exits without cleanup to test crash recovery.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_refresh_lock:test_lock_released_when_holder_crashes fingerprint=e146cba42b6a03c824c609b2039cb6f8183d8ddc97aafed57587a0bd6c9c94ec body_fp=55394c43d079f2be61a82704ae1317474a130d3ebbdc43e7de2530dd8148c2af source_ref=a247889420e6c77627c6b64724dd207c13c8bf27 -->
Verifies that when a lock holder process crashes without cleanup, the OS releases the flock and subsequent processes can acquire the lock normally.

- Uses `_hold_and_crash` subprocess that calls `os._exit()` to skip context manager cleanup
- Confirms the crashed process had acquired the lock before dying
- Tests that a new `try_acquire()` call succeeds after the crash
<!-- trie:end -->
<!-- trie:section symbol=tests/test_refresh_lock:test_cli_refresh_when_contended_queues_and_exits_zero fingerprint=f6d69648eb1e68bd974e36df7869e38c8cc20bef67544657499bf1b17db256d1 body_fp=bbd530795ed5235f4041a202a5e091e2676d7f6b3832fd64ae35d79b833ced9d source_ref=a247889420e6c77627c6b64724dd207c13c8bf27 -->
Verifies `trie refresh` CLI queues when contended and exits zero instead of blocking.

- Sets up minimal trie project with git repository to pass freshness gate
- Spawns child process holding refresh lock to simulate contention
- Invokes `trie refresh` CLI which should detect lock contention
- Asserts exit code 0 and "queued" message in output
- Confirms queued sentinel file exists for lock holder to consume
<!-- trie:end -->
<!-- trie:section symbol=tests/test_refresh_lock:_make_minimal_trie_project fingerprint=d26724620fc7e0de633567db6872771e9e400e24a9ff452df9c5f9a221f09e06 body_fp=21964a348ad318141fcd855673798456555ff9e9bda52be2d25e2af31502bce3 source_ref=a247889420e6c77627c6b64724dd207c13c8bf27 -->
Creates a minimal trie project with configuration file, source tree, and git repository for testing.

- Sets up `trie.toml` with default configuration including scope and model settings
- Creates `src/alpha.py` with a simple function definition
- Initializes git repo with user config and commits the initial files
<!-- trie:end -->
<!-- trie:section symbol=tests/test_refresh_lock:test_cli_sync_when_contended_exits_two_with_explanation fingerprint=3a772bb425b6060844eafc3672ea959d26d6424016c7d15b5504038b7dce988e body_fp=162ffbee2335042e0eb6b9f28244dee990ffa7e20e1af8d5d6922c5a3c937903 source_ref=a247889420e6c77627c6b64724dd207c13c8bf27 -->
Verifies that `trie sync` exits with code 2 and prints an explanatory message when another process holds the refresh lock.

- Uses subprocess to simulate lock contention during CLI invocation
- Confirms sync exits 2 (transient error) rather than queueing like refresh command
- Validates no queued sentinel is created since sync fails explicitly rather than deferring
<!-- trie:end -->
<!-- trie:section symbol=tests/test_refresh_lock:test_cli_lock_check_when_free_exits_zero fingerprint=6c3e8123f52edb3e23a6c52e14af4b0a5eed829066380d068e64631ecbbd7022 body_fp=b455f8b21c29527786a5dde00ec51ebd747b0c2ba756da7016e18566552736d4 source_ref=a247889420e6c77627c6b64724dd207c13c8bf27 -->
Tests that `trie lock-check` exits 0 with "free" message when no process holds the refresh lock.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_refresh_lock:test_cli_lock_check_when_no_trie_toml_exits_zero fingerprint=6bed6cededf4924a0d32f1e0a8b7e5cfb94090daf833346c269f4353281f06f4 body_fp=4d4eff02880d15a7e36f35d5a9d4f94807ee62a64350beb92dfe404da7b696d2 source_ref=a247889420e6c77627c6b64724dd207c13c8bf27 -->
Verifies `trie lock-check` exits 0 with no-op message when no trie.toml exists.

- Tests graceful degradation for pre-commit hooks in unconfigured repositories
- Ensures lock-check doesn't error on missing configuration
<!-- trie:end -->
<!-- trie:section symbol=tests/test_refresh_lock:test_cli_lock_check_when_contended_exits_two fingerprint=5c325164beec1dde3174f126d7cbbae3f429d6fc4cf67780c3d80a8ee7996f1c body_fp=c7f9e57b31f8dbd729d6da573a288bc714a5f5b66c5bb5602e1b02b78880b4d1 source_ref=a247889420e6c77627c6b64724dd207c13c8bf27 -->
Tests that `trie lock-check` exits 2 when another process holds the refresh lock.

- Creates subprocess holding lock via `_hold_lock_subprocess` helper
- Invokes `trie lock-check` CLI command while lock is contested
- Verifies exit code 2 and error message mentioning "another trie process"
<!-- trie:end -->
<!-- trie:section symbol=tests/test_refresh_lock:test_cli_plan_when_contended_exits_two fingerprint=defbb4e21f11935fcee5881c43a0feb5e59cb265a6eff5b815a8ec0ffdc8dabd body_fp=39822fc25f743bc752d00d701450fa5b7eba4c5c710df57eb5c3d34b7ae8b52e source_ref=a247889420e6c77627c6b64724dd207c13c8bf27 -->
Tests that `trie plan` exits with code 2 when another process holds the lock.

- Creates a child process that holds the lock via `_hold_lock_subprocess`
- Verifies the contended `trie plan` command exits with status code 2
- Confirms the error message mentions "another trie process"
- Uses multiprocessing because flock is per-process, not per-thread
<!-- trie:end -->