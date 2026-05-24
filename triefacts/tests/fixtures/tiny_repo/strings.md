---
trie_version: 0.1.2
source: tests/fixtures/tiny_repo/strings.py
file_fingerprint: 0830b9bb0e7a6ca8e4f734e7f28e3ad7abf16f56e057f617a390052217e059fd
last_synced_at: '2026-05-23T23:54:49Z'
description: String manipulation helpers.
defines:
- kind: function
  qualified_name: tests/fixtures/tiny_repo/strings:shout
  lines: 4-6
- kind: function
  qualified_name: tests/fixtures/tiny_repo/strings:whisper
  lines: 9-11
incoming_refs: 0
outgoing_refs: 0
---
<!-- trie:section symbol=tests/fixtures/tiny_repo/strings:shout fingerprint=1d10d56594df40a91357c18f7f14b9551ccd74b0de1de3d68a296802a3f94094 body_fp=f4ebe85ca91174d660c09e7cafef6faf8d7e0ea6ad803b9710e1eaa6697b54f9 source_ref=bb1fd351d835d5ee9516479bac7a26c3c2541488 -->
## `shout(s: str) -> str`

Uppercase a string and append an exclamation mark.
<!-- trie:end -->
<!-- trie:section symbol=tests/fixtures/tiny_repo/strings:whisper fingerprint=f351c011a0fdd6ad18e98a2adef4f29d680d8f31fe7c50ca721b49012c6f7d8e body_fp=c889d69d535c95f17647404c6dcc3d6816be08aba168faef5aa201673a0bdcfb source_ref=bb1fd351d835d5ee9516479bac7a26c3c2541488 -->
## `whisper(s: str) -> str`

Lowercase a string.
<!-- trie:end -->