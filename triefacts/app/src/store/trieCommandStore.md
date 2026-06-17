---
trie_version: 0.1.9
source: app/src/store/trieCommandStore.ts
file_fingerprint: 4573cfe600592a526c376ee694c992cde58e04ccb1b9a7caa343a106e3e2f86f
last_synced_at: '2026-06-17T16:40:45Z'
defines:
- kind: function
  qualified_name: app/src/store/trieCommandStore:trie
  lines: 5-5
- kind: interface
  qualified_name: app/src/store/trieCommandStore:OutputLine
  lines: 7-10
- kind: type
  qualified_name: app/src/store/trieCommandStore:CommandCompleteListener
  lines: 15-15
- kind: interface
  qualified_name: app/src/store/trieCommandStore:TrieCommandStore
  lines: 17-38
- kind: function
  qualified_name: app/src/store/trieCommandStore:defFor
  lines: 40-42
- kind: constant
  qualified_name: app/src/store/trieCommandStore:useTrieCommandStore
  lines: 44-161
- kind: function
  qualified_name: app/src/store/trieCommandStore:summariseJson
  lines: 164-175
incoming_refs: 6
outgoing_refs: 3
---
<!-- trie:section symbol=app/src/store/trieCommandStore:trie fingerprint=d81964481f895264e77431f65c590a5ffe9eef7a7a98fcfddb6a40ac89d33cf5 body_fp=0cc2d905ac7e9952bdfad01979a1563908dd6e56940ef59e9d77147a1444dfdc source_ref=dc6321b3f5ecc6f272eda5dbbecd44577a05bf8c role=util -->
Return the `trie` IPC bridge object attached to `window` by the Tauri preload script.
<!-- trie:end -->
<!-- trie:section symbol=app/src/store/trieCommandStore:OutputLine fingerprint=86d2fc9f61d0d4a53527540598618630a046f52a20e66d156e9e66786e015fd7 body_fp=938623b898cb9961403e25d720a1a9ab1259de86cc357758300c11b49107f257 source_ref=dc6321b3f5ecc6f272eda5dbbecd44577a05bf8c role=model -->
Represents a single line of terminal output with its source stream.

- `stream`: distinguishes process stdout/stderr from in-app system messages.
<!-- trie:end -->
<!-- trie:section symbol=app/src/store/trieCommandStore:CommandCompleteListener fingerprint=3c148f01681d84fedce3bd71e470a13215c03d347a76afeb3dc2f1eebd73000f body_fp=5f865e7bca9d0923198c53db1d086746368e9792e99e66ec3ac2b829cf18aeb7 source_ref=dc6321b3f5ecc6f272eda5dbbecd44577a05bf8c role=model -->
Callback fired when a trie command finishes; receives the command name and whether it exited cleanly.

- `ok` — `true` only on exit code 0
<!-- trie:end -->
<!-- trie:section symbol=app/src/store/trieCommandStore:TrieCommandStore fingerprint=85c27a36c7003797d941924af39af005d3949468b238b6a5c611fe8297dc13a6 body_fp=19c7b4680f3d8f7c1bd4dd51d0646f3050419d0d4950de7b69020b47b78e1bad source_ref=dc6321b3f5ecc6f272eda5dbbecd44577a05bf8c role=model -->
Zustand store shape for managing trie CLI command execution, output streaming, and completion callbacks.

- `runId`: IPC run identifier for the active/last run; used to discard stale events.
- `exitCode`: `null` while running or before any run; set on clean or error exit.
- `jsonEvents`: structured events emitted only when the command runs with `--json`.
- `subscribed`: guards against registering the global IPC `onEvent` listener twice.
- `completeListeners`: called after each run; registered externally by App/Settings.
- `onComplete`: registers a listener and returns an unsubscribe function.
- `run`: resolves after the IPC `run` call is acknowledged; output arrives asynchronously via `subscribe`.
- `cancel`: best-effort; appends a system line to `output` regardless of IPC result.
<!-- trie:end -->
<!-- trie:section symbol=app/src/store/trieCommandStore:defFor fingerprint=cae6ebcb96675885479e343f25d20123aacd582d51026cdae42064a3510d6c53 body_fp=cf8839b215ab2a3a7213aa5498a5860a9db8f6714fc6d428b70a43ed655b2b4a source_ref=dc6321b3f5ecc6f272eda5dbbecd44577a05bf8c role=util -->
Look up and return the `CommandDef` entry matching `command` from `TRIE_COMMANDS`, or `undefined` if not found.
<!-- trie:end -->
<!-- trie:section symbol=app/src/store/trieCommandStore:useTrieCommandStore fingerprint=5fbe64e50dc7e2afa93012ad9987745cca5d746d4cc01975d3ba269355561b9f body_fp=783b21941aadfbb669f533fafc0be8d3cf5b7d2f1bcbc031dbb7fd45c340aa66 source_ref=dc6321b3f5ecc6f272eda5dbbecd44577a05bf8c role=orchestration -->
Zustand store managing the lifecycle of a single trie CLI command: spawning, streaming output, cancellation, and completion notifications.

- `subscribe` — wires the global IPC `onEvent` listener once; subsequent calls are no-ops.
- `run` — resets state, builds CLI args from `CommandDef`, invokes `trie().trieCommand.run`, and stores the returned `runId`.
- `cancel` — calls `trie().trieCommand.cancel()` best-effort and appends a system line to output.
- `onComplete` — registers a `CommandCompleteListener`; returns an unsubscribe function.
- `jsonEvents` — accumulates parsed JSON objects from `--json`-mode commands.
- `exitCode` — `null` while running or before first run; set to the process exit code on `"exit"` event.
<!-- trie:end -->
<!-- trie:section symbol=app/src/store/trieCommandStore:summariseJson fingerprint=1482108e04c16e5c7aff3f80a1781ffc76a6e0187a48429564531d19d3ef2ebb body_fp=87a692160457ed6f401769e480ec1f58f1ad757584654ff46f61b37170a839b7 source_ref=dc6321b3f5ecc6f272eda5dbbecd44577a05bf8c role=util -->
Convert a structured JSONL event object into a single human-readable summary line for display in the command output log.

- Falls back to compact `JSON.stringify` for unrecognised `kind` values.
<!-- trie:end -->