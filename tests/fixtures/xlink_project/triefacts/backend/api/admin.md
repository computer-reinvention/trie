---
trie_version: 0.3.0
source: backend/api/admin.py
file_fingerprint: 5b38d204aa79f4d10a80f329a7decc4feb93e8384e207a22f015a9b910f2643c
last_synced_at: '2026-08-30T02:43:02Z'
defines:
- kind: constant
  qualified_name: backend/api/admin:app
  lines: 5-5
- kind: constant
  qualified_name: backend/api/admin:bp
  lines: 6-6
- kind: function
  qualified_name: backend/api/admin:get_stats
  lines: 10-11
  signature: def get_stats()
- kind: function
  qualified_name: backend/api/admin:get_settings
  lines: 15-16
  signature: def get_settings()
- kind: function
  qualified_name: backend/api/admin:update_settings
  lines: 20-21
  signature: 'def update_settings(data: dict)'
- kind: function
  qualified_name: backend/api/admin:bulk_update
  lines: 25-26
  signature: def bulk_update()
- kind: function
  qualified_name: backend/api/admin:get_item
  lines: 30-31
  signature: 'def get_item(item_id: str)'
incoming_refs: 0
outgoing_refs: 0
---
<!-- trie:section symbol=backend/api/admin:app fingerprint=2308bba0f2b72b9f8aa6cd409f3330a47076395b828b6d670ff58ae1bcc72725 body_fp=47ef9dc99872aa66a80ae77f13b28b1149529ae7ab562d564200c9e09e2209d8 source_ref=573c4a8064c1bcd39eb393877ec342e953ac35ee role=entrypoint -->
Flask application instance serving as the root HTTP server for admin API endpoints.

- Decorated with `@app.route`, `@app.get`, `@app.post` to register handlers for `/api/admin/*` and `/api/items/*` paths.
<!-- trie:end -->
<!-- trie:section symbol=backend/api/admin:bp fingerprint=d0c16be46641d2344840f64cdb1b8e643ab5d50d15262d4adbd2f34f5e3e9307 body_fp=da39fe764e5a29f0403ece0eb3de5a6fe30e089ec669042e13851d3bdc9347ce source_ref=573c4a8064c1bcd39eb393877ec342e953ac35ee role=config -->
Blueprint instance for admin routes, named `"admin"` with module-level package context.

- Serves as a namespace for route handlers (e.g. `bulk_update()`) registered via `@bp.route()`.
<!-- trie:end -->
<!-- trie:section symbol=backend/api/admin:get_stats fingerprint=b506b954cfbb2a3121e8e3a64327b8f4a327c7b45ab51b499227d42bbfcc2bf9 body_fp=c8ac9562875082df0cb1cc861154531c853783d0202b1400c375a5d58f452819 source_ref=573c4a8064c1bcd39eb393877ec342e953ac35ee role=api -->
## `def get_stats()`

Returns active user count as a dictionary.

- **boundary:** entry
- **role:** api
<!-- trie:end -->
<!-- trie:section symbol=backend/api/admin:get_settings fingerprint=94d0e3350e633169f5b2bb5a40d4a96a5721d08f7317eec7f05e406345963c28 body_fp=c02e51be5d7bbbd38b0ccbdf05fb41f67cb56bac51f17286cedee03531dc912d source_ref=573c4a8064c1bcd39eb393877ec342e953ac35ee role=api -->
## `def get_settings()`

GET handler registered at `/api/admin/settings` that returns the current admin settings.

- Returns a dict with `theme` set to "dark".
<!-- trie:end -->
<!-- trie:section symbol=backend/api/admin:update_settings fingerprint=32045501f47a25841cef2ba47f2719f131e8c9ac0dcec0412ce1d16b0f696c16 body_fp=afa7e790fa627a212a24c672d5e1eaccd28cbb192df77441b045e9108276b145 source_ref=573c4a8064c1bcd39eb393877ec342e953ac35ee role=api -->
## `def update_settings(data: dict)`

Updates admin settings and returns a confirmation response.

- `data`: dictionary of settings key-value pairs to apply.
<!-- trie:end -->
<!-- trie:section symbol=backend/api/admin:bulk_update fingerprint=44bf31fe0aad84c4d11596499b513684d2edda0262853b15640f086158c9a3e9 body_fp=de28178c26954b723009f98be8034859bb601368c3227c5da13c734914e2ff21 source_ref=573c4a8064c1bcd39eb393877ec342e953ac35ee role=api -->
## `def bulk_update()`

Handles PUT requests to `/api/admin/bulk` and returns a JSON response with the count of processed items.
<!-- trie:end -->
<!-- trie:section symbol=backend/api/admin:get_item fingerprint=4d9f0f8f14e370354bf40ca97bdd880340c3153c699a18ddc3d9721af8bee585 body_fp=a439b8ff1a17db7ecae4b58e57b618549dc9ae70e51ef1ea41a0c2225f721870 source_ref=573c4a8064c1bcd39eb393877ec342e953ac35ee role=api -->
## `def get_item(item_id: str)`

Handles GET requests to `/api/items/{item_id}`, returning the item's ID as a JSON object.

- `item_id`: path parameter capturing the item identifier from the URL
<!-- trie:end -->