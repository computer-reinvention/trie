---
trie_version: 0.1.0
source: trie/reporter.py
file_fingerprint: 0d25e92681b94ef96d032a5e5f36c20fcbfab84a6061886aae0515f89fb991e8
last_synced_at: '2026-05-14T17:24:22Z'
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
<!-- trie:section symbol=trie/reporter:Verbosity fingerprint=68167be5fddb8748e7165d3e1141f0c0c352b1dcef0f7a2e6430f8fd2efa74be body_fp=2ade04d5064a3cee43c83b4faa196138a0bff288a70e5736817d6d29c385fbf5 -->
## `Verbosity(IntEnum)`

Three-level verbosity enum controlling output suppression across `Reporter` and `ProgressHandle`.

- `MUTE`: silences everything except `error`.
- `MEDIUM`: enables `info`, `success`, `warn`, `status`, and progress bars.
- `VERBOSE`: adds per-file start lines and token/cache detail.
<!-- trie:end -->

<!-- trie:section symbol=trie/reporter:Reporter fingerprint=6175ff59d9a94c9793a6a742a13614406a715ec2bb4940a212dbf397392e1507 body_fp=168f3789a908ad08a7f670880f0b01be5eddcc8ae8269a6720c8ed7ef6d57260 -->
## `Reporter(verbosity: Verbosity = Verbosity.MEDIUM, console: Console | None = None)`

Verbosity-gated console wrapper that threads through CLI subcommands for formatted output.

- `verbosity`: controls which methods produce output; `MUTE` silences all but `error`
- `info` / `detail`: print at `MEDIUM` / `VERBOSE` respectively
- `status`: returns a spinner context manager, or a no-op at `MUTE`
- `start_progress`: returns a `ProgressHandle` context manager for file-level progress
<!-- trie:end -->

<!-- trie:section symbol=trie/reporter:Reporter.info fingerprint=c360aff5e763c039038842e46cffcdf806016693b8a32a9024ba31ed85535328 body_fp=77fe1940dc75860b01c84ec749547600c2777c84766fedccdfe537277bb81a62 -->
## `info(self, msg: str) -> None`

Print `msg` to the console at `MEDIUM` verbosity or above.
<!-- trie:end -->

<!-- trie:section symbol=trie/reporter:Reporter.detail fingerprint=ac606f27fc31292a6bb92bfb6309ad7ae4085a8a3eb6b93f04537a3b5bea9d96 body_fp=e028acb9bdfd0653d383cb63cf246d3fc2ab8cd77d3589d2178c484f89b00447 -->
## `detail(self, msg: str) -> None`

Print `msg` to the console only when verbosity is `VERBOSE`.
<!-- trie:end -->

<!-- trie:section symbol=trie/reporter:Reporter.success fingerprint=0ba3187d9ed4ea88e566b86760233ab296a70d00fc5649524dd22ade54779161 body_fp=6e80baf8aaec6af2bd53ba8e46e7a7b542df36558eb3345b2b26ae1860491f99 -->
## `success(self, msg: str) -> None`

Print a green check-mark prefixed message at `MEDIUM` verbosity or above.
<!-- trie:end -->

<!-- trie:section symbol=trie/reporter:Reporter.warn fingerprint=2fe62f1d72c6acf6e6770afee5f9b3964fd5fc4d5bff48f9eab88d0a5e088e3a body_fp=afa98cac409baede84f298d2b4fda4604cc04740be4ed022f1f4598ea2f7d8f6 -->
## `warn(self, msg: str) -> None`

Print a yellow-prefixed warning message at `MEDIUM` verbosity or above.
<!-- trie:end -->

<!-- trie:section symbol=trie/reporter:Reporter.error fingerprint=ea5624fd1f2b32eb63d048435076a064359cac7a8c910f24d88533142f203feb body_fp=563836d8b03995d7c90e6d5599f032f71f3d114d96742dd0aa829bccf38cdd48 -->
## `error(self, msg: str) -> None`

Print an error message unconditionally, regardless of verbosity level.
<!-- trie:end -->

<!-- trie:section symbol=trie/reporter:Reporter.status fingerprint=1ce7a4b2274ea11bda01d7bafb2195d03be906e09dc394540a996384bb481c77 body_fp=84057683c74d2cd15087e09082dbc755af4f52400ba9ec3a2b1841d55d1a6864 -->
## `status(self, msg: str) -> AbstractContextManager`

Return a live spinner context manager, or a no-op context if verbosity is below MEDIUM.
<!-- trie:end -->

<!-- trie:section symbol=trie/reporter:Reporter.start_progress fingerprint=a71b5d1c595a24d65267bee23143bc679a28d76569344578c49e6d107dc67279 body_fp=d5cbd4cd1b299dae198e4294c8df4300cd044aef46b9e6771d64d79393372738 -->
## `start_progress(self, total: int, label: str) -> ProgressHandle`

Create and return a `ProgressHandle` context manager for tracking progress over `total` items.
<!-- trie:end -->

<!-- trie:section symbol=trie/reporter:ProgressHandle fingerprint=125bef14fe34e5b9d3e4da98c499c9b980cc3a6e6dd00519176987508b839599 body_fp=56e3b06ab7f4efdac42397b4a166f8a07de65291b70ee92bc50f0468388de803 -->
## `ProgressHandle(reporter: Reporter, total: int, label: str)`

Context-manager progress bar for a batch of files, gated on verbosity.

- `total`: expected file count; zero suppresses the Rich bar entirely.
- `label`: task description shown in the progress bar.
- MEDIUM+: renders a Rich bar with spinner, count, and ETA.
- VERBOSE: also prints a `→ rel_path` line per `start_file` call and token/cache detail per `finish_file` call.
- MUTE: all methods are no-ops.
<!-- trie:end -->

<!-- trie:section symbol=trie/reporter:ProgressHandle.start_file fingerprint=e1db160ef3c1e5c842d9d39ce5758c26312cc966187c314d617000236375fe8f body_fp=fe175cc4ef2d6eb6b1aeabc1889cf7ee048e2bb005e9faeae53e0c6bf66bb0da -->
## `start_file(self, rel_path: str) -> None`

Update the progress bar description to the current file and print a `→ rel_path` line at VERBOSE level.
<!-- trie:end -->

<!-- trie:section symbol=trie/reporter:ProgressHandle.finish_file fingerprint=4afa6c0f41126ce73f145bb430e3bd99d0295aff0226d74fc3197c64c31ac1a3 body_fp=724ad2391dd21fddfbc9edb020fc8b729a4c2c562596a64bf8d7fcc06aacefa9 -->
## `finish_file(rel_path: str, *, cost_usd: float | None = None, symbols: int | None = None, tokens_in: int | None = None, tokens_out: int | None = None, cache_read: int | None = None, cache_write: int | None = None) -> None`

Advance the progress bar and print a completion line for a processed file.

- `cost_usd`: included in output as `$X.XXXX` when provided.
- `symbols`: included as `N sym` when provided.
- `tokens_in`/`tokens_out`, `cache_read`/`cache_write`: printed only at `VERBOSE`; omitted when `None`.
<!-- trie:end -->

<!-- trie:section symbol=trie/reporter:ProgressHandle.skip_file fingerprint=54054bdb5cf751f343914ba6c9b74a73a7fdb5f4fcd8f3108fa8322a1099b3d8 body_fp=b315adad406c14a4115023f69abe8c0578736251dd0220475d902c7200ad64c0 -->
## `skip_file(self, rel_path: str, reason: str) -> None`

Advance the progress bar and print a skip notice (MEDIUM+ only).
<!-- trie:end -->