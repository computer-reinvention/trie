---
trie_version: 0.1.1
source: tests/test_parallel_sync.py
file_fingerprint: 980b842b9b3a0aea541dcb53329d44f98c454644e3decce780b5d5f9e3ee0be6
last_synced_at: '2026-05-19T10:38:38Z'
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
<!-- trie:section symbol=tests/test_parallel_sync:_DeterministicClient fingerprint=c791affbf3ed0ce3504e97f46d4fa1bd050b64d8a9becb9284827892c0773986 body_fp=1bf54d5f598be29bcec6e3d579d92b12f74ca664b1fc13389f5cd551e441a80b source_ref=3993c78c6e7b7c371ac27bcf3850721a81dda112 -->
## `_DeterministicClient`

Fake LLM client returning deterministic prose keyed on symbol qname; tracks peak concurrent `generate` calls.

- `model_id`: identifies the fake model, unused by real infra.
- `peak_in_flight`: records maximum simultaneous `generate` calls observed across threads.
- `delay_seconds`: artificial sleep to force worker overlap in concurrency tests.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_parallel_sync:_DeterministicClient.generate fingerprint=a2416d7c378769a6decb13b3c0576208f23498ae961dfd5a735802daadac5f4a body_fp=4cc992fcba413f036f096b284bb0645cd0f01e59d3eeb6464b96b54c218334c3 source_ref=3993c78c6e7b7c371ac27bcf3850721a81dda112 -->
## `generate(self, req: GenerationRequest) -> GenerationResponse`

Return a deterministic `GenerationResponse` keyed on the symbol qname extracted from the request, tracking peak concurrency during execution.

- `delay_seconds`: holds the thread slot to force worker overlap when nonzero.
- `peak_in_flight`: updated atomically; reflects maximum concurrent callers seen.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_parallel_sync:_DeterministicClient.count_tokens fingerprint=d2e54258807160cae2cd3e384f807ff7ab8c686f8c79830c0798dd9ba6b1e027 body_fp=9d067b772e73f67b1bb1b8cb6fc3a256c95035c670c6695fa426a36018030c0b source_ref=3993c78c6e7b7c371ac27bcf3850721a81dda112 -->
## `count_tokens(_req: GenerationRequest) -> int`

Return a fixed token count of 100 for any request.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_parallel_sync:_make_project fingerprint=1ddb32adbfee64db0a81e3f5a1f10f55bb31f4d36fe46c950206627ab40c5ebd body_fp=f75aad38a896fab602b188e12673dd135a9ca4ef8826e44362c7fdae8337b146 source_ref=3993c78c6e7b7c371ac27bcf3850721a81dda112 -->
## `_make_project(tmp_path: Path, *, concurrency: int) -> Path`

Copy the fixture repo into `tmp_path` and write a `trie.toml` with the given concurrency setting.

- `concurrency`: written verbatim into `[sync] concurrency = …`
<!-- trie:end -->

<!-- trie:section symbol=tests/test_parallel_sync:serial_project fingerprint=73535c5a8b10ab4cbd679a6ce35def2889d342e0d1ceb9995f80c9edace7eef9 body_fp=4d790626cf946e60bca27f6f0d646bf920d1eb2f776942760dbef56731d490e9 source_ref=3993c78c6e7b7c371ac27bcf3850721a81dda112 -->
## `serial_project(tmp_path: Path) -> Path`

Pytest fixture providing a project copy configured with `concurrency=1`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_parallel_sync:parallel_project fingerprint=65df3c2d8681b15bae08068dfffe6a69b3efb46957ac52a503fe1743df043ecd body_fp=b8f31977f6599356f4e373b0a3aa28e416de783128b557e5628d9a879e122d81 source_ref=3993c78c6e7b7c371ac27bcf3850721a81dda112 -->
## `parallel_project(tmp_path: Path) -> Path`

Pytest fixture that creates a temporary project directory with `concurrency=8`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_parallel_sync:test_parallel_output_byte_identical_to_serial fingerprint=2a2638fbbb83fd6b648c58c3e42250559cb63103c0724259196e13b7c9c1201b body_fp=5e6a65a4166fdc4edfe2110f4152a957f81701a63e16cdb68f1169767b26fc02 source_ref=3993c78c6e7b7c371ac27bcf3850721a81dda112 -->
## `test_parallel_output_byte_identical_to_serial(serial_project: Path, parallel_project: Path) -> None`

Assert that `sync_single_file` with `concurrency=1` and `concurrency=8` produce byte-identical triefact output for the same deterministic client.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_parallel_sync:test_parallel_actually_fans_out fingerprint=03b67607f546b5ebfb4044ee129b7a990b433b5b9f4e69dbf65d2421839678ac body_fp=e0aefa8ebafa76023d724d9e30e40cc6e2363558c04fc16fcece7e5ace363375 source_ref=3993c78c6e7b7c371ac27bcf3850721a81dda112 -->
## `test_parallel_actually_fans_out(parallel_project: Path) -> None`

Assert that `concurrency=8` causes multiple `generate()` calls to overlap simultaneously.

- `peak_in_flight > 1` proves the thread pool was not silently serialised.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_parallel_sync:test_serial_never_fans_out fingerprint=7374f90491595edce080218008f01b129f54d61021b0019fe89d55a4027c35f6 body_fp=6bec1933cbb62bc1276fa713774aa0dd4d70eac802374a065b14ed84eac496c8 source_ref=3993c78c6e7b7c371ac27bcf3850721a81dda112 -->
## `test_serial_never_fans_out(serial_project: Path) -> None`

Assert that `concurrency=1` never exceeds a peak in-flight count of 1, regardless of per-call delay.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_parallel_sync:test_totals_match_between_serial_and_parallel fingerprint=6fb4417701ea003521251eebfc8cbe4ae17ed70f43de15de8e0a6fd63e74ed3c body_fp=a173e16c4c304026c7fdf9fa39cda4ffb4280887cd9a4ab102a898884e16d492 source_ref=3993c78c6e7b7c371ac27bcf3850721a81dda112 -->
## `test_totals_match_between_serial_and_parallel(serial_project: Path, parallel_project: Path) -> None`

Assert that token counts and symbol counts from `sync_single_file` are identical regardless of concurrency setting.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_parallel_sync:FIXTURE_DIR fingerprint=2635a439793a81128764c32977c9356050865c2ac61f8264769219675508cca2 body_fp=d2aa30cdb1a93d189630fadf958e6547c99213aad8557458c9d988042e5f9aa2 source_ref=075099ac3dcebfe91dd9a31be55fe436db16c124 -->
## `FIXTURE_DIR`

Path to the `tests/fixtures/tiny_repo` directory used as the source tree for all test projects.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_parallel_sync:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=1d892ceca84d82b7818ac9df043b5841e40b18cd8f1a32d593cf067df38f5d2a source_ref=075099ac3dcebfe91dd9a31be55fe436db16c124 -->
## `tests/test_parallel_sync`

Pin the contract that `sync_single_file`'s parallel generate phase produces byte-identical output to a serial run.

- `_DeterministicClient`: fake LLM returning stable prose keyed on symbol qname; tracks peak concurrency.
- `serial_project` / `parallel_project`: fixtures with concurrency=1 and concurrency=8 respectively.
- Tests assert output identity, real fan-out under concurrency=8, no fan-out under concurrency=1, and equal token/symbol totals.
<!-- trie:end -->