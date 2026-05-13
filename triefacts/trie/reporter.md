---
trie_version: 0.1.0
source: trie/reporter.py
file_fingerprint: 0d25e92681b94ef96d032a5e5f36c20fcbfab84a6061886aae0515f89fb991e8
last_synced_at: '2026-05-12T18:26:43Z'
defines:
- kind: class
  qualified_name: trie/reporter:Verbosity
  lines: 19-22
- kind: class
  qualified_name: trie/reporter:Reporter
  lines: 25-64
- kind: method
  qualified_name: trie/reporter:Reporter.info
  lines: 37-39
- kind: method
  qualified_name: trie/reporter:Reporter.detail
  lines: 41-43
- kind: method
  qualified_name: trie/reporter:Reporter.success
  lines: 45-47
- kind: method
  qualified_name: trie/reporter:Reporter.warn
  lines: 49-52
- kind: method
  qualified_name: trie/reporter:Reporter.error
  lines: 54-55
- kind: method
  qualified_name: trie/reporter:Reporter.status
  lines: 57-61
- kind: method
  qualified_name: trie/reporter:Reporter.start_progress
  lines: 63-64
- kind: class
  qualified_name: trie/reporter:ProgressHandle
  lines: 75-170
- kind: method
  qualified_name: trie/reporter:ProgressHandle.start_file
  lines: 124-130
- kind: method
  qualified_name: trie/reporter:ProgressHandle.finish_file
  lines: 132-164
- kind: method
  qualified_name: trie/reporter:ProgressHandle.skip_file
  lines: 166-170
incoming_refs: 16
outgoing_refs: 0
---
<!-- trie:section symbol=trie/reporter:Verbosity fingerprint=68167be5fddb8748e7165d3e1141f0c0c352b1dcef0f7a2e6430f8fd2efa74be body_fp=6d511eed6a2e22232efb187235bef8e170ac5d9d39919c595195bbc12200f9e6 -->
## `Verbosity(IntEnum)`

Three-level verbosity enum: `MUTE=0`, `MEDIUM=1`, `VERBOSE=2`.
<!-- trie:end -->

<!-- trie:section symbol=trie/reporter:Reporter fingerprint=6175ff59d9a94c9793a6a742a13614406a715ec2bb4940a212dbf397392e1507 body_fp=773848aba7459d68ea85afa1af33f423210717d50f22f2b3c5d9501964df20d2 -->
## `Reporter(verbosity: Verbosity = Verbosity.MEDIUM, console: Console | None = None)`

Verbosity-gated console wrapper that threads through CLI subcommands for all user-facing output.

- `verbosity`: controls which methods produce output; `MUTE` suppresses all except `error`.
- `status`: returns a no-op context manager when verbosity is below `MEDIUM`.
- `start_progress`: returns a `ProgressHandle` context manager for file-level progress tracking.
<!-- trie:end -->

<!-- trie:section symbol=trie/reporter:Reporter.info fingerprint=c360aff5e763c039038842e46cffcdf806016693b8a32a9024ba31ed85535328 body_fp=77fe1940dc75860b01c84ec749547600c2777c84766fedccdfe537277bb81a62 -->
## `info(self, msg: str) -> None`

Print `msg` to the console at `MEDIUM` verbosity or above.
<!-- trie:end -->

<!-- trie:section symbol=trie/reporter:Reporter.detail fingerprint=ac606f27fc31292a6bb92bfb6309ad7ae4085a8a3eb6b93f04537a3b5bea9d96 body_fp=e028acb9bdfd0653d383cb63cf246d3fc2ab8cd77d3589d2178c484f89b00447 -->
## `detail(self, msg: str) -> None`

Print `msg` to the console only when verbosity is `VERBOSE`.
<!-- trie:end -->

<!-- trie:section symbol=trie/reporter:Reporter.success fingerprint=0ba3187d9ed4ea88e566b86760233ab296a70d00fc5649524dd22ade54779161 body_fp=83eeeb574030f8b4de9538b94adb78d41ccedb2064fc37eb9ba854f9d3a0e41e -->
## `success(self, msg: str) -> None`

Print a green `✓`-prefixed message at `MEDIUM` verbosity or above.
<!-- trie:end -->

<!-- trie:section symbol=trie/reporter:Reporter.warn fingerprint=2fe62f1d72c6acf6e6770afee5f9b3964fd5fc4d5bff48f9eab88d0a5e088e3a body_fp=afa98cac409baede84f298d2b4fda4604cc04740be4ed022f1f4598ea2f7d8f6 -->
## `warn(self, msg: str) -> None`

Print a yellow-prefixed warning message at `MEDIUM` verbosity or above.
<!-- trie:end -->

<!-- trie:section symbol=trie/reporter:Reporter.error fingerprint=ea5624fd1f2b32eb63d048435076a064359cac7a8c910f24d88533142f203feb body_fp=563836d8b03995d7c90e6d5599f032f71f3d114d96742dd0aa829bccf38cdd48 -->
## `error(self, msg: str) -> None`

Print an error message unconditionally, regardless of verbosity level.
<!-- trie:end -->

<!-- trie:section symbol=trie/reporter:Reporter.status fingerprint=1ce7a4b2274ea11bda01d7bafb2195d03be906e09dc394540a996384bb481c77 body_fp=2bf08c2df4d27e89f221ac8f8b8d13c8c6e9a9a19b1d017ae0a2cae374fc0b6e -->
## `status(self, msg: str) -> AbstractContextManager`

Return a spinner context manager while a step runs, or a no-op context when verbosity is below MEDIUM.
<!-- trie:end -->

<!-- trie:section symbol=trie/reporter:Reporter.start_progress fingerprint=a71b5d1c595a24d65267bee23143bc679a28d76569344578c49e6d107dc67279 body_fp=8bd879cbf40ac1dd7ff480bf45e11278dd0f663bbb6a0bfd8cf5459b9d1ec6a9 -->
## `start_progress(self, total: int, label: str) -> ProgressHandle`

Construct and return a `ProgressHandle` context manager for tracking file-level progress.
<!-- trie:end -->

<!-- trie:section symbol=trie/reporter:ProgressHandle fingerprint=125bef14fe34e5b9d3e4da98c499c9b980cc3a6e6dd00519176987508b839599 body_fp=429818f355c48f3b676e52706828ae5baa0164864d2a22f4140076aaf40e8d8a -->
## `ProgressHandle(reporter: Reporter, total: int, label: str)`

Context-manager progress bar for a batch of files, with verbosity-gated Rich output.

- `total`: total file count; bar is suppressed when zero.
- `start_file`: updates bar description and prints `→ rel_path` at VERBOSE.
- `finish_file`: advances bar, prints `✓ rel_path · $cost · N sym`, and token/cache detail at VERBOSE.
- `skip_file`: advances bar and prints `⊘ rel_path · skipped: reason` at MEDIUM+.
- MUTE verbosity: all output is a no-op.
<!-- trie:end -->

<!-- trie:section symbol=trie/reporter:ProgressHandle.start_file fingerprint=e1db160ef3c1e5c842d9d39ce5758c26312cc966187c314d617000236375fe8f body_fp=fe175cc4ef2d6eb6b1aeabc1889cf7ee048e2bb005e9faeae53e0c6bf66bb0da -->
## `start_file(self, rel_path: str) -> None`

Update the progress bar description to the current file and print a `→ rel_path` line at VERBOSE level.
<!-- trie:end -->

<!-- trie:section symbol=trie/reporter:ProgressHandle.finish_file fingerprint=4afa6c0f41126ce73f145bb430e3bd99d0295aff0226d74fc3197c64c31ac1a3 body_fp=55d57030e162ded211147781d5c56027fadd5f24c66398fb2e66ff4ee6621cc7 -->
## `finish_file(rel_path: str, *, cost_usd: float | None = None, symbols: int | None = None, tokens_in: int | None = None, tokens_out: int | None = None, cache_read: int | None = None, cache_write: int | None = None) -> None`

Advance the progress bar and print a completion line for a finished file.

- `cost_usd`: included in output as `$X.XXXX` when provided.
- `symbols`: included as `N sym` when provided.
- `tokens_in`/`tokens_out`, `cache_read`/`cache_write`: printed only at `VERBOSE`; missing values default to `0`.
<!-- trie:end -->

<!-- trie:section symbol=trie/reporter:ProgressHandle.skip_file fingerprint=54054bdb5cf751f343914ba6c9b74a73a7fdb5f4fcd8f3108fa8322a1099b3d8 body_fp=6ea8a79c74cd017abf0fb13a03521b7328c2889e0be3dd36186d61abb06b94b5 -->
## `skip_file(self, rel_path: str, reason: str) -> None`

Advance the progress bar and print a yellow skip notice at MEDIUM+ verbosity.
<!-- trie:end -->