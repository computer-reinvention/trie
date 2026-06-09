---
trie_version: 0.1.5
source: trie/reporter.py
file_fingerprint: 7984f26bb818a3e310c930b90450211dc2e3cc828dd8edde6a9180ddd0b29008
last_synced_at: '2026-06-07T03:56:58Z'
defines:
- kind: module
  qualified_name: trie/reporter:__module__
  lines: 1-254
- kind: class
  qualified_name: trie/reporter:_OverallOnlyBar
  lines: 32-36
- kind: method
  qualified_name: trie/reporter:_OverallOnlyBar.render
  lines: 33-36
- kind: class
  qualified_name: trie/reporter:_OverallOnlyMofN
  lines: 39-43
- kind: method
  qualified_name: trie/reporter:_OverallOnlyMofN.render
  lines: 40-43
- kind: class
  qualified_name: trie/reporter:Verbosity
  lines: 46-49
- kind: class
  qualified_name: trie/reporter:Reporter
  lines: 52-97
- kind: method
  qualified_name: trie/reporter:Reporter.__init__
  lines: 60-63
- kind: method
  qualified_name: trie/reporter:Reporter.info
  lines: 65-67
- kind: method
  qualified_name: trie/reporter:Reporter.detail
  lines: 69-71
- kind: method
  qualified_name: trie/reporter:Reporter.success
  lines: 73-75
- kind: method
  qualified_name: trie/reporter:Reporter.warn
  lines: 77-80
- kind: method
  qualified_name: trie/reporter:Reporter.error
  lines: 82-83
- kind: method
  qualified_name: trie/reporter:Reporter.status
  lines: 85-89
- kind: method
  qualified_name: trie/reporter:Reporter.elapsed
  lines: 91-94
- kind: method
  qualified_name: trie/reporter:Reporter.start_progress
  lines: 96-97
- kind: class
  qualified_name: trie/reporter:_NullContext
  lines: 100-105
- kind: method
  qualified_name: trie/reporter:_NullContext.__enter__
  lines: 101-102
- kind: method
  qualified_name: trie/reporter:_NullContext.__exit__
  lines: 104-105
- kind: class
  qualified_name: trie/reporter:ProgressHandle
  lines: 108-253
- kind: method
  qualified_name: trie/reporter:ProgressHandle.__init__
  lines: 127-134
- kind: method
  qualified_name: trie/reporter:ProgressHandle.__enter__
  lines: 136-160
- kind: method
  qualified_name: trie/reporter:ProgressHandle.__exit__
  lines: 162-184
- kind: method
  qualified_name: trie/reporter:ProgressHandle._print
  lines: 186-192
- kind: method
  qualified_name: trie/reporter:ProgressHandle.start_file
  lines: 194-205
- kind: method
  qualified_name: trie/reporter:ProgressHandle._end_file_task
  lines: 207-215
- kind: method
  qualified_name: trie/reporter:ProgressHandle.finish_file
  lines: 217-248
- kind: method
  qualified_name: trie/reporter:ProgressHandle.skip_file
  lines: 250-253
incoming_refs: 17
outgoing_refs: 0
---
<!-- trie:section symbol=trie/reporter:__module__ fingerprint=9ab13fd9b838c6b87fb62b143ba0330db33c452a4409281be3f3ebc0c84d440b body_fp=37df5d1ba79a59a9b669823577300a1026d9e66b729f96885fac6f36a7ac5234 source_ref=6577d244da82eb536e12f7501ed4b0e6350a4b25 role=io -->
Provides console reporting infrastructure with verbosity controls and Rich-based progress tracking.

- Requires Rich library for terminal output
- `Reporter` class handles verbosity-gated console messages and status displays
- `ProgressHandle` implements uv-style parallel file processing progress with overall bar and per-file spinners
- `Verbosity` enum defines three output levels: MUTE, MEDIUM, VERBOSE
- Custom Rich column classes prevent progress bars on spinner-only tasks
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:_OverallOnlyBar fingerprint=58f9db3e4a84b1b7f35702ae67cfa05ff79e119d01c584588483109d88aa79cf body_fp=4bf55886024d7ea526bdd9d452e92d3f6eb259b7cc0550249f9d7c6d1932d247 source_ref=b952f8c0f670efda761b03e342b67367021c2ed6 role=util -->
Renders a progress bar only for determinate tasks, hiding bars from indeterminate spinner tasks.
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:_OverallOnlyBar.render fingerprint=f5dd789c2297600a905c4625c9c7ad2779b586f0cc7b44c6921d25cd064d0c09 body_fp=03dfe02dd7c8f75c9662c6e3285cd64012cc6026925f2e062ed5d997c54e9496 source_ref=b952f8c0f670efda761b03e342b67367021c2ed6 role=util -->
Renders an empty string for indeterminate tasks, delegates to BarColumn for determinate tasks.
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:_OverallOnlyMofN fingerprint=58f9db3e4a84b1b7f35702ae67cfa05ff79e119d01c584588483109d88aa79cf body_fp=d067745b128d998c5fbd667c11cd0857e5f83e60256d1d1e8016e6e3158f7dd5 source_ref=b952f8c0f670efda761b03e342b67367021c2ed6 role=util -->
Custom Rich column that renders M/N completion counts only for determinate tasks.

- Returns empty string for indeterminate tasks (task.total is None) to avoid showing meaningless "0/?" text
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:_OverallOnlyMofN.render fingerprint=f5dd789c2297600a905c4625c9c7ad2779b586f0cc7b44c6921d25cd064d0c09 body_fp=4ad671809db549ccac4f4e8444810fa9872cf10baf1b7ec6436691a8b7528a86 source_ref=b952f8c0f670efda761b03e342b67367021c2ed6 role=util -->
Returns empty string for indeterminate tasks, otherwise delegates to MofNCompleteColumn.render.
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:Verbosity fingerprint=68167be5fddb8748e7165d3e1141f0c0c352b1dcef0f7a2e6430f8fd2efa74be body_fp=324af3e729efa07d0d1ece1cf916d741109f2f048d5fee6f8ce71260e850dab2 source_ref=28f57b77c1af9ed66d987b41f89a42b11a006e0e role=cli-interface -->
Defines integer enum levels for controlling Reporter output verbosity.

- `MUTE`: No output except errors
- `MEDIUM`: Standard info, success, and warning messages 
- `VERBOSE`: All messages plus detailed progress information
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:Reporter fingerprint=f2f9eb0d0db812c01986aa8de45e8112145fc59fb1d1c249d40a0b3bf10e0f6c body_fp=87bc9c4ddc03966ab4fbe502c8a28fa2b9c4af3f45599208494bf5a8906ae40f source_ref=28f57b77c1af9ed66d987b41f89a42b11a006e0e role=cli-interface -->
Verbosity-gated console wrapper for CLI output with Rich formatting and progress tracking.

- `verbosity`: Controls which messages are displayed based on level
- `console`: Rich Console instance for formatted output
- `info()`, `detail()`: Print messages at MEDIUM/VERBOSE levels respectively  
- `success()`, `warn()`, `error()`: Print styled status messages with icons
- `status()`: Returns context manager for spinner during operations
- `elapsed()`: Returns formatted wall-clock time since Reporter creation
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:Reporter.__init__ fingerprint=4cde0d3d19c674bce9d5999617edd36f6c1991fac11b08f19a6ddba17b0f59ce body_fp=198a7e0d04d274b35e0584a7e7be32a7863ca99772f85f89217392b154ef9a34 source_ref=28f57b77c1af9ed66d987b41f89a42b11a006e0e role=cli-interface -->
Initializes Reporter with verbosity level and console instance, recording creation timestamp.

- `verbosity`: Controls output filtering level, defaults to MEDIUM
- `console`: Rich Console instance, creates new one if None
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:Reporter.info fingerprint=c360aff5e763c039038842e46cffcdf806016693b8a32a9024ba31ed85535328 body_fp=85ec5108f23658acd661fdf5a95302714893d02b1139f95ab96f4513106fb725 source_ref=28f57b77c1af9ed66d987b41f89a42b11a006e0e role=cli-interface -->
Reporter method that prints informational messages if verbosity is MEDIUM or higher.
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:Reporter.detail fingerprint=ac606f27fc31292a6bb92bfb6309ad7ae4085a8a3eb6b93f04537a3b5bea9d96 body_fp=b70d365672d1d47cb4668c87411eee1cb6d01e1b9676b67b13187da3a8536ae8 source_ref=28f57b77c1af9ed66d987b41f89a42b11a006e0e role=cli-interface -->
Reporter prints a detailed message to console only when verbosity is VERBOSE or higher.
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:Reporter.success fingerprint=0ba3187d9ed4ea88e566b86760233ab296a70d00fc5649524dd22ade54779161 body_fp=ed26a16cd9b755bb1e417473c3d18c816cbb01338ca49694bf37f475e8ce1739 source_ref=28f57b77c1af9ed66d987b41f89a42b11a006e0e role=cli-interface -->
Prints a success message with green checkmark prefix to Reporter console if verbosity is MEDIUM or higher.
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:Reporter.warn fingerprint=2fe62f1d72c6acf6e6770afee5f9b3964fd5fc4d5bff48f9eab88d0a5e088e3a body_fp=468c8fb2db11ee920f4944dc83a8bb5531c04cb542af5b7ae06bb3a0c292bc31 source_ref=28f57b77c1af9ed66d987b41f89a42b11a006e0e role=cli-interface -->
Prints a warning message to the Reporter console with yellow formatting if verbosity is MEDIUM or higher.
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:Reporter.error fingerprint=ea5624fd1f2b32eb63d048435076a064359cac7a8c910f24d88533142f203feb body_fp=8934823778ebe9b35c15cc496239cc17b422b297a6150ed6656498905dd10881 source_ref=28f57b77c1af9ed66d987b41f89a42b11a006e0e role=cli-interface -->
Prints an error message to Reporter's console with red formatting, bypassing verbosity checks.
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:Reporter.status fingerprint=1ce7a4b2274ea11bda01d7bafb2195d03be906e09dc394540a996384bb481c77 body_fp=03e1b99b4e88a82ff299a74fe8152ae63a3faa12422f2c6fb700f3de55935db9 source_ref=28f57b77c1af9ed66d987b41f89a42b11a006e0e role=cli-interface -->
Returns a context manager that displays a transient spinner with the given message during execution if Reporter verbosity is MEDIUM or higher.
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:Reporter.elapsed fingerprint=36090c883265c26b545bd9e37f5a46b55d6b46b76e83bedb1e7013e812e21919 body_fp=82cdd0e0105016e2bc135e302a81388da3c5a73179f2a7adad71c3e4d556b5ef source_ref=28f57b77c1af9ed66d987b41f89a42b11a006e0e role=cli-interface -->
Returns human-readable wall-clock elapsed time since Reporter creation as "took X.XXs" string.
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:Reporter.start_progress fingerprint=a71b5d1c595a24d65267bee23143bc679a28d76569344578c49e6d107dc67279 body_fp=f9c55c5c0fbcc596c2a9eaec5c2f56f083cd81b50197ee6c50816a21acc0ebfa source_ref=28f57b77c1af9ed66d987b41f89a42b11a006e0e role=cli-interface -->
Creates and returns a `ProgressHandle` context manager for tracking progress across multiple files.

- `total`: number of files to process
- `label`: description text shown in the progress bar
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:_NullContext fingerprint=83551b487c19ee10276faa46f53cc5f87b4d0223fa118d136b8a9c2fae376504 body_fp=dd89f1288504cff24362936e3022996b985e50f857496c7824ec104dd2e18726 source_ref=28f57b77c1af9ed66d987b41f89a42b11a006e0e role=cli-interface -->
No-op context manager that does nothing on enter and exit.
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:_NullContext.__enter__ fingerprint=9f210cb9718c0e2ccf1afd3e1a8f2d55beb6c6390abbe06ed35fdd33a7172f7f body_fp=59ecb286f8001785f07338bf13a23f40020dee3f63d3ed7365d23fae08a09359 source_ref=28f57b77c1af9ed66d987b41f89a42b11a006e0e role=cli-interface -->
Returns the _NullContext instance itself to satisfy the context manager protocol.
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:_NullContext.__exit__ fingerprint=9f730a1a70a6144b0dc8da4942d9093cd268d625eafac5188775d0d6b8b25f08 body_fp=5c0b19c96fc480a1a85ce448370405955de677a65f6966eb39ec6bdb859a34f8 source_ref=28f57b77c1af9ed66d987b41f89a42b11a006e0e role=cli-interface -->
Implements context manager exit protocol for _NullContext, returning None to allow any exceptions to propagate.
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:ProgressHandle fingerprint=7c37e0354ca69800ae8d23e8ded1d6690c16bbc0d4a6deaee82a3b6d97046194 body_fp=e18a9ac739d1c194d4b4edad9c4632caa69b349e9903ff4b159c83ae759ec4cc source_ref=b952f8c0f670efda761b03e342b67367021c2ed6 role=io -->
Manages live progress display with overall progress bar and per-file spinners for parallel processing.

- Thread-safe for concurrent start_file/finish_file calls from multiple workers
- Falls back to plain text output when not in terminal or at MUTE verbosity
- Context manager that sets up Rich Progress with custom columns on enter
- Tracks individual file tasks by path to avoid conflicts in parallel execution
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:ProgressHandle.__init__ fingerprint=94f49138b10bd106f67f53cbeba4b0f27997d16f2b4301210af9612687792d65 body_fp=688baa04b3e6d27561f0730700505972145dc4a605d893412003edcea44492a3 source_ref=73579df29bd5d7b8d08ffd3baa92f5bf60385325 role=model -->
Initialize ProgressHandle with reporter, total count, and label for progress tracking.
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:ProgressHandle.__enter__ fingerprint=d6a6cf322cd20046b13d068931dd415303d4216a6d729cbecb0a31c61e2c9ea0 body_fp=0d070d6c307d0f2674d2b68121649bbdd7d656c99c74cf1fbe920e510adb3f43 source_ref=b952f8c0f670efda761b03e342b67367021c2ed6 role=util -->
Initializes Rich Progress display for ProgressHandle if terminal supports live rendering.

- Only creates live progress if verbosity is MEDIUM+, total > 0, and console is a terminal
- Falls back to plain print mode for pipes/redirected output to avoid escape sequence corruption
- Sets up overall progress bar and prepares for per-file spinner tasks
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:ProgressHandle.__exit__ fingerprint=68c9ab8452f2c2ea52662b54d85b27889c2c44f43099fbc03ef619f5215b6bd2 body_fp=151d7adf8524e04a696a0817895fbba9a38023277c086c267f53f3d32e1b9a43 source_ref=3ba652d6105715f40601b888262fe8cfd75296ee role=io -->
ProgressHandle.__exit__ cleans up the Rich progress display and ensures the console cursor remains visible.

- Removes all lingering per-file spinner tasks before teardown
- Forces cursor visibility to prevent shell prompt issues after interruption
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:ProgressHandle._print fingerprint=0587173aa56c0bd7479119eebcdf7b3056cc2980f27405895f6a4532541fd28f body_fp=5705026bf13df5de41ece1f16f648d782853f2dd6d19039d30f891775184d43a source_ref=28f57b77c1af9ed66d987b41f89a42b11a006e0e role=cli-interface -->
Prints a line through the active progress bar's console if available, otherwise through ProgressHandle's reporter console.
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:ProgressHandle.start_file fingerprint=fc544b93e10844cf41a30de33c44894d6fa43c8b5a0f0d8410b7d01e5383eded body_fp=8bc327fb9ee8b8afa0ff6f1b7272fa49f7a12b9741985d3c2effdde8f5b38ee0 source_ref=73579df29bd5d7b8d08ffd3baa92f5bf60385325 role=io -->
Creates a new spinner task for the given file path and tracks it in the in-flight file tasks map.

- Skips if file already has an active task
- Uses thread-safe locking for task map updates
- Returns early if progress display is disabled
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:ProgressHandle._end_file_task fingerprint=37c5419b2c3ecaad84462bc64b85a5915fa67af6391256147462d97c3ccac616 body_fp=933d0f1cc3e0f218ca1561fe546d35e31b90b2acf1e4659944a075d5d631ed2d source_ref=73579df29bd5d7b8d08ffd3baa92f5bf60385325 role=util -->
ProgressHandle._end_file_task removes a file's spinner task and advances the overall progress bar.

- Synchronizes access to shared task state via lock
- Advances overall progress counter regardless of whether file task existed
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:ProgressHandle.finish_file fingerprint=83f34c660a267fab6e0d02c104fa0ec753ab0e8c1f2d6e3f91586e3d3405a630 body_fp=1170c335d846dc6601f7e2c665e88b34ac2efc22accb8c7a99dfee3a4a06b859 source_ref=73579df29bd5d7b8d08ffd3baa92f5bf60385325 role=io -->
Removes per-file task and advances ProgressHandle progress bar, then prints completion status for a processed file with optional metrics.

- `cost_usd`: displays cost formatted as currency
- `symbols`: shows symbol count with "sym" suffix  
- `tokens_in`/`tokens_out`: token usage stats (verbose mode only)
- `cache_read`/`cache_write`: cache hit/miss counts (verbose mode only)
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:ProgressHandle.skip_file fingerprint=d4fd5b8e272b1712a1297c3f450cf73856853ae050991f3de0b74d981a842e86 body_fp=505c77e345ed6867f204f9c7640424e142ea8105cd96346c4ad365fb0042fb71 source_ref=73579df29bd5d7b8d08ffd3baa92f5bf60385325 role=io -->
Records a skipped file in ProgressHandle progress tracking, removing its task and printing a skip message at medium verbosity or higher.
<!-- trie:end -->