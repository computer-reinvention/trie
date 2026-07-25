---
trie_version: 0.1.9
source: tests/test_parallel_sync.py
file_fingerprint: 201fd60491690c10f5f92e56a3d086dd7f51507404c0323d326e8e5232d5f6ca
last_synced_at: '2026-07-25T01:56:27Z'
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
<!-- trie:section symbol=tests/test_parallel_sync:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=e38b261094711f8ce81a379aa047d737fccf2e4b2e854e74e05149565c16fedd source_ref=a9dcb8151c96c9b3d8edbe90dc0b33084d2ada58 role=test-infrastructure -->
Tests that parallel symbol generation produces byte-identical output to serial runs and actually uses thread pool concurrency.

- Contains deterministic mock LLM client that tracks peak concurrent requests
- Verifies triefact files are identical between serial (concurrency=1) and parallel (concurrency=8) runs
- Ensures parallel execution actually fans out to multiple threads simultaneously
- Validates token counts and symbol statistics remain consistent regardless of completion order
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parallel_sync:FIXTURE_DIR fingerprint=2635a439793a81128764c32977c9356050865c2ac61f8264769219675508cca2 body_fp=feaac6f299c5fe0e6bb962a57984d858aa343c4dbd340cd95a14fa10ca3979cc source_ref=a9dcb8151c96c9b3d8edbe90dc0b33084d2ada58 role=test-infrastructure -->
Path to the tiny_repo test fixture directory used by parallel sync tests.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parallel_sync:_DeterministicClient fingerprint=19ce26c9c7deb8a374b689ef93279bb9d335697de771a0d050daeae12dd1ee29 body_fp=2a30f727f79919bef66d02bce90f457343adea28d8d86242d4f613b226f5f380 source_ref=a9dcb8151c96c9b3d8edbe90dc0b33084d2ada58 role=test -->
Simulates an LLM client that returns deterministic prose keyed by symbol name and tracks concurrency metrics.

- `peak_in_flight`: maximum number of concurrent `run()` calls observed
- `delay_seconds`: artificial delay to simulate LLM latency for testing
- `run()`: extracts symbol qname from prompt and returns fixed documentation body
- `count_tokens()`: returns constant token count for testing
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parallel_sync:_DeterministicClient.run fingerprint=a3c8ee445cc41eefc0b4c1cc2280efc949ac507e6b09c3f5f5fe1c645af8d0c1 body_fp=605c33ab5818d068b8115366ce2aa91b2c9c3acf3944103167c6c62a33bc976f source_ref=a9dcb8151c96c9b3d8edbe90dc0b33084d2ada58 role=test -->
Simulates LLM calls by returning deterministic prose keyed on symbol qname from user prompt.

- Tracks concurrent calls via `in_flight` and `peak_in_flight` counters
- Optionally sleeps for `delay_seconds` to simulate processing time
- Extracts qname from user prompt between "symbol `" markers
- Returns fixed token usage counts for testing
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parallel_sync:_DeterministicClient.count_tokens fingerprint=d2e54258807160cae2cd3e384f807ff7ab8c686f8c79830c0798dd9ba6b1e027 body_fp=2f311117c495febd2ea8f7be9b77105b27057cf7398b727f47aa05494648f18f source_ref=a9dcb8151c96c9b3d8edbe90dc0b33084d2ada58 role=test-infrastructure -->
_DeterministicClient.count_tokens returns a fixed token count of 100 for any prompt.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parallel_sync:_make_project fingerprint=1ddb32adbfee64db0a81e3f5a1f10f55bb31f4d36fe46c950206627ab40c5ebd body_fp=04d663444db883438e9692d10b332fd60835ddca6f23f81b35e39278314ec084 source_ref=a9dcb8151c96c9b3d8edbe90dc0b33084d2ada58 role=test-infrastructure -->
Creates a test project directory by copying the tiny_repo fixture and generating a trie.toml config file.

- `concurrency`: Sets the sync concurrency level in the generated config
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parallel_sync:serial_project fingerprint=73535c5a8b10ab4cbd679a6ce35def2889d342e0d1ceb9995f80c9edace7eef9 body_fp=ff2cf0180d3a37205cf2b0bce470f1c02a9b2fc9dd4a5e50c6c8d98ee3597edf source_ref=a9dcb8151c96c9b3d8edbe90dc0b33084d2ada58 role=test-infrastructure -->
Creates a test project with concurrency=1 for serial execution testing.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parallel_sync:parallel_project fingerprint=65df3c2d8681b15bae08068dfffe6a69b3efb46957ac52a503fe1743df043ecd body_fp=662b043918a871427341970d3e68c150cbc5d94aa804b39719537a584d73dc71 source_ref=a9dcb8151c96c9b3d8edbe90dc0b33084d2ada58 role=test-infrastructure -->
Creates a test project directory with concurrency=8 configuration for parallel sync testing.

- Calls `_make_project` with concurrency set to 8 to enable parallel execution
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parallel_sync:test_parallel_output_byte_identical_to_serial fingerprint=2a2638fbbb83fd6b648c58c3e42250559cb63103c0724259196e13b7c9c1201b body_fp=c50541f9469811a0cfd28c0139b3bbc6695a0e54d1c70d4e88fdf77bd8e89b96 source_ref=a9dcb8151c96c9b3d8edbe90dc0b33084d2ada58 role=test-infrastructure -->
Verifies that serial and parallel sync runs produce byte-identical triefact output for the same inputs.

- Uses deterministic client to ensure output depends only on inputs, not completion order
- Compares generated triefact files byte-for-byte between concurrency=1 and concurrency=8 runs
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parallel_sync:test_parallel_actually_fans_out fingerprint=03b67607f546b5ebfb4044ee129b7a990b433b5b9f4e69dbf65d2421839678ac body_fp=e516192cd5a965c58031145c5ec88ecc221a8613bff56457246e2f9959fe7b0a source_ref=a9dcb8151c96c9b3d8edbe90dc0b33084d2ada58 role=test-infrastructure -->
Verifies that parallel sync actually uses multiple concurrent workers by checking peak in-flight count exceeds 1.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parallel_sync:test_serial_never_fans_out fingerprint=7374f90491595edce080218008f01b129f54d61021b0019fe89d55a4027c35f6 body_fp=61d5d64ed2228d2626cd35d2354e7c0917e8e0e39a71685f6358d8894463a409 source_ref=a9dcb8151c96c9b3d8edbe90dc0b33084d2ada58 role=test-infrastructure -->
Verifies that concurrency=1 configuration serializes processing with maximum one worker in flight.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parallel_sync:test_totals_match_between_serial_and_parallel fingerprint=6fb4417701ea003521251eebfc8cbe4ae17ed70f43de15de8e0a6fd63e74ed3c body_fp=b48dac2445af509b82dd179074e32ca3354fdaca425fc2eda5609891a6312263 source_ref=a9dcb8151c96c9b3d8edbe90dc0b33084d2ada58 role=test-infrastructure -->
Verifies that serial and parallel sync produce identical token counts and symbol statistics.

- Runs sync on the same file with both concurrency=1 and concurrency=8 configs
- Asserts all result metrics match between serial and parallel execution
<!-- trie:end -->