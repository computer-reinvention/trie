---
trie_version: 0.1.2
source: trie/telemetry.py
file_fingerprint: 139de3396f21b6ea7bf609a055d7cee08a071a4fae7439e93e65104014d2b6fe
last_synced_at: '2026-05-19T10:42:34Z'
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
incoming_refs: 30
outgoing_refs: 0
---
<!-- trie:section symbol=trie/telemetry:configure fingerprint=3d7526358fbe30bf4a41e3bfcc6b5c89580f453b6f8c407595d25483a1214caf body_fp=859ffc13888898ef833937b73f46c2032d9b90d237f097162e027dbe58a1ddd7 source_ref=cf002b82dfc49d9b31513e0a29c2f60d2fe0c63d -->
## `configure(cfg: Debug, project_root: Path) -> None`

Apply `[debug]` config from `trie.toml` process-wide; forces re-resolution on the next emit.

- `cfg`: supplies `log_to_stderr`, `capture_args`, `capture_responses`, `redact_keys`; `TRIE_DEBUG` env var still overrides enable/path.
- Calling multiple times is safe; re-opens log file if path changed.
<!-- trie:end -->

<!-- trie:section symbol=trie/telemetry:is_enabled fingerprint=d642b8f5ca8a8a7555eb9f8c0a66632811aa43c8020ba7c0350a01ef08d96548 body_fp=316d23cd52586adfaeb57b506529d68f67331456f70f0c2364722e43a894cb37 source_ref=cf002b82dfc49d9b31513e0a29c2f60d2fe0c63d -->
## `is_enabled() -> bool`

Return whether telemetry is active for this process, triggering lazy resolution if needed.
<!-- trie:end -->

<!-- trie:section symbol=trie/telemetry:capture_args fingerprint=660c1bcba0896e7c441a5403f1ad313a838a7a14dc22699b2d5c918fdd0ab6ed body_fp=759757e69abd676c50e438ec541e08a57100a9c44158cec39fec4c411cdf321e source_ref=cf002b82dfc49d9b31513e0a29c2f60d2fe0c63d -->
## `capture_args() -> bool`

Return whether MCP tool arguments should be included in telemetry events.
<!-- trie:end -->

<!-- trie:section symbol=trie/telemetry:capture_responses fingerprint=acea27da4d13a7d809beb946585c7624b46364240bc9ae35d0124ce705b143f3 body_fp=fb0fa9bc40165f94bd4a8dc63d3ad5bbe78e3901b69fc1bd140b54ccf6b214ce source_ref=cf002b82dfc49d9b31513e0a29c2f60d2fe0c63d -->
## `capture_responses() -> bool`

Return whether full MCP response bodies should be captured rather than just sizes.
<!-- trie:end -->

<!-- trie:section symbol=trie/telemetry:emit fingerprint=fb39e43c1ddece91be45d130799d2e85fe3d8d926af7d96147100187e17a06f1 body_fp=7a40819a61a397e57b4578e3492b4fe75929fe2922de550b6b9619a51e9e54fb source_ref=cf002b82dfc49d9b31513e0a29c2f60d2fe0c63d -->
## `emit(event: str, **fields: Any) -> None`

Append one JSONL event to the telemetry log; silent no-op when disabled.

- `event`: short event-type name (e.g. `"scan"`, `"cli"`).
- `ts` and `event` fields are stamped automatically; all other fields come from `**fields`.
- Non-JSON-serialisable values (Path, datetime) are stringified via `default=str`.
- Redactions defined in config are applied before writing.
<!-- trie:end -->

<!-- trie:section symbol=trie/telemetry:timed fingerprint=adf66e22e173e164a803b841f555fc7823acccc234c7aac8df2e0f8edc481bc2 body_fp=0fa0a211e54a567a23f9be8d749c0d1bc587c642af05ec2569ff94760db6f816 source_ref=cf002b82dfc49d9b31513e0a29c2f60d2fe0c63d -->
## `timed(event: str, **fields: Any) -> Iterator[dict[str, Any]]`

Context manager that emits `event` on exit with elapsed `duration_ms` automatically appended.

- Yields a mutable dict; caller adds fields learned inside the block.
- On exception, adds `error` (exception class name) before emitting.
<!-- trie:end -->

<!-- trie:section symbol=trie/telemetry:reset_for_tests fingerprint=f4cbaa364efb9c47aa27e981e77bb54fa7f851375bc3e0e4c4315c99c17769b3 body_fp=ec508a422d93aca4ef11e4ace6bbffe05de0226158f88bc9cfb93db1812e6f0a source_ref=cf002b82dfc49d9b31513e0a29c2f60d2fe0c63d -->
## `reset_for_tests() -> None`

Reset all process-level telemetry state to defaults, closing any open log file.
<!-- trie:end -->

<!-- trie:section symbol=trie/telemetry:_resolve fingerprint=2b823d46e6a7cc0c7cfc52d279a833200768631f198ede261bfc2994067a27dc body_fp=34a09b9566ee7ebc7207a0d04bf2032cec6ad74679c75a0715c108687b4f48e0 source_ref=cf002b82dfc49d9b31513e0a29c2f60d2fe0c63d -->
## `_resolve() -> None`

Resolve whether telemetry is enabled and open the log file, reading `TRIE_DEBUG` env var then `cfg.enabled`; idempotent unless `configure()` reset `_resolved`.

- `TRIE_DEBUG=0/false/no/off`: disables telemetry immediately.
- `TRIE_DEBUG=1/true/yes/on`: enables, writing to default path.
- `TRIE_DEBUG=<path>`: enables, writing to that path.
- Subsequent calls are no-ops while `_resolved` is `True`.
<!-- trie:end -->

<!-- trie:section symbol=trie/telemetry:_open fingerprint=d2382bca32b3053880c2f7e6d30f328b5cda996fc590dec5752861d2b1a3cb7d body_fp=ac4bf49c72a09aae3cfb6d0844e8ae17eba3669acd7855cb0d40990061ab3edf source_ref=cf002b82dfc49d9b31513e0a29c2f60d2fe0c63d -->
## `_open(path: Path) -> None`

Open the append-mode log file at `path`; disables telemetry and prints to stderr on `OSError`.
<!-- trie:end -->

<!-- trie:section symbol=trie/telemetry:_close fingerprint=171eb098b8d920cbcff51070df2295d2cf8c29c8e46aa8158c069b3d486e31c4 body_fp=929e80a9313a76e664bfc57bf91b89b3a0dc1d762e999541ec21c558152aa87b source_ref=cf002b82dfc49d9b31513e0a29c2f60d2fe0c63d -->
## `_close() -> None`

Flush and close the open log file handle, setting `_file` to `None`; silently swallows `OSError`.
<!-- trie:end -->

<!-- trie:section symbol=trie/telemetry:_apply_redactions fingerprint=d72a6e1ff48f56b4aebf8d4fa8033bd30739a0ccc8d9a88fd5cce437939ac442 body_fp=71872cd3721ffe9638b8e9c29a9deafb2465784556226992c09a787320a318ce source_ref=cf002b82dfc49d9b31513e0a29c2f60d2fe0c63d -->
## `_apply_redactions(record: dict[str, Any]) -> dict[str, Any]`

Replace values at `_redact_keys` paths with `"<redacted>"` in-place, then return the record.

- Dotted key strings (e.g. `"a.b"`) navigate into nested dicts.
<!-- trie:end -->

<!-- trie:section symbol=trie/telemetry:_DEFAULT_FILENAME fingerprint=9a55f4f84be667ae97ac1a341d080e215f879fba1717c412b86e8be00d921548 body_fp=82f4fc3835a8303eeece6c861e9f33600202fdab40f9e85f0b736892fe093f11 source_ref=cf002b82dfc49d9b31513e0a29c2f60d2fe0c63d -->
## `_DEFAULT_FILENAME = "debug.jsonl"`

Default log filename used when no path is specified in config or env var.
<!-- trie:end -->

<!-- trie:section symbol=trie/telemetry:_cfg fingerprint=f803a03ddbedf169fed3b561490db8ebf2c25cb36f6f6925e575472fd5a4e569 body_fp=e7ad71523c31ef9f93eaf1f3186b311198c4e06ff9fd11a1701f94fd4da06d43 source_ref=cf002b82dfc49d9b31513e0a29c2f60d2fe0c63d -->
## `_cfg: Debug | None = None`

Holds the process-wide `Debug` config; `None` until `configure()` is called.
<!-- trie:end -->

<!-- trie:section symbol=trie/telemetry:_project_root fingerprint=7f1404a6ae2c27aa098d65beb4a5ec00e484dda4224db1c3e0531d94f989f5e4 body_fp=8c4b519359deda04eebe8d8f332e3696a158d73af595bab75ee1f2ce74c0e421 source_ref=cf002b82dfc49d9b31513e0a29c2f60d2fe0c63d -->
## `_project_root: Path | None = None`

Stores the project root path set by `configure()`; used to resolve relative log paths.
<!-- trie:end -->

<!-- trie:section symbol=trie/telemetry:_file fingerprint=f80c5dc793cb1be2813736697260ba3e49782620ce68eb959bb8dcc77c2b5c4c body_fp=b7d28a1eb63fcb1549b81c6e694732b404629f83cfe3aca2da1a0fe6e12da3a7 source_ref=cf002b82dfc49d9b31513e0a29c2f60d2fe0c63d -->
## `_file: IO[str] | None`

Holds the open log file handle; `None` until the first emit resolves and opens it.
<!-- trie:end -->

<!-- trie:section symbol=trie/telemetry:_resolved fingerprint=4a21f07148902d26342f7f14c95bf97c09277efe7d1c8af024a200aa306e900b body_fp=30aafed792a366269e085e3bd1351f7ea64819d67e432a3bada152cd5df57e2e source_ref=cf002b82dfc49d9b31513e0a29c2f60d2fe0c63d -->
## `_resolved: bool = False`

Tracks whether telemetry enable/path resolution has run for this process; reset to `False` by `configure()` to force re-resolution.
<!-- trie:end -->

<!-- trie:section symbol=trie/telemetry:_enabled fingerprint=a4a7acc6d0e8418ce4f4bee46dc2a6528bf2533f2fb58c10da89b6e3ab11cd96 body_fp=5e40d6c0b3e42c28006e370bc0289c2587956d41d0d69fa21a3f583ed4deb69c source_ref=cf002b82dfc49d9b31513e0a29c2f60d2fe0c63d -->
## `_enabled: bool = False`

Process-wide flag; `True` when telemetry is active and the log file is open.
<!-- trie:end -->

<!-- trie:section symbol=trie/telemetry:_log_to_stderr fingerprint=c2a4b91a3b5aacafcf5c68ebdfca09c9c3dd10928bb36485e00a429d7c641321 body_fp=e37877748dea07a21505d7b0418bf89fc1bf77f139b489983b05135be95a4cd5 source_ref=cf002b82dfc49d9b31513e0a29c2f60d2fe0c63d -->
## `_log_to_stderr: bool = False`

Controls whether each emitted event is also printed to stderr.
<!-- trie:end -->

<!-- trie:section symbol=trie/telemetry:_capture_args fingerprint=9d9dcc1072cfa01be373db7e7616a95ba37a9705f456cc7703fe9712c186b6f6 body_fp=38677ea0a4d10faa97491b3c0183352a5886cb9078fedb05230c40511aaec799 source_ref=cf002b82dfc49d9b31513e0a29c2f60d2fe0c63d -->
## `_capture_args: bool = True`

Controls whether MCP tool arguments are included in emitted telemetry events.
<!-- trie:end -->

<!-- trie:section symbol=trie/telemetry:_capture_responses fingerprint=18d89ca3817c4b9efae98046148b77f3d349be60bbe5bbe5af4e8e31b87208f5 body_fp=d9c5ea846166e30ad35ff6bf1677d371906dfce8c246bb8f84824c5f6211f91b source_ref=cf002b82dfc49d9b31513e0a29c2f60d2fe0c63d -->
## `_capture_responses: bool = False`

Process-wide flag controlling whether full MCP response bodies are captured in telemetry events.
<!-- trie:end -->

<!-- trie:section symbol=trie/telemetry:_redact_keys fingerprint=a71082ab8e3ad2ceea716fd06a5efffe0bfa80f926db07fb76c16be4195e8e00 body_fp=ca6a878e88d98e73c8a30868591d0f8861ee6f665af586576be2f695f7cf4d77 source_ref=cf002b82dfc49d9b31513e0a29c2f60d2fe0c63d -->
## `_redact_keys: tuple[str, ...] = ()`

Stores dot-separated key paths whose values are replaced with `"<redacted>"` before writing each event.
<!-- trie:end -->

<!-- trie:section symbol=trie/telemetry:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=646aa0b6766078d13228ca0659b9b8620970c9c26249c7a46959d71ee7f83dc3 source_ref=cf002b82dfc49d9b31513e0a29c2f60d2fe0c63d -->
## `telemetry`

Append-only JSONL telemetry for trie's own operations, enabled via `TRIE_DEBUG` env var or `[debug]` config block.

- `emit(event, **fields)` — write a single timestamped event line
- `timed(event, **fields)` — context manager; auto-adds `duration_ms` and optional `error`
- `configure(cfg, project_root)` — apply config after `Config.find_and_load`; env var wins for enable/path
- `is_enabled()` — cheap process-wide check; triggers lazy resolution on first call
- File opened lazily on first emit, flushed on `atexit`; failures are silent, never propagate
<!-- trie:end -->