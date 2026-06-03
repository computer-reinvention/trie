---
trie_version: 0.1.5
source: tests/test_parallel_sync.py
file_fingerprint: 201fd60491690c10f5f92e56a3d086dd7f51507404c0323d326e8e5232d5f6ca
last_synced_at: '2026-06-03T20:58:27Z'
description: 'Parallel per-symbol sync: the threaded generate phase must produce output'
defines:
- kind: module
  qualified_name: tests/test_parallel_sync:__module__
  lines: 1-199
- kind: constant
  qualified_name: tests/test_parallel_sync:FIXTURE_DIR
  lines: 25-25
- kind: class
  qualified_name: tests/test_parallel_sync:_DeterministicClient
  lines: 29-84
- kind: method
  qualified_name: tests/test_parallel_sync:_DeterministicClient.run
  lines: 41-81
- kind: method
  qualified_name: tests/test_parallel_sync:_DeterministicClient.count_tokens
  lines: 83-84
- kind: function
  qualified_name: tests/test_parallel_sync:_make_project
  lines: 87-99
- kind: function
  qualified_name: tests/test_parallel_sync:serial_project
  lines: 103-104
- kind: function
  qualified_name: tests/test_parallel_sync:parallel_project
  lines: 108-109
- kind: function
  qualified_name: tests/test_parallel_sync:test_parallel_output_byte_identical_to_serial
  lines: 112-135
- kind: function
  qualified_name: tests/test_parallel_sync:test_parallel_actually_fans_out
  lines: 138-155
- kind: function
  qualified_name: tests/test_parallel_sync:test_serial_never_fans_out
  lines: 158-171
- kind: function
  qualified_name: tests/test_parallel_sync:test_totals_match_between_serial_and_parallel
  lines: 174-198
incoming_refs: 0
outgoing_refs: 12
---
<!-- trie:section symbol=tests/test_parallel_sync:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=ce60cd1ee1cb96e0caab32625cceac56bded94652b1b0e72962db53ef9153189 source_ref=a9dcb8151c96c9b3d8edbe90dc0b33084d2ada58 -->
Tests that parallel symbol generation produces byte-identical output to serial execution.

- Validates threaded generate phase maintains deterministic ordering in triefact output
- Uses `_DeterministicClient` to ensure completion order cannot affect final bytes
- Confirms parallel pool actually fans out workers versus silently serializing
- Verifies token accounting and symbol counts remain consistent across execution modes
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parallel_sync:FIXTURE_DIR fingerprint=2635a439793a81128764c32977c9356050865c2ac61f8264769219675508cca2 body_fp=2a479ce4942642a6e26afe51f89f48c7d336afa200b068b952020e92b6894419 source_ref=a9dcb8151c96c9b3d8edbe90dc0b33084d2ada58 -->
Path to test fixture directory containing a minimal Python repository for parallel sync tests.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parallel_sync:_DeterministicClient fingerprint=19ce26c9c7deb8a374b689ef93279bb9d335697de771a0d050daeae12dd1ee29 body_fp=e2ba98822c6a1044084ebf19d127adec3024dc3351ad4d5209f7b8a2d35dd7cd source_ref=a9dcb8151c96c9b3d8edbe90dc0b33084d2ada58 -->
Deterministic test client that generates identical documentation based on symbol names and tracks concurrency metrics.

- `peak_in_flight`: maximum number of concurrent calls observed during execution
- `delay_seconds`: artificial delay to simulate processing time and test parallelization
- `run()`: returns fixed documentation keyed on symbol qname extracted from user prompt
- `count_tokens()`: returns constant token count for testing
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parallel_sync:_DeterministicClient.run fingerprint=a3c8ee445cc41eefc0b4c1cc2280efc949ac507e6b09c3f5f5fe1c645af8d0c1 body_fp=f318dc0d3bea51ebcec9a16f8c7764d66ea36444a6b01337a132428cb6355d3e source_ref=a9dcb8151c96c9b3d8edbe90dc0b33084d2ada58 -->
_DeterministicClient.run returns deterministic documentation keyed on symbol qname from the user prompt.

- Tracks concurrent calls via `in_flight` and `peak_in_flight` counters under lock
- Optionally delays execution via `delay_seconds` to simulate overlapping workers
- Extracts symbol qname from user prompt after "symbol `" to generate stable body text
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parallel_sync:_DeterministicClient.count_tokens fingerprint=d2e54258807160cae2cd3e384f807ff7ab8c686f8c79830c0798dd9ba6b1e027 body_fp=eeecea7934660922ee247ca3b92913f91286e970d821fb1d84ec303e212380a6 source_ref=a9dcb8151c96c9b3d8edbe90dc0b33084d2ada58 -->
Returns a fixed count of 100 tokens for any prompt pair in _DeterministicClient.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parallel_sync:_make_project fingerprint=1ddb32adbfee64db0a81e3f5a1f10f55bb31f4d36fe46c950206627ab40c5ebd body_fp=44e5291cb03e53821fb3c2d8f155d50f388ac80b5eb22a34a7ddf8c0549a463e source_ref=a9dcb8151c96c9b3d8edbe90dc0b33084d2ada58 -->
Creates test project by copying fixture directory and configuring trie.toml with specified concurrency.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parallel_sync:serial_project fingerprint=73535c5a8b10ab4cbd679a6ce35def2889d342e0d1ceb9995f80c9edace7eef9 body_fp=680153ac630c1fbacd5af274d7269c85ec67caa3fa3b526a653c1effb69eb958 source_ref=a9dcb8151c96c9b3d8edbe90dc0b33084d2ada58 -->
Creates a test project configured with concurrency=1 for serial processing tests.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parallel_sync:parallel_project fingerprint=65df3c2d8681b15bae08068dfffe6a69b3efb46957ac52a503fe1743df043ecd body_fp=765c4251508742416a7e16d20f0e6ca682b7bd892bb69674fd058849ece9edb6 source_ref=a9dcb8151c96c9b3d8edbe90dc0b33084d2ada58 -->
Creates a test project fixture with concurrency=8 for parallel sync testing.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parallel_sync:test_parallel_output_byte_identical_to_serial fingerprint=2a2638fbbb83fd6b648c58c3e42250559cb63103c0724259196e13b7c9c1201b body_fp=dc74cff6403b81898063ee1bef92d20eb76e556696eabe47a24f3c00bf8cc226 source_ref=a9dcb8151c96c9b3d8edbe90dc0b33084d2ada58 -->
Verifies that serial and parallel sync modes produce identical triefact output for the same input file.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parallel_sync:test_parallel_actually_fans_out fingerprint=03b67607f546b5ebfb4044ee129b7a990b433b5b9f4e69dbf65d2421839678ac body_fp=9fa4f42e4fc66fe6e07bf45bf7276e86db0475fde1e57360307840e539cd0f51 source_ref=a9dcb8151c96c9b3d8edbe90dc0b33084d2ada58 -->
Verifies that parallel sync actually uses multiple workers concurrently by checking peak in-flight requests.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parallel_sync:test_serial_never_fans_out fingerprint=7374f90491595edce080218008f01b129f54d61021b0019fe89d55a4027c35f6 body_fp=20997a94108945746905ffab22df78d7c7c6789be59ed4ac5daee4470823d9a1 source_ref=a9dcb8151c96c9b3d8edbe90dc0b33084d2ada58 -->
Verifies that `sync_single_file` with concurrency=1 never runs parallel generate calls, maintaining deterministic evaluation order.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parallel_sync:test_totals_match_between_serial_and_parallel fingerprint=6fb4417701ea003521251eebfc8cbe4ae17ed70f43de15de8e0a6fd63e74ed3c body_fp=7c13fb17209fc283a1b1f32d656daed16886bedea4200027102aa5033524fb55 source_ref=a9dcb8151c96c9b3d8edbe90dc0b33084d2ada58 -->
Verifies that token accounting and symbol counts remain identical between serial and parallel sync executions.

- Compares `symbols_generated`, `sections_removed`, `input_tokens`, and `output_tokens` across both modes
- Ensures deterministic apply phase behavior regardless of generation completion order
<!-- trie:end -->