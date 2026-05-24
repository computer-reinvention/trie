---
trie_version: 0.1.2
source: trie/reporter.py
file_fingerprint: 0d25e92681b94ef96d032a5e5f36c20fcbfab84a6061886aae0515f89fb991e8
last_synced_at: '2026-05-23T23:51:21Z'
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
<!-- trie:section symbol=trie/reporter:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=a6e554260c57038883616cc25e85ad5af597d7a0638b266dda89147f019607b8 source_ref=7f0e336261956631a0d9573b96ff6567f35b0c87 -->
## `reporter`

Verbosity-gated console and progress-bar utilities for CLI output.

- `Verbosity`: three-level enum (`MUTE`, `MEDIUM`, `VERBOSE`) controlling all output gates.
- `Reporter`: primary façade; wraps a Rich `Console` with verbosity-filtered print methods.
- `ProgressHandle`: context-manager rendering a Rich progress bar with per-file start/finish/skip callbacks.
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:Verbosity fingerprint=68167be5fddb8748e7165d3e1141f0c0c352b1dcef0f7a2e6430f8fd2efa74be body_fp=744d995411b96f4b4703b386ac7d15da6f3d0a7b956dec75fdd9ac29b2dce726 source_ref=7f0e336261956631a0d9573b96ff6567f35b0c87 -->
## `Verbosity`

Three-level verbosity enum controlling `Reporter` output gates.

- `MUTE`: suppresses everything except errors.
- `MEDIUM`: enables info, success, warnings, and progress bars.
- `VERBOSE`: adds per-file start lines and token/cache detail.
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:Reporter fingerprint=6175ff59d9a94c9793a6a742a13614406a715ec2bb4940a212dbf397392e1507 body_fp=bb1b41992ce5c08ae2385e13eac184074af05942e7505fbe98ca14d1a7e87b92 source_ref=7f0e336261956631a0d9573b96ff6567f35b0c87 -->
## `Reporter(verbosity: Verbosity = Verbosity.MEDIUM, console: Console | None = None)`

Verbosity-gated Rich console wrapper threaded through CLI subcommand handlers.

- `verbosity`: gates which methods produce output; `error` is always unconditional
- `info` / `success` / `warn`: print at `MEDIUM+`
- `detail`: prints at `VERBOSE` only
- `status`: returns a no-op context manager when below `MEDIUM`
- `start_progress`: returns a `ProgressHandle` context manager for file-level progress
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:Reporter.__init__ fingerprint=014fff4f617144fe244251854a6e2c712bf6c84f9fa795c3aeafeb1467bbcb81 body_fp=c251635d5a289bbe45185cd3caa987eb38255984ee560ae9efcc32daccea0761 source_ref=7f0e336261956631a0d9573b96ff6567f35b0c87 -->
## `Reporter.__init__(self, verbosity: Verbosity = Verbosity.MEDIUM, console: Console | None = None)`

Initialise a `Reporter` with a verbosity level and optional Rich console.

- `console`: uses a default `Console()` when not provided.
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:Reporter.info fingerprint=c360aff5e763c039038842e46cffcdf806016693b8a32a9024ba31ed85535328 body_fp=ce436e7605422c038d6810982201905229aed200ab31a71e57c24cd669ad47d7 source_ref=7f0e336261956631a0d9573b96ff6567f35b0c87 -->
## `Reporter.info(msg: str) -> None`

Print `msg` to the `Reporter` console at `MEDIUM` verbosity or above.
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:Reporter.detail fingerprint=ac606f27fc31292a6bb92bfb6309ad7ae4085a8a3eb6b93f04537a3b5bea9d96 body_fp=23f86e3189ef603dd16dc3b4e607ffc8bf8de68a6ba4ed6c602c0498e6997117 source_ref=7f0e336261956631a0d9573b96ff6567f35b0c87 -->
## `Reporter.detail(msg: str) -> None`

Print `msg` to the `Reporter` console only when verbosity is `VERBOSE`.
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:Reporter.success fingerprint=0ba3187d9ed4ea88e566b86760233ab296a70d00fc5649524dd22ade54779161 body_fp=d0fe7b83f84d144dea2d2ebbf44a15abce2bfaf1cb13b81072bfcd8111d0ebe0 source_ref=7f0e336261956631a0d9573b96ff6567f35b0c87 -->
## `Reporter.success(msg: str) -> None`

Print a green `✓`-prefixed success message at MEDIUM verbosity or above.
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:Reporter.warn fingerprint=2fe62f1d72c6acf6e6770afee5f9b3964fd5fc4d5bff48f9eab88d0a5e088e3a body_fp=f202209a03c32103b715e1f419842321048a1401d54a870ecbf38cd9dcc380a2 source_ref=7f0e336261956631a0d9573b96ff6567f35b0c87 -->
## `Reporter.warn(msg: str) -> None`

Print a yellow-prefixed warning via the `Reporter` console, suppressed at `MUTE` verbosity.
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:Reporter.error fingerprint=ea5624fd1f2b32eb63d048435076a064359cac7a8c910f24d88533142f203feb body_fp=5fe6ea7b45c0f4bc08dc56929d11d36d9275e2e4fc91bfbe941c6815a7c759ce source_ref=7f0e336261956631a0d9573b96ff6567f35b0c87 -->
## `Reporter.error(msg: str) -> None`

Print an error message unconditionally, regardless of `Reporter` verbosity level.
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:Reporter.status fingerprint=1ce7a4b2274ea11bda01d7bafb2195d03be906e09dc394540a996384bb481c77 body_fp=d2b74c3abfbf2226666087db4061eb9270c7706f9ec4ce1e17eb47ad32cf1ae4 source_ref=7f0e336261956631a0d9573b96ff6567f35b0c87 -->
## `Reporter.status(msg: str) -> AbstractContextManager`

Render a transient spinner context manager for `Reporter`; returns a no-op context when verbosity is below `MEDIUM`.
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:Reporter.start_progress fingerprint=a71b5d1c595a24d65267bee23143bc679a28d76569344578c49e6d107dc67279 body_fp=85a898a073976fc54a9f9445e7c28e9a78e7e00a7df75ee05039b6a4a0460dd5 source_ref=7f0e336261956631a0d9573b96ff6567f35b0c87 -->
## `Reporter.start_progress(self, total: int, label: str) -> ProgressHandle`

Create and return a `ProgressHandle` for tracking progress across `total` files under `label`.
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:_NullContext fingerprint=83551b487c19ee10276faa46f53cc5f87b4d0223fa118d136b8a9c2fae376504 body_fp=7d7463883f279ddaa2813be7a32f48eab7902f87247e59084addc31aa0bc3e9d source_ref=7f0e336261956631a0d9573b96ff6567f35b0c87 -->
## `_NullContext`

No-op context manager returned by `Reporter.status` when verbosity is below `MEDIUM`.
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:_NullContext.__enter__ fingerprint=9f210cb9718c0e2ccf1afd3e1a8f2d55beb6c6390abbe06ed35fdd33a7172f7f body_fp=fe708a4b378a43cec607656ff48687b3f596b48e449789fb19029c00bc5e4355 source_ref=7f0e336261956631a0d9573b96ff6567f35b0c87 -->
## `__enter__(self) -> _NullContext`

Return the `_NullContext` instance unchanged.
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:_NullContext.__exit__ fingerprint=9f730a1a70a6144b0dc8da4942d9093cd268d625eafac5188775d0d6b8b25f08 body_fp=8a5a003997ccd5727870590bdf8ab8d2559af620c9c0eb416607227ae7c2d089 source_ref=7f0e336261956631a0d9573b96ff6567f35b0c87 -->
## `__exit__(self, *exc: Any) -> None`

No-op exit for `_NullContext`.
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:ProgressHandle fingerprint=125bef14fe34e5b9d3e4da98c499c9b980cc3a6e6dd00519176987508b839599 body_fp=5762ccffb5ade16c06180960c3418ffe01d6acfc348d5068f63ac726f05404c0 source_ref=7f0e336261956631a0d9573b96ff6567f35b0c87 -->
## `ProgressHandle`

Context-manager progress reporter that wraps a Rich progress bar and emits per-file status lines gated by `Reporter` verbosity.

- `total`: expected file count; bar is skipped entirely when zero.
- `start_file`: updates bar description and prints `→ rel_path` at VERBOSE.
- `finish_file`: advances bar and prints `✓ rel_path · $cost · N sym`; VERBOSE appends token/cache detail.
- `skip_file`: advances bar and prints `⊘ rel_path · skipped: reason` at MEDIUM+.
- MUTE verbosity: all methods are no-ops except bar advancement.
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:ProgressHandle.__init__ fingerprint=9fe2bc3db3e89583fe4c67c5533f44b25630873d1c3d52254cf9f4719866f0c1 body_fp=bf15ea40373839eb6806c686bf4c0e78d83e793fa742992b838a7521a6cc4e80 source_ref=7f0e336261956631a0d9573b96ff6567f35b0c87 -->
## `ProgressHandle.__init__(self, reporter: Reporter, total: int, label: str)`

Initialize a `ProgressHandle` with a parent reporter, file count, and progress bar label.
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:ProgressHandle.__enter__ fingerprint=2ae868997c36e66820006407e666b9295cdd9635a2abf4d7434f1c79cd4b08b7 body_fp=1e8592be9c590b7e75f157c5068b8862dc6279e012d43ceb900f33cd2bed1165 source_ref=7f0e336261956631a0d9573b96ff6567f35b0c87 -->
## `ProgressHandle.__enter__() -> ProgressHandle`

Start the `ProgressHandle` context, initialising a Rich progress bar when verbosity is MEDIUM+ and `total > 0`.
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:ProgressHandle.__exit__ fingerprint=f7249b97149bb3359cf78e0141969f8be0b13fc309365f184bdfe2c0cfc6b6dd body_fp=da8fcb6f8a9bf2db078a9178e0fd96a64274f0011d0b65fdfd42d9268418eddf source_ref=7f0e336261956631a0d9573b96ff6567f35b0c87 -->
## `ProgressHandle.__exit__(self, exc_type, exc, tb) -> None`

Tear down the `ProgressHandle` Rich progress bar and clear internal state.
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:ProgressHandle._print fingerprint=0587173aa56c0bd7479119eebcdf7b3056cc2980f27405895f6a4532541fd28f body_fp=6369acba8cecdaaa537903251b9dfc99f65099c6cd705fc22aa1a378cbc3c7d7 source_ref=7f0e336261956631a0d9573b96ff6567f35b0c87 -->
## `ProgressHandle._print(line: str) -> None`

Route output above the live progress bar, or fall back to the `Reporter` console.
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:ProgressHandle.start_file fingerprint=e1db160ef3c1e5c842d9d39ce5758c26312cc966187c314d617000236375fe8f body_fp=4eb2015aeeb293879df51c21277a067d4a5dbbccad8f56ff51af252837138bc4 source_ref=7f0e336261956631a0d9573b96ff6567f35b0c87 -->
## `ProgressHandle.start_file(rel_path: str) -> None`

Update the `ProgressHandle` progress bar description and, at VERBOSE level, print a `→ rel_path` line.
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:ProgressHandle.finish_file fingerprint=4afa6c0f41126ce73f145bb430e3bd99d0295aff0226d74fc3197c64c31ac1a3 body_fp=f319caf9a45b3491663bb8c063cbd5fceb6a83d9b74b500d872a366ac55a16b0 source_ref=7f0e336261956631a0d9573b96ff6567f35b0c87 -->
## `ProgressHandle.finish_file(rel_path, *, cost_usd, symbols, tokens_in, tokens_out, cache_read, cache_write)`

Advance the progress bar and print a completion line for a finished file.

- `cost_usd`: formatted as `$X.XXXX`; omitted from output if `None`.
- `symbols`: printed as `N sym`; omitted if `None`.
- `tokens_in`/`tokens_out`: shown at VERBOSE as `tok in/out`.
- `cache_read`/`cache_write`: shown at VERBOSE as `cache rN/wN`.
- Suppressed entirely below `MEDIUM` verbosity after advancing the task.
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:ProgressHandle.skip_file fingerprint=54054bdb5cf751f343914ba6c9b74a73a7fdb5f4fcd8f3108fa8322a1099b3d8 body_fp=fd33912b51cb0e94a21bb96894833019948c3c96a9eb11d35b14d87abb24eb95 source_ref=7f0e336261956631a0d9573b96ff6567f35b0c87 -->
## `ProgressHandle.skip_file(rel_path: str, reason: str) -> None`

Advance the progress bar and print a yellow skip notice for a skipped file at MEDIUM+ verbosity.
<!-- trie:end -->