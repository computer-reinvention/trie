---
trie_version: 0.3.0
source: trie/reporter.py
file_fingerprint: 5a1111786624b62a769deef2b827c3abc4e5744ecd33c72f38041239ab44acfe
last_synced_at: '2026-07-20T13:09:01Z'
defines:
- kind: module
  qualified_name: trie/reporter:__module__
  lines: 1-304
- kind: class
  qualified_name: trie/reporter:_OverallOnlyBar
  lines: 33-37
  signature: class _OverallOnlyBar(BarColumn)
- kind: method
  qualified_name: trie/reporter:_OverallOnlyBar.render
  lines: 34-37
  signature: 'def render(self, task): # type: ignore[no-untyped-def]'
- kind: class
  qualified_name: trie/reporter:_OverallOnlyMofN
  lines: 40-44
  signature: class _OverallOnlyMofN(MofNCompleteColumn)
- kind: method
  qualified_name: trie/reporter:_OverallOnlyMofN.render
  lines: 41-44
  signature: 'def render(self, task): # type: ignore[no-untyped-def]'
- kind: class
  qualified_name: trie/reporter:_BottomBarProgress
  lines: 47-68
  signature: class _BottomBarProgress(Progress)
- kind: method
  qualified_name: trie/reporter:_BottomBarProgress.get_renderables
  lines: 58-68
  signature: 'def get_renderables(self): # type: ignore[no-untyped-def]'
- kind: class
  qualified_name: trie/reporter:Verbosity
  lines: 71-74
  signature: class Verbosity(IntEnum)
- kind: class
  qualified_name: trie/reporter:Reporter
  lines: 77-133
  signature: class Reporter
- kind: method
  qualified_name: trie/reporter:Reporter.__init__
  lines: 85-97
  signature: 'def __init__( self, verbosity: Verbosity = Verbosity.MEDIUM, console: Console | None = None, err_console: Console | None = None, )'
- kind: method
  qualified_name: trie/reporter:Reporter.info
  lines: 99-101
  signature: 'def info(self, msg: str) -> None'
- kind: method
  qualified_name: trie/reporter:Reporter.detail
  lines: 103-105
  signature: 'def detail(self, msg: str) -> None'
- kind: method
  qualified_name: trie/reporter:Reporter.success
  lines: 107-109
  signature: 'def success(self, msg: str) -> None'
- kind: method
  qualified_name: trie/reporter:Reporter.warn
  lines: 111-114
  signature: "def warn(self, msg: str) -> None: # Warnings still suppressed in MUTE \u2014 only errors are unconditional."
- kind: method
  qualified_name: trie/reporter:Reporter.error
  lines: 116-119
  signature: 'def error(self, msg: str) -> None: # Unconditional (even in MUTE) and routed to stderr: error text must # survive stdout being consumed, piped, or discarded by a wrapper.'
- kind: method
  qualified_name: trie/reporter:Reporter.status
  lines: 121-125
  signature: 'def status(self, msg: str) -> AbstractContextManager[Any]'
- kind: method
  qualified_name: trie/reporter:Reporter.elapsed
  lines: 127-130
  signature: def elapsed(self) -> str
- kind: method
  qualified_name: trie/reporter:Reporter.start_progress
  lines: 132-133
  signature: 'def start_progress(self, total: int, label: str) -> ProgressHandle'
- kind: class
  qualified_name: trie/reporter:_NullContext
  lines: 136-141
  signature: class _NullContext
- kind: method
  qualified_name: trie/reporter:_NullContext.__enter__
  lines: 137-138
  signature: def __enter__(self) -> _NullContext
- kind: method
  qualified_name: trie/reporter:_NullContext.__exit__
  lines: 140-141
  signature: 'def __exit__(self, *exc: Any) -> None'
- kind: class
  qualified_name: trie/reporter:ProgressHandle
  lines: 144-303
  signature: class ProgressHandle
- kind: method
  qualified_name: trie/reporter:ProgressHandle.__init__
  lines: 163-173
  signature: 'def __init__(self, reporter: Reporter, total: int, label: str)'
- kind: method
  qualified_name: trie/reporter:ProgressHandle.__enter__
  lines: 175-199
  signature: 'def __enter__(self) -> ProgressHandle: # Only drive a live render when attached to a real terminal. In a pipe, # a redirected file, or any non-interactive shell, Rich''s Live region # writes cursor-control escapes that corrupt the output and can clobber # the user''s prompt on exit. There we fall back to plain printed lines # (the `_progress is None` paths in start_file/finish_file/skip_file).'
- kind: method
  qualified_name: trie/reporter:ProgressHandle.__exit__
  lines: 201-223
  signature: 'def __exit__( self, exc_type: type[BaseException] | None, exc: BaseException | None, tb: TracebackType | None, ) -> None'
- kind: method
  qualified_name: trie/reporter:ProgressHandle._print
  lines: 225-231
  signature: 'def _print(self, line: str) -> None: # Route through the live Progress''s console so output lands above the # live region instead of fighting with it.'
- kind: method
  qualified_name: trie/reporter:ProgressHandle.start_file
  lines: 233-251
  signature: 'def start_file(self, rel_path: str, *, cascade: bool = False) -> None: # Cascade files (pulled in because they reference a directly-changed # symbol, not because their own source drifted) get a marker so the # operator can see why N files sync when only a few drifted.'
- kind: method
  qualified_name: trie/reporter:ProgressHandle._end_file_task
  lines: 253-261
  signature: 'def _end_file_task(self, rel_path: str) -> None'
- kind: method
  qualified_name: trie/reporter:ProgressHandle.finish_file
  lines: 263-297
  signature: 'def finish_file( self, rel_path: str, *, cost_usd: float | None = None, symbols: int | None = None, tokens_in: int | None = None, tokens_out: int | None = None, cache_read: int | None = None, cache_write: int | None = None, ) -> None'
- kind: method
  qualified_name: trie/reporter:ProgressHandle.skip_file
  lines: 299-303
  signature: 'def skip_file(self, rel_path: str, reason: str) -> None'
incoming_refs: 171
outgoing_refs: 0
---
<!-- trie:section symbol=trie/reporter:__module__ fingerprint=07290628d1de53b4706aea1dc1f836f538577d35dc30a41a16720a177edab4df body_fp=37df5d1ba79a59a9b669823577300a1026d9e66b729f96885fac6f36a7ac5234 source_ref=5d5181cfe117f8d9faaf106bc52b54cb076eec58 role=io -->
Provides console reporting infrastructure with verbosity controls and Rich-based progress tracking.

- Requires Rich library for terminal output
- `Reporter` class handles verbosity-gated console messages and status displays
- `ProgressHandle` implements uv-style parallel file processing progress with overall bar and per-file spinners
- `Verbosity` enum defines three output levels: MUTE, MEDIUM, VERBOSE
- Custom Rich column classes prevent progress bars on spinner-only tasks
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:_OverallOnlyBar fingerprint=58f9db3e4a84b1b7f35702ae67cfa05ff79e119d01c584588483109d88aa79cf body_fp=335941d602c991e85c34db668e56fa58cc5c51591f7ccd32cf9836a9862a0b97 source_ref=b952f8c0f670efda761b03e342b67367021c2ed6 role=util -->
## `class _OverallOnlyBar(BarColumn)`

Renders a progress bar only for determinate tasks, hiding bars from indeterminate spinner tasks.
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:_OverallOnlyBar.render fingerprint=f5dd789c2297600a905c4625c9c7ad2779b586f0cc7b44c6921d25cd064d0c09 body_fp=4962dbe775ed66844d0fc3a53cbd0a874d26781f3e1d5f667de08352b14423b2 source_ref=b952f8c0f670efda761b03e342b67367021c2ed6 role=util -->
## `def render(self, task): # type: ignore[no-untyped-def]`

Renders an empty string for indeterminate tasks, delegates to BarColumn for determinate tasks.
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:_OverallOnlyMofN fingerprint=58f9db3e4a84b1b7f35702ae67cfa05ff79e119d01c584588483109d88aa79cf body_fp=ceae2c75e0ba2a15ce1662f7a053cb2e494ee423184f9df1696f063321d9c93b source_ref=b952f8c0f670efda761b03e342b67367021c2ed6 role=util -->
## `class _OverallOnlyMofN(MofNCompleteColumn)`

Custom Rich column that renders M/N completion counts only for determinate tasks.

- Returns empty string for indeterminate tasks (task.total is None) to avoid showing meaningless "0/?" text
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:_OverallOnlyMofN.render fingerprint=f5dd789c2297600a905c4625c9c7ad2779b586f0cc7b44c6921d25cd064d0c09 body_fp=f284b361282feb36dfcf9d33d84ba95e48129915063df87f94b9513b1b56e627 source_ref=b952f8c0f670efda761b03e342b67367021c2ed6 role=util -->
## `def render(self, task): # type: ignore[no-untyped-def]`

Returns empty string for indeterminate tasks, otherwise delegates to MofNCompleteColumn.render.
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:_BottomBarProgress fingerprint=fbbcb76a44b1281dc7988c76a8d15448fae2d2f67968f039e860318eb9cda092 body_fp=5b0187505bc8016efe1934f5a659b28ea3e48c4f526fd1af70cea7fd1b6abce8 source_ref=5d5181cfe117f8d9faaf106bc52b54cb076eec58 role=util -->
## `class _BottomBarProgress(Progress)`

Extends Rich Progress to render the overall progress bar at bottom instead of top.

- Separates indeterminate file tasks (spinners) from determinate overall tasks (progress bars)
- Adds blank line separator between file list and overall bar when both are present
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:_BottomBarProgress.get_renderables fingerprint=4fd7d2f1f8d4f8593abefd7d25ffdeadb8b23cfaf1b1014648f164979bb08126 body_fp=de43b781caa87c41e5e025fcbbb3dbd5410d03c3b13af6d035218f8a5d63b1b8 source_ref=5d5181cfe117f8d9faaf106bc52b54cb076eec58 role=io -->
## `def get_renderables(self): # type: ignore[no-untyped-def]`

Renders _BottomBarProgress tasks with indeterminate file tasks first, then a separator, then determinate overall tasks last.

- Yields file tasks (total=None) before overall tasks (total is not None)
- Inserts blank Text separator only when both task types exist
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:Verbosity fingerprint=68167be5fddb8748e7165d3e1141f0c0c352b1dcef0f7a2e6430f8fd2efa74be body_fp=6f2ead4a99a5c5380019c21e082911347fb3ba898f6b71910554ea05ea41e742 source_ref=28f57b77c1af9ed66d987b41f89a42b11a006e0e role=cli-interface -->
## `class Verbosity(IntEnum)`

Defines integer enum levels for controlling Reporter output verbosity.

- `MUTE`: No output except errors
- `MEDIUM`: Standard info, success, and warning messages 
- `VERBOSE`: All messages plus detailed progress information
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:Reporter fingerprint=58f465091a581227e152c3de33154e238659a16640df7d728384785a40fab785 body_fp=ed3fb0e66f734aa7f00df0416700f867f004b188e56f63167012e13b03fa734a source_ref=58bb4ba240999c95abf285c660d76632710fef41 role=api -->
## `class Reporter`

Verbosity-gated console wrapper for CLI output with Rich formatting and progress tracking.

- `verbosity`: Controls which messages are displayed based on level
- `console`: Rich Console instance for stdout formatted output
- `err_console`: Separate stderr Console; `error()` routes here unconditionally regardless of verbosity
- `info()`, `detail()`: Print messages at MEDIUM/VERBOSE levels respectively
- `success()`, `warn()`, `error()`: Print styled status messages with icons
- `status()`: Returns context manager for spinner during operations
- `elapsed()`: Returns formatted wall-clock time since Reporter creation
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:Reporter.__init__ fingerprint=3e8630975130be40881601ab19ac933adaf54c9c9c013ae93791bb9b538cbe33 body_fp=59677c0ae26b86a12ede0cf7ddd7f606e105feef62b79679090e6f254c9ec36e source_ref=58bb4ba240999c95abf285c660d76632710fef41 role=domain -->
## `def __init__( self, verbosity: Verbosity = Verbosity.MEDIUM, console: Console | None = None, err_console: Console | None = None, )`

Initializes `Reporter` with verbosity level, stdout console, and stderr error console, recording creation timestamp.

- `verbosity`: Controls output filtering level, defaults to `MEDIUM`
- `console`: Rich `Console` instance for stdout; creates new one if `None`
- `err_console`: Rich `Console` instance for stderr; creates a `stderr=True` console if `None`
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:Reporter.info fingerprint=c360aff5e763c039038842e46cffcdf806016693b8a32a9024ba31ed85535328 body_fp=b4d61e382e2430a339388c0de420021c1ccadf1612b616ebbc98325f99bacfdb source_ref=28f57b77c1af9ed66d987b41f89a42b11a006e0e role=cli-interface -->
## `def info(self, msg: str) -> None`

Reporter method that prints informational messages if verbosity is MEDIUM or higher.
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:Reporter.detail fingerprint=ac606f27fc31292a6bb92bfb6309ad7ae4085a8a3eb6b93f04537a3b5bea9d96 body_fp=af790e802c4d11bb6b6dc9177bfb502cfa99f42b90ae3bea1b059a785c3139e5 source_ref=28f57b77c1af9ed66d987b41f89a42b11a006e0e role=cli-interface -->
## `def detail(self, msg: str) -> None`

Reporter prints a detailed message to console only when verbosity is VERBOSE or higher.
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:Reporter.success fingerprint=0ba3187d9ed4ea88e566b86760233ab296a70d00fc5649524dd22ade54779161 body_fp=8e2bde4816c108168638211411504e96308c46dbd3ae3813befbdcc5a700c3e4 source_ref=28f57b77c1af9ed66d987b41f89a42b11a006e0e role=cli-interface -->
## `def success(self, msg: str) -> None`

Prints a success message with green checkmark prefix to Reporter console if verbosity is MEDIUM or higher.
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:Reporter.warn fingerprint=2fe62f1d72c6acf6e6770afee5f9b3964fd5fc4d5bff48f9eab88d0a5e088e3a body_fp=c1c4754b51e6e1ac7c9dd3c507e580aadfe9804f5e733ef732fb72a7e6d70665 source_ref=28f57b77c1af9ed66d987b41f89a42b11a006e0e role=cli-interface -->
## `def warn(self, msg: str) -> None: # Warnings still suppressed in MUTE — only errors are unconditional.`

Prints a warning message to the Reporter console with yellow formatting if verbosity is MEDIUM or higher.
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:Reporter.error fingerprint=4e62ed6871c5808b410086267accbfc1df2a3c10e68abd30c445d854d826cefc body_fp=557390f8dd925eefa57c137d0bf1cf4d03dc85a36356c418c518f6be3903a726 source_ref=58bb4ba240999c95abf285c660d76632710fef41 role=util -->
## `def error(self, msg: str) -> None: # Unconditional (even in MUTE) and routed to stderr: error text must # survive stdout being consumed, piped, or discarded by a wrapper.`

Prints an error message to `Reporter`'s `err_console` (stderr) with red formatting, bypassing verbosity checks.
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:Reporter.status fingerprint=1ce7a4b2274ea11bda01d7bafb2195d03be906e09dc394540a996384bb481c77 body_fp=a1f501a2245464350e57957029227e87afad1a32307c46aabfb1a35eeef9bd27 source_ref=28f57b77c1af9ed66d987b41f89a42b11a006e0e role=cli-interface -->
## `def status(self, msg: str) -> AbstractContextManager[Any]`

Returns a context manager that displays a transient spinner with the given message during execution if Reporter verbosity is MEDIUM or higher.
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:Reporter.elapsed fingerprint=36090c883265c26b545bd9e37f5a46b55d6b46b76e83bedb1e7013e812e21919 body_fp=e9dc273bd324e066e8b6639ee1d9ecf9db2d19886368742c60490d95c4982978 source_ref=28f57b77c1af9ed66d987b41f89a42b11a006e0e role=cli-interface -->
## `def elapsed(self) -> str`

Returns human-readable wall-clock elapsed time since Reporter creation as "took X.XXs" string.
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:Reporter.start_progress fingerprint=a71b5d1c595a24d65267bee23143bc679a28d76569344578c49e6d107dc67279 body_fp=116b15e85a2786ddb7cefa24b29d89ab7c3c9620772156b9da8f2f4e50e4789b source_ref=28f57b77c1af9ed66d987b41f89a42b11a006e0e role=cli-interface -->
## `def start_progress(self, total: int, label: str) -> ProgressHandle`

Creates and returns a `ProgressHandle` context manager for tracking progress across multiple files.

- `total`: number of files to process
- `label`: description text shown in the progress bar
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:_NullContext fingerprint=83551b487c19ee10276faa46f53cc5f87b4d0223fa118d136b8a9c2fae376504 body_fp=8e597402fe36c6b634d56a933a0706617017d7be99fe3fe743ea39325e79ab01 source_ref=28f57b77c1af9ed66d987b41f89a42b11a006e0e role=cli-interface -->
## `class _NullContext`

No-op context manager that does nothing on enter and exit.
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:_NullContext.__enter__ fingerprint=9f210cb9718c0e2ccf1afd3e1a8f2d55beb6c6390abbe06ed35fdd33a7172f7f body_fp=8acd190ea9e3c07f717b385c626cda2c4cd8b5c9081ada41994b0cb5cd27881b source_ref=28f57b77c1af9ed66d987b41f89a42b11a006e0e role=cli-interface -->
## `def __enter__(self) -> _NullContext`

Returns the _NullContext instance itself to satisfy the context manager protocol.
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:_NullContext.__exit__ fingerprint=9f730a1a70a6144b0dc8da4942d9093cd268d625eafac5188775d0d6b8b25f08 body_fp=6341bc94cbf786d5e0a89ac2eca25e8767ff6ed424ae8edf2f4dd16b84b39752 source_ref=28f57b77c1af9ed66d987b41f89a42b11a006e0e role=cli-interface -->
## `def __exit__(self, *exc: Any) -> None`

Implements context manager exit protocol for _NullContext, returning None to allow any exceptions to propagate.
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:ProgressHandle fingerprint=3541aef8bc1224001d54815593778ad51464f3ff74f3388d3a36cec871c6d1d2 body_fp=7475557b3c21da981829585904f853d7da9b2e2fd03986420f9dff3fce18afc1 source_ref=4c23c22ea99f201078bf3db965430f378e9b9521 role=io -->
## `class ProgressHandle`

Context manager providing thread-safe live progress display for parallel file processing operations.

- Uses Rich to render an overall progress bar pinned to bottom with ephemeral per-file spinner lines above
- Thread-safe via internal lock protecting file task map from concurrent access
- Falls back to plain text output when not attached to terminal or in MUTE mode
- `start_file()` adds spinner line for in-flight file, with optional cascade marker
- `finish_file()` removes spinner, prints permanent completion line with optional cost/token stats
- `skip_file()` removes spinner and prints skip reason
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:ProgressHandle.__init__ fingerprint=d99731260f64d86081d126201fcdf50470ba4af00456087d7bb3b543d30643b9 body_fp=2f98fdef82bb2a36cbd8b8f78274754552cb2e74cb161d2a5f895d9273cee005 source_ref=9e8839433bf791dcd4d8c0b22356111cbefb404b role=model -->
## `def __init__(self, reporter: Reporter, total: int, label: str)`

Initializes ProgressHandle with reporter, file count, and progress label, setting up internal state for progress tracking.

- `total`: number of files to process
- `label`: display text for the overall progress bar
- `_cascade_files`: tracks files pulled in by symbol references rather than direct changes
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:ProgressHandle.__enter__ fingerprint=a9c264073b53093f3660c6e538c2e182c13dc246090fff335152bb2ddd04cdbc body_fp=e2e2403d202b495b87bc439d8cbe57630b64a10e671d5c4046e61727923faa09 source_ref=5d5181cfe117f8d9faaf106bc52b54cb076eec58 role=orchestration -->
## `def __enter__(self) -> ProgressHandle: # Only drive a live render when attached to a real terminal. In a pipe, # a redirected file, or any non-interactive shell, Rich's Live region # writes cursor-control escapes that corrupt the output and can clobber # the user's prompt on exit. There we fall back to plain printed lines # (the `_progress is None` paths in start_file/finish_file/skip_file).`

Initializes ProgressHandle's live progress display for terminal output with verbosity checks.

- Only creates Rich progress UI when attached to terminal with MEDIUM+ verbosity and total > 0
- Falls back to plain print mode for pipes/redirected output to avoid cursor escape corruption
- Sets up bottom-pinned overall progress bar and prepares for per-file spinner tasks
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:ProgressHandle.__exit__ fingerprint=68c9ab8452f2c2ea52662b54d85b27889c2c44f43099fbc03ef619f5215b6bd2 body_fp=1d27eff4051071adf58f391dde4133bb8d0d8a897685c7c251adab56314d4682 source_ref=3ba652d6105715f40601b888262fe8cfd75296ee role=io -->
## `def __exit__( self, exc_type: type[BaseException] | None, exc: BaseException | None, tb: TracebackType | None, ) -> None`

ProgressHandle.__exit__ cleans up the Rich progress display and ensures the console cursor remains visible.

- Removes all lingering per-file spinner tasks before teardown
- Forces cursor visibility to prevent shell prompt issues after interruption
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:ProgressHandle._print fingerprint=0587173aa56c0bd7479119eebcdf7b3056cc2980f27405895f6a4532541fd28f body_fp=1a46c1beac3087c62d174e7c2f4dd9bc5fc84c5c2d1197db5a2ee71cf56c5aa2 source_ref=28f57b77c1af9ed66d987b41f89a42b11a006e0e role=cli-interface -->
## `def _print(self, line: str) -> None: # Route through the live Progress's console so output lands above the # live region instead of fighting with it.`

Prints a line through the active progress bar's console if available, otherwise through ProgressHandle's reporter console.
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:ProgressHandle.start_file fingerprint=0850eaeb3aed5197e9de71ca66a3d52ffaabec1cc7ce550633cc1b4d8806d91b body_fp=a7192d0bafbcdce340ad250cfded8602f925fd82a744bfb9523c6072468ed29f source_ref=4c23c22ea99f201078bf3db965430f378e9b9521 role=api -->
## `def start_file(self, rel_path: str, *, cascade: bool = False) -> None: # Cascade files (pulled in because they reference a directly-changed # symbol, not because their own source drifted) get a marker so the # operator can see why N files sync when only a few drifted.`

Initiates progress tracking for a file, adding a spinner line to the live display if progress is enabled.

- `cascade`: marks the file as cascade-pulled (referenced by a changed symbol) for visual distinction
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:ProgressHandle._end_file_task fingerprint=37c5419b2c3ecaad84462bc64b85a5915fa67af6391256147462d97c3ccac616 body_fp=1813084feb2622edeb142635c913abe81319beff921e8df351176226e614419b source_ref=73579df29bd5d7b8d08ffd3baa92f5bf60385325 role=util -->
## `def _end_file_task(self, rel_path: str) -> None`

ProgressHandle._end_file_task removes a file's spinner task and advances the overall progress bar.

- Synchronizes access to shared task state via lock
- Advances overall progress counter regardless of whether file task existed
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:ProgressHandle.finish_file fingerprint=1ccf311e081ba7a3d7ccac53323295880522bbf65a504f12909bae2411b2b68b body_fp=17f46893295746080a2a099dec04cff525419dd7c891a3954c60c25e2ce4cb0b source_ref=9e8839433bf791dcd4d8c0b22356111cbefb404b role=io -->
## `def finish_file( self, rel_path: str, *, cost_usd: float | None = None, symbols: int | None = None, tokens_in: int | None = None, tokens_out: int | None = None, cache_read: int | None = None, cache_write: int | None = None, ) -> None`

Marks a file as completed in ProgressHandle, removing its spinner task and printing completion message with optional metrics.

- `cost_usd`: USD cost to include in summary line
- `symbols`: Symbol count to include in summary line  
- `tokens_in`/`tokens_out`: Token counts shown in verbose detail line
- `cache_read`/`cache_write`: Cache hit/miss counts shown in verbose detail line
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:ProgressHandle.skip_file fingerprint=285fae9be169fbf189fddfa16ab948599b58c4abf2b2a9ba3653e4d19f1a1a36 body_fp=b68384bcc565878d8edae98a8597a5ca245e8d94da82a761bb2ba0669bcb20a9 source_ref=9e8839433bf791dcd4d8c0b22356111cbefb404b role=io -->
## `def skip_file(self, rel_path: str, reason: str) -> None`

Marks a file as skipped in ProgressHandle, removing its spinner and printing a skip notice.

- `reason`: descriptive text explaining why the file was skipped
<!-- trie:end -->