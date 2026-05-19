---
trie_version: 0.1.1
source: trie/sync/writer.py
file_fingerprint: fba68b4d92b0b42c4ef52ce8dcfbd05d5cecf3d04e0a3b0655d3ec43c1e2c53a
last_synced_at: '2026-05-19T10:42:23Z'
defines:
- kind: module
  qualified_name: trie/sync/writer:__module__
  lines: 1-270
- kind: constant
  qualified_name: trie/sync/writer:SECTION_OPEN_RE
  lines: 42-47
- kind: constant
  qualified_name: trie/sync/writer:SECTION_CLOSE_RE
  lines: 48-48
- kind: constant
  qualified_name: trie/sync/writer:SECTION_CLOSE
  lines: 49-49
- kind: constant
  qualified_name: trie/sync/writer:FRONT_MATTER_RE
  lines: 50-50
- kind: function
  qualified_name: trie/sync/writer:hash_body
  lines: 53-60
- kind: constant
  qualified_name: trie/sync/writer:_HEADING_RE
  lines: 63-63
- kind: constant
  qualified_name: trie/sync/writer:_SENTENCE_END_RE
  lines: 64-64
- kind: function
  qualified_name: trie/sync/writer:extract_one_liner
  lines: 67-98
- kind: class
  qualified_name: trie/sync/writer:Section
  lines: 102-107
- kind: class
  qualified_name: trie/sync/writer:Prose
  lines: 111-112
- kind: constant
  qualified_name: trie/sync/writer:Chunk
  lines: 115-115
- kind: class
  qualified_name: trie/sync/writer:TriefactFile
  lines: 119-269
- kind: method
  qualified_name: trie/sync/writer:TriefactFile.parse
  lines: 124-171
- kind: method
  qualified_name: trie/sync/writer:TriefactFile.empty
  lines: 174-175
- kind: method
  qualified_name: trie/sync/writer:TriefactFile.get_section
  lines: 179-183
- kind: method
  qualified_name: trie/sync/writer:TriefactFile.section_qnames
  lines: 185-186
- kind: method
  qualified_name: trie/sync/writer:TriefactFile.upsert_section
  lines: 190-217
- kind: method
  qualified_name: trie/sync/writer:TriefactFile.remove_section
  lines: 219-224
- kind: method
  qualified_name: trie/sync/writer:TriefactFile._append_section
  lines: 226-237
- kind: method
  qualified_name: trie/sync/writer:TriefactFile.render
  lines: 241-269
incoming_refs: 56
outgoing_refs: 0
---
<!-- trie:section symbol=trie/sync/writer:hash_body fingerprint=ab22edfb13d8ba9c75b86d2384923163f1c839f46c4a2ed06ca566491fc6f96d body_fp=ff4cc0d8d37a35d35446d795e12b6d335ea4491d8f9b3e64ac1d995839f65670 source_ref=bb3efe260f5fd45bd8f95219af0e2e36472bd19d -->
## `hash_body(body: str) -> str`

Compute SHA-256 over a section body with leading/trailing whitespace stripped.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/writer:extract_one_liner fingerprint=fb87254713b9705aec49bf5aaed06df13d5765c8d66d19dd661b746b0045cd82 body_fp=2435e7a856eb779aee893e311f40ee9620cef4245c2386e7e7d501da2b5397b1 source_ref=bb3efe260f5fd45bd8f95219af0e2e36472bd19d -->
## `extract_one_liner(body: str, *, max_chars: int = 200) -> str`

Pull the first sentence from a section body, skipping any leading heading.

- `body`: expected shape `## signature\n\n<prose...>`
- Returns `""` if no usable text is found.
- Truncates to `max_chars` with a `…` suffix if exceeded.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/writer:Section fingerprint=9ba5f768080a5d934fd87a6cab7e6eed1cd53c7a143db4e39169a3f1d1205a7a body_fp=1ea3d1c54f683e6dfebc5bd2985d3cfdfe91d3b6ed9a740b779d25e564b5af93 source_ref=bb3efe260f5fd45bd8f95219af0e2e36472bd19d -->
## `Section(qualified_name, fingerprint, body, body_fingerprint=None, source_ref=None)`

Immutable dataclass representing a parsed trie-managed documentation section.

- `fingerprint`: SHA-256 of the normalized source symbol body.
- `body_fingerprint`: SHA-256 of the section body; `None` for legacy sections.
- `source_ref`: git blob hash of the file at generation time; `None` if unavailable.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/writer:Prose fingerprint=cf49910dc87437bc09897192fbd13b0a347f9433a85c94f1e599b18c7eceaf2b body_fp=69558d8cb4d5a4532fe9b2274879285d7ea277f8e9652f6965191131a6c1bc3f source_ref=bb3efe260f5fd45bd8f95219af0e2e36472bd19d -->
## `Prose(text: str)`

Immutable chunk representing verbatim human-written text between (or outside) trie sections.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/writer:TriefactFile fingerprint=15f21b4a7c65e88ab89014cb08291b8d85859b24dc105722ea2d71372583d1ee body_fp=7edfff56642c7f15a4c151a9990e20cb55dd935a55147227e626a53e95560ab4 source_ref=bb3efe260f5fd45bd8f95219af0e2e36472bd19d -->
## `TriefactFile(front_matter={}, chunks=[])`

Parse, mutate, and render a Markdown file containing trie-managed documentation sections interleaved with free-form prose.

- `front_matter`: YAML metadata preserved at the top of the file.
- `chunks`: ordered list of `Section` and `Prose` segments.
- `parse(text)`: deserialises a full Markdown document including front matter.
- `upsert_section(...)`: replaces existing section or appends; auto-computes `body_fp`.
- `remove_section(...)`: returns `False` if the qualified name is not found.
- `render()`: serialises back to Markdown; always emits `body_fp` in open sentinels.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/writer:TriefactFile.parse fingerprint=d2f423ca6746de2c7f3e04dbb4ff83ee8a1b5b90dddec9f49559e442a2d86e55 body_fp=45c8926eff27cd0390b026d5d9e70696d1e2dae8b50bd8be184d7e76e4826744 source_ref=bb3efe260f5fd45bd8f95219af0e2e36472bd19d -->
## `TriefactFile.parse(cls, text: str) -> TriefactFile`

Parse a Markdown string into a `TriefactFile` with front matter and a sequence of `Section` and `Prose` chunks.

- `text`: full file contents including optional YAML front matter
- Raises `ValueError` if any trie section opener has no matching close sentinel
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/writer:TriefactFile.empty fingerprint=cc0676809bee8efb34856efbd9c950ae148db930ab90e76ebd3d17bd1eefbc7e body_fp=980432ddb3c2b2dadcce80c797e7679798e9a79cd9d6b740e8ab52488eff4fc2 source_ref=bb3efe260f5fd45bd8f95219af0e2e36472bd19d -->
## `empty() -> TriefactFile`

Return a new, blank `TriefactFile` with no front matter and no chunks.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/writer:TriefactFile.get_section fingerprint=aec43c04e2eaaaaf39f4d6be228e0198afa191d15abda68a3879b41b391204d8 body_fp=32eedbbfb4497f08444162f2ca01c9fee3e8538c61410a47930655f6d49be9f2 source_ref=bb3efe260f5fd45bd8f95219af0e2e36472bd19d -->
## `get_section(self, qualified_name: str) -> Section | None`

Return the first `Section` matching `qualified_name`, or `None` if absent.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/writer:TriefactFile.section_qnames fingerprint=b3198e06079669f9cdabe77cd2292e047d5fc68e79e8ecb7e0a9f7bff28f0f60 body_fp=b66f9e5134c9d610bf0cfee8cb8aeb5685a0911f6aa446b3d587dc1eeb3e41d6 source_ref=bb3efe260f5fd45bd8f95219af0e2e36472bd19d -->
## `section_qnames(self) -> list[str]`

Return the qualified names of all `Section` chunks in order.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/writer:TriefactFile.upsert_section fingerprint=68a8c8a909c8f5a0c7c91dc04c4b6331439d75e93eb0e3af19524143d7c6fccc body_fp=cf7489466ed68e98d77873e06b65a59661a944ca728d87cdd6277fa8557cedd5 source_ref=bb3efe260f5fd45bd8f95219af0e2e36472bd19d -->
## `upsert_section(self, *, qualified_name: str, fingerprint: str, body: str, source_ref: str | None = None) -> None`

Replace an existing section by `qualified_name` or append a new one, computing `body_fingerprint` automatically.

- `source_ref`: omitted from rendered sentinel when `None`.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/writer:TriefactFile.remove_section fingerprint=d8dc7a57db15d5144ac0f1cb113b03fbe74d7608b5e9b23572384079c5ce8032 body_fp=bb8507fe822a2daf5d736cee80726dc6fd671fb68375e41bd2066dbe9187d3f9 source_ref=bb3efe260f5fd45bd8f95219af0e2e36472bd19d -->
## `remove_section(self, qualified_name: str) -> bool`

Remove the first section matching `qualified_name` from `chunks`; return `True` if found and removed, `False` otherwise.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/writer:TriefactFile.render fingerprint=ab891f4de74b2a14cbbb00185c908d8a85f6ec33546ce2589f056c1c04c9ac48 body_fp=34f64831e6ca4f0a675d2b6592daf74c0e9a3eb7ba45f2dcfdc46175476406a5 source_ref=bb3efe260f5fd45bd8f95219af0e2e36472bd19d -->
## `render(self) -> str`

Serialise the `TriefactFile` to a Markdown string, emitting front matter, prose chunks, and trie section sentinels.

- `body_fp` is always stamped; legacy sections without it are hashed on the fly.
- `source_ref` field is omitted from the sentinel when `None`.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/writer:TriefactFile._append_section fingerprint=39d0ed815c7e15cf563957738a217245397a9ae9c72076762ea523a6b7cb189c body_fp=dad3fbc6ec434ca412558a314b5ab58e20b8ff0e88c8def9ac7142aab4e765ef source_ref=bb3efe260f5fd45bd8f95219af0e2e36472bd19d -->
## `_append_section(self, section: Section) -> None`

Append a `Section` chunk, inserting blank-line separators to keep rendered output well-formed.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/writer:SECTION_OPEN_RE fingerprint=1be5610e8a8a656183d1ce9d75ecba54ebb2113537e3c28d43cce24d941e0194 body_fp=3ca629bb2cb6510de86a1f84ce4161dc199faccbe230288b0dddf7f6d6bec79b source_ref=bb3efe260f5fd45bd8f95219af0e2e36472bd19d -->
## `SECTION_OPEN_RE: re.Pattern`

Match a trie section-open sentinel line, capturing `symbol`, `fp`, `body_fp`, and `source_ref` named groups.

- `body_fp`, `source_ref`: optional; absent in sections written by older trie versions.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/writer:SECTION_CLOSE_RE fingerprint=49aa71874073d7e43da82cffb2e8446d3946ff6b664d86a74e4b8105f2ce602a body_fp=2004ebe542ee79fdad658aa9904ba1b0442250354b178a4fcdb94a6855062a34 source_ref=bb3efe260f5fd45bd8f95219af0e2e36472bd19d -->
## `SECTION_CLOSE_RE = re.compile(r"(?m)^<!--\s*trie:end\s*-->[ \t]*$")`

Match a `<!-- trie:end -->` sentinel that occupies its own line.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/writer:SECTION_CLOSE fingerprint=742e69c224d8d71b2d79094222e59b783d57ae9cf4e3a050b3874e1d05981d20 body_fp=644eeff9d597ebeb68e9c9f8e3877a510c976201f3b29b7680b02161e97d603e source_ref=bb3efe260f5fd45bd8f95219af0e2e36472bd19d -->
## `SECTION_CLOSE = "<!-- trie:end -->"`

Canonical closing sentinel string emitted by `render()` to terminate a trie section.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/writer:FRONT_MATTER_RE fingerprint=f100241e2f09e0c34d4dd9fbfafad078e9b2edeb64ad505b28512c83a51cdb48 body_fp=8ec49c3b262dd47d1f73cf8bdf8dcf4f60c2a937c05d5de64bcf3ec1de881979 source_ref=bb3efe260f5fd45bd8f95219af0e2e36472bd19d -->
## `FRONT_MATTER_RE = re.compile(r"\A---\s*\n(?P<yaml>.*?)\n---\s*\n", re.DOTALL)`

Match and capture YAML front matter at the start of a triefact file.

- `yaml` group: raw YAML text between the `---` delimiters.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/writer:_HEADING_RE fingerprint=b171a12459c1801f28b3970483335daeacef5462126ceb123ef5793ee735f80b body_fp=205572cc4ec41ed44d4c479422c7505dae789fb4bbffde524fb3b1cde6779bf9 source_ref=bb3efe260f5fd45bd8f95219af0e2e36472bd19d -->
## `_HEADING_RE = re.compile(r"^\s{0,3}#{1,6}\s")`

Match lines that begin with a Markdown ATX heading (1–6 `#` characters, up to 3 leading spaces).
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/writer:_SENTENCE_END_RE fingerprint=46839332c70a94fc506bb56b7637497fd1a8b3a93af0eb5c4ff8390ddeb08946 body_fp=71fc01a373746c402544aa9ac4663d9c635d469a7afb75a4ad6588839709263a source_ref=bb3efe260f5fd45bd8f95219af0e2e36472bd19d -->
## `_SENTENCE_END_RE = re.compile(r"(?<=[.!?])\s+|\Z")`

Matches the boundary after a sentence-ending punctuation or the string end.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/writer:Chunk fingerprint=27a576a701491dcbdfeae28c3b7f87ee71a034e04c90aa8a336c241cf4a788c1 body_fp=4ae0b7ee81c0a0304c7f57f47b520acb02a29be2ccd0a21a5d81c160fb60121d source_ref=bb3efe260f5fd45bd8f95219af0e2e36472bd19d -->
## `Chunk = Section | Prose`

Type alias for a parsed unit of a triefact file: either a managed section or verbatim prose.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/writer:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=6630d0815b795c7d9e7a939e77866835dd791e1f7c3ca8b329ffe1aa162285cd source_ref=bb3efe260f5fd45bd8f95219af0e2e36472bd19d -->
## `writer`

Parse, mutate, and render trie-managed Markdown files containing sentinel-delimited documentation sections.

- `SECTION_OPEN_RE` / `SECTION_CLOSE_RE`: line-anchored regexes for sentinel detection
- `Section`: frozen dataclass holding parsed section metadata and body text
- `Prose`: frozen dataclass for verbatim human-written text between sections
- `TriefactFile`: mutable container with `parse`, `render`, and upsert/remove mutations
<!-- trie:end -->