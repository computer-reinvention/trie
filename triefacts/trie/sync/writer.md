---
trie_version: 0.1.0
source: trie/sync/writer.py
file_fingerprint: b8cd8fce625c54ece164fd84fda87eb570039e64550a7fa886889fc3d3f227dd
last_synced_at: '2026-05-14T17:22:44Z'
defines:
- kind: function
  qualified_name: trie/sync/writer:hash_body
  lines: 34-41
- kind: function
  qualified_name: trie/sync/writer:extract_one_liner
  lines: 48-79
- kind: class
  qualified_name: trie/sync/writer:Section
  lines: 83-87
- kind: class
  qualified_name: trie/sync/writer:Prose
  lines: 91-92
- kind: class
  qualified_name: trie/sync/writer:TriefactFile
  lines: 99-227
- kind: method
  qualified_name: trie/sync/writer:TriefactFile.parse
  lines: 104-144
- kind: method
  qualified_name: trie/sync/writer:TriefactFile.empty
  lines: 147-148
- kind: method
  qualified_name: trie/sync/writer:TriefactFile.get_section
  lines: 152-156
- kind: method
  qualified_name: trie/sync/writer:TriefactFile.section_qnames
  lines: 158-159
- kind: method
  qualified_name: trie/sync/writer:TriefactFile.upsert_section
  lines: 163-179
- kind: method
  qualified_name: trie/sync/writer:TriefactFile.remove_section
  lines: 181-186
- kind: method
  qualified_name: trie/sync/writer:TriefactFile.render
  lines: 203-227
incoming_refs: 42
outgoing_refs: 0
---
<!-- trie:section symbol=trie/sync/writer:hash_body fingerprint=ab22edfb13d8ba9c75b86d2384923163f1c839f46c4a2ed06ca566491fc6f96d body_fp=ff4cc0d8d37a35d35446d795e12b6d335ea4491d8f9b3e64ac1d995839f65670 -->
## `hash_body(body: str) -> str`

Compute SHA-256 over a section body with leading/trailing whitespace stripped.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/writer:extract_one_liner fingerprint=fb87254713b9705aec49bf5aaed06df13d5765c8d66d19dd661b746b0045cd82 body_fp=fbe02250065df6f7d871cc24064a6213d4ab39fdc6fc1bee8820723590acf04b -->
## `extract_one_liner(body: str, *, max_chars: int = 200) -> str`

Extract the first sentence from a section body, skipping any leading heading line.

- `body`: expected shape `## signature\n\n<prose...>`
- Returns `""` if no usable text is found.
- Truncates to `max_chars`, appending `…` if clipped.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/writer:Section fingerprint=f2f71e742865948a573388a17b2da7e5f769cf5cd515c61388c799173c8f9c42 body_fp=a71a255b8f244da91764d8396b6b478e5e564e330a94f2c0b991a7640997404b -->
## `Section(qualified_name: str, fingerprint: str, body: str, body_fingerprint: str | None = None)`

Frozen dataclass representing one trie-managed documentation section parsed from a triefact file.

- `fingerprint`: SHA-256 of the source symbol body at sync time.
- `body`: text between sentinels, leading/trailing newlines stripped.
- `body_fingerprint`: SHA-256 of `body`; `None` for legacy sections written before trie 0.2.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/writer:Prose fingerprint=cf49910dc87437bc09897192fbd13b0a347f9433a85c94f1e599b18c7eceaf2b body_fp=627c075e9a38fbce5f6f638cd517e5092b277a7fd6fbc23042bad0c4eb735bd1 -->
## `Prose(text: str)`

Represent a verbatim human-prose chunk between (or outside) trie sections.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/writer:TriefactFile fingerprint=5d30448fbf88903aef7acae2627a565e8a19ea1cd838a18ce1cf031d36133505 body_fp=ccdc43d8b00e1484b7c1b7ab66d8b49af836def458a30f3f8be119e6b463dfd7 -->
## `TriefactFile(front_matter: dict[str, Any], chunks: list[Chunk])`

Parse, mutate, and render a trie-managed Markdown file containing prose and documented sections.

- `front_matter`: YAML front matter preserved across round-trips.
- `chunks`: ordered mix of `Prose` and `Section` objects.
- `parse(text)`: deserialises a full Markdown string into a `TriefactFile`.
- `empty()`: returns a blank instance with no front matter or chunks.
- `get_section(qualified_name)`: returns matching `Section` or `None`.
- `section_qnames()`: returns ordered list of all section qualified names.
- `upsert_section(...)`: replaces or appends a section; auto-computes `body_fingerprint`.
- `remove_section(qualified_name)`: removes section by name; returns `False` if absent.
- `render()`: serialises back to a Markdown string with sentinels and front matter.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/writer:TriefactFile.parse fingerprint=3be5e2c7a3017435762be997134f13559c76a6b92fc0bb7d33ac4fe0922a6781 body_fp=fc41ebecb95fab4f421d4091ad4d4064d8973f32e14e3135ca4eed76752b34a7 -->
## `TriefactFile.parse(cls, text: str) -> TriefactFile`

Parse a Markdown string into a `TriefactFile` with optional YAML front matter and a list of `Section`/`Prose` chunks.

- Raises `ValueError` if a trie section open sentinel has no matching close sentinel.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/writer:TriefactFile.empty fingerprint=cc0676809bee8efb34856efbd9c950ae148db930ab90e76ebd3d17bd1eefbc7e body_fp=2b1e4bd6386ffd4e44c9e94752c2029a28abf29b14d2b90877f1727670e8c5c0 -->
## `TriefactFile.empty() -> TriefactFile`

Return a new, empty `TriefactFile` with no front matter and no chunks.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/writer:TriefactFile.get_section fingerprint=aec43c04e2eaaaaf39f4d6be228e0198afa191d15abda68a3879b41b391204d8 body_fp=07a32b37205ea3b4c1c6c6c1e092bbab7de0c13747057df82a3086bfcdc8b9da -->
## `get_section(self, qualified_name: str) -> Section | None`

Return the first `Section` chunk matching `qualified_name`, or `None` if absent.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/writer:TriefactFile.section_qnames fingerprint=b3198e06079669f9cdabe77cd2292e047d5fc68e79e8ecb7e0a9f7bff28f0f60 body_fp=b66f9e5134c9d610bf0cfee8cb8aeb5685a0911f6aa446b3d587dc1eeb3e41d6 -->
## `section_qnames(self) -> list[str]`

Return the qualified names of all `Section` chunks in order.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/writer:TriefactFile.upsert_section fingerprint=2bdb1c4090ef7afade75d9ea2851c9b36b91f9bad036102163b078da3f1e7d74 body_fp=d45d4e64a66b9182e02dc636c4938cb3a2285ad835c220f366875f35243e5630 -->
## `upsert_section(self, *, qualified_name: str, fingerprint: str, body: str) -> None`

Replace an existing section by `qualified_name`, or append a new one at the end.

- `body_fingerprint` is computed automatically via `hash_body`; callers need not supply it.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/writer:TriefactFile.remove_section fingerprint=d8dc7a57db15d5144ac0f1cb113b03fbe74d7608b5e9b23572384079c5ce8032 body_fp=3d88f9e248c66e2b63fe196fa06e60abc2d2f2cc8c6cf86cbc47509ef2af7351 -->
## `remove_section(self, qualified_name: str) -> bool`

Remove the first section matching `qualified_name` from `chunks`.

- Returns `True` if a section was found and removed, `False` otherwise.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/writer:TriefactFile.render fingerprint=dea4d47b10b50a3354eee144920010c5bcb18792813b3e74516e76c8bf21b57c body_fp=6307c46e721eaa26124fdbad645984c1c56f703b06e9f3e36e451b17dc5fb6d3 -->
## `render(self) -> str`

Serialize the `TriefactFile` to a Markdown string, including front matter, prose chunks, and section sentinels with `body_fp`.

- Legacy sections without `body_fingerprint` have it computed on the fly.
<!-- trie:end -->