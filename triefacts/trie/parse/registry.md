---
trie_version: 0.1.9
source: trie/parse/registry.py
file_fingerprint: 3731039df89a3839e1573e71cd6ab9e2fbe9876a59577add64cdba31d85a5a86
last_synced_at: '2026-06-17T16:41:55Z'
description: "Language-backend registry \u2014 dispatch by file extension."
defines:
- kind: module
  qualified_name: trie/parse/registry:__module__
  lines: 1-118
- kind: function
  qualified_name: trie/parse/registry:_build_registry
  lines: 24-36
- kind: constant
  qualified_name: trie/parse/registry:_BACKENDS
  lines: 39-39
- kind: constant
  qualified_name: trie/parse/registry:_BY_EXTENSION
  lines: 43-47
- kind: function
  qualified_name: trie/parse/registry:all_backends
  lines: 50-52
- kind: function
  qualified_name: trie/parse/registry:get_backend
  lines: 55-60
- kind: function
  qualified_name: trie/parse/registry:get_backend_for_file
  lines: 63-73
- kind: function
  qualified_name: trie/parse/registry:source_suffixes
  lines: 76-82
- kind: function
  qualified_name: trie/parse/registry:is_indexable
  lines: 85-87
- kind: function
  qualified_name: trie/parse/registry:extract_file_data
  lines: 90-104
- kind: function
  qualified_name: trie/parse/registry:extract_symbols
  lines: 107-117
incoming_refs: 21
outgoing_refs: 2
---
<!-- trie:section symbol=trie/parse/registry:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=564c5ea59f7a063651a525e0104d098afaccb1fadf02b5a8d84b5f1483f91a24 source_ref=eb8b31b98e0c496b7ffd217770dd85030edef53d role=orchestration -->
Language-backend registry that dispatches parse calls by file extension, with longest-suffix-first matching so compound suffixes like `.d.ts` win over `.ts`.

- `_BACKENDS`: ordered list of all registered `LanguageBackend` instances
- `_BY_EXTENSION`: flat `(ext, backend)` pairs sorted longest-suffix-first for unambiguous dispatch
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/registry:_build_registry fingerprint=e11a423230d9cda2e924a3320fd6a54bf1362630e01688865c125718c6bcba9c body_fp=abe3df0e066149b33d8641fa3eaa76244a389e41ebd29bdef3d112041abb75dd source_ref=eb8b31b98e0c496b7ffd217770dd85030edef53d role=config -->
Build and return the list of available `LanguageBackend` instances, appending `TypeScriptBackend` only if its module imports successfully.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/registry:_BACKENDS fingerprint=cb943c770b9c9cd8a3f06ee1677079c2d35811248d76740edc9daef7f4e6bcc4 body_fp=6ec23a6890c92487c52893eb8756cb7fe762e3f72e78f2e95c577a9325acc7a1 source_ref=eb8b31b98e0c496b7ffd217770dd85030edef53d role=config -->
Module-level list of all instantiated `LanguageBackend` objects, populated once at import time by `_build_registry()`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/registry:_BY_EXTENSION fingerprint=ae09c2267b43191b0386c7855cc8e7ee281fccca3b785754943a2161c5d067f2 body_fp=3cd517446feeff71b5b58b541ca1c6914cd0c85dd1e770aeac4dddb2645f5bb7 source_ref=eb8b31b98e0c496b7ffd217770dd85030edef53d role=config -->
Flat list of `(extension, backend)` pairs sorted by extension length descending, enabling longest-suffix-first dispatch.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/registry:all_backends fingerprint=9822a76f7176fe4a498ffd83a0e313486715cd754e2fab1607042eb76d6c5f8a body_fp=234fceb234d2b291f1e5c6210056a6d817c020f21f8575ec3932c3084468af89 source_ref=eb8b31b98e0c496b7ffd217770dd85030edef53d role=util -->
Return all registered `LanguageBackend` instances as a tuple.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/registry:get_backend fingerprint=9118a38b4eef13f5b282db7b2edef5cbc9c23352d028f400f86dcccd93c15663 body_fp=bb11a141ed61f2c8981e22ac0a4e0c4ba2c662715bef63a31c5ebc21f9be34cb source_ref=eb8b31b98e0c496b7ffd217770dd85030edef53d role=util -->
Return the registered `LanguageBackend` whose `name` matches the given string, or `None` if no backend matches.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/registry:get_backend_for_file fingerprint=ffdc08e85132d84ef027f4d5312fc2b59a26b3819245b67e78084e893a49ec71 body_fp=89032c1606713290e652c75bd9e8092739701022916d91e6c317519ec7a80c89 source_ref=eb8b31b98e0c496b7ffd217770dd85030edef53d role=util -->
Return the `LanguageBackend` that owns `path`'s extension, or `None` if no backend claims it.

- Matches longest suffix first, so `.d.ts` wins over `.ts`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/registry:source_suffixes fingerprint=6e8f412de8448f1e3e9d87363483344f83425e7a811edd966a702ebb7f474cb5 body_fp=a3ccd3806640edb80c99bc9b7c30565905ad46de56320e7f0a2ba502f7a69705 source_ref=eb8b31b98e0c496b7ffd217770dd85030edef53d role=util -->
Return all registered source suffixes ordered longest-first for triefact↔source path recovery.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/registry:is_indexable fingerprint=cdf7e81ad2821ec4a4f3d142b36046beb869504cc31aecc43caafd0b6dd3542c body_fp=8372d3572b9e488c8e43e4353da5c3dc5d9825818115b565b535763c51a585ef source_ref=eb8b31b98e0c496b7ffd217770dd85030edef53d role=util -->
Return `True` if any registered backend claims `path`'s file extension.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/registry:extract_file_data fingerprint=ecef07bb33418b374c79a28476d5caa71f68ed21737adc4ad7a5c19ced08837c body_fp=99aaa2a5db78201085fb44782d3cfdffaff2a5fe9403f0de8b9fded4a61a0a50 source_ref=eb8b31b98e0c496b7ffd217770dd85030edef53d role=orchestration -->
Dispatch `file_path` parsing to the owning backend and return a `FileData` object.

- `source_text`: optional pre-read source; skips filesystem read if provided.
- Raises `ValueError` if no backend claims the file's extension.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/registry:extract_symbols fingerprint=9814001a866105d512c0274107db3f4f74881d91ec000cc1851deb395f8d0ce2 body_fp=08d7a34463baf6e5d88b04dc28821400eb2be8792850103bc19173ab26c478f0 source_ref=eb8b31b98e0c496b7ffd217770dd85030edef53d role=parsing -->
Dispatch symbol extraction for `file_path` to the owning language backend.

- `file_path`: source file whose extension determines the backend.
- `source_text`: optional pre-read source; bypasses filesystem read if provided.
- Raises `ValueError` if no backend claims the file's extension.
<!-- trie:end -->