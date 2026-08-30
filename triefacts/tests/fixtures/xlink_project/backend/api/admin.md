---
trie_version: 0.3.0
source: tests/fixtures/xlink_project/backend/api/admin.py
file_fingerprint: 5b38d204aa79f4d10a80f329a7decc4feb93e8384e207a22f015a9b910f2643c
last_synced_at: '2026-08-30T02:44:15Z'
defines:
- kind: constant
  qualified_name: tests/fixtures/xlink_project/backend/api/admin:app
  lines: 5-5
- kind: constant
  qualified_name: tests/fixtures/xlink_project/backend/api/admin:bp
  lines: 6-6
- kind: function
  qualified_name: tests/fixtures/xlink_project/backend/api/admin:get_stats
  lines: 10-11
  signature: def get_stats()
- kind: function
  qualified_name: tests/fixtures/xlink_project/backend/api/admin:get_settings
  lines: 15-16
  signature: def get_settings()
- kind: function
  qualified_name: tests/fixtures/xlink_project/backend/api/admin:update_settings
  lines: 20-21
  signature: 'def update_settings(data: dict)'
- kind: function
  qualified_name: tests/fixtures/xlink_project/backend/api/admin:bulk_update
  lines: 25-26
  signature: def bulk_update()
- kind: function
  qualified_name: tests/fixtures/xlink_project/backend/api/admin:get_item
  lines: 30-31
  signature: 'def get_item(item_id: str)'
incoming_refs: 4
outgoing_refs: 0
---
<!-- trie:section symbol=tests/fixtures/xlink_project/backend/api/admin:app fingerprint=2308bba0f2b72b9f8aa6cd409f3330a47076395b828b6d670ff58ae1bcc72725 body_fp=aac64975a787e594762c5a00286f998988f3270929ed30c3d9fa8e2b72c16f8c source_ref=573c4a8064c1bcd39eb393877ec342e953ac35ee role=config -->
Module-level Flask application instance used to register routes in this admin API module.
<!-- trie:end -->
<!-- trie:section symbol=tests/fixtures/xlink_project/backend/api/admin:bp fingerprint=d0c16be46641d2344840f64cdb1b8e643ab5d50d15262d4adbd2f34f5e3e9307 body_fp=cedc47e5457677863b12e2be6a698bfe950c652066373ce5cd1b37dfe5ab45d3 source_ref=573c4a8064c1bcd39eb393877ec342e953ac35ee role=config -->
Flask `Blueprint` instance named `"admin"`, used to register the `/api/admin/bulk` route independently of the main `app`.
<!-- trie:end -->
<!-- trie:section symbol=tests/fixtures/xlink_project/backend/api/admin:get_stats fingerprint=b506b954cfbb2a3121e8e3a64327b8f4a327c7b45ab51b499227d42bbfcc2bf9 body_fp=22fbcf46699379a95fcd8547b5cfff974aac8f74792c08f04e658d296516f151 source_ref=573c4a8064c1bcd39eb393877ec342e953ac35ee role=api -->
## `def get_stats()`

Flask route handler for `GET /api/admin/stats`; returns a static dict with a hardcoded `active_users` count of 100.
<!-- trie:end -->
<!-- trie:section symbol=tests/fixtures/xlink_project/backend/api/admin:get_settings fingerprint=94d0e3350e633169f5b2bb5a40d4a96a5721d08f7317eec7f05e406345963c28 body_fp=24e72a6ca35f6662d20bd1cf2cdd43f89129b50eed641f2fd1a54c64ab22f29f source_ref=573c4a8064c1bcd39eb393877ec342e953ac35ee role=api -->
## `def get_settings()`

Flask `GET /api/admin/settings` handler returning a hardcoded settings payload.
<!-- trie:end -->
<!-- trie:section symbol=tests/fixtures/xlink_project/backend/api/admin:update_settings fingerprint=32045501f47a25841cef2ba47f2719f131e8c9ac0dcec0412ce1d16b0f696c16 body_fp=f0393a0a0dbadd9e9813dd8132c3dc15c0fe70e90eb9e5e8cb17676e3091ffaa source_ref=573c4a8064c1bcd39eb393877ec342e953ac35ee role=api -->
## `def update_settings(data: dict)`

Handle POST requests to `/api/admin/settings`, accepting a settings payload and returning a fixed acknowledgement dict.

- `data`: incoming settings payload; not validated or applied in this fixture implementation.
<!-- trie:end -->
<!-- trie:section symbol=tests/fixtures/xlink_project/backend/api/admin:bulk_update fingerprint=44bf31fe0aad84c4d11596499b513684d2edda0262853b15640f086158c9a3e9 body_fp=5369cc923a4fc662fa34476d3e685eea99aa06dc82d5ccbfcb27f44166f48476 source_ref=573c4a8064c1bcd39eb393877ec342e953ac35ee role=api -->
## `def bulk_update()`

Handle PUT requests to `/api/admin/bulk`, returning a fixed payload indicating 50 processed items.
<!-- trie:end -->
<!-- trie:section symbol=tests/fixtures/xlink_project/backend/api/admin:get_item fingerprint=4d9f0f8f14e370354bf40ca97bdd880340c3153c699a18ddc3d9721af8bee585 body_fp=384fed4140908be871a4c52d2816a2d683b23caa55fc52d59b32bb5f1c43a693 source_ref=573c4a8064c1bcd39eb393877ec342e953ac35ee role=api -->
## `def get_item(item_id: str)`

Return a JSON object containing the given `item_id` from the `/api/items/{item_id}` GET endpoint.
<!-- trie:end -->