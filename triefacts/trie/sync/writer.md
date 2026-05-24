---
trie_version: 0.1.2
source: trie/sync/writer.py
file_fingerprint: e52c149cb863ae0965c51ea285478b5ef347e435983931d9fc488ddeb2881166
last_synced_at: '2026-05-23T23:47:43Z'
defines:
- kind: module
  qualified_name: trie/sync/writer:__module__
  lines: 1-379
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
- kind: constant
  qualified_name: trie/sync/writer:AGENT_FRONT_MATTER_KEYS
  lines: 106-111
- kind: class
  qualified_name: trie/sync/writer:Section
  lines: 115-120
- kind: class
  qualified_name: trie/sync/writer:Prose
  lines: 124-125
- kind: constant
  qualified_name: trie/sync/writer:Chunk
  lines: 128-128
- kind: class
  qualified_name: trie/sync/writer:TriefactFile
  lines: 132-313
- kind: method
  qualified_name: trie/sync/writer:TriefactFile.parse
  lines: 137-184
- kind: method
  qualified_name: trie/sync/writer:TriefactFile.empty
  lines: 187-188
- kind: method
  qualified_name: trie/sync/writer:TriefactFile.get_section
  lines: 192-196
- kind: method
  qualified_name: trie/sync/writer:TriefactFile.section_qnames
  lines: 198-199
- kind: method
  qualified_name: trie/sync/writer:TriefactFile.upsert_section
  lines: 203-230
- kind: method
  qualified_name: trie/sync/writer:TriefactFile.sort_sections
  lines: 232-254
- kind: method
  qualified_name: trie/sync/writer:TriefactFile.remove_section
  lines: 256-261
- kind: method
  qualified_name: trie/sync/writer:TriefactFile._append_section
  lines: 263-274
- kind: method
  qualified_name: trie/sync/writer:TriefactFile.render
  lines: 278-313
- kind: function
  qualified_name: trie/sync/writer:render_for_agent
  lines: 316-378
incoming_refs: 64
outgoing_refs: 0
---
<!-- trie:section symbol=trie/sync/writer:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=ebb5aeafa4ad18ffb202486b304972673f59767993e26e76f115ba12bf8df3f7 source_ref=7779abbc571fd9eb4f6d6cdcb9583c2521743028 -->
## `writer`

Parse, mutate, and render trie-managed Markdown files containing delimited symbol-documentation sections.

- `SECTION_OPEN_RE`: matches opening sentinels carrying `symbol`, `fingerprint`, and optional `body_fp`/`source_ref`
- `SECTION_CLOSE_RE`: matches closing `<!-- trie:end -->` sentinels
- `AGENT_FRONT_MATTER_KEYS`: frontmatter keys preserved by `render_for_agent`
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:SECTION_OPEN_RE fingerprint=1be5610e8a8a656183d1ce9d75ecba54ebb2113537e3c28d43cce24d941e0194 body_fp=29f690fe61aba7d2bcb4de997c50ad80a86efc087047949ae0e1353256bac086 source_ref=7779abbc571fd9eb4f6d6cdcb9583c2521743028 -->
## `SECTION_OPEN_RE`

Compiled regex matching a `trie:section` open sentinel line, capturing `symbol`, `fp`, and optionally `body_fp` and `source_ref`.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:SECTION_CLOSE_RE fingerprint=49aa71874073d7e43da82cffb2e8446d3946ff6b664d86a74e4b8105f2ce602a body_fp=c468311503a76d1105d50fff0bbd93f56eca77f46399ef663f6aee5a23fdfc43 source_ref=7779abbc571fd9eb4f6d6cdcb9583c2521743028 -->
## `SECTION_CLOSE_RE = re.compile(r"(?m)^<!--\s*trie:end\s*-->[ \t]*$")`

Compiled regex matching a `<!-- trie:end -->` close sentinel occupying its own line.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:SECTION_CLOSE fingerprint=742e69c224d8d71b2d79094222e59b783d57ae9cf4e3a050b3874e1d05981d20 body_fp=644eeff9d597ebeb68e9c9f8e3877a510c976201f3b29b7680b02161e97d603e source_ref=7779abbc571fd9eb4f6d6cdcb9583c2521743028 -->
## `SECTION_CLOSE = "<!-- trie:end -->"`

Canonical closing sentinel string emitted by `render()` to terminate a trie section.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:FRONT_MATTER_RE fingerprint=f100241e2f09e0c34d4dd9fbfafad078e9b2edeb64ad505b28512c83a51cdb48 body_fp=2c40d27ad90fb9bed4c9620b96042ed4b09ecc38dc08e14e0aa1dc1d113e280a source_ref=7779abbc571fd9eb4f6d6cdcb9583c2521743028 -->
## `FRONT_MATTER_RE`

Regex matching a YAML front-matter block at the start of a triefact file, capturing its content in the `yaml` group.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:hash_body fingerprint=ab22edfb13d8ba9c75b86d2384923163f1c839f46c4a2ed06ca566491fc6f96d body_fp=dcc872ff1eec4a0bb1a0a2195eaaadb21a7c830048fb943566134672aff3d391 source_ref=7779abbc571fd9eb4f6d6cdcb9583c2521743028 -->
## `hash_body(body: str) -> str`

Compute SHA-256 hex digest of `body` with leading/trailing whitespace stripped.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:_HEADING_RE fingerprint=b171a12459c1801f28b3970483335daeacef5462126ceb123ef5793ee735f80b body_fp=91f56f57755182b568886d452b14aa82a50d380676a58337f83907ed4605db11 source_ref=7779abbc571fd9eb4f6d6cdcb9583c2521743028 -->
## `_HEADING_RE = re.compile(r"^\s{0,3}#{1,6}\s")`

Matches ATX-style Markdown headings (1–6 `#` with up to 3 leading spaces).
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:_SENTENCE_END_RE fingerprint=46839332c70a94fc506bb56b7637497fd1a8b3a93af0eb5c4ff8390ddeb08946 body_fp=56a4335cb388fd4a2cb68b53e0a186bc50f23a16a8fdfbcfc7d2b4716bacc8e4 source_ref=7779abbc571fd9eb4f6d6cdcb9583c2521743028 -->
## `_SENTENCE_END_RE = re.compile(r"(?<=[.!?])\s+|\Z")`

Regex matching the boundary after a sentence-ending punctuation or end-of-string.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:extract_one_liner fingerprint=fb87254713b9705aec49bf5aaed06df13d5765c8d66d19dd661b746b0045cd82 body_fp=4e861c4a0684fe585e41e687c2abc06b6ba594bc18e6c2d08bdceda9a5329cf5 source_ref=7779abbc571fd9eb4f6d6cdcb9583c2521743028 -->
## `extract_one_liner(body: str, *, max_chars: int = 200) -> str`

Pull the first sentence from a triefact section body, skipping any leading heading.

- `body`: expected shape `## signature\n\n<prose...>`; headings and blank leading lines are skipped.
- Returns `""` if no usable prose is found; truncates to `max_chars` with `…` if exceeded.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:AGENT_FRONT_MATTER_KEYS fingerprint=4ffdf447d675342eb7e62f591eb81f0dbe4b8236a7ecbc21145d49565aaf7fa7 body_fp=2c3fbcfcbc57f09ed2c243c7e7bea2fd2cfbccd65757f3212ac551e32c0ab2b4 source_ref=7779abbc571fd9eb4f6d6cdcb9583c2521743028 -->
## `AGENT_FRONT_MATTER_KEYS: tuple[str, ...] = ("description", "defines", "incoming_refs", "outgoing_refs")`

Frontmatter keys retained when rendering a triefact for agent-facing output; all others are stripped as bookkeeping noise.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:Section fingerprint=9ba5f768080a5d934fd87a6cab7e6eed1cd53c7a143db4e39169a3f1d1205a7a body_fp=0e6c367a7bef7bb129049070102fde1083d79fa2693252ce0cafc4093fb26612 source_ref=7779abbc571fd9eb4f6d6cdcb9583c2521743028 -->
## `Section(qualified_name, fingerprint, body, body_fingerprint=None, source_ref=None)`

Immutable record representing one trie-managed section parsed from a triefact file.

- `fingerprint`: SHA-256 over the normalized source symbol body.
- `body`: text between sentinels, leading/trailing newlines stripped.
- `body_fingerprint`: SHA-256 over `body`; `None` for legacy sections lacking `body_fp=`.
- `source_ref`: git blob hash of the source file at generation time; `None` if absent.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:Prose fingerprint=cf49910dc87437bc09897192fbd13b0a347f9433a85c94f1e599b18c7eceaf2b body_fp=147d109e5c0eed4c8fff1512805ce03b06a73bf862bdc53f23d7dea8652d12be source_ref=7779abbc571fd9eb4f6d6cdcb9583c2521743028 -->
## `Prose(text: str)`

Immutable chunk representing raw Markdown text between or outside trie sections, preserved verbatim.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:Chunk fingerprint=27a576a701491dcbdfeae28c3b7f87ee71a034e04c90aa8a336c241cf4a788c1 body_fp=d37b49e568228aee5b074f11644055c6493abc5931a965cee7f9dc89602a6333 source_ref=7779abbc571fd9eb4f6d6cdcb9583c2521743028 -->
## `Chunk = Section | Prose`

Type alias for a parsed triefact unit: either a managed `Section` or verbatim `Prose`.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:TriefactFile fingerprint=0bed48a61acf0cfc07707fcf183261f7e1de3e9bed89bcd9396c488f428e0104 body_fp=81d2e6f0edc80e03d1b65c97f7de9704cd1744facc632f3b6487ee8352f031e6 source_ref=7779abbc571fd9eb4f6d6cdcb9583c2521743028 -->
## `TriefactFile`

Parse, mutate, and render a triefact Markdown file containing YAML front matter and sentinel-delimited `Section`/`Prose` chunks.

- `front_matter`: parsed YAML front matter as a plain dict.
- `chunks`: ordered list of `Section` and `Prose` segments.
- `parse(text)`: classmethod; deserialises a full triefact string into a `TriefactFile`.
- `empty()`: classmethod; returns a blank `TriefactFile` with no front matter or chunks.
- `get_section(qualified_name)`: returns the first matching `Section` or `None`.
- `section_qnames()`: returns qualified names of all `Section` chunks in order.
- `upsert_section(...)`: replaces an existing section or appends a new one; auto-computes `body_fingerprint`.
- `sort_sections(start_line_by_qname)`: reorders sections by source line; non-whitespace `Prose` moves to front.
- `remove_section(qualified_name)`: removes the named section; returns `True` if found.
- `render()`: serialises the `TriefactFile` back to a Markdown string with sentinels and front matter.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:TriefactFile.parse fingerprint=d2f423ca6746de2c7f3e04dbb4ff83ee8a1b5b90dddec9f49559e442a2d86e55 body_fp=de1e66628add88b9e23746f31b1f3e3a51179c5d81c44906188ebf56fceb8c21 source_ref=7779abbc571fd9eb4f6d6cdcb9583c2521743028 -->
## `TriefactFile.parse(cls, text: str) -> TriefactFile`

Parse a triefact Markdown string into a `TriefactFile` with front matter and ordered `Chunk` list.

- `text`: raw triefact file contents, including optional YAML front matter and sentinel-delimited sections.
- Raises `ValueError` if any `trie:section` open sentinel has no matching `trie:end`.
- Text between and after sections becomes `Prose` chunks; unreadable YAML front matter silently defaults to `{}`.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:TriefactFile.empty fingerprint=cc0676809bee8efb34856efbd9c950ae148db930ab90e76ebd3d17bd1eefbc7e body_fp=5125099768a7844595d775d3cca304c3183084730810f6bde5d3b392b5bb463b source_ref=7779abbc571fd9eb4f6d6cdcb9583c2521743028 -->
## `TriefactFile.empty() -> TriefactFile`

Construct and return a blank `TriefactFile` with no front matter and no chunks.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:TriefactFile.get_section fingerprint=aec43c04e2eaaaaf39f4d6be228e0198afa191d15abda68a3879b41b391204d8 body_fp=3cf71de53c5572a8f2cf2d77d595f47ae4f2f29d45d1d1b0458054adb1121b52 source_ref=7779abbc571fd9eb4f6d6cdcb9583c2521743028 -->
## `TriefactFile.get_section(self, qualified_name: str) -> Section | None`

Return the first `Section` chunk matching `qualified_name`, or `None` if absent.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:TriefactFile.section_qnames fingerprint=b3198e06079669f9cdabe77cd2292e047d5fc68e79e8ecb7e0a9f7bff28f0f60 body_fp=c05e24d37c0fa6f9d76d14dfa8fb5ec3c3138e181d8255c2c1d52932ee0e88ed source_ref=7779abbc571fd9eb4f6d6cdcb9583c2521743028 -->
## `section_qnames(self) -> list[str]`

Return the qualified names of all `Section` chunks in this `TriefactFile`, in order.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:TriefactFile.upsert_section fingerprint=68a8c8a909c8f5a0c7c91dc04c4b6331439d75e93eb0e3af19524143d7c6fccc body_fp=a0915ac2baab3bec38931b6b8232cedd874051a91c671f3e541dbc6b697c76fb source_ref=7779abbc571fd9eb4f6d6cdcb9583c2521743028 -->
## `TriefactFile.upsert_section(*, qualified_name, fingerprint, body, source_ref=None) -> None`

Replace an existing `TriefactFile` section by `qualified_name`, or append a new one at the end.

- `body_fingerprint`: computed automatically via `hash_body`; callers cannot omit it.
- `source_ref`: git blob hash stamped into the sentinel; omitted from output when `None`.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:TriefactFile.sort_sections fingerprint=3a5abfe00c1190b093875944af69f77a27689bb7a756b7a12c709e067e398038 body_fp=d9fe89a60c537702cfcd06079f263d1e44a8edc5e5ea14e9d3153600496ff880 source_ref=7779abbc571fd9eb4f6d6cdcb9583c2521743028 -->
## `TriefactFile.sort_sections(self, start_line_by_qname: dict[str, int]) -> None`

Reorder `TriefactFile` section chunks to match source-line order in-place.

- `start_line_by_qname`: maps qualified name → source line; absent names sort last.
- Whitespace-only `Prose` chunks are dropped; non-whitespace `Prose` is moved to the front.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:TriefactFile.remove_section fingerprint=d8dc7a57db15d5144ac0f1cb113b03fbe74d7608b5e9b23572384079c5ce8032 body_fp=2daa478e46bad4fd8ad8f62c5c516db6431ba0094330e1a7534986185739e421 source_ref=7779abbc571fd9eb4f6d6cdcb9583c2521743028 -->
## `TriefactFile.remove_section(self, qualified_name: str) -> bool`

Remove the first `Section` chunk matching `qualified_name` from a `TriefactFile`; return `True` if removed, `False` if not found.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:TriefactFile._append_section fingerprint=39d0ed815c7e15cf563957738a217245397a9ae9c72076762ea523a6b7cb189c body_fp=3aa1438ad029d13008f34875fa213b897c5720c18fe3f891e579b6b635805da4 source_ref=7779abbc571fd9eb4f6d6cdcb9583c2521743028 -->
## `TriefactFile._append_section(section: Section) -> None`

Append a `Section` to `TriefactFile.chunks`, inserting a blank-line separator before it.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:TriefactFile.render fingerprint=b89097c162426efec69cd3120b0294e523ca70a0015b74ea3338ace3ca6c5abd body_fp=ae62437b5dd947d193e99f69a00e3ca02db89533364cfed95f1beae64d232869 source_ref=7779abbc571fd9eb4f6d6cdcb9583c2521743028 -->
## `TriefactFile.render(self) -> str`

Serialize a `TriefactFile` to a complete Markdown string with YAML frontmatter and trie sentinels.

- Always emits `body_fp=`; computes it on-the-fly for legacy sections lacking `body_fingerprint`.
- Omits `source_ref=` from sentinels when `Section.source_ref` is falsy.
- Inserts a blank-line separator between consecutive `Section` chunks so each sentinel is line-anchored.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:render_for_agent fingerprint=092ba74e28cdec14b0df2de55c6ab0105f9f6c074da00f6bcccb774d76160d8c body_fp=6661b78f021888011815cf3bc1d5e6a5ae783fb2ae40a1ee31f495f89a27be2a source_ref=7779abbc571fd9eb4f6d6cdcb9583c2521743028 -->
## `render_for_agent(text: str) -> str`

Strip trie machinery noise from a triefact, returning clean Markdown for agent consumption.

- Frontmatter: retains only `AGENT_FRONT_MATTER_KEYS`; omits block entirely if none apply.
- Section sentinels (`<!-- trie:section ... -->` / `<!-- trie:end -->`): removed; bodies emitted as plain Markdown with blank-line separation.
- Inter-section prose and section body content are preserved verbatim.
<!-- trie:end -->