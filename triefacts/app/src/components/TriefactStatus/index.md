---
trie_version: 0.1.9
source: app/src/components/TriefactStatus/index.tsx
file_fingerprint: a40e8ded95b7a13b6b8015aa6ebcac2ab7499dd15a6b7cf398733b0106c5dfac
last_synced_at: '2026-06-17T16:38:32Z'
defines:
- kind: constant
  qualified_name: app/src/components/TriefactStatus/index:REASON_LABEL
  lines: 5-12
- kind: function
  qualified_name: app/src/components/TriefactStatus/index:TriefactStatus
  lines: 22-127
incoming_refs: 1
outgoing_refs: 1
---
<!-- trie:section symbol=app/src/components/TriefactStatus/index:REASON_LABEL fingerprint=a8978458f1b59c0b3f564796948a613e8aa3db382b8f953ee035d4ebcdeffa1b body_fp=06afe94d7935cf065db9a4c26f5916aa0dc2a822fdb13151ddb8bd252f103f96 source_ref=cbf855ee6c7b635a0c2a98da2351772992937ede role=model -->
Map freshness-gate reason keys emitted by `trie refresh --json` to human-readable status label strings.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/TriefactStatus/index:TriefactStatus fingerprint=5a0636cf56d3759b9e107084171d87c3cbbc91080e7751cbe422aa4989ee08a3 body_fp=7edeba60cf04c862536b8c7fa26d8cf876ac0eae25961f70e2919ed7b10ee0a7 source_ref=cbf855ee6c7b635a0c2a98da2351772992937ede role=api -->
Render a floating bottom-right status card driven by `useRefreshStore`, showing spinner, progress bar, and success/error summary for triefact refresh runs.

- Returns `null` when `phase` is `"idle"` or the user has dismissed the card.
- Progress bar and per-file filename only appear when `total > 0` (a real file sync).
- Auto-dismisses 2600 ms after `phase` reaches `"done"`; resets dismissal on each new `"running"` phase.
- Success line includes `runningCostUsd` only when it is greater than zero.
<!-- trie:end -->