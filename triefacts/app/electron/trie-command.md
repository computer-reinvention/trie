---
trie_version: 0.1.9
source: app/electron/trie-command.ts
file_fingerprint: 002d9c69c70cf74b32378901ee68009b6209c7b59894facc3d3d349b7a46385b
last_synced_at: '2026-06-17T16:35:18Z'
defines:
- kind: interface
  qualified_name: app/electron/trie-command:RunSpec
  lines: 23-30
- kind: class
  qualified_name: app/electron/trie-command:TrieCommandRunner
  lines: 32-157
- kind: property
  qualified_name: app/electron/trie-command:TrieCommandRunner.proc
  lines: 33-33
- kind: property
  qualified_name: app/electron/trie-command:TrieCommandRunner.currentRunId
  lines: 34-34
- kind: method
  qualified_name: app/electron/trie-command:TrieCommandRunner.constructor
  lines: 36-39
- kind: method
  qualified_name: app/electron/trie-command:TrieCommandRunner.broadcast
  lines: 41-45
- kind: method
  qualified_name: app/electron/trie-command:TrieCommandRunner.isRunning
  lines: 48-50
- kind: method
  qualified_name: app/electron/trie-command:TrieCommandRunner.cancel
  lines: 53-61
- kind: method
  qualified_name: app/electron/trie-command:TrieCommandRunner.start
  lines: 68-142
- kind: method
  qualified_name: app/electron/trie-command:TrieCommandRunner.emitLine
  lines: 144-156
incoming_refs: 1
outgoing_refs: 0
---
<!-- trie:section symbol=app/electron/trie-command:RunSpec fingerprint=8143d2c9ba83201ecbbd719f7745401eee9a26d753a714de066225ade4808d1f body_fp=3495fa8b0e266558b2950a6cf7efc0452b7a728c8941b8c18fcf6eb804a64f70 source_ref=a070eaf8f8f26f9fcbfc0fe1d2d028b6bf220223 role=model -->
Describes a single trie-cli invocation passed to `TrieCommandRunner.start`.

- `command`: trie subcommand name, e.g. `"sync"` or `"refresh"`.
- `json`: when `true`, stdout lines are parsed as JSON and emitted as `kind: "json"` events.
<!-- trie:end -->
<!-- trie:section symbol=app/electron/trie-command:TrieCommandRunner fingerprint=9659231eedfa0f2fd98e544bdedd7a066cfa6b34d428b4192a2e61b0c887a9e9 body_fp=169ed8bd039d953b2c255d5701316e621aee22196bdcf55f3d46e73e9b66be42 source_ref=a070eaf8f8f26f9fcbfc0fe1d2d028b6bf220223 role=io -->
Spawns the bundled `trie-cli` binary for a given subcommand and relays its lifecycle (stdout, stderr, exit, errors) line-by-line to all renderer windows over the `ipc:trie-command` IPC channel, keyed by a monotonic `runId`.

- `getProjectDir`: injected accessor; throws if it returns `null` at run time.
- `getTrieCliBin`: injected accessor; `start` throws if the returned path does not exist on disk.
- `start(spec)`: cancels any in-flight run before spawning, returns `{ runId }` for renderer correlation; throws synchronously on precondition failure.
- `cancel()`: sends `SIGTERM` to the active process; silently ignores errors.
- `isRunning()`: `true` only when a process is alive and not yet killed.
- JSON mode (`spec.json`): stdout lines are parsed and emitted as `kind:"json"`; non-JSON lines fall back to `kind:"stdout"`.
- On non-zero exit: last 15 stderr lines are included in the `kind:"exit"` payload.
<!-- trie:end -->
<!-- trie:section symbol=app/electron/trie-command:TrieCommandRunner.proc fingerprint=592827af3f2f1e944d81e5651eb3787f84227a6bd938b52c46082f43d66fb16a body_fp=55fbe8a63443f72e438b0f5273cf9383fc7cbd732b8ffe05ed8c9845be59f12d source_ref=a070eaf8f8f26f9fcbfc0fe1d2d028b6bf220223 role=model -->
`TrieCommandRunner.proc` holds the currently active child process, or `null` when no command is running.
<!-- trie:end -->
<!-- trie:section symbol=app/electron/trie-command:TrieCommandRunner.currentRunId fingerprint=90861d34915c5049faade82af8ecdd381f3a2d69d72fc79a7a59665cf9616936 body_fp=3fc918d64b1bdebef22ccfdbd20bca5aaad1736828b65b5775e64408b41fe31a source_ref=a070eaf8f8f26f9fcbfc0fe1d2d028b6bf220223 role=model -->
`TrieCommandRunner.currentRunId` is a monotonically incrementing counter used to assign a unique `runId` to each spawned command.
<!-- trie:end -->
<!-- trie:section symbol=app/electron/trie-command:TrieCommandRunner.constructor fingerprint=257c1be96ae69f4b01c2c69bdb6d78605f59175819fb007d0bf245bf48444c4a body_fp=242e563b2d717017ce1b8f41b5df042887f2ced79bb23132270983d5621cc772 source_ref=a070eaf8f8f26f9fcbfc0fe1d2d028b6bf220223 role=domain -->
Initialise a `TrieCommandRunner` with injected accessors for the project directory and CLI binary path.

- `getProjectDir`: returns `null` when no project is open
- `getTrieCliBin`: returns the absolute path to the bundled `trie-cli` binary
<!-- trie:end -->
<!-- trie:section symbol=app/electron/trie-command:TrieCommandRunner.broadcast fingerprint=d7fd8fb4049778a7983ebdc37c850dd3e031bef9c10bdc1455670839726ef6b5 body_fp=8e4b23c25069cd878c4d81ee200e0ba1ffd341327eb88a2187df2be2835c8c50 source_ref=a070eaf8f8f26f9fcbfc0fe1d2d028b6bf220223 role=io -->
Send `payload` over the `ipc:trie-command` channel to every open `BrowserWindow`.
<!-- trie:end -->
<!-- trie:section symbol=app/electron/trie-command:TrieCommandRunner.isRunning fingerprint=f04ae49f1808f362dda6e792b3f2e5131441cb4c8470f1a6d49c32b28b52b682 body_fp=02474356db554f11392cf6a60777368349497cce147c4327d14ab818af3983d4 source_ref=a070eaf8f8f26f9fcbfc0fe1d2d028b6bf220223 role=domain -->
Returns `true` if `TrieCommandRunner` has a live, unkilled child process.
<!-- trie:end -->
<!-- trie:section symbol=app/electron/trie-command:TrieCommandRunner.cancel fingerprint=a360552ea84a75999434f333a4deb447e5d2d9e457f54309f40cdda0269f8bb3 body_fp=42072675eaae2ef3dfca4ba94ff9b1e01cc464e7992acb657c5b2afb992d448e source_ref=a070eaf8f8f26f9fcbfc0fe1d2d028b6bf220223 role=domain -->
Send `SIGTERM` to the currently running `TrieCommandRunner` child process, if one exists and has not already been killed.
<!-- trie:end -->
<!-- trie:section symbol=app/electron/trie-command:TrieCommandRunner.start fingerprint=64575e696726d48dd554ec97e6f462f9df4d0184d9cc37c82b4557fab640bc4d body_fp=8bf957a7021e455bc591896f28395a68f96b303bb8fc9a9b0359517ede92193c source_ref=a070eaf8f8f26f9fcbfc0fe1d2d028b6bf220223 role=orchestration -->
Cancel any in-flight run, spawn `trie-cli` with the given `RunSpec`, wire stdout/stderr/exit/error to `ipc:trie-command` broadcasts, and return the new `runId`.

- Throws synchronously if no project is open or the `trie-cli` binary is missing.
- `runId` — monotonically incrementing integer; renderer uses it to correlate broadcast events.
- On non-zero exit, broadcasts up to the last 15 stderr lines in the `exit` payload's `stderr` field.
<!-- trie:end -->
<!-- trie:section symbol=app/electron/trie-command:TrieCommandRunner.emitLine fingerprint=4d2f384ca96c58effed74207646a2519c413747d90347f84dbceb6cf8696cab4 body_fp=13652387cd54c75a69c5c35c0b02369c3d8a970b9fa25739ae10d367f20d4fc0 source_ref=a070eaf8f8f26f9fcbfc0fe1d2d028b6bf220223 role=util -->
Broadcast a single trimmed stdout line from `TrieCommandRunner`, emitting a `json` event if `json` is true and the line parses, otherwise a `stdout` event.

- `json`: when true, attempts `JSON.parse`; falls back to raw `stdout` on failure.
- Silently drops empty/whitespace-only lines.
<!-- trie:end -->