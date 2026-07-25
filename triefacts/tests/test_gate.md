---
trie_version: 0.1.9
source: tests/test_gate.py
file_fingerprint: 10d498bb0e1d461cf1150e7e9cb52ae8ef943605adfa989c1e2727bd3baba4aa
last_synced_at: '2026-07-25T11:18:23Z'
description: "Spec for `trie gate` \u2014 the commit guard as one command."
defines:
- kind: module
  qualified_name: tests/test_gate:__module__
  lines: 1-137
- kind: constant
  qualified_name: tests/test_gate:runner
  lines: 16-16
- kind: function
  qualified_name: tests/test_gate:_repo
  lines: 19-24
- kind: function
  qualified_name: tests/test_gate:test_gate_noop_without_config
  lines: 27-31
- kind: function
  qualified_name: tests/test_gate:_synced_repo
  lines: 34-55
- kind: function
  qualified_name: tests/test_gate:test_gate_blocks_unsynced_source
  lines: 58-65
- kind: function
  qualified_name: tests/test_gate:test_gate_passes_clean_then_blocks_unexplained_change
  lines: 68-113
- kind: function
  qualified_name: tests/test_gate:test_gate_exits_2_when_writer_holds_the_lock
  lines: 116-136
incoming_refs: 0
outgoing_refs: 4
---
<!-- trie:section symbol=tests/test_gate:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=344269b0874680fdcac103211c4b3981e2baaa650449fa871f98ed18e4b47d17 source_ref=1dd00ca9aebbf98ecbad24aef4365f2e5a630bc0 role=test -->
Integration tests for the `trie gate` commit-guard command, covering no-op, verify failure, intent-gate blocking, lock contention, and clean-pass scenarios.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_gate:runner fingerprint=b42b7c759c50309961428cbfb9fa84326b53fd54aab43e858839f19911d931ec body_fp=039282146efad9803cc54bee94d7fab783b438c3198cdd7c41fdd2ed97286382 source_ref=1dd00ca9aebbf98ecbad24aef4365f2e5a630bc0 role=test -->
Module-level `CliRunner` instance used by all test functions to invoke the `app` CLI without spawning a subprocess.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_gate:_repo fingerprint=5276f4900d5c2205fab1ec43a8d18a48b9498bfedca66d95c0443ad8815c00bc body_fp=b05ee1ffde976952a0072d0df06099758668b44ef019edb32582d5d55642fda6 source_ref=1dd00ca9aebbf98ecbad24aef4365f2e5a630bc0 role=test -->
Initialise a bare git repo in `tmp_path` with minimal config and a `trie.toml`, then return `tmp_path`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_gate:test_gate_noop_without_config fingerprint=b1cc78532a671f02d7e36a27ec8d58b3069083d9ef2ebcf20ad68c21d1a31d6f body_fp=ed6c4e629322a53ab6f71c090c913a720e7b2100318d7f90b47f4f4b71ff8f83 source_ref=1dd00ca9aebbf98ecbad24aef4365f2e5a630bc0 role=test -->
Assert `trie gate` exits 0 and reports "nothing to gate" when no `trie.toml` config exists.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_gate:_synced_repo fingerprint=6874e27878ea10b8fef55809972e1e8b76c9c4501654acd384a9ed639e10b86b body_fp=1d254da0569943fee1bda5b05ea39b91a39a1fb1205ca003a2bcd7d4b8e7121a source_ref=1dd00ca9aebbf98ecbad24aef4365f2e5a630bc0 role=test -->
Create a temporary git repo containing one committed Python module (`m.py`) and a coherent, fingerprint-matched triefact for its sole symbol `f`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_gate:test_gate_blocks_unsynced_source fingerprint=f0e4fd2bea3be06b25e4fea12cb4c21af68568f283b8afcdd7f01ffca300a165 body_fp=549a131fbf58615aae54d71f78601432e6e2e2617498c98b9070f0619c56dbfd source_ref=1dd00ca9aebbf98ecbad24aef4365f2e5a630bc0 role=test -->
Assert that `trie gate --no-digest` exits 1 and prints `trie sync` when a source file has no corresponding triefact.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_gate:test_gate_passes_clean_then_blocks_unexplained_change fingerprint=8b25bbe19476772c302b456b16751059103e37344446943b9efa8dc37d30dea4 body_fp=fa401431939ebd642ef97a408373bd463928b27d2b8ca4b041a8cbc2fdfb1e6c source_ref=1dd00ca9aebbf98ecbad24aef4365f2e5a630bc0 role=test -->
Verify that `gate` passes on a clean synced repo, blocks after an unexplained source change, then passes again once a patch note is recorded.

- Mutates `m.py` and updates the triefact fingerprint to isolate the intent gate from the verify gate.
- Falls back to a full `scan_project` if `patch create` fails due to a missing graph entry.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_gate:test_gate_exits_2_when_writer_holds_the_lock fingerprint=4f0dac5754fc546d8e694a544cf190ad13088de5c7fa5bec1542529c60de7dc7 body_fp=756e92096495b25a57214e2d54c4383930182864ed9969f434c6a3286a562cdc source_ref=1dd00ca9aebbf98ecbad24aef4365f2e5a630bc0 role=test -->
Assert `trie gate` exits with code 2 and emits a retry message when `refresh_lock.try_acquire` yields an unacquired lock.
<!-- trie:end -->