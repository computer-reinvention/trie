---
trie_version: 0.1.2
source: trie/refresh_lock.py
file_fingerprint: 61056ade51e9c5714da16cd2dd35c2b8ff75a5c2f11dfbe5a5a9d160fa32419b
last_synced_at: '2026-05-19T10:41:40Z'
description: Mutual exclusion + coalescing queue for `trie refresh`.
defines:
- kind: module
  qualified_name: trie/refresh_lock:__module__
  lines: 1-176
- kind: constant
  qualified_name: trie/refresh_lock:LOCK_FILENAME
  lines: 51-51
- kind: constant
  qualified_name: trie/refresh_lock:QUEUED_FILENAME
  lines: 52-52
- kind: function
  qualified_name: trie/refresh_lock:lock_path
  lines: 55-57
- kind: function
  qualified_name: trie/refresh_lock:queued_path
  lines: 60-62
- kind: class
  qualified_name: trie/refresh_lock:LockHolder
  lines: 66-117
- kind: method
  qualified_name: trie/refresh_lock:LockHolder.mark_queued
  lines: 79-94
- kind: method
  qualified_name: trie/refresh_lock:LockHolder.consume_queued
  lines: 96-117
- kind: function
  qualified_name: trie/refresh_lock:try_acquire
  lines: 121-175
incoming_refs: 20
outgoing_refs: 0
---
<!-- trie:section symbol=trie/refresh_lock:lock_path fingerprint=fa3088fd68739b854180275954958c8a963a73e37727f2320f06ad463de967ae body_fp=8b9866bc4f1e921021af794e232c499c3c8796ec1dc784c5e3aa63c1f1f3a812 source_ref=6b6fb8bf76ce617c5f239ce25cd25d4c0c1b377d -->
## `lock_path(project_root: Path) -> Path`

Return the conventional path to the refresh lock file under `<project_root>/.trie/`.
<!-- trie:end -->

<!-- trie:section symbol=trie/refresh_lock:queued_path fingerprint=95879d8bf8bf8e968c77a60ea271e4ae651e7c92546d422b5101977181858495 body_fp=6af725a0b1a78080e153d2639520dfabac4b3d35b040a042775fa565af3eb003 source_ref=6b6fb8bf76ce617c5f239ce25cd25d4c0c1b377d -->
## `queued_path(project_root: Path) -> Path`

Return the conventional path of the queued sentinel file under `.trie/`.
<!-- trie:end -->

<!-- trie:section symbol=trie/refresh_lock:LockHolder fingerprint=e439d723dd88420de64af59d7f5afb1254d78ef77abaefa15688d43e6a1bcc91 body_fp=5393eea647d2539f55f1db284e538c5945c26cd3a755e01f965b54d9d5aa6ab8 source_ref=6b6fb8bf76ce617c5f239ce25cd25d4c0c1b377d -->
## `LockHolder(project_root: Path, acquired: bool, _fd: IO[bytes] | None = None)`

Handle returned by `try_acquire`; lets callers branch on lock ownership and manage the queued-refresh sentinel.

- `acquired`: `True` if this process holds the exclusive lock.
- `mark_queued()`: creates the sentinel file; no-op if already acquired.
- `consume_queued()`: removes sentinel and returns `True` if a queued refresh was pending; only meaningful when `acquired` is `True`.
<!-- trie:end -->

<!-- trie:section symbol=trie/refresh_lock:LockHolder.mark_queued fingerprint=3617b6220645cf133dc03e1790150b06f1ba85993dfb1a164ab33719285eef3a body_fp=09bb23a9b2b80da33838e91b84d0862bc6c2764fc78da595cf427a30b4e611aa source_ref=6b6fb8bf76ce617c5f239ce25cd25d4c0c1b377d -->
## `mark_queued(self) -> None`

Touch the queued-sentinel file to signal the lock holder that another refresh is wanted.

- Only creates the sentinel when `acquired` is `False`.
<!-- trie:end -->

<!-- trie:section symbol=trie/refresh_lock:LockHolder.consume_queued fingerprint=631fb126c50921f21ab18ff51f25092d1fe0a61275f82801982e65ae117f7f65 body_fp=edfed8b91ed909e53f8bbe0c5b762b5f35919b6ec0d5816d4ae5e66d021a5137 source_ref=6b6fb8bf76ce617c5f239ce25cd25d4c0c1b377d -->
## `consume_queued(self) -> bool`

Atomically check and clear the queued-refresh sentinel, returning `True` if a tail pass is needed.

- Only callable safely while holding the exclusive flock.
- Returns `False` if not the lock holder or sentinel absent.
<!-- trie:end -->

<!-- trie:section symbol=trie/refresh_lock:try_acquire fingerprint=f8de1fece64c1bcb8892f7b44b2af75e6f447096db53f0ede3a47034ab8b659d body_fp=18977817bfbfb9681e430bfdf335a964c8dd0ce1b0a7aaa3c4ee63aba246469d source_ref=6b6fb8bf76ce617c5f239ce25cd25d4c0c1b377d -->
## `try_acquire(project_root: Path) -> Iterator[LockHolder]`

Context-manager that non-blockingly attempts an exclusive `flock` on the refresh lock file, yielding a `LockHolder` indicating success or contention.

- `acquired=True`: caller holds the lock; fd is closed on context exit.
- `acquired=False`: another process holds the lock; no fd to clean up.
- Raises any `OSError` that isn't `EAGAIN`/`EWOULDBLOCK`.
<!-- trie:end -->

<!-- trie:section symbol=trie/refresh_lock:LOCK_FILENAME fingerprint=296a1160b03c3354b363b929e63bc996a136b8fc4b15c4e01a9d2363b44aa28f body_fp=51208f7a3f2857c13bf1c1251d5a418943b025c24d2eebb3679681fa1d48284f source_ref=6b6fb8bf76ce617c5f239ce25cd25d4c0c1b377d -->
## `LOCK_FILENAME = "refresh.lock"`

Filename of the on-disk exclusive lock file inside `.trie/`.
<!-- trie:end -->

<!-- trie:section symbol=trie/refresh_lock:QUEUED_FILENAME fingerprint=ac36b1424db45b3f82f1af66a5c5f5305cb7bade6e39d059b3d4185e5b40a632 body_fp=2511dc591c71f64bff439bd97b8d911c35b28e65fb42b33e8a224568329a34d3 source_ref=6b6fb8bf76ce617c5f239ce25cd25d4c0c1b377d -->
## `QUEUED_FILENAME = "refresh.queued"`

Filename of the boolean sentinel that signals a pending coalesced refresh request.
<!-- trie:end -->

<!-- trie:section symbol=trie/refresh_lock:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=e6f5d768cf9cb861a4701f5509f2a2763df2eb8de7786108d8e6b988ac9ea044 source_ref=6b6fb8bf76ce617c5f239ce25cd25d4c0c1b377d -->
## `refresh_lock`

Provide mutual-exclusion and coalescing-queue primitives for concurrent `trie refresh` processes on POSIX systems.

- `try_acquire`: context manager yielding a `LockHolder`; non-blocking flock
- `LockHolder.acquired`: `True` if this process won the exclusive lock
- `LockHolder.mark_queued`: called by losers to request a follow-up pass
- `LockHolder.consume_queued`: called by winner to drain the sentinel and loop
<!-- trie:end -->