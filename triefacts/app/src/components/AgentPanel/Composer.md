---
trie_version: 0.1.9
source: app/src/components/AgentPanel/Composer.tsx
file_fingerprint: 45fabedc907b8c5f3a917239c8644e904570378d0b4ce111babe2bc44b55105b
last_synced_at: '2026-06-17T16:36:54Z'
defines:
- kind: interface
  qualified_name: app/src/components/AgentPanel/Composer:Pill
  lines: 7-10
- kind: function
  qualified_name: app/src/components/AgentPanel/Composer:Composer
  lines: 16-181
- kind: function
  qualified_name: app/src/components/AgentPanel/Composer:ModelSwitcher
  lines: 186-286
incoming_refs: 1
outgoing_refs: 3
---
<!-- trie:section symbol=app/src/components/AgentPanel/Composer:Pill fingerprint=2a85aeee6ea8e7d32a50010511c37bf72e13ede47d80b35050cf612d7bd472d0 body_fp=5489cca0b775bb95e5366a7c18005aa6df53201a7e6a071fed048f62343808b8 source_ref=0507ebfbf94c6e4ab501411b0c76f24a5f80306c role=model -->
Represents a single symbol context pill attached to a composer message.

- `qname`: fully-qualified symbol name used to resolve documentation via the graph client.
- `label`: shortened display name shown in the pill UI (typically the last segment of `qname`).
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/AgentPanel/Composer:Composer fingerprint=1617f77614b4aa054a645f9f894c4400541e2a15f7b776d44390ce3b976e6beb body_fp=178054720b9c555440d721662dc4615ccdb3bc5914789baca9c74d43ea1465ce source_ref=0507ebfbf94c6e4ab501411b0c76f24a5f80306c role=api -->
Message composer component that manages symbol-context pills, resolves them via `graphClient` on send, and renders a Send/Stop control.

- `running` — when `true`, replaces the Send button with a Stop button that calls `onStop`
- `disabled` — greys out and locks the entire composer
- `onSend` — receives the fully assembled message string, including resolved symbol prose prepended as context
- `onStop` — called when the user clicks the Stop button during a running turn
- Listens for `trie:node-selected` custom events to add pills from graph node selections
- Cmd/Ctrl+K globally focuses the textarea
- Backspace on empty input removes the last pill
- Send-on-Enter behaviour is driven by the `agent.sendOnEnter` setting
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/AgentPanel/Composer:ModelSwitcher fingerprint=7d64d75e087707d4def16fccc6087d07a82063fd2f22ab652dc8404547edc472 body_fp=5a36e0eaa31d758426f50fc72e4ac20dd958097655e6400cd019175182dda93b source_ref=0507ebfbf94c6e4ab501411b0c76f24a5f80306c role=api -->
Render a compact model-picker button that opens a searchable popover, persisting the selection to `useModelStore`.

- `disabled` — disables the trigger button; also disabled when no models are loaded
- Search input only shown when more than 8 models exist in the flat list
- Popover closes on outside click or Escape; query resets on close
<!-- trie:end -->