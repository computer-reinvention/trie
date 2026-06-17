---
trie_version: 0.1.9
source: app/src/components/AgentPanel/Transcript.tsx
file_fingerprint: 81109e6c61eee44e5b47c37e0e241b4948f1ac98939a37b8e34b759dbbeea439
last_synced_at: '2026-06-17T16:37:16Z'
defines:
- kind: function
  qualified_name: app/src/components/AgentPanel/Transcript:Transcript
  lines: 30-123
- kind: function
  qualified_name: app/src/components/AgentPanel/Transcript:StreamingIndicator
  lines: 125-145
- kind: function
  qualified_name: app/src/components/AgentPanel/Transcript:MessageView
  lines: 147-218
- kind: function
  qualified_name: app/src/components/AgentPanel/Transcript:PartView
  lines: 220-273
- kind: function
  qualified_name: app/src/components/AgentPanel/Transcript:ReasoningView
  lines: 275-298
- kind: function
  qualified_name: app/src/components/AgentPanel/Transcript:AssistantFooter
  lines: 300-315
- kind: function
  qualified_name: app/src/components/AgentPanel/Transcript:CopyButton
  lines: 317-334
incoming_refs: 1
outgoing_refs: 19
---
<!-- trie:section symbol=app/src/components/AgentPanel/Transcript:Transcript fingerprint=e66e871f308b8f3449e3dce2e0025684424a7a67cdce415c7da0e9a41bb534c4 body_fp=45bf74551aabc907a6531af571a22a63c56ad92608bc7ba6777b87c53b916778 source_ref=5e138c7bc0bac21539743adc243cac3aa3d8df2e role=api -->
Render the full agent conversation with sticky-scroll, a streaming indicator, and an inline error banner.

- `permissionsByCallID` — maps tool call IDs to pending `PermissionRequest` objects
- `onResolvePermission` — callback invoked when the user approves or denies a permission prompt
- `running` — when `true`, shows the animated `StreamingIndicator` after the last message
- `error` — non-null string renders a danger-styled banner at the bottom of the scroll area
- Auto-scroll sticks only when the viewport is within 80 px of the bottom; a "Latest" button re-attaches it
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/AgentPanel/Transcript:StreamingIndicator fingerprint=1c054bb28273fa3fe8f0cd356f3e510dafc654af5430551fb8fb03cc7fa2844b body_fp=1086d9d83df2d794778fe44475ed6f643eae4a617fe9773f0b0ffb27a94bc25f source_ref=5e138c7bc0bac21539743adc243cac3aa3d8df2e role=ui -->
Render a three-dot animated typing indicator with a shimmer "thinking" label while the agent is streaming.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/AgentPanel/Transcript:MessageView fingerprint=2c88e027b964bcff05269c9f3a0fa6a8ada42bc937a6df0c1b3785341ea187fb body_fp=7af3cecf9308ecc344123b90f1e7219ae1ed2f2f898dc3770a4b44f761aa6121 source_ref=5e138c7bc0bac21539743adc243cac3aa3d8df2e role=api -->
Render a single `OpencodeMessage` as either a right-aligned user bubble or a left-aligned assistant column with per-part views and a cost/token footer.

- `permissionsByCallID` — maps tool call IDs to pending `PermissionRequest` objects passed down to `PartView`.
- `onResolvePermission` — callback forwarded to `PartView` for resolving tool permission prompts.
- Filters hidden parts via `isHiddenText` before rendering; returns `null` for user messages with no visible text.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/AgentPanel/Transcript:PartView fingerprint=114573b54b4e57bb7bef26280cb630684a0be9b2380a8a70d4deb6a4d3d78915 body_fp=d67f06547f8934e7a6b87d8bb30cc0e7ee7cddca718d10bb0c46ecf51e29ddd4 source_ref=5e138c7bc0bac21539743adc243cac3aa3d8df2e role=domain -->
Render a single `OpencodePart` as the appropriate UI element based on its `type` field.

- `text` — rendered via `ReactMarkdown`; blank text returns `null`
- `reasoning` — delegates to `ReasoningView`
- `tool` — delegates to `ToolRow`, passing the matching `PermissionRequest` by `callID`
- `patch` — renders a styled chip listing affected filenames and count
- any other type — returns `null`
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/AgentPanel/Transcript:ReasoningView fingerprint=8e4f09320dd6dce269c41b41818c1811205df7fe9795ff8c75b38dc06c95033f body_fp=e09f953202237dade9d478f18393458b8b68cdab2cbd36577b62647d4e536b0d source_ref=5e138c7bc0bac21539743adc243cac3aa3d8df2e role=domain -->
Render a collapsible disclosure widget for a `ReasoningPart`, hiding its text content until the user toggles it open; returns `null` if the text is blank.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/AgentPanel/Transcript:AssistantFooter fingerprint=48801511e7302ea7d6559876fbb255e76597ce1cd19c0585cf706e92acea9acb body_fp=c61e502b36fdae7e082bd66530daa107a5b98732b25fda225e240c8dceca24ac source_ref=5e138c7bc0bac21539743adc243cac3aa3d8df2e role=domain -->
Render a cost/token/error footer for an assistant message; returns `null` when `info.finish` is falsy and `info.cost` is `null`.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/AgentPanel/Transcript:CopyButton fingerprint=03a1ad1dda4830790a6d9f2c08a8b08720f905c244bee94037dd557205d4edb1 body_fp=6f301cba42793b4400e3e2dfcd11c9e913f3e78599b11057427773413f42db89 source_ref=5e138c7bc0bac21539743adc243cac3aa3d8df2e role=util -->
Render a clipboard copy button that shows a check icon for 1200 ms after a successful copy.
<!-- trie:end -->