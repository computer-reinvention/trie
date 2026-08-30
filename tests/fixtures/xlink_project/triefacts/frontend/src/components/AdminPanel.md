---
trie_version: 0.3.0
source: frontend/src/components/AdminPanel.tsx
file_fingerprint: 6cace60e204ad4f137b0bec89b0ffaccee5808317e47214a25183481e78fe54c
last_synced_at: '2026-08-30T02:43:25Z'
defines:
- kind: function
  qualified_name: frontend/src/components/AdminPanel:getAdminStats
  lines: 4-7
  signature: async function getAdminStats()
- kind: function
  qualified_name: frontend/src/components/AdminPanel:updateSettings
  lines: 9-12
  signature: 'async function updateSettings(settings: any)'
- kind: function
  qualified_name: frontend/src/components/AdminPanel:getItemDetails
  lines: 14-17
  signature: 'async function getItemDetails(itemId: string)'
- kind: function
  qualified_name: frontend/src/components/AdminPanel:bulkUpdate
  lines: 19-26
  signature: 'async function bulkUpdate(data: any)'
incoming_refs: 0
outgoing_refs: 0
---
<!-- trie:section symbol=frontend/src/components/AdminPanel:getAdminStats fingerprint=c6a723efdad549be58d9412544caf635480f5a55db653efec9959c674f67e966 body_fp=cf6efbb19ca6abc5e4f646d052f1701a06255fa48d06b817bda489a8a2b2fc9b source_ref=f3043eb44f09b3a088fddb2957c0909f260c5485 role=io -->
## `async function getAdminStats()`

Fetches admin statistics from the backend via GET request to `/api/admin/stats`.

Returns the response data payload.
<!-- trie:end -->
<!-- trie:section symbol=frontend/src/components/AdminPanel:updateSettings fingerprint=d57abdba401989686035ce8174dc01500ce0a264838923ec8afad2b84db023f9 body_fp=6fc9b98ece2303cfe4cd16c64ec767e6d54ba350a48564abfc2722d20c806cbe source_ref=f3043eb44f09b3a088fddb2957c0909f260c5485 role=io -->
## `async function updateSettings(settings: any)`

Sends admin settings to the server and returns the response data.

- `settings`: Arbitrary configuration object posted to the settings endpoint.
<!-- trie:end -->
<!-- trie:section symbol=frontend/src/components/AdminPanel:getItemDetails fingerprint=2196be867cd1eb3ebd2406f4cbce0d19cf0aa71c0cbc3f7ca23176fc71248eb8 body_fp=f0e951bf577397771e40a313b6346f9b75c2df6e0a08162bfead2483349c1e90 source_ref=f3043eb44f09b3a088fddb2957c0909f260c5485 role=io -->
## `async function getItemDetails(itemId: string)`

Fetches item details from the API for the given item ID.

- `itemId`: unique identifier for the item to retrieve.
- Returns: response data from the server.
<!-- trie:end -->
<!-- trie:section symbol=frontend/src/components/AdminPanel:bulkUpdate fingerprint=ac4a0e4b704de45a2c6d8fdc9a09a20720cc1a8be54bd5f82087c040705ba38e body_fp=1bdfdc4f955d459604348e1fa10e99f0db51db3217bbf0a97dc4efcb19c12663 source_ref=f3043eb44f09b3a088fddb2957c0909f260c5485 role=io -->
## `async function bulkUpdate(data: any)`

Sends a PUT request to `/api/admin/bulk` with the provided data and returns the response payload.

- `data`: arbitrary object sent in the request body.
<!-- trie:end -->