---
trie_version: 0.1.2
source: trie/reporter.py
file_fingerprint: 0d25e92681b94ef96d032a5e5f36c20fcbfab84a6061886aae0515f89fb991e8
last_synced_at: '2026-05-19T10:41:44Z'
defines:
- kind: module
  qualified_name: trie/reporter:__module__
  lines: 1-171
- kind: class
  qualified_name: trie/reporter:Verbosity
  lines: 19-22
- kind: class
  qualified_name: trie/reporter:Reporter
  lines: 25-64
- kind: method
  qualified_name: trie/reporter:Reporter.__init__
  lines: 33-35
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
  qualified_name: trie/reporter:_NullContext
  lines: 67-72
- kind: method
  qualified_name: trie/reporter:_NullContext.__enter__
  lines: 68-69
- kind: method
  qualified_name: trie/reporter:_NullContext.__exit__
  lines: 71-72
- kind: class
  qualified_name: trie/reporter:ProgressHandle
  lines: 75-170
- kind: method
  qualified_name: trie/reporter:ProgressHandle.__init__
  lines: 82-87
- kind: method
  qualified_name: trie/reporter:ProgressHandle.__enter__
  lines: 89-103
- kind: method
  qualified_name: trie/reporter:ProgressHandle.__exit__
  lines: 105-114
- kind: method
  qualified_name: trie/reporter:ProgressHandle._print
  lines: 116-122
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
<!-- trie:section symbol=trie/reporter:Verbosity fingerprint=68167be5fddb8748e7165d3e1141f0c0c352b1dcef0f7a2e6430f8fd2efa74be body_fp=2ade04d5064a3cee43c83b4faa196138a0bff288a70e5736817d6d29c385fbf5 source_ref=7f0e336261956631a0d9573b96ff6567f35b0c87 -->
## `Verbosity(IntEnum)`

Three-level verbosity enum controlling output suppression across `Reporter` and `ProgressHandle`.

- `MUTE`: silences everything except `error`.
- `MEDIUM`: enables `info`, `success`, `warn`, `status`, and progress bars.
- `VERBOSE`: adds per-file start lines and token/cache detail.
<!-- trie:end -->

<!-- trie:section symbol=trie/reporter:Reporter fingerprint=6175ff59d9a94c9793a6a742a13614406a715ec2bb4940a212dbf397392e1507 body_fp=168f3789a908ad08a7f670880f0b01be5eddcc8ae8269a6720c8ed7ef6d57260 source_ref=7f0e336261956631a0d9573b96ff6567f35b0c87 -->
## `Reporter(verbosity: Verbosity = Verbosity.MEDIUM, console: Console | None = None)`

Verbosity-gated console wrapper that threads through CLI subcommands for formatted output.

- `verbosity`: controls which methods produce output; `MUTE` silences all but `error`
- `info` / `detail`: print at `MEDIUM` / `VERBOSE` respectively
- `status`: returns a spinner context manager, or a no-op at `MUTE`
- `start_progress`: returns a `ProgressHandle` context manager for file-level progress
<!-- trie:end -->

<!-- trie:section symbol=trie/reporter:Reporter.info fingerprint=c360aff5e763c039038842e46cffcdf806016693b8a32a9024ba31ed85535328 body_fp=77fe1940dc75860b01c84ec749547600c2777c84766fedccdfe537277bb81a62 source_ref=7f0e336261956631a0d9573b96ff6567f35b0c87 -->
## `info(self, msg: str) -> None`

Print `msg` to the console at `MEDIUM` verbosity or above.
<!-- trie:end -->

<!-- trie:section symbol=trie/reporter:Reporter.detail fingerprint=ac606f27fc31292a6bb92bfb6309ad7ae4085a8a3eb6b93f04537a3b5bea9d96 body_fp=e028acb9bdfd0653d383cb63cf246d3fc2ab8cd77d3589d2178c484f89b00447 source_ref=7f0e336261956631a0d9573b96ff6567f35b0c87 -->
## `detail(self, msg: str) -> None`

Print `msg` to the console only when verbosity is `VERBOSE`.
<!-- trie:end -->

<!-- trie:section symbol=trie/reporter:Reporter.success fingerprint=0ba3187d9ed4ea88e566b86760233ab296a70d00fc5649524dd22ade54779161 body_fp=6e80baf8aaec6af2bd53ba8e46e7a7b542df36558eb3345b2b26ae1860491f99 source_ref=7f0e336261956631a0d9573b96ff6567f35b0c87 -->
## `success(self, msg: str) -> None`

Print a green check-mark prefixed message at `MEDIUM` verbosity or above.
<!-- trie:end -->

<!-- trie:section symbol=trie/reporter:Reporter.warn fingerprint=2fe62f1d72c6acf6e6770afee5f9b3964fd5fc4d5bff48f9eab88d0a5e088e3a body_fp=afa98cac409baede84f298d2b4fda4604cc04740be4ed022f1f4598ea2f7d8f6 source_ref=7f0e336261956631a0d9573b96ff6567f35b0c87 -->
## `warn(self, msg: str) -> None`

Print a yellow-prefixed warning message at `MEDIUM` verbosity or above.
<!-- trie:end -->

<!-- trie:section symbol=trie/reporter:Reporter.error fingerprint=ea5624fd1f2b32eb63d048435076a064359cac7a8c910f24d88533142f203feb body_fp=563836d8b03995d7c90e6d5599f032f71f3d114d96742dd0aa829bccf38cdd48 source_ref=7f0e336261956631a0d9573b96ff6567f35b0c87 -->
## `error(self, msg: str) -> None`

Print an error message unconditionally, regardless of verbosity level.
<!-- trie:end -->

<!-- trie:section symbol=trie/reporter:Reporter.status fingerprint=1ce7a4b2274ea11bda01d7bafb2195d03be906e09dc394540a996384bb481c77 body_fp=84057683c74d2cd15087e09082dbc755af4f52400ba9ec3a2b1841d55d1a6864 source_ref=7f0e336261956631a0d9573b96ff6567f35b0c87 -->
## `status(self, msg: str) -> AbstractContextManager`

Return a live spinner context manager, or a no-op context if verbosity is below MEDIUM.
<!-- trie:end -->

<!-- trie:section symbol=trie/reporter:Reporter.start_progress fingerprint=a71b5d1c595a24d65267bee23143bc679a28d76569344578c49e6d107dc67279 body_fp=d5cbd4cd1b299dae198e4294c8df4300cd044aef46b9e6771d64d79393372738 source_ref=7f0e336261956631a0d9573b96ff6567f35b0c87 -->
## `start_progress(self, total: int, label: str) -> ProgressHandle`

Create and return a `ProgressHandle` context manager for tracking progress over `total` items.
<!-- trie:end -->

<!-- trie:section symbol=trie/reporter:ProgressHandle fingerprint=125bef14fe34e5b9d3e4da98c499c9b980cc3a6e6dd00519176987508b839599 body_fp=56e3b06ab7f4efdac42397b4a166f8a07de65291b70ee92bc50f0468388de803 source_ref=7f0e336261956631a0d9573b96ff6567f35b0c87 -->
## `ProgressHandle(reporter: Reporter, total: int, label: str)`

Context-manager progress bar for a batch of files, gated on verbosity.

- `total`: expected file count; zero suppresses the Rich bar entirely.
- `label`: task description shown in the progress bar.
- MEDIUM+: renders a Rich bar with spinner, count, and ETA.
- VERBOSE: also prints a `→ rel_path` line per `start_file` call and token/cache detail per `finish_file` call.
- MUTE: all methods are no-ops.
<!-- trie:end -->

<!-- trie:section symbol=trie/reporter:ProgressHandle.start_file fingerprint=e1db160ef3c1e5c842d9d39ce5758c26312cc966187c314d617000236375fe8f body_fp=fe175cc4ef2d6eb6b1aeabc1889cf7ee048e2bb005e9faeae53e0c6bf66bb0da source_ref=7f0e336261956631a0d9573b96ff6567f35b0c87 -->
## `start_file(self, rel_path: str) -> None`

Update the progress bar description to the current file and print a `→ rel_path` line at VERBOSE level.
<!-- trie:end -->

<!-- trie:section symbol=trie/reporter:ProgressHandle.finish_file fingerprint=4afa6c0f41126ce73f145bb430e3bd99d0295aff0226d74fc3197c64c31ac1a3 body_fp=724ad2391dd21fddfbc9edb020fc8b729a4c2c562596a64bf8d7fcc06aacefa9 source_ref=7f0e336261956631a0d9573b96ff6567f35b0c87 -->
## `finish_file(rel_path: str, *, cost_usd: float | None = None, symbols: int | None = None, tokens_in: int | None = None, tokens_out: int | None = None, cache_read: int | None = None, cache_write: int | None = None) -> None`

Advance the progress bar and print a completion line for a processed file.

- `cost_usd`: included in output as `$X.XXXX` when provided.
- `symbols`: included as `N sym` when provided.
- `tokens_in`/`tokens_out`, `cache_read`/`cache_write`: printed only at `VERBOSE`; omitted when `None`.
<!-- trie:end -->

<!-- trie:section symbol=trie/reporter:ProgressHandle.skip_file fingerprint=54054bdb5cf751f343914ba6c9b74a73a7fdb5f4fcd8f3108fa8322a1099b3d8 body_fp=b315adad406c14a4115023f69abe8c0578736251dd0220475d902c7200ad64c0 source_ref=7f0e336261956631a0d9573b96ff6567f35b0c87 -->
## `skip_file(self, rel_path: str, reason: str) -> None`

Advance the progress bar and print a skip notice (MEDIUM+ only).
<!-- trie:end -->

<!-- trie:section symbol=trie/reporter:Reporter.__init__ fingerprint=014fff4f617144fe244251854a6e2c712bf6c84f9fa795c3aeafeb1467bbcb81 body_fp=d9f2a8a3bdab158d41a65db4f5d9e483e7b573688f111d23ac848e6e15706aa6 source_ref=7f0e336261956631a0d9573b96ff6567f35b0c87 -->
## `Reporter.__init__(self, verbosity: Verbosity = Verbosity.MEDIUM, console: Console | None = None)`

Initialise with an optional verbosity level and Rich console, defaulting to `MEDIUM` and a fresh `Console`.
<!-- trie:end -->

<!-- trie:section symbol=trie/reporter:_NullContext fingerprint=83551b487c19ee10276faa46f53cc5f87b4d0223fa118d136b8a9c2fae376504 body_fp=fe5b7696c22f47ae87ad432a90fb046611e2a26a41a34691b63225e29980409b source_ref=7f0e336261956631a0d9573b96ff6567f35b0c87 -->
## `_NullContext()`

No-op context manager returned by `Reporter.status` when verbosity is below `MEDIUM`.
<!-- trie:end -->

<!-- trie:section symbol=trie/reporter:_NullContext.__enter__ fingerprint=9f210cb9718c0e2ccf1afd3e1a8f2d55beb6c6390abbe06ed35fdd33a7172f7f body_fp=d3fb1f90062b08b61edebe5f1ab8d21f9692f07bf2392c204868a62bf14c4ca5 source_ref=7f0e336261956631a0d9573b96ff6567f35b0c87 -->
## `__enter__(self) -> _NullContext`

Return self to satisfy the context manager protocol.
<!-- trie:end -->

<!-- trie:section symbol=trie/reporter:_NullContext.__exit__ fingerprint=9f730a1a70a6144b0dc8da4942d9093cd268d625eafac5188775d0d6b8b25f08 body_fp=12cfa75cf9eb51eecbb828e56d425ba7f292f2eab9fa1282a93f8211a91bf51c source_ref=7f0e336261956631a0d9573b96ff6567f35b0c87 -->
## `__exit__(self, *exc: Any) -> None`

No-op exit that satisfies the context manager protocol.
<!-- trie:end -->

<!-- trie:section symbol=trie/reporter:ProgressHandle.__init__ fingerprint=9fe2bc3db3e89583fe4c67c5533f44b25630873d1c3d52254cf9f4719866f0c1 body_fp=6403515aa06c30a306b365051139cd7a0bb81fef09c264c08810e7d0d60fc3e7 source_ref=7f0e336261956631a0d9573b96ff6567f35b0c87 -->
## `ProgressHandle.__init__(self, reporter: Reporter, total: int, label: str)`

Store reporter, total file count, and label; initialize progress bar state to `None`.
<!-- trie:end -->

<!-- trie:section symbol=trie/reporter:ProgressHandle.__enter__ fingerprint=2ae868997c36e66820006407e666b9295cdd9635a2abf4d7434f1c79cd4b08b7 body_fp=606eab9c27cf23454adc80acec4263c11ef1b5333443c626bd39ef6f9efb02be source_ref=7f0e336261956631a0d9573b96ff6567f35b0c87 -->
## `__enter__(self) -> ProgressHandle`

Start the Rich progress bar if verbosity is MEDIUM+ and `total > 0`, then return `self`.
<!-- trie:end -->

<!-- trie:section symbol=trie/reporter:ProgressHandle.__exit__ fingerprint=f7249b97149bb3359cf78e0141969f8be0b13fc309365f184bdfe2c0cfc6b6dd body_fp=83c4d274d8d31577ebe837295b2eef22835e09230ea1829962b458485c45e8f2 source_ref=7f0e336261956631a0d9573b96ff6567f35b0c87 -->
## `__exit__(self, exc_type, exc, tb) -> None`

Tear down the Rich progress bar and reset internal state.
<!-- trie:end -->

<!-- trie:section symbol=trie/reporter:ProgressHandle._print fingerprint=0587173aa56c0bd7479119eebcdf7b3056cc2980f27405895f6a4532541fd28f body_fp=2ff625c70f74dca8825b25eb247d283fa05171643af9a1b649122cbae16fee15 source_ref=7f0e336261956631a0d9573b96ff6567f35b0c87 -->
## `_print(self, line: str) -> None`

Route a line to the active progress bar's console or fall back to the reporter's console.
<!-- trie:end -->

<!-- trie:section symbol=trie/reporter:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=4eaefe99795bdf2d1e0a971a4381a1d0eb3c9bdd8340fbf82442ac96e547f121 source_ref=7f0e336261956631a0d9573b96ff6567f35b0c87 -->
## `reporter`

Provide verbosity-gated console output and Rich progress-bar utilities for CLI commands.

- `Verbosity`: three-level enum (`MUTE`, `MEDIUM`, `VERBOSE`) controlling output suppression.
- `Reporter`: main wrapper; errors always print, warnings/info suppressed below `MEDIUM`.
- `ProgressHandle`: context manager rendering a Rich progress bar at `MEDIUM+`; no-op at `MUTE`.
<!-- trie:end -->