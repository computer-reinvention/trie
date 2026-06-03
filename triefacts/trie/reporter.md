---
trie_version: 0.1.5
source: trie/reporter.py
file_fingerprint: 32f52b2ab59ed7b633ee252ad085f9f274bf50005d2ac231d267431714c1e53e
last_synced_at: '2026-06-03T21:15:04Z'
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
<!-- trie:section symbol=trie/reporter:__module__ fingerprint=5e8b08dfe65f9f795689fb53568d42681062a72da8c7731c23dce6381ade108a body_fp=be9663af1505bc402b5492219d7b35ab77c2441cc59bc86be311b79db83c4bd6 source_ref=28f57b77c1af9ed66d987b41f89a42b11a006e0e -->
Provides console reporting infrastructure with verbosity-gated output and progress tracking.

- **Verbosity**: Three-level enum controlling output volume (MUTE/MEDIUM/VERBOSE)
- **Reporter**: Main console wrapper with info/success/error logging and status display
- **ProgressHandle**: Context manager for file-by-file progress bars with ETA and metrics
- **_NullContext**: No-op context manager for silent mode operations
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:Verbosity fingerprint=68167be5fddb8748e7165d3e1141f0c0c352b1dcef0f7a2e6430f8fd2efa74be body_fp=324af3e729efa07d0d1ece1cf916d741109f2f048d5fee6f8ce71260e850dab2 source_ref=28f57b77c1af9ed66d987b41f89a42b11a006e0e -->
Defines integer enum levels for controlling Reporter output verbosity.

- `MUTE`: No output except errors
- `MEDIUM`: Standard info, success, and warning messages 
- `VERBOSE`: All messages plus detailed progress information
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:Reporter fingerprint=f2f9eb0d0db812c01986aa8de45e8112145fc59fb1d1c249d40a0b3bf10e0f6c body_fp=87bc9c4ddc03966ab4fbe502c8a28fa2b9c4af3f45599208494bf5a8906ae40f source_ref=28f57b77c1af9ed66d987b41f89a42b11a006e0e -->
Verbosity-gated console wrapper for CLI output with Rich formatting and progress tracking.

- `verbosity`: Controls which messages are displayed based on level
- `console`: Rich Console instance for formatted output
- `info()`, `detail()`: Print messages at MEDIUM/VERBOSE levels respectively  
- `success()`, `warn()`, `error()`: Print styled status messages with icons
- `status()`: Returns context manager for spinner during operations
- `elapsed()`: Returns formatted wall-clock time since Reporter creation
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:Reporter.__init__ fingerprint=4cde0d3d19c674bce9d5999617edd36f6c1991fac11b08f19a6ddba17b0f59ce body_fp=198a7e0d04d274b35e0584a7e7be32a7863ca99772f85f89217392b154ef9a34 source_ref=28f57b77c1af9ed66d987b41f89a42b11a006e0e -->
Initializes Reporter with verbosity level and console instance, recording creation timestamp.

- `verbosity`: Controls output filtering level, defaults to MEDIUM
- `console`: Rich Console instance, creates new one if None
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:Reporter.info fingerprint=c360aff5e763c039038842e46cffcdf806016693b8a32a9024ba31ed85535328 body_fp=85ec5108f23658acd661fdf5a95302714893d02b1139f95ab96f4513106fb725 source_ref=28f57b77c1af9ed66d987b41f89a42b11a006e0e -->
Reporter method that prints informational messages if verbosity is MEDIUM or higher.
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:Reporter.detail fingerprint=ac606f27fc31292a6bb92bfb6309ad7ae4085a8a3eb6b93f04537a3b5bea9d96 body_fp=b70d365672d1d47cb4668c87411eee1cb6d01e1b9676b67b13187da3a8536ae8 source_ref=28f57b77c1af9ed66d987b41f89a42b11a006e0e -->
Reporter prints a detailed message to console only when verbosity is VERBOSE or higher.
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:Reporter.success fingerprint=0ba3187d9ed4ea88e566b86760233ab296a70d00fc5649524dd22ade54779161 body_fp=ed26a16cd9b755bb1e417473c3d18c816cbb01338ca49694bf37f475e8ce1739 source_ref=28f57b77c1af9ed66d987b41f89a42b11a006e0e -->
Prints a success message with green checkmark prefix to Reporter console if verbosity is MEDIUM or higher.
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:Reporter.warn fingerprint=2fe62f1d72c6acf6e6770afee5f9b3964fd5fc4d5bff48f9eab88d0a5e088e3a body_fp=468c8fb2db11ee920f4944dc83a8bb5531c04cb542af5b7ae06bb3a0c292bc31 source_ref=28f57b77c1af9ed66d987b41f89a42b11a006e0e -->
Prints a warning message to the Reporter console with yellow formatting if verbosity is MEDIUM or higher.
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:Reporter.error fingerprint=ea5624fd1f2b32eb63d048435076a064359cac7a8c910f24d88533142f203feb body_fp=8934823778ebe9b35c15cc496239cc17b422b297a6150ed6656498905dd10881 source_ref=28f57b77c1af9ed66d987b41f89a42b11a006e0e -->
Prints an error message to Reporter's console with red formatting, bypassing verbosity checks.
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:Reporter.status fingerprint=1ce7a4b2274ea11bda01d7bafb2195d03be906e09dc394540a996384bb481c77 body_fp=03e1b99b4e88a82ff299a74fe8152ae63a3faa12422f2c6fb700f3de55935db9 source_ref=28f57b77c1af9ed66d987b41f89a42b11a006e0e -->
Returns a context manager that displays a transient spinner with the given message during execution if Reporter verbosity is MEDIUM or higher.
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:Reporter.elapsed fingerprint=36090c883265c26b545bd9e37f5a46b55d6b46b76e83bedb1e7013e812e21919 body_fp=82cdd0e0105016e2bc135e302a81388da3c5a73179f2a7adad71c3e4d556b5ef source_ref=28f57b77c1af9ed66d987b41f89a42b11a006e0e -->
Returns human-readable wall-clock elapsed time since Reporter creation as "took X.XXs" string.
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:Reporter.start_progress fingerprint=a71b5d1c595a24d65267bee23143bc679a28d76569344578c49e6d107dc67279 body_fp=f9c55c5c0fbcc596c2a9eaec5c2f56f083cd81b50197ee6c50816a21acc0ebfa source_ref=28f57b77c1af9ed66d987b41f89a42b11a006e0e -->
Creates and returns a `ProgressHandle` context manager for tracking progress across multiple files.

- `total`: number of files to process
- `label`: description text shown in the progress bar
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:_NullContext fingerprint=83551b487c19ee10276faa46f53cc5f87b4d0223fa118d136b8a9c2fae376504 body_fp=dd89f1288504cff24362936e3022996b985e50f857496c7824ec104dd2e18726 source_ref=28f57b77c1af9ed66d987b41f89a42b11a006e0e -->
No-op context manager that does nothing on enter and exit.
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:_NullContext.__enter__ fingerprint=9f210cb9718c0e2ccf1afd3e1a8f2d55beb6c6390abbe06ed35fdd33a7172f7f body_fp=59ecb286f8001785f07338bf13a23f40020dee3f63d3ed7365d23fae08a09359 source_ref=28f57b77c1af9ed66d987b41f89a42b11a006e0e -->
Returns the _NullContext instance itself to satisfy the context manager protocol.
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:_NullContext.__exit__ fingerprint=9f730a1a70a6144b0dc8da4942d9093cd268d625eafac5188775d0d6b8b25f08 body_fp=5c0b19c96fc480a1a85ce448370405955de677a65f6966eb39ec6bdb859a34f8 source_ref=28f57b77c1af9ed66d987b41f89a42b11a006e0e -->
Implements context manager exit protocol for _NullContext, returning None to allow any exceptions to propagate.
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:ProgressHandle fingerprint=28ff21ac130486863ec732556ba4c070942c2c2e199c82b5077209f6d1112c4e body_fp=771a2cd3c14a040b3ddc48369cf5b620e54be22de80943cef047e2db8bd3f604 source_ref=28f57b77c1af9ed66d987b41f89a42b11a006e0e -->
Context manager for file-by-file progress tracking with verbosity-gated Rich progress bars.

- `start_file`: Updates progress bar description and optionally prints file start message
- `finish_file`: Advances progress and prints completion with optional cost/token metrics
- `skip_file`: Advances progress and prints skip message with reason
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:ProgressHandle.__init__ fingerprint=7db3d0385ca9d91f7d3d72a231d4bdab74ee74393f8ce2c29e6c3904c766396b body_fp=688baa04b3e6d27561f0730700505972145dc4a605d893412003edcea44492a3 source_ref=28f57b77c1af9ed66d987b41f89a42b11a006e0e -->
Initialize ProgressHandle with reporter, total count, and label for progress tracking.
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:ProgressHandle.__enter__ fingerprint=fa8f8db25bfe291e05bbcf2fae90906b02b98f66c18727e21b41b7ef3e573d8b body_fp=cbb17d98c3f6bd99dbaa0a16686fa7cbc694b7527474f4b86ed44637c713d29a source_ref=28f57b77c1af9ed66d987b41f89a42b11a006e0e -->
ProgressHandle context manager entry that initializes a Rich progress bar if verbosity is MEDIUM+ and total > 0.
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:ProgressHandle.__exit__ fingerprint=f7249b97149bb3359cf78e0141969f8be0b13fc309365f184bdfe2c0cfc6b6dd body_fp=70ca7acc2411cdc117e79b0e45d2dd1ad889bc464c38369f3e1fedd69c8a611b source_ref=28f57b77c1af9ed66d987b41f89a42b11a006e0e -->
Cleans up ProgressHandle by exiting the Rich progress display and clearing internal state.
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:ProgressHandle._print fingerprint=0587173aa56c0bd7479119eebcdf7b3056cc2980f27405895f6a4532541fd28f body_fp=5705026bf13df5de41ece1f16f648d782853f2dd6d19039d30f891775184d43a source_ref=28f57b77c1af9ed66d987b41f89a42b11a006e0e -->
Prints a line through the active progress bar's console if available, otherwise through ProgressHandle's reporter console.
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:ProgressHandle.start_file fingerprint=e1db160ef3c1e5c842d9d39ce5758c26312cc966187c314d617000236375fe8f body_fp=d56c5897ff8efc4b818c93189fde8a370ce9c84d2b8690dec48528a0409a1d6d source_ref=28f57b77c1af9ed66d987b41f89a42b11a006e0e -->
Updates ProgressHandle's active task description to show the current file being processed and optionally prints a verbose start indicator.
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:ProgressHandle.finish_file fingerprint=4afa6c0f41126ce73f145bb430e3bd99d0295aff0226d74fc3197c64c31ac1a3 body_fp=6f32a3429a684401af5097a312a278f38d49f6ce2a6d57d1aa78af24e68080ca source_ref=28f57b77c1af9ed66d987b41f89a42b11a006e0e -->
Advances ProgressHandle progress bar and prints completion status for a processed file with optional metrics.

- `cost_usd`: displays cost formatted as currency
- `symbols`: shows symbol count with "sym" suffix  
- `tokens_in`/`tokens_out`: token usage stats (verbose mode only)
- `cache_read`/`cache_write`: cache hit/miss counts (verbose mode only)
<!-- trie:end -->
<!-- trie:section symbol=trie/reporter:ProgressHandle.skip_file fingerprint=54054bdb5cf751f343914ba6c9b74a73a7fdb5f4fcd8f3108fa8322a1099b3d8 body_fp=c2fd04212361262b3fabb1171b54254197ce499aaf8343fdf573a3ac1a136423 source_ref=28f57b77c1af9ed66d987b41f89a42b11a006e0e -->
Records a skipped file in ProgressHandle progress tracking, advancing the task counter and printing a skip message at medium verbosity or higher.
<!-- trie:end -->