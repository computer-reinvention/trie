---
trie_version: 0.3.0
source: tests/fixtures/xlink_project/frontend/src/components/AdminPanel.tsx
file_fingerprint: 6cace60e204ad4f137b0bec89b0ffaccee5808317e47214a25183481e78fe54c
last_synced_at: '2026-08-30T02:44:27Z'
defines:
- kind: function
  qualified_name: tests/fixtures/xlink_project/frontend/src/components/AdminPanel:getAdminStats
  lines: 4-7
  signature: async function getAdminStats()
- kind: function
  qualified_name: tests/fixtures/xlink_project/frontend/src/components/AdminPanel:updateSettings
  lines: 9-12
  signature: 'async function updateSettings(settings: any)'
- kind: function
  qualified_name: tests/fixtures/xlink_project/frontend/src/components/AdminPanel:getItemDetails
  lines: 14-17
  signature: 'async function getItemDetails(itemId: string)'
- kind: function
  qualified_name: tests/fixtures/xlink_project/frontend/src/components/AdminPanel:bulkUpdate
  lines: 19-26
  signature: 'async function bulkUpdate(data: any)'
incoming_refs: 0
outgoing_refs: 4
---
<!-- trie:section symbol=tests/fixtures/xlink_project/frontend/src/components/AdminPanel:getAdminStats fingerprint=c6a723efdad549be58d9412544caf635480f5a55db653efec9959c674f67e966 body_fp=ea0f1f7a39538fee47dfacaefcfbe0e901899e76e1b3aa84bc157aa5f920bf90 source_ref=f3043eb44f09b3a088fddb2957c0909f260c5485 role=io -->
## `async function getAdminStats()`

Fetches admin statistics from the `/api/admin/stats` endpoint and returns the response payload.
<!-- trie:end -->
<!-- trie:section symbol=tests/fixtures/xlink_project/frontend/src/components/AdminPanel:updateSettings fingerprint=d57abdba401989686035ce8174dc01500ce0a264838923ec8afad2b84db023f9 body_fp=5ca17cd18dfc99c4a7a608160276313415608e5c1b755b0a2640a06ea834f40b source_ref=f3043eb44f09b3a088fddb2957c0909f260c5485 role=io -->
## `async function updateSettings(settings: any)`

POST `settings` to `/api/admin/settings` via axios and return the response data.
<!-- trie:end -->
<!-- trie:section symbol=tests/fixtures/xlink_project/frontend/src/components/AdminPanel:getItemDetails fingerprint=2196be867cd1eb3ebd2406f4cbce0d19cf0aa71c0cbc3f7ca23176fc71248eb8 body_fp=b6d595878325c7ab60d9644a195f2b60da389346f7acb0279883e4747b37ddb9 source_ref=f3043eb44f09b3a088fddb2957c0909f260c5485 role=io -->
## `async function getItemDetails(itemId: string)`

Fetch item details from `/api/items/{itemId}` via a GET request and return the response payload.

- `itemId`: path segment interpolated into the request URL.
<!-- trie:end -->
<!-- trie:section symbol=tests/fixtures/xlink_project/frontend/src/components/AdminPanel:bulkUpdate fingerprint=ac4a0e4b704de45a2c6d8fdc9a09a20720cc1a8be54bd5f82087c040705ba38e body_fp=2c0f467628eadc8dc6df83ea1f8cbf1e273bf5e9af726c73b1cc3c9c448417ee source_ref=f3043eb44f09b3a088fddb2957c0909f260c5485 role=io -->
## `async function bulkUpdate(data: any)`

Send a PUT request to `/api/admin/bulk` via axios and return the response data payload.
<!-- trie:end -->