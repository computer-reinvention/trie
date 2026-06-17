---
trie_version: 0.1.9
source: app/src/components/GraphCanvas/Legend.tsx
file_fingerprint: fdb9efe3c5428b1b78463a6bda70c789192a7f57e6b22be4befcc9cb1bd2009e
last_synced_at: '2026-06-17T16:37:57Z'
defines:
- kind: constant
  qualified_name: app/src/components/GraphCanvas/Legend:MEMBER_GROUPINGS
  lines: 8-12
- kind: function
  qualified_name: app/src/components/GraphCanvas/Legend:Legend
  lines: 16-132
incoming_refs: 1
outgoing_refs: 5
---
<!-- trie:section symbol=app/src/components/GraphCanvas/Legend:MEMBER_GROUPINGS fingerprint=afd3fbeec4360e3ad153371a89bd0e41c4d12e3d7e23476d16683710e82c983c body_fp=f3ad26042a20406ac8312aad9d87b0aa581f3c9f6f99787d87b89fcbd7db2fb6 source_ref=10c8b5b49d4b81fd6749703a9a77c7a526b62882 role=config -->
Static list of the three available `MemberGrouping` options with their display labels for the `Legend` selector UI.

- `key`: the `MemberGrouping` store value passed to `setMemberGrouping`
- `label`: the human-readable button text shown in the UI
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/GraphCanvas/Legend:Legend fingerprint=5c545458456432f3eed7e1cb45a87c2d2b7991aa79152ce826c4193df2ebee91 body_fp=d4241a0415963caec275435fd6013bbe11cd9242604b96d119ed7dcea7665774 source_ref=10c8b5b49d4b81fd6749703a9a77c7a526b62882 role=api -->
Render the sidebar Legend panel with a lens switcher (role/subsystem axis), call-depth colour key, click-to-isolate group list, member-grouping selector, and tests toggle.

- `groups` — up to 20 groups from `componentView`, sorted by `order` ascending.
- Toggling "Show tests" refetches both the system model and all edges via `graphClient`, then updates the store; failures are silently swallowed.
- Returns `null` when `model` is not yet loaded.
<!-- trie:end -->