---
trie_version: 0.1.5
source: trie/reporter.py
file_fingerprint: 5f09dde7f78ebe9c4f4bd6aa94bf86456f49c99139d87fdffc586554611b4fc0
last_synced_at: '2026-06-09T10:02:49Z'
defines:
- kind: module
  qualified_name: trie/reporter:__module__
  lines: 1-293
- kind: class
  qualified_name: trie/reporter:_OverallOnlyBar
  lines: 33-37
- kind: method
  qualified_name: trie/reporter:_OverallOnlyBar.render
  lines: 34-37
- kind: class
  qualified_name: trie/reporter:_OverallOnlyMofN
  lines: 40-44
- kind: method
  qualified_name: trie/reporter:_OverallOnlyMofN.render
  lines: 41-44
- kind: class
  qualified_name: trie/reporter:_BottomBarProgress
  lines: 47-68
- kind: method
  qualified_name: trie/reporter:_BottomBarProgress.get_renderables
  lines: 58-68
- kind: class
  qualified_name: trie/reporter:Verbosity
  lines: 71-74
- kind: class
  qualified_name: trie/reporter:Reporter
  lines: 77-122
- kind: method
  qualified_name: trie/reporter:Reporter.__init__
  lines: 85-88
- kind: method
  qualified_name: trie/reporter:Reporter.info
  lines: 90-92
- kind: method
  qualified_name: trie/reporter:Reporter.detail
  lines: 94-96
- kind: method
  qualified_name: trie/reporter:Reporter.success
  lines: 98-100
- kind: method
  qualified_name: trie/reporter:Reporter.warn
  lines: 102-105
- kind: method
  qualified_name: trie/reporter:Reporter.error
  lines: 107-108
- kind: method
  qualified_name: trie/reporter:Reporter.status
  lines: 110-114
- kind: method
  qualified_name: trie/reporter:Reporter.elapsed
  lines: 116-119
- kind: method
  qualified_name: trie/reporter:Reporter.start_progress
  lines: 121-122
- kind: class
  qualified_name: trie/reporter:_NullContext
  lines: 125-130
- kind: method
  qualified_name: trie/reporter:_NullContext.__enter__
  lines: 126-127
- kind: method
  qualified_name: trie/reporter:_NullContext.__exit__
  lines: 129-130
- kind: class
  qualified_name: trie/reporter:ProgressHandle
  lines: 133-292
- kind: method
  qualified_name: trie/reporter:ProgressHandle.__init__
  lines: 152-162
- kind: method
  qualified_name: trie/reporter:ProgressHandle.__enter__
  lines: 164-188
- kind: method
  qualified_name: trie/reporter:ProgressHandle.__exit__
  lines: 190-212
- kind: method
  qualified_name: trie/reporter:ProgressHandle._print
  lines: 214-220
- kind: method
  qualified_name: trie/reporter:ProgressHandle.start_file
  lines: 222-240
- kind: method
  qualified_name: trie/reporter:ProgressHandle._end_file_task
  lines: 242-250
- kind: method
  qualified_name: trie/reporter:ProgressHandle.finish_file
  lines: 252-286
- kind: method
  qualified_name: trie/reporter:ProgressHandle.skip_file
  lines: 288-292
incoming_refs: 18
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
<!-- trie:section symbol=trie/reporter:_BottomBarProgress fingerprint=fbbcb76a44b1281dc7988c76a8d15448fae2d2f67968f039e860318eb9cda092 body_fp=97aa82401ccd690e56c5efa0ab87179d09c05983669135073c56760e63b37b57 source_ref=5d5181cfe117f8d9faaf106bc52b54cb076eec58 role=util -->
Extends Rich Progress to render the overall progress bar at bottom instead of top.

- Separates indeterminate file tasks (spinners) from determinate overall tasks (progress bars)
- Adds blank line separator between file list and overall bar when both are present
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:_BottomBarProgress.get_renderables fingerprint=4fd7d2f1f8d4f8593abefd7d25ffdeadb8b23cfaf1b1014648f164979bb08126 body_fp=b751513f1224b81973b6d5116c53113651c79d71acf43704e27e53751ef3cef6 source_ref=5d5181cfe117f8d9faaf106bc52b54cb076eec58 role=io -->
Renders _BottomBarProgress tasks with indeterminate file tasks first, then a separator, then determinate overall tasks last.

- Yields file tasks (total=None) before overall tasks (total is not None)
- Inserts blank Text separator only when both task types exist
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
<!-- trie:section symbol=trie/reporter:ProgressHandle fingerprint=3541aef8bc1224001d54815593778ad51464f3ff74f3388d3a36cec871c6d1d2 body_fp=3da3d03a9fcd5f658393056ad43bf232247c33d6f67f63f80347ae9db0c37924 source_ref=4c23c22ea99f201078bf3db965430f378e9b9521 role=io -->
Context manager providing thread-safe live progress display for parallel file processing operations.

- Uses Rich to render an overall progress bar pinned to bottom with ephemeral per-file spinner lines above
- Thread-safe via internal lock protecting file task map from concurrent access
- Falls back to plain text output when not attached to terminal or in MUTE mode
- `start_file()` adds spinner line for in-flight file, with optional cascade marker
- `finish_file()` removes spinner, prints permanent completion line with optional cost/token stats
- `skip_file()` removes spinner and prints skip reason
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:ProgressHandle.__init__ fingerprint=d99731260f64d86081d126201fcdf50470ba4af00456087d7bb3b543d30643b9 body_fp=bf620ff8e22ef43457a510a67f05db1da8a55c5f127341419311fd3b39d7c888 source_ref=9e8839433bf791dcd4d8c0b22356111cbefb404b role=model -->
Initializes ProgressHandle with reporter, file count, and progress label, setting up internal state for progress tracking.

- `total`: number of files to process
- `label`: display text for the overall progress bar
- `_cascade_files`: tracks files pulled in by symbol references rather than direct changes
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:ProgressHandle.__enter__ fingerprint=a9c264073b53093f3660c6e538c2e182c13dc246090fff335152bb2ddd04cdbc body_fp=f4edb6ae4985b93b6e6f513fb84a9be467bba7cd6a1e90fb37472ef41364648c source_ref=5d5181cfe117f8d9faaf106bc52b54cb076eec58 role=orchestration -->
Initializes ProgressHandle's live progress display for terminal output with verbosity checks.

- Only creates Rich progress UI when attached to terminal with MEDIUM+ verbosity and total > 0
- Falls back to plain print mode for pipes/redirected output to avoid cursor escape corruption
- Sets up bottom-pinned overall progress bar and prepares for per-file spinner tasks
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:ProgressHandle.__exit__ fingerprint=68c9ab8452f2c2ea52662b54d85b27889c2c44f43099fbc03ef619f5215b6bd2 body_fp=151d7adf8524e04a696a0817895fbba9a38023277c086c267f53f3d32e1b9a43 source_ref=3ba652d6105715f40601b888262fe8cfd75296ee role=io -->
ProgressHandle.__exit__ cleans up the Rich progress display and ensures the console cursor remains visible.

- Removes all lingering per-file spinner tasks before teardown
- Forces cursor visibility to prevent shell prompt issues after interruption
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:ProgressHandle._print fingerprint=0587173aa56c0bd7479119eebcdf7b3056cc2980f27405895f6a4532541fd28f body_fp=5705026bf13df5de41ece1f16f648d782853f2dd6d19039d30f891775184d43a source_ref=28f57b77c1af9ed66d987b41f89a42b11a006e0e role=cli-interface -->
Prints a line through the active progress bar's console if available, otherwise through ProgressHandle's reporter console.
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:ProgressHandle.start_file fingerprint=0850eaeb3aed5197e9de71ca66a3d52ffaabec1cc7ce550633cc1b4d8806d91b body_fp=fcaa2d7dff3dffa3fcaf515d5cc1362aa30ec27426a5d2f367d18ecb9dcb6496 source_ref=4c23c22ea99f201078bf3db965430f378e9b9521 role=api -->
Initiates progress tracking for a file, adding a spinner line to the live display if progress is enabled.

- `cascade`: marks the file as cascade-pulled (referenced by a changed symbol) for visual distinction
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:ProgressHandle._end_file_task fingerprint=37c5419b2c3ecaad84462bc64b85a5915fa67af6391256147462d97c3ccac616 body_fp=933d0f1cc3e0f218ca1561fe546d35e31b90b2acf1e4659944a075d5d631ed2d source_ref=73579df29bd5d7b8d08ffd3baa92f5bf60385325 role=util -->
ProgressHandle._end_file_task removes a file's spinner task and advances the overall progress bar.

- Synchronizes access to shared task state via lock
- Advances overall progress counter regardless of whether file task existed
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:ProgressHandle.finish_file fingerprint=1ccf311e081ba7a3d7ccac53323295880522bbf65a504f12909bae2411b2b68b body_fp=ebb5af160e911418ba6bba3b63b7d125fce9ec01e34b234c38b1bcc5aa2a20f9 source_ref=9e8839433bf791dcd4d8c0b22356111cbefb404b role=io -->
Marks a file as completed in ProgressHandle, removing its spinner task and printing completion message with optional metrics.

- `cost_usd`: USD cost to include in summary line
- `symbols`: Symbol count to include in summary line  
- `tokens_in`/`tokens_out`: Token counts shown in verbose detail line
- `cache_read`/`cache_write`: Cache hit/miss counts shown in verbose detail line
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:ProgressHandle.skip_file fingerprint=285fae9be169fbf189fddfa16ab948599b58c4abf2b2a9ba3653e4d19f1a1a36 body_fp=d1c31b6b4a1ff9c6b86b8d5a095c1e9bbc8bbff37a8d5d344dfcbdf8a1ef0239 source_ref=9e8839433bf791dcd4d8c0b22356111cbefb404b role=io -->
Marks a file as skipped in ProgressHandle, removing its spinner and printing a skip notice.

- `reason`: descriptive text explaining why the file was skipped
<!-- trie:end -->