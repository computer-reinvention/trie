---
trie_version: 0.1.9
source: app/src/hooks/useActivityPoll.ts
file_fingerprint: ca003675add5f5172b1501aa14f30b23b55c3884bd7d85047ca05ef6c9ee50fa
last_synced_at: '2026-06-17T16:39:06Z'
defines:
- kind: constant
  qualified_name: app/src/hooks/useActivityPoll:POLL_MS
  lines: 13-13
- kind: constant
  qualified_name: app/src/hooks/useActivityPoll:SUSTAIN_MS
  lines: 16-16
- kind: function
  qualified_name: app/src/hooks/useActivityPoll:useActivityPoll
  lines: 18-87
incoming_refs: 1
outgoing_refs: 3
---
<!-- trie:section symbol=app/src/hooks/useActivityPoll:POLL_MS fingerprint=43b05b598fc723a1dfc0fe2399da1d96adbd7d6401449da65ba1f98a7ab24797 body_fp=c23ead028151e9eded2e6b94c69243761cd47212d06d594100b02d7edd30c299 source_ref=f59b29880eb7ee5863257083439e7fd0c85d415e role=config -->
Interval in milliseconds between successive activity poll requests.
<!-- trie:end -->
<!-- trie:section symbol=app/src/hooks/useActivityPoll:SUSTAIN_MS fingerprint=342e8f994a7afabdfbcd0dc2d76d4f5b6f05e802484947943cc36768c0711f6b body_fp=3d61b346642664e1e71e1e307afc94ae405035dd7881a6d5a6c35be89ff298b7 source_ref=f59b29880eb7ee5863257083439e7fd0c85d415e role=config -->
Interval in milliseconds between sustain-loop ticks that re-apply the active file's pulse to prevent glow decay between polls.
<!-- trie:end -->
<!-- trie:section symbol=app/src/hooks/useActivityPoll:useActivityPoll fingerprint=ee24e02e06db9e7aa96c4ba602b7c992701a8c5036083f3795a0e13f8c08ac31 body_fp=368eba84ce2f2eeda4039e2999e0ee2f181fbcbf0726e0ddeecb3c35c58d6679 source_ref=f59b29880eb7ee5863257083439e7fd0c85d415e role=orchestration -->
React hook that polls the activity API every 1500 ms and projects agent write/stale state onto graph nodes, with a 300 ms sustain loop to hold the active file's glow between polls.

- `enabled` — when `false`, skips all polling and cleanup is a no-op
- On unmount or `enabled` flip, resets all previously glowed files to `idle` and cancels both timers
<!-- trie:end -->