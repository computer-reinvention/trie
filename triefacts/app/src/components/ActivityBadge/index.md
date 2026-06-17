---
trie_version: 0.1.9
source: app/src/components/ActivityBadge/index.tsx
file_fingerprint: 47c86530cd7546fb7e738d3db9d981b515d646412caf2908fe817cf64c5732f1
last_synced_at: '2026-06-17T16:36:47Z'
defines:
- kind: constant
  qualified_name: app/src/components/ActivityBadge/index:OP_LABEL
  lines: 11-16
- kind: function
  qualified_name: app/src/components/ActivityBadge/index:ActivityBadge
  lines: 18-73
incoming_refs: 1
outgoing_refs: 1
---
<!-- trie:section symbol=app/src/components/ActivityBadge/index:OP_LABEL fingerprint=0616cd993a09c83ad070aadde51deb4dcb1d9078e98bda9f788f345191017baa body_fp=2e5a74c9d3fc1f4d70375d8c99ac2084a11767028adbb19b0e766488e1138e3e source_ref=d96356eeca7efb674b7481bb112647956ed200bc role=model -->
Maps raw activity `op` strings to human-readable present-participle labels displayed in `ActivityBadge`.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/ActivityBadge/index:ActivityBadge fingerprint=045219c8380abffc6045fa2bcdef9e544829cf9ffc6948761781b779341278bc body_fp=41212ee696bd728bcf4a67f1f129e2a18d31d0dbf75b62319143fd74dedc4016 source_ref=d96356eeca7efb674b7481bb112647956ed200bc role=api -->
Render a title-bar activity indicator with three mutually exclusive states driven by `useActivityStore`.

- **active**: spinner with op label (`OP_LABEL` lookup) and optional `done/total` counter
- **error**: red "sync failed" pill with `status.error` as tooltip
- **stale**: amber `N stale` pill listing up to 12 filenames in the tooltip
- Returns `null` when idle and clean
<!-- trie:end -->