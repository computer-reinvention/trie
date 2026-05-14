---
trie_version: 0.1.0
source: trie/sync/writer.py
file_fingerprint: ef0d50aaeba69ca5dd066d04d02d2fbdb81aa8ee81598d628b3c7917576b5bc1
last_synced_at: '2026-05-14T17:52:20Z'
defines:
- kind: function
  qualified_name: trie/sync/writer:hash_body
  lines: 39-46
- kind: function
  qualified_name: trie/sync/writer:extract_one_liner
  lines: 53-84
- kind: class
  qualified_name: trie/sync/writer:Section
  lines: 88-92
- kind: class
  qualified_name: trie/sync/writer:Prose
  lines: 96-97
- kind: class
  qualified_name: trie/sync/writer:TriefactFile
  lines: 104-238
- kind: method
  qualified_name: trie/sync/writer:TriefactFile.parse
  lines: 109-155
- kind: method
  qualified_name: trie/sync/writer:TriefactFile.empty
  lines: 158-159
- kind: method
  qualified_name: trie/sync/writer:TriefactFile.get_section
  lines: 163-167
- kind: method
  qualified_name: trie/sync/writer:TriefactFile.section_qnames
  lines: 169-170
- kind: method
  qualified_name: trie/sync/writer:TriefactFile.upsert_section
  lines: 174-190
- kind: method
  qualified_name: trie/sync/writer:TriefactFile.remove_section
  lines: 192-197
- kind: method
  qualified_name: trie/sync/writer:TriefactFile.render
  lines: 214-238
incoming_refs: 42
outgoing_refs: 0
---
<!-- trie:section symbol=trie/sync/writer:hash_body fingerprint=ab22edfb13d8ba9c75b86d2384923163f1c839f46c4a2ed06ca566491fc6f96d body_fp=0de3381420da9676c033051fdc133810f7a1c28e8d85b6002595ede10e6fca9f -->
## `hash_body(body: str) -> str`

Compute SHA-256 hex digest of `body` after stripping leading/trailing whitespace.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/writer:extract_one_liner fingerprint=fb87254713b9705aec49bf5aaed06df13d5765c8d66d19dd661b746b0045cd82 body_fp=290fe67ce73d2d8429b001f953e89152d9e6beb0eedf927b563fc70e83f1ebc3 -->
## `extract_one_liner(body: str, *, max_chars: int = 200) -> str`

Pull the first sentence from a section body, skipping any leading heading line.

- `body`: expected shape `## signature\n\n<prose...>`
- Returns `""` if no usable text is found.
- Truncates to `max_chars`, appending `…` if trimmed.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/writer:Section fingerprint=f2f71e742865948a573388a17b2da7e5f769cf5cd515c61388c799173c8f9c42 body_fp=ca0ebc331da8eae8d193a081fe666cc0be5e41329ee3ca638e9711c93f8d1d73 -->
## `Section(qualified_name: str, fingerprint: str, body: str, body_fingerprint: str | None = None)`

Frozen dataclass representing a parsed trie-managed documentation section.

- `fingerprint`: SHA-256 over the normalized source symbol body.
- `body`: text between sentinels, leading/trailing newlines stripped.
- `body_fingerprint`: SHA-256 over `body`; `None` for legacy sections written by trie ≤ 0.1.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/writer:Prose fingerprint=cf49910dc87437bc09897192fbd13b0a347f9433a85c94f1e599b18c7eceaf2b body_fp=09d5f56b09541d023bb4693ded2537daf14cb2f268ba7bb8c76e36d6c6c2668a -->
## `Prose(text: str)`

Represent a verbatim human-prose chunk between (or outside) trie-managed sections.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/writer:TriefactFile fingerprint=a3d8d2f852ee36118154f5b25442bc8c8803a4dab7494126ea6163cf3f4c904b body_fp=e0c3aeeca05d0b135b5e4fe81b4ed572d1559e128bdc36c4db751c623b350f25 -->
## `TriefactFile(front_matter={}, chunks=[])`

Parse, mutate, and render a trie-managed Markdown file containing prose and documented sections.

- `front_matter`: YAML dict from the file's `---` block.
- `chunks`: ordered list of `Section` and `Prose` segments.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/writer:TriefactFile.parse fingerprint=b1813f995532190754d866fe91682cf1e0252a576ca5f7bbde226e8190300d78 body_fp=91c64e2b03f2f25efb9c5ab27bcc1ba6c4dabe0910e2919904e25149601a9e86 -->
## `TriefactFile.parse(cls, text: str) -> TriefactFile`

Parse a raw Markdown string into a `TriefactFile` with front-matter and ordered chunks.

- `text`: full file contents including optional YAML front matter and trie sections
- Raises `ValueError` if any `trie:section` open sentinel has no matching close sentinel
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/writer:TriefactFile.empty fingerprint=cc0676809bee8efb34856efbd9c950ae148db930ab90e76ebd3d17bd1eefbc7e body_fp=2d7abfcc086c70f09b233627e294123f6a759a2dc9c4285d7e79057a0171859a -->
## `empty(cls) -> TriefactFile`

Return a new, empty `TriefactFile` with no front matter and no chunks.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/writer:TriefactFile.get_section fingerprint=aec43c04e2eaaaaf39f4d6be228e0198afa191d15abda68a3879b41b391204d8 body_fp=07a32b37205ea3b4c1c6c6c1e092bbab7de0c13747057df82a3086bfcdc8b9da -->
## `get_section(self, qualified_name: str) -> Section | None`

Return the first `Section` chunk matching `qualified_name`, or `None` if absent.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/writer:TriefactFile.section_qnames fingerprint=b3198e06079669f9cdabe77cd2292e047d5fc68e79e8ecb7e0a9f7bff28f0f60 body_fp=b3b9c109054c842ed01fe3225fd3ea67edafe9ff262442247a21787053010117 -->
## `section_qnames(self) -> list[str]`

Return qualified names of all `Section` chunks in order.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/writer:TriefactFile.upsert_section fingerprint=2bdb1c4090ef7afade75d9ea2851c9b36b91f9bad036102163b078da3f1e7d74 body_fp=4b0e865b978286c8fb7c8c24f61a6a0c64d5714b85ea097adc7430984e4388e0 -->
## `upsert_section(self, *, qualified_name: str, fingerprint: str, body: str) -> None`

Replace an existing section by qualified name, or append a new one at the end.

- `body_fingerprint` is computed automatically via `hash_body`; callers must not supply it.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/writer:TriefactFile.remove_section fingerprint=d8dc7a57db15d5144ac0f1cb113b03fbe74d7608b5e9b23572384079c5ce8032 body_fp=ed06efe2861bff7fee3d30b23d4411a099b7b4381fdbeaf991f7c5a52d51abd8 -->
## `remove_section(self, qualified_name: str) -> bool`

Remove the first section matching `qualified_name` from `chunks`; return `True` if found, `False` otherwise.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/writer:TriefactFile.render fingerprint=dea4d47b10b50a3354eee144920010c5bcb18792813b3e74516e76c8bf21b57c body_fp=6bdfc595614b20388322b7934dba7be2dbb09b23fdaec7716eec38b796cce5aa -->
## `render(self) -> str`

Serialize the `TriefactFile` to a Markdown string with front matter and trie sentinel-delimited sections.

- Always emits `body_fp=` on every section, hashing legacy sections on the fly.
<!-- trie:end -->