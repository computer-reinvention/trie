---
trie_version: 0.1.2
source: tests/test_parallel_sync.py
file_fingerprint: cad16241f23173bb51f0d895bfa0b376f57b34e2e3d44b9b7f5bc8d0b3a81a86
last_synced_at: '2026-05-23T23:52:23Z'
description: 'Parallel per-symbol sync: the threaded generate phase must produce output'
defines:
- kind: module
  qualified_name: tests/test_parallel_sync:__module__
  lines: 1-182
- kind: constant
  qualified_name: tests/test_parallel_sync:FIXTURE_DIR
  lines: 25-25
- kind: class
  qualified_name: tests/test_parallel_sync:_DeterministicClient
  lines: 29-67
- kind: method
  qualified_name: tests/test_parallel_sync:_DeterministicClient.generate
  lines: 41-64
- kind: method
  qualified_name: tests/test_parallel_sync:_DeterministicClient.count_tokens
  lines: 66-67
- kind: function
  qualified_name: tests/test_parallel_sync:_make_project
  lines: 70-82
- kind: function
  qualified_name: tests/test_parallel_sync:serial_project
  lines: 86-87
- kind: function
  qualified_name: tests/test_parallel_sync:parallel_project
  lines: 91-92
- kind: function
  qualified_name: tests/test_parallel_sync:test_parallel_output_byte_identical_to_serial
  lines: 95-118
- kind: function
  qualified_name: tests/test_parallel_sync:test_parallel_actually_fans_out
  lines: 121-138
- kind: function
  qualified_name: tests/test_parallel_sync:test_serial_never_fans_out
  lines: 141-154
- kind: function
  qualified_name: tests/test_parallel_sync:test_totals_match_between_serial_and_parallel
  lines: 157-181
incoming_refs: 0
outgoing_refs: 11
---
<!-- trie:section symbol=tests/test_parallel_sync:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=47c1317aa449e0ea5053f6be7bae755d29e1a3c068a45e031d976b2755836322 source_ref=a82385f7947314cf1ddd1a52434fd73a6744672f -->
## `tests/test_parallel_sync`

Verify that the threaded generate phase in `sync_single_file` produces byte-identical output to a serial run and genuinely fans out workers.

- `_DeterministicClient`: fake LLM returning stable text keyed on symbol qname; tracks peak concurrency
- `serial_project` / `parallel_project`: fixtures cloning `tiny_repo` with `concurrency=1` and `concurrency=8` respectively
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parallel_sync:FIXTURE_DIR fingerprint=2635a439793a81128764c32977c9356050865c2ac61f8264769219675508cca2 body_fp=a09ba5bde7a77a550b5cc980be982c2dd142b1678720536f3b34377d5a52ea16 source_ref=a82385f7947314cf1ddd1a52434fd73a6744672f -->
## `FIXTURE_DIR = Path(__file__).parent / "fixtures" / "tiny_repo"`

Absolute path to the `tiny_repo` fixture directory used as the source tree for test projects.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parallel_sync:_DeterministicClient fingerprint=c791affbf3ed0ce3504e97f46d4fa1bd050b64d8a9becb9284827892c0773986 body_fp=7802dfee36ec0d6f489654102b9073eb9381b81cc0e4216c3ac0525927ae350a source_ref=a82385f7947314cf1ddd1a52434fd73a6744672f -->
## `_DeterministicClient`

Fake LLM client returning deterministic prose keyed on symbol qname while tracking peak concurrent `generate()` calls.

- `peak_in_flight`: maximum simultaneous `generate()` calls observed across all threads.
- `delay_seconds`: sleep duration per call; set >0 to force worker overlap.
- `generate`: returns output stable under any completion order; updates `in_flight` under `_lock`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parallel_sync:_DeterministicClient.generate fingerprint=a2416d7c378769a6decb13b3c0576208f23498ae961dfd5a735802daadac5f4a body_fp=de2b27d71d5a17894734a6f512b1157e5a4a508d6a18765edb3646e1cd0c9103 source_ref=a82385f7947314cf1ddd1a52434fd73a6744672f -->
## `generate(self, req: GenerationRequest) -> GenerationResponse`

Produce a deterministic fake `GenerationResponse`, tracking peak concurrent in-flight calls.

- `req`: qname extracted from backtick-delimited text in `req.request` to key output.
- `peak_in_flight`: updated atomically; callers assert this to verify parallelism.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parallel_sync:_DeterministicClient.count_tokens fingerprint=d2e54258807160cae2cd3e384f807ff7ab8c686f8c79830c0798dd9ba6b1e027 body_fp=313c5c5e5e2560d9ea1820b4631083562d368cda2144ff8a31db5501daf8326c source_ref=a82385f7947314cf1ddd1a52434fd73a6744672f -->
## `count_tokens(self, _req: GenerationRequest) -> int`

Return a fixed token count of 100 for any `_DeterministicClient` request.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parallel_sync:_make_project fingerprint=1ddb32adbfee64db0a81e3f5a1f10f55bb31f4d36fe46c950206627ab40c5ebd body_fp=b3c13bde012185a32d4b0a057c9a86184adb56cd33ddc0bceebd67ff8771a085 source_ref=a82385f7947314cf1ddd1a52434fd73a6744672f -->
## `_make_project(tmp_path: Path, *, concurrency: int) -> Path`

Copy the fixture repo into `tmp_path/demo` and write a `trie.toml` with the given concurrency setting.

- `concurrency`: written verbatim into `[sync]` section of the generated config.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parallel_sync:serial_project fingerprint=73535c5a8b10ab4cbd679a6ce35def2889d342e0d1ceb9995f80c9edace7eef9 body_fp=e40fa40e1e57dad1ff0832f23daf6d4a026973dacfe68c51fe23b779fa490d4d source_ref=a82385f7947314cf1ddd1a52434fd73a6744672f -->
## `serial_project(tmp_path: Path) -> Path`

Pytest fixture providing a project directory configured with `concurrency=1`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parallel_sync:parallel_project fingerprint=65df3c2d8681b15bae08068dfffe6a69b3efb46957ac52a503fe1743df043ecd body_fp=a221d8da4776fbcb8ba33d4a17010cc58b3ad6bb730f35a3b341a0f15f0a3803 source_ref=a82385f7947314cf1ddd1a52434fd73a6744672f -->
## `parallel_project(tmp_path: Path) -> Path`

Pytest fixture providing a project copy configured with `concurrency=8`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parallel_sync:test_parallel_output_byte_identical_to_serial fingerprint=2a2638fbbb83fd6b648c58c3e42250559cb63103c0724259196e13b7c9c1201b body_fp=7490eeeb3b63b467738effb7099d5aaee356144607369017d2bd245b73953312 source_ref=a82385f7947314cf1ddd1a52434fd73a6744672f -->
## `test_parallel_output_byte_identical_to_serial(serial_project: Path, parallel_project: Path) -> None`

Assert that `sync_single_file` with `concurrency=1` and `concurrency=8` produce byte-identical triefact output for the same inputs.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parallel_sync:test_parallel_actually_fans_out fingerprint=03b67607f546b5ebfb4044ee129b7a990b433b5b9f4e69dbf65d2421839678ac body_fp=1dfa27731c316fe192f770c31c6b9196e96f5ad3075c9b873bb8b0659f7455e5 source_ref=a82385f7947314cf1ddd1a52434fd73a6744672f -->
## `test_parallel_actually_fans_out(parallel_project: Path) -> None`

Assert that `sync_single_file` with `concurrency=8` genuinely overlaps `generate()` calls rather than silently serialising them.

- `peak_in_flight > 1` required; failure means the thread pool collapsed to serial.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parallel_sync:test_serial_never_fans_out fingerprint=7374f90491595edce080218008f01b129f54d61021b0019fe89d55a4027c35f6 body_fp=775050a768f6ca9837ff10144b36e3bf7daa2c6221acb09f6aee6545c2003273 source_ref=a82385f7947314cf1ddd1a52434fd73a6744672f -->
## `test_serial_never_fans_out(serial_project: Path) -> None`

Assert that `concurrency=1` never executes more than one `generate()` call simultaneously, keeping `peak_in_flight` at exactly 1.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parallel_sync:test_totals_match_between_serial_and_parallel fingerprint=6fb4417701ea003521251eebfc8cbe4ae17ed70f43de15de8e0a6fd63e74ed3c body_fp=a173e16c4c304026c7fdf9fa39cda4ffb4280887cd9a4ab102a898884e16d492 source_ref=a82385f7947314cf1ddd1a52434fd73a6744672f -->
## `test_totals_match_between_serial_and_parallel(serial_project: Path, parallel_project: Path) -> None`

Assert that token counts and symbol counts from `sync_single_file` are identical regardless of concurrency setting.
<!-- trie:end -->