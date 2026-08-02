---
trie_version: 0.3.0
source: trie/refresh_lock.py
file_fingerprint: 140c55fdab29fb4933077e65b9b11f4bd24918a36163ec12d7ad1990745bac83
last_synced_at: '2026-06-03T21:14:40Z'
description: Mutual exclusion + coalescing queue for trie's write-side commands.
defines:
- kind: module
  qualified_name: trie/refresh_lock:__module__
  lines: 1-185
- kind: constant
  qualified_name: trie/refresh_lock:LOCK_FILENAME
  lines: 51-51
- kind: constant
  qualified_name: trie/refresh_lock:QUEUED_FILENAME
  lines: 52-52
- kind: constant
  qualified_name: trie/refresh_lock:LOCK_NAMES
  lines: 54-54
- kind: function
  qualified_name: trie/refresh_lock:_register_lock_name
  lines: 57-59
  signature: 'def _register_lock_name(name: str) -> None'
- kind: function
  qualified_name: trie/refresh_lock:lock_path
  lines: 65-70
  signature: 'def lock_path(project_root: Path, name: str = "refresh") -> Path'
- kind: function
  qualified_name: trie/refresh_lock:queued_path
  lines: 73-78
  signature: 'def queued_path(project_root: Path, name: str = "refresh") -> Path'
- kind: class
  qualified_name: trie/refresh_lock:LockHolder
  lines: 82-121
  signature: class LockHolder
- kind: method
  qualified_name: trie/refresh_lock:LockHolder.mark_queued
  lines: 96-104
  signature: def mark_queued(self) -> None
- kind: method
  qualified_name: trie/refresh_lock:LockHolder.consume_queued
  lines: 106-121
  signature: def consume_queued(self) -> bool
- kind: function
  qualified_name: trie/refresh_lock:try_acquire
  lines: 125-184
  signature: 'def try_acquire(project_root: Path, name: str = "refresh") -> Iterator[LockHolder]'
incoming_refs: 30
outgoing_refs: 0
---
<!-- trie:section symbol=trie/refresh_lock:__module__ fingerprint=105fd9e2cb19d65e5a58241b307951982df73a98eefe163e2ed77c7e28088af6 body_fp=4e213414784df03bbead654633c9eae91e21dd3d960ec808ec46fae447d5d69e source_ref=4f938fe8d35c1e2a4c3c1c2542008b437cfabcde role=change-detection -->
Implements mutual exclusion and coalescing for `trie refresh` processes to prevent racing on shared SQLite database and triefact tree.

- Uses file-based locking with `fcntl.flock()` for POSIX systems
- Coalesces multiple rapid refresh requests into single operations via sentinel files
- Lock automatically released on process exit including crashes
- Provides context manager interface for acquiring exclusive locks with non-blocking semantics
<!-- trie:end -->
<!-- trie:section symbol=trie/refresh_lock:LOCK_FILENAME fingerprint=296a1160b03c3354b363b929e63bc996a136b8fc4b15c4e01a9d2363b44aa28f body_fp=7932e513f1a2b764f95ad1a13ee1ab845934dc9fbf74d088672f951bb6b58e19 source_ref=4f938fe8d35c1e2a4c3c1c2542008b437cfabcde role=change-detection -->
Filename for the exclusive lock file used in mutual exclusion.
<!-- trie:end -->
<!-- trie:section symbol=trie/refresh_lock:QUEUED_FILENAME fingerprint=ac36b1424db45b3f82f1af66a5c5f5305cb7bade6e39d059b3d4185e5b40a632 body_fp=b390f803a01c1a6ddcf0d4b4e8b221c811dfa5d4c55b57ce7583f701bb6a0063 source_ref=4f938fe8d35c1e2a4c3c1c2542008b437cfabcde role=change-detection -->
String constant for the default queued sentinel filename `"refresh.queued"`.
<!-- trie:end -->
<!-- trie:section symbol=trie/refresh_lock:LOCK_NAMES fingerprint=c53f2ac7ddea965a4eba06568fa0a67759e9caed568f9374710e4d6f892b482b body_fp=dd881189578bbd5dd3eabe50bf27c75b70f7c04306288dd61edbb2b3411a6d3c source_ref=4f938fe8d35c1e2a4c3c1c2542008b437cfabcde role=change-detection -->
Registry of valid lock names for validation purposes.
<!-- trie:end -->
<!-- trie:section symbol=trie/refresh_lock:_register_lock_name fingerprint=17f91ff119b7aa625e8976c7fa00bfe70b5e5018e1e985de026dc83d32c30fa8 body_fp=27225606f75461dfe78c6005520f3a00d18d330501f3e778e0dcaafebbbe3b3e source_ref=4f938fe8d35c1e2a4c3c1c2542008b437cfabcde role=change-detection -->
## `def _register_lock_name(name: str) -> None`

Adds a lock name to the global `LOCK_NAMES` set for validation purposes.
<!-- trie:end -->
<!-- trie:section symbol=trie/refresh_lock:lock_path fingerprint=c610e86a3f8542a0e1e182730727359ea33d3ac720a46ed3f5f681146368091f body_fp=faac89e3e0d971a8af65fe9fdab796fc536cf18ba291d98a6d3599f542800da0 source_ref=4f938fe8d35c1e2a4c3c1c2542008b437cfabcde role=change-detection -->
## `def lock_path(project_root: Path, name: str = "refresh") -> Path`

Returns the path to a named lock file under the project's `.trie/` directory.

- `name`: Determines the lock filename (e.g., "refresh" → "refresh.lock", "apply" → "apply.lock")
<!-- trie:end -->
<!-- trie:section symbol=trie/refresh_lock:queued_path fingerprint=68114fd059c6f0347ee6f892e273a22863abb4039065b72f3256a6e2f6ca2137 body_fp=206cd6d471570b827c109dd9b217b3661a6d4ac3d418c0dc462a5ffceddb4d22 source_ref=4f938fe8d35c1e2a4c3c1c2542008b437cfabcde role=change-detection -->
## `def queued_path(project_root: Path, name: str = "refresh") -> Path`

Returns the path to the queued sentinel file for a given lock name under the `.trie/` directory.

• `name`: determines the filename suffix (e.g., "refresh" → "refresh.queued")
<!-- trie:end -->
<!-- trie:section symbol=trie/refresh_lock:LockHolder fingerprint=b55694a146f40bf55285a276cd4df716502c440e040bb4cf4fde471f11a8b1bf body_fp=55d5b337fbfb417eaa54ba9557ab7c75e3d8b83523fbb1a86b3921be6ac5dd77 source_ref=4f938fe8d35c1e2a4c3c1c2542008b437cfabcde role=change-detection -->
## `class LockHolder`

Handle to an acquired or contested refresh lock enabling mutual exclusion with coalescing.

- `acquired`: whether this process holds the lock vs. needs to queue
- `mark_queued()`: creates sentinel file to request another refresh pass (no-op if not acquired)
- `consume_queued()`: removes and returns existence of queued sentinel (false if not acquired)
<!-- trie:end -->
<!-- trie:section symbol=trie/refresh_lock:LockHolder.mark_queued fingerprint=9aed2862bedff649eb249383557d2cddd31ef4a4a00c4933e32ba9521edb4857 body_fp=bdc73c68ebe6bad4833a86c12acaa507694954110db758621fc820c7041e19f7 source_ref=4f938fe8d35c1e2a4c3c1c2542008b437cfabcde role=change-detection -->
## `def mark_queued(self) -> None`

Writes a queued sentinel file to signal that another refresh operation is wanted.

- Only effective when `LockHolder.acquired` is `False` (contention case)
- Creates `.trie/{name}.queued` file under the project root
- Idempotent: multiple calls have same effect as single call
<!-- trie:end -->
<!-- trie:section symbol=trie/refresh_lock:LockHolder.consume_queued fingerprint=fb0387219d5a28f6c9e532241df5b67970a48d1252b5698e377364d9dcbebdd5 body_fp=3285ef73a5fc462dd5979b5a68dcf281e431d3ffb2874405394841fc4c091dd8 source_ref=4f938fe8d35c1e2a4c3c1c2542008b437cfabcde role=change-detection -->
## `def consume_queued(self) -> bool`

Checks for and removes the queued sentinel file, returning whether one existed.

- Returns `False` immediately if `LockHolder` doesn't hold the lock
- Returns `True` if sentinel file was found and successfully deleted
<!-- trie:end -->
<!-- trie:section symbol=trie/refresh_lock:try_acquire fingerprint=505f7d32ed2a79bce34da78a62c7a116f27146d64b62ffa5b247928d7f5b7179 body_fp=3decd9db5b5252a1110703b7022956786b68a97dbe1e4d4d1cb482b723f75836 source_ref=4f938fe8d35c1e2a4c3c1c2542008b437cfabcde role=change-detection -->
## `def try_acquire(project_root: Path, name: str = "refresh") -> Iterator[LockHolder]`

Try to acquire an exclusive file lock without blocking and yield a LockHolder.

- `name`: lock file suffix (e.g., "refresh" → "refresh.lock") 
- Returns LockHolder with `acquired=True` if lock won, `acquired=False` if contested
- Automatically releases lock on context exit if acquired
- Creates `.trie/` directory and lock file if they don't exist
<!-- trie:end -->