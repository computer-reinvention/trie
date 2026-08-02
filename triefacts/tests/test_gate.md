---
trie_version: 0.3.0
source: tests/test_gate.py
file_fingerprint: 3a7a12a5078ebc2b026a456d2ca997032eaacac3ec42b36b54f4250d4577d7b7
last_synced_at: '2026-08-02T21:19:27Z'
description: "Spec for `trie gate` \u2014 the commit guard as one command."
defines:
- kind: module
  qualified_name: tests/test_gate:__module__
  lines: 1-226
- kind: constant
  qualified_name: tests/test_gate:runner
  lines: 16-16
- kind: function
  qualified_name: tests/test_gate:_repo
  lines: 19-24
  signature: 'def _repo(tmp_path: Path) -> Path'
- kind: function
  qualified_name: tests/test_gate:test_gate_noop_without_config
  lines: 27-31
  signature: 'def test_gate_noop_without_config(tmp_path: Path, monkeypatch)'
- kind: function
  qualified_name: tests/test_gate:_synced_repo
  lines: 34-55
  signature: 'def _synced_repo(tmp_path: Path) -> Path'
- kind: function
  qualified_name: tests/test_gate:test_gate_blocks_unsynced_source
  lines: 58-65
  signature: 'def test_gate_blocks_unsynced_source(tmp_path: Path, monkeypatch)'
- kind: function
  qualified_name: tests/test_gate:test_gate_passes_clean_then_blocks_unexplained_change
  lines: 68-113
  signature: 'def test_gate_passes_clean_then_blocks_unexplained_change(tmp_path: Path, monkeypatch)'
- kind: function
  qualified_name: tests/test_gate:test_gate_exits_2_when_writer_holds_the_lock
  lines: 116-136
  signature: 'def test_gate_exits_2_when_writer_holds_the_lock(tmp_path: Path, monkeypatch)'
- kind: function
  qualified_name: tests/test_gate:test_gate_warns_on_self_hosting_version_skew
  lines: 139-151
  signature: 'def test_gate_warns_on_self_hosting_version_skew(tmp_path: Path, monkeypatch)'
- kind: function
  qualified_name: tests/test_gate:test_gate_no_skew_warning_for_other_projects
  lines: 154-162
  signature: 'def test_gate_no_skew_warning_for_other_projects(tmp_path: Path, monkeypatch)'
- kind: function
  qualified_name: tests/test_gate:test_patch_create_suggests_close_qnames_on_miss
  lines: 165-192
  signature: 'def test_patch_create_suggests_close_qnames_on_miss(tmp_path: Path, monkeypatch)'
- kind: function
  qualified_name: tests/test_gate:test_patch_create_batch_reports_did_you_mean
  lines: 195-225
  signature: 'def test_patch_create_batch_reports_did_you_mean(tmp_path: Path, monkeypatch)'
incoming_refs: 0
outgoing_refs: 26
---
<!-- trie:section symbol=tests/test_gate:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=344269b0874680fdcac103211c4b3981e2baaa650449fa871f98ed18e4b47d17 source_ref=1dd00ca9aebbf98ecbad24aef4365f2e5a630bc0 role=test -->
Integration tests for the `trie gate` commit-guard command, covering no-op, verify failure, intent-gate blocking, lock contention, and clean-pass scenarios.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_gate:runner fingerprint=b42b7c759c50309961428cbfb9fa84326b53fd54aab43e858839f19911d931ec body_fp=039282146efad9803cc54bee94d7fab783b438c3198cdd7c41fdd2ed97286382 source_ref=1dd00ca9aebbf98ecbad24aef4365f2e5a630bc0 role=test -->
Module-level `CliRunner` instance used by all test functions to invoke the `app` CLI without spawning a subprocess.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_gate:_repo fingerprint=5276f4900d5c2205fab1ec43a8d18a48b9498bfedca66d95c0443ad8815c00bc body_fp=1bb2892e67fbcfe6e2dabc55124d481b9191bbb0ce5e8af7454b7a8bd4d3e643 source_ref=1dd00ca9aebbf98ecbad24aef4365f2e5a630bc0 role=test -->
## `def _repo(tmp_path: Path) -> Path`

Initialise a bare git repo in `tmp_path` with minimal config and a `trie.toml`, then return `tmp_path`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_gate:test_gate_noop_without_config fingerprint=b1cc78532a671f02d7e36a27ec8d58b3069083d9ef2ebcf20ad68c21d1a31d6f body_fp=82e2b59f35eb4e59c0d62642c0b1556ca7a5be14e3c54f60c14450c08ea641f8 source_ref=1dd00ca9aebbf98ecbad24aef4365f2e5a630bc0 role=test -->
## `def test_gate_noop_without_config(tmp_path: Path, monkeypatch)`

Assert `trie gate` exits 0 and reports "nothing to gate" when no `trie.toml` config exists.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_gate:_synced_repo fingerprint=6874e27878ea10b8fef55809972e1e8b76c9c4501654acd384a9ed639e10b86b body_fp=e02cfc5a2917896ab467e5d97f102accc7883d164527df3b4a7abb3ee030f191 source_ref=7b8f2a7a07be98865520def7215e885563a70208 role=test -->
## `def _synced_repo(tmp_path: Path) -> Path`

Create a temporary git repo containing one committed Python module (`m.py`) and a coherent, fingerprint-matched triefact for its sole symbol `f`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_gate:test_gate_blocks_unsynced_source fingerprint=f0e4fd2bea3be06b25e4fea12cb4c21af68568f283b8afcdd7f01ffca300a165 body_fp=5c53543da9c01d766e8b1b3f05b85eb43ee36cdda1a5239bfe0b42a84f01354b source_ref=1dd00ca9aebbf98ecbad24aef4365f2e5a630bc0 role=test -->
## `def test_gate_blocks_unsynced_source(tmp_path: Path, monkeypatch)`

Assert that `trie gate --no-digest` exits 1 and prints `trie sync` when a source file has no corresponding triefact.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_gate:test_gate_passes_clean_then_blocks_unexplained_change fingerprint=8b25bbe19476772c302b456b16751059103e37344446943b9efa8dc37d30dea4 body_fp=0a4a68d130fe5c4cf94c3f7243dc37009e029608a3eab5cc7ff4e7880353ed83 source_ref=7b8f2a7a07be98865520def7215e885563a70208 role=test -->
## `def test_gate_passes_clean_then_blocks_unexplained_change(tmp_path: Path, monkeypatch)`

Verify that `gate` passes on a clean synced repo, blocks after an unexplained source change, then passes again once a patch note is recorded.

- Mutates `m.py` and updates the triefact fingerprint to isolate the intent gate from the verify gate.
- Falls back to a full `scan_project` if `patch create` fails due to a missing graph entry.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_gate:test_gate_exits_2_when_writer_holds_the_lock fingerprint=4f0dac5754fc546d8e694a544cf190ad13088de5c7fa5bec1542529c60de7dc7 body_fp=a905ef1dfcde289b3979bced6ddad606b74e9049b131ab74bb533c6f5c1dcd9e source_ref=1dd00ca9aebbf98ecbad24aef4365f2e5a630bc0 role=test -->
## `def test_gate_exits_2_when_writer_holds_the_lock(tmp_path: Path, monkeypatch)`

Assert `trie gate` exits with code 2 and emits a retry message when `refresh_lock.try_acquire` yields an unacquired lock.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_gate:test_gate_warns_on_self_hosting_version_skew fingerprint=1b96adae73a0b495e9fa2a9b608e594d87bb8ffb1e2a94eebce5d57d930a2dc8 body_fp=d2fd1357fc0679a2481f081463a73a546de21c22312f2884483f32de7f150140 source_ref=6b2b5f37fb6e6eff07b99ad0ef92e460be785e97 role=test -->
## `def test_gate_warns_on_self_hosting_version_skew(tmp_path: Path, monkeypatch)`

Assert that `trie gate` emits a version-skew warning with the detected version and `uv tool install --force` when the project being gated is the trie source repo itself at a mismatched version.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_gate:test_gate_no_skew_warning_for_other_projects fingerprint=4be10d29db38cafd906999f5a05b8b81f59d7a1b9d99310dfe09ca04df67aef0 body_fp=d70283be27622f70825277bbb9216837e160d9c591031d8a0bb8c7c45473cb81 source_ref=6b2b5f37fb6e6eff07b99ad0ef92e460be785e97 role=test -->
## `def test_gate_no_skew_warning_for_other_projects(tmp_path: Path, monkeypatch)`

Assert that `trie gate` emits no version-skew warning when the project's `pyproject.toml` names a package other than `trie`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_gate:test_patch_create_suggests_close_qnames_on_miss fingerprint=6f350483096d3c2405b084146756ccad717d74e4e1c049ea42046a85f9654956 body_fp=d55da5ea60be3c31c1885796f9844007df89cb847aead084b41a02b02ffaa949 source_ref=a1751f70f339ca1dd429f735fa9eef29e1b549a3 role=test -->
## `def test_patch_create_suggests_close_qnames_on_miss(tmp_path: Path, monkeypatch)`

Assert that `patch create` with an unknown qname outputs "did you mean" candidates and mentions `--gone` as a secondary hint, not the primary error.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_gate:test_patch_create_batch_reports_did_you_mean fingerprint=b5218c92c5e26c8c37c3d1028aa494697c8ff1a88b6612a08d92bcb2c76fea84 body_fp=5255b1e2c185eedadf6a123c82e7fa7ef294d7e7084db5d26a9c03020173827c source_ref=7b8f2a7a07be98865520def7215e885563a70208 role=test -->
## `def test_patch_create_batch_reports_did_you_mean(tmp_path: Path, monkeypatch)`

Verify that `patch create-batch` includes `did_you_mean` candidates in JSON result rows when a qualified name is not found in the graph.
<!-- trie:end -->