---
trie_version: 0.1.9
source: app/src/components/AgentPanel/ToolRow.tsx
file_fingerprint: 154c141b8d10d92aa02042881baf484f3bd63282d3b5ba12339273df0b6629b5
last_synced_at: '2026-06-17T16:37:13Z'
defines:
- kind: module
  qualified_name: app/src/components/AgentPanel/ToolRow:__module__
  lines: 1-358
- kind: function
  qualified_name: app/src/components/AgentPanel/ToolRow:intentColor
  lines: 13-21
- kind: function
  qualified_name: app/src/components/AgentPanel/ToolRow:inputSummary
  lines: 28-42
- kind: function
  qualified_name: app/src/components/AgentPanel/ToolRow:bareTool
  lines: 44-46
- kind: function
  qualified_name: app/src/components/AgentPanel/ToolRow:StatusIcon
  lines: 48-57
- kind: function
  qualified_name: app/src/components/AgentPanel/ToolRow:ToolRow
  lines: 59-192
- kind: function
  qualified_name: app/src/components/AgentPanel/ToolRow:SubAgentSection
  lines: 197-255
- kind: function
  qualified_name: app/src/components/AgentPanel/ToolRow:SubAgentStep
  lines: 259-278
- kind: function
  qualified_name: app/src/components/AgentPanel/ToolRow:prettyTarget
  lines: 283-290
- kind: function
  qualified_name: app/src/components/AgentPanel/ToolRow:Pre
  lines: 292-330
- kind: function
  qualified_name: app/src/components/AgentPanel/ToolRow:PermBtn
  lines: 332-354
incoming_refs: 1
outgoing_refs: 13
---
<!-- trie:section symbol=app/src/components/AgentPanel/ToolRow:__module__ fingerprint=ceafe300809ced01182526f0e3c6c11837fddcfaa5cae422de254cca63931410 body_fp=684340fc36d452cd053b98512800d241e1c245503cb3ef86108e9b63843b4418 source_ref=6505192c7a3549c60aaa0a7321e7e0588c53f960 role=api -->
Renders a single tool-invocation row in the agent transcript, including status icon, input summary, collapsible raw I/O, inline permission prompts, and nested sub-agent transcripts.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/AgentPanel/ToolRow:intentColor fingerprint=59f21175c0b0fd88f616cf02eb8204064ea7df410f8c075b7548ad1290799799 body_fp=86f76eea844a24ead36857ab89b8255a01e41df40e566fc6f6dd3adb2c9958c0 source_ref=6505192c7a3549c60aaa0a7321e7e0588c53f960 role=util -->
Map a tool name to its `ACTIVITY` hue so chat rows and graph nodes share the same intent color.

- Returns `"#475569"` (muted slate) for unrecognised tools.
- Strips a `trie_` prefix before matching.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/AgentPanel/ToolRow:inputSummary fingerprint=1e8864e50a56c4f7cfe4a021e1a4209be61576c0e9ed9cae38eb2fb758ef76f8 body_fp=f232c83d2bd1c60e0702dc999952f3e7324c53bfbf511481a0bd7cb594cd90eb source_ref=6505192c7a3549c60aaa0a7321e7e0588c53f960 role=util -->
Return the first matching string field from `input` using a priority-ordered key list for display in `ToolRow`.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/AgentPanel/ToolRow:bareTool fingerprint=2c654faaff2aabbc1649e2593d811b1c6f5f58bb5e0ddbf19e0f4e00da337dcd body_fp=394289517be2e4f960dfdd61c2498c41918ae23e41af8960968ddee308224580 source_ref=6505192c7a3549c60aaa0a7321e7e0588c53f960 role=util -->
Strip the `trie_` prefix from a tool name, returning the bare verb.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/AgentPanel/ToolRow:StatusIcon fingerprint=9056935385baec45954c8d67d03c0e9267496330c59e7b8050168ec04105387e body_fp=2d3cb25a115795c4c8b039cf011b09f9d8dcb64b9096b6b5b96b2bb20bdb6de5 source_ref=6505192c7a3549c60aaa0a7321e7e0588c53f960 role=util -->
Render a status icon for a tool invocation: spinning loader, check, alert, or faint dot.

- `status`: one of `"running"`, `"completed"`, `"error"`, or any other value (renders dot).
- `color`: applied to the running spinner; completed and error icons use fixed CSS variables.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/AgentPanel/ToolRow:ToolRow fingerprint=b6799dc8cc52b9d7e5b667eaf9687cddb6769ca8865914e67eeb63449ee671c3 body_fp=10363b8708a792a0115a7a7c5895e79dc6a1b80495a2a612548b5c9c3067c48f source_ref=6505192c7a3549c60aaa0a7321e7e0588c53f960 role=api -->
Render a single tool invocation row with status icon, input summary, collapsible raw I/O, inline permission prompt, and optional sub-agent transcript.

- `part` — `ToolPart` carrying tool name, status, input/output, and timing metadata.
- `permission` — when present, renders an approve/deny banner correlated to this call.
- `onResolvePermission` — called with the request ID and `"once" | "always" | "reject"` on user action.
- Left-border color pulses with live graph activity for the tool's target symbol; clicking the summary reveals that symbol in the topology tab.
- If the tool is `task`, renders a `SubAgentSection` for the spawned child session.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/AgentPanel/ToolRow:SubAgentSection fingerprint=a67af4280a40dd930aae88809080300370e0bccdc3447a082f7b4365f2308b1e body_fp=43d45ca22b2b21efca28d9f66ca8e4e297a99fd8cef94e780fad193477c5f8da source_ref=6505192c7a3549c60aaa0a7321e7e0588c53f960 role=api -->
Render a collapsible inline transcript for a child agent session identified by `sessionId`, showing tool steps via `SubAgentStep` and text parts via `ReactMarkdown`.

- `sessionId`: looked up in `agentStore` to obtain messages and running state.
- `accent`: color propagated from the parent `ToolRow`'s left-border hue.
- Filters messages through `isRenderablePart` to exclude synthetic/system artifacts.
- Collapsed by default; shows a live spinner while `session.running` is true.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/AgentPanel/ToolRow:SubAgentStep fingerprint=30ce392df16312c6cf24171e572c5b468b05f29777081344d2c36208ac417e1b body_fp=239d1c499a7b65b6b61894e12bb4d323a26e76099ed16048f4884df33584d31c source_ref=6505192c7a3549c60aaa0a7321e7e0588c53f960 role=api -->
Render a single compact tool step inside a `SubAgentSection`: status icon, tool verb, and prettified target summary.

- `accent`: color used for the status icon, overriding the tool's intent color.
- `color`: derived from `intentColor` and applied to the tool name span.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/AgentPanel/ToolRow:prettyTarget fingerprint=7130b1bd0347b8da9cee77b5b9b0b503bee2868524da6d417cec8eb31935554a body_fp=f1464297dbf1526ae966ba64f4c3db75ca10636de64a05d227a5f1bcc74878b8 source_ref=6505192c7a3549c60aaa0a7321e7e0588c53f960 role=util -->
Trim a tool-target string for compact display: strips a trailing `:__module__` suffix and collapses paths longer than 48 characters to their last two segments prefixed with `…/`.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/AgentPanel/ToolRow:Pre fingerprint=2f8d879624bb95c34cd5f52bde118f8ccc5943df5b011d90c5916ea6efe8c6d2 body_fp=201ed853c4a38ee24bdca58b5a3a9996771530754b217ca8e55153d475206772 source_ref=6505192c7a3549c60aaa0a7321e7e0588c53f960 role=util -->
Render preformatted text with a hover-activated clipboard copy button.

- `scrollable`: caps block height at `max-h-48` with overflow scroll when true.
- `danger`: switches text color to `--danger` instead of `--text-2`.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/AgentPanel/ToolRow:PermBtn fingerprint=4db697d93427adcb230ad5dd3760333e8837a1fdc4c2a6db1ba6c48075bd9ddf body_fp=3347fdbdb4043ba2f32414111e77513136f98240af217f612f5064ec962779d3 source_ref=6505192c7a3549c60aaa0a7321e7e0588c53f960 role=util -->
Render a styled permission-prompt button with warn or danger coloring.

- `danger`: when `true`, applies `--danger-soft` background instead of warn tint.
<!-- trie:end -->