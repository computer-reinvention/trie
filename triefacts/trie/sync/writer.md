---
trie_version: 0.1.0
source: trie/sync/writer.py
file_fingerprint: e2b88d0d2e940ec7989830064b4f7888d2f3938d7875295798c2b75ad91ff20c
last_synced_at: '2026-05-12T18:28:07Z'
defines:
- kind: function
  qualified_name: trie/sync/writer:hash_body
  lines: 34-41
- kind: class
  qualified_name: trie/sync/writer:Section
  lines: 45-49
- kind: class
  qualified_name: trie/sync/writer:Prose
  lines: 53-54
- kind: class
  qualified_name: trie/sync/writer:TriefactFile
  lines: 61-189
- kind: method
  qualified_name: trie/sync/writer:TriefactFile.parse
  lines: 66-106
- kind: method
  qualified_name: trie/sync/writer:TriefactFile.empty
  lines: 109-110
- kind: method
  qualified_name: trie/sync/writer:TriefactFile.get_section
  lines: 114-118
- kind: method
  qualified_name: trie/sync/writer:TriefactFile.section_qnames
  lines: 120-121
- kind: method
  qualified_name: trie/sync/writer:TriefactFile.upsert_section
  lines: 125-141
- kind: method
  qualified_name: trie/sync/writer:TriefactFile.remove_section
  lines: 143-148
- kind: method
  qualified_name: trie/sync/writer:TriefactFile.render
  lines: 165-189
incoming_refs: 41
outgoing_refs: 0
---
<!-- trie:section symbol=trie/sync/writer:hash_body fingerprint=ab22edfb13d8ba9c75b86d2384923163f1c839f46c4a2ed06ca566491fc6f96d body_fp=6766cc72874c8c5f9df3663f255c190a7200cfc806b2cea5385af43759dfe4dc -->
## `hash_body(body: str) -> str`

Compute SHA-256 of a section body with leading/trailing whitespace stripped.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/writer:Section fingerprint=f2f71e742865948a573388a17b2da7e5f769cf5cd515c61388c799173c8f9c42 body_fp=5928ca4870f9dde174a02eea3aa9ef264bff7fc5e630fbf36d38c062c7fce13f -->
## `Section(qualified_name: str, fingerprint: str, body: str, body_fingerprint: str | None = None)`

Immutable dataclass representing one trie-managed documentation section parsed from a triefact file.

- `fingerprint`: SHA-256 of the source symbol body at sync time.
- `body`: text between sentinels, leading/trailing newlines stripped.
- `body_fingerprint`: SHA-256 of `body`; `None` for legacy sections lacking `body_fp`.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/writer:Prose fingerprint=cf49910dc87437bc09897192fbd13b0a347f9433a85c94f1e599b18c7eceaf2b body_fp=65a9906315d429e168fffda99b47648f8109f2466959a8987c066a7c5281591b -->
## `Prose(text: str)`

Immutable chunk representing human-written Markdown content preserved verbatim between trie sections.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/writer:TriefactFile fingerprint=5d30448fbf88903aef7acae2627a565e8a19ea1cd838a18ce1cf031d36133505 body_fp=86aefc9b4c6d741900a9682396a54ab9856a70e65f2619bb024fc647383c3377 -->
## `TriefactFile(front_matter={}, chunks=[])`

Parse, mutate, and render a trie-managed Markdown file containing `Section` and `Prose` chunks.

- `front_matter`: YAML front matter as a dict, preserved on render.
- `chunks`: ordered mix of `Section` and `Prose` blocks.
- `parse(text)`: deserializes full file text including front matter and all sentinels.
- `upsert_section`: replaces existing section or appends; auto-computes `body_fingerprint`.
- `remove_section`: returns `False` if qualified name not found.
- `render()`: emits valid Markdown with sentinel comments; always writes `body_fp=`.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/writer:TriefactFile.parse fingerprint=3be5e2c7a3017435762be997134f13559c76a6b92fc0bb7d33ac4fe0922a6781 body_fp=7e442e39b3e076db3ae0446599f30094b74fec79df70117b920362a151c52906 -->
## `TriefactFile.parse(cls, text: str) -> TriefactFile`

Parse a Markdown string into a `TriefactFile` with optional YAML front matter and a sequence of `Section`/`Prose` chunks.

- `text`: raw Markdown content of a triefact file
- Raises `ValueError` if a `trie:section` open sentinel has no matching close sentinel
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/writer:TriefactFile.empty fingerprint=cc0676809bee8efb34856efbd9c950ae148db930ab90e76ebd3d17bd1eefbc7e body_fp=41048221a012d369d2446ee8fef05446af2ac024df4ca997da6c5a1e758df6c1 -->
## `empty(cls) -> TriefactFile`

Return a new empty `TriefactFile` with no front matter and no chunks.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/writer:TriefactFile.get_section fingerprint=aec43c04e2eaaaaf39f4d6be228e0198afa191d15abda68a3879b41b391204d8 body_fp=32eedbbfb4497f08444162f2ca01c9fee3e8538c61410a47930655f6d49be9f2 -->
## `get_section(self, qualified_name: str) -> Section | None`

Return the first `Section` matching `qualified_name`, or `None` if absent.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/writer:TriefactFile.section_qnames fingerprint=b3198e06079669f9cdabe77cd2292e047d5fc68e79e8ecb7e0a9f7bff28f0f60 body_fp=b66f9e5134c9d610bf0cfee8cb8aeb5685a0911f6aa446b3d587dc1eeb3e41d6 -->
## `section_qnames(self) -> list[str]`

Return the qualified names of all `Section` chunks in order.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/writer:TriefactFile.upsert_section fingerprint=2bdb1c4090ef7afade75d9ea2851c9b36b91f9bad036102163b078da3f1e7d74 body_fp=4b0e865b978286c8fb7c8c24f61a6a0c64d5714b85ea097adc7430984e4388e0 -->
## `upsert_section(self, *, qualified_name: str, fingerprint: str, body: str) -> None`

Replace an existing section by qualified name, or append a new one at the end.

- `body_fingerprint` is computed automatically via `hash_body`; callers must not supply it.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/writer:TriefactFile.remove_section fingerprint=d8dc7a57db15d5144ac0f1cb113b03fbe74d7608b5e9b23572384079c5ce8032 body_fp=5d155eed1f0af1c371c0009a78b5161c4883d2e7c1c257daab117f1112e19e23 -->
## `remove_section(self, qualified_name: str) -> bool`

Remove the first section matching `qualified_name`; return `True` if found and deleted, `False` otherwise.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/writer:TriefactFile.render fingerprint=dea4d47b10b50a3354eee144920010c5bcb18792813b3e74516e76c8bf21b57c body_fp=b8d5aeb32dc9a3b2652a6bb73e8f2b841a2672560d24ca2b4e83981507fd16d0 -->
## `render(self) -> str`

Serialize the `TriefactFile` to a Markdown string with front matter and trie sentinel comments.

- Always emits `body_fp=` on every section, upgrading legacy sections in-place.
<!-- trie:end -->