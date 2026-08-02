---
trie_version: 0.3.0
source: tests/test_models_retry.py
file_fingerprint: d998000650aa0be2cec28cc8d410d899e861fe26a99bb82d95ec17f7dca7c4fb
last_synced_at: '2026-08-01T01:51:57Z'
description: Retry-on-rate-limit behaviour of `AnthropicClient`.
defines:
- kind: module
  qualified_name: tests/test_models_retry:__module__
  lines: 1-380
- kind: function
  qualified_name: tests/test_models_retry:_fake_response
  lines: 42-48
  signature: 'def _fake_response(status: int, *, retry_after: str | None = None) -> httpx.Response'
- kind: function
  qualified_name: tests/test_models_retry:_rate_limit
  lines: 51-56
  signature: 'def _rate_limit(retry_after: str | None = None) -> RateLimitError'
- kind: function
  qualified_name: tests/test_models_retry:_overloaded
  lines: 59-64
  signature: def _overloaded() -> InternalServerError
- kind: function
  qualified_name: tests/test_models_retry:_auth_error
  lines: 67-72
  signature: def _auth_error() -> AuthenticationError
- kind: class
  qualified_name: tests/test_models_retry:_Recorder
  lines: 76-82
  signature: class _Recorder
- kind: method
  qualified_name: tests/test_models_retry:_Recorder.sleep
  lines: 81-82
  signature: 'def sleep(self, seconds: float) -> None'
- kind: function
  qualified_name: tests/test_models_retry:_frozen_rng
  lines: 85-86
  signature: 'def _frozen_rng(seed: int = 0) -> random.Random'
- kind: function
  qualified_name: tests/test_models_retry:test_is_retryable_picks_up_rate_limit_and_5xx_and_timeout
  lines: 92-95
  signature: def test_is_retryable_picks_up_rate_limit_and_5xx_and_timeout()
- kind: function
  qualified_name: tests/test_models_retry:test_is_retryable_picks_up_connection_errors
  lines: 98-102
  signature: 'def test_is_retryable_picks_up_connection_errors(): # Transient network failures (DNS lookup failure, connection refused) surface # as APIConnectionError and must be retried, not crash the whole sync.'
- kind: function
  qualified_name: tests/test_models_retry:test_is_retryable_rejects_auth_and_other_4xx
  lines: 105-107
  signature: def test_is_retryable_rejects_auth_and_other_4xx()
- kind: function
  qualified_name: tests/test_models_retry:test_is_retryable_unwraps_pydantic_ai_model_api_error
  lines: 110-128
  signature: def test_is_retryable_unwraps_pydantic_ai_model_api_error()
- kind: function
  qualified_name: tests/test_models_retry:test_per_thread_models_are_distinct_and_reused
  lines: 131-160
  signature: def test_per_thread_models_are_distinct_and_reused()
- kind: function
  qualified_name: tests/test_models_retry:test_retry_after_reads_header_when_present
  lines: 163-165
  signature: def test_retry_after_reads_header_when_present()
- kind: function
  qualified_name: tests/test_models_retry:test_retry_after_none_when_header_missing_or_unparseable
  lines: 168-170
  signature: def test_retry_after_none_when_header_missing_or_unparseable()
- kind: function
  qualified_name: tests/test_models_retry:test_backoff_delay_within_cap
  lines: 173-181
  signature: def test_backoff_delay_within_cap()
- kind: function
  qualified_name: tests/test_models_retry:test_run_with_retry_honours_retry_after_exactly
  lines: 187-205
  signature: def test_run_with_retry_honours_retry_after_exactly()
- kind: function
  qualified_name: tests/test_models_retry:test_run_with_retry_caps_retry_after
  lines: 208-225
  signature: def test_run_with_retry_caps_retry_after()
- kind: function
  qualified_name: tests/test_models_retry:test_run_with_retry_uses_backoff_when_no_retry_after
  lines: 228-244
  signature: def test_run_with_retry_uses_backoff_when_no_retry_after()
- kind: function
  qualified_name: tests/test_models_retry:test_run_with_retry_backs_off_on_overloaded
  lines: 247-262
  signature: def test_run_with_retry_backs_off_on_overloaded()
- kind: function
  qualified_name: tests/test_models_retry:test_run_with_retry_gives_up_after_max_retries
  lines: 265-277
  signature: def test_run_with_retry_gives_up_after_max_retries()
- kind: function
  qualified_name: tests/test_models_retry:test_run_with_retry_propagates_non_retryable_immediately
  lines: 280-291
  signature: def test_run_with_retry_propagates_non_retryable_immediately()
- kind: function
  qualified_name: tests/test_models_retry:test_count_tokens_retries_on_rate_limit
  lines: 297-309
  signature: def test_count_tokens_retries_on_rate_limit()
- kind: function
  qualified_name: tests/test_models_retry:test_trie_client_disables_sdk_internal_retries
  lines: 312-327
  signature: 'def test_trie_client_disables_sdk_internal_retries(monkeypatch: pytest.MonkeyPatch)'
- kind: function
  qualified_name: tests/test_models_retry:test_retry_total_seconds_bounds_the_loop
  lines: 330-357
  signature: def test_retry_total_seconds_bounds_the_loop(monkeypatch)
- kind: function
  qualified_name: tests/test_models_retry:test_retry_total_seconds_zero_is_unbounded
  lines: 360-379
  signature: def test_retry_total_seconds_zero_is_unbounded(monkeypatch)
incoming_refs: 0
outgoing_refs: 31
---
<!-- trie:section symbol=tests/test_models_retry:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=6230e0b6dac96c666f4c643a238e8932016fce96586b9091c4f78ad67994b7c1 source_ref=85a5a52974f5f74ebaec7d5758ff3fb98966a251 role=test-infrastructure -->
Tests retry behavior of `AnthropicClient` against rate limits, server errors, timeouts, and non-retryable exceptions.

- Tests proper handling of `retry-after` headers vs exponential backoff
- Verifies retry loop applies to both `messages.create` and `messages.count_tokens`
- Ensures SDK internal retries are disabled to avoid double-retry
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models_retry:_fake_response fingerprint=fe8fd6035dcb46c04e29a488aa45d382ac2b3da33fbeaf3f74f28d1db959576b body_fp=4eee1fba0f8b5dfacb8dfa2a6cb7277c8570925b942e24f33f845b68165f7220 source_ref=85a5a52974f5f74ebaec7d5758ff3fb98966a251 role=test-infrastructure -->
## `def _fake_response(status: int, *, retry_after: str | None = None) -> httpx.Response`

Builds an httpx.Response object with specified status and optional retry-after header for testing SDK exception handling.

- `retry_after`: When provided, sets the "retry-after" header value
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models_retry:_rate_limit fingerprint=817d1f499887aef57cd5bba15d5b0e6425ba9d6dfd19bf4589b67b7534d58c2d body_fp=8de137269a22857fbcd4635934709598638c3c1cd680c1f909636f0e36e25ce1 source_ref=85a5a52974f5f74ebaec7d5758ff3fb98966a251 role=test-infrastructure -->
## `def _rate_limit(retry_after: str | None = None) -> RateLimitError`

Creates a RateLimitError exception with 429 status and optional retry-after header for testing.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models_retry:_overloaded fingerprint=623c945b55ddebd9607ef7be5d70b96290bd820023bd75445a18f08a49b5617c body_fp=756a5c17a080ba6b48be73ff5950566cf69ec91ce862eeb0b2f3c00de81db758 source_ref=85a5a52974f5f74ebaec7d5758ff3fb98966a251 role=test-infrastructure -->
## `def _overloaded() -> InternalServerError`

Creates an InternalServerError representing a 529 overloaded server response for testing retry logic.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models_retry:_auth_error fingerprint=2107cda8409df874e0dc468d7445a1094a779ebe23afebfc673a3e4b0c232a06 body_fp=35013f237103cc2618d6d2050bdb2df3abc71f68ef6ad59b98080dc588561eca source_ref=85a5a52974f5f74ebaec7d5758ff3fb98966a251 role=test-infrastructure -->
## `def _auth_error() -> AuthenticationError`

Creates an AuthenticationError with a 401 response for testing non-retryable error handling.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models_retry:_Recorder fingerprint=826822d20981072b453816aaf9b60f912784c91a83a4ac4e87296e36785412fd body_fp=c03c093729936f7767f6822c5248f673a8300a818753ffb764005011ad41d994 source_ref=85a5a52974f5f74ebaec7d5758ff3fb98966a251 role=test-infrastructure -->
## `class _Recorder`

Records sleep durations during retry testing without actually blocking execution.

- `sleeps`: List of sleep durations passed to the `sleep` method for verification
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models_retry:_Recorder.sleep fingerprint=e45d93e687af0bc59b5bf2e3bd6e8c5c5dbf519386b2560872a90a23f43e8ef9 body_fp=0a2aa8048838dd5287407b12ed32ef82d44c417a23df29332df2d17cc4906bf1 source_ref=85a5a52974f5f74ebaec7d5758ff3fb98966a251 role=test-infrastructure -->
## `def sleep(self, seconds: float) -> None`

Records the sleep duration in `_Recorder.sleeps` list without actually blocking execution.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models_retry:_frozen_rng fingerprint=21a30f0dca12cc5a6c96c27a311a47b71773540767a177151ea8082a02589cbf body_fp=c116ea0b064d0d93b38cbd2cffa3e3dd6291e73d933a9ddf276b5accb88da817 source_ref=85a5a52974f5f74ebaec7d5758ff3fb98966a251 role=test-infrastructure -->
## `def _frozen_rng(seed: int = 0) -> random.Random`

Creates a seeded Random instance for deterministic test outcomes.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models_retry:test_is_retryable_picks_up_rate_limit_and_5xx_and_timeout fingerprint=57e8cdd19d86cc19a2e20ade35d7eec104a0e39a2510080690d734677e8027dd body_fp=06e2c170b1c99748defb36fad1522b1d27c07a627ba09e4ee3094a1e2867abd5 source_ref=642bbe46cefd8feb139704cd6fe30e494544ec76 role=test -->
## `def test_is_retryable_picks_up_rate_limit_and_5xx_and_timeout()`

Verifies that `_is_retryable` returns True for rate limit, 5xx server errors, and timeout exceptions.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models_retry:test_is_retryable_picks_up_connection_errors fingerprint=b84afa39a66ae629bd3f4b4a9ca4b6101e84fe979bae7325a8e82096f1f7affd body_fp=73d76d9c947bd337d97441b0557d91174f018ed66e54320225a0de259a791882 source_ref=642bbe46cefd8feb139704cd6fe30e494544ec76 role=test -->
## `def test_is_retryable_picks_up_connection_errors(): # Transient network failures (DNS lookup failure, connection refused) surface # as APIConnectionError and must be retried, not crash the whole sync.`

Tests that `_is_retryable` correctly identifies `APIConnectionError` as retryable.

- Creates an `APIConnectionError` representing transient network failures like DNS lookup or connection refused
- Verifies the error is classified as retryable to prevent sync crashes
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models_retry:test_is_retryable_rejects_auth_and_other_4xx fingerprint=ad1733d7e18cc28b638ccebae3dbd460280fc5547172d8d6b73456101792f9ea body_fp=cce2bd9daa764e81c900f6c2ed96694c643065fb0a881c2daac91f7bcd7d0e16 source_ref=642bbe46cefd8feb139704cd6fe30e494544ec76 role=test -->
## `def test_is_retryable_rejects_auth_and_other_4xx()`

Verifies `_is_retryable` returns False for authentication errors and non-API exceptions.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models_retry:test_is_retryable_unwraps_pydantic_ai_model_api_error fingerprint=3d88bbfec2cfe3c0211f9ac1e50594a8126e088e50452d10f07d0950f39a9bcc body_fp=f3aabd211bffb2a950f9c92eaffeed1caedbc3aed62632704dc242bafb6bd35f source_ref=642bbe46cefd8feb139704cd6fe30e494544ec76 role=test -->
## `def test_is_retryable_unwraps_pydantic_ai_model_api_error()`

Tests that `_is_retryable` correctly handles pydantic-ai's ModelAPIError wrappers around retryable exceptions.

- Tests message-based matching for connection errors
- Tests __cause__ chain unwrapping for wrapped anthropic exceptions
- Verifies non-retryable errors remain non-retryable when wrapped
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models_retry:test_per_thread_models_are_distinct_and_reused fingerprint=8d223b1bbd94023b408c389bf435b8f82b4f09420d56812fd38db9b00df4e288 body_fp=ae3978a00cf9ac7a6e0eb04b6051a86b2f408dc3882058a4ac2d6090aa807fc6 source_ref=642bbe46cefd8feb139704cd6fe30e494544ec76 role=test -->
## `def test_per_thread_models_are_distinct_and_reused()`

Tests that TrieClient creates distinct models per thread but reuses within threads.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models_retry:test_retry_after_reads_header_when_present fingerprint=8a962d853de085e033e2f8972799ca75d5534b32d48aca2c5962f79497c57210 body_fp=5ca6aaa4763219ea66aaaeb64eb83188d4f20c2db30a6755544bdba7c7f90241 source_ref=642bbe46cefd8feb139704cd6fe30e494544ec76 role=test -->
## `def test_retry_after_reads_header_when_present()`

Tests that `_retry_after_seconds` correctly parses numeric retry-after header values from rate limit errors.

- Verifies both integer ("3") and decimal ("0.5") string values are converted to floats
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models_retry:test_retry_after_none_when_header_missing_or_unparseable fingerprint=840924acaed456cea64cc1304e5051d92ea6b63661cce9ef689669eb57b0b949 body_fp=07aae734d41dd779d35c92689260ce795a8fdb416881d9a9b49ef839a1844a18 source_ref=642bbe46cefd8feb139704cd6fe30e494544ec76 role=test -->
## `def test_retry_after_none_when_header_missing_or_unparseable()`

Tests that `_retry_after_seconds` returns `None` when the retry-after header is missing or contains unparseable values.

- Returns `None` when `retry_after` parameter is `None`
- Returns `None` when `retry_after` contains non-numeric string
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models_retry:test_backoff_delay_within_cap fingerprint=01fcdc55abf97e3557281070b9ad43c1bcc8b05701af9f4be88ee8b3aef8fef8 body_fp=2ed04fa13fa537f2df730bf6e96c040a4bbf93166f16d25514d0abb826803db8 source_ref=642bbe46cefd8feb139704cd6fe30e494544ec76 role=test -->
## `def test_backoff_delay_within_cap()`

Tests that `_backoff_delay` respects the retry cap even when attempt count would exceed it.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models_retry:test_run_with_retry_honours_retry_after_exactly fingerprint=14003a3322d64979d8d605ba62373a1f973903240285043c6ef912db080fa0af body_fp=ecc90a4482e3cf52e904dafba48caa7f5f8ab04c3e055180e9a6cef76df9a99b source_ref=642bbe46cefd8feb139704cd6fe30e494544ec76 role=test -->
## `def test_run_with_retry_honours_retry_after_exactly()`

Verifies `_run_with_retry` respects the retry-after header value exactly without applying jitter.

- Tests that a 429 with retry-after="7" causes exactly 7.0 seconds of sleep
- Confirms the function succeeds after one retry and two total attempts
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models_retry:test_run_with_retry_caps_retry_after fingerprint=da7b5b845dc1ed536c16b052cdbc62c4a53bdcbdffb39690d9129610c14a8852 body_fp=6a2b198bf057581f317b51dfa86e8879c4088004f600a71110917489056ae891 source_ref=642bbe46cefd8feb139704cd6fe30e494544ec76 role=test -->
## `def test_run_with_retry_caps_retry_after()`

Tests that retry-after headers exceeding retry_cap_seconds are clamped to the configured maximum delay.

- Simulates malicious 9999-second retry-after header that gets clamped to 2.0 seconds
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models_retry:test_run_with_retry_uses_backoff_when_no_retry_after fingerprint=10f2bc60c406fba9d3c61e64e5ddcb970900091a2089b53dbe6780fa279acdc0 body_fp=499de6a2dfc6e54d09350cf451db64c4e18dd65d025be851cf38f7a546bd1f2d source_ref=642bbe46cefd8feb139704cd6fe30e494544ec76 role=test -->
## `def test_run_with_retry_uses_backoff_when_no_retry_after()`

Tests that `_run_with_retry` uses exponential backoff with jitter when rate limit responses lack retry-after headers.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models_retry:test_run_with_retry_backs_off_on_overloaded fingerprint=3cec4f4c645759f9a9756073727e18d70e342d25313642ed06bdaafb168d3516 body_fp=564996b10408626269e4040648842a41b6b8ee4ab8f64cc82d2f0fdf12115171 source_ref=642bbe46cefd8feb139704cd6fe30e494544ec76 role=test -->
## `def test_run_with_retry_backs_off_on_overloaded()`

Verifies that `_run_with_retry` applies exponential backoff with jitter when encountering 5xx server overload errors.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models_retry:test_run_with_retry_gives_up_after_max_retries fingerprint=c4f15661eb0102df7180752f5c2ff0bb83396f79eb0b98358af3ad2d3ae96517 body_fp=cc9898cd44f2a960d0390ec316a0fe0c4273b6664ec60ad80f728b87f29078f2 source_ref=642bbe46cefd8feb139704cd6fe30e494544ec76 role=test -->
## `def test_run_with_retry_gives_up_after_max_retries()`

Verifies _run_with_retry respects max_retries and propagates the original exception after exhausting attempts.

- Creates scenario where call always fails with rate limit
- Confirms 2 retries means 2 sleep calls (3 total attempts)
- Validates original RateLimitError propagates after limit reached
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models_retry:test_run_with_retry_propagates_non_retryable_immediately fingerprint=9503d02df17aa8a31ae1080d7f49b5535de0952085b6062231401a67680e32cb body_fp=6a95483749d889ce45cb63b13c67470d954f71772c9acb0b8731d12993362e5b source_ref=642bbe46cefd8feb139704cd6fe30e494544ec76 role=test -->
## `def test_run_with_retry_propagates_non_retryable_immediately()`

Verifies that `_run_with_retry` immediately propagates non-retryable errors without sleeping or retrying.

- Sets up a function that always raises `AuthenticationError` (non-retryable)
- Confirms the error propagates without any recorded sleep calls
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models_retry:test_count_tokens_retries_on_rate_limit fingerprint=fe50e5e6a9dd7a4d2c7beea67c571e08c7c8d43d55c786363d5329ffdd6b20ed body_fp=112db4b1210e76789a340dc821e43ed4519ed7bfad9ca38c0de287c61ff847d1 source_ref=642bbe46cefd8feb139704cd6fe30e494544ec76 role=test -->
## `def test_count_tokens_retries_on_rate_limit()`

Verifies that TrieClient.count_tokens retries on rate limit errors during token counting.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models_retry:test_trie_client_disables_sdk_internal_retries fingerprint=2e2e831e32c15451c5afcf7a3d491f67386e186895df981ca3b964c032ac8488 body_fp=a657c5eab4f1df9c433ad155763216b2c84a46d98677e2e55df35a8af07100a5 source_ref=dd3619333df2496a6de3788135dbd0285a85606c role=test -->
## `def test_trie_client_disables_sdk_internal_retries(monkeypatch: pytest.MonkeyPatch)`

Verifies that TrieClient passes `max_retries=0` to the Anthropic SDK to disable its internal retry layer.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models_retry:test_retry_total_seconds_bounds_the_loop fingerprint=ef693c670abe4792072ca3f67a7c5d38b67a2b1b49aeacacd31daa77161247a6 body_fp=99ce33f60596b22395a71943c3d47dc29fa8e3439b62566fa837dacff59c3d77 source_ref=642bbe46cefd8feb139704cd6fe30e494544ec76 role=test -->
## `def test_retry_total_seconds_bounds_the_loop(monkeypatch)`

Assert that `_run_with_retry` stops retrying once `retry_total_seconds` wall-clock budget is exceeded, regardless of remaining attempt count.

- Monkeypatches `trie.models.time.monotonic` to advance 6 s per call, budget set to 10 s; expects exactly 2 calls before `APITimeoutError` propagates.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models_retry:test_retry_total_seconds_zero_is_unbounded fingerprint=5328b52d5e0e10699af66b12676c3cbaa99efff8d938f19d7c312df902965312 body_fp=c0fa31006999d56995f89f46c97285edb19b81a4cf07e8c6760a03731348522a source_ref=642bbe46cefd8feb139704cd6fe30e494544ec76 role=test -->
## `def test_retry_total_seconds_zero_is_unbounded(monkeypatch)`

Assert that `retry_total_seconds=0.0` disables the wall-clock budget, allowing all `max_retries` attempts to complete.
<!-- trie:end -->