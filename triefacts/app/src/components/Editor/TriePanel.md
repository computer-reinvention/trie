---
trie_version: 0.1.9
source: app/src/components/Editor/TriePanel.tsx
file_fingerprint: b44184b5bf17e7063b7280194b713c63a5325b27943930c274dbd7615554debf
last_synced_at: '2026-06-17T16:37:38Z'
defines:
- kind: type
  qualified_name: app/src/components/Editor/TriePanel:FlagValues
  lines: 9-9
- kind: function
  qualified_name: app/src/components/Editor/TriePanel:TriePanel
  lines: 11-132
- kind: function
  qualified_name: app/src/components/Editor/TriePanel:FlagControl
  lines: 134-209
- kind: function
  qualified_name: app/src/components/Editor/TriePanel:OutputView
  lines: 211-292
incoming_refs: 1
outgoing_refs: 5
---
<!-- trie:section symbol=app/src/components/Editor/TriePanel:FlagValues fingerprint=a86c01660f3d6e341e4a9529ac641fac9b1e18810f00e7782089b6f1486db73d body_fp=82e436bde14756ab087223e46624ae54b74e93fe6c87c22dfa41cd2abd100cfb source_ref=e31eccb36e8e3e137de68d87a0e8ee3c50eb6d48 role=model -->
Map of CLI flag keys to their current values, used to track per-command form state in `TriePanel`.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/Editor/TriePanel:TriePanel fingerprint=cb87ddcfebf65d0e0e1d0a00b63690d2c42d673141a5c1e55ca5e5c9ad63f789 body_fp=423d477baf7c13a4a0d8ccb1da6e37e94857064cb4b7adc275317b57c7684a67 source_ref=e31eccb36e8e3e137de68d87a0e8ee3c50eb6d48 role=api -->
Render the trie command panel: command picker, per-command flag form, run/stop controls, and live output view.

- Disables the Run button when no `projectDir` is set in `appStore`.
- Enforces single-run exclusivity by guarding `onRun` against an already-running state.
- Subscribes to `trieCommandStore` output stream on mount via `subscribe()`.
- Shows a warning badge for commands marked `costly` (paid LLM calls).
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/Editor/TriePanel:FlagControl fingerprint=cb1d5cdfbdfdf4659053f4a866d29225882f5a3d02cb7c9fa2640890d66bd7d4 body_fp=ef915a69d4045758eb788e9d9e7baf514b08e1002d674002d80cf3047907afae source_ref=e31eccb36e8e3e137de68d87a0e8ee3c50eb6d48 role=ui -->
Render a single command flag as a toggle switch (`boolean`), dropdown (`enum`), or text/number input based on `flag.type`.

- `flag`: `CommandDef` flag descriptor; `type` determines which control is rendered.
- `value`: current flag value; `undefined` renders as empty/default state.
- `onChange`: called with `undefined` when the input is cleared.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/Editor/TriePanel:OutputView fingerprint=5057ed41b179ccf3fa2bc0389fc94c4a5113d89d1463fd64f81469c65ad3d3cb body_fp=3c983d7cb4971f4210644a938f8fe77f4ccfe1378b269aa41feff01a6045555c source_ref=e31eccb36e8e3e137de68d87a0e8ee3c50eb6d48 role=api -->
Render live command output lines with auto-scroll-to-bottom, exit-code status, and a Clear button.

- `output` — array of log lines; each line carries a `stream` field (`stderr`, `system`, or stdout) that controls text colour.
- `exitCode` — shown as ✓/✗ badge when not `null` and not running.
- `stick` — internal state; disables auto-scroll when user scrolls more than 40 px from the bottom.
- `onClear` — called only when output is non-empty and the command is not running.
<!-- trie:end -->