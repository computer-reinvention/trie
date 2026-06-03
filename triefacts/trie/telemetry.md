---
trie_version: 0.1.5
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
<!-- trie:section symbol=trie/telemetry:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=34b8104bbf3b909fb71a60314379f0506475022ca018f809456b3551f4a615ab source_ref=cf002b82dfc49d9b31513e0a29c2f60d2fe0c63d -->
Provides append-only JSONL telemetry for trie's development and validation operations.

- Enabled via `TRIE_DEBUG` env var or `[debug]` config in `trie.toml`
- Captures 8 event types: `cli`, `scan`, `parse_file`, `cascade`, `verify`, `sync_file`, `mcp_call`, `model_call`
- Uses `emit(event, **fields)` for one-off events and `timed(event, **fields)` context manager for duration capture
- Process-wide configuration applied via `configure(cfg, project_root)`
- Lazy file opening with buffered writes, never blocks or raises into user code
<!-- trie:end -->
<!-- trie:section symbol=trie/telemetry:_DEFAULT_FILENAME fingerprint=9a55f4f84be667ae97ac1a341d080e215f879fba1717c412b86e8be00d921548 body_fp=294469750694409b4f90412be80f0ea30313456580fb139b100c0dc2c0a8bdf6 source_ref=cf002b82dfc49d9b31513e0a29c2f60d2fe0c63d -->
Default filename for telemetry output when no specific path is configured.
<!-- trie:end -->
<!-- trie:section symbol=trie/telemetry:_cfg fingerprint=f803a03ddbedf169fed3b561490db8ebf2c25cb36f6f6925e575472fd5a4e569 body_fp=0ca45842c743f3c7af9ce91dc0408adb9a99c5ff53381095c84fa7aff6bbcb90 source_ref=cf002b82dfc49d9b31513e0a29c2f60d2fe0c63d -->
Global variable storing the Debug configuration from trie.toml, set by `configure()` and read by telemetry functions.
<!-- trie:end -->
<!-- trie:section symbol=trie/telemetry:_project_root fingerprint=7f1404a6ae2c27aa098d65beb4a5ec00e484dda4224db1c3e0531d94f989f5e4 body_fp=6906848dcd86ee27e62bf69132a61f56504b6171ce4b13944a0f1dab21f1559a source_ref=cf002b82dfc49d9b31513e0a29c2f60d2fe0c63d -->
Stores the project root path for resolving relative telemetry log paths when configured.
<!-- trie:end -->
<!-- trie:section symbol=trie/telemetry:_file fingerprint=f80c5dc793cb1be2813736697260ba3e49782620ce68eb959bb8dcc77c2b5c4c body_fp=e0f6cf26e805bd3b0bc1b7a81457fd5c05685f3340464ae56f7afc6c7a45de9a source_ref=cf002b82dfc49d9b31513e0a29c2f60d2fe0c63d -->
Open file handle for the telemetry log, or None when closed/disabled.
<!-- trie:end -->
<!-- trie:section symbol=trie/telemetry:_resolved fingerprint=4a21f07148902d26342f7f14c95bf97c09277efe7d1c8af024a200aa306e900b body_fp=9b44843b5195f02aeede95c917fd0f6293919dd858c43cff34b5abd073f5a11d source_ref=cf002b82dfc49d9b31513e0a29c2f60d2fe0c63d -->
Process-wide flag tracking whether telemetry enable/path resolution has been performed yet.
<!-- trie:end -->
<!-- trie:section symbol=trie/telemetry:_enabled fingerprint=a4a7acc6d0e8418ce4f4bee46dc2a6528bf2533f2fb58c10da89b6e3ab11cd96 body_fp=337c8e4fdc2c85e8cbbc0267fb34a0adab17bb1ec06429b73c7aa3f5c605ac08 source_ref=cf002b82dfc49d9b31513e0a29c2f60d2fe0c63d -->
Process-wide flag indicating whether telemetry is currently enabled.
<!-- trie:end -->
<!-- trie:section symbol=trie/telemetry:_log_to_stderr fingerprint=c2a4b91a3b5aacafcf5c68ebdfca09c9c3dd10928bb36485e00a429d7c641321 body_fp=bfe177db5b751a0b9bf876b975562bf5d80954edbbe62aab6034244fbd8db2a3 source_ref=cf002b82dfc49d9b31513e0a29c2f60d2fe0c63d -->
Controls whether telemetry events are echoed to stderr in addition to the log file.
<!-- trie:end -->
<!-- trie:section symbol=trie/telemetry:_capture_args fingerprint=9d9dcc1072cfa01be373db7e7616a95ba37a9705f456cc7703fe9712c186b6f6 body_fp=b055be59421177303ad4de05863cae67f54861d4e68a6c2ebbf3fef4c21e0200 source_ref=cf002b82dfc49d9b31513e0a29c2f60d2fe0c63d -->
Process-global flag controlling whether MCP tool arguments are included in telemetry events.
<!-- trie:end -->
<!-- trie:section symbol=trie/telemetry:_capture_responses fingerprint=18d89ca3817c4b9efae98046148b77f3d349be60bbe5bbe5af4e8e31b87208f5 body_fp=163f97fd68fd04197928f4a6c62449304a5b48d2f39bc342f202bf82dc54bb88 source_ref=cf002b82dfc49d9b31513e0a29c2f60d2fe0c63d -->
Process-global flag controlling whether telemetry captures full MCP response bodies instead of just response sizes.
<!-- trie:end -->
<!-- trie:section symbol=trie/telemetry:_redact_keys fingerprint=a71082ab8e3ad2ceea716fd06a5efffe0bfa80f926db07fb76c16be4195e8e00 body_fp=6d786ead135797c7bd73b5c9bec32f35522d44aab495552a43a7167fac1f516d source_ref=cf002b82dfc49d9b31513e0a29c2f60d2fe0c63d -->
Global tuple storing dotted key paths to redact from telemetry records.
<!-- trie:end -->
<!-- trie:section symbol=trie/telemetry:configure fingerprint=3d7526358fbe30bf4a41e3bfcc6b5c89580f453b6f8c407595d25483a1214caf body_fp=bc70ddf9b3281289a1e03745acf906bf0730bec9bf4fd9cfb4e74290ddefe1db source_ref=cf002b82dfc49d9b31513e0a29c2f60d2fe0c63d -->
Applies debug settings from trie.toml configuration to process-wide telemetry state.

- Environment variable TRIE_DEBUG overrides cfg.enabled for enable/disable and path decisions
- Forces re-resolution of telemetry configuration on next emit operation
<!-- trie:end -->
<!-- trie:section symbol=trie/telemetry:_resolve fingerprint=2b823d46e6a7cc0c7cfc52d279a833200768631f198ede261bfc2994067a27dc body_fp=2c920d34f455b5199a804d91db941b478a024be592ab6e540c550acd00b0951c source_ref=cf002b82dfc49d9b31513e0a29c2f60d2fe0c63d -->
Determines telemetry enable state and log file path from environment and configuration.

- Prioritizes `TRIE_DEBUG` environment variable over configuration settings
- Parses boolean values from environment variable or uses custom path
- Sets global flags for stderr logging, argument capture, and response capture
- Opens log file at resolved path using `_open()`
<!-- trie:end -->
<!-- trie:section symbol=trie/telemetry:_open fingerprint=d2382bca32b3053880c2f7e6d30f328b5cda996fc590dec5752861d2b1a3cb7d body_fp=bb7b9e37bc49e206d873925191ba0e00fe5a62dc531962154273d29b2682b3d8 source_ref=cf002b82dfc49d9b31513e0a29c2f60d2fe0c63d -->
Opens the telemetry log file for append with line buffering, creating parent directories as needed.

- Disables telemetry silently on OSError instead of raising
- Registers `_close` to run on process exit
- Sets global `_file` handle and `_enabled` flag
<!-- trie:end -->
<!-- trie:section symbol=trie/telemetry:_close fingerprint=171eb098b8d920cbcff51070df2295d2cf8c29c8e46aa8158c069b3d486e31c4 body_fp=325374c34c0f00b4643e28fdfc70b2b4e3a4a4a15a8331eb1a99d8ec5b129ef6 source_ref=cf002b82dfc49d9b31513e0a29c2f60d2fe0c63d -->
Closes the telemetry log file and resets the global file handle, suppressing any OSError exceptions.
<!-- trie:end -->
<!-- trie:section symbol=trie/telemetry:is_enabled fingerprint=d642b8f5ca8a8a7555eb9f8c0a66632811aa43c8020ba7c0350a01ef08d96548 body_fp=f7166c5d422d3650be0ce6cf66c193a0f3c086919eeced6ab75ef7f97f22f7bd source_ref=cf002b82dfc49d9b31513e0a29c2f60d2fe0c63d -->
Returns whether telemetry is enabled for the current process, resolving configuration lazily.
<!-- trie:end -->
<!-- trie:section symbol=trie/telemetry:capture_args fingerprint=660c1bcba0896e7c441a5403f1ad313a838a7a14dc22699b2d5c918fdd0ab6ed body_fp=1198d26ab8a1a0f42d971478b4c1994ac4973fa600bc0eb7919f82c25fbc4d75 source_ref=cf002b82dfc49d9b31513e0a29c2f60d2fe0c63d -->
Returns whether MCP tool arguments should be captured in telemetry events.
<!-- trie:end -->
<!-- trie:section symbol=trie/telemetry:capture_responses fingerprint=acea27da4d13a7d809beb946585c7624b46364240bc9ae35d0124ce705b143f3 body_fp=2b5899be86bc62b13f6d41aa142efe5d048d10fefb07021c7ea8d6bbd8f02262 source_ref=cf002b82dfc49d9b31513e0a29c2f60d2fe0c63d -->
Returns whether full MCP response bodies should be captured in telemetry events.
<!-- trie:end -->
<!-- trie:section symbol=trie/telemetry:_apply_redactions fingerprint=d72a6e1ff48f56b4aebf8d4fa8033bd30739a0ccc8d9a88fd5cce437939ac442 body_fp=7ff7cc3eb37852f0cf7319dd07d21198fbaf789eda24b768d0a15e2167fc54e0 source_ref=cf002b82dfc49d9b31513e0a29c2f60d2fe0c63d -->
Redacts sensitive values from telemetry records by replacing them with `"<redacted>"` at configured key paths.

- Supports dotted paths like `"auth.token"` to reach nested dictionary values
- Returns the original record unchanged if no redaction keys are configured
- Modifies the input record in-place and returns it
<!-- trie:end -->
<!-- trie:section symbol=trie/telemetry:emit fingerprint=fb39e43c1ddece91be45d130799d2e85fe3d8d926af7d96147100187e17a06f1 body_fp=09ae2d5d2ca5499c70fde6b6a2e180721e389ddc39d9832a571009c82c43fe21 source_ref=cf002b82dfc49d9b31513e0a29c2f60d2fe0c63d -->
Appends one telemetry event to the debug log with automatic timestamp and optional redactions.

- **event**: Event type name (e.g., 'scan', 'parse_file')
- **fields**: Arbitrary key-value data merged into the event record
- Automatically adds `ts` (ISO-8601 UTC timestamp) and `event` fields
- Serializes with `default=str` so unsupported types become strings
- Silent no-op when telemetry is disabled or file unavailable
<!-- trie:end -->
<!-- trie:section symbol=trie/telemetry:timed fingerprint=adf66e22e173e164a803b841f555fc7823acccc234c7aac8df2e0f8edc481bc2 body_fp=824b8cae82c0d8d660f19e576d40a3870ba415d5be8dc0791ab319d8e3873362 source_ref=cf002b82dfc49d9b31513e0a29c2f60d2fe0c63d -->
Context manager that times a block and emits a telemetry event with duration on exit.

- Yields a mutable dict for the caller to update with additional fields
- Adds `duration_ms` field automatically based on elapsed time
- Adds `error` field with exception class name if the block raises
<!-- trie:end -->
<!-- trie:section symbol=trie/telemetry:reset_for_tests fingerprint=f4cbaa364efb9c47aa27e981e77bb54fa7f851375bc3e0e4c4315c99c17769b3 body_fp=906239b201c6365da726bb6537f1679b2b351124781a8c61f26a24a40e20d402 source_ref=cf002b82dfc49d9b31513e0a29c2f60d2fe0c63d -->
Resets all global telemetry state to initial values and closes any open log file.
<!-- trie:end -->