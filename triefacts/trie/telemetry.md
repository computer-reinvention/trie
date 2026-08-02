---
trie_version: 0.3.0
source: trie/telemetry.py
file_fingerprint: 139de3396f21b6ea7bf609a055d7cee08a071a4fae7439e93e65104014d2b6fe
last_synced_at: '2026-06-03T21:17:36Z'
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
  signature: 'def configure(cfg: Debug, project_root: Path) -> None'
- kind: function
  qualified_name: trie/telemetry:_resolve
  lines: 78-137
  signature: def _resolve() -> None
- kind: function
  qualified_name: trie/telemetry:_open
  lines: 140-149
  signature: 'def _open(path: Path) -> None'
- kind: function
  qualified_name: trie/telemetry:_close
  lines: 152-160
  signature: def _close() -> None
- kind: function
  qualified_name: trie/telemetry:is_enabled
  lines: 163-166
  signature: def is_enabled() -> bool
- kind: function
  qualified_name: trie/telemetry:capture_args
  lines: 169-172
  signature: def capture_args() -> bool
- kind: function
  qualified_name: trie/telemetry:capture_responses
  lines: 175-178
  signature: def capture_responses() -> bool
- kind: function
  qualified_name: trie/telemetry:_apply_redactions
  lines: 181-195
  signature: 'def _apply_redactions(record: dict[str, Any]) -> dict[str, Any]'
- kind: function
  qualified_name: trie/telemetry:emit
  lines: 198-220
  signature: 'def emit(event: str, **fields: Any) -> None'
- kind: function
  qualified_name: trie/telemetry:timed
  lines: 224-250
  signature: 'def timed(event: str, **fields: Any) -> Iterator[dict[str, Any]]'
- kind: function
  qualified_name: trie/telemetry:reset_for_tests
  lines: 253-261
  signature: def reset_for_tests() -> None
incoming_refs: 62
outgoing_refs: 0
---
<!-- trie:section symbol=trie/telemetry:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=34b8104bbf3b909fb71a60314379f0506475022ca018f809456b3551f4a615ab source_ref=cf002b82dfc49d9b31513e0a29c2f60d2fe0c63d role=monitoring-telemetry -->
Provides append-only JSONL telemetry for trie's development and validation operations.

- Enabled via `TRIE_DEBUG` env var or `[debug]` config in `trie.toml`
- Captures 8 event types: `cli`, `scan`, `parse_file`, `cascade`, `verify`, `sync_file`, `mcp_call`, `model_call`
- Uses `emit(event, **fields)` for one-off events and `timed(event, **fields)` context manager for duration capture
- Process-wide configuration applied via `configure(cfg, project_root)`
- Lazy file opening with buffered writes, never blocks or raises into user code
<!-- trie:end -->
<!-- trie:section symbol=trie/telemetry:_DEFAULT_FILENAME fingerprint=9a55f4f84be667ae97ac1a341d080e215f879fba1717c412b86e8be00d921548 body_fp=294469750694409b4f90412be80f0ea30313456580fb139b100c0dc2c0a8bdf6 source_ref=cf002b82dfc49d9b31513e0a29c2f60d2fe0c63d role=monitoring-telemetry -->
Default filename for telemetry output when no specific path is configured.
<!-- trie:end -->
<!-- trie:section symbol=trie/telemetry:_cfg fingerprint=f803a03ddbedf169fed3b561490db8ebf2c25cb36f6f6925e575472fd5a4e569 body_fp=0ca45842c743f3c7af9ce91dc0408adb9a99c5ff53381095c84fa7aff6bbcb90 source_ref=cf002b82dfc49d9b31513e0a29c2f60d2fe0c63d role=monitoring-telemetry -->
Global variable storing the Debug configuration from trie.toml, set by `configure()` and read by telemetry functions.
<!-- trie:end -->
<!-- trie:section symbol=trie/telemetry:_project_root fingerprint=7f1404a6ae2c27aa098d65beb4a5ec00e484dda4224db1c3e0531d94f989f5e4 body_fp=6906848dcd86ee27e62bf69132a61f56504b6171ce4b13944a0f1dab21f1559a source_ref=cf002b82dfc49d9b31513e0a29c2f60d2fe0c63d role=monitoring-telemetry -->
Stores the project root path for resolving relative telemetry log paths when configured.
<!-- trie:end -->
<!-- trie:section symbol=trie/telemetry:_file fingerprint=f80c5dc793cb1be2813736697260ba3e49782620ce68eb959bb8dcc77c2b5c4c body_fp=e0f6cf26e805bd3b0bc1b7a81457fd5c05685f3340464ae56f7afc6c7a45de9a source_ref=cf002b82dfc49d9b31513e0a29c2f60d2fe0c63d role=monitoring-telemetry -->
Open file handle for the telemetry log, or None when closed/disabled.
<!-- trie:end -->
<!-- trie:section symbol=trie/telemetry:_resolved fingerprint=4a21f07148902d26342f7f14c95bf97c09277efe7d1c8af024a200aa306e900b body_fp=9b44843b5195f02aeede95c917fd0f6293919dd858c43cff34b5abd073f5a11d source_ref=cf002b82dfc49d9b31513e0a29c2f60d2fe0c63d role=monitoring-telemetry -->
Process-wide flag tracking whether telemetry enable/path resolution has been performed yet.
<!-- trie:end -->
<!-- trie:section symbol=trie/telemetry:_enabled fingerprint=a4a7acc6d0e8418ce4f4bee46dc2a6528bf2533f2fb58c10da89b6e3ab11cd96 body_fp=337c8e4fdc2c85e8cbbc0267fb34a0adab17bb1ec06429b73c7aa3f5c605ac08 source_ref=cf002b82dfc49d9b31513e0a29c2f60d2fe0c63d role=monitoring-telemetry -->
Process-wide flag indicating whether telemetry is currently enabled.
<!-- trie:end -->
<!-- trie:section symbol=trie/telemetry:_log_to_stderr fingerprint=c2a4b91a3b5aacafcf5c68ebdfca09c9c3dd10928bb36485e00a429d7c641321 body_fp=bfe177db5b751a0b9bf876b975562bf5d80954edbbe62aab6034244fbd8db2a3 source_ref=cf002b82dfc49d9b31513e0a29c2f60d2fe0c63d role=monitoring-telemetry -->
Controls whether telemetry events are echoed to stderr in addition to the log file.
<!-- trie:end -->
<!-- trie:section symbol=trie/telemetry:_capture_args fingerprint=9d9dcc1072cfa01be373db7e7616a95ba37a9705f456cc7703fe9712c186b6f6 body_fp=b055be59421177303ad4de05863cae67f54861d4e68a6c2ebbf3fef4c21e0200 source_ref=cf002b82dfc49d9b31513e0a29c2f60d2fe0c63d role=monitoring-telemetry -->
Process-global flag controlling whether MCP tool arguments are included in telemetry events.
<!-- trie:end -->
<!-- trie:section symbol=trie/telemetry:_capture_responses fingerprint=18d89ca3817c4b9efae98046148b77f3d349be60bbe5bbe5af4e8e31b87208f5 body_fp=163f97fd68fd04197928f4a6c62449304a5b48d2f39bc342f202bf82dc54bb88 source_ref=cf002b82dfc49d9b31513e0a29c2f60d2fe0c63d role=monitoring-telemetry -->
Process-global flag controlling whether telemetry captures full MCP response bodies instead of just response sizes.
<!-- trie:end -->
<!-- trie:section symbol=trie/telemetry:_redact_keys fingerprint=a71082ab8e3ad2ceea716fd06a5efffe0bfa80f926db07fb76c16be4195e8e00 body_fp=6d786ead135797c7bd73b5c9bec32f35522d44aab495552a43a7167fac1f516d source_ref=cf002b82dfc49d9b31513e0a29c2f60d2fe0c63d role=monitoring-telemetry -->
Global tuple storing dotted key paths to redact from telemetry records.
<!-- trie:end -->
<!-- trie:section symbol=trie/telemetry:configure fingerprint=3d7526358fbe30bf4a41e3bfcc6b5c89580f453b6f8c407595d25483a1214caf body_fp=17f34e0a61b88393ab413d19f2939440fc3a6e32d43fa004a5ad37ea284a62f3 source_ref=cf002b82dfc49d9b31513e0a29c2f60d2fe0c63d role=monitoring-telemetry -->
## `def configure(cfg: Debug, project_root: Path) -> None`

Applies debug settings from trie.toml configuration to process-wide telemetry state.

- Environment variable TRIE_DEBUG overrides cfg.enabled for enable/disable and path decisions
- Forces re-resolution of telemetry configuration on next emit operation
<!-- trie:end -->
<!-- trie:section symbol=trie/telemetry:_resolve fingerprint=2b823d46e6a7cc0c7cfc52d279a833200768631f198ede261bfc2994067a27dc body_fp=69dfc0a849dbfcf1458b8f13c47cd43e327aa1cf1fd1fba1ce89dd584bfed47e source_ref=cf002b82dfc49d9b31513e0a29c2f60d2fe0c63d role=monitoring-telemetry -->
## `def _resolve() -> None`

Determines telemetry enable state and log file path from environment and configuration.

- Prioritizes `TRIE_DEBUG` environment variable over configuration settings
- Parses boolean values from environment variable or uses custom path
- Sets global flags for stderr logging, argument capture, and response capture
- Opens log file at resolved path using `_open()`
<!-- trie:end -->
<!-- trie:section symbol=trie/telemetry:_open fingerprint=d2382bca32b3053880c2f7e6d30f328b5cda996fc590dec5752861d2b1a3cb7d body_fp=62e8004d8f03badcc902d467101fe9c2a11cd5f866bc478cbbb909b7545d7737 source_ref=cf002b82dfc49d9b31513e0a29c2f60d2fe0c63d role=monitoring-telemetry -->
## `def _open(path: Path) -> None`

Opens the telemetry log file for append with line buffering, creating parent directories as needed.

- Disables telemetry silently on OSError instead of raising
- Registers `_close` to run on process exit
- Sets global `_file` handle and `_enabled` flag
<!-- trie:end -->
<!-- trie:section symbol=trie/telemetry:_close fingerprint=171eb098b8d920cbcff51070df2295d2cf8c29c8e46aa8158c069b3d486e31c4 body_fp=282903a841f54ce76b00db4c7372c93d8109cecded0ce0a4b174bef783bfabc7 source_ref=cf002b82dfc49d9b31513e0a29c2f60d2fe0c63d role=monitoring-telemetry -->
## `def _close() -> None`

Closes the telemetry log file and resets the global file handle, suppressing any OSError exceptions.
<!-- trie:end -->
<!-- trie:section symbol=trie/telemetry:is_enabled fingerprint=d642b8f5ca8a8a7555eb9f8c0a66632811aa43c8020ba7c0350a01ef08d96548 body_fp=d24db49a2703b74a9c64a3d470dba7496d0c6e86f6582b6df2e4512abee74f2a source_ref=cf002b82dfc49d9b31513e0a29c2f60d2fe0c63d role=monitoring-telemetry -->
## `def is_enabled() -> bool`

Returns whether telemetry is enabled for the current process, resolving configuration lazily.
<!-- trie:end -->
<!-- trie:section symbol=trie/telemetry:capture_args fingerprint=660c1bcba0896e7c441a5403f1ad313a838a7a14dc22699b2d5c918fdd0ab6ed body_fp=5c22ea7c7b8e62134008d7bd73dd959864074ff9784ac9f6ddbf5471e058823e source_ref=cf002b82dfc49d9b31513e0a29c2f60d2fe0c63d role=monitoring-telemetry -->
## `def capture_args() -> bool`

Returns whether MCP tool arguments should be captured in telemetry events.
<!-- trie:end -->
<!-- trie:section symbol=trie/telemetry:capture_responses fingerprint=acea27da4d13a7d809beb946585c7624b46364240bc9ae35d0124ce705b143f3 body_fp=e75fa12e93790084cd999a347ae58381e8481e8ba007669ab26c2126ab0fc7ca source_ref=cf002b82dfc49d9b31513e0a29c2f60d2fe0c63d role=monitoring-telemetry -->
## `def capture_responses() -> bool`

Returns whether full MCP response bodies should be captured in telemetry events.
<!-- trie:end -->
<!-- trie:section symbol=trie/telemetry:_apply_redactions fingerprint=d72a6e1ff48f56b4aebf8d4fa8033bd30739a0ccc8d9a88fd5cce437939ac442 body_fp=f790af39334b7493b4155157278a0b5e8d289f943cb9e88b43a4b5214bccca4f source_ref=cf002b82dfc49d9b31513e0a29c2f60d2fe0c63d role=monitoring-telemetry -->
## `def _apply_redactions(record: dict[str, Any]) -> dict[str, Any]`

Redacts sensitive values from telemetry records by replacing them with `"<redacted>"` at configured key paths.

- Supports dotted paths like `"auth.token"` to reach nested dictionary values
- Returns the original record unchanged if no redaction keys are configured
- Modifies the input record in-place and returns it
<!-- trie:end -->
<!-- trie:section symbol=trie/telemetry:emit fingerprint=fb39e43c1ddece91be45d130799d2e85fe3d8d926af7d96147100187e17a06f1 body_fp=ec47fb56454ced2ab2d2b82a644d4107ae38ee9ae3b9b7114efab0b38105b33d source_ref=cf002b82dfc49d9b31513e0a29c2f60d2fe0c63d role=monitoring-telemetry -->
## `def emit(event: str, **fields: Any) -> None`

Appends one telemetry event to the debug log with automatic timestamp and optional redactions.

- **event**: Event type name (e.g., 'scan', 'parse_file')
- **fields**: Arbitrary key-value data merged into the event record
- Automatically adds `ts` (ISO-8601 UTC timestamp) and `event` fields
- Serializes with `default=str` so unsupported types become strings
- Silent no-op when telemetry is disabled or file unavailable
<!-- trie:end -->
<!-- trie:section symbol=trie/telemetry:timed fingerprint=adf66e22e173e164a803b841f555fc7823acccc234c7aac8df2e0f8edc481bc2 body_fp=bd5b11aa166a71a9cd7710410bca0cceeb12993320e5ee5bac55b9fff908dc59 source_ref=cf002b82dfc49d9b31513e0a29c2f60d2fe0c63d role=monitoring-telemetry -->
## `def timed(event: str, **fields: Any) -> Iterator[dict[str, Any]]`

Context manager that times a block and emits a telemetry event with duration on exit.

- Yields a mutable dict for the caller to update with additional fields
- Adds `duration_ms` field automatically based on elapsed time
- Adds `error` field with exception class name if the block raises
<!-- trie:end -->
<!-- trie:section symbol=trie/telemetry:reset_for_tests fingerprint=f4cbaa364efb9c47aa27e981e77bb54fa7f851375bc3e0e4c4315c99c17769b3 body_fp=ad97ed4b7b422d4897ce68be47ce6d5456d80c2dffdfa56d88b296529b46cafb source_ref=cf002b82dfc49d9b31513e0a29c2f60d2fe0c63d role=test-infrastructure -->
## `def reset_for_tests() -> None`

Resets all global telemetry state to initial values and closes any open log file.
<!-- trie:end -->