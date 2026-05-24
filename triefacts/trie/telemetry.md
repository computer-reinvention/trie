---
trie_version: 0.1.2
source: trie/telemetry.py
file_fingerprint: 139de3396f21b6ea7bf609a055d7cee08a071a4fae7439e93e65104014d2b6fe
last_synced_at: '2026-05-23T23:51:49Z'
description: Append-only JSONL telemetry for trie's own operations.
defines:
- kind: module
  qualified_name: trie/telemetry:__module__
  lines: 1-262
- kind: constant
  qualified_name: trie/telemetry:_DEFAULT_FILENAME
  lines: 50-50
- kind: constant
  qualified_name: trie/telemetry:_cfg
  lines: 53-53
- kind: constant
  qualified_name: trie/telemetry:_project_root
  lines: 54-54
- kind: constant
  qualified_name: trie/telemetry:_file
  lines: 55-55
- kind: constant
  qualified_name: trie/telemetry:_resolved
  lines: 56-56
- kind: constant
  qualified_name: trie/telemetry:_enabled
  lines: 57-57
- kind: constant
  qualified_name: trie/telemetry:_log_to_stderr
  lines: 58-58
- kind: constant
  qualified_name: trie/telemetry:_capture_args
  lines: 59-59
- kind: constant
  qualified_name: trie/telemetry:_capture_responses
  lines: 60-60
- kind: constant
  qualified_name: trie/telemetry:_redact_keys
  lines: 61-61
- kind: function
  qualified_name: trie/telemetry:configure
  lines: 64-75
- kind: function
  qualified_name: trie/telemetry:_resolve
  lines: 78-137
- kind: function
  qualified_name: trie/telemetry:_open
  lines: 140-149
- kind: function
  qualified_name: trie/telemetry:_close
  lines: 152-160
- kind: function
  qualified_name: trie/telemetry:is_enabled
  lines: 163-166
- kind: function
  qualified_name: trie/telemetry:capture_args
  lines: 169-172
- kind: function
  qualified_name: trie/telemetry:capture_responses
  lines: 175-178
- kind: function
  qualified_name: trie/telemetry:_apply_redactions
  lines: 181-195
- kind: function
  qualified_name: trie/telemetry:emit
  lines: 198-220
- kind: function
  qualified_name: trie/telemetry:timed
  lines: 224-250
- kind: function
  qualified_name: trie/telemetry:reset_for_tests
  lines: 253-261
incoming_refs: 46
outgoing_refs: 0
---
<!-- trie:section symbol=trie/telemetry:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=25568a31db0e83797b30d5d5ee39eba3b1d635213621cf05cd6e01696148cd26 source_ref=cf002b82dfc49d9b31513e0a29c2f60d2fe0c63d -->
## `telemetry`

Provide append-only JSONL telemetry for trie's internal operations, controlled via `TRIE_DEBUG` env var or `[debug]` config block.

- `emit(event, **fields)`: writes one timestamped event; silent when disabled
- `timed(event, **fields)`: context manager; auto-captures `duration_ms` and `error`
- `configure(cfg, project_root)`: applies `trie.toml` settings process-wide
- `is_enabled()`, `capture_args()`, `capture_responses()`: cheap state queries
- Log file opened lazily on first emit; flushed on `atexit`; never raises into caller
<!-- trie:end -->
<!-- trie:section symbol=trie/telemetry:_DEFAULT_FILENAME fingerprint=9a55f4f84be667ae97ac1a341d080e215f879fba1717c412b86e8be00d921548 body_fp=d404dbaf02e3cf3e07c279865b1afffd9d1d7e019497106816a14c5c231722c3 source_ref=cf002b82dfc49d9b31513e0a29c2f60d2fe0c63d -->
## `_DEFAULT_FILENAME = "debug.jsonl"`

Default log filename used when no explicit path is configured.
<!-- trie:end -->
<!-- trie:section symbol=trie/telemetry:_cfg fingerprint=f803a03ddbedf169fed3b561490db8ebf2c25cb36f6f6925e575472fd5a4e569 body_fp=2b065b2787795cf6f8c18ddc5bc2a47625ec420ddf59fb67afe4e7de523778a7 source_ref=cf002b82dfc49d9b31513e0a29c2f60d2fe0c63d -->
## `_cfg: Debug | None = None`

Process-wide `Debug` config; set by `configure()`, read by `_resolve()`.
<!-- trie:end -->
<!-- trie:section symbol=trie/telemetry:_project_root fingerprint=7f1404a6ae2c27aa098d65beb4a5ec00e484dda4224db1c3e0531d94f989f5e4 body_fp=49d2ec6d8d284605e2a63fe61f109b8cb4d747afa694faa93e035c262e63fc74 source_ref=cf002b82dfc49d9b31513e0a29c2f60d2fe0c63d -->
## `_project_root: Path | None = None`

Process-wide project root used to resolve relative log paths; set by `configure()`.
<!-- trie:end -->
<!-- trie:section symbol=trie/telemetry:_file fingerprint=f80c5dc793cb1be2813736697260ba3e49782620ce68eb959bb8dcc77c2b5c4c body_fp=e99bd02555049d24e33aa24da7a7a859ae115107ad9c3938f6ffd302cb043324 source_ref=cf002b82dfc49d9b31513e0a29c2f60d2fe0c63d -->
## `_file: IO[str] | None = None`

Open log file handle; `None` until the first emit triggers lazy open.
<!-- trie:end -->
<!-- trie:section symbol=trie/telemetry:_resolved fingerprint=4a21f07148902d26342f7f14c95bf97c09277efe7d1c8af024a200aa306e900b body_fp=ee5d3cf26838881c6b4cba2feb597eb6c708091a872fc17f11181a7d2c0e26b0 source_ref=cf002b82dfc49d9b31513e0a29c2f60d2fe0c63d -->
## `_resolved: bool = False`

Flag indicating whether telemetry enable/path resolution has been performed for this process; reset to `False` by `configure()` to force re-resolution.
<!-- trie:end -->
<!-- trie:section symbol=trie/telemetry:_enabled fingerprint=a4a7acc6d0e8418ce4f4bee46dc2a6528bf2533f2fb58c10da89b6e3ab11cd96 body_fp=9fd1ee9a556f99604862be64a0dc2f05bd6b28db42bacd1c0b54184108158ed8 source_ref=cf002b82dfc49d9b31513e0a29c2f60d2fe0c63d -->
## `_enabled: bool = False`

Process-wide flag indicating whether telemetry emission is currently active.
<!-- trie:end -->
<!-- trie:section symbol=trie/telemetry:_log_to_stderr fingerprint=c2a4b91a3b5aacafcf5c68ebdfca09c9c3dd10928bb36485e00a429d7c641321 body_fp=7c586b10daf0a92b5d33eb8a8547c0a9cbe91decfdc24fecf1e4fa5603c2ce32 source_ref=cf002b82dfc49d9b31513e0a29c2f60d2fe0c63d -->
## `_log_to_stderr: bool = False`

Process-wide flag controlling whether emitted events are also printed to stderr.
<!-- trie:end -->
<!-- trie:section symbol=trie/telemetry:_capture_args fingerprint=9d9dcc1072cfa01be373db7e7616a95ba37a9705f456cc7703fe9712c186b6f6 body_fp=d1196f1397901a1f01452498f4729965262ebdd7e8ffd0b58eb9e6855d9305dc source_ref=cf002b82dfc49d9b31513e0a29c2f60d2fe0c63d -->
## `_capture_args: bool = True`

Process-wide flag controlling whether MCP tool arguments are included in emitted events.
<!-- trie:end -->
<!-- trie:section symbol=trie/telemetry:_capture_responses fingerprint=18d89ca3817c4b9efae98046148b77f3d349be60bbe5bbe5af4e8e31b87208f5 body_fp=cd7674e718bbea6dc69c8f1b405d0fbc03ce55a9c412567b4458afd5aa3b895f source_ref=cf002b82dfc49d9b31513e0a29c2f60d2fe0c63d -->
## `_capture_responses: bool = False`

Process-wide flag controlling whether full MCP response bodies are captured.
<!-- trie:end -->
<!-- trie:section symbol=trie/telemetry:_redact_keys fingerprint=a71082ab8e3ad2ceea716fd06a5efffe0bfa80f926db07fb76c16be4195e8e00 body_fp=ce83bb5142fabd2a3339e43f8fb95beb80b0fca317f7f16629f2bf34fc6c0b9f source_ref=cf002b82dfc49d9b31513e0a29c2f60d2fe0c63d -->
## `_redact_keys: tuple[str, ...]`

Process-wide list of dotted-path keys whose values are replaced with `"<redacted>"` before writing.
<!-- trie:end -->
<!-- trie:section symbol=trie/telemetry:configure fingerprint=3d7526358fbe30bf4a41e3bfcc6b5c89580f453b6f8c407595d25483a1214caf body_fp=09561270b37919e9eee68a19416c521301f15967ac4941f3885df2c4ca62bcf7 source_ref=cf002b82dfc49d9b31513e0a29c2f60d2fe0c63d -->
## `configure(cfg: Debug, project_root: Path) -> None`

Apply process-wide telemetry settings from a loaded `trie.toml` `[debug]` block.

- `TRIE_DEBUG` env var still overrides enable/path after this call.
- Safe to call repeatedly; forces re-resolution on next emit.
<!-- trie:end -->
<!-- trie:section symbol=trie/telemetry:_resolve fingerprint=2b823d46e6a7cc0c7cfc52d279a833200768631f198ede261bfc2994067a27dc body_fp=d608b6531423f4e937675f6ce606a39a43caec35d8da6d2bdeb75ecec8398cbe source_ref=cf002b82dfc49d9b31513e0a29c2f60d2fe0c63d -->
## `_resolve() -> None`

Resolve process-wide telemetry enable state and log path, then open the log file; idempotent after first call.

- `TRIE_DEBUG` env var takes priority over `_cfg.enabled`; any non-boolean value is treated as a file path.
- Resets `_enabled`, `_log_to_stderr`, `_capture_args`, `_capture_responses`, `_redact_keys` globals.
- Subsequent calls are no-ops unless `configure()` cleared `_resolved`.
<!-- trie:end -->
<!-- trie:section symbol=trie/telemetry:_open fingerprint=d2382bca32b3053880c2f7e6d30f328b5cda996fc590dec5752861d2b1a3cb7d body_fp=5e8c9033a148983644f25d0841e8126bcd8d7267c0e6d84796debb7c3c0218fa source_ref=cf002b82dfc49d9b31513e0a29c2f60d2fe0c63d -->
## `_open(path: Path) -> None`

Open the telemetry log file for line-buffered append, disabling telemetry silently on `OSError`.
<!-- trie:end -->
<!-- trie:section symbol=trie/telemetry:_close fingerprint=171eb098b8d920cbcff51070df2295d2cf8c29c8e46aa8158c069b3d486e31c4 body_fp=e87bac1081e43149118b778e8d22a023e755fe941f5b936f00ed72a5ff4277ba source_ref=cf002b82dfc49d9b31513e0a29c2f60d2fe0c63d -->
## `_close() -> None`

Flush and close the open telemetry log file, suppressing `OSError`.
<!-- trie:end -->
<!-- trie:section symbol=trie/telemetry:is_enabled fingerprint=d642b8f5ca8a8a7555eb9f8c0a66632811aa43c8020ba7c0350a01ef08d96548 body_fp=5b5f73df7f296cb4864a58d336d78bb11f2154a146500c9105bc89775c4615a6 source_ref=cf002b82dfc49d9b31513e0a29c2f60d2fe0c63d -->
## `is_enabled() -> bool`

Indicates whether telemetry is enabled for the current process.
<!-- trie:end -->
<!-- trie:section symbol=trie/telemetry:capture_args fingerprint=660c1bcba0896e7c441a5403f1ad313a838a7a14dc22699b2d5c918fdd0ab6ed body_fp=4fdbb96f9818817bb15182c62a864d636c1a16ec94e44bc84a7cb8a41673e008 source_ref=cf002b82dfc49d9b31513e0a29c2f60d2fe0c63d -->
## `capture_args() -> bool`

Whether MCP tool arguments should be included in emitted telemetry events.
<!-- trie:end -->
<!-- trie:section symbol=trie/telemetry:capture_responses fingerprint=acea27da4d13a7d809beb946585c7624b46364240bc9ae35d0124ce705b143f3 body_fp=3a64f8bcce0c86b8d9c7df7f36dd7abfb1a9c29593c692222c948524e5531df2 source_ref=cf002b82dfc49d9b31513e0a29c2f60d2fe0c63d -->
## `capture_responses() -> bool`

Whether full MCP response bodies should be captured rather than only their sizes.
<!-- trie:end -->
<!-- trie:section symbol=trie/telemetry:_apply_redactions fingerprint=d72a6e1ff48f56b4aebf8d4fa8033bd30739a0ccc8d9a88fd5cce437939ac442 body_fp=fc2b03f719709dc10168435a6603be78c7df45cf7018d3eed6d4c513d678ca53 source_ref=cf002b82dfc49d9b31513e0a29c2f60d2fe0c63d -->
## `_apply_redactions(record: dict[str, Any]) -> dict[str, Any]`

Replace values at `_redact_keys` paths with `"<redacted>"`, supporting dotted keys for nested dicts.
<!-- trie:end -->
<!-- trie:section symbol=trie/telemetry:emit fingerprint=fb39e43c1ddece91be45d130799d2e85fe3d8d926af7d96147100187e17a06f1 body_fp=5520b35c848f9440ffc2a37d5c8a36eae2f1a54e1b44a8eac08c00839af9797a source_ref=cf002b82dfc49d9b31513e0a29c2f60d2fe0c63d -->
## `emit(event: str, **fields: Any) -> None`

Append one JSONL telemetry event to the log; silent no-op when disabled.

- `event`: string label identifying the event type (e.g. `"scan"`, `"cli"`).
- `ts` and `event` are auto-stamped; non-JSON-native values are stringified via `default=str`.
- Errors during write print to stderr and never propagate.
<!-- trie:end -->
<!-- trie:section symbol=trie/telemetry:timed fingerprint=adf66e22e173e164a803b841f555fc7823acccc234c7aac8df2e0f8edc481bc2 body_fp=58b43396b24b213c0f79434dd64ff8feb81c5b247902446e42b145379bca1896 source_ref=cf002b82dfc49d9b31513e0a29c2f60d2fe0c63d -->
## `timed(event: str, **fields: Any) -> Iterator[dict[str, Any]]`

Emit a telemetry event with automatic `duration_ms` on block exit.

- Yields a mutable dict; caller adds fields during the block before emission.
- On exception, adds `error` (exception class name) and re-raises.
<!-- trie:end -->
<!-- trie:section symbol=trie/telemetry:reset_for_tests fingerprint=f4cbaa364efb9c47aa27e981e77bb54fa7f851375bc3e0e4c4315c99c17769b3 body_fp=9e1f422b5a703b072ca1b59116fa382ae9d4a36c49c7178e22579496f77d6f46 source_ref=cf002b82dfc49d9b31513e0a29c2f60d2fe0c63d -->
## `reset_for_tests() -> None`

Reset all process-wide telemetry state and close any open log file.
<!-- trie:end -->