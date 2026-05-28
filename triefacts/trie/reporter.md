---
trie_version: 0.1.5
source: trie/reporter.py
file_fingerprint: 14ad3f2c8b5d7bed7a6da7c7ee0a460528b42a0de8ab90c6a26cc2a107e06c50
last_synced_at: '2026-05-28T03:46:36Z'
defines:
- kind: module
  qualified_name: trie/reporter:__module__
  lines: 1-183
- kind: class
  qualified_name: trie/reporter:Verbosity
  lines: 24-27
- kind: class
  qualified_name: trie/reporter:Reporter
  lines: 30-75
- kind: method
  qualified_name: trie/reporter:Reporter.__init__
  lines: 38-41
- kind: method
  qualified_name: trie/reporter:Reporter.info
  lines: 43-45
- kind: method
  qualified_name: trie/reporter:Reporter.detail
  lines: 47-49
- kind: method
  qualified_name: trie/reporter:Reporter.success
  lines: 51-53
- kind: method
  qualified_name: trie/reporter:Reporter.warn
  lines: 55-58
- kind: method
  qualified_name: trie/reporter:Reporter.error
  lines: 60-61
- kind: method
  qualified_name: trie/reporter:Reporter.status
  lines: 63-67
- kind: method
  qualified_name: trie/reporter:Reporter.elapsed
  lines: 69-72
- kind: method
  qualified_name: trie/reporter:Reporter.start_progress
  lines: 74-75
- kind: class
  qualified_name: trie/reporter:_NullContext
  lines: 78-83
- kind: method
  qualified_name: trie/reporter:_NullContext.__enter__
  lines: 79-80
- kind: method
  qualified_name: trie/reporter:_NullContext.__exit__
  lines: 82-83
- kind: class
  qualified_name: trie/reporter:ProgressHandle
  lines: 86-182
- kind: method
  qualified_name: trie/reporter:ProgressHandle.__init__
  lines: 93-98
- kind: method
  qualified_name: trie/reporter:ProgressHandle.__enter__
  lines: 100-115
- kind: method
  qualified_name: trie/reporter:ProgressHandle.__exit__
  lines: 117-126
- kind: method
  qualified_name: trie/reporter:ProgressHandle._print
  lines: 128-134
- kind: method
  qualified_name: trie/reporter:ProgressHandle.start_file
  lines: 136-142
- kind: method
  qualified_name: trie/reporter:ProgressHandle.finish_file
  lines: 144-176
- kind: method
  qualified_name: trie/reporter:ProgressHandle.skip_file
  lines: 178-182
incoming_refs: 16
outgoing_refs: 0
---
<!-- trie:section symbol=trie/reporter:Reporter fingerprint= body_fp=cc965222e8eb81c0781c8d4fdd9af18daacded83c3b91b5306161d4ca51ed01b -->
## `Reporter(verbosity: Verbosity = Verbosity.MEDIUM, console: Console | None = None)`

Verbosity-gated Rich console wrapper threaded through CLI subcommand handlers.

- `verbosity`: gates which methods produce output; `error` is always unconditional
- `info` / `success` / `warn`: print at `MEDIUM+`
- `detail`: prints at `VERBOSE` only
- `status`: returns a no-op context manager when below `MEDIUM`
- `elapsed`: returns a formatted string like `"took 1.23s"` measuring wall-clock time since the `Reporter` was constructed; useful for printing total duration at the end of a command
- `start_progress`: returns a `ProgressHandle` context manager for file-level progress
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:__module__ fingerprint=5e8b08dfe65f9f795689fb53568d42681062a72da8c7731c23dce6381ade108a body_fp=8bc2b47d837b44eb8a630e7beb1621a0e61952b5027652a9619dbc32fa76b092 source_ref=a4f47faea03f1c6cf869bda0c0d2b7ed2badeae8 -->
## `reporter`

Provide verbosity-gated console output and Rich progress-bar reporting for CLI commands.

- `Verbosity`: three-level enum (`MUTE=0`, `MEDIUM=1`, `VERBOSE=2`) controlling output suppression.
- `Reporter`: central console wrapper; CLI commands share one instance, passing callbacks to sync internals.
- `ProgressHandle`: context-manager progress bar with per-file start/finish/skip hooks.
- Requires `rich`; raises `ImportError` with install hint if absent.
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:Verbosity fingerprint=68167be5fddb8748e7165d3e1141f0c0c352b1dcef0f7a2e6430f8fd2efa74be body_fp=744d995411b96f4b4703b386ac7d15da6f3d0a7b956dec75fdd9ac29b2dce726 source_ref=7f0e336261956631a0d9573b96ff6567f35b0c87 -->
## `Verbosity`

Three-level verbosity enum controlling `Reporter` output gates.

- `MUTE`: suppresses everything except errors.
- `MEDIUM`: enables info, success, warnings, and progress bars.
- `VERBOSE`: adds per-file start lines and token/cache detail.
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:Reporter fingerprint=f2f9eb0d0db812c01986aa8de45e8112145fc59fb1d1c249d40a0b3bf10e0f6c body_fp=047a7b3b0502ed76cb87d3a71659fbc484921c6d3bccfe32ab2afb636bb6a158 source_ref=85c1d7e08391fdf4591efecab54488744b0d9af3 -->
## `Reporter(verbosity: Verbosity = Verbosity.MEDIUM, console: Console | None = None)`

Verbosity-gated Rich console wrapper threaded through CLI subcommand handlers.

- `verbosity`: gates which methods produce output; `MUTE` suppresses all except `error`
- `error`: always prints regardless of verbosity level
- `status`: returns a no-op context manager when verbosity is below `MEDIUM`
- `start_progress`: returns a `ProgressHandle` context manager for file-level progress
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:Reporter.__init__ fingerprint=4cde0d3d19c674bce9d5999617edd36f6c1991fac11b08f19a6ddba17b0f59ce body_fp=ae79feb172bb679d4713ab766a717eb4097dfa3360c3b18744859be50f0477e2 source_ref=85c1d7e08391fdf4591efecab54488744b0d9af3 -->
## `Reporter.__init__(self, verbosity: Verbosity = Verbosity.MEDIUM, console: Console | None = None)`

Initialise a `Reporter` with a verbosity level, optional Rich console, and a wall-clock start time.

- `console`: uses a default `Console()` when not provided.
- `_start`: records `time.monotonic()` for use by `elapsed()`.
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
<!-- trie:section symbol=trie/reporter:Reporter.elapsed fingerprint=36090c883265c26b545bd9e37f5a46b55d6b46b76e83bedb1e7013e812e21919 body_fp=67bd266d81a61abc8a5b39aef6d4cccd9fa561dd4f6003e5599c9cd153bfde8b source_ref=85c1d7e08391fdf4591efecab54488744b0d9af3 -->
## `Reporter.elapsed() -> str`

Human-readable wall-clock elapsed time since the `Reporter` was created, formatted as `"took X.XXs"`.
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
<!-- trie:section symbol=trie/reporter:ProgressHandle fingerprint=28ff21ac130486863ec732556ba4c070942c2c2e199c82b5077209f6d1112c4e body_fp=fcb65b370bdd34ee9b5ffd105227d57732a9554d943635863c70fc70f41c48c1 source_ref=a4f47faea03f1c6cf869bda0c0d2b7ed2badeae8 -->
## `ProgressHandle(reporter: Reporter, total: int, label: str)`

Context-manager progress reporter that wraps a Rich progress bar and per-file status lines, gated by `Reporter` verbosity.

- `total`: expected file count; bar is skipped entirely when zero.
- `start_file`: updates bar description and prints `→ rel_path` at VERBOSE.
- `finish_file`: advances bar and prints `✓ rel_path · $cost · N sym` at MEDIUM+; adds token/cache detail at VERBOSE.
- `skip_file`: advances bar and prints `⊘ rel_path · skipped: reason` at MEDIUM+.
- MUTE: all methods are no-ops except bar advancement.
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:ProgressHandle.__init__ fingerprint=7db3d0385ca9d91f7d3d72a231d4bdab74ee74393f8ce2c29e6c3904c766396b body_fp=bf15ea40373839eb6806c686bf4c0e78d83e793fa742992b838a7521a6cc4e80 source_ref=a4f47faea03f1c6cf869bda0c0d2b7ed2badeae8 -->
## `ProgressHandle.__init__(self, reporter: Reporter, total: int, label: str)`

Initialize a `ProgressHandle` with a parent reporter, file count, and progress bar label.
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:ProgressHandle.__enter__ fingerprint=fa8f8db25bfe291e05bbcf2fae90906b02b98f66c18727e21b41b7ef3e573d8b body_fp=1e8592be9c590b7e75f157c5068b8862dc6279e012d43ceb900f33cd2bed1165 source_ref=85c1d7e08391fdf4591efecab54488744b0d9af3 -->
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